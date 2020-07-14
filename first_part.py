from connection import *
import pandas as pd

def customers_average_age(db):
    df_customers = pd.DataFrame(db.select_table("customers"))
    return df_customers[1].mean()

def card_family_limit_analisys(db):
    df_cards = pd.DataFrame(db.select_table("cards"))
    group_average = df_cards[[1, 2]].groupby(1)
    group_average.mean().columns = ["Average Limit"]
    print("The average of credit limits of each card family is:")
    print(group_average.mean())

