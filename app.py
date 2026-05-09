import streamlit as st

# Page config
st.set_page_config(
    page_title="Triple C Digital",
    page_icon="💻",
    layout="centered"
)

# Header
st.title("💻 Triple C Digital")
st.subheader("Modern Technology Solutions for Small Businesses")
st.markdown("---")

# About section
st.markdown("""
### Welcome
At Triple C Digital we help small local businesses grow through 
modern, affordable technology. Whether you need a website, app, 
or smarter systems — we handle everything in plain English.
No confusing tech talk. No runaround. No surprises.
""")

st.markdown("---")

# Client intake form
st.header("📋 Request a Free Quote")
st.write("Fill out the form below and we'll get back to you within 24 hours.")

business_name = st.text_input("Business Name")
contact_name = st.text_input("Your Name")
contact_email = st.text_input("Email Address")
contact_phone = st.text_input("Phone Number")
business_type = st.text_input("What does your business do?")

st.markdown("---")

# Service selection
st.header("🛠️ Select Your Service")

service = st.selectbox(
    "What do you need help with?",
    [
        "Select a service...",
        "Brand New Website",
        "Website Redesign",
        "Website Maintenance",
        "Mobile App Development",
        "Business Automation",
        "Data Analysis and Reporting",
        "Full Tech Package"
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

# Pricing logic
pricing = {
    "Brand New Website": {"Just Me (Solo)": 800, "Small (2-10 employees)": 1500, "Medium (11-50 employees)": 2500},
    "Website Redesign": {"Just Me (Solo)": 600, "Small (2-10 employees)": 1200, "Medium (11-50 employees)": 2000},
    "Website Maintenance": {"Just Me (Solo)": 150, "Small (2-10 employees)": 250, "Medium (11-50 employees)": 400},
    "Mobile App Development": {"Just Me (Solo)": 2000, "Small (2-10 employees)": 3500, "Medium (11-50 employees)": 6000},
    "Business Automation": {"Just Me (Solo)": 500, "Small (2-10 employees)": 1000, "Medium (11-50 employees)": 2000},
    "Data Analysis and Reporting": {"Just Me (Solo)": 400, "Small (2-10 employees)": 800, "Medium (11-50 employees)": 1500},
    "Full Tech Package": {"Just Me (Solo)": 2500, "Small (2-10 employees)": 4500, "Medium (11-50 employees)": 8000},
}

# Show quote
if service != "Select a service..." and business_size != "Select size...":
    price = pricing[service][business_size]
    st.markdown("---")
    st.header("💰 Your Estimated Quote")
    st.success(f"**{service}** for a **{business_size}** business: **${price:,}**")
    st.caption("Final pricing confirmed after free consultation. No surprises.")

st.markdown("---")

# Additional info
st.header("📝 Tell Us More")
project_details = st.text_area(
    "Describe your biggest tech challenge or what you want built:",
    height=150
)

timeline = st.selectbox(
    "When do you need this?",
    [
        "Select timeline...",
        "As soon as possible",
        "Within 1 month",
        "Within 3 months",
        "Just exploring options"
    ]
)

budget_confirmed = st.checkbox(
    "I understand this is an estimate and final price will be confirmed in consultation"
)

st.markdown("---")

# Submit
st.header("🚀 Submit Your Request")

if st.button("Submit Quote Request", type="primary"):
    if not business_name:
        st.error("Please enter your business name.")
    elif not contact_email:
        st.error("Please enter your email address.")
    elif service == "Select a service...":
        st.error("Please select a service.")
    elif not project_details:
        st.error("Please describe your project.")
    else:
        st.success(f"""
        ✅ Thank you, {contact_name}!
        
        Your quote request has been received. 
        Triple C Digital will contact you at {contact_email} within 24 hours.
        
        Here's your summary:
        - Business: {business_name}
        - Service: {service}
        - Estimated Investment: ${pricing[service][business_size] if business_size != 'Select size...' else 'TBD':,}
        """)
        st.balloons()

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; color: gray;'>
    <p>Triple C Digital | Modern Tech for Small Business</p>
    <p>Professional • Affordable • Trustworthy</p>
</div>
""", unsafe_allow_html=True)
