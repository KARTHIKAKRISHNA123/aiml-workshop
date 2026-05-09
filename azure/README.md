# ☁️ AIML With Azure

<p align="center">
  <img src="https://img.shields.io/badge/Microsoft%20Azure-0089D6?style=for-the-badge&logo=microsoftazure&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/Azure%20AI%20Foundry-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white"/>
  <img src="https://img.shields.io/badge/Azure%20Vision-00BCF2?style=for-the-badge&logo=microsoftazure&logoColor=white"/>
  <img src="https://img.shields.io/badge/Azure%20Language-7B2D8B?style=for-the-badge&logo=microsoftazure&logoColor=white"/>
</p>

<p align="center">
  A hands-on learning repository exploring <strong>Microsoft Azure AI services</strong> — covering Computer Vision, Natural Language Processing, AI Agents, and Azure AI Foundry — with deployed Streamlit applications.
</p>

---

## 📁 Repository Structure

```
AIML_With_Azure-main/
│
├── app.py                          # Azure Vision Image Analysis (tags, URL fallback)
├── cv.py                           # Image captioning with Azure Computer Vision
├── objects.py                      # Object detection with bounding boxes
├── tags.py                         # Image tag extraction with confidence scores
├── requirements.txt                # Root-level dependencies
├── startup.sh                      # Azure App Service startup script
├── .gitignore
│
├── Azure_Project/                  # ✅ Deployed Streamlit Vision App
│   ├── app.py                      # Full Streamlit UI for Azure Vision AI
│   ├── requirements.txt
│   └── startup.sh                  # Port 8501 startup (Azure App Service)
│
├── ai-foundry/                     # Azure AI Foundry + GPT-4.1 experiments
│   ├── connect.py                  # Client connection setup
│   ├── simple.py                   # Basic chat completion
│   ├── streaming.py                # Streaming response with delta chunks
│   ├── pirate_assistant.py         # Custom system prompt persona
│   ├── multi_conversion.py         # Multi-turn conversation with assistant role
│   ├── tool_passing.py             # Function/tool calling (weather tool)
│   └── requirements.txt
│
├── agents/                         # Azure AI Agents SDK experiments
│   ├── setup.py                    # AgentsClient + DeviceCodeCredential setup
│   ├── helloWorld.py               # Basic agent creation and thread messaging
│   ├── multidemo.py                # Multi-turn memory-aware agent chat
│   ├── rag.py                      # RAG agent with FileSearch + VectorStore
│   ├── policy.txt                  # Sample document for RAG knowledge base
│   └── requirements.txt
│
└── nlp_demo/                       # Azure AI Language Service demos
    ├── connect.py                  # TextAnalyticsClient setup
    ├── sentiment.py                # Sentiment analysis with confidence scores
    ├── language_detection.py       # Multi-language detection (8 languages)
    ├── key_phrases.py              # Key phrase extraction
    ├── pii_detection.py            # PII entity recognition and redaction
    ├── all.py                      # Unified runner for all NLP features
    ├── requirements.txt
    └── nlp_project/                # ✅ Deployed Streamlit NLP Dashboard
        ├── app.py                  # Neon NLP Studio — animated Streamlit UI
        └── requirements.txt
```

---

## 🧩 Module Breakdown

### 🖼️ Root — Azure Computer Vision Scripts

Quick-start Python scripts exploring Azure AI Vision's `ImageAnalysisClient`.

| File | Feature | Visual Feature Used |
|------|---------|-------------------|
| `cv.py` | AI-generated image caption | `VisualFeatures.CAPTION` |
| `objects.py` | Object detection with bounding boxes | `VisualFeatures.OBJECTS` |
| `tags.py` | Tag extraction with confidence scores | `VisualFeatures.TAGS` |
| `app.py` | Tags + 429 rate-limit fallback handler | `VisualFeatures.TAGS` |

**Azure Service:** `Azure AI Vision` (Cognitive Services)  
**SDK:** `azure-ai-vision-imageanalysis`

---

### 🚀 Azure_Project — Deployed Vision App

A production-ready **Streamlit web application** deployed to **Azure App Service** that wraps the Azure Vision API in an interactive UI.

**Features:**
- Sidebar credential input (Endpoint + API Key) — no hardcoded secrets
- Image uploader supporting JPG, JPEG, PNG
- Side-by-side layout: uploaded image | AI analysis results
- Displays AI Caption with confidence percentage
- Displays top 8 Tags with confidence scores
- Displays detected Objects list
- Full error handling with user-friendly messages

**Deployment:**
```bash
# Azure App Service startup command
python -m streamlit run app.py \
  --server.port 8501 \
  --server.address 0.0.0.0 \
  --server.headless true
```

**Tech Stack:** `Streamlit` · `azure-ai-vision-imageanalysis` · `Pillow` · `Azure App Service`

---

### 🤖 ai-foundry — Azure AI Foundry + GPT-4.1 Nano

Experiments using **Azure AI Foundry** with the `gpt-4.1-nano-1` deployment via the OpenAI-compatible API.

| File | Concept | Key Feature |
|------|---------|------------|
| `connect.py` | Client setup | `OpenAI(base_url, api_key)` |
| `simple.py` | Basic chat completion | System + user message roles |
| `streaming.py` | Real-time streaming | `stream=True`, delta chunks |
| `pirate_assistant.py` | Custom persona | System prompt engineering |
| `multi_conversion.py` | Multi-turn context | Assistant role in message history |
| `tool_passing.py` | Function/Tool calling | `tools`, `tool_choice="auto"`, tool result injection |

**Highlights:**
- `streaming.py` — Streams tokens in real time, printing each `delta.content` chunk as it arrives
- `tool_passing.py` — Full tool-calling loop: model decides to call `get_weather()`, result is injected back, and a final response is generated
- `pirate_assistant.py` — Demonstrates system prompt persona control

**Tech Stack:** `openai` · `azure-ai-inference` · `Azure AI Foundry` · `GPT-4.1 Nano`

---

### 🧠 agents — Azure AI Agents SDK

Experiments with **Azure AI Agents** using the `AgentsClient` and `DeviceCodeCredential` for secure, interactive authentication.

| File | What it Demonstrates |
|------|---------------------|
| `setup.py` | Environment-variable-based client setup with `DeviceCodeCredential` |
| `helloWorld.py` | Agent creation → thread → message → run → response loop |
| `multidemo.py` | Multi-turn memory agent that remembers context across messages |
| `rag.py` | RAG agent with file upload, vector store, and `FileSearchTool` |
| `policy.txt` | Sample e-commerce policy document used as RAG knowledge base |

**`policy.txt` covers:** Refund policy, shipping, payment methods, cancellations, order tracking, support hours.

**Tech Stack:** `azure-ai-agents` · `azure-ai-projects` · `azure-identity` · `python-dotenv`

---

### 💬 nlp_demo — Azure AI Language Service

Standalone scripts and a deployed Streamlit app using **Azure Text Analytics** (`azure-ai-textanalytics`).

**Individual Scripts:**

| File | Feature | Description |
|------|---------|-------------|
| `sentiment.py` | Sentiment Analysis | Returns positive/neutral/negative with confidence scores |
| `language_detection.py` | Language Detection | Detects language across 8 input documents (English, Spanish, French, German, Japanese, Korean, Portuguese, Russian) |
| `key_phrases.py` | Key Phrase Extraction | Pulls key concepts from documents |
| `pii_detection.py` | PII Detection & Redaction | Detects email, phone, address — returns redacted text + entity categories |
| `all.py` | Unified Runner | Runs all features in a single consolidated script |

**`nlp_project/` — Neon NLP Studio (Deployed App):**

A visually styled **Streamlit dashboard** with animated UI (Space Grotesk + Syne fonts, glassmorphism design) that wraps all NLP features into a single interactive interface.

**Tech Stack:** `azure-ai-textanalytics` · `azure-identity` · `Streamlit`

---

## 🛠️ Full Tech Stack

| Category | Technologies |
|----------|-------------|
| **Cloud Platform** | Microsoft Azure (App Service, Cognitive Services) |
| **AI Services** | Azure AI Vision, Azure AI Language, Azure AI Foundry, Azure AI Agents |
| **LLM** | GPT-4.1 Nano (via Azure AI Foundry) |
| **Language** | Python 3.x |
| **Web Framework** | Streamlit |
| **Azure SDKs** | `azure-ai-vision-imageanalysis`, `azure-ai-textanalytics`, `azure-ai-agents`, `azure-identity` |
| **OpenAI SDK** | `openai` (Azure-compatible endpoint) |
| **Image Processing** | Pillow (PIL) |
| **Auth** | `AzureKeyCredential`, `DeviceCodeCredential`, `python-dotenv` |
| **Version Control** | Git, GitHub |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- An active [Microsoft Azure subscription](https://azure.microsoft.com/free/)
- Azure resources provisioned:
  - Azure AI Vision (Cognitive Services)
  - Azure AI Language (Text Analytics)
  - Azure AI Foundry project with a GPT-4.1 deployment

### 1. Clone the Repository

```bash
git clone https://github.com/KARTHIKAKRISHNA123/AIML_With_Azure.git
cd AIML_With_Azure
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

Install per-module based on what you want to run:

```bash
# Root CV scripts
pip install azure-ai-vision-imageanalysis pillow

# AI Foundry experiments
pip install openai azure-ai-inference

# Agents
pip install azure-ai-agents azure-ai-projects azure-identity python-dotenv

# NLP demos
pip install azure-ai-textanalytics azure-identity streamlit

# Azure_Project (Vision Streamlit App)
pip install azure-ai-vision-imageanalysis pillow streamlit
```

### 4. Set Environment Variables (for Agents module)

Create a `.env` file in the `agents/` directory:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/...
MODEL_DEPLOYMENT_NAME=<your-model-deployment-name>
```

> ⚠️ **Security Note:** Never commit API keys or endpoints to version control. The `agents/` module uses environment variables via `python-dotenv`. For other modules, replace hardcoded credentials with `.env` variables before deploying.

### 5. Run a Script

```bash
# Example: run the Vision caption demo
python cv.py

# Example: run all NLP features
python nlp_demo/all.py

# Example: launch the Vision Streamlit app locally
cd Azure_Project
streamlit run app.py
```

---

## 🌐 Deployed Applications

| App | Description | Stack |
|-----|-------------|-------|
| **Azure Vision AI Demo** | Upload images → get AI captions, tags, and objects via Azure Vision | Streamlit + Azure Vision + Azure App Service |
| **Neon NLP Studio** | Interactive NLP dashboard — sentiment, language detection, PII, key phrases | Streamlit + Azure Language + Azure App Service |

---

## 📌 Key Concepts Covered

- Connecting to **Azure Cognitive Services** using `AzureKeyCredential`
- Using **Azure AI Vision** for image captioning, object detection, and tagging
- Using **Azure AI Language** for sentiment analysis, language detection, PII redaction, and key phrase extraction
- Calling **Azure AI Foundry (GPT-4.1)** with streaming, personas, and multi-turn context
- Implementing **function/tool calling** with the OpenAI SDK on Azure
- Building and running **Azure AI Agents** with threads, runs, and memory
- Implementing **RAG (Retrieval-Augmented Generation)** with file upload and vector stores
- Deploying Python/Streamlit apps to **Azure App Service** with startup scripts

---

## 👩‍💻 Author

**Karthika Krishna**  
AI/ML Learner · Azure Cloud · Full Stack Developer  
[![GitHub](https://img.shields.io/badge/GitHub-KARTHIKAKRISHNA123-181717?style=flat&logo=github)](https://github.com/KARTHIKAKRISHNA123)

---

## 📄 License

This repository is for educational and learning purposes. Please credit the author if you reference or build upon this work.

---

<p align="center">
  Built with ☁️ Azure AI · 🐍 Python · 🎈 Streamlit
</p>
