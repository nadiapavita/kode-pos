# receipt_generator.py - Improved version with better form layout
import streamlit as st
import streamlit.components.v1 as components
import random
import datetime
from pymongo import MongoClient
from css import css_loket1, css_header_loket

def sensor_phone(phone_number):
    """Sensor nomor telepon, tampilkan hanya 3 digit pertama dan 2 digit terakhir"""
    if len(phone_number) > 5:
        return phone_number[:3] + "*" * (len(phone_number) - 5) + phone_number[-2:]
    return phone_number

def generate_receipt_html(transaction_data):
    """Generate HTML receipt yang sama persis dengan versi HTML"""
    data = transaction_data['data']
    selected_layanan = transaction_data['selected_layanan']
    nomor_resi = transaction_data['nomor_resi']
    
    # Real mitra logos with actual URLs
    mitra_logos = [
        {
            "name": "Shopee", 
            "color": "#EE4D2D", 
            "bg": "#FFF0ED",
            "logo_url": "https://logospng.org/wp-content/uploads/shopee.png"
        },
        {
            "name": "TikTok Shop", 
            "color": "#000000", 
            "bg": "#F5F5F5",
            "logo_url": "https://get-picto.com/wp-content/uploads/2024/02/tiktok-shop-logo-png-800x800.webp"
        },
        {
            "name": "Lazada", 
            "color": "#FF6600", 
            "bg": "#FFF5E6",
            "logo_url": "https://www.liblogo.com/img-logo/la8780l1ef-lazada-logo-lazada-group-large-image-download-pr-newswire.png"
        },
        {
            "name": "Bukalapak", 
            "color": "#E31E24", 
            "bg": "#FFF0F0",
            "logo_url": "https://vectorseek.com/wp-content/uploads/2023/07/Bukalapak-Logo-Vector.svg-.png"
        }
    ]
    selected_mitra = random.choice(mitra_logos)
    
    # Generate more realistic barcode
    barcode_lines = []
    for i in range(50):
        if i % 5 == 0:
            barcode_lines.append("|||")
        elif i % 3 == 0:
            barcode_lines.append("||")
        else:
            barcode_lines.append("|")
    barcode_display = " ".join(barcode_lines)

    return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Resi POS Indonesia - {nomor_resi}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ 
            font-family: 'Arial', 'Segoe UI', sans-serif; 
            font-size: 12px; 
            line-height: 1.2; 
            color: #2c2c2c; 
            background: #f8f9fa; 
            padding: 8px; 
        }}
        .receipt-container {{ 
            border: 2px solid #d32f2f; 
            max-width: 800px; 
            margin: 0 auto; 
            background: white; 
            box-shadow: 0 4px 16px rgba(0,0,0,0.1); 
            border-radius: 8px; 
            overflow: hidden; 
            position: relative;
        }}
        .receipt-container::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #d32f2f 0%, #ff5722 50%, #d32f2f 100%);
        }}
        .receipt-header {{ 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            padding: 15px 20px; 
            background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%); 
            border-bottom: 2px solid #d32f2f; 
            position: relative;
            gap: 15px;
        }}
        .header-left {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex: 1;
        }}
        .pos-logo-container {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .pos-main-logo {{
            width: 50px;
            height: 38px;
            object-fit: contain;
        }}
        .pos-text {{
            display: flex;
            flex-direction: column;
        }}
        .pos-title {{ 
            color: #d32f2f; 
            font-weight: 900; 
            font-size: 20px; 
            letter-spacing: -0.5px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }}
        .pos-subtitle {{ 
            color: #ff5722; 
            font-size: 10px; 
            font-weight: 600; 
            margin-top: -2px;
            font-style: italic;
        }}
        .mitra-section {{
            display: flex;
            align-items: center;
            gap: 8px;
            background: {selected_mitra['bg']}; 
            padding: 8px 12px; 
            border-radius: 15px; 
            border: 1px solid {selected_mitra['color']}; 
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}
        .mitra-logo {{
            width: 24px;
            height: 24px;
            object-fit: contain;
        }}
        .mitra-text {{
            color: {selected_mitra['color']}; 
            font-weight: bold; 
            font-size: 10px; 
        }}
        .receipt-number {{ 
            background: #d32f2f;
            color: white;
            padding: 8px 12px;
            border-radius: 6px;
            font-weight: bold; 
            font-size: 13px; 
            box-shadow: 0 2px 8px rgba(211, 47, 47, 0.25);
            letter-spacing: 0.3px;
        }}
        .receipt-content {{ 
            display: flex; 
            min-height: 400px; 
        }}
        .left-panel {{ 
            flex: 2.2; 
            padding: 15px; 
            background: linear-gradient(180deg, #fafafa 0%, #f5f5f5 100%); 
        }}
        .right-panel {{ 
            flex: 1; 
            border-left: 2px solid #d32f2f; 
            padding: 15px; 
            background: white; 
            position: relative;
        }}
        .right-panel::before {{
            content: '';
            position: absolute;
            left: -1px;
            top: 0;
            bottom: 0;
            width: 1px;
            background: linear-gradient(180deg, transparent 0%, #d32f2f 20%, #d32f2f 80%, transparent 100%);
        }}
        .info-section {{ 
            background: white; 
            border: 1px solid #e0e0e0; 
            border-radius: 8px; 
            margin-bottom: 12px; 
            overflow: hidden; 
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            transition: all 0.3s ease;
        }}
        .info-section:hover {{
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        .section-title {{ 
            background: linear-gradient(135deg, #d32f2f 0%, #b71c1c 100%); 
            color: white; 
            padding: 8px 12px; 
            font-weight: bold; 
            font-size: 11px; 
            text-transform: uppercase; 
            letter-spacing: 0.5px;
            position: relative;
        }}
        .section-title::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent 0%, rgba(255,255,255,0.3) 50%, transparent 100%);
        }}
        .section-content {{ 
            padding: 12px; 
            line-height: 1.4; 
        }}
        .field-label {{ 
            font-weight: 700; 
            color: #424242; 
            display: block; 
            margin-bottom: 3px; 
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 0.3px;
        }}
        .field-value {{ 
            color: #1a1a1a; 
            margin-bottom: 10px; 
            word-wrap: break-word; 
            font-size: 11px;
            font-weight: 500;
            padding: 5px 8px;
            background: #f8f9fa;
            border-radius: 4px;
            border-left: 3px solid #d32f2f;
        }}
        .routing-display {{ 
            background: linear-gradient(135deg, #1976d2 0%, #1565c0 100%); 
            color: white; 
            border-radius: 12px; 
            padding: 15px; 
            text-align: center; 
            margin: 12px 0; 
            box-shadow: 0 4px 12px rgba(25, 118, 210, 0.25);
            position: relative;
            overflow: hidden;
        }}
        .routing-display::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: shimmer 3s infinite;
        }}
        @keyframes shimmer {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
        .routing-code {{ 
            font-size: 18px; 
            font-weight: 900; 
            position: relative;
            z-index: 1;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        }}
        .routing-label {{
            font-size: 9px; 
            margin-top: 5px;
            opacity: 0.9;
            font-weight: 600;
            letter-spacing: 0.5px;
            position: relative;
            z-index: 1;
        }}
        .barcode {{ 
            text-align: center; 
            margin: 12px 0; 
            background: #f8f9fa;
            padding: 10px;
            border-radius: 6px;
            border: 1px dashed #d32f2f;
        }}
        .barcode-image {{
            width: 100%;
            max-width: 120px;
            height: auto;
            object-fit: contain;
        }}
        .barcode-text {{
            font-family: 'Courier New', monospace;
            font-size: 8px;
            color: #666;
            margin-top: 5px;
            letter-spacing: 0.5px;
        }}
        .price-info {{ 
            background: linear-gradient(135deg, #e8f5e8 0%, #c8e6c9 100%); 
            border: 1px solid #4caf50; 
            padding: 12px; 
            border-radius: 12px; 
            text-align: center; 
            margin: 12px 0; 
            box-shadow: 0 2px 10px rgba(76, 175, 80, 0.15);
        }}
        .price-label {{
            font-size: 10px; 
            margin-bottom: 5px;
            color: #2e7d32;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.3px;
        }}
        .price-amount {{ 
            font-size: 16px; 
            font-weight: 900; 
            color: #1b5e20; 
            text-shadow: 0.5px 0.5px 1px rgba(0,0,0,0.1);
        }}
        .additional-info {{
            background: #f8f9fa;
            padding: 10px;
            border-radius: 8px;
            margin-top: 15px;
            border: 1px solid #e0e0e0;
        }}
        .additional-info p {{
            margin-bottom: 5px;
            font-size: 9px;
            color: #555;
        }}
        .additional-info strong {{
            color: #d32f2f;
            font-weight: 700;
        }}
        .footer-info {{ 
            background: linear-gradient(135deg, #d32f2f 0%, #b71c1c 100%); 
            color: white;
            padding: 12px 20px; 
            font-size: 10px; 
        }}
        .footer-content {{
            display: flex; 
            justify-content: space-between; 
            align-items: center;
        }}
        .footer-brand {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .footer-logo {{
            width: 24px;
            height: 18px;
            object-fit: contain;
        }}
        .footer-text {{
            font-weight: bold;
            font-size: 11px;
        }}
        .footer-slogan {{
            font-style: italic;
            opacity: 0.9;
            margin-top: 1px;
            font-size: 9px;
        }}
        .footer-buttons {{
            display: flex;
            gap: 8px;
        }}
        .footer-btn {{
            padding: 6px 12px; 
            border-radius: 6px; 
            cursor: pointer; 
            font-weight: 600;
            font-size: 10px;
            border: none;
            transition: all 0.3s ease;
            text-transform: uppercase;
            letter-spacing: 0.3px;
        }}
        .btn-print {{
            background: #ff9800; 
            color: white; 
        }}
        .btn-print:hover {{
            background: #f57c00;
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(255, 152, 0, 0.3);
        }}
        .watermark {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-45deg);
            font-size: 80px;
            color: rgba(211, 47, 47, 0.025);
            font-weight: 900;
            z-index: 0;
            pointer-events: none;
            user-select: none;
        }}
        
        /* PRINT STYLES - Improved for consistent appearance */
        @media print {{
            @page {{
                size: A4;
                margin: 0.5in;
            }}
            
            body {{ 
                background: white !important; 
                padding: 0 !important; 
                font-size: 11px !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }}
            
            .receipt-container {{ 
                border: 2px solid #333 !important; 
                box-shadow: none !important; 
                border-radius: 0 !important; 
                max-width: none !important;
                margin: 0 !important;
                page-break-inside: avoid !important;
            }}
            
            .receipt-header {{
                padding: 12px 15px !important;
                border-bottom: 2px solid #333 !important;
                background: white !important;
            }}
            
            .pos-title {{
                color: #333 !important;
                font-size: 18px !important;
            }}
            
            .pos-subtitle {{
                color: #666 !important;
            }}
            
            .receipt-number {{
                background: #333 !important;
                color: white !important;
                font-size: 12px !important;
            }}
            
            .receipt-content {{
                min-height: auto !important;
            }}
            
            .left-panel {{
                padding: 12px !important;
                background: white !important;
            }}
            
            .right-panel {{
                padding: 12px !important;
                border-left: 2px solid #333 !important;
            }}
            
            .section-title {{
                background: #333 !important;
                color: white !important;
                padding: 6px 10px !important;
                font-size: 10px !important;
            }}
            
            .section-content {{
                padding: 10px !important;
            }}
            
            .field-value {{
                font-size: 10px !important;
                padding: 3px 6px !important;
                background: #f5f5f5 !important;
                border-left: 2px solid #333 !important;
            }}
            
            .routing-display {{
                background: #333 !important;
                color: white !important;
                padding: 12px !important;
            }}
            
            .routing-code {{
                font-size: 16px !important;
            }}
            
            .routing-label {{
                font-size: 8px !important;
            }}
            
            .price-info {{
                background: #f0f0f0 !important;
                border: 2px solid #333 !important;
                padding: 10px !important;
            }}
            
            .price-label {{
                color: #333 !important;
                font-size: 9px !important;
            }}
            
            .price-amount {{
                color: #000 !important;
                font-size: 14px !important;
            }}
            
            .footer-info {{
                background: #333 !important;
                color: white !important;
                padding: 10px 15px !important;
            }}
            
            .footer-buttons {{ 
                display: none !important; 
            }}
            
            .watermark {{
                font-size: 60px !important;
                color: rgba(0,0,0,0.03) !important;
            }}
            
            .info-section {{
                break-inside: avoid !important;
                margin-bottom: 8px !important;
            }}
            
            .barcode {{
                padding: 8px !important;
                border: 1px solid #333 !important;
            }}
            
            .barcode-image {{
                max-width: 100px !important;
            }}
            
            .additional-info {{
                background: #f5f5f5 !important;
                padding: 8px !important;
            }}
            
            .mitra-section {{
                background: #f0f0f0 !important;
                border: 1px solid #666 !important;
            }}
        }}
    </style>
    <script>
        function printReceipt() {{
            window.print();
        }}
        
        function downloadReceipt() {{
            const element = document.createElement('a');
            const file = new Blob([document.documentElement.outerHTML], {{type: 'text/html'}});
            element.href = URL.createObjectURL(file);
            element.download = 'resi_{nomor_resi}.html';
            document.body.appendChild(element);
            element.click();
            document.body.removeChild(element);
        }}
    </script>
</head>
<body>
    <div class="receipt-container">
        <div class="watermark">POS INDONESIA</div>
        
        <!-- Header -->
        <div class="receipt-header">
            <div class="header-left">
                <div class="pos-logo-container">
                    <img src="https://media.suara.com/pictures/970x544/2023/09/07/89962-pos-ind-logistik.jpg" 
                         alt="POS Indonesia" class="pos-main-logo" 
                         onerror="this.style.display='none'">
                    <div class="pos-text">
                        <div class="pos-title">POS INDONESIA</div>
                        <div class="pos-subtitle">Connecting People & Places</div>
                    </div>
                </div>
                <div class="mitra-section">
                    <img src="{selected_mitra['logo_url']}" 
                         alt="{selected_mitra['name']}" class="mitra-logo"
                         onerror="this.style.display='none'">
                    <div class="mitra-text">MITRA<br>{selected_mitra['name'].upper()}</div>
                </div>
            </div>
            <div class="receipt-number">RESI: {nomor_resi}</div>
        </div>

        <!-- Content -->
        <div class="receipt-content">
            <!-- Left Panel -->
            <div class="left-panel">
                <!-- Pengirim -->
                <div class="info-section">
                    <div class="section-title">Data Pengirim</div>
                    <div class="section-content">
                        <span class="field-label">Nama Lengkap:</span>
                        <div class="field-value">{data['pengirim']['nama']}</div>
                        <span class="field-label">Alamat Lengkap:</span>
                        <div class="field-value">{data['pengirim']['alamat']}</div>
                        <span class="field-label">Kode Pos:</span>
                        <div class="field-value">{data['pengirim']['kodepos']}</div>
                        <span class="field-label">No. Handphone:</span>
                        <div class="field-value">{sensor_phone(data['pengirim']['no_hp'])}</div>
                    </div>
                </div>

                <!-- Penerima -->
                <div class="info-section">
                    <div class="section-title">Data Penerima</div>
                    <div class="section-content">
                        <span class="field-label">Nama Lengkap:</span>
                        <div class="field-value">{data['penerima']['nama']}</div>
                        <span class="field-label">Alamat Lengkap:</span>
                        <div class="field-value">{data['penerima']['alamat']}</div>
                        <span class="field-label">Kode Pos:</span>
                        <div class="field-value">{data['penerima']['kodepos']}</div>
                        <span class="field-label">No. Handphone:</span>
                        <div class="field-value">{sensor_phone(data['penerima']['no_hp'])}</div>
                    </div>
                </div>

                <!-- Layanan -->
                <div class="info-section">
                    <div class="section-title">Detail Layanan & Transaksi</div>
                    <div class="section-content">
                        <span class="field-label">Jenis Layanan:</span>
                        <div class="field-value">{data['layanan']['nama_layanan']}</div>
                        <span class="field-label">Tanggal Posting:</span>
                        <div class="field-value">{data.get('tanggal_posting', datetime.datetime.now().strftime('%d-%b-%Y'))}</div>
                        <span class="field-label">Waktu Posting:</span>
                        <div class="field-value">{data.get('waktu_posting', datetime.datetime.now().strftime('%H:%M:%S'))}</div>
                        <span class="field-label">Status:</span>
                        <div class="field-value">✅ TERDAFTAR & DIPROSES</div>
                    </div>
                </div>
            </div>

            <!-- Right Panel -->
            <div class="right-panel">
                <!-- Routing -->
                <div class="routing-display">
                    <div class="routing-code">{data['pengirim']['kodepos']} ➤ {data['penerima']['kodepos']}</div>
                    <div class="routing-label">KODE ROUTING OTOMATIS</div>
                </div>

                <!-- Barcode -->
                <div class="barcode">
                    <div style="font-weight: bold; margin-bottom: 8px; color: #d32f2f; font-size: 10px;">BARCODE TRACKING</div>
                    <img src="https://tse1.mm.bing.net/th/id/OIP.Qitxc4XNDuOlrmxzfvRr5AHaE8?r=0&w=1000&h=667&rs=1&pid=ImgDetMain&o=7&rm=3" 
                         alt="Barcode" class="barcode-image"
                         onerror="this.style.display='none'">
                    <div class="barcode-text">
                        {nomor_resi}
                    </div>
                    <div style="font-size: 8px; color: #666; margin-top: 3px;">
                        Scan untuk tracking otomatis
                    </div>
                </div>

                <!-- Price -->
                <div class="price-info">
                    <div class="price-label">Total Biaya Pengiriman</div>
                    <div class="price-amount">Rp {data['layanan']['tarif']:,}</div>
                    <div style="font-size: 9px; margin-top: 5px; color: #2e7d32;">
                        *Sudah termasuk biaya administrasi
                    </div>
                </div>

                <!-- Additional Info -->
                <div class="additional-info">
                    <p><strong>👤 Petugas Input:</strong><br>{data.get('diinput_oleh', {}).get('nama', 'Admin')}</p>
                    <p><strong>🏢 Kantor Cabang:</strong><br>{data.get('diinput_oleh', {}).get('cabang', 'Jakarta Pusat')}</p>
                    <p><strong>🎯 Estimasi Tiba:</strong><br>2-5 Hari Kerja*</p>
                    <p style="font-size: 8px; margin-top: 8px; color: #999;">
                        *Estimasi dapat berbeda tergantung kondisi cuaca dan hari libur
                    </p>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer-info">
            <div class="footer-content">
                <div class="footer-brand">
                    <img src="https://media.suara.com/pictures/970x544/2023/09/07/89962-pos-ind-logistik.jpg" 
                         alt="POS" class="footer-logo"
                         onerror="this.style.display='none'">
                    <div>
                        <div class="footer-text">POS INDONESIA</div>
                        <div class="footer-slogan">Connecting Indonesia, Delivering Dreams</div>
                    </div>
                </div>
                <div class="footer-buttons">
                    <button onclick="printReceipt()" class="footer-btn btn-print">🖨️ Cetak Resi</button>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

def show_receipt_in_streamlit(transaction_data):
    """Tampilkan resi HTML di dalam Streamlit menggunakan components.html"""
    html_content = generate_receipt_html(transaction_data)
    components.html(html_content, height=700, scrolling=True)

def create_receipt_download_button(transaction_data):
    """Generate HTML content untuk download button"""
    html_content = generate_receipt_html(transaction_data)
    filename = f"resi_{transaction_data['nomor_resi']}.html"
    return html_content, filename

def loket_page():
    css_loket1()
    css_header_loket()
    client = MongoClient("mongodb+srv://masukannamatemananda:masukanpasswordtemananda@posindo.5juwxxh.mongodb.net/")
    db = client["pos_indonesia"]
    loket_collection = db["loket"]
    tarif_pos_collection = db["tarif_pos"]

    # Initialize session state
    if 'clear_form' not in st.session_state:
        st.session_state.clear_form = False
    if 'success_message' not in st.session_state:
        st.session_state.success_message = None
    if "form_counter" not in st.session_state:
        st.session_state.form_counter = 0
    form_key = f"form_loket_{st.session_state.form_counter}"
        
    # Clear form jika flag True
    if st.session_state.clear_form:
        st.session_state.clear_form = False
        for key in list(st.session_state.keys()):
            if key.startswith('loket_'):
                del st.session_state[key]
        if 'show_receipt' in st.session_state:
            del st.session_state.show_receipt

    # Form Input dengan layout yang diperbaiki  
    st.markdown('<div class="form-section">Form Input Data Pengiriman</div>', unsafe_allow_html=True)
    
    with st.form(form_key):
        # Data Pengirim
        st.markdown('<div class="form-section">Data Pengirim</div>', unsafe_allow_html=True)
        nama_pengirim = st.text_input("Nama Pengirim", placeholder="Masukkan nama lengkap pengirim", key="loket_nama_pengirim")
        no_hp_pengirim = st.text_input("No HP Pengirim", placeholder="Contoh: 08123456789", key="loket_no_hp_pengirim")
        alamat_pengirim = st.text_area("Alamat Pengirim", placeholder="Masukkan alamat lengkap pengirim", height=100, key="loket_alamat_pengirim")
        kodepos_pengirim = st.text_input("Kodepos Pengirim", placeholder="Contoh: 12345", key="loket_kodepos_pengirim")

        # Data Penerima
        st.markdown('<div class="form-section">Data Penerima</div>', unsafe_allow_html=True)
        nama_penerima = st.text_input("Nama Penerima", placeholder="Masukkan nama lengkap penerima", key="loket_nama_penerima")
        no_hp_penerima = st.text_input("No HP Penerima", placeholder="Contoh: 08987654321", key="loket_no_hp_penerima")
        alamat_penerima = st.text_area("Alamat Penerima", placeholder="Masukkan alamat lengkap penerima", height=100, key="loket_alamat_penerima")
        kodepos_penerima = st.text_input("Kodepos Penerima", placeholder="Contoh: 54321", key="loket_kodepos_penerima")
        
        # Form Isi Kiriman
        st.markdown('<div class="form-section">Detail Kiriman</div>', unsafe_allow_html=True)
        jenis_kiriman = st.selectbox(
            "Jenis Kiriman",
            options=["Dokumen", "Pakaian", "Elektronik", "Makanan", "Obat-obatan", "Buku", "Aksesoris", "Lainnya"],
            index=None,
            placeholder="Pilih jenis kiriman",
            key="loket_jenis_kiriman"
        )
        isi_kiriman = st.text_area("Deskripsi Isi Kiriman", placeholder="Jelaskan detail isi kiriman (contoh: Baju kaos warna merah ukuran L)", height=80, key="loket_isi_kiriman")
        berat_kiriman = st.number_input("Berat Kiriman (gram)", min_value=1, max_value=30000, step=1, placeholder="Masukkan berat dalam gram", key="loket_berat_kiriman")

        # Pilihan Layanan
        st.markdown('<div class="form-section">Pilihan Layanan</div>', unsafe_allow_html=True)
        layanan_options = {}
        layanan_pengirim = None

        if kodepos_pengirim and kodepos_penerima:
            doc = tarif_pos_collection.find_one({
                "asal": kodepos_pengirim,
                "tujuan": kodepos_penerima
            })
            if doc and "layanan" in doc:
                for layanan in doc["layanan"]:
                    # Hitung tarif berdasarkan berat (per kilo, dibulatkan ke atas)
                    import math
                    berat_kg = math.ceil(berat_kiriman / 1000) if berat_kiriman else 1
                    total_tarif = layanan['tarif'] * berat_kg
                    display_text = f"{layanan['nama_layanan']} - Rp {total_tarif:,}"
                    if layanan.get('estimasi'):
                        display_text += f" ({layanan['estimasi']})"
                    layanan_options[display_text] = {
                        'nama': layanan['nama_layanan'],
                        'tarif': total_tarif,
                        'estimasi': layanan.get('estimasi', ''),
                        'catatan': layanan.get('catatan', '')
                    }
                layanan_pengirim = st.selectbox(
                    "Pilih Layanan",
                    options=list(layanan_options.keys()),
                    index=None,
                    placeholder="Pilih jenis layanan",
                    key="loket_layanan_pengirim"
                )
                if layanan_pengirim:
                    selected_service = layanan_options[layanan_pengirim]
                    st.info(f"Tarif: Rp {selected_service['tarif']:,}")
                    if selected_service['estimasi']:
                        st.info(f"Estimasi: {selected_service['estimasi']}")
                    if selected_service['catatan']:
                        st.warning(f"Catatan: {selected_service['catatan']}")
            else:
                st.warning("Tidak ada layanan untuk kombinasi kodepos ini.")
        else:
            st.info("Isi kodepos pengirim & penerima untuk melihat layanan yang tersedia.")

        # Submit buttons
        col1 = st.columns(1)[0]
        with col1:
            submitted = st.form_submit_button("SIMPAN DATA", use_container_width=True, type="primary")

        # Process form submission
        if submitted:
            if all([nama_pengirim, alamat_pengirim, kodepos_pengirim, no_hp_pengirim,
                   layanan_pengirim, nama_penerima, alamat_penerima, kodepos_penerima, no_hp_penerima,
                   jenis_kiriman, isi_kiriman, berat_kiriman]):
                
                identitas_yang_input = {
                    "nama": st.session_state.get('username', 'Admin'),
                    "role": st.session_state.get('role', 'Operator'),
                    "cabang": st.session_state.get('cabang', 'Jakarta Pusat')
                }
                
                selected_layanan = layanan_options[layanan_pengirim]
                nomor_resi = f"PID{random.randint(10000, 99999)}PKH{datetime.datetime.now().strftime('%Y%m%d')}{random.randint(1000, 9999)}.1"
                
                data = {
                    "pengirim": {
                        "nama": nama_pengirim,
                        "alamat": alamat_pengirim,
                        "kodepos": kodepos_pengirim,
                        "no_hp": no_hp_pengirim
                    },
                    "penerima": {
                        "nama": nama_penerima,
                        "alamat": alamat_penerima,
                        "kodepos": kodepos_penerima,
                        "no_hp": no_hp_penerima
                    },
                    "kiriman": {
                        "jenis": jenis_kiriman,
                        "isi": isi_kiriman,
                        "berat": berat_kiriman
                    },
                    "layanan": {
                        "nama_layanan": selected_layanan['nama'],
                        "tarif": selected_layanan['tarif']
                    },
                    "diinput_oleh": identitas_yang_input,
                    "nomor_resi": nomor_resi,
                    "tanggal_posting": datetime.datetime.now().strftime("%d-%b-%Y"),
                    "waktu_posting": datetime.datetime.now().strftime("%H:%M:%S")
                }
                
                try:
                    result = loket_collection.insert_one(data)
                    
                    st.session_state.last_transaction = {
                        "id": str(result.inserted_id),
                        "nomor_resi": nomor_resi,
                        "data": data,
                        "selected_layanan": selected_layanan
                    }
                    
                    st.success(f"Data berhasil disimpan! Nomor Resi: **{nomor_resi}**")
                    st.session_state.show_input_lagi = True
                    # st.session_state.clear_form = True
                    # st.rerun()
                    
                except Exception as e:
                    st.error(f"Error menyimpan data: {str(e)}")
            else:
                st.error("Semua field harus diisi! Pastikan jenis kiriman, isi kiriman, dan berat kiriman telah diisi.")
    
    if st.session_state.get("show_input_lagi", False):
        if st.button("Input Lagi"):
            st.session_state.show_input_lagi = False
            st.session_state.form_counter += 1
            st.rerun()
            
    # Tampilkan tombol resi setelah berhasil simpan
    if 'last_transaction' in st.session_state:
        st.markdown("---")
        col1 = st.columns(1)[0]
        
        with col1:
            if st.button("Lihat Resi", use_container_width=True, type="primary"):
                st.session_state.show_receipt = True

    # Tampilkan resi jika diminta
    if st.session_state.get('show_receipt', False) and 'last_transaction' in st.session_state:
        st.markdown("---")
        st.subheader("Resi POS Indonesia")
        
        if st.button("Tutup Preview", key="close_receipt"):
            # Clear form fields when closing preview
            st.session_state.clear_form = True
            del st.session_state.show_receipt
            if 'last_transaction' in st.session_state:
                del st.session_state.last_transaction
            st.rerun()
            
        show_receipt_in_streamlit(st.session_state.last_transaction)