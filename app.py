# 3rd
import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# Load Model
model = pickle.load(open("cyberbullying_model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

stop_words = set(stopwords.words('english'))

bad_words = [
"kill yourself","suicide","die","ugly",
"loser","idiot","worthless","stupid",
"moron","hate you","bitch","fuck"
]

# SAME preprocessing as training
def clean_text(text):

    text = str(text).lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    words = text.split()
    words = [w for w in words if w not in stop_words]

    return " ".join(words)

def keyword_check(text):
    text = text.lower()
    return any(word in text for word in bad_words)

# UI
st.title("Cyberbullying Detection System")

st.write("Enter a comment to check toxicity.")

comment = st.text_area("Enter Comment")

if st.button("Check Comment"):

    if keyword_check(comment):
        st.error("🚫 Cyberbullying Detected (Keyword)")
    else:
        cleaned = clean_text(comment)
        vec = vectorizer.transform([cleaned])
        pred = model.predict(vec)

        if pred[0]==1:
            st.error("🚫 Cyberbullying Detected")
        else:
            st.success("✅ Safe Comment")

# 2nd
# import streamlit as st
# import pickle
# import re

# # Load Model
# model = pickle.load(open("cyberbullying_model.pkl","rb"))
# vectorizer = pickle.load(open("vectorizer.pkl","rb"))

# bad_words = [
# "kill yourself","suicide","die","ugly",
# "loser","idiot","worthless","stupid",
# "moron","hate you","bitch","fuck"
# ]

# def clean_text(text):
#     text = text.lower()
#     text = re.sub(r'[^a-zA-Z]',' ',text)
#     return text

# def keyword_check(text):
#     text=text.lower()
#     return any(word in text for word in bad_words)

# # UI
# st.title("Cyberbullying Detection System")

# st.write("Enter a comment to check toxicity.")

# comment = st.text_area("Enter Comment")

# if st.button("Check Comment"):

#     if keyword_check(comment):
#         st.error("🚫 Cyberbullying Detected (Keyword)")
#     else:
#         cleaned = clean_text(comment)
#         vec = vectorizer.transform([cleaned])
#         pred = model.predict(vec)

#         if pred[0]==1:
#             st.error("🚫 Cyberbullying Detected")
#         else:
#             st.success("✅ Safe Comment")


# 1st
# import streamlit as st

# st.title("Cyberbullying Detection System")

# st.write("Enter a comment to check if it is cyberbullying.")

# comment = st.text_input("Enter Comment")

# bad_words = [
# "kill yourself",
# "suicide",
# "die",
# "ugly",
# "loser",
# "idiot",
# "worthless",
# "stupid",
# "moron",
# "hate you",
# "go to hell",
# "fuck",
# "bitch",
# "muderer",
# "hang yourself",
# "prostitute"
# ]

# def keyword_check(text):

#     text = text.lower()

#     for word in bad_words:
#         if word in text:
#             return True

#     return False


# if st.button("Check Comment"):

#     if keyword_check(comment):
#         st.error("🚫 Cyberbullying detected. Comment Blocked")

#     else:
#         st.success("✅ Safe Comment")