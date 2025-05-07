
import streamlit as st
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier

# Function to clean resume text
def clean_resume(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'RT|cc', '', text)  # Remove RT and cc
    text = re.sub(r'#\S+', '', text)  # Remove hashtags
    text = re.sub(r'@\S+', '', text)  # Remove mentions
    text = re.sub(r'[^\w\s]', ' ', text)  # Remove punctuations
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    return text.strip()

# Streamlit UI
st.title("Resume Screening App")
st.write("Upload a CSV file with 'Resume' and 'Category' columns.")

uploaded_file = st.file_uploader("Upload a Resume CSV", type="csv")

if uploaded_file:
    try:
        # Load data
        data = pd.read_csv(uploaded_file)

        if 'Resume' not in data.columns or 'Category' not in data.columns:
            st.error("CSV must contain 'Resume' and 'Category' columns.")
        else:
            st.subheader("Data Preview")
            st.dataframe(data.head())

            # Preprocess resumes
            data['cleaned_resume'] = data['Resume'].apply(clean_resume)

            # TF-IDF vectorization
            vectorizer = TfidfVectorizer(stop_words='english', max_features=1500)
            X = vectorizer.fit_transform(data['cleaned_resume'])
            y = data['Category']

            # Train the model
            clf = OneVsRestClassifier(KNeighborsClassifier())
            clf.fit(X, y)

            st.success("✅ Model trained successfully!")

            # Predict a new resume
            st.subheader("Predict Resume Category")
            new_resume = st.text_area("Paste a new resume below for prediction:")

            if new_resume:
                cleaned_input = clean_resume(new_resume)
                X_new = vectorizer.transform([cleaned_input])
                prediction = clf.predict(X_new)
                st.write("🧠 Predicted Category:", prediction[0])

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
