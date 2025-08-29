import streamlit as st
import pandas as pd
from pymongo import MongoClient

def update_provinsi_page():
  st.title("Update Pemekaran Wilayah")
  # Koneksi ke MongoDB Atlas
  client = MongoClient("mongodb+srv://pavita:pavitamongodb@cluster0.cqmcd12.mongodb.net/")
  db = client['datapos']
  collection = db['csvdatapos']
  data = list(collection.find())
  df = pd.DataFrame(data)

  prov_lama = st.selectbox("Pilih Provinsi Lama", df['PROV'].unique())
  prov_baru = st.text_input("Masukkan Nama Provinsi Baru (contoh: Jawa Bogor)")

# Filter wilayah di provinsi lama
  filtered = df[df['PROV'] == prov_lama]
  kelurahan_pindah = st.multiselect("Pilih Desa/Kelurahan yang pindah ke provinsi baru", filtered['DESA_KELURAHAN'].unique())

  if st.button("Update Data"):
    # Salin data asli
    df_updated = df.copy()

    # Update provinsi sesuai input user
    mask = (df_updated['PROV'] == prov_lama) & (df_updated['DESA_KELURAHAN'].isin(kelurahan_pindah))
    df_updated.loc[mask, 'PROV'] = prov_baru

    # Tambahkan log perubahan
    perubahan = df_updated.loc[mask].copy()
    perubahan['DARI_PROVINSI'] = prov_lama
    perubahan['KE_PROVINSI'] = prov_baru

    # Simpan hasil
    df_updated.to_csv("kode_pos_indonesia_gabungan_final.csv", index=False)
    st.success("berhasil")
    st.write("Log Perubahan:")
    st.dataframe(perubahan)
