import streamlit as st
import pandas as pd
from pymongo import MongoClient
from css import css_tabeldata, css_datacontainer, css_pagination_controls
import datetime

def datanya_page():
    css_tabeldata()
    # client = MongoClient("mongodb://salsa_ro:readonly@localhost:27017/?authSource=admin")
    client = MongoClient("mongodb+srv://masukannamatemananda:masukanpasswordtemananda@posindo.5juwxxh.mongodb.net/")
    db = client['pos_indonesia']
    collection = db['testtransaksi']
    data = list(collection.find({}, {
        "timestamps.createdAt": 1,
        "orderId": 1,
        "status": 1,
        "user.userId": 1,
        "kantorPengirim.propinsi":1,
        "pengirim.nama": 1,
        "penerima.nama":1, 
        "barang.beratGram": 1,
        "hasilApi.tarif.totalFee":1,
        "_id": 0
    }))

    df = pd.json_normalize(data)
    if "timestamps.createdAt" in df.columns:
        df["timestamps.createdAt"] = pd.to_datetime(df["timestamps.createdAt"], errors="coerce")

    gantinamafitur = {
        "orderId": "ID Transaksi",
        "timestamps.createdAt": "Tanggal Transaksi",
        "status": "Status",
        "user.userId": "ID Pengguna",
        "kantorPengirim.propinsi": "Propinsi Pengirim",
        "pengirim.nama": "Nama Pengirim",
        "penerima.nama": "Nama Penerima", 
        "barang.beratGram": "Berat Barang",
        "hasilApi.tarif.totalFee": "Total Tarif"
    }
    df.rename(columns=gantinamafitur, inplace=True)
    
    # Filter berdasarkan tanggal
    if not df.empty:
        # Cari kolom yang berisi tanggal
        date_columns = []
        for col in df.columns:
            if any(keyword in col.lower() for keyword in ['tanggal', 'date', 'tgl', 'waktu', 'time']):
                try:
                    df[col] = pd.to_datetime(df[col], errors='coerce')
                    date_columns.append(col) 
                except:
                    pass
        
        month_names = [
            "Januari", "Februari", "Maret", "April", "Mei", "Juni",
            "Juli", "Agustus", "September", "Oktober", "November", "Desember"
        ]

        # Filter Section
        if date_columns:
            st.markdown('<div class="filter-title">Filter Data Transaksi</div>', unsafe_allow_html=True)
            
            selected_date_col = date_columns[0]
            df_available = df.dropna(subset=[selected_date_col])
            
            if not df_available.empty:
                col1, col2, col3, col4 = st.columns(4)
                
                # Get available years
                available_years = sorted(df_available[selected_date_col].dt.year.unique())
                today = datetime.date.today()
                
                # Ubah opsi default - hapus "Hari ini" dan mulai dengan "Pilih..."
                day_options = ["Pilih Tanggal...", "Hari ini"] + list(range(1, 32))
                month_options = ["Pilih Bulan...", "Hari ini"] + list(range(1, 13))
                year_options = ["Pilih Tahun...", "Hari ini"] + available_years

                with col1:
                    selected_day = st.selectbox(
                        "Pilih Tanggal:",
                        options=day_options,
                        index=0  
                    )
                with col2:
                    selected_month = st.selectbox(
                        "Pilih Bulan:",
                        options=month_options,
                        index=0,
                        format_func=lambda x: x if isinstance(x, str) else month_names[x-1]
                    )
                with col3:
                    selected_year = st.selectbox(
                        "Pilih Tahun:",
                        options=year_options,
                        index=0  # Default ke "Pilih Tahun..."
                    )
                
                with col4:
                    # Tombol untuk menampilkan data
                    st.markdown("<br>", unsafe_allow_html=True)
                    show_data = st.button("Tampilkan Data", type="primary")

                # Check if user changed any selection (untuk reset data display)
                current_selection = f"{selected_day}-{selected_month}-{selected_year}"
                if 'last_selection' not in st.session_state:
                    st.session_state.last_selection = ""
                
                # Reset display flag jika user mengubah pilihan
                if st.session_state.last_selection != current_selection:
                    if 'data_displayed' in st.session_state:
                        del st.session_state.data_displayed
                    st.session_state.last_selection = current_selection

                # Convert "Hari ini" ke nilai aktual
                actual_day = selected_day
                actual_month = selected_month
                actual_year = selected_year
                
                if selected_day == "Hari ini":
                    actual_day = today.day
                if selected_month == "Hari ini":
                    actual_month = today.month
                if selected_year == "Hari ini":
                    actual_year = today.year

                # Cek apakah user sudah memilih filter yang valid
                has_valid_selection = (
                    selected_day != "Pilih Tanggal..." and
                    selected_month != "Pilih Bulan..." and
                    selected_year != "Pilih Tahun..."
                )
                
                # Hanya tampilkan data jika user sudah memilih DAN tombol ditekan
                if has_valid_selection and show_data:
                    # Set flag bahwa data sudah ditampilkan untuk session ini
                    st.session_state.data_displayed = True
                    
                    # Apply filter dengan nilai yang sudah dikonversi
                    filtered_df = df_available.copy()
                    
                    filter_info = []
                    
                    # Filter berdasarkan tanggal
                    filtered_df = filtered_df[filtered_df[selected_date_col].dt.day == actual_day]
                    if selected_day == "Hari ini":
                        filter_info.append(f"Tanggal: {actual_day} (Hari ini)")
                    else:
                        filter_info.append(f"Tanggal: {actual_day}")
                    
                    # Filter berdasarkan bulan
                    filtered_df = filtered_df[filtered_df[selected_date_col].dt.month == actual_month]
                    if selected_month == "Hari ini":
                        filter_info.append(f"Bulan: {month_names[actual_month-1]} (Hari ini)")
                    else:
                        filter_info.append(f"Bulan: {month_names[actual_month-1]}")
                    
                    # Filter berdasarkan tahun
                    filtered_df = filtered_df[filtered_df[selected_date_col].dt.year == actual_year]
                    if selected_year == "Hari ini":
                        filter_info.append(f"Tahun: {actual_year} (Hari ini)")
                    else:
                        filter_info.append(f"Tahun: {actual_year}")

                    # Tampilkan info filter
                    st.markdown(f'''
                        <div class="info-card">
                            <strong>Filter Aktif:</strong> {' | '.join(filter_info)}<br>
                            <strong>Hasil:</strong> Menampilkan <strong>{len(filtered_df)}</strong> dari <strong>{len(df)}</strong> data total
                        </div>
                    ''', unsafe_allow_html=True)
                    
                    # Tampilkan statistik
                    col_stat1, col_stat2, col_stat3 = st.columns(3)
                    with col_stat1:
                        st.markdown(f'''
                            <div class="metric-card pulse">
                                <h3 style="color: #28a745; margin-left: 20px;">{len(filtered_df)}</h3>
                                <p style="margin: 0; color: #6c757d;">Data Terfilter</p>
                            </div>
                        ''', unsafe_allow_html=True)
                    
                    with col_stat2:
                        st.markdown(f'''
                            <div class="metric-card pulse">
                                <h3 style="color: #28a745; margin: 0; padding-left: 20px;">{len(df)}</h3>
                                <p style="margin: 0; color: #6c757d;">Total Data</p>
                            </div>
                        ''', unsafe_allow_html=True)
                    
                    with col_stat3:
                        percentage = (len(filtered_df) / len(df) * 100) if len(df) > 0 else 0
                        st.markdown(f'''
                            <div class="metric-card pulse">
                                <h3 style="color: #28a745; margin: 0 0 0 20px;">{percentage:.1f}%</h3>
                                <p style="margin: 0; color: #6c757d;">Persentase</p>
                            </div>
                        ''', unsafe_allow_html=True)
                    
                    df_to_display = filtered_df
                    show_table = True
                    
                elif not has_valid_selection:
                    # Tampilkan pesan instruksi
                    st.markdown('''
                        <div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 15px; margin: 20px 0;">
                            <h3 style="color: #495057; margin-bottom: 15px;">Pilih Filter Tanggal</h3>
                            <p style="color: #6c757d; font-size: 16px;">Silakan pilih <strong>Tanggal</strong>, <strong>Bulan</strong>, dan <strong>Tahun</strong> untuk menampilkan data transaksi.</p>
                        </div>
                    ''', unsafe_allow_html=True)
                    show_table = False
                    
                else:
                    show_table = False
                    # Reset flag jika user mengubah pilihan tanpa menekan tombol
                    if 'data_displayed' in st.session_state:
                        del st.session_state.data_displayed

            else:
                st.markdown('''
                    <div class="warning-card">
                        <strong>Peringatan:</strong> Tidak ada data dengan tanggal yang valid.
                    </div>
                ''', unsafe_allow_html=True)
                show_table = False
                
        else:
            st.markdown('''
                <div class="warning-card">
                    <strong>Peringatan:</strong> Tidak ditemukan kolom tanggal dalam data.
                </div>
            ''', unsafe_allow_html=True)
            show_table = False
    else:
        st.markdown('''
            <div class="warning-card">
                <strong>Peringatan:</strong> Data kosong.
            </div>
        ''', unsafe_allow_html=True)
        show_table = False

    # Tampilkan tabel hanya jika kondisi terpenuhi
    if show_table and 'df_to_display' in locals() and not df_to_display.empty:
        # Initialize session state untuk pagination
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 1
        if 'items_per_page' not in st.session_state:
            st.session_state.items_per_page = 25
            
        # Reset halaman jika filter berubah atau baru pertama kali tampil
        current_filter = f"{actual_day}-{actual_month}-{actual_year}"
        if 'previous_filter' not in st.session_state:
            st.session_state.previous_filter = None
            
        if st.session_state.previous_filter != current_filter:
            st.session_state.current_page = 1
            st.session_state.previous_filter = current_filter
        
        total_items = len(df_to_display)
        items_per_page = st.session_state.items_per_page
        total_pages = (total_items + items_per_page - 1) // items_per_page
        
        # Hitung data untuk halaman saat ini
        start_idx = (st.session_state.current_page - 1) * items_per_page
        end_idx = min(start_idx + items_per_page, total_items)
        df_current_page = df_to_display.iloc[start_idx:end_idx]
        
        # Tampilkan tabel
        css_datacontainer()
        st.dataframe(df_current_page, use_container_width=True, hide_index=True)
        
        # Pagination controls
        css_pagination_controls()
        col_left, col_center, col_right = st.columns([2, 3, 2])
        
        with col_left:
            page_options = [10, 25, 50, 100, 200]
            current_index = page_options.index(st.session_state.items_per_page) if st.session_state.items_per_page in page_options else 1
            
            new_items_per_page = st.selectbox(
                "",
                options=page_options,
                index=current_index,
                format_func=lambda x: f"{x} rows",
                key="page_size_selector",
                label_visibility="collapsed"
            )
            
            if new_items_per_page != st.session_state.items_per_page:
                st.session_state.items_per_page = new_items_per_page
                st.session_state.current_page = 1
                st.rerun()
        
        with col_center:
            st.markdown(f"""
                <div style="text-align: center;">
                    <div class="pagination-info">
                        {start_idx + 1} - {end_idx} of {total_items}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        with col_right:
            nav_col1, nav_col2 = st.columns(2)
            
            # Atur rasio kolom: spacer di kiri (biar geser kanan), lalu dua kolom tombol
            spacer, nav_col1, nav_col2 = st.columns([10, 10, 10])  # Angka bisa disesuaikan

            with nav_col1:
                if st.button("◀ Prev", disabled=(st.session_state.current_page <= 1), key="prev_btn", help="Previous page"):
                    st.session_state.current_page -= 1
                    st.rerun()

            with nav_col2:
                if st.button("Next ▶", disabled=(st.session_state.current_page >= total_pages), key="next_btn", help="Next page"):
                    st.session_state.current_page += 1
                    st.rerun()



    st.markdown('</div>', unsafe_allow_html=True)