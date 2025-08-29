import streamlit as st
from pymongo import MongoClient
import pandas as pd
from css import headernya
def cari_kode_pos_page():
    headernya('Pencarian Kode Pos Indonesia', 'Temukan kode pos dengan mudah menggunakan dropdown alamat yang tersedia')
    # client = MongoClient("mongodb://pavita_ro:readonly@localhost:27017/?authSource=admin")
    client = MongoClient("mongodb+srv://masukannamatemananda:masukanpasswordtemananda@posindo.5juwxxh.mongodb.net/")
    db = client['pos_indonesia']
    collection = db['kodepos']

    if collection is not None:
            st.markdown('<div class="section-header">Pilih Alamat Lengkap</div>', unsafe_allow_html=True)

            with st.container():

                col1, col2 = st.columns(2)

                with col1:
                    provinsi_list = collection.distinct("Provinsi")
                    provinsi_list.sort()
                    st.markdown("**Provinsi**")
                    prov = st.selectbox("Pilih Provinsi", provinsi_list, key="prov")

                    kota_list = collection.distinct("Kota_Kabupaten",{"Provinsi": prov})
                    kota_list.sort()
                    st.markdown("**Kabupaten/Kota**")
                    kota = st.selectbox("Pilih Kabupaten/Kota", kota_list, key="kota")

                with col2:
                    kecamatan_list = collection.distinct("Kecamatan",{"Provinsi": prov, "Kota_Kabupaten": kota})
                    kecamatan_list.sort()
                    st.markdown("**Kecamatan**")
                    kec = st.selectbox("Pilih Kecamatan", kecamatan_list, key="kec")

                    desa_list = collection.distinct("Desa_Kelurahan",{"Provinsi": prov, "Kota_Kabupaten": kota, "Kecamatan": kec})
                    desa_list.sort()
                    st.markdown("**Kelurahan/Desa**")
                    kel = st.selectbox("Pilih Kelurahan/Desa", desa_list, key="kel")

                st.markdown('</div>', unsafe_allow_html=True)

                # Result Display
                if prov and kota and kec and kel:
                    query = {
                        "Provinsi": prov,
                        "Kota_Kabupaten": kota,
                        "Kecamatan": kec,
                        "Desa_Kelurahan": kel
                    }
                    fields = {"Kodepos": 1, "_id": 0}
                    result = collection.find_one(query, fields)

                    if result:
                        kodepos = result["Kodepos"]
                        st.markdown(f'''
                            <div class="result-card">
                                <h2>Kode Pos Ditemukan!</h2>
                                <div class="postal-code">{kodepos}</div>
                                <p style="margin-top: 1.5rem; font-size: 1.1rem; opacity: 0.9;">
                                    📍 {kel}, {kec}, {kota}, {prov}
                                </p>
                            </div>
                        ''', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    else:
            st.markdown('''
                <div class="main-card">
                    <div style="text-align: center; padding: 3rem;">
                        <div style="font-size: 5rem; margin-bottom: 2rem;">⚠️</div>
                        <h3 style="color: #ef4444; margin-bottom: 1rem;">File Data Tidak Ditemukan</h3>
                        <p style="color: #64748b; font-size: 1.1rem;">
                            collection 'kodepos' tidak ditemukan.<br>
                            Cek mongo siapa tau ada typo.
                        </p>
                    </div>
                </div>
            ''', unsafe_allow_html=True)
