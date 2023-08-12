import pandas as pd


def clean_loan_data(loan_data):
    # Set Loan_ID as the index column
    loan_data.set_index("Loan_ID", inplace=True)

    # Remove duplicates if any
    loan_data.drop_duplicates(inplace=True)

    # Fill missing values
    loan_data["Gender"].fillna(loan_data["Gender"].mode()[0], inplace=True)
    loan_data["Married"].fillna(loan_data["Married"].mode()[0], inplace=True)
    loan_data["Dependents"].fillna(loan_data["Dependents"].mode()[0], inplace=True)
    loan_data["Self_Employed"].fillna(
        loan_data["Self_Employed"].mode()[0], inplace=True
    )
    loan_data["LoanAmount"].fillna(loan_data["LoanAmount"].mean(), inplace=True)
    loan_data["Loan_Amount_Term"].fillna(
        loan_data["Loan_Amount_Term"].mode()[0], inplace=True
    )
    loan_data["Credit_History"].fillna(
        loan_data["Credit_History"].mode()[0], inplace=True
    )

    # Encode categorical variables
    loan_data = encode_categorical_variables(loan_data)

    return loan_data


def encode_categorical_variables(loan_data):
    # Encode Loan_Status variable as binary variable
    loan_data["Loan_Status"] = loan_data["Loan_Status"].apply(
        lambda x: 1 if x == "Y" else 0
    )

    return loan_data


if __name__ == "__main__":
    # Clean loan data
    loan_data = clean_loan_data()
