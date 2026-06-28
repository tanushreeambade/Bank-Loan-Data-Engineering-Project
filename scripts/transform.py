import pandas as pd


def transform_data(df):

    print("\n========== TRANSFORM ==========")

    # =====================================================
    # Handle Missing Values
    # =====================================================

    df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
    df["Married"] = df["Married"].fillna(df["Married"].mode()[0])
    df["Dependents"] = df["Dependents"].fillna(df["Dependents"].mode()[0])
    df["Self_Employed"] = df["Self_Employed"].fillna(df["Self_Employed"].mode()[0])

    df["LoanAmount"] = df["LoanAmount"].fillna(df["LoanAmount"].median())
    df["Loan_Amount_Term"] = df["Loan_Amount_Term"].fillna(df["Loan_Amount_Term"].median())
    df["Credit_History"] = df["Credit_History"].fillna(df["Credit_History"].mode()[0])

    print("\nMissing Values After Cleaning")
    print("=" * 30)
    print(df.isnull().sum())

    # =====================================================
    # Feature Engineering
    # =====================================================

    # Total Income
    df["TotalIncome"] = (
        df["ApplicantIncome"] +
        df["CoapplicantIncome"]
    )

    # Income Category
    df["Income_Category"] = pd.cut(
        df["TotalIncome"],
        bins=[0, 4000, 7000, 100000],
        labels=["Low", "Medium", "High"],
        include_lowest=True
    )

    # Loan Category
    df["Loan_Category"] = pd.cut(
        df["LoanAmount"],
        bins=[0, 100, 200, 1000],
        labels=["Small", "Medium", "Large"],
        include_lowest=True
    )

    print("\nFeature Engineering Preview")
    print("=" * 30)
    print(
        df[
            [
                "TotalIncome",
                "Income_Category",
                "Loan_Category"
            ]
        ].head()
    )

    # =====================================================
    # Rename Columns (snake_case)
    # =====================================================

    df = df.rename(columns={

        "Loan_ID": "loan_id",
        "Gender": "gender",
        "Married": "married",
        "Dependents": "dependents",
        "Education": "education",
        "Self_Employed": "self_employed",

        "ApplicantIncome": "applicant_income",
        "CoapplicantIncome": "coapplicant_income",

        "LoanAmount": "loan_amount",
        "Loan_Amount_Term": "loan_amount_term",

        "Credit_History": "credit_history",

        "Property_Area": "property_area",

        "Loan_Status": "loan_status",

        "TotalIncome": "total_income",

        "Income_Category": "income_category",

        "Loan_Category": "loan_category"

    })

    print("\nColumns After Renaming")
    print("=" * 30)
    print(df.columns)

    print("\nTransformation Completed!")

    return df

