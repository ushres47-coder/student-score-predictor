import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_absolute_error, r2_score


    def load_data(file_path: str) -> pd.DataFrame:
        """Load the dataset from a CSV file."""
        return pd.read_csv(file_path)


    def train_model(data: pd.DataFrame):
        """Train a linear regression model and return the model and test results."""
        X = data[["study_hours", "attendance", "sleep_hours", "previous_score"]]
        y = data["final_score"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        return model, mae, r2


    def predict_score(model, study_hours: float, attendance: float, sleep_hours: float, previous_score: float) -> float:
        """Predict the final score for a new student."""
        new_student = pd.DataFrame({
            "study_hours": [study_hours],
            "attendance": [attendance],
            "sleep_hours": [sleep_hours],
            "previous_score": [previous_score]
        })
        return float(model.predict(new_student)[0])


    def main():
        data = load_data('data.csv')
        model, mae, r2 = train_model(data)

        print('Model Evaluation')
        print('----------------')
        print(f'Mean Absolute Error: {mae:.2f}')
        print(f'R2 Score: {r2:.2f}')

        predicted_score = predict_score(
            model,
            study_hours=5,
            attendance=85,
            sleep_hours=7,
            previous_score=72
        )

        print('
New Prediction')
        print('--------------')
        print(f'Predicted Final Score: {predicted_score:.2f}')


    if __name__ == '__main__':
        main()
