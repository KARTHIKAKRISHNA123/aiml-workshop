# 🚀 AIML Workshop

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Microsoft%20Azure-0089D6?style=for-the-badge&logo=microsoftazure&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>
</p>

<p align="center">
  A comprehensive hands-on AI/ML engineering repository covering 
  <strong>Machine Learning</strong>, 
  <strong>Deep Learning</strong>, 
  <strong>Natural Language Processing</strong>, 
  <strong>Azure AI Services</strong>, 
  <strong>LLMs</strong>, 
  <strong>AI Agents</strong>, and 
  <strong>Cloud AI Deployment</strong>.
</p>

---

# 📚 Repository Vision

AIML Workshop is designed as a centralized AI engineering workspace that combines:

- Foundational AI/ML learning
- Practical deep learning implementations
- NLP pipelines
- Computer Vision systems
- Azure Cognitive Services
- GPT-powered AI applications
- AI Agents and RAG systems
- Streamlit deployments
- Cloud-native AI engineering

This repository evolves as a long-term AI engineering knowledge base and experimentation lab.

---

# 📁 Repository Structure

```bash
AIML-Workshop/
│
├── Machine_Learning/
│   ├── ANN_with_Iris.ipynb
│   ├── Basic_ANN_Implementation.ipynb
│   └── ML experiments
│
├── Deep_Learning/
│   ├── CNN.ipynb
│   ├── CNN_mnist_and_cifar.ipynb
│   └── Deep learning architectures
│
├── NLP/
│   ├── NLP_Practice.ipynb
│   ├── sentiment.py
│   ├── language_detection.py
│   ├── key_phrases.py
│   └── pii_detection.py
│
├── Azure_AI/
│   ├── Azure_Project/
│   ├── ai-foundry/
│   ├── agents/
│   └── nlp_demo/
│
├── Computer_Vision/
│   ├── cv.py
│   ├── objects.py
│   ├── tags.py
│   └── app.py
│
├── Generative_AI/
│   ├── streaming.py
│   ├── tool_passing.py
│   ├── pirate_assistant.py
│   └── multi_conversion.py
│
├── AI_Agents/
│   ├── helloWorld.py
│   ├── multidemo.py
│   ├── rag.py
│   └── policy.txt
│
├── Streamlit_Apps/
│   ├── Vision AI Demo
│   └── Neon NLP Studio
│
└── README.md
```

---

# 🧠 Core Learning Domains

---

# 🤖 Machine Learning & Neural Networks

Hands-on implementations of:

- Artificial Neural Networks (ANN)
- TensorFlow/Keras fundamentals
- Iris classification
- Training pipelines
- Model evaluation

### Key Concepts

- Dense layers
- Activation functions
- Optimizers
- Loss functions
- Backpropagation
- Model training and validation

### Tech Stack

- TensorFlow
- Keras
- scikit-learn
- NumPy

---

# 🖼️ Deep Learning & Computer Vision

Implementation of CNN architectures and image analysis systems.

### Includes

- CNN architecture design
- MNIST classification
- CIFAR-10 classification
- Image preprocessing
- Feature extraction
- Object detection
- Image captioning
- Image tagging

### Azure Vision Features

- AI-generated captions
- Object detection with bounding boxes
- Tag extraction with confidence scores

### Tech Stack

- TensorFlow
- Keras
- Azure AI Vision
- Pillow
- Matplotlib

---

# 💬 Natural Language Processing

End-to-end NLP workflows using both traditional NLP and Azure AI Language Services.

### Traditional NLP

- Tokenization
- Stopword removal
- Stemming
- Lemmatization
- Regex-based preprocessing

### Azure NLP Features

- Sentiment analysis
- Language detection
- Key phrase extraction
- PII detection and redaction

### Tech Stack

- NLTK
- Azure AI Language
- Python regex
- Streamlit

---

# ☁️ Azure AI Engineering

Production-oriented Azure AI integrations.

### Services Used

- Azure AI Vision
- Azure AI Language
- Azure AI Foundry
- Azure AI Agents
- Azure App Service

### Features

- Streamlit deployment on Azure
- GPT-powered applications
- Azure SDK integrations
- Secure credential handling
- Cloud AI experimentation

---

# 🤖 Generative AI & LLMs

Experiments using GPT models through Azure AI Foundry.

### Concepts Covered

- Prompt engineering
- Streaming responses
- Multi-turn conversations
- Function/tool calling
- Assistant personas
- OpenAI-compatible Azure APIs

### Example Features

- Real-time token streaming
- Weather tool calling
- Persona-controlled assistants
- Context-aware chat systems

---

# 🧠 AI Agents & RAG

Advanced AI engineering concepts using Azure AI Agents SDK.

### Includes

- Agent creation
- Threads and runs
- Multi-turn memory
- Retrieval-Augmented Generation (RAG)
- Vector stores
- File search tools

### RAG Workflow

```text
Document Upload → Vector Store → Retrieval → LLM Response
```

---

# 🌐 Streamlit Applications

Interactive AI applications deployed using Streamlit.

### Included Apps

| App | Description |
|------|-------------|
| Azure Vision AI Demo | AI captions, object detection, image tagging |
| Neon NLP Studio | Sentiment analysis, PII detection, language detection |

---

# 🛠️ Full Tech Stack

| Category | Technologies |
|----------|-------------|
| Language | Python 3.x |
| ML/DL | TensorFlow, Keras, scikit-learn |
| NLP | NLTK, Azure AI Language |
| Cloud | Microsoft Azure |
| LLMs | GPT-4.1 Nano |
| Web Framework | Streamlit |
| AI SDKs | Azure AI SDKs |
| Visualization | Matplotlib |
| Image Processing | Pillow |
| Environment | Jupyter, Google Colab |
| Version Control | Git, GitHub |

---

# 🚀 Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AIML-Workshop.git
cd AIML-Workshop
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install tensorflow keras scikit-learn nltk matplotlib
pip install azure-ai-textanalytics
pip install azure-ai-vision-imageanalysis
pip install azure-ai-agents
pip install azure-ai-projects
pip install azure-identity
pip install openai
pip install streamlit
pip install pillow
```

---

# 📊 Learning Outcomes

By working through this repository, you will learn:

- Machine Learning fundamentals
- Deep Learning architectures
- CNN implementation
- NLP preprocessing pipelines
- Azure Cognitive Services
- GPT integrations
- AI Agents
- RAG pipelines
- Streamlit deployments
- Cloud AI engineering workflows

---

# 🎯 Repository Goals

- Build strong AI engineering fundamentals
- Explore cloud-native AI systems
- Learn production AI workflows
- Create deployable AI applications
- Experiment with modern LLM ecosystems
- Develop industry-ready AI engineering skills

---

# 👩‍💻 Author

## Karthika Krishna

AI/ML Learner · Azure AI Enthusiast · Full Stack Developer

<p align="left">
  <a href="https://github.com/KARTHIKAKRISHNA123">
    <img src="https://img.shields.io/badge/GitHub-KARTHIKAKRISHNA123-181717?style=for-the-badge&logo=github"/>
  </a>
</p>

---

# 📄 License

This repository is intended for educational and learning purposes.

Feel free to explore, learn, and build upon the projects. Please credit the author when referencing this work.

---

<p align="center">
  Built with ☁️ Azure · 🤖 AI · 🧠 Deep Learning · 🐍 Python · 🚀 Curiosity
</p>
