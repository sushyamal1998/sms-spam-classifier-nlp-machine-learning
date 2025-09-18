# Sms Spam Detection
_This project implements a machine learning model to classify SMS/Email messages as Spam or Not Spam.<br>
It uses Natural Language Processing (NLP) techniques for text preprocessing and models like Logistic Regression, Naive Bayes, and SVM for classification._

---
## Contents
- <a href="#overview">Overview</a>
- <a href="#dataset">Dataset</a>
- <a href="#technologies--tools">Technologies & Tools</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-cleaning--preprocessing">Data Cleaning & Preprocessing</a>
- <a href="#model">Model</a>
- <a href="#results">Results</a>
- <a href="#conclusion">Conclusion</a>

---
<h2><a class="anchor" id="overview"></a>Overview</h2>

Spam detection is a critical task in modern communication systems. This project applies **machine learning** + **NLP techniques** to automatically classify incoming SMS messages into spam or ham (not spam).


---
<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- **Source:** Kaggle
- **Size:** 5574
- **Attributes:**
    - Text (spam/ham)
    - Target (sms text content)

---
<h2><a class="anchor" id="technologies--tools"></a>Technologies & Tools</h2>

- **Python** (pandas, numpy, scikit-learn, nltk)
- **NLP** (tokenization, stopword removal, stemming)
- **ML Models:** Logistic Regression, Naive Bayes, Support Vector Machine
- **Vectorization:** TF-IDF
- **Deployment:**
    - Flask (API)
- **Version Control:** Git/GitHub
- **Jupyter Notebook** for analysis

---
<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
sms-spam-detection/
│
├── README.md                        
├── notebooks/
│   └── sms_spam_detection.ipynb   
│
├── models/
│   ├── model.pkl            
│   └── vectorizer.pkl 
|      
├── templates/
│   └── index.html
|
├── app/
│   └── flask_app.py         
│
└── data/
    └── spam.csv            

```
--- 
<h2><a class="anchor" id="data-cleaning--preprocessing"></a>Data Cleaning & Preprocessing</h2>

- Convert text to lowercase
- Tokenization (split into words)
- Remove stopwords & punctuation
- Apply stemming (PorterStemmer)
- Vectorize using TF-IDF

---
<h2><a class="anchor" id="research-question--key-finding"></a>Research Queation & Key Finding</h2>

- **Top vendor with max profit:**  name DIAGEO NORTH AMERICA INC and profit 17780038.12
- **Brand for promotion:** 198 brands with low sales and high profit margin
- **Inventory Turnover:** Total unsold inventory 2.71M
- **Vendor Profibility:**
  - High vendors: Mean Margin = 31.17%
  - Low vendors: Mean Margin = 41.55%
- **Hypothesis Testing:** significant difference in mean profit margin of top performing and low performing vendor
  

---

<h2><a class="anchor" id="model"></a>Model</h2>

- Trained multiple models:
  - Logistic Regression
  - Naive Bayes (GNB, MNB, BNB)
  - Support Vector Machine
Best model was saved as model.pkl (MNB)

---

<h2><a class="anchor" id="results"></a>Results</h2>

- multinomial naive bayes gives accuracy ~ 97% and precision score ~ 99.98%
- logistic regression give accuracy ~ 95% and precision score ~ 97%
- svm give accuracy ~ 97% and precision score ~ 97%
- KNN give accuracy ~ 90% and precision score ~ 99%
--

<h2><a class="anchor" id="conclusions"></a>Conclusions</h2>

- This project demonstrates how **NLP + ML** models can be applied to detect spam messages effectively.
