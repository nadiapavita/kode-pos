import streamlit as st
from pymongo import MongoClient
import time

active_sessions = {}

def get_user_from_db(username):
    #client = MongoClient("mongodb://pavita_ro:readonly@localhost:27017/?authSource=admin")
    client = MongoClient("mongodb+srv://masukannamatemananda:masukanpasswordtemananda@posindo.5juwxxh.mongodb.net/")
    
    db = client["pos_indonesia"]
    collection = db["datalogin"]
    user = collection.find_one({"username": username})
    return user 

def init_session_state():
    defaults = {
        "logged_in": False,
        "show_register": False,
        "show_forgot_password": False,
        "username": None,
        "role":None,
        "cabang": None,
        "token": None
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def login(username, password):
    user = get_user_from_db(username)
    if user and user.get("password") == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.session_state.role = user.get("role", "user")
        st.session_state.cabang = user.get("cabang")
        st.session_state.token = generate_token(username)
        return True
    return False

def generate_token(username):
    token = f"{username}_{int(time.time())}"
    active_sessions[username] = token
    return token

def is_token_valid(username, token):
    return active_sessions.get(username) == token


def login_page():
    st.markdown("""
      <div style="text-align: center;">
        <img src="https://tse4.mm.bing.net/th/id/OIP.kvmRXFUus_NUlVUUf_8p6AAAAA?r=0&cb=thvnextc1&pid=ImgDet&w=150&h=150&c=7&dpr=1,5&o=7&rm=3" width="150">
      </div>
    """, unsafe_allow_html=True)
    st.markdown('<p class="compact-form-subtitle">Silakan masukkan kredensial Anda</p>', unsafe_allow_html=True)

    with st.form("login_form"):
        username = st.text_input("Username", placeholder="Masukkan username", key="login_username")
        password = st.text_input("Password", type="password", placeholder="Masukkan password", key="login_password")

        login_button = st.form_submit_button("Masuk", use_container_width=True)

        if login_button:
            if username and password:
                if login(username, password):
                    st.success("Login berhasil! Mengarahkan...")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Username atau password salah!")
            else:
                st.warning("Mohon lengkapi semua field!")

def logout():
    username = st.session_state.username
    if username in active_sessions:
        del active_sessions[username]
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.role = None
    st.session_state.cabang = None
    st.session_state.token = None
    st.rerun()