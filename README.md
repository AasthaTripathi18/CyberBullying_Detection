Project Overview

This project presents an intelligent Cyberbullying Detection System that identifies toxic and abusive comments on online platforms using Natural Language Processing (NLP) and Machine Learning techniques.
The system automatically analyzes user comments and classifies them as Cyberbullying or Safe. Harmful comments can be blocked or flagged before being posted, helping create safer digital environments.
The application is deployed using Streamlit to provide an interactive web interface for real-time cyberbullying detection.

Objectives

1.Detect toxic and abusive comments in online text.
2.Classify comments into Cyberbullying or Normal categories.
3.Prevent harmful language from being posted on digital platforms.
4.Compare multiple machine learning algorithms.
5.Build a deployable real-time detection system.

Datasets Used

Datasets are too large to upload to GitHub.They can be downloaded from:
1. Hate Speech and Offensive Language Dataset
https://www.kaggle.com/datasets/mrmorj/hate-speech-and-offensive-language-dataset
2. Toxic Comment Classification Dataset
https://www.kaggle.com/datasets/julian3833/jigsaw-toxic-comment-classification-challenge

These datasets contain comments labeled as toxic, offensive, hate speech or normal.

Technologies Used

1.Python
2.Natural Language Processing (NLP)
3.Machine Learning
4.TF-IDF Vectorization
5.Streamlit Web Application

Libraries used:

1.pandas
2.numpy
3.nltk
4.scikit-learn
5.matplotlib
6.seaborn
7.wordcloud
8.streamlit
9.pickle

Machine Learning Models

The following models were implemented and compared:

1.Naive Bayes
2.Logistic Regression
3.Support Vector Machine (SVM)

The Support Vector Machine (SVM) achieved the best performance and was selected as the final cyberbullying detection model.

Project Workflow

1.Data Collection and Dataset Loading
2.Data Integration and Label Standardization
3.Data Cleaning and Text Preprocessing
->Lowercasing
->Removing URLs and special characters
->Stopword removal
4.Feature Extraction using TF-IDF Vectorization
5.Train-Test Data Split
6.Model Training, Comparison and Selection
7.Performance Evaluation
8.Visualization and Analysis
9.Model Saving using Pickle
10.Real-time Prediction using Streamlit

Model Evaluation Metrics

1.Accuracy
2.Precision
3.Recall
4.F1 Score
5.Confusion Matrix
6.ROC Curve
7.Overfitting Analysis

Visualizations

1.Cyberbullying vs Normal Comment Distribution
2.Most Frequent Words Analysis
3.WordCloud of Toxic Comments
4.Confusion Matrix
5.Model Accuracy Comparison
6.ROC Curve

Streamlit Web Application

The project includes a Streamlit interface for live testing.

Example Detection

Input comment:
"You are ugly and useless"

Output:
🚫 Cyberbullying Detected – Comment Blocked

