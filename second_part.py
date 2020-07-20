import pandas as pd
from connection import *

def analyse_fraudulent_transactions(db):
    df_frauds_trans = get_frauds_transactions(db)
    
    analyse_value(df_frauds_trans)

    df_fraud_rate_seg = get_fraud_rate_segments(df_frauds_trans)
    df_fraud_rate_month = get_fraud_rate_month(df_frauds_trans)
    df_fraud_rate_seg.to_csv(r'fraud_rate_seg.csv')
    df_fraud_rate_month.to_csv(r'fraud_rate_month.csv')
    
    print("\n{}".format(df_fraud_rate_seg))
    print("\n{}".format(df_fraud_rate_month))

def get_frauds_transactions(db):
    df_trans = pd.DataFrame(db.select_table("transactions"))
    df_frauds = pd.DataFrame(db.select_table("frauds"))

    df_frauds_trans = pd.merge(df_trans, df_frauds, how = 'outer', on = 0)
    df_frauds_trans.fillna(False, inplace=True)

    df_frauds_trans.columns = 'ID Card_number Date Value Segment Fraud_flag'.split()
    return df_frauds_trans

def get_only_frauds(df_frauds_trans):
    return df_frauds_trans[df_frauds_trans['Fraud_flag']==True]

def get_only_not_frauds(df_frauds_trans):
    return df_frauds_trans[df_frauds_trans['Fraud_flag']==False]

def analyse_value(df_frauds_trans):
    analyse_mean(df_frauds_trans)
    analyse_std(df_frauds_trans)
    analyse_max_min(df_frauds_trans)
    analyse_median(df_frauds_trans)

def analyse_mean(df_frauds_trans):
    mean_trans = get_only_not_frauds(df_frauds_trans)['Value'].mean()
    mean_frauds = get_only_frauds(df_frauds_trans)['Value'].mean()
    fraud_value = (1 - (mean_trans/mean_frauds))*100
    
    print("\nValor médio das transações normais: {:.2f}".format(mean_trans))
    print("Valor médio das fraudes: {:.2f}".format(mean_frauds))
    print("As fraudes possuem valor {:.2f}% mais alto do que as transações normais".format(fraud_value))

def analyse_std(df_frauds_trans):
    std_trans = get_only_not_frauds(df_frauds_trans)['Value'].std()
    std_frauds = get_only_frauds(df_frauds_trans)['Value'].std()

    print("\nO desvio padrão das transações é {:.2f}".format(std_trans))
    print("O desvio padrão das fraudes é {:.2f}".format(std_frauds))

def analyse_median(df_frauds_trans):
    median_trans = get_only_not_frauds(df_frauds_trans)['Value'].median()
    median_frauds = get_only_frauds(df_frauds_trans)['Value'].median()
    fraud_value = (1 - (median_trans/median_frauds))*100

    print("\nA mediana das transações não fraudulentas é: {:.2f}".format(median_trans))
    print("A mediana das fraudes é {:.2f}".format(median_frauds))
    print("A mediana das fraudes é {:.2f}% mais alto que as transações normais".format(fraud_value))

def analyse_max_min(df_frauds_trans):
    min_trans = get_only_not_frauds(df_frauds_trans)['Value'].min()
    min_frauds = get_only_frauds(df_frauds_trans)['Value'].min()
    max_trans = get_only_not_frauds(df_frauds_trans)['Value'].max()
    max_frauds = get_only_frauds(df_frauds_trans)['Value'].max()
    print("\nValor minimo das transações não fraudulentas: R${}".format(min_trans))
    print("Valor minimo das fraudes: R${}".format(min_frauds))
    print("Valor maximo das transações não fraudulentas: R${}".format(max_trans))
    print("Valor maximo das fraudes: R${}".format(max_frauds))


def get_fraud_rate_segments(df_frauds_trans):
    group_frauds_seg = get_only_frauds(df_frauds_trans).groupby('Segment')
    df_frauds_seg = pd.DataFrame(group_frauds_seg.describe()['Value']['count'])
    df_frauds_seg.columns = ['Frauds']
    
    group_trans = df_frauds_trans.groupby('Segment')
    df_trans_seg = pd.DataFrame(group_trans.describe()['Value']['count'])
    df_trans_seg.columns = ['Transactions']

    df_fraud_rate = df_trans_seg.join(df_frauds_seg)
    df_fraud_rate['Fraud Rate (%)'] = round(100*df_fraud_rate['Frauds']/df_fraud_rate['Transactions'], 2)
    return df_fraud_rate

def get_fraud_rate_month(df_frauds_trans):
    df_frauds_trans["Month"] = df_frauds_trans['Date'].apply(lambda x : x.month)
    df_frauds_month = pd.DataFrame(get_only_frauds(df_frauds_trans).groupby("Month").describe()["Value"]["count"])
    df_trans_month = pd.DataFrame(df_frauds_trans.groupby('Month').describe()['Value']['count'])
    df_trans_month.columns = ['Transactions']
    df_frauds_month.columns = ['Frauds']
    df_trans_frauds_month = df_trans_month.join(df_frauds_month)

    df_trans_frauds_month['Fraud Rate (%)'] = round(100*df_trans_frauds_month['Frauds']/df_trans_frauds_month['Transactions'], 2)
    return df_trans_frauds_month
