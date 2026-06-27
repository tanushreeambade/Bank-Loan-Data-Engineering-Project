import pandas as pd

def transform_data(df):

    print("\n========== TRANSFORM ==========")

    # Fill categorical columns
    df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
    df["Married"] = df["Married"].fillna(df["Married"].mode()[0])
    df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])
    df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])
    df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])

    # Fill numerical columns
    df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].median())
    df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].median())

    # Feature Engineering
    df["TotalIncome"] = df["ApplicantIncome"] + df["CoapplicantIncome"]

    df["Income_Category"] = pd.cut(
        df["TotalIncome"],
        bins=[0,3000,6000,9000,100000],
        labels=["Low","Medium","High","Very High"],
        include_lowest=True
    )

    df["Loan_Category"] = pd.cut(
        df["LoanAmount"],
        bins=[0,100,200,700],
        labels=["Small","Medium","Large"],
        include_lowest=True
    )

    print("Transformation Completed!")

    return df