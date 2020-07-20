from connection import *
import pandas as pd

def customers_average_age(db):
    df_customers = pd.DataFrame(db.select_table("customers"))
    return df_customers[1].mean()

def card_family_limit_analisys(db):
    df_cards = pd.DataFrame(db.select_table("cards"))
    df_cards.columns = ['Card Number', 'Card Family', 'Card Limit', 'Customer ID']
    group = df_cards[['Card Family', 'Card Limit']].groupby('Card Family')

    group_description = group.describe()['Card Limit'][['mean', 'std', 'min', 'max']]
    group_description.columns = ['Mean (R$)', 'Std (R$)', 'Minimum Value (R$)', 'Maximum Value (R$)']
    return group_description

def highest_value_fraud_id(db):
    df_trans_value = pd.DataFrame(db.select_table("transactions"))[[0, 3]]
    df_frauds = pd.DataFrame(db.select_table("frauds"))

    df_frauds_value = pd.merge(df_trans_value, df_frauds, how = 'inner', on = 0)
    df_frauds_value.columns = ['id', 'value', 'fraud flag']

    max_value = df_frauds_value['value'].max()
    return df_frauds_value[df_frauds_value['value'] == max_value]['id']

def most_expensive_frauds(db):
    df_trans = pd.DataFrame(db.select_table('transactions'))
    df_frauds = pd.DataFrame(db.select_table('frauds'))

    df_frauds_trans = pd.merge(df_trans, df_frauds, how = 'inner', on = 0)
    df_frauds_trans.columns = ['Fraud ID', 'Card Number', 'Date', 'Value (R$)', 'Segment', 'Fraud Flag']

    df_frauds_trans.sort_values(by = 'Value', ascending=False, inplace=True)
    return df_frauds_trans.head()
