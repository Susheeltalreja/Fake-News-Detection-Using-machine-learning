# -*- coding: utf-8 -*-
"""FakeNewsDetection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xG2xVdF_vceirOdhVtMifMzKs8OTTfSd
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import re
import string

fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

"""Insert the labeling in the CSV file table fake = 0 and true = 1"""

true['label'] = 1

fake['label'] = 0

true.head()

fake.head()

"""news = pd.concat([fake, true], axis = 0) use for merge 2 files in one fake and true"""

news = pd.concat([fake, true], axis = 0)

news.head()

news.tail()

news.isnull().sum()

"""news = news.drop(['title', 'subject','date'], axis = 1) use for remove 3 coloumns from data"""

news = news.drop(['title', 'subject','date'], axis = 1)

news.head()

"""Use for reshuffle the date which will be mixed of fake and true"""

news = news.sample(frac = 1)

news.head()

"""When you modify a DataFrame (like removing rows, filtering data, etc.), the row numbers (called index) can get messed up or be out of order. reset_index() fixes this problem by giving the DataFrame new index numbers starting from 0, 1, 2, and so on."""

news.reset_index(inplace=True)

news.head()

news.drop(['index'], axis = 1, inplace = True)

news.head()

"""This function cleans text data by removing unnecessary elements like URLs, HTML tags, punctuation, numbers, and newline characters."""

def wordopt(text):
  #convert into lowercase
  text = text.lower()
  #Remove URLs and replacce with nothing
  text = re.sub(r'https?://\S+|www\.\S+', '' ,text)

  #Remove HTML Tags
  text = re.sub(r'<.*?>', '', text)

  #Remove punctuation
  text = re.sub(r'[^\w\s]', '', text)

  #Remove digits
  text = re.sub(r'\d', '', text)

  #Remove newline Characters
  text = re.sub(r'\n', '', text)

  return text

news['text'] = news['text'].apply(wordopt)

news['text']

x = news['text']
y = news['label']

x

y

"""Divide a data in 2 parts one is training and other one is testing and the test size is 0.3 means 30% of the data goes to testing"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

x_train.shape

x_test.shape

vectorization = TfidfVectorizer()

xv_train = vectorization.fit_transform(x_train)

xv_test = vectorization.transform(x_test)

xv_train

xv_test

LR = LogisticRegression()

LR.fit(xv_train, y_train)

pred_lr = LR.predict(xv_test)

LR.score(xv_test, y_test)

print(classification_report(y_test, pred_lr))

Dtc = DecisionTreeClassifier()

Dtc.fit(xv_train, y_train)

predicted_Dtc = Dtc.predict(xv_test)

Dtc.score(xv_test, y_test)

print(classification_report(y_test, predicted_Dtc))

rfc = RandomForestClassifier()

rfc.fit(xv_train, y_train)

predicted_rfc = rfc.predict(xv_test)

rfc.score(xv_test, y_test)

print(classification_report(y_test, predicted_rfc))

gbc = GradientBoostingClassifier()

gbc.fit(xv_train, y_train)

predicted_gbc = gbc.predict(xv_test)

gbc.score(xv_test, y_test)

print(classification_report(y_test,predicted_gbc))

def output_label(n):
  if n == 0:
    return "It is a fake news"
  elif n == 1:
    return "It is a true news"
  else:
    return "Invalid news"

def is_valid_news(news):
    """Check if the input news is valid."""
    if len(news.split()) < 3:  # Too short
        return False
    return True

def is_news_presentInDS(news, new_data):
  if news not in new_data["text"].values:
    print("Invalid news ❌. This news is not present in the dataset.")
    return False
  else:
    return True

def manual_testing(news):
  testing_news = {"text": [news]}
  new_def_test = pd.DataFrame(testing_news)
  new_def_test["text"] = new_def_test["text"].apply(wordopt)
  new_x_test = new_def_test["text"]
  new_xv_test = vectorization.transform(new_x_test)
  pred_lr = LR.predict(new_xv_test)
  predicted_Dtc = Dtc.predict(new_xv_test)
  predicted_rfc = rfc.predict(new_xv_test)
  predicted_gbc = gbc.predict(new_xv_test)

  # 4️⃣ Confidence Check
  prob_lr = max(LR.predict_proba(new_xv_test)[0])  # max probability for LR
  prob_dtc = max(Dtc.predict_proba(new_xv_test)[0])  # max probability for DTC
  prob_rfc = max(rfc.predict_proba(new_xv_test)[0])  # max probability for RFC
  prob_gbc = max(gbc.predict_proba(new_xv_test)[0])  # max probability for GBC

  #Check the probability of news
  if prob_lr < 0.6 and prob_dtc < 0.6 and prob_rfc < 0.6 and prob_gbc < 0.6:
    return print("❌ Invalid news. The model is not confident about this input.")

  return print("\n\n✅ LR Prediction: {} \n✅ DTC Prediction: {} \n✅ RFC Prediction: {} \n✅ GBC Prediction: {}".format(
      output_label(pred_lr[0]),
      output_label(predicted_Dtc[0]),
      output_label(predicted_rfc[0]),
      output_label(predicted_gbc[0])
  ))

while True:
  new_data = pd.concat([fake, true], axis = 0)
  news_article = str(input("Put your news here! \n"))
  if news_article == 'Exit' or news_article == 'exit' or news_article == 'e':
    print('Thank you for using')
    break
  elif not is_valid_news(news_article):
    print("❌ Invalid news. The input does not look like valid news text.")
  elif is_news_presentInDS(news_article, new_one):
    manual_testing(news_article)
  else:
    print('Invalid input\n')
  print('Type Exit or e for end\n')




