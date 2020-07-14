from connection import *
import pandas as pd

def customers_average_age(db):
    df_customers = pd.DataFrame(db.select_table("customers"))
    return df_customers[1].mean()
