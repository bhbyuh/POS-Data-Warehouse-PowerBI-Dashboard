import psycopg2
import pandas as pd
from psycopg2.extras import execute_values

conn = psycopg2.connect("dbname=POS user=postgres password=123 host=localhost port=5432")
cur = conn.cursor()


def load_dim_date(dim_date):
    sql = """
    INSERT INTO dim_date (date_id, date, year, month, day, day_of_week, quarter)
    VALUES %s
    """
    tuples = list(dim_date[['date_id','date','year','month','day','day_of_week','quarter']].itertuples(index=False, name=None))
    execute_values(cur,sql, tuples)
    conn.commit()


def load_dim_payment_method(dim_payment_method):
    sql = """
    INSERT INTO dim_payment_method (payment_method_id, payment_method)
    VALUES %s
    """
    tuples = list(dim_payment_method[['payment_method_id','payment_method']].itertuples(index=False, name=None))
    execute_values(cur,sql, tuples)
    conn.commit()


def load_dim_item(dim_item):
    sql = """
    INSERT INTO dim_item (item_id, item_category, item_name, price)
    VALUES %s
    """
    tuples = list(dim_item[['item_id','item_category','item_name','price']].itertuples(index=False, name=None))
    execute_values(cur,sql, tuples)
    conn.commit()


def load_dim_customer(dim_customer):
    sql = """
    INSERT INTO dim_customer (customer_id, customer_name)
    VALUES %s
    """
    tuples = list(dim_customer[['customer_id','customer_name']].itertuples(index=False, name=None))
    execute_values(cur,sql, tuples)
    conn.commit()


def load_fact_sales(fact_sales):
    sql = """
    INSERT INTO fact_sales 
      (timestamp, date_id, customer_id, item_id, payment_method_id, quantity, price_per_item, total_price)
    VALUES %s;
    """
    tuples = list(fact_sales[['Timestamp','date_id','customer_id','item_id','payment_method_id','quantity','price_per_item','total_price']]
                  .itertuples(index=False, name=None))
    execute_values(cur,sql, tuples)
    conn.commit()


if __name__ == '__main__':
    dim_customer=pd.read_csv("data/dim_customer.csv")
    dim_date=pd.read_csv("data/dim_date.csv")
    dim_item=pd.read_csv("data/dim_item.csv")
    dim_payment_method=pd.read_csv("data/dim_payment_method.csv")
    fact_sales=pd.read_csv("data/fact_sales.csv")

    load_dim_customer(dim_customer)
    load_dim_date(dim_date)
    load_dim_payment_method(dim_payment_method)
    load_dim_item(dim_item)
    load_fact_sales(fact_sales)