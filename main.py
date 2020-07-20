from connection import *
from first_part import *
from second_part import *

def main():
    db = Connection("db-stone.cjepwwjnksng.us-east-1.rds.amazonaws.com",
                    "postgres",
                    "read_only_user",
                    "banking123",
                    5432)
    #Primeira parte
    #Resolucao do primeiro exercicio
    print("A média de idade dos clientes é de: {} anos \n".format(int(get_customers_average_age(db))))

    #Resolucao do segundo exercicio
    df_family_limit = get_card_family_limit_analisys(db)
    print(df_family_limit)
    df_family_limit.to_csv(r'card_family_limit_analisys.csv')

    #Resolucao do terceiro exercicio
    print("\n")
    print("O ID da fraude de maior valor é:\n{}".format(get_highest_value_fraud_id(db)))
    print("\nAs 5 fraudes de maior valor são:\n{}".format(get_most_expensive_frauds(db)))
    #Segunda parte
    analyse_fraudulent_transactions(db)
    db.close()
if __name__ == "__main__":
    main()
