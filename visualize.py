import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages


import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages


def visualize_loan_data(loan_data, filename):
    with PdfPages(f"{filename}.pdf") as pdf:
        # Visualization 1: Loan Status Distribution
        sns.countplot(x="Loan_Status", data=loan_data)
        plt.title("Loan Status Distribution")
        plt.xlabel("Loan Status")
        plt.ylabel("Count")
        pdf.savefig()
        plt.clf()

        # Visualization 2: Applicant Income Distribution
        sns.histplot(x="ApplicantIncome", data=loan_data, bins=20)
        plt.title("Applicant Income Distribution")
        plt.xlabel("Applicant Income")
        plt.ylabel("Count")
        pdf.savefig()
        plt.clf()

        # Visualization 3: Loan Amount Distribution
        sns.histplot(x="LoanAmount", data=loan_data, bins=20)
        plt.title("Loan Amount Distribution")
        plt.xlabel("Loan Amount")
        plt.ylabel("Count")
        pdf.savefig()
        plt.clf()

        # Visualization 4: Loan Status by Gender
        sns.countplot(
            x="Loan_Status",
            hue="Gender",
            data=loan_data.replace({"Gender": {1: "Male", 2: "Female"}}),
        )
        plt.title("Loan Status by Gender")
        plt.xlabel("Loan Status")
        plt.ylabel("Count")
        pdf.savefig()
        plt.clf()
