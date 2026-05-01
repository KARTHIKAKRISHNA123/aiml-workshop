# 🧠 AIML Learnings

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/NLTK-2496ED?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=black"/>
</p>

<p align="center">
  A structured collection of hands-on AI/ML notebooks covering <strong>Artificial Neural Networks</strong>, <strong>Convolutional Neural Networks</strong>, and <strong>Natural Language Processing</strong> — built and executed on Google Colab.
</p>

---

## 📁 Repository Structure

```
AIML_Learnings/
│
├── ANN_with_Iris.ipynb              # ANN applied to Iris flower classification
├── Basic_ANN_Implementation.ipynb  # ANN fundamentals with TensorFlow/Keras
├── CNN.ipynb                        # CNN architecture from scratch
├── CNN_mnist_and_cifar.ipynb        # CNN on MNIST & CIFAR-10 datasets
├── NLP_Practice.ipynb               # NLP pipeline with NLTK
└── test.ipynb                       # Scratch / sandbox notebook
```

---

## 📓 Notebooks Overview

### 1. 🌸 ANN with Iris Dataset
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KARTHIKAKRISHNA123/AIML_Learnings/blob/main/ANN_with_Iris.ipynb)

Implements a multi-layer Artificial Neural Network using the classic **Iris flower dataset** (150 samples, 3 classes).

**Key Concepts:**
- Dataset loading via `sklearn.datasets.load_iris`
- Train/test split using `sklearn.model_selection`
- One-Hot Encoding with `sklearn.preprocessing.OneHotEncoder`
- ANN model built and trained with **TensorFlow / Keras**
- Model evaluation and accuracy metrics

**Tech Stack:** `TensorFlow` · `Keras` · `scikit-learn` · `NumPy`

---

### 2. ⚡ Basic ANN Implementation
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KARTHIKAKRISHNA123/AIML_Learnings/blob/main/Basic_ANN_Implementation.ipynb)

Foundational implementation of an Artificial Neural Network from scratch using TensorFlow's Keras API.

**Key Concepts:**
- TensorFlow version check and GPU detection (`tf.config.list_physical_devices`)
- Layer-by-layer ANN construction using `tensorflow.keras.layers`
- Dense layers, activations, loss functions, and optimizers
- Training loop and validation

**Tech Stack:** `TensorFlow` · `Keras` · `NumPy`

---

### 3. 🖼️ CNN Architecture
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KARTHIKAKRISHNA123/AIML_Learnings/blob/main/CNN.ipynb)

Builds a Convolutional Neural Network architecture from first principles, exploring spatial feature extraction.

**Key Concepts:**
- Convolutional layers, pooling, and flattening
- Image data preprocessing and normalization
- Visualization of feature maps using Matplotlib

**Tech Stack:** `TensorFlow` · `Keras` · `NumPy` · `Matplotlib`

---

### 4. 🔢 CNN on MNIST & CIFAR-10
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KARTHIKAKRISHNA123/AIML_Learnings/blob/main/CNN_mnist_and_cifar.ipynb)

Applies CNN models to two industry-standard benchmark datasets for image classification.

**Key Concepts:**
- **MNIST** — 70,000 grayscale handwritten digit images (28×28), 10 classes
- **CIFAR-10** — 60,000 color images (32×32×3), 10 object categories
- Dataset loading via `tensorflow.keras.datasets`
- Model building using `layers` and `models` API
- Training, evaluation, and accuracy/loss visualization

**Tech Stack:** `TensorFlow` · `Keras` · `NumPy` · `Matplotlib`

---

### 5. 💬 NLP Practice
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/KARTHIKAKRISHNA123/AIML_Learnings/blob/main/NLP_Practice.ipynb)

End-to-end Natural Language Processing pipeline using NLTK, covering all core text preprocessing techniques.

**Key Concepts:**

| Step | Method | Purpose |
|------|--------|---------|
| Text Cleaning | `re` (regex) | Lowercase, remove special chars |
| Tokenization | `word_tokenize` | Split text into tokens |
| Stopword Removal | `stopwords.words("english")` | Remove noise words |
| Stemming | `PorterStemmer` | Reduce words to root form |
| Lemmatization | `WordNetLemmatizer` | Morphologically correct normalization |

**Tech Stack:** `NLTK` · `Python` · `re`

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.x |
| **Deep Learning** | TensorFlow 2.x, Keras |
| **ML Library** | scikit-learn |
| **NLP** | NLTK (tokenize, stem, lemmatize, stopwords) |
| **Data & Viz** | NumPy, Matplotlib |
| **Datasets** | Iris, MNIST, CIFAR-10 |
| **Environment** | Google Colab, Jupyter Notebook |
| **Version Control** | Git, GitHub |

---

## 🚀 Getting Started

### Run on Google Colab (Recommended)

Click any **"Open in Colab"** badge above — no local setup required. Google Colab provides free GPU access for faster model training.

### Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/KARTHIKAKRISHNA123/AIML_Learnings.git
cd AIML_Learnings
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install tensorflow scikit-learn nltk numpy matplotlib jupyter
```

**4. Download NLTK corpora** (required for NLP notebook)
```python
import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
```

**5. Launch Jupyter**
```bash
jupyter notebook
```

---

## 📊 Learning Outcomes

By working through these notebooks, you will understand:

- How **Artificial Neural Networks** are constructed layer by layer and trained on real datasets
- How **Convolutional Neural Networks** extract spatial features from images
- How to benchmark CNN models on **MNIST** and **CIFAR-10**
- How to build a complete **NLP preprocessing pipeline** — from raw text to clean, normalized tokens
- How to use **TensorFlow/Keras** for model definition, compilation, training, and evaluation
- How to use **scikit-learn** utilities for data splitting and encoding

---

## 📌 Prerequisites

- Basic Python programming
- Familiarity with linear algebra and probability fundamentals
- No prior deep learning experience required — notebooks are beginner-friendly

---

## 👩‍💻 Author

**Karthika Krishna**
AI/ML Learner · Full Stack Developer
[![GitHub](https://img.shields.io/badge/GitHub-KARTHIKAKRISHNA123-181717?style=flat&logo=github)](https://github.com/KARTHIKAKRISHNA123)

---

## 📄 License

This repository is intended for educational purposes. Feel free to reference and learn from the code. Please credit the author if you use these materials in your own work.

---

<p align="center">
  Made with ❤️ and lots of <code>epochs</code>
</p>
