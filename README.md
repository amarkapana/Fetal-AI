# Fetal AI Health Care Prediction
A web application built with Flask to predict fetal health conditions using machine learning based on CTG data.
## 🚀 Features
- Input form for 8 key CTG features
- Predicts: Normal, Suspect, or Pathological
- Real-time results using a trained ML model
## 🛠️ Tech Stack
- Backend: Python, Flask
- Frontend: HTML, CSS
- ML Model: Trained with scikit-learn, saved as fetal_health.pkl
- Dataset: fetal_health.csv from Kaggle
## 📁 Project Structure
├── app.py                   # Flask server logic
├── fetal_health.pkl         # Trained ML model
├── fetal_health.csv         # Original dataset
├── templates/
│   └── index.html           # Web form and result display
├── static/
│   └── css/
│       └── style.css        # Optional styling
└── README.md
## 🧪 How to Run
1. Install dependencies:
pip install flask numpy scikit-learn
2. Update model path in app.py:
Replace:
with open(r'C:\Users\user\Documents\Fetal AI\fetal_health.pkl', 'rb') as file:
With:
with open('fetal_health.pkl', 'rb') as file:
3. Run the app:
python app.py
4. Visit in browser: http://127.0.0.1:5000/
## 📥 Inputs
- Accelerations
- Prolongued Decelerations
- Abnormal Short-Term Variability
- % Abnormal Long-Term Variability
- Mean Long-Term Variability
- Histogram Mode
- Histogram Median
- Histogram Variance
## 📤 Output
- Normal
- Suspect
- Pathological
## 📊 About the Dataset
This project uses the Fetal Health Classification Dataset, which includes features derived from cardiotocograms of pregnant women to classify fetal status.
Source: https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification
