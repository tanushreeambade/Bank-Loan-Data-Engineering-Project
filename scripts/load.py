from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def load_data(df):

    url = URL.create(
        drivername="postgresql+psycopg2",
        username="postgres",
        password="@*tanushree06*",
        host="localhost",
        port=5432,
        database="bank_loan_db"
    )

    engine = create_engine(url)

    df.to_sql(
        "bank_loan_data",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("\nData Loaded Successfully into PostgreSQL!")