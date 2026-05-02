# Phishing-Email-Classification-and-Analysis

Using the "zefang-liu/phishing-email-dataset" dataset from Hugging Face, our team built four models (TF-IDF+Logestic Regression, BERT, RoBERTa, and T5) to test various model complexities and architectures to create a high performing classifier and build insight into common patterns in phishing and safe emails.

Notebooks included and steps:
1. Preprocessing: look at our shared preprocessing method for the data
2. Deduplication_and_Leakage_Analysis: check for data leakage in dataset
3. LDA_Topic_Modeling: find topics in safe and phishing emails
4. TF-IDF+LR_final: build the TFIDF+LR model
5. BERT_implementation_NLP_Project: build BERT transfer learning model
6. ROBERTA_training_evaluation: build RoBERTa transfer learning model
7. RoBERTa_phishing_project_shap: interpretability for RoBERTa model
8. T5_notebook: build the T5 model
9. NLP Phishing-Main notebook:evaluating model performance and created demo
