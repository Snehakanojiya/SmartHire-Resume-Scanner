 SmartHire ResumeScanner

SmartHire ResumeScanner is an AI-powered resume screening tool designed to streamline the recruitment process. This project leverages machine learning algorithms to analyze and classify resumes, helping hiring managers quickly identify top talent. The tool uses natural language processing (NLP) techniques to extract and evaluate key skills, experience, and qualifications, providing a fast and efficient way to filter candidates.

 Features

-Automated Resume Screening**: The tool automatically reads, processes, and categorizes resumes to help hiring managers save time.
-Machine Learning Models**: Trains on a labeled dataset of resumes, predicting the best-suited job category for a candidate.
-Text Preprocessing**: Cleans and processes resume content by removing URLs, special characters, and unnecessary whitespace.
-AI-Driven Recommendations**: Categorizes resumes based on key skills, job roles, and qualifications.
-Interactive Web Interface**: Built with Streamlit, allowing easy resume upload and prediction for single candidates.

 Getting Started

To run this project locally, follow these steps:

-Prerequisites

Make sure you have Python 3.x installed and have the following libraries:

-pandas
-sklearn
-joblib
-nltk
-streamlit
-wordcloud
-matplotlib
-seaborn

You can install the dependencies using pip:

bash
pip install pandas scikit-learn joblib nltk streamlit wordcloud matplotlib seaborn


Installation

1. Clone this repository to your local machine:

   bash
   git clone https://github.com/yourusername/smarthire-resumescanner.git
   

2. Navigate to the project directory:

   bash
   cd smarthire-resumescanner
   

3. Install the necessary dependencies:

   bash
   pip install -r requirements.txt
   

4. To run the Streamlit app, use the following command:

   bash
   streamlit run app.py
   

 Usage

1. Upload CSV File: Upload a CSV file containing resumes (with columns for 'Resume' and 'Category').
2. Train Model: Once the data is uploaded, the model will train and categorize resumes.
3. Prediction: Paste a new resume to get an AI-powered prediction for the category.

 Example

Here’s an example of a resume prediction:

1. Upload CSV: Upload a sample CSV with resume data.
2. Prediction: Paste a resume into the input field to predict the job category.


Example Project Flow:

1. Data Preprocessing: Resumes are cleaned (removing URLs, punctuation, etc.) using regular expressions and natural language processing (NLP) techniques.
2. Model Training: The data is used to train a machine learning model, which can categorize resumes into job roles.
3. Prediction: The trained model allows for categorizing new resumes, offering a rapid method for hiring managers.

Technologies Used

- Python: The main programming language for data processing, model training, and building the web app.
- Streamlit: A framework for building interactive web applications for machine learning.
- Scikit-learn: A machine learning library used for classification algorithms.
- NLP: Natural language processing techniques for cleaning and processing resumes.
- TfidfVectorizer: Used to convert resume text into numerical data suitable for machine learning models.

Contributing

Contributions are welcome! If you want to improve this project, feel free to fork this repository, make your changes, and submit a pull request. Any suggestions for improving the model or enhancing the user interface are highly appreciated!

