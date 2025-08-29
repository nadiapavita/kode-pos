import streamlit as st
def load_css_login():
  st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    .main {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #3b82f6 100%);
        font-family: 'Poppins', sans-serif;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1rem;
    }

    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 450px !important;
        margin: 0 auto !important;
    }

    /* Compact Header */
    .compact-header {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .compact-header h1 {
        color: white;
        font-size: 2rem;
        font-weight: 700;
        margin: 0 0 0.5rem 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    .compact-header p {
        color: rgba(255,255,255,0.9);
        font-size: 0.9rem;
        margin: 0;
        font-weight: 400;
    }

    /* Compact Login Container */
    .compact-login-container {
        max-width: 400px;
        margin: 0 auto;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 20px 40px rgba(30, 60, 114, 0.2);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        position: relative;
        overflow: hidden;
    }

    .compact-login-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #1e3c72, #2a5298, #3b82f6);
    }

    /* Compact Form Title */
    .compact-form-title {
        text-align: center;
        color: #1e3c72;
        font-size: 1.6rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .compact-form-subtitle {
        text-align: center;
        color: #64748b;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
        font-weight: 400;
    }

    /* Compact Form Styling */
    .stTextInput > div > div > input {
        background: rgba(248, 250, 252, 0.8) !important;
        border: 1.5px solid rgba(30, 60, 114, 0.2) !important;
        border-radius: 12px !important;
        transition: all 0.3s ease !important;
        font-weight: 500 !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.95rem !important;
        box-sizing: border-box !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: #9ca3af !important;
        font-weight: 400 !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #2a5298 !important;
        box-shadow: 0 0 0 3px rgba(30, 60, 114, 0.1) !important;
        outline: none !important;
    }

    .stTextInput label {
        font-weight: 600 !important;
        color: #1e3c72 !important;
        font-size: 0.9rem !important;
        margin-bottom: 0.4rem !important;
    }

    /* Compact Button Styling */
    .stButton > button,
    .stFormSubmitButton > button {
        background: linear-gradient(45deg, #1e3c72, #2a5298) !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        font-size: 0.95rem !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        margin: 0.5rem 0 !important;
        box-shadow: 0 6px 16px rgba(30, 60, 114, 0.3) !important;
        height: 2.8rem !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        background: linear-gradient(45deg, #153358, #1e3c72) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 8px 20px rgba(30, 60, 114, 0.4) !important;
    }

    /* Compact Secondary Button */
    .stButton button[kind="secondary"] {
        background: transparent !important;
        color: #1e3c72 !important;
        border: 1.5px solid #1e3c72 !important;
        font-weight: 500 !important;
    }

    .stButton button[kind="secondary"]:hover {
        background: #1e3c72 !important;
        color: white !important;
    }

    /* Compact Navigation Links */
    .compact-nav-links {
        margin-top: 1.5rem;
        display: flex;
        gap: 0.5rem;
    }

    .compact-nav-links .stButton {
        flex: 1;
    }

    .compact-nav-links .stButton > button {
        background: transparent !important;
        color: #2a5298 !important;
        border: 1.5px solid #2a5298 !important;
        font-size: 0.85rem !important;
        height: 2.5rem !important;
        font-weight: 500 !important;
    }

    .compact-nav-links .stButton > button:hover {
        background: #2a5298 !important;
        color: white !important;
    }

    /* Compact Messages */
    .stSuccess, .stError, .stWarning, .stInfo {
        border-radius: 12px !important;
        padding: 0.75rem 1rem !important;
        margin: 1rem 0 !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        text-align: center !important;
        border: none !important;
    }

    .stSuccess {
        background: linear-gradient(45deg, #10b981, #34d399) !important;
        color: white !important;
    }

    .stError {
        background: linear-gradient(45deg, #ef4444, #f87171) !important;
        color: white !important;
    }

    .stWarning {
        background: linear-gradient(45deg, #f59e0b, #fbbf24) !important;
        color: white !important;
    }

    .stInfo {
        background: linear-gradient(45deg, #1e3c72, #2a5298) !important;
        color: white !important;
    }

    /* Form spacing */
    .stForm {
        margin-bottom: 1rem;
    }

    .stForm > div {
        gap: 0.75rem;
    }

    /* Mobile Responsiveness */
    @media (max-width: 768px) {
        .block-container {
            max-width: 90% !important;
            padding: 0.5rem !important;
        }

        .compact-login-container {
            padding: 1.5rem;
        }

        .compact-header {
            padding: 1rem;
        }

        .compact-header h1 {
            font-size: 1.6rem;
        }

        .compact-form-title {
            font-size: 1.4rem;
        }
    }

    /* Hide streamlit default elements */
    .stDeployButton {
        display: none !important;
    }

    footer {
        display: none !important;
    }

    .stApp > header {
        display: none !important;
    }

    /* Animation */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .fade-in {
        animation: fadeInUp 0.6s ease-out;
    }

    /* Sidebar Styling (untuk setelah login) */
    .css-1d391kg {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
    }

    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1e3c72 0%, #2a5298 100%);
    }

    /* Main Content Card (untuk setelah login) */
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

    /* Title Styling (untuk setelah login) */
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

    /* Section Headers (untuk setelah login) */
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

    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }

    /* Result Cards (untuk setelah login) */
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

    /* Input Containers (untuk setelah login) */
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

    /* Search Card Styling (untuk setelah login) */
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

    /* Error and Info Cards (untuk setelah login) */
    .error-card {
        background: linear-gradient(135deg, #fee, #fdd);
        border: 2px solid #f87171;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 4px 15px rgba(248, 113, 113, 0.2);
    }

    .info-card {
        background: linear-gradient(135deg, #eff6ff, #dbeafe);
        border: 2px solid #60a5fa;
        border-radius: 15px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 4px 15px rgba(96, 165, 250, 0.2);
    }

    .info-card ul {
        list-style: none;
        padding-left: 0;
    }

    .info-card li {
        margin: 0.5rem 0;
        padding: 0.5rem;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 8px;
    }

    .error-card h2, .info-card h2 {
        margin-bottom: 1rem;
        color: #1f2937;
    }
    </style>
""", unsafe_allow_html=True)
