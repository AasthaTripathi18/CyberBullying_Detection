import streamlit as st

st.title("Cyberbullying Detection System")

st.write("Enter a comment to check if it is cyberbullying.")

comment = st.text_input("Enter Comment")

bad_words = [
"kill yourself",
"suicide",
"die",
"ugly",
"loser",
"idiot",
"worthless",
"stupid",
"moron",
"hate you",
"fuck","kill","naked"
]

def keyword_check(text):

    text = text.lower()

    for word in bad_words:
        if word in text:
            return True

    return False


if st.button("Check Comment"):

    if keyword_check(comment):
        st.error("🚫 Cyberbullying detected. Comment Blocked")

    else:
        st.success("✅ Safe Comment")