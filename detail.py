import streamlit as st
import pandas as pd
from pymongo import MongoClient
import plotly.express as px
from css import load_css_detail_page, css_header_detail_page
# pake dataset testtransaksi

def detaildashboard():
    # client = MongoClient("mongodb://pavita_ro:readonly@localhost:27017/?authSource=admin")
    client = MongoClient("mongodb+srv://masukannamatemananda:masukanpasswordtemananda@posindo.5juwxxh.mongodb.net/")
    db = client['pos_indonesia']

    # AGGREGATION PIPELINE
    testtransaksi_pipeline = [
        {"$facet": {
                "max_tarif": [
                    {
                        "$group": {
                            "_id": None,
                            "max_val": { "$max": "$hasilApi.tarif.totalFee" }
                        }
                    }
                ],
                "min_tarif": [
                    {
                        "$group": {
                            "_id": None,
                            "min_val": { "$min": "$hasilApi.tarif.totalFee" }
                        }
                    }
                ],
                "jumlah_transaksi": [
                    {"$group": {"_id": "$orderId"}},
                    {"$count": "count"}
                ],
                "status_transaksi": [
                    {"$group": {"_id": "$status", "count": {"$sum": 1}}}
                ],
                "rata_rata_berat": [
                    {"$project": {
                        "orderId": 1,
                        "total_berat": {"$sum": "$barang.berat"}
                    }},
                    {"$group": {
                        "_id": None,
                        "total_berat": {"$sum": "$total_berat"},
                        "jumlah_transaksi": {"$sum": 1}
                    }},
                    {"$project": { "rata_rata_berat": {
                        "$cond": [
                            {"$gt": ["$jumlah_transaksi", 0]},
                            {"$round": [{"$divide": ["$total_berat", "$jumlah_transaksi"]}, 2]},
                            0
                        ]
                    }}}
                ],
                "total_biaya": [
                    {"$group": {
                            "_id": None,
                            "total_biaya": {"$sum": "$hasilApi.tarif.totalFee"}
                    }}
                ],
                "distribusi_jenis_layanan": [
                    {"$group": {"_id": "$hasilApi.tarif.serviceName", "count": {"$sum": 1}}}
                ],
                "item_counts": [
                    {"$group": {"_id": "$barang.deskripsi", "count": {"$sum": 1}}}
                ], 
                "tracking_per_hari": [
                    {"$group": {
                        "_id": {"$dateToString": {"format": "%Y-%m-%d", "date": "$timestamps.updatedAt"}},
                        "count": {"$sum": 1}
                    }}, 
                    {"$sort": {"_id": 1}}
                ],
                "top_customer": [
                    {"$group": {
                        "_id": "$pengirim.nama",
                        "nama": {"$first": "$pengirim.nama"},
                        "jumlah_transaksi": {"$sum": 1}
                    }},
                    {"$sort": {"jumlah_transaksi": -1}},
                    {"$limit": 1}
                ],
                "biaya_pengiriman": [ # ambil biaya dari setiap pengiriman
                    {"$project": {
                            "_id": 0,
                            "orderId": 1,
                            "biaya_pengiriman": "$hasilApi.tarif.totalFee"
                    }}
                ],
                "kota_asal": [
                    {"$group": {"_id": "$pengirim.alamat.kota_kabupaten", "count": {"$sum": 1}}},
                    {"$sort": {"count": -1}},
                    {"$limit": 10}
                ],
                "jumlah_kiriman_per_tanggal": [
                    {"$group": {"_id": "$timestamps.createdAt", "count": {"$sum": 1}}},
                    {"$sort": {"_id": 1}}
                ],
                "status_tracking_detail": [
                    {
                        "$group": {
                            "_id": "$status",
                            "total": { "$sum": 1 }
                        }
                    },
                    { "$sort": { "total": -1 } }
                ]
        }}
    ]
    transaksi_agg = list(db['testtransaksi'].aggregate(testtransaksi_pipeline))[0]

    dashboard_data = {}

    # Jumlah transaksi
    dashboard_data['jumlah_transaksi'] = transaksi_agg['jumlah_transaksi'][0]['count'] if transaksi_agg['jumlah_transaksi'] else 0

    # Status transaksi
    dashboard_data['status_transaksi'] = {row['_id']: row['count'] for row in transaksi_agg['status_transaksi']}

    # Rata-rata berat
    dashboard_data['rata_rata_berat'] = transaksi_agg['rata_rata_berat'][0]['rata_rata_berat'] if transaksi_agg['rata_rata_berat'] else 0

    # Total biaya
    dashboard_data['total_biaya'] = transaksi_agg['total_biaya'][0]['total_biaya'] if transaksi_agg['total_biaya'] else 0

    # Distribusi jenis layanan
    dashboard_data['distribusi_jenis_layanan'] = {row['_id']: row['count'] for row in transaksi_agg['distribusi_jenis_layanan']}

    # Distribusi kota asal (mapping ke nama kota)
    dashboard_data['distribusi_kota_asal'] = {
        row['_id']: row['count']
        for row in transaksi_agg['kota_asal']
    }


    # Item counts untuk chart
    dashboard_data['item_counts'] = {row['_id']: row['count'] for row in transaksi_agg['item_counts']}
    
    # Tarif tertinggi dan terendah
    dashboard_data['tarif_tertinggi'] = transaksi_agg['max_tarif'][0]['max_val'] if transaksi_agg['max_tarif'] else None
    dashboard_data['tarif_terendah'] = transaksi_agg['min_tarif'][0]['min_val'] if transaksi_agg['min_tarif'] else None

    # Biaya pengiriman per kiriman 
    dashboard_data['biaya_pengiriman_per_kiriman'] = transaksi_agg['biaya_pengiriman']

    # Status tracking detail 
    dashboard_data['status_tracking_detail'] = {item["_id"]: item["total"] for item in transaksi_agg["status_tracking_detail"]}
    # Jumlah kiriman per tanggal
    dashboard_data['jumlah_kiriman_per_tanggal'] = {
        row['_id']: row['count']
        for row in transaksi_agg['jumlah_kiriman_per_tanggal']
    }
    
    # # Tracking per hari
    dashboard_data['tracking_per_hari'] = {item["_id"]: item["count"] for item in transaksi_agg["tracking_per_hari"]}

    # Top customer
    top_customer = transaksi_agg['top_customer'][0] if transaksi_agg['top_customer'] else {}
    dashboard_data['top_customer'] = {
        'id_customer': top_customer.get('_id', ''),
        'nama_customer': top_customer.get('nama', ''),
        'jumlah_transaksi': top_customer.get('jumlah_transaksi', 0)
    }

    return dashboard_data

def tampilkan_dashboard():
    load_css_detail_page()
    css_header_detail_page()
    dashboard = detaildashboard()

    st.markdown('<h2 class="section-header" style="color:white;">Ringkasan Utama</h2>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="Total Kiriman",
            value=dashboard['jumlah_transaksi'],
            delta="Semua status"
        )
    with col2:
        st.metric(
            label="Rata-rata Berat",
            value=f"{dashboard['rata_rata_berat']} g",
            delta="Per kiriman"
        )
    with col3:
        st.metric(
            label="Total Estimasi Biaya",
            value=f"Rp {dashboard['total_biaya']:,.0f}",
            delta="Semua kiriman"
        )

    st.markdown('<h2 class="section-header" style="color:white;">Visualisasi Data</h2>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Distribusi Kota Asal")
        kota_data = dashboard['distribusi_kota_asal']
        fig_kota = px.pie(
            values=list(kota_data.values()),
            names=list(kota_data.keys()),
            title="Top 10 Kota Asal Pengiriman",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_kota.update_layout(
            title_font_size=16,
            title_x=0.5,
            height=400
        )
        st.plotly_chart(fig_kota, use_container_width=True)
    with col2:
        st.subheader("Jenis Item Dikirim")
        item_counts = dashboard['item_counts']
        fig_items = px.bar(
            x=list(item_counts.keys()),
            y=list(item_counts.values()),
            title="Distribusi Jenis Item",
            color=list(item_counts.values()),
            color_continuous_scale="viridis"
        )
        fig_items.update_layout(
            title_font_size=16,
            title_x=0.5,
            height=400,
            showlegend=False,
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig_items, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-header" style="color:white;">Trend Pengiriman</h2>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Kiriman per Tanggal")
        kiriman_dates = list(dashboard['jumlah_kiriman_per_tanggal'].keys())
        kiriman_counts = list(dashboard['jumlah_kiriman_per_tanggal'].values())
        fig_kiriman = px.line(
            x=kiriman_dates,
            y=kiriman_counts,
            title="Trend Jumlah Kiriman Harian",
            markers=True
        )
        fig_kiriman.update_layout(
            title_font_size=16,
            title_x=0.5,
            height=400
        )
        st.plotly_chart(fig_kiriman, use_container_width=True)
    with col2:
        st.subheader("Aktivitas Tracking")
        tracking_dates = list(dashboard['tracking_per_hari'].keys())
        tracking_counts = list(dashboard['tracking_per_hari'].values())
        fig_tracking = px.bar(
            x=tracking_dates,
            y=tracking_counts,
            title="Aktivitas Tracking Harian",
            color=tracking_counts,
            color_continuous_scale="blues"
        )
        fig_tracking.update_layout(
            title_font_size=16,
            title_x=0.5,
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig_tracking, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<h2 class="section-header" style="color:white;">Informasi Biaya & Tarif</h2>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h4>Tarif Tertinggi per gram</h4>
            <h2 style="color: #e74c3c;">Rp {:,.0f}</h2>
        </div>
        """.format(dashboard['tarif_tertinggi']), unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h4>Tarif Terendah per kg</h4>
            <h2 style="color: #27ae60;">Rp {:,.0f}</h2>
        </div>
        """.format(dashboard['tarif_terendah']), unsafe_allow_html=True)

    st.subheader("Detail Biaya Pengiriman")
    biaya_df = pd.DataFrame(dashboard['biaya_pengiriman_per_kiriman'])
    if not biaya_df.empty:
        biaya_df['biaya_pengiriman'] = biaya_df['biaya_pengiriman'].apply(lambda x: f"Rp {x:,.0f}")
        st.dataframe(
            biaya_df,
            use_container_width=True,
            hide_index=True
        )
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<h2 class="section-header" style="color:white;">Top Customer</h2>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    top_customer = dashboard['top_customer']
    st.markdown(f"""
    <div class="highlight-box">
        <h3>Customer Terbaik</h3>
        <p><strong>Nama:</strong> {top_customer['nama_customer']}</p>
        <p><strong>Jumlah Kiriman:</strong> {top_customer['jumlah_transaksi']} pengiriman</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<h2 class="section-header" style="color:white;">Status Tracking Detail</h2>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    tracking_detail = dashboard['status_tracking_detail']
    col1, col2 = st.columns(2)
    with col1:
        fig_tracking_detail = px.bar(
            x=list(tracking_detail.keys()),
            y=list(tracking_detail.values()),
            title="Distribusi Status Tracking",
            color=list(tracking_detail.values()),
            color_continuous_scale="plasma",
            labels={'x': 'status', 'y': 'Jumlah'}
        )
        fig_tracking_detail.update_layout(
            title_font_size=16,
            title_x=0.5,
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig_tracking_detail, use_container_width=True)
    with col2:
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Return", 0, delta="Paket kembali")
            st.metric("Delivery", 0, delta="Dalam pengiriman")
        with col_b:
            st.metric("Received", 0, delta="Telah diterima")
            st.metric("In Location", 0, delta="Di lokasi transit")
    st.markdown("<br>", unsafe_allow_html=True)