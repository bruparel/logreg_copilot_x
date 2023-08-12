import pandas as pd


def generate_descriptive_statistics(loan_data, filename):
    with open(f"{filename}.txt", "w") as f:
        # Check for missing values
        missing_values = loan_data.isnull().sum().sum()
        f.write(f"Number of missing values: {missing_values}\n")

        # Calculate percentage of female applicants that had their loan approved
        female_approved = (
            loan_data[loan_data["Gender"] == 2]["Loan_Status"].value_counts(
                normalize=True
            )[0]
            * 100
        )
        f.write(
            f"Percentage of female applicants that had their loan approved: {female_approved:.2f}%\n"
        )

        # Calculate average income of all applicants
        avg_income_all = loan_data["ApplicantIncome"].mean()
        f.write(f"Average income of all applicants: {avg_income_all:.2f}\n")

        # Calculate average income of all self-employed applicants
        avg_income_self_employed = loan_data[loan_data["Self_Employed"] == 1][
            "ApplicantIncome"
        ].mean()
        f.write(
            f"Average income of all self-employed applicants: {avg_income_self_employed:.2f}\n"
        )
