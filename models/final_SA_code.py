from keras.datasets import imdb
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
import joblib
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

# Load the IMDB dataset
# num_words specifies the number of most frequent words to keep in the vocabulary
# Words less frequent than num_words will be discarded.
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)

word_index = imdb.get_word_index()

# Reverse the word index mapping
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

# Decode a review from integer indices to words
def decode_review(indices):
    return ' '.join([reverse_word_index.get(i - 3, '') for i in indices])

decoded_reviews = []
for review in x_train:
  decoded_reviews.append(decode_review(review))

decoded_xtest = []
for review in x_test:
  decoded_xtest.append(decode_review(review))

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(decoded_reviews)
'''
This is for training the model using svm and logistic regression
'''
# # Create and train the SVM model
# svm_model = SVC(kernel='linear')
# print("Training the model...")
# svm_model.fit(X_train, y_train)
# print("Model training is completed.")
# joblib.dump(svm_model, 'svm_model.joblib')
#
# logreg_model = LogisticRegression(max_iter=1000)
# print("Training the logistic regression model...")
# logreg_model.fit(X_train, y_train)
# print("Model training is completed.")
#
# # Save the logistic regression model
# joblib.dump(logreg_model, 'logreg_model.joblib')

'''
This is for training the model using the hyper parameter tuning
'''
# Define the parameter grid
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100]}

# Create an SVM model
svm_model = SVC(kernel='linear')

# Create a GridSearchCV object
print("Finding the best model...")
grid_search = GridSearchCV(estimator=svm_model, param_grid=param_grid, scoring='accuracy', cv=5)

print("Training the best model...")
# Fit the GridSearchCV object to the training data
grid_search.fit(X_train, y_train)

# Get the best parameters and the best model
best_params = grid_search.best_params_
best_model = grid_search.best_estimator_

joblib.dump(best_model, 'tuned_SVM_mode.joblib')