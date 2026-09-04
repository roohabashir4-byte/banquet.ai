import streamlit as st
import os
import urllib.parse
import re
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

# Initialize the next-gen native Google Gen AI SDK engine
client = genai.Client(api_key=api_key)

# =====================================================================
# 📲 SIDEBAR: ENTERPRISE HUB & AUTOMATED QR SUITE (FIXED INDEPENDENT)
# =====================================================================
st.sidebar.markdown("### 🏢 BanquetAI Enterprise Console")
st.sidebar.caption("Operational Node: Active")
st.sidebar.markdown("---")

st.sidebar.markdown("### 📲 Live Audience Testing")
st.sidebar.write("Scan this code right now to open this interface live on your mobile device directly from your seat!")

# Dynamic web URL discovery engine
try:
    from streamlit.web.server.websocket_headers import _get_websocket_headers
    headers = _get_websocket_headers()
    host = headers.get("Host") if headers else None
    if not host or "localhost" in host or "127.0.0.1" in host:
        app_url = "https://streamlit.app"  # Fallback to absolute production deployment URL
    else:
        app_url = f"https://{host}"
except Exception:
    app_url = "https://streamlit.app"

# Generate static, bulletproof QR code frame targeting the verified live endpoint
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
    
    # Clean, isolated prompt string allocation block targeting precise regional culinary weight formulas
    base_instructions = """
    You are an elite hospitality operations architect specializing in computer vision spatial layouts and event logistics.
    Scan the provided image to locate text markers, dimensions, scale bars, or layout bounds indicating the room footprint.
    Extract the actual total structural square footage numbers natively written or implied in the blueprint sketch.
    
    Output exactly in this strict baseline format with values matching the requested calculations. Do not modify the headers:
    Footprint: [Extract the precise structural square footage area string from the image, e.g., 4500 sq ft or 12500 sq ft]
    PerHeadRate: [Calculate a dynamic realistic catering per head cost in PKR digits only based on menu complexity, e.g., 2100]
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
    
    📢 STRUCTURAL ADVISORY NOTE: CAPACITY_ALERT_MSG
    """
    
    # Overwrite template payload properties cleanly using native string transformations 
    final_prompt = base_instructions.replace("CUSTOM_GUESTS", str(guest_count)).replace("CUSTOM_MENU", menu_details)

    with st.spinner("Executing spatial reasoning calculations via gemini-2.5-flash..."):
        image_data = uploaded_blueprint.read()
        image_part = types.Part.from_bytes(data=image_data, mime_type="image/jpeg")
        
        # FIXED: Corrected model naming structure flag parameter to native canonical string
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[final_prompt, image_part]
        )
        
        text_payload = response.text
        
        # Defensive regex value extraction to bypass any unexpected model generation variations
        def extract_metric(pattern, text, fallback):
            match = re.search(pattern, text)
            return match.group(1).strip() if match else fallback

        footprint_str = extract_metric(r"Footprint:\s*(.*)", text_payload, "1890 sq ft")
        
        # Extract purely the digits out of the spatial footprint string for transparent math calculations
        try:
            area_digits = int(''.join(filter(str.isdigit, footprint_str)))
        except Exception:
            area_digits = 1890

        # =====================================================================
        # 📐 CRITICAL SPATIAL SAFETY CALCULATOR ENGINE (DETERMINISTIC LOGIC)
        # =====================================================================
        # Safety Protocol: 1 standard 10-seater round table requires 150 sq ft for fire lanes and service paths
        max_safe_tables = area_digits // 150
        max_safe_guests = max_safe_tables * 10
        requested_tables = int(guest_count // 10)
        
        # Dynamic capacity constraint checks
        capacity_status = "🟢 Safe Capacity Allocation"
        alert_msg = "All tables fit perfectly within structural bounds with regular emergency clearance walkways active."
        
        if requested_tables > max_safe_tables:
            capacity_status = "🔴 Capacity Overload Warning"
            table_deficit = requested_tables - max_safe_tables
            alert_msg = f"OVERLOAD WARNING: You are forcing {requested_tables} tables into an area built safely for only {max_safe_tables} tables. Severe layout bottleneck detected! Please reduce count by {table_deficit * 10} guests or widen space borders."
        # =====================================================================

        # Deterministic local catering allocation math (Tied exactly to the guest input variable)
        meat_stock = f"{int(guest_count * 0.40)} kg"      # 250g Rice dish + 150g Kebab
        rice_stock = f"{int(guest_count * 0.15)} kg"      # 150g high-quality Basmati baseline
        naan_count = f"{int(guest_count * 1.50)} pcs"     # 1.5 Naan per head distribution
        sweet_stock = f"{int(guest_count * 0.10)} kg"     # 100g serving size allocation
        
        # Explicit Financial Audit Extraction
        per_head_str = extract_metric(r"PerHeadRate:\s*(.*)", text_payload, "2100")
        hall_rent_str = extract_metric(r"HallRent:\s*(.*)", text_payload, "90000")
        
        try:
            per_head = int(''.join(filter(str.isdigit, per_head_str)))
            hall_rent = int(''.join(filter(str.isdigit, hall_rent_str)))
        except Exception:
            per_head, hall_rent = 2100, 90000
            
        total_budget = (guest_count * per_head) + hall_rent
        saas_fee = int(total_budget * 0.015)
        
        # Format the automated operational text blocks safely without breaks
        if "====DISPATCH====" in text_payload:
            ai_dispatch_block = text_payload.split("====DISPATCH====")[-1].strip()
            final_manifest = ai_dispatch_block.replace("METRIC_MEAT", meat_stock).replace("METRIC_RICE", rice_stock).replace("METRIC_NAAN", naan_count).replace("METRIC_SWEET", sweet_stock).replace("CAPACITY_ALERT_MSG", alert_msg)
        else:
            final_manifest = f"✨ BANQUETAI OFFICIAL OPERATIONAL DISPATCH MANIFEST\n📍 Venue Scope: Visual Layout Inspected\n👥 Target Capacity: {guest_count} Pax\n🍱 Catering Blueprint: {menu_details}\n\n📢 RAW PROCUREMENT MATRIX LOG:\n- Estimated Total Meat Required: {meat_stock}\n- Estimated Total Rice Required: {rice_stock}\n- Total Tandoori Naan Allocation: {naan_count}\n- Total Sweet Dessert Base (Gajar Halwa): {sweet_stock}\n\n⚠️ FLOOR-PLAN RULE: {alert_msg} Khuda Hafiz."

        # =====================================================================
        # 📈 HIGH-IMPACT METRICS VISUAL GRID (CLEANLY ALIGNED)
        # =====================================================================
        st.subheader("📊 Operational Analytics & Resource Matrix")
        
        # Row 1 columns definition
