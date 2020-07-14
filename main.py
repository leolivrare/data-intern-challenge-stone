from connection import *
from first_part import *

def main():
    db = Connection("db-stone.cjepwwjnksng.us-east-1.rds.amazonaws.com",
                    "postgres",
                    "read_only_user",
                    "banking123",
                    5432)
    #Resolucao do primeiro exercicio
    print("The average age of the customers is: {} \n".format(customers_average_age(db)))

    #Resolucao do segundo exercicio
    card_family_limit_analisys(db);

    #Resolucao do terceiro exercicio
    print("The highest value fraud id is:\n{}".format(highest_value_fraud_id(db)))

if __name__ == "__main__":
    main()
