import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import pandas as pd
import nltk

data = pd.read_csv('feedback_dataset.csv')
stopwords = nltk.download('stopwords')

X_test = data['text']
y_test = data['category']

#print(X_test.head())

# Preprocessing steps
def preprocess_text(text):
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters, punctuation, and numbers
    text = text.lower()  # Convert to lowercase
    return text


def tokenize_and_stem(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.lower() not in stop_words]

    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]

    return ' '.join(stemmed_tokens)



# Apply preprocessing to each text sample
preprocessed_texts = []
for text in X_test:
    preprocessed_texts.append(preprocess_text(text))

