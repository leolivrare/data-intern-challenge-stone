from connection import *
from first_part import *

def main():
    db = Connection("db-stone.cjepwwjnksng.us-east-1.rds.amazonaws.com",
                    "postgres",
                    "read_only_user",
                    "banking123",
                    5432)
    print("The average age of the customers is: {} \n".format(customers_average_age(db)))


if __name__ == "__main__":
    main()
