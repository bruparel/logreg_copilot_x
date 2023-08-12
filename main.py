from clean_data import clean_loan_data
from generate_statistics import generate_descriptive_statistics
from visualize import visualize_loan_data
from logistic_regression import logistic_regression, predict_sample
import pandas as pd

if __name__ == "__main__":
    # Load loan data into a pandas dataframe
    loan_data = pd.read_csv("loan_data.csv")
    # Clean loan data
    loan_data = clean_loan_data(loan_data)

    # Generate descriptive statistics for loan data
    generate_descriptive_statistics(loan_data, "loan_data_stats")
    # Visualize loan data
    visualize_loan_data(loan_data, "loan_data_charts")

    # Train and return the model to analyze loan applications using logistic regression
    logreg_model, data_scaler = logistic_regression(loan_data)

    # Sample Predictive Analysis Session
    sample_data = (
        loan_data.iloc[0].drop("Loan_Status").values.reshape(1, -1)
    )  # Using first row as a sample
    prediction_result = predict_sample(logreg_model, data_scaler, sample_data)
    print(prediction_result)
