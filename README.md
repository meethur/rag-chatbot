# 📄 RAG Chatbot (PDF Q&A)

A Streamlit-based Retrieval-Augmented Generation (RAG) chatbot that allows users to upload a PDF and ask questions about its content.

---

## 🚀 Features

* 📂 Upload PDF documents
* 🔍 Extract and split text into chunks
* 🧠 Generate embeddings using OpenAI
* 📊 Store vectors using FAISS
* 💬 Ask questions and get contextual answers
* ⚡ Built with Streamlit for an interactive UI

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* OpenAI API
* FAISS
* pdfplumber

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run ragchatbot.py
```

---

## 📌 Usage

1. Upload a PDF file
2. Enter your question
3. Get answers based only on the document content

---

## ⚠️ Notes

* Do NOT expose your API key publicly
* Works best with text-based PDFs (not scanned images)
* Large PDFs may take longer to process

---

## 📷 Future Improvements

* Chat history support
* Multi-file upload
* Source citation highlighting
* Deployment on Streamlit Cloud

---

## 👨‍💻 Author

MEETHU R

---

## ⭐ If you like this project

Give it a star on GitHub!
