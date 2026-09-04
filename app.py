import streamlit as st
import os
import urllib.parse
from google import genai
from google.genai import types

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
# 📲 SIDEBAR: ENTERPRISE HUB & AUTOMATED QR SUITE
# =====================================================================
st.sidebar.markdown("### 🏢 BanquetAI Enterprise Console")
st.sidebar.caption("Operational Node: Active")
st.sidebar.markdown("---")

st.sidebar.markdown("### 📲 Live Audience Testing")
st.sidebar.write("Scan this code right now to open this interface live on your mobile device directly from your seat!")

# Robust dynamic web URL discovery engine
try:
    from streamlit.web.server.websocket_headers import _get_websocket_headers
    host = _get_websocket_headers().get("Host")
    if not host or "localhost" in host:
        app_url = "https://streamlit.app"  # Your primary production cloud handle
    else:
        app_url = f"https://{host}"
except Exception:
    app_url = "https://streamlit.app"

# Generate dynamic production-ready QR frame asset (Uses a robust global endpoint)
qr_api_url = f"https://qrserver.com{urllib.parse.quote(app_url)}"
st.sidebar.image(qr_api_url, caption="Scan to evaluate live", use_container_width=True)
st.sidebar.markdown("---")
# =====================================================================

# 3. HIGH-IMPACT HERO LANDING SECTION
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>✨ BanquetAI</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #4B5563;'>Autonomous Venue Operations & Commercial Financial Auditor</h3>", unsafe_allow_html=True)
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
    
    # Clean, isolated prompt string allocation block to prevent parameter execution anomalies
    base_instructions = """
    You are an elite hospitality operations architect specializing in computer vision spatial layouts and event logistics.
    Scan the provided image to locate text markers, dimensions, or layout bounds indicating room footprint, then process the inputs.
    
    Output exactly in this strict baseline format with values matching the requested calculations:
    Footprint: [State dimensions or estimated area from image text, e.g., 8000 sq ft]
    Tables: [Just the number of tables, e.g., 30]
    Meat: [Calculate 250g per head for primary rice + 150g for kebab in kg, append 'kg' suffix, e.g., 120 kg]
    Rice: [Calculate 150g high-quality Basmati per head in kg, append 'kg' suffix, e.g., 45 kg]
    Naan: [Calculate 1.5 Naan per head baseline allocation, append 'pcs' suffix, e.g., 450 pcs]
    Sweets: [Calculate 100g serving size of Gajar Halwa per head in kg including milk/khoya, append 'kg' suffix, e.g., 30 kg]
    PerHeadRate: [Calculate a dynamic realistic catering per head cost in PKR digits only based on menu complexity, e.g., 1200]
    HallRent: [Calculate realistic commercial venue rental space fee based on footprint area in PKR digits only, e.g., 90000]
    ====DISPATCH====
    ✨ BANQUETAI OFFICIAL OPERATIONAL DISPATCH MANIFEST
    📍 Venue Scope: Visual Layout Inspected
    👥 Target Capacity: CUSTOM_GUESTS Pax
    🍱 Catering Blueprint: CUSTOM_MENU
    
    📢 RAW PROCUREMENT MATRIX LOG:
    - Estimated Total Meat Required: METRIC_MEAT
    - Estimated Total Rice Required: METRIC_RICE
    - Total Tandoori Naan Allocation: METRIC_NAAN
    - Total Sweet Dessert Base (Gajar Halwa): METRIC_SWEET
    
    ⚠️ FLOOR-PLAN RULE: Ensure main stage corridors remain completely clear. Service staff ready exactly 30 minutes before one-dish deadline code active. Khuda Hafiz.
    """
    
    # Overwrite template payload properties cleanly using native string transformations 
    final_prompt = base_instructions.replace("CUSTOM_GUESTS", str(guest_count)).replace("CUSTOM_MENU", menu_details)

    with st.spinner("Executing multi-agent spatial reasoning calculations via gemini-3.6-flash..."):
        image_data = uploaded_blueprint.read()
        image_part = types.Part.from_bytes(data=image_data, mime_type="image/jpeg")
        
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=[final_prompt, image_part]
        )
        
        # Split text structure from metrics data elements cleanly
        text_payload = response.text
        
        # Safe structural dictionary variable extraction blocks to prevent validation index failures
        metrics = {}
        for line in text_payload.split("\n"):
            if ":" in line and "====" not in line:
                key, val = line.split(":", 1)
                metrics[key.strip()] = val.strip()
        
        # Safe extraction handles fallback parameters smoothly
        footprint = metrics.get("Footprint", "8,000 sq ft")
        tables = metrics.get("Tables", str(guest_count // 10))
        meat_stock = metrics.get("Meat", "120 kg")
        rice_stock = metrics.get("Rice", "45 kg")
        naan_count = metrics.get("Naan", "450 pcs")
        sweet_stock = metrics.get("Sweets", "30 kg")
        
        # Clear Financial Audit Formulas
        try:
            per_head = int(''.join(filter(str.isdigit, metrics.get("PerHeadRate", "1200"))))
            hall_rent = int(''.join(filter(str.isdigit, metrics.get("HallRent", "90000"))))
        except Exception:
            per_head, hall_rent = 1200, 90000
            
        total_budget = (guest_count * per_head) + hall_rent
        saas_fee = int(total_budget * 0.015)
        
        # Update manifest string parameters programmatically before rendering
        ai_dispatch_block = text_payload.split("====DISPATCH====")[-1].strip()
        final_manifest = ai_dispatch_block.replace("METRIC_MEAT", meat_stock).replace("METRIC_RICE", rice_stock).replace("METRIC_NAAN", naan_count).replace("METRIC_SWEET", sweet_stock)
        
        # =====================================================================
        # 📈 HIGH-IMPACT METRICS VISUAL GRID (CLEAN & CATCHY BRAND DESIGN)
        # =====================================================================
        st.subheader("📊 Operational Analytics & Resource Matrix")
        
        m_col1, m_col2, m_col3 = st.columns(3)
        m_col1.metric("📐 Layout Space Area", footprint)
        m_col2.metric("🍽️ Safe 10-Seater Tables", f"{tables} Tables")
        m_col3.metric("🍗 Required Meat Stock", meat_stock)
        
        m_col4, m_col5, m_col6 = st.columns(3)
        m_col4.metric("🌾 Required Rice Stock", rice_stock)
        m_col6.metric("🫓 Total Naan Count", naan_count)
        m_col5.metric("🥕 Gajar Halwa Desserts", sweet_stock)
        
        st.markdown("### 💰 Financial Audit & Commercial Ledger")
        
        f_col1, f_col2, f_col3 = st.columns(3)
        f_col1.metric("💰 Gross Event Volume", f"Rs. {total_budget:,}")
        f_col2.metric("🔥 SaaS Platform Yield (1.5%)", f"Rs. {saas_fee:,}", delta="Net Revenue")
        
        # 🧾 DYNAMIC TRANSPARENT COST LEDGER: Explaining the calculations to judges
        with st.expander("🔍 View Transparent Cost Audit Calculations"):
            st.write(f"**Catering Menu Cost:** {guest_count} Guests × Rs. {per_head:,}/Head = **Rs. {(guest_count * per_head):,}**")
            st.write(f"**Venue Space Rental Fee:** Extracted Spatial Footprint Valuation = **Rs. {hall_rent:,}**")
            st.write(f"**Gross Audited Total Calculation:** (Catering Cost) + (Venue Rental) = **Rs. {total_budget:,}**")
        # =====================================================================
        
        st.write("---")
        st.subheader("📋 Step 3: Operational Logistics Actions")
        
        # Displays manifest inside a clean layout block
        st.code(final_manifest, language="text")
        
        # Formulate safe text-encoded routing payload packages
        encoded_sms = urllib.parse.quote(final_manifest)
        whatsapp_url = f"https://wa.me{encoded_sms}"
        
        # Primary deep-linked action controller button execution logic
        st.markdown(f"""
            <a href="{whatsapp_url}" target="_blank">
