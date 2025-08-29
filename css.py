import streamlit as st
def headernya(judul, subjudul):
    st.markdown(f'''
        <div class="header-gradient fade-in">
            <h1 class="main-title" style="color: white; -webkit-text-fill-color: white; margin-bottom: 1rem;">{judul}</h1>
            <p class="subtitle" style="color: rgba(255,255,255,0.9); font-size: 1.3rem;">{subjudul}</p>
        </div>
    ''', unsafe_allow_html=True)

def load_css():
  st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    .main {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #3b82f6 100%);
        font-family: 'Poppins', sans-serif;
        min-height: 100vh;
    }
 
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Sidebar Styling dengan warna biru Pos Indonesia */
    .css-1d391kg {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
    }

    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
    }

    /* Main Content Card */
    .main-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 2.5rem;
        box-shadow: 0 25px 50px rgba(30, 60, 114, 0.15);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }

    .main-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #1e3c72, #2a5298, #3b82f6);
    }

    /* Title Styling */
    .main-title {
        text-align: center;
        color: #1e3c72;
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(30, 60, 114, 0.1);
        background: linear-gradient(45deg, #1e3c72, #2a5298, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-weight: 400;
    }

    /* Section Headers */
    .section-header {
        background: linear-gradient(45deg, #1e3c72, #2a5298);
        color: white;
        padding: 1.2rem 2rem;
        border-radius: 20px;
        margin: 2rem 0 1.5rem 0;
        font-weight: 600;
        font-size: 1.3rem;
        box-shadow: 0 15px 30px rgba(30, 60, 114, 0.3);
        border: none;
        text-align: center;
        position: relative;
        overflow: hidden;
    }

    .section-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        animation: shimmer 2s infinite;
    }

    /* Input Containers */
    .input-container {
        background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(248,250,252,0.9));
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 2px solid rgba(30, 60, 114, 0.1);
        box-shadow: 0 10px 25px rgba(30, 60, 114, 0.08);
        transition: all 0.4s ease;
        position: relative;
    }

    .input-container:hover {
        border-color: rgba(30, 60, 114, 0.3);
        box-shadow: 0 15px 35px rgba(30, 60, 114, 0.15);
        transform: translateY(-3px);
    }

    /* Form Styling */
    .stSelectbox label, .stNumberInput label {
        font-weight: 600;
        color: #1e3c72;
        font-size: 1rem;
        margin-bottom: 0.8rem;
    }

    .stSelectbox > div > div {
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.95));
        border: 2px solid rgba(30, 60, 114, 0.2);
        border-radius: 15px;
        transition: all 0.3s ease;
        font-weight: 500;
    }

    .stSelectbox > div > div:focus-within {
        border-color: #2a5298;
        box-shadow: 0 0 0 4px rgba(30, 60, 114, 0.1);
        transform: translateY(-1px);
    }

    .stNumberInput > div > div > input {
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.95));
        border: 2px solid rgba(30, 60, 114, 0.2);
        border-radius: 15px;
        transition: all 0.3s ease;
        font-weight: 500;
    }

    .stNumberInput > div > div > input:focus {
        border-color: #2a5298;
        box-shadow: 0 0 0 4px rgba(30, 60, 114, 0.1);
        transform: translateY(-1px);
    }

    /* Button Styling */
    .stButton > button {
        background: linear-gradient(45deg, #1e3c72, #2a5298);
        color: white;
        font-weight: 600;
        border-radius: 20px;
        border: none;
        padding: 1rem 2.5rem;
        font-size: 1.2rem;
        box-shadow: 0 15px 30px rgba(30, 60, 114, 0.3);
        transition: all 0.4s ease;
        width: 100%;
        position: relative;
        overflow: hidden;
    }

    .stButton > button:hover {
        background: linear-gradient(45deg, #153358, #1e3c72);
        transform: translateY(-4px);
        box-shadow: 0 20px 40px rgba(30, 60, 114, 0.4);
    }

    .stButton > button:active {
        transform: translateY(-2px);
    }

    /* Result Cards */
    .result-card {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #3b82f6 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(30, 60, 114, 0.3);
        margin: 1.5rem 0;
        border: 2px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }

    .result-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }

    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .result-card h2 {
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        position: relative;
        z-index: 2;
    }

    .result-card .postal-code {
        font-size: 3rem;
        font-weight: 800;
        background: rgba(255, 255, 255, 0.2);
        padding: 1.5rem;
        border-radius: 20px;
        margin-top: 1.5rem;
        border: 2px solid rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
        position: relative;
        z-index: 2;
    }

    /* Search Card Styling */
    .search-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.95), rgba(248,250,252,0.95));
        border-radius: 25px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 2px solid rgba(30, 60, 114, 0.1);
        box-shadow: 0 15px 35px rgba(30, 60, 114, 0.1);
        text-align: center;
    }

    .search-icon {
        font-size: 4rem;
        color: #2a5298;
        margin-bottom: 1rem;
    }

    /* Success/Info/Warning Messages */
    .stSuccess, .stInfo, .stWarning {
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: none;
        font-weight: 500;
        text-align: center;
    }

    .stSuccess {
        background: linear-gradient(45deg, #10b981, #34d399);
        color: white;
        box-shadow: 0 15px 30px rgba(16, 185, 129, 0.3);
    }

    .stInfo {
        background: linear-gradient(45deg, #1e3c72, #2a5298);
        color: white;
        box-shadow: 0 15px 30px rgba(30, 60, 114, 0.3);
    }

    .stWarning {
        background: linear-gradient(45deg, #f59e0b, #fbbf24);
        color: white;
        box-shadow: 0 15px 30px rgba(245, 158, 11, 0.3);
    }

    /* Error Messages */
    .stError {
        background: linear-gradient(45deg, #ef4444, #f87171);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: none;
        font-weight: 500;
        box-shadow: 0 15px 30px rgba(239, 68, 68, 0.3);
        text-align: center;
    }

    /* Sidebar Enhancements */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1d2a5f 0%, #1d2a5f 100%) !important;
        color: white;
    }

    .sidebar .sidebar-content,
    .sidebar-content * {
        color: white !important;
    }

    .sidebar-title {
        color: white !important;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-size: 1.8rem;
    }


    .logo-container {
        text-align: center;
        margin-bottom: 2rem;
        padding: 1rem;
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }

    /* Animation for loading */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .fade-in {
        animation: fadeInUp 0.8s ease-out;
    }

    /* Mobile Responsiveness */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.2rem;
        }

        .result-card .postal-code {
            font-size: 2.5rem;
        }

        .input-container {
            padding: 1.5rem;
        }
    }

    /* Enhanced glassmorphism effect */
    .glass-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 25px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 25px 50px rgba(30, 60, 114, 0.1);
    }

    /* Header gradient */
    .header-gradient {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #3b82f6 100%);
        color: white;
        border-radius: 25px;
        padding: 3rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }

    .header-gradient::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: slide 3s infinite;
    }

    @keyframes slide {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    </style>
""", unsafe_allow_html=True)
  
def load_css1():
  st.markdown("""
    <style>
    .stRadio > div {
        color: white !important;
    }
    .stRadio > div > label {
        color: white !important;
    }
    .stRadio > div > label > div {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)
  
def load_css_informasi():
  st.markdown("""
    <div style="background: rgba(255,255,255,0.15); padding: 1.5rem; border-radius: 15px; margin-top: 1.5rem; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2);">
        <h4 style="color: white; margin-bottom: 1rem; text-align: center;">ℹ️ Informasi</h4>
        <p style="color: rgba(255,255,255,0.9); font-size: 0.95rem; margin-bottom: 0; text-align: center; line-height: 1.6;">
            Aplikasi resmi untuk mencari kode pos dan menghitung tarif pengiriman Pos Indonesia dengan mudah dan akurat.
        </p>
    </div>
    """, unsafe_allow_html=True)
  
def load_css_info():
  st.markdown("""
    <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; margin-top: 1rem; text-align: center;">
        <h5 style="color: white; margin-bottom: 0.5rem;">📞 Bantuan</h5>
        <p style="color: rgba(255,255,255,0.8); font-size: 0.85rem; margin-bottom: 0;">
            Hubungi: 161 (24 jam)
        </p>
    </div>
    """, unsafe_allow_html=True)

def load_css_footer():
  st.markdown('''
    <div style="margin-top: 4rem; text-align: center; padding: 3rem 2rem; background: linear-gradient(135deg, rgba(30, 60, 114, 0.1), rgba(42, 82, 152, 0.1)); border-radius: 25px; backdrop-filter: blur(10px);">
        <div style="font-size: 2rem; margin-bottom: 1rem;">📮</div>
        <h4 style="color: #1e3c72; margin-bottom: 1rem; font-weight: 600;">POSINDO - Pos Indonesia</h4>
        <p style="color: #64748b; font-size: 1rem; margin-bottom: 0.5rem;">
            © 2024 Aplikasi Resmi Cek Kode Pos & Tarif Pengiriman
        </p>
        <p style="color: #64748b; font-size: 0.9rem; margin-bottom: 0;">
        </p>
        <div style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(30, 60, 114, 0.2);">
            <p style="color: #2a5298; font-size: 0.95rem; font-weight: 500; margin-bottom: 0;">
                📞 Layanan Pelanggan: 161 (24 Jam) | 🌐 www.posindonesia.co.id
            </p>
        </div>
    </div>
  ''', unsafe_allow_html=True)

def load_css_detail_page():
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(45deg, #1e3c72, #2a5298, #3b82f6);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: white;
        text-align: center;
        margin: 0;
        font-size: 2.5rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
    }
    .section-header {
        color: #2c3e50;
        font-size: 1.5rem;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #667eea;
    }
    .highlight-box {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e9ecef;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

def css_header_detail_page():
    st.markdown("""
    <div class="main-header">
        <h1>Dashboard Pengiriman & Logistik</h1>
        <p style="color: white; text-align: center; margin: 0; font-size: 1.2rem;">
            Analisis Data Pengiriman & Tracking Real-time
        </p>
    </div>
    """, unsafe_allow_html=True)

def css_tabeldata():
    st.markdown('''
        <style>
        .header-gradient {
            background: linear-gradient(135deg, #4a6fa5 0%, #3b5998 100%);
            padding: 2.5rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            text-align: center;
            box-shadow: 0 15px 40px rgba(0,0,0,0.15);
            position: relative;
            overflow: hidden;
        }
        
        .header-gradient::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: shimmer 3s infinite;
        }
        
        @keyframes shimmer {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .fade-in {
            animation: fadeIn 1s ease-in-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .main-title {
            font-size: 3rem;
            font-weight: 800;
            margin: 0;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
            position: relative;
            z-index: 1;
        }
        
        .filter-container {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 2rem;
            border-radius: 20px;
            margin-bottom: 2rem;
            border: 1px solid #dee2e6;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            position: relative;
            overflow: hidden;
        }
        
        .filter-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2, #667eea);
            background-size: 200% 100%;
            animation: gradientShift 3s ease infinite;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 0%; }
            50% { background-position: 100% 0%; }
            100% { background-position: 0% 0%; }
        }
        
        .filter-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: #495057;
            margin-bottom: 1.5rem;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        
        .filter-title::before,
        .filter-title::after {
            content: '';
            flex: 1;
            height: 2px;
            background: linear-gradient(90deg, transparent, #667eea, transparent);
        }
        
        .data-container {
            background: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.12);
            border: 1px solid #e9ecef;
            position: relative;
            overflow: hidden;
        }
        
        .data-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, #28a745, #20c997, #17a2b8);
            background-size: 200% 100%;
            animation: gradientShift 4s ease infinite;
        }
        
        .stDataFrame {
            border: none;
        }
        
        .stDataFrame > div {
            border-radius: 15px;
            overflow: hidden;
            border: 1px solid #e9ecef;
        }
        
        .stSelectbox > div > div {
            background: white;
            border-radius: 10px;
            border: 2px solid #e9ecef;
            transition: all 0.3s ease;
        }
        
        .stSelectbox > div > div:hover {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        
        .info-card {
            background: linear-gradient(135deg, #d1ecf1 0%, #b8daff 100%);
            padding: 1rem;
            border-radius: 15px;
            border-left: 5px solid #17a2b8;
            margin: 1rem 0;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .warning-card {
            background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
            padding: 1rem;
            border-radius: 15px;
            border-left: 5px solid #ffc107;
            margin: 1rem 0;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .metric-card {
            background: linear-gradient(135deg, #e8f5e8 0%, #d4edda 100%);
            padding: 1rem;
            border-radius: 15px;
            text-align: center;
            border: 1px solid #c3e6cb;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .pulse {
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.02); }
            100% { transform: scale(1); }
        }
        </style>
    ''', unsafe_allow_html=True)
    
    st.markdown('''
        <div class="header-gradient fade-in">
            <h1 class="main-title" style="color: white; -webkit-text-fill-color: white; margin-bottom: 1rem;">Data Transaksi</h1>
        </div>
    ''', unsafe_allow_html=True)

def css_datacontainer():
    st.markdown('''
        <style>
            .data-container {
                height: 60px;
                display: flex;
                justify-content: center;  /* Tengahin horizontal */
                align-items: center;      /* Tengahin vertikal */
                background-color: white;
                border-radius: 10px;
                box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
                margin-top: 20px;         /* Jarak atas */
                margin-bottom: 30px;      /* Jarak bawah */
            }
            .data-container h3 {
                font-size: 24px;
                margin: 0;
                text-align: center;
            }
        </style>
    ''', unsafe_allow_html=True)

    st.markdown('''
        <div class="data-container fade-in">
            <h3>Detail Transaksi</h3>
        </div>
    ''', unsafe_allow_html=True)

def css_pagination_controls():
    st.markdown("""
    <style>
    .pagination-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 10px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

def css_loket():
    st.markdown("""
    <style>
    /* Main container styling */
    .main-container {
        background: linear-gradient(135deg, #003d82 0%, #0056b8 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    /* Header styling */
    .header-title {
        background: linear-gradient(45deg, #003d82, #0056b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Section headers */
    .section-header {
    background: linear-gradient(90deg, #003d82, #0056b8, #0066cc);
    color: white;
    padding: 0.5rem 1rem;              /* kurangi padding atas bawah */
    border-radius: 15px;
    margin: 0.5rem 0 -2rem 0;         /* margin atas & bawah kecilin */
    text-align: center;
    font-weight: 700;
    font-size: 1.3rem;
    box-shadow: 0 3px 8px rgba(0,0,0,0.15);  /* kecilin shadow */
    border: 2px solid rgba(255,255,255,0.3);
    }

    
    /* Form container */
    .form-container {
        background: rgba(255,255,255,0.95);
        padding: 2rem;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        margin: 1rem 0;
    }
    
    /* Input styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        background: rgba(255,255,255,0.9) !important;
        border: 1px solid #4a5568 !important;
        border-radius: 10px !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #003d82 !important;
        box-shadow: 0 0 0 3px rgba(0,61,130,0.1) !important;
        transform: translateY(-1px) !important;
    }
    
    /* Label styling */
    .stTextInput > label,
    .stTextArea > label,
    .stSelectbox > label {
        color: #4a5568 !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Submit button styling */
    .stFormSubmitButton > button {
        background: linear-gradient(45deg, #003d82, #0056b8) !important;
        color: white !important;
        border: none !important;
        padding: 1rem 3rem !important;
        border-radius: 25px !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        margin-top: 2rem !important;
    }
    
    .stFormSubmitButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3) !important;
        background: linear-gradient(45deg, #0056b8, #0066cc) !important;
    }
    
    /* Success/Warning message styling */
    .stSuccess, .stWarning {
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 1rem !important;
        margin: 1rem 0 !important;
    }
    
    /* Card effect for sections */
    .info-card {
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255,255,255,0.2);
        backdrop-filter: blur(5px);
    }
    
    /* Animated icons */
    .icon {
        font-size: 2rem;
        margin-right: 1rem;
        vertical-align: middle;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .header-title {
            font-size: 2rem;
        }
        .section-header {
            font-size: 1.1rem;
            padding: 0.8rem 1.5rem;
        }
        .form-container {
            padding: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def css_footer_loket():
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem; padding: 1rem; 
                background: rgba(255,255,255,0.1); border-radius: 10px;
                border: 1px solid rgba(255,255,255,0.2);">
        <p style="color: #4a5568; font-weight: 500;">
            <strong>Catatan:</strong> Pastikan semua data yang dimasukkan sudah benar sebelum menyimpan
        </p>
    </div>
    """, unsafe_allow_html=True)

def load_css_sidebar():
    st.markdown("""
    <style>
    .css-1d391kg {
        width: 21rem;
    }
    .css-1544g2n {
        width: 21rem;
    }
    section[data-testid="stSidebar"] {
        width: 280px !important;
    }
    section[data-testid="stSidebar"] > div {
        width: 280px !important;
    }
    .css-17eq0hr {
        width: 280px !important;
    }
    
    /* Toast notification untuk welcome message */
    .welcome-toast {
        position: fixed;
        top: 20px;
        right: 20px;
        background: rgba(0, 0, 0, 0.85);
        color: white;
        padding: 12px 18px;
        border-radius: 8px;
        border-left: 3px solid #4CAF50;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        z-index: 9999;
        animation: slideInRight 0.5s ease, fadeOut 0.5s ease 2.5s forwards;
        font-size: 14px;
        max-width: 300px;
    }
    
    .welcome-name {
        font-weight: 600;
        margin-bottom: 2px;
    }
    
    .welcome-role {
        font-size: 12px;
        opacity: 0.8;
    }
    
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes fadeOut {
        to {
            opacity: 0;
            transform: translateX(100%);
        }
    }
    
    .menu-title {
        color: #1f4e79;
        font-size: 16px;
        font-weight: 600;
        margin-bottom: 20px;
        text-align: left;
        padding: 0;
        border: none;
    }
    
    /* Simple Menu Buttons */
    .menu-btn {
        display: flex;
        align-items: center;
        width: 100%;
        padding: 12px 16px;
        margin: 6px 0;
        background: #ffffff;
        border: 1px solid #e0e6ed;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s ease;
        text-decoration: none;
        color: #374151;
        font-size: 14px;
        font-weight: 500;
    }
    
    .menu-btn:hover {
        background: #f8fafc;
        border-color: #3b82f6;
        color: #3b82f6;
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(59, 130, 246, 0.15);
    }
    
    .menu-btn.active {
        background: #3b82f6;
        border-color: #3b82f6;
        color: white;
        box-shadow: 0 2px 12px rgba(59, 130, 246, 0.25);
    }
    
    .menu-btn.active:hover {
        background: #2563eb;
        border-color: #2563eb;
        color: white;
    }
    
    .menu-icon {
        margin-right: 12px;
        display: flex;
        align-items: center;
    }
    
    .menu-icon svg {
        width: 20px;
        height: 20px;
    }
    
    .menu-text {
        flex: 1;
    }
    </style>
    """, unsafe_allow_html=True)

def css_loket1():
   st.markdown("""
    <style>
    .form-header {
        background: linear-gradient(135deg, #2E3192 0%, #1E88E5 100%);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 30px;
        text-align: center;
        color: white;
    }
    .form-header h1 {
        font-size: 2.5rem;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .form-header p {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    .form-section {
        background: #3366CC;
        padding: 15px 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        color: white;
        font-weight: bold;
        text-align: center;
        font-size: 1.2rem;
    }
    .stSelectbox > div > div > div {
        background-color: #f8f9fa;
    }
    .address-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        margin-bottom: 20px;
    }
    @media (max-width: 768px) {
        .address-container {
            grid-template-columns: 1fr;
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
def css_header_loket():
    st.markdown("""
    <div class="form-header">
        <h1>SISTEM LOKET TERPADU</h1>
        <p>Input data pengiriman dengan mudah dan cepat</p>
    </div>
    """, unsafe_allow_html=True)