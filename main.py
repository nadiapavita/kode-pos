import streamlit as st
st.set_page_config(
    page_title="POSINDO - Alamat & Tarif",
    layout="wide",
    initial_sidebar_state="expanded",
)
from login import login_page, logout, init_session_state
from cari_kode_pos import cari_kode_pos_page
from css import load_css, load_css1, load_css_informasi, load_css_info, load_css_footer, load_css_sidebar
from csslogin import load_css_login
from hitung_tarif import hitung_tarif_kirim_page
from update import update_provinsi_page
from detail import tampilkan_dashboard
from tabeldata import datanya_page

load_css()
load_css_sidebar()
init_session_state()

if not st.session_state.logged_in:
    if not st.session_state.show_register and not st.session_state.show_forgot_password:
      load_css_login()
      login_page()

else:
  with st.sidebar:
    # Logo Pos Indonesia
    st.image("https://www.posindonesia.co.id/assets/logo.png", width=200)
    
    # Welcome toast notification pas baru login
    if 'show_welcome' not in st.session_state:
        st.session_state.show_welcome = True
    
    if st.session_state.show_welcome:
        #role_display = "Administrator" if st.session_state.role == "admin" else "Pengguna"
        st.markdown(f"""
        <div class="welcome-toast">
            <div class="welcome-name">Selamat datang, {st.session_state.username}</div>
            <div class="welcome-role">Login sebagai {st.session_state.role}</div>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.show_welcome = False
    
    st.markdown('</div>', unsafe_allow_html=True)

    load_css1()
    if st.session_state.role == "admin":
      st.markdown("<h4 style='margin-bottom: -500px;'>Pilih Layanan</h4>", unsafe_allow_html=True)
      page = st.selectbox(
            "",
            ["Cari Kode Pos", "Hitung Tarif Kirim", "Update Provinsi", "Detail laporan", "Data Transaksi"]
      )
    elif st.session_state.role == "user":
      st.markdown("<h4 style='margin-bottom: -500px;'>Pilih Layanan</h4>", unsafe_allow_html=True)
      page = st.selectbox(
            "",
            ["Cari Kode Pos", "Hitung Tarif Kirim", "Detail laporan", "Data Transaksi"]
      )

    st.markdown("---")

    # Add informasi dengan design yang lebih menarik
    load_css_informasi()
    load_css_info()

    st.markdown("<div style= 'height : 200px;'></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    if st.button("Logout"):
      logout()
      st.session_state.clear()
      st.rerun()

  if st.session_state.role == "admin":
      if page == "Cari Kode Pos":
            cari_kode_pos_page()
      elif page == "Hitung Tarif Kirim":
            hitung_tarif_kirim_page()
      elif page == "Update Provinsi":
            update_provinsi_page()
      elif page == "Detail laporan":
            tampilkan_dashboard()
      elif page == "Data Transaksi":
            datanya_page()

      load_css_footer()
  elif st.session_state.role == "user":
      if page == "Cari Kode Pos":
            cari_kode_pos_page()
      elif page == "Hitung Tarif Kirim":
            hitung_tarif_kirim_page()
      elif page == "Detail laporan":
            tampilkan_dashboard()
      elif page == "Data Transaksi":
            datanya_page()

      load_css_footer()
