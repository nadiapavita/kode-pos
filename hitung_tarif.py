import streamlit as st
from pymongo import MongoClient
from css import headernya

def hitung_tarif_kirim_page():
    headernya('Tarif Pengiriman', 'Hitung biaya pengiriman paket Anda dengan akurat dan terpercaya')
    try:
        # Koneksi MongoDB
        client = MongoClient("mongodb+srv://masukannamatemananda:masukanpasswordtemananda@posindo.5juwxxh.mongodb.net/")
        db = client['pos_indonesia']
        collection = db['tarif_pos']

        # Form input
        with st.form("form_tarif"):
            st.markdown("### Input Data Pengiriman")
            kode_pos_asal = st.text_input("Kode Pos Asal").strip()
            kode_pos_tujuan = st.text_input("Kode Pos Tujuan").strip()
            berat_gram = st.number_input("Berat Paket (gram)", min_value=0.1, step=0.1)
            submit = st.form_submit_button("Cari Tarif")

        # Proses setelah submit
        if submit and kode_pos_asal and kode_pos_tujuan and berat_gram > 0:
            # Query database
            query = {
                "asal": kode_pos_asal,
                "tujuan": kode_pos_tujuan
            }
            
            tarif_data = collection.find_one(query)
            
            if tarif_data:
                # Simpan data di session state
                st.session_state.tarif_data = tarif_data
                st.session_state.berat_input = berat_gram
                st.success(f"Data tarif ditemukan! Pilih layanan di bawah.")
            else:
                st.error("Data tarif untuk rute ini tidak ditemukan di database.")
                st.info("Pastikan kode pos yang dimasukkan sesuai dengan data yang ada di database.")

        # Tampilkan dropdown layanan dan hasil jika data sudah ada
        if hasattr(st.session_state, 'tarif_data') and st.session_state.tarif_data:
            tarif_data = st.session_state.tarif_data
            berat_gram = st.session_state.berat_input
            
            layanan_list = tarif_data.get('layanan', [])
            
            st.markdown("### Pilih Layanan")
            layanan_nama = st.selectbox(
                "Layanan Pengiriman",
                [l.get('nama_layanan', 'Unnamed') for l in layanan_list],
                key="layanan_selectbox"
            )
            
            if layanan_nama:
                layanan_terpilih = next(
                    (l for l in layanan_list if l.get('nama_layanan') == layanan_nama), None
                )
                
                if layanan_terpilih:
                    tarif_total_db = layanan_terpilih.get('tarif', 0)
                    estimasi = layanan_terpilih.get('estimasi', 'Tidak tersedia')
                    catatan = layanan_terpilih.get('catatan', '')

                    berat_db = float(tarif_data.get('berat_gram', 1))
                    tarif_per_gram = tarif_total_db / berat_db
                    total_tarif = tarif_per_gram * float(berat_gram)

                    st.markdown("## Hasil Perhitungan Tarif")
                    
                    # Tampilkan dalam box yang menarik
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.metric(
                            label="Total Tarif",
                            value=f"Rp {total_tarif:,.0f}",
                            delta=f"Untuk {berat_gram} gram"
                        )
                    
                    with col2:
                        st.metric(
                            label="Tarif per Gram",
                            value=f"Rp {tarif_per_gram:,.0f}",
                            delta=f"Estimasi: {estimasi}"
                        )
                    
                    # Detail lengkap
                    st.success(f"""
                        **Layanan:** {layanan_nama}  
                        **Estimasi Pengiriman:** {estimasi}  
                        **Catatan:** {catatan if catatan else 'Tidak ada catatan khusus'}  
                        **Berat Paket:** {berat_gram} gram  
                        **Total Tarif:** Rp {total_tarif:,.0f}
                    """)
                    
                    # Tampilkan detail perhitungan
                    with st.expander("Lihat Detail Perhitungan"):
                        st.write(f"""
                        **Perhitungan:**
                        - Tarif referensi database: Rp {tarif_total_db:,.0f} untuk {berat_db} gram
                        - Tarif per gram: Rp {tarif_total_db:,.0f} ÷ {berat_db} = Rp {tarif_per_gram:,.2f}
                        - Total tarif: Rp {tarif_per_gram:,.2f} × {berat_gram} gram = Rp {total_tarif:,.0f}
                        """)

        elif submit:
            st.warning("Mohon isi semua input dengan benar.")

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
        st.write("**Detail error untuk debugging:**")
        import traceback
        st.code(traceback.format_exc())