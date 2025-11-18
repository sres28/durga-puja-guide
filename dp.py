import streamlit as st
import google.generativeai as genai

# Configure Gemini (replace with your key safely)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash-lite")

st.title("🪔 Durga Puja Companion App 🎉")

# Create 2 tabs
tab1, tab2 = st.tabs(["🤖 Food Suggestions", "🏛️ Pandal Suggestions"])

# ---------------- Tab 1: Food ----------------
with tab1:
    st.header("🤖 Tell us about your food taste")

    # User input options
    food_type = st.selectbox("Which type of food do you prefer?", ["No preference", "Street Food", "Main Dishes", "Sweets"])
    spicy_pref = st.selectbox("Do you like spicy food?", ["Yes", "No"])
    veg_pref = st.selectbox("Do you prefer Veg or Non-Veg?", ["Both", "Veg", "Non-Veg"])
    user_prompt = st.text_area("Or write in your own words:")
    if st.button("🍴 Get Food Suggestion"):
             prompt = f"User selected: Food={food_type}, Spicy={spicy_pref}, VegPref={veg_pref}. Suggest 3 Durga Puja foods with reasons for Kolkata City and give me the famous Place as well"
    else:
            prompt = f"User wrote: {user_prompt}. Suggest 3 Durga Puja pandal based out of the Kolkata City and give your perferences."

    response = model.generate_content(prompt)
    st.subheader("Food Suggestion")
    st.write(response.text)

# ---------------- Tab 2: Pandal ----------------
with tab2:
    st.header("🤖 Tell us your pandal preference")

    pandal_choice = st.selectbox("Which pandal are you visiting?", ["No preference", "Bagbazar", "College Square", "Ekdalia Evergreen", "Santosh Mitra Square"])
    pandal_prompt = st.text_area("Or describe your pandal style (e.g., traditional, modern, theme-based):")

    if st.button("🏛️ Get Pandal Suggestion"):
             prompt = f"User selected Pandal={pandal_choice}. Suggest what foods to try near this pandal based of the kolkata city."
    else:
            prompt = f"User wrote: {pandal_prompt}. Suggest a famous pandal in Kolkata they should visit and what food to eat nearby."

    response = model.generate_content(prompt)
    st.subheader("Pandal Suggestion")
    st.write(response.text)

