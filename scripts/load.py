def load_data(df):

    print("\n========== LOAD ==========")

    df.to_csv("data/bank_loan_cleaned.csv", index=False)

    print("Clean dataset saved successfully!")