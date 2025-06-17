import streamlit as st
import datetime

st.set_page_config(page_title="Investors Bank", page_icon="🏦", layout="wide")

# Simulated user session
def login():
    st.session_state.logged_in = True
    st.session_state.name = "Investor John"
    st.session_state.savings_balance = 5000
    st.session_state.current_balance = 10000

def logout():
    st.session_state.clear()

# Sidebar for login/logout and navigation
with st.sidebar:
    st.image("https://i.imgur.com/5Jm8ZqF.png", width=120)
    st.title("🏦 Investors Bank")

    if not st.session_state.get("logged_in"):
        if st.button("🔐 Login"):
            login()
    else:
        st.write(f"Welcome, {st.session_state.name}")
        if st.button("🚪 Logout"):
            logout()

# Main App Logic
if st.session_state.get("logged_in"):
    st.markdown("""
    <style>
    .big-font { font-size:30px !important; font-weight: bold; color: #044389; }
    .highlight { color: #048BA8; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='big-font'>Welcome to Investors Bank 💼</div>", unsafe_allow_html=True)
    st.subheader("Your Smart and Simple Banking Experience")

    col1, col2, col3 = st.columns(3)
    col1.metric("Savings Balance", f"₦{st.session_state.savings_balance:,}")
    col2.metric("Current Balance", f"₦{st.session_state.current_balance:,}")
    col3.metric("Last Login", datetime.datetime.now().strftime("%d %b %Y %H:%M"))

    st.markdown("---")
    tab1, tab2, tab3, tab4 = st.tabs(["💰 Deposit", "💸 Withdraw", "🔁 Transfer", "📊 Summary"])

    with tab1:
        acc_type = st.selectbox("Select Account", ["Savings", "Current"])
        amount = st.number_input("Deposit Amount", min_value=100)
        if st.button("Deposit"):
            if acc_type == "Savings":
                st.session_state.savings_balance += amount
            else:
                st.session_state.current_balance += amount
            st.success(f"₦{amount:,} deposited to your {acc_type} account.")

    with tab2:
        acc_type = st.selectbox("Select Account to Withdraw From", ["Savings", "Current"], key="withdraw")
        amount = st.number_input("Withdraw Amount", min_value=100, key="withdraw_amt")
        if st.button("Withdraw"):
            if acc_type == "Savings" and amount <= st.session_state.savings_balance:
                st.session_state.savings_balance -= amount
                st.success(f"₦{amount:,} withdrawn from your Savings account.")
            elif acc_type == "Current" and amount <= st.session_state.current_balance:
                st.session_state.current_balance -= amount
                st.success(f"₦{amount:,} withdrawn from your Current account.")
            else:
                st.error("Insufficient funds.")

    with tab3:
        from_acc = st.selectbox("Transfer from", ["Savings", "Current"], key="from")
        to_acc = st.selectbox("Transfer to", ["Current", "Savings"], key="to")
        trans_amt = st.number_input("Amount", min_value=100, key="trans")
        if st.button("Transfer"):
            if from_acc == to_acc:
                st.warning("Cannot transfer to the same account.")
            elif from_acc == "Savings" and trans_amt <= st.session_state.savings_balance:
                st.session_state.savings_balance -= trans_amt
                st.session_state.current_balance += trans_amt
                st.success(f"₦{trans_amt:,} transferred from Savings to Current.")
            elif from_acc == "Current" and trans_amt <= st.session_state.current_balance:
                st.session_state.current_balance -= trans_amt
                st.session_state.savings_balance += trans_amt
                st.success(f"₦{trans_amt:,} transferred from Current to Savings.")
            else:
                st.error("Insufficient funds.")

    with tab4:
        st.info("This dashboard shows your account activities.")
        st.write("Coming soon: Expense tracking, charts, and statement downloads!")

else:
    st.title("🏦 Investors Bank")
    st.subheader("Please login from the sidebar to continue")
