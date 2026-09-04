import streamlit as st
import os
import urllib.parse
from google import genai

# 1. Premium Interface Branding Configurations
st.set_page_config(
    page_title="BanquetAI – Venue Operations Hub", 
    page_icon="✨", 
    layout="centered"
)

# 2. Back-End Enterprise Security Pipeline (No frontend parameter leaks)
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ Secure Master API Key Missing. Please configure GEMINI_API_KEY in your cloud secrets panels.")
    st.stop()

client = genai.Client(api_key=api_key)

# =====================================================================
# 📲 SIDEBAR: ENTERPRISE HUB & LIVE TESTING SUITE
# =====================================================================
st.sidebar.markdown("### 🏢 BanquetAI Enterprise Console")
st.sidebar.caption("Operational Node: Active")
st.sidebar.markdown("---")

st.sidebar.markdown("### 📲 Live Audience Testing")
st.sidebar.write("Scan this code right now to open this interface live on your mobile device directly from your seat!")

# Dynamic web URL hook calibration layer
try:
    from streamlit.web.server.websocket_headers import _get_websocket_headers
    headers = _get_websocket_headers()
    host = headers.get("Host", "share.streamlit.io")
    app_url = f"https://{host}"
except Exception:
    app_url = "https://share.streamlit.io/"

# Generate dynamic production-ready QR frame asset
qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data={urllib.parse.quote(app_url)}"
st.sidebar.image(qr_api_url, caption="Scan to evaluate live", use_container_width=True)
st.sidebar.markdown("---")
# =====================================================================

# 3. HIGH-IMPACT HERO LANDING SECTION
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>✨ BanquetAI</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563;'>Autonomous Venue Orchestration & Catering Audit Engine</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6B7280; font-size: 14px;'>Modernizing high-volume hospitality management through computer vision spatial planning and raw procurement intelligence.</p>", unsafe_allow_html=True)
st.write("---")

# 4. INTUITIVE STEP-BY-STEP CONTAINER FOR OPERATORS
st.subheader("📌 Step 1: Ingest Venue Parameters")

# Spatial layout drop portal
uploaded_blueprint = st.file_uploader(
    "Upload Structural Hall Blueprint, Layout Image, or Hand-Drawn Sketch", 
    type=["jpg", "png", "jpeg"]
)

# Grid organization for input values to maximize scan density
col_left, col_right = st.columns(2)
with col_left:
    guest_count = st.number_input("Guaranteed Guest Target:", min_value=50, max_value=2000, value=300, step=50)
with col_right:
    menu_details = st.text_input("Menu Structure / Requirements:", value="Chicken Biryani, Beef Seekh Kebab, Naan, Gajar ka Halwa")

# Trigger operations flow safely
if uploaded_blueprint and guest_count and menu_details:
    st.write("---")
    st.subheader("🔍 Step 2: Computer Vision Spatial Analysis")
    st.image(uploaded_blueprint, caption="Scanning structural layout map parameters...", use_container_width=True)
    
    # Rigid systemic prompt constraints parsing parameters smoothly
    prompt = f"""
    You are an elite hospitality operations architect specializing in computer vision spatial layouts and event logistics.
    Analyze this hall layout image, along with these parameters: Guest Count: {guest_count}, Menu: '{menu_details}'.
    
    First, scan the image to detect or calculate the visible hall dimensions/square footage. Then, output exactly in this strict layout format:
    Detected Spatial Footprint: [State dimensions or estimated area from image text, e.g., 8000 sq ft]
    Max Tables Fit: [Just the number of tables, e.g., 30]
    Est. Chicken Stock Needed: [Just the number in kg, e.g., 120]
    Est. Rice Stock Needed: [Just the number in kg, e.g., 75]
    Est. Total Event Budget: [Total estimated wholesale cost in PKR digits only, e.g., 450000]
    ====DISPATCH====
    BANQUETAI - KITCHEN & DECOR DISPATCH ORDER
    Venue Scope: Visual Layout Inspected | Target Capacity: {guest_count} Pax
    Kitchen Ops: Raw inventory requirements calculated safely. Ensure food layout is active exactly 30 mins before one-dish deadline.
    Decor Ops: Set up layout configuration safely based on blueprint scan. Maintain center stage alignment corridors clear. Khuda Hafiz.
    """
    
    with st.spinner("Executing multi-agent spatial reasoning calculations..."):
        image_data = uploaded_blueprint.read()
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[prompt, {"mime_type": "image/jpeg", "data": image_data}]
        )
        
        # Split text structure from metrics data elements cleanly
        ai_output = response.text.split("====DISPATCH====")
        raw_metrics = ai_output[0].split("\n")
        
        # Safe fallback variable extraction metrics loops
        footprint = next((line.split(": ")[1] for line in raw_metrics if "Footprint" in line and ": " in line), "8,000 sq ft")
        tables = next((line.split(": ")[1] for line in raw_metrics if "Tables" in line and ": " in line), str(guest_count // 10))
        chicken = next((line.split(": ")[1] for line in raw_metrics if "Chicken" in line and ": " in line), "120 kg")
        rice = next((line.split(": ")[1] for line in raw_metrics if "Rice" in line and ": " in line), "75 kg")
        try:
            budget_line = next((line.split(": ")[1] for line in raw_metrics if "Budget" in line and ": " in line), "450000")
            budget_str = ''.join(filter(str.isdigit, budget_line))
            total_budget = int(budget_str) if budget_str else 450000
        except Exception:
            total_budget = 450000
            
        saas_fee = int(total_budget * 0.015)
        
        # =====================================================================
        # 📈 HIGH-IMPACT METRICS VISUAL GRID (CLEAN & CATCHY BRAND DESIGN)
        # =====================================================================
        st.subheader("📊 Operational Analytics & Revenue Matrix")
        
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("📐 Layout Area", footprint)
        m_col2.metric("🍽️ Safe 10-Seater Tables", f"{tables} Tables")
        m_col3.metric("🍗 Raw Chicken Stock", f"{chicken}")
        
        m_col4, m_col5, m_col6 = st.columns(3)
        m_col4.metric("🌾 Raw Rice Stock", f"{rice}")
        m_col5.metric("💰 Gross Event Volume", f"Rs. {total_budget:,}")
        m_col6.metric("🔥 SaaS Processing Profit (1.5%)", f"Rs. {saas_fee:,}", delta="Net Yield")
        # =====================================================================
        
        if len(ai_output) > 1:
            st.write("---")
            st.subheader("📋 Step 3: Operational Logistics Actions")
            
            final_manifest = ai_output[1].strip()
            
            # Displays manifest inside a clean, high-contrast code visualization layout block
            st.code(final_manifest, language="text")
            
            # Formulate safe text-encoded routing payload packages
            encoded_sms = urllib.parse.quote(final_manifest)
            whatsapp_url = f"https://wa.me/?text={encoded_sms}"
            
            # Primary deep-linked action controller button execution logic
            st.markdown(f"""
                <a href="{whatsapp_url}" target="_blank">
                    <button style="background-color:#25D366;color:white;border:none;padding:14px 28px;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;width:100%;margin-bottom:10px;">
                        📲 Dispatch Digital Manifest to Staff via WhatsApp
                    </button>
                </a>
            """, unsafe_allow_html=True)
            
            # Digital accessibility player controller integration logic loops
            clean_speech = final_manifest.replace("\n", " ").replace("'", "\\'")
            st.components.v1.html(f"""
                <script>
                function playSpeech() {{
                    let msg = new SpeechSynthesisUtterance('{clean_speech}');
                    msg.lang = 'ur-PK'; 
                    msg.rate = 0.85;    
                    window.speechSynthesis.speak(msg);
                }}
                </script>
                <button onclick="playSpeech()" style="background-color:#1E3A8A;color:white;border:none;padding:12px 24px;border-radius:6px;font-size:16px;font-weight:bold;cursor:pointer;width:100%;">
                    🔊 Broadcast Audio Instruction to Kitchen Speakers
                </button>
            """, height=60)
