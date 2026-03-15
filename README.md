Project Overview

This project aims to detect cyberbullying and toxic comments on online platforms using Natural Language Processing (NLP) and Machine Learning.
The system analyzes user comments and identifies whether they contain abusive, offensive, or harmful language.
If cyberbullying is detected, the comment can be blocked or flagged automatically.

Objectives

1. Detect toxic and abusive comments in online text.
2. Classify comments into cyberbullying or normal categories.
3. Prevent harmful language from being posted on digital platforms.

Datasets Used

The project uses two publicly available datasets:
1. Toxic Comment Classification Dataset
2. Hate Speech and Offensive Language Dataset

These datasets contain comments labeled as toxic, offensive, or normal.

Technologies Used

1.Python
2.Natural Language Processing (NLP)
3.Machine Learning
4.TF-IDF Vectorization

Libraries used:

1.pandas
2.numpy
3.nltk
4.scikit-learn
5.matplotlib
6.seaborn

Machine Learning Models

The following models were implemented and compared:

1.Naive Bayes
2.Logistic Regression
3.Support Vector Machine (SVM)

The model with the highest accuracy was selected for cyberbullying detection.

Project Workflow

1.Data collection and dataset loading
2.Data preprocessing (cleaning text, removing stopwords)
3.Feature extraction using TF-IDF
4.Training machine learning models
5.Evaluating model performance
6.Detecting cyberbullying comments

Visualizations

The project includes several visualizations such as:
1.Cyberbullying vs normal comment distribution
2.Most frequent words in comments
3.Confusion matrix
4.Model accuracy comparison

Example Detection

Input comment:
"You are ugly and useless"

Output:
Cyberbullying detected – Comment Blocked

