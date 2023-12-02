from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from tensorflow.keras.datasets import imdb
# from tensorflow.keras.preprocessing import sequence
import joblib

# Load the IMDB dataset
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)

# # Preprocess the data
# max_review_length = 500
# x_train = sequence.pad_sequences(x_train, maxlen=max_review_length)
# x_test = sequence.pad_sequences(x_test, maxlen=max_review_length)

# Convert the sequence data back to text
word_index = imdb.get_word_index()
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

def decode_review(sequence):
    return ' '.join([reverse_word_index.get(i, '?') for i in sequence])

# Convert sequences to text
x_train_text = [decode_review(seq) for seq in x_train]
x_test_text = [decode_review(seq) for seq in x_test]

# Use TF-IDF to convert text to numerical features
vectorizer = TfidfVectorizer(max_features=10000)
x_train_tfidf = vectorizer.fit_transform(x_train_text)
x_test_tfidf = vectorizer.transform(x_test_text)

print("Fitting the model..")
# Train KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train_tfidf, y_train)

print("Making the predictions...")
# Predict on the test set
y_pred = knn.predict(x_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: {:.2f}%".format(accuracy * 100))

joblib.dump(knn, 'knn_for_SA.joblib')