import streamlit as st

# Page config
st.set_page_config(
    page_title="Triple C Digital",
    page_icon="💻",
    layout="centered"
)

# Custom CSS for red and black branding
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .stButton>button {
        background-color: #cc0000;
        color: white;
        border: none;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #990000;
        color: white;
    }
    h1, h2, h3 {
        color: #1a1a1a;
    }
    .header-bar {
        background-color: #cc0000;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        color: #888888;
        font-size: 13px;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 2px solid #cc0000;
    }
    .quote-box {
        background-color: #f9f9f9;
        border-left: 5px solid #cc0000;
        padding: 20px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .section-divider {
        border-top: 2px solid #cc0000;
        margin: 25px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Logo and Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(
        "https://raw.githubusercontent.com/triplecdigitalservice/triple-c-digital-portal/main/IMG_3184.png",
        width=250
    )


st.markdown("""
<div style='text-align: center; margin-bottom: 10px;'>
    <h1 style='color: #1a1a1a; font-size: 36px; margin: 0;'>TRIPLE C DIGITAL</h1>
    <p style='color: #cc0000; font-size: 16px; font-weight: bold; letter-spacing: 3px;'>
        MODERN TECHNOLOGY FOR SMALL BUSINESS
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# Value proposition
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### ✅ Personal\nOne on one service from someone who actually listens.")
with col2:
    st.markdown("### 💰 Affordable\nPricing that makes sense for small business budgets.")
with col3:
    st.markdown("### 🗣️ Plain English\nNo confusing tech talk. Ever.")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# About
st.markdown("""
### About Triple C Digital
We believe outdated technology is one of the biggest hidden costs draining small businesses 
today. From slow websites that drive customers away to manual processes that eat up your time — 
we've seen firsthand how the wrong tech holds hardworking business owners back.

**We exist to change that.**
""")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# Quote Request Form
st.markdown("## 📋 Request Your Free Quote")
st.write("Fill out the form below. We respond within 24 hours — guaranteed.")

col1, col2 = st.columns(2)
with col1:
    business_name = st.text_input("Business Name *")
    contact_name = st.text_input("Your Name *")
with col2:
    contact_email = st.text_input("Email Address *")
    contact_phone = st.text_input("Phone Number")

business_type = st.text_input("What does your business do? *")

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# Service Selection
st.markdown("## 🛠️ Select Your Service")

service = st.selectbox(
    "What do you need help with?",
    [
        "Select a service...",
        "Brand New Website",
        "Website Redesign",
        "Website Maintenance — Monthly",
        "Mobile App Development",
        "Business Automation",
        "Data Analysis and Reporting",
        "Full Tech Package — Best Value"
    ]
)

business_size = st.selectbox(
    "Business Size",
    [
        "Select size...",
        "Just Me (Solo)",
        "Small (2-10 employees)",
        "Medium (11-50 employees)"
    ]
)

# Pricing
pricing = {
    "Brand New Website": {
        "Just Me (Solo)": 400,
        "Small (2-10 employees)": 750,
        "Medium (11-50 employees)": 1250
    },
    "Website Redesign": {
        "Just Me (Solo)": 300,
        "Small (2-10 employees)": 600,
        "Medium (11-50 employees)": 1000
    },
    "Website Maintenance — Monthly": {
        "Just Me (Solo)": 75,
        "Small (2-10 employees)": 125,
        "Medium (11-50 employees)": 200
    },
    "Mobile App Development": {
        "Just Me (Solo)": 1000,
        "Small (2-10 employees)": 1750,
        "Medium (11-50 employees)": 3000
    },
    "Business Automation": {
        "Just Me (Solo)": 250,
        "Small (2-10 employees)": 500,
        "Medium (11-50 employees)": 1000
    },
    "Data Analysis and Reporting": {
        "Just Me (Solo)": 200,
        "Small (2-10 employees)": 400,
        "Medium (11-50 employees)": 750
    },
    "Full Tech Package — Best Value": {
        "Just Me (Solo)": 1250,
        "Small (2-10 employees)": 2250,
        "Medium (11-50 employees)": 4000
    },
}


# Live quote display
if service != "Select a service..." and business_size != "Select size...":
    price = pricing[service][business_size]
    st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
    st.markdown("## 💰 Your Estimated Investment")
    st.markdown(f"""
    <div class='quote-box'>
        <h3 style='color: #cc0000; margin: 0;'>{service}</h3>
        <p style='font-size: 28px; font-weight: bold; margin: 10px 0;'>${price:,}</p>
        <p style='color: #666; margin: 0;'>Final pricing confirmed after your free consultation. No surprises. No hidden fees.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# Project details
st.markdown("## 📝 Tell Us About Your Project")

project_details = st.text_area(
    "Describe your biggest tech challenge or what you want built:",
    placeholder="Example: I have no website and I'm losing customers to competitors who do. I need something professional that shows what my business does and lets people contact me easily.",
    height=150
)

timeline = st.selectbox(
    "When do you need this completed?",
    [
        "Select timeline...",
        "As soon as possible",
        "Within 1 month",
        "Within 3 months",
        "Just exploring options"
    ]
)

how_found = st.selectbox(
    "How did you hear about Triple C Digital?",
    [
        "Select one...",
        "Nextdoor",
        "Word of mouth",
        "Google search",
        "Social media",
        "Other"
    ]
)

budget_confirmed = st.checkbox(
    "✅ I understand this is an estimate and final pricing will be confirmed during my free consultation."
)

st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

# Submit section
st.markdown("## 🚀 Submit Your Request")
st.write("Zero obligation. Zero pressure. Just a conversation about how we can help.")

if st.button("Submit My Free Quote Request"):
    if not business_name:
        st.error("⚠️ Please enter your business name.")
    elif not contact_name:
        st.error("⚠️ Please enter your name.")
    elif not contact_email:
        st.error("⚠️ Please enter your email address.")
    elif service == "Select a service...":
        st.error("⚠️ Please select a service.")
    elif not project_details:
        st.error("⚠️ Please describe your project.")
    elif not budget_confirmed:
        st.error("⚠️ Please confirm you understand the pricing is an estimate.")
    else:
        price_display = f"${pricing[service][business_size]:,}" if business_size != "Select size..." else "TBD in consultation"

        formspree_data = {
            "Business Name": business_name,
            "Contact Name": contact_name,
            "Email": contact_email,
            "Phone": contact_phone,
            "Business Type": business_type,
            "Service Requested": service,
            "Business Size": business_size,
            "Estimated Price": price_display,
            "Project Details": project_details,
            "Timeline": timeline,
            "How They Found Us": how_found
        }

        response = requests.post(
            "https://formspree.io/f/xgodpwed",
            data=formspree_data
        )

        if response.status_code == 200:
            st.success(f"""
            ✅ Thank you, {contact_name}! Your request has been received.

            **Here's your summary:**
            - 🏢 Business: {business_name}
            - 🛠️ Service: {service}
            - 💰 Estimated Investment: {price_display}
            - ⏱️ Timeline: {timeline}

            **What happens next:**
            Triple C Digital will reach out to {contact_email} within 24 hours
            to schedule your free consultation.

            We look forward to working with you!
            """)
            st.balloons()
        else:
            st.error("Something went wrong submitting your request. Please try again.")

# Footer
st.markdown("""
<div class='footer'>
    <p><strong>Triple C Digital</strong></p>
    <p>Modern Technology Solutions for Small Business</p>
    <p>Professional • Affordable • Trustworthy</p>
</div>
""", unsafe_allow_html=True)
