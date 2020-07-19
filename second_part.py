import pandas as pd
from connection import *

def analyse_fraudulent_transactions(db):
    df_merge = get_frauds_transactions(db)
    analyse_value(df_merge)
    df_fraud_rate_seg = get_fraud_rate_segments(df_merge)
    df_fraud_rate_month = get_fraud_rate_month(df_merge)
    
    df_fraud_rate_seg.to_csv(r'fraud_rate_seg.csv')
    df_fraud_rate_month.to_csv(r'fraud_rate_month.csv')
    print("\n{}".format(df_fraud_rate_seg))
    print("\n{}".format(df_fraud_rate_month))

def get_frauds_transactions(db):
    df_trans = pd.DataFrame(db.select_table("transactions"))
    df_frauds = pd.DataFrame(db.select_table("frauds"))

    df_merge = pd.merge(df_trans, df_frauds, how = 'outer', on = 0)
    df_merge.fillna(False, inplace=True)

    df_merge.columns = 'ID Card_number Date Value Segment Fraud_flag'.split()
    return df_merge

def analyse_value(df_merge):
    analyse_mean(df_merge)
    analyse_std(df_merge)
    analyse_max_min(df_merge)
    analyse_median(df_merge)

def analyse_mean(df_merge):
    mean_trans = df_merge[df_merge['Fraud_flag']==False]['Value'].mean()
    mean_frauds = df_merge[df_merge['Fraud_flag']==True]['Value'].mean()
    fraud_value = (1 - (mean_trans/mean_frauds))*100
    
    print("\nValor médio das transações normais: {}".format(mean_trans))
    print("Valor médio das fraudes: {}".format(mean_frauds))
    print("As fraudes possuem valor {:.2f}% mais alto do que as transações normais".format(fraud_value))

def analyse_std(df_merge):
    std_trans = df_merge[df_merge['Fraud_flag']==False]['Value'].std()
    std_frauds = df_merge[df_merge['Fraud_flag']==True]['Value'].std()

    print("\nO desvio padrão das transações é {}".format(std_trans))
    print("O desvio padrão das fraudes é {}".format(std_frauds))

def analyse_median(df_merge):
    median_trans = df_merge[df_merge['Fraud_flag']==False]['Value'].median()
    median_frauds = df_merge[df_merge['Fraud_flag']==True]['Value'].median()
    fraud_value = (1 - (median_trans/median_frauds))*100

    print("\nA mediana das transações não fraudulentas é: {}".format(median_trans))
    print("A mediana das fraudes é {}".format(median_frauds))
    print("A mediana das fraudes é {:.2f}% mais alto que as transações normais".format(fraud_value))

def analyse_max_min(df_merge):
    min_trans = df_merge[df_merge['Fraud_flag']==False]['Value'].min()
    min_frauds = df_merge[df_merge['Fraud_flag']==True]['Value'].min()
    max_trans = df_merge[df_merge['Fraud_flag']==False]['Value'].max()
    max_frauds = df_merge[df_merge['Fraud_flag']==True]['Value'].max()
    print("\nValor minimo das transações não fraudulentas: R${}".format(min_trans))
    print("Valor minimo das fraudes: R${}".format(min_frauds))
    print("Valor maximo das transações não fraudulentas: R${}".format(max_trans))
    print("Valor maximo das fraudes: R${}".format(max_frauds))


def get_fraud_rate_segments(df_merge):
    group_frauds_seg = df_merge[df_merge['Fraud_flag']==True].groupby('Segment')
    df_frauds_seg = pd.DataFrame(group_frauds_seg.describe()['Value']['count'])
    df_frauds_seg.columns = ['Frauds']
    
    group_trans = df_merge.groupby('Segment')
    df_trans_seg = pd.DataFrame(group_trans.describe()['Value']['count'])
    df_trans_seg.columns = ['Transactions']

    df_fraud_rate = df_trans_seg.join(df_frauds_seg)
    df_fraud_rate['Fraud Rate (%)'] = 100*df_fraud_rate['Frauds']/df_fraud_rate['Transactions']
    return df_fraud_rate

def get_fraud_rate_month(df_merge):
    df_merge["Month"] = df_merge['Date'].apply(lambda x : x.month)
    df_frauds_month = pd.DataFrame(df_merge[df_merge['Fraud_flag']==True].groupby("Month").describe()["Value"]["count"])
    df_trans_month = pd.DataFrame(df_merge.groupby('Month').describe()['Value']['count'])
    df_trans_month.columns = ['Transactions']
    df_frauds_month.columns = ['Frauds']
    df_trans_frauds_month = df_trans_month.join(df_frauds_month)

    df_trans_frauds_month['Fraud Rate (%)'] = 100*df_trans_frauds_month['Frauds']/df_trans_frauds_month['Transactions']
    return df_trans_frauds_month
