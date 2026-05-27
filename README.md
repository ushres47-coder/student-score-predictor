# Student Score Predictor

A beginner-friendly machine learning project that predicts a student's final exam score using **Linear Regression**.

## Project Objective

This project predicts a student's **final score** based on:
- Study hours
- Attendance percentage
- Sleep hours
- Previous score

It is a great first portfolio project for anyone learning:
- Python
- Pandas
- Scikit-learn
- Basic machine learning workflow

---

## Project Structure

```
student-score-predictor/
├── data.csv
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- Scikit-learn

---

## Dataset Columns

- `study_hours` → number of hours studied
- `attendance` → attendance percentage
- `sleep_hours` → average hours of sleep
- `previous_score` → previous exam/test score
- `final_score` → target value to predict

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-score-predictor.git
cd student-score-predictor
```

### 2. Create a virtual environment (optional but recommended)

**Windows**
```bash
python -m venv venv
venv\Scriptsctivate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the project

```bash
python main.py
```

---

## Example Output

```bash
Model Evaluation
----------------
Mean Absolute Error: 2.35
R2 Score: 0.91

New Prediction
--------------
Predicted Final Score: 77.84
```

> Note: Output values may vary slightly depending on how the train/test split is performed.

---

## Skills Demonstrated

- Loading and working with CSV data using Pandas
- Splitting data into training and testing sets
- Training a machine learning model with Scikit-learn
- Evaluating model performance using MAE and R2 score
- Predicting outcomes for new input data

---

## Resume / Portfolio Description

**Resume bullet:**

Built a **Student Score Predictor** using **Python, Pandas, and Scikit-learn** to forecast final exam scores based on study hours, attendance, sleep, and previous academic performance.

**GitHub description:**

Beginner machine learning project using linear regression to predict student exam scores from academic habits and previous performance.

---

## Future Improvements

- Add data visualization with Matplotlib
- Save the trained model using Joblib
- Accept user input from the terminal
- Build a simple web app version using Streamlit or Flask

---

## License

This project is open for learning and portfolio use.
