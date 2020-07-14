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

    print("The maximum credit limit of each card family is:")
    print(group_average.max())

    print("The minimum credit limit of each card family is:")
    print(group_average.min())


def highest_value_fraud_id(db):
    df_trans_value = pd.DataFrame(db.select_table("transactions"))[[0, 3]]
    df_frauds = pd.DataFrame(db.select_table("frauds"))

    df_frauds_value = pd.merge(df_trans_value, df_frauds, how = 'inner', on = 0)
    df_frauds_value.columns = ['id', 'value', 'fraud flag']

    max_value = df_frauds_value['value'].max()

    return df_frauds_value[df_frauds_value['value'] == max_value]['id']

