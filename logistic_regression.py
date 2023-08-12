import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


def logistic_regression(loan_data):
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        loan_data.drop("Loan_Status", axis=1),
        loan_data["Loan_Status"],
        test_size=0.2,
        random_state=42,
    )

    # Standardize data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Create and Train the model
    logreg = LogisticRegression(max_iter=1000)
    logreg.fit(X_train, y_train)

    # Make predictions on testing data
    y_pred = logreg.predict(X_test)

    # Calculate accuracy of model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy of logistic regression model: {accuracy:.2f}")

    return logreg, scaler


# Predictive Analysis
def predict_sample(logreg, scaler, sample_data):
    import warnings

    warnings.filterwarnings(action="ignore", category=UserWarning)

    sample_data_scaled = scaler.transform(sample_data)
    prediction = logreg.predict(sample_data_scaled)
    return "Approved" if prediction[0] == 1 else "Not Approved"
