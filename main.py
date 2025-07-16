import streamlit as st
st.set_page_config(
    page_title="POSINDO - Alamat & Tarif",
    layout="wide",
    initial_sidebar_state="expanded",
)
from login import login_page, logout, init_session_state
from cari_kode_pos import cari_kode_pos_page
from css import load_css, load_css1, load_css_informasi, load_css_info, load_css_footer
from csslogin import load_css_login
from hitung_tarif import hitung_tarif_kirim_page
from update import update_provinsi_page
from detail import tampilkan_dashboard
from datakiriman import datanya_page

load_css()
init_session_state()

if not st.session_state.logged_in: #if not st.session_state.logged_in: ---- pake ini kalo mau login dulu
    if not st.session_state.show_register and not st.session_state.show_forgot_password:
      load_css_login()
      login_page()

else:
  with st.sidebar:
    # Logo Pos Indonesia
    st.image("https://www.posindonesia.co.id/assets/logo.png", width=200)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### Pilih Layanan")
    load_css1()

    page = st.selectbox(
        "Pilih Halaman",
        ["Cari Kode Pos", "Hitung Tarif Kirim", "Update Provinsi", "Detail laporan", "Data Kiriman"]
    )

    st.markdown("---")

    # Add informasi dengan design yang lebih menarik
    load_css_informasi()
    load_css_info()

    st.markdown("<div style= 'height : 200px;'></div')>", unsafe_allow_html=True)
    st.markdown("---")
    if st.button("Logout"):
      logout()
      st.session_state.clear()
      st.experimental_rerun()

  if page == "Cari Kode Pos":
        cari_kode_pos_page()
  elif page == "Hitung Tarif Kirim":
        hitung_tarif_kirim_page()
  elif page == "Update Provinsi":
        update_provinsi_page()
  elif page == "Detail laporan":
        tampilkan_dashboard()
  elif page == "Data Kiriman":
        datanya_page()

  load_css_footer()