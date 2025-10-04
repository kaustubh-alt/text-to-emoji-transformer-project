
# Precision Emojifier

**An AI-powered web application that summarizes text and converts it into relevant emojis, based on the core meaning and user-selected precision.**  

---

## 🌟 Features

- **Text Summarization**: Distills input text into key points based on a **precision slider**.  
- **Emoji Mapping**: Converts meaningful words or summaries into emojis using semantic matching.  
- **Semantic Understanding**: Uses **Sentence Transformers** to understand context and meaning.  
- **Interactive UI**: Built with **Streamlit** for real-time text-to-emoji conversion.  
- **Flexible Precision Control**: Low precision → short summary & fewer emojis, High precision → detailed summary & precise emojis.  

---

## 🛠️ Tech Stack

- **Python**  
- **Libraries**:  
  - `streamlit` – Web interface  
  - `nltk` – Text preprocessing  
  - `emoji` – Emoji utilities  
  - `sentence-transformers` – Semantic embeddings  
  - `pandas` – CSV handling  
  - `torch` – Deep learning backend for embeddings  

---

## ⚙️ How It Works

1. **Input Stage**  
   - User enters a sentence, paragraph, or article.  
   - Sets the **precision level** using a slider.  

2. **Text Preprocessing**  
   - Removes stopwords and unnecessary words.  
   - Tokenizes and selects important words.  

3. **Semantic Matching**  
   - Converts input text to **embedding vector** using **Sentence Transformer**.  
   - Emoji descriptions (from CSV) are converted to embeddings (precomputed).  
   - Computes **cosine similarity** to find emojis most relevant to the input.  

4. **Output Stage**  
   - Displays a **summary of the text**.  
   - Shows **matching emojis** according to similarity score and precision level.  

---

## 📁 Project Structure

```

precision-emojifier/
│
├── emoji_dataset.csv        # Emoji symbols, keywords, and descriptions
│
├── temp.py                       # Streamlit web application and Core logic for text-to-emoji mapping
├── requirements.txt             # Python dependencies
└── README.md

````

---

## 🚀 How to Run

1. Clone the repository:
git clone https://github.com/yourusername/precision-emojifier.git
cd precision-emojifier


2. Install dependencies:
pip install -r requirements.txt


3. Run the Streamlit app:
streamlit run temp.py


4. Open the URL in your browser and start converting text to emojis!

---

## 📈 Future Enhancements

* Add **multilingual support**.
* Improve **emoji selection** using more advanced contextual embeddings.
* Add **sentiment analysis** to match emojis with tone.
* Provide **downloadable summary + emoji output** for sharing.


