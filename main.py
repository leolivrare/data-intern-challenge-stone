from connection import *


def main():
    db = Connection("db-stone.cjepwwjnksng.us-east-1.rds.amazonaws.com",
                    "postgres",
                    "read_only_user",
                    "banking123",
                    5432)


if __name__ == "__main__":
    main()
