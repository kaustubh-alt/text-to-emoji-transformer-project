# text2emoji_context_fixed.py
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

# -----------------------
# 1️⃣ Load emoji CSV
# -----------------------
@st.cache_data
def load_emoji_csv(path="emoji_df.csv"):
    df = pd.read_csv(path)
    df['name'] = df['name'].str.lower()
    return df

emoji_df = load_emoji_csv()

# -----------------------
# 2️⃣ Load embedding model
# -----------------------
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

# -----------------------
# 3️⃣ Precompute emoji embeddings
# -----------------------
@st.cache_resource
def precompute_embeddings(_model, df):
    return np.array([_model.encode([desc])[0] for desc in df['name']])

emoji_embeddings = precompute_embeddings(model, emoji_df)

# -----------------------
# 4️⃣ Streamlit UI
# -----------------------
st.title("Context-Aware Text to Emoji Converter 🎯")
st.write("Type a sentence and get meaningful emojis!")

text_input = st.text_area("Enter text:", "")
max_emojis = st.slider("Max number of emojis:", 1, 10, 5)

if st.button("Convert to Emoji"):
    if not text_input.strip():
        st.warning("Please enter some text!")
    else:
        text_emb = model.encode([text_input])[0]

        # Cosine similarity with emoji embeddings
        sims = np.dot(emoji_embeddings, text_emb) / (
            np.linalg.norm(emoji_embeddings, axis=1) * np.linalg.norm(text_emb)
        )

        # Top N emojis
        top_indices = sims.argsort()[::-1][:max_emojis]
        output_emojis = "".join([emoji_df.iloc[i]['emoji'] for i in top_indices])

        st.subheader("Output Emojis:")
        st.write(output_emojis)
