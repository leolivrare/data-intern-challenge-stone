from connection import *
import pandas as pd

def get_customers_average_age(db):
    df_customers = pd.DataFrame(db.select_table("customers"))
    return df_customers[1].mean()

def get_card_family_limit_analisys(db):
    df_cards = pd.DataFrame(db.select_table("cards"))
    df_cards.columns = ['Card Number', 'Card Family', 'Card Limit', 'Customer ID']
    group = df_cards[['Card Family', 'Card Limit']].groupby('Card Family')

    df_group_description = group.describe()['Card Limit'][['mean', 'std', 'min', 'max']]
    df_group_description.columns = ['Mean (R$)', 'Std (R$)', 'Minimum Value (R$)', 'Maximum Value (R$)']
    df_group_description['Mean (R$)'] = df_group_description['Mean (R$)'].apply(lambda x : round(x, 2))
    df_group_description['Std (R$)'] = df_group_description['Std (R$)'].apply(lambda x : round(x, 2))
    return df_group_description

def get_highest_value_fraud_id(db):
    df_trans_value = pd.DataFrame(db.select_table("transactions"))[[0, 3]]
    df_frauds = pd.DataFrame(db.select_table("frauds"))

    df_frauds_value = pd.merge(df_trans_value, df_frauds, how = 'inner', on = 0)
    df_frauds_value.columns = ['id', 'value', 'fraud flag']

    max_value = df_frauds_value['value'].max()
    return df_frauds_value[df_frauds_value['value'] == max_value]['id']

def get_most_expensive_frauds(db):
    df_trans = pd.DataFrame(db.select_table('transactions'))
    df_frauds = pd.DataFrame(db.select_table('frauds'))

    df_frauds_trans = pd.merge(df_trans, df_frauds, how = 'inner', on = 0)
    df_frauds_trans.columns = ['Fraud ID', 'Card Number', 'Date', 'Value', 'Segment', 'Fraud Flag']

    df_frauds_trans.sort_values(by = 'Value', ascending=False, inplace=True)
    
    return df_frauds_trans.head()
