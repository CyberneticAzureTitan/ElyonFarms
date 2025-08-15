import streamlit as st
from streamlit_option_menu import option_menu

# Page config (top)
st.set_page_config(page_title="Elyon Farms", page_icon=":seedling:", layout="wide")

# Sidebar menu with all pages (including Employee Area)
with st.sidebar:
    selected = option_menu(
        menu_title="About Us",
        options=["Home", "Projects", "Contact Us"],
        icons=["house", "bar-chart-line", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation= ""
    )

# Public pages
if selected == "Home":
    st.title("🌾 Welcome to Elyon Farms")
    st.subheader("🌟 Our Vision")
    st.write("We believe that what we eat impacts our health and wellness. That's why we carved our niche in food, provision, processing, and education.")

    st.subheader("🎯 Our Mission")
    st.write("To provide quality food and agricultural products, promote sustainable farming practices, and educate communities on the importance of healthy eating and environmental stewardship.")

    st.subheader("🍂 Who We Are")
    st.markdown("""
    - Elyon Farms is a proudly Nigerian agricultural enterprise focused on cultivating cash crops like **cassava, maize, soybeans, groundnuts**, and more.  
    - With deep roots in both **traditional and modern farming practices**, we blend local wisdom with cutting-edge techniques to ensure each harvest meets the highest standards of quality and sustainability.  
    - Farming is not just our livelihood — **it's our way of life**. Whether you're a customer, a partner, or just stopping by, you're family here.
    """)

    st.subheader("🌱 Our Values")
    st.markdown("""
    - ✅ Sustainability First  
    - ✅ Community Empowerment  
    - ✅ Innovation in Agriculture  
    - ✅ Quality You Can Trust  
    - ✅ Faith and Family at Our Core
    """)

elif selected == "Projects":
    st.title("🚜 Ongoing Projects at Elyon Farms")
    st.markdown("""
    We are actively involved in several initiatives aimed at boosting food security, supporting local farmers, and increasing agricultural output across Nigeria:
    
    - 🌾 Crop Expansion Program: Scaling up production of cassava and soybeans in rural communities.  
    - 🏫 Farm-to-School Initiative: Supplying healthy farm produce to schools while teaching kids about farming.  
    - 🌍 Agro-Education Workshops: Hosting workshops to teach sustainable farming and agribusiness.  
    - 💧 Irrigation Project: Implementing solar-powered drip irrigation systems to enhance productivity year-round.
    """)

elif selected == "Contact Us":
    st.title("📬 Contact Us")
    st.write("We'd love to hear from you! Whether you have questions, feedback, or just want to say hello, feel free to reach out.")
    st.markdown("""
<form action="https://formsubmit.co/info@elyonfarms.com" method="POST" target="_blank">
    <input type="text" name="name" placeholder="Your Name" required><br><br>
    <input type="email" name="email" placeholder="Your Email" required><br><br>
    <textarea name="message" placeholder="Your Message" required></textarea><br><br>
    <!-- Honeypot to avoid spam -->
    <input type="text" name="_honey" style="display:none">
    <!-- Disable captcha -->
    <input type="hidden" name="_captcha" value="false">
    <button type="submit">Send</button>
</form>
""", unsafe_allow_html=True)

st.markdown("""
<style>
  form {
    max-width: 400
    margin: auto;
    padding: 10px;
  }
  input, textarea {
    width: 25%;
    padding: 8px;
    margin: 6px 0 12px 0;
    border: 1px solid #4CAF50;
    border-radius: 4px;
  }
  button {
    background-color: #4CAF50;
    color: WHITE;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  button:hover {
    background-color: #45a049;
  }
</style>
""", unsafe_allow_html=True)


