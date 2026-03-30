# 💊 MediBot Jaipur — Local Medical AI Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-green?style=for-the-badge&logo=python)
![Mistral](https://img.shields.io/badge/Mistral-7B-orange?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-Latest-purple?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-blue?style=for-the-badge)
![Gradio](https://img.shields.io/badge/Gradio-UI-red?style=for-the-badge)
![Offline](https://img.shields.io/badge/Runs-100%25_Offline-success?style=for-the-badge)

### 🤖 Ask about Indian medicines + find nearest medical stores in Jaipur — powered by local AI, zero internet needed!

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Architecture](#-architecture) • [Tech Stack](#-tech-stack) • [Datasets](#-datasets)

</div>

---

## 🌟 What is MediBot Jaipur?

> **MediBot Jaipur** is a fully offline, privacy-first Medical AI Assistant that answers questions about **253,973 Indian medicines** and helps you find the **nearest medical store** from **383 verified Jaipur pharmacies** — all running locally on your laptop using Mistral 7B.

No API keys. No internet. No data leaving your machine. Just pure AI magic. 🔥

---

## ✨ Features

| Feature | Description |
|---|---|
| 💊 **253K+ Medicines** | Complete A-Z Indian medicine database with prices in ₹ |
| 📍 **383 Jaipur Stores** | Find nearest medical stores by area name |
| 🧠 **RAG Architecture** | Retrieval Augmented Generation for accurate answers |
| 🔒 **100% Offline** | No internet, no API costs, no data privacy concerns |
| ⚡ **Fast Search** | MiniLM embeddings search 323K chunks in milliseconds |
| 🗺️ **Google Maps Links** | Direct links to stores on Google Maps |
| 📞 **Store Details** | Phone, timings, delivery, ratings for each store |
| 🎨 **Beautiful UI** | Dark-themed Gradio interface with quick-question buttons |
| 🤖 **Mistral 7B** | Powerful 7B parameter LLM running on local GPU |

---

## 🎬 Demo

```
📍 Area: Malviya Nagar
💊 Question: "medicine for fever"

MediBot →
"For fever, common medicines include:
 1. Paracetamol (500mg) - ₹15-30
 2. Dolo 650 - ₹30
 3. Calpol - ₹25

 Always consult a real doctor before use.

 🏥 Nearby Medical Stores in Malviya Nagar:

 1. Apollo Pharmacy (Malviya Nagar)
    ⭐ 3.4/5 (302 reviews)
    🕐 7AM - 11PM | ❌ No delivery
    📞 9198488707
    🗺️ maps.google.com/?q=26.86,75.81

 2. City Med House (Malviya Nagar)
    ⭐ 4.7/5 (2790 reviews)
    🕐 7AM - 9PM | 🚚 Delivery: 5km
    📞 9181639077
    🗺️ maps.google.com/?q=26.86,75.80"
```

---

## 🚀 Installation

### Prerequisites
- Python 3.10+
- NVIDIA GPU (8GB+ VRAM recommended)
- [Ollama](https://ollama.com/download) installed
- 16GB+ RAM

### Step 1 — Clone the repo
```bash
git clone https://github.com/Jashanjindal/MediBot.git
cd MediBot
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Pull Mistral model
```bash
ollama pull mistral
```

### Step 4 — Download datasets
Download these and place in `data/` folder:
- [A-Z Medicines Dataset of India](https://www.kaggle.com/datasets/shudhanshusingh/az-medicine-dataset-of-india) → `A_Z_medicines_dataset_of_india.csv`
- [Medical Q&A Dataset](https://www.kaggle.com/datasets/keivalya/medquad-medicinal-question-answer-dataset) → `medDataset_processed.csv`
- Jaipur Medical Stores Dataset → `jaipur_medical_stores_ml.xlsx`

### Step 5 — Build vectorstore (one time only!)
```bash
# Open ingest.ipynb in Jupyter and run all cells
# This takes ~26 minutes — only needed ONCE!
jupyter notebook ingest.ipynb
```

### Step 6 — Launch MediBot!
```bash
# Open launch.ipynb and run all 4 cells
jupyter notebook launch.ipynb
# Opens at http://127.0.0.1:7860
```

---

## 📁 Project Structure

```
MediBot/
│
├── 📓 launch.ipynb          ← Run this every day! (4 cells, ~2 mins)
├── 📁 setup/
│   └── ingest.ipynb         ← Run once to build vectorstore
│
├── 📁 data/
│   ├── A_Z_medicines_dataset_of_india.csv
│   ├── medDataset_processed.csv
│   └── jaipur_medical_stores_ml.xlsx
│
├── 📁 vectorstore/          ← Auto-generated (not on GitHub)
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md
```

---

## 🧠 Architecture

```
┌─────────────────────────────────────────────────────────┐
│              USER INPUT                                  │
│   Area: "Malviya Nagar"                                 │
│   Question: "medicine for fever"                         │
└──────────────┬──────────────────────────┬───────────────┘
               │                          │
               ▼                          ▼
┌──────────────────────┐    ┌─────────────────────────────┐
│   RAG PIPELINE       │    │   LOCATION ENGINE           │
│                      │    │                             │
│  MiniLM Embeddings   │    │  Search 383 Jaipur stores   │
│         ↓            │    │  by area name / GPS         │
│  ChromaDB Search     │    │  using GeoPy distance       │
│         ↓            │    │         ↓                   │
│  Top 8 relevant      │    │  Top 3 nearest stores       │
│  medical chunks      │    │  with full details          │
└──────────┬───────────┘    └──────────────┬──────────────┘
           │                               │
           └──────────────┬────────────────┘
                          ▼
            ┌─────────────────────────┐
            │      MISTRAL 7B         │
            │  Reads medicine context │
            │  + store information    │
            │  Generates full answer  │
            │  Running on RTX GPU     │
            └────────────┬────────────┘
                         ▼
            ┌─────────────────────────┐
            │      GRADIO UI          │
            │  Dark themed chat       │
            │  Quick question buttons │
            │  Location input box     │
            └─────────────────────────┘
```

---

## 🔧 Tech Stack

| Component | Technology | Why |
|---|---|---|
| **LLM** | Mistral 7B via Ollama | Best 7B model, runs on 8GB VRAM |
| **Embeddings** | MiniLM (sentence-transformers) | 50x faster than LLM embeddings |
| **Vector DB** | ChromaDB | Fast similarity search |
| **Location** | GeoPy | Distance calculation between GPS coordinates |
| **Framework** | LangChain | Connects all AI components |
| **UI** | Gradio | Beautiful dark-themed web interface |
| **Language** | Python 3.10+ | ML ecosystem |
| **GPU** | NVIDIA RTX 4050 | Local GPU inference |

---

## 📊 Datasets

```
Dataset 1 — A-Z Medicines of India
├── Total medicines    : 253,973
├── Key columns        : name, price(₹), manufacturer, composition
└── Source             : Kaggle

Dataset 2 — Medical Q&A
├── Total Q&A pairs    : 16,407
├── Key columns        : question, answer, type
└── Source             : Kaggle

Dataset 3 — Jaipur Medical Stores
├── Total stores       : 383
├── Key columns        : name, address, locality, lat/lon,
│                        phone, timings, delivery, rating
└── Coverage           : All major Jaipur localities

Combined Knowledge Base
├── Total documents    : 270,380
├── After chunking     : 323,516 chunks
└── Embedding model    : all-MiniLM-L6-v2
```

---

## 📍 Jaipur Areas Covered

```
Malviya Nagar    Vaishali Nagar    C-Scheme
Mansarovar       Tonk Road         Ajmer Road
Sanganer         Jagatpura         Pratap Nagar
Civil Lines      Raja Park         Shyam Nagar
Nirman Nagar     Sodala            Vidhyadhar Nagar
...and many more!
```

---

## 💡 Sample Questions

```
💊 Medicine Info
→ "What is Paracetamol used for?"
→ "What medicines contain Amoxicillin?"
→ "Composition of Augmentin 625?"

💰 Pricing
→ "Price of Dolo 650 in India?"
→ "Cheapest fever medicines?"

⚠️ Side Effects
→ "Side effects of Azithromycin?"
→ "Is Ibuprofen safe for children?"

📍 With Location (Jaipur specific)
→ Area: Vaishali Nagar | "medicine for cold"
→ Area: C-Scheme | "where can I get Metformin?"
→ Area: Mansarovar | "nearest 24x7 pharmacy?"
```

---

## 🗓️ Daily Usage

```bash
# Step 1 — Start Ollama (keep terminal open)
ollama serve

# Step 2 — Open launch notebook
jupyter notebook launch.ipynb

# Step 3 — Run All Cells (Ctrl+F9)
# Takes ~2 minutes total

# Step 4 — Open browser
# Go to http://127.0.0.1:7860
```

---

## 🏆 What Makes This Special

- ✅ **No API costs** — completely free to run forever
- ✅ **Privacy first** — your medical questions never leave your laptop
- ✅ **Indian medicine focused** — built specifically for Indian medicines with ₹ prices
- ✅ **Jaipur specific** — 383 verified local pharmacies with real contact details
- ✅ **Location aware** — finds nearest store in your area instantly using GPS data
- ✅ **Massive knowledge base** — 323K chunks of medical knowledge
- ✅ **Production ready UI** — looks and feels like a real product
- ✅ **Fully reproducible** — anyone can clone and rebuild in ~30 minutes

---

## ⚠️ Disclaimer

> **MediBot Jaipur is for educational purposes only.**
> Always consult a qualified medical professional before taking any medicine.
> Store information may not be 100% accurate — always verify before visiting.
> The creators are not responsible for any medical decisions made based on this tool.

---

## 👨‍💻 Author

**Jashan Jindal**
- B.Tech CS (AI & ML) — JECRC University, Jaipur
- GitHub: [@Jashanjindal](https://github.com/Jashanjindal)
- LinkedIn: [Jashan Jindal](https://linkedin.com/in/jashanjindal)

---

## 📜 License

MIT License — free to use, modify, and distribute!

---

<div align="center">

**Built with ❤️ in Jaipur, Rajasthan 🇮🇳**

*If this helped you, give it a ⭐ on GitHub!*

*"Built a complete offline Medical AI with RAG architecture, local LLM inference, and location-based pharmacy search — running 100% on my laptop!"*

</div>
