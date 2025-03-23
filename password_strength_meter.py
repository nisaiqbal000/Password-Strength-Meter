import streamlit as st
import re

# Custom CSS for styling
st.markdown("""
<style>
    .stProgress > div > div > div {
        background-color: green;
    }
    .stTextInput > div > div > input {
        color: #4F8BF9;
    }
    .stButton > button {
        background-color: #4F8BF9;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stMarkdown {
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# Function to evaluate password strength
def evaluate_password_strength(password):
    strength = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        suggestions.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        suggestions.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        suggestions.append("Password should contain at least one special character.")

    # Determine strength level
    if strength == 5:
        return "Strong 💪", suggestions, "green"
    elif strength >= 3:
        return "Moderate 😐", suggestions, "orange"
    else:
        return "Weak 😟", suggestions, "red"

# Title of the app
st.title("🔐 Password Strength Meter")

# Input field for password
password = st.text_input("Enter your password:", type="password")

# Evaluate password strength
if password:
    strength, suggestions, color = evaluate_password_strength(password)
    st.markdown(f"**Password Strength:** <span style='color:{color}; font-size: 20px;'>{strength}</span>", unsafe_allow_html=True)

    # Progress bar with color
    if strength == "Strong 💪":
        st.progress(100)
    elif strength == "Moderate 😐":
        st.progress(60)
    else:
        st.progress(30)

    # Suggestions to improve password
    if suggestions:
        st.markdown("**Suggestions to improve your password:**")
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")

# Add a fun footer
st.markdown("---")
st.markdown("Made by Nisa Iqbal❤️ using [Streamlit](https://streamlit.io/)")