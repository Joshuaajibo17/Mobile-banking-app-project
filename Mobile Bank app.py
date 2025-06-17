import streamlit as st

# ---------------------------
# Page Config and Styling
st.set_page_config(page_title="Investors Bank", page_icon="💼", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #0b3d91;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
    }
    .title-style {
        color: #0b3d91;
        font-size: 28px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Simulated Database
users_db = {"joshua": "pass123"}
balances = {"joshua": 15000}

# ---------------------------
# Session State
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''

# ---------------------------
# Login Function
def login():
    st.markdown('<div class="title-style">Investors Bank 💼</div>', unsafe_allow_html=True)
    st.subheader("Login to your secure account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users_db and users_db[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome, {username.capitalize()} 👋")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# ---------------------------
# Dashboard Function
def dashboard():
    st.markdown('<div class="title-style">Investors Bank 💼</div>', unsafe_allow_html=True)
    st.write(f"👋 Hello, **{st.session_state.username.capitalize()}**")
    
    st.markdown("### 💰 Account Balance")
    balance = balances.get(st.session_state.username, 0)
    st.info(f"₦{balance:,.2f}")

    st.markdown("---")
    st.markdown("### 🏧 Withdraw Funds")

    amount = st.number_input("Enter amount to withdraw", min_value=100, step=100)

    if st.button("Withdraw"):
        if amount > balances[st.session_state.username]:
            st.error("Insufficient balance.")
        else:
            balances[st.session_state.username] -= amount
            st.success(f"₦{amount:,.2f} withdrawn successfully.")
            st.experimental_rerun()

    st.markdown("---")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.experimental_rerun()

# ---------------------------
# App Main Logic
def main():
    if not st.session_state.logged_in:
        login()
    else:
        dashboard()

if __name__ == "__main__":
    main()
