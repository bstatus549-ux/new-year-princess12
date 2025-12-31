import streamlit as st
import time

st.set_page_config(page_title="For My Princess ❤️", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background-color: #ff1a1a;  /* Red background */
    background-image: url('https://i.ibb.co/6R0KQpM/flowers-bg.png'); /* flower background image */
    background-size: cover;
}
.big-year {
    font-size: 120px;
    font-weight: bold;
    color: #ffff00; /* Yellow for contrast */
    text-align: center;
    animation: pulse 1.5s infinite;
}
@keyframes pulse {
    0% { transform: scale(1); opacity: 1; }
    50% { transform: scale(1.1); opacity: 0.8; }
    100% { transform: scale(1); opacity: 1; }
}
.center {
    text-align: center;
    color: white;
}
.heart {
    font-size: 80px;
    text-align: center;
    animation: beat 1s infinite;
}
@keyframes beat {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}
.button > button {
    background-color: #ff4b5c;
    color: white;
    border-radius: 30px;
    padding: 10px 30px;
    font-size: 18px;
}
.fireworks {
    text-align: center;
    font-size: 50px;
}
</style>
""", unsafe_allow_html=True)

# ---------- PAGE STATE ----------
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------- PAGE 1 : 2026 ----------
if st.session_state.page == 1:
    st.markdown("<div class='big-year'>2026</div>", unsafe_allow_html=True)
    st.markdown("<h2 class='center'>A new year, a new chapter 💫</h2>", unsafe_allow_html=True)

    if st.button("✨ Continue"):
        st.session_state.page = 2
        st.rerun()

# ---------- PAGE 2 : For My Love ----------
elif st.session_state.page == 2:
    st.markdown("<h1 class='center'>For My Princess 💗</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='center'>Every moment, every fight, every smile… I choose you.</h3>", unsafe_allow_html=True)

    if st.button("❤️ Touch My Heart"):
        st.session_state.page = 3
        st.rerun()

# ---------- PAGE 3 : Heart Button ----------
elif st.session_state.page == 3:
    st.markdown("<div class='heart'>❤️</div>", unsafe_allow_html=True)
    st.markdown("<h2 class='center'>This heart beats only for you Princess</h2>", unsafe_allow_html=True)

    if st.button("💓 Open"):
        st.session_state.page = 4
        st.rerun()

# ---------- PAGE 4 : New Year Wish ----------
elif st.session_state.page == 4:
    st.markdown("<h1 class='center'>🎇 Happy New Year Dehaa 🎇</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='center'>May 2026 bring us closer, stronger and happier ❤️</h3>", unsafe_allow_html=True)
    st.markdown("<div class='fireworks'>🎆🎆🎆🎆🎆🎆🎆</div>", unsafe_allow_html=True)
    
    if st.button("🌹 One More Thing"):
        st.session_state.page = 5
        st.rerun()

# ---------- PAGE 5 : Lifetime Message ----------
elif st.session_state.page == 5:
    messages = [
        "I don’t promise perfection…",
        "But I promise effort.",
        "I promise loyalty.",
        "I promise to love you my whole life ❤️"
    ]

    for msg in messages:
        st.markdown(f"<h3 class='center'>{msg}</h3>", unsafe_allow_html=True)
        time.sleep(1)

    if st.button("💍 Final Question"):
        st.session_state.page = 6
        st.rerun()

# ---------- PAGE 6 : Proposal ----------
elif st.session_state.page == 6:
    st.markdown("<h1 class='center'>💍 My Proposal 💍</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='center'>Princess, will you be my girlfriend, wifey, and Bhargavi for 2026? ❤️</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes 💕"):
            st.success("You just made me the happiest person alive ❤️")

    with col2:
        if st.button("Forever 🫶"):
            st.success("Forever starts now 💍✨")