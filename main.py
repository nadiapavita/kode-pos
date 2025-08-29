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
from detail import tampilkan_dashboard
from tabeldata import datanya_page
from loket import loket_page

load_css()
load_css_sidebar()
init_session_state()

if 'selected_page' not in st.session_state:
    st.session_state.selected_page = "Loket"

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
        role_display = "Administrator" if st.session_state.role == "admin" else "Pengguna"
        st.markdown(f"""
        <div class="welcome-toast">
            <div class="welcome-name">Selamat datang, {st.session_state.username}</div>
            <div class="welcome-role">Login sebagai {role_display}</div>
            <div class="welcome-cabang">Cabang nya di {st.session_state.cabang}</div>
        </div>
        """, unsafe_allow_html=True)
        st.session_state.show_welcome = True
    
    st.markdown('</div>', unsafe_allow_html=True)

    load_css1()
    
    st.markdown('<div class="menu-container">', unsafe_allow_html=True)
    st.markdown('<h4 class="menu-title">Pilih Layanan</h4>', unsafe_allow_html=True)
    
    menu_items = [
        ("ikonloket", "Loket", "Loket"),
        ("search", "Cari Kode Pos", "Cari Kode Pos"),
        ("calculator", "Hitung Tarif Kirim", "Hitung Tarif Kirim"),
        ("chart", "Detail Laporan", "Detail laporan"),
        ("database", "Data Transaksi", "Data Transaksi")
    ]

    icons = {
        "search": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5l-1.5 1.5l-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16A6.5 6.5 0 0 1 3 9.5A6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14S14 12 14 9.5S12 5 9.5 5"/></svg>""",
        "calculator": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M7 2h10a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2m0 2v4h10V4zm0 6v2h2v-2zm4 0v2h2v-2zm4 0v2h2v-2zm-8 4v2h2v-2zm4 0v2h2v-2zm4 0v2h2v-2zm-8 4v2h2v-2zm4 0v2h6v-2z"/></svg>""",
        "refresh": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M12 20q-3.35 0-5.675-2.325T4 12t2.325-5.675T12 4q1.725 0 3.3.712T18 6.75V4h2v7h-7V9h4.2q-.8-1.4-2.187-2.2T12 6Q9.5 6 7.75 7.75T6 12t1.75 4.25T12 18q1.925 0 3.475-1.1T17.65 14h2.1q-.7 2.65-2.85 4.325T12 20"/></svg>""",
        "chart": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M22 21H2l4-7l4 7l4-7l4 7l4-7zm0-9l-4 7l-4-7l-4 7l-4-7l-4 7V3h20z"/></svg>""",
        "database": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M12 3C7.58 3 4 4.79 4 7s3.58 4 8 4s8-1.79 8-4s-3.58-4-8-4M4 9v3c0 2.21 3.58 4 8 4s8-1.79 8-4V9c0 2.21-3.58 4-8 4s-8-1.79-8-4m0 5v3c0 2.21 3.58 4 8 4s8-1.79 8-4v-3c0 2.21-3.58 4-8 4s-8-1.79-8-4"/></svg>""",
        "ikonloket": """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24"><path fill="currentColor" d="M21 5H3c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h18c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 12H3V7h18v10z"/><path fill="currentColor" d="M5 9h2v2H5zm0 4h2v2H5zm4-4h8v2H9zm0 4h6v2H9z"/></svg>"""
    }
    
    for icon_key, display_text, page_key in menu_items:
        is_active = st.session_state.selected_page == page_key
        
        col1, col2 = st.columns([1, 10])
        with col1:
            st.markdown(f'<div class="icon-display">{icons[icon_key]}</div>', unsafe_allow_html=True)
        with col2:
            if st.button(display_text, 
                        key=f"btn_{page_key}",
                        use_container_width=True,
                        type="primary" if is_active else "secondary"):
                st.session_state.selected_page = page_key
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

    load_css_informasi()
    load_css_info()

    st.markdown("<div style= 'height : 200px;'></div>", unsafe_allow_html=True)
    st.markdown("---")
    
    if st.button("Logout", use_container_width=True, type="primary"):
      logout()
      st.session_state.clear()
      st.rerun()

  page = st.session_state.selected_page
  
  if page == "Loket":
    loket_page()
  elif page == "Cari Kode Pos":
    cari_kode_pos_page()
  elif page == "Hitung Tarif Kirim":
    hitung_tarif_kirim_page()
  elif page == "Detail laporan":
    tampilkan_dashboard()
  elif page == "Data Transaksi":
    datanya_page()

  load_css_footer()
