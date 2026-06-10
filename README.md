# 📧 Email Spam Detection using Python

## 📌 Overview

Email Spam Detection is a machine learning project developed using Python that classifies emails as **Spam** or **Ham (Not Spam)**. The project uses Natural Language Processing (NLP) techniques to convert email text into numerical features and applies the **Multinomial Naive Bayes** algorithm for classification.

This project demonstrates the fundamentals of text preprocessing, feature extraction, model training, and spam detection using machine learning.

---

## 🚀 Features

* Load and process email datasets from CSV files
* Convert text data into numerical features using CountVectorizer
* Train a Machine Learning model using Multinomial Naive Bayes
* Classify emails as Spam or Ham
* Evaluate model performance using accuracy metrics
* Beginner-friendly implementation

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-Learn
* CountVectorizer
* Multinomial Naive Bayes

---

## 📂 Project Structure

Email-Spam-Detection/

├── spam.csv

├── spam_detection.py

├── requirements.txt

└── README.md

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/suji2826/email-spam-detection.git
```

Navigate to the project folder:

```bash
cd email-spam-detection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Python script:

```bash
python spam_detection.py
```

The program will:

1. Load the email dataset
2. Process email text
3. Train the machine learning model
4. Classify emails as Spam or Ham
5. Display model performance metrics

---

## 📊 Dataset

The dataset contains email messages labeled as:

* **Spam** – Unwanted promotional or fraudulent emails
* **Ham** – Legitimate emails

Example:

| Label | Email Text                             |
| ----- | -------------------------------------- |
| Spam  | Congratulations! You won a free iPhone |
| Ham   | Can we meet tomorrow?                  |

---

## 🎯 Learning Outcomes

Through this project, you will learn:

* Data preprocessing using Pandas
* Text vectorization using CountVectorizer
* Machine Learning model training
* Spam classification techniques
* Model evaluation and accuracy analysis

---

## 📈 Future Enhancements

* Larger email dataset
* Advanced NLP preprocessing
* TF-IDF Vectorization
* GUI using Tkinter
* Real-time email classification
* Model deployment using Flask

---

## 👨‍💻 Author

**Sujitha S**
B.Tech Artificial Intelligence & Data Science (AI & DS)

This mini project was developed as part of the **"Python Using ML, AI & DS"** training program conducted by **CodeBind Technologies**. The project demonstrates the application of Machine Learning techniques for email spam classification using Python, Scikit-Learn, and Natural Language Processing concepts.

Through this project, I gained hands-on experience in data preprocessing, text vectorization, machine learning model development, and classification techniques used in real-world spam detection systems.
