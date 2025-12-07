# Briefify – Extractive Text Summarizer 

**Try it here** [Try now](https://briefify-by-eman.streamlit.app/)

**Project Type:** NLP / Text Summarization  
**Model Type:** Sequence-to-Sequence (Encoder–Decoder)  
**Base Model Used:** T5-Base (Fine-Tuned)

---

## Overview

**Briefify** is an extractive text summarizer built using a fine-tuned T5-Base model. Extractive summarizer picks up important senetences from the given text.

The project takes a paragraph as input and produces a concise, human-like summary.

---

## Dataset

- **Original Dataset:** TLDR Challenge Dataset from Zenodo [Dataset](https://zenodo.org/records/1168855#.XoD8i4hKiUk)
- **Original Size:** 55,000 samples  
- **Subset Used for Training:** 5,000 samples

Access the dataset from here: [Drive link](https://drive.google.com/file/d/1iGimoScd9Hf1gTZuCS-uOkDJbz3eXCL-/view?usp=sharing)

**Task Type:** Extractive Summarization (No class labels)  

**Preprocessing:** Tokenization applied during training. Text length normalized.

---

## Model & Training

- **Model:** T5-Base  
- **Training Settings:**  
  - Learning Rate: 5e-5  
  - Max Input Length: 512 tokens  
  - Max Summary Length: 128 tokens  
  - Batch Size: 2  
  - Epochs: 1  

**Evaluation Methodology:** Train–Validation Split (80–20)  
**Evaluation Metric:** ROUGE Scores (ROUGE-1, ROUGE-2, ROUGE-L)  

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/emaaanbutt/Briefify.git
cd Briefify
```
2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
3. Download the fine-tuned T5-Base model and place it in the project folder. [Download](https://drive.google.com/drive/folders/10kz7_vAHlspjoLMCW83MXs6n2mIBxHXr?usp=sharing)
4. **Run the demo:**
```bash
streamlit run app.py
```

## Usage

- Open the app in the browser.
- Paste any text paragraph into the input box.
- Click Summarize.
- The model will generate a summary.

  


