from keras.datasets import imdb
import joblib
from sklearn.metrics import accuracy_score

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)

word_index = imdb.get_word_index()

# Reverse the word index mapping
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# Decode a review from integer indices to words
def decode_review(indices):
    return ' '.join([reverse_word_index.get(i - 3, '') for i in indices])

decoded_reviews = []
for review in x_test:
  decoded_reviews.append(decode_review(review))

vectorizer = joblib.load('vectorizer.joblib')
# Preprocess and vectorize the user data
test_data = vectorizer.transform(decoded_reviews)

# svm_model = joblib.load('svm_model.joblib')
# print("Making predictions...")
# predictions = svm_model.predict(test_data)
#
# print("Calculating the accuracy..")
# # Calculate accuracy
# accuracy = accuracy_score(y_test, predictions)

lr = joblib.load('logreg_model.joblib')
print("Making predictions with lr model...")

predictions = lr.predict(test_data)
accuracy = accuracy_score(y_test, predictions)
# Print the accuracy
print(f"Accuracy: {accuracy * 100:.2f}%")