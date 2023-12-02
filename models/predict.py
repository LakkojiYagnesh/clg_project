import joblib
# Load the saved model and vectorizer
# svm_model = joblib.load('svm_model.joblib')
vectorizer = joblib.load('vectorizer.joblib')
lr_model = joblib.load('logreg_model.joblib')
# User-provided text data for prediction
user_text = "Hostel rooms are not clean and ugly"

# Preprocess and vectorize the user data
user_data_vectorized = vectorizer.transform([user_text])

# Make predictions using the loaded model
# prediction = svm_model.predict(user_data_vectorized)

prediction = lr_model.predict(user_data_vectorized)

# Print the prediction
if prediction[0] == 1:
    print("positive")
else:
    print("negative")
