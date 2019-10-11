from cli_input_output import input_loop
from database_operations import json_to_database, clear_database

if __name__ == "__main__":
    json_to_database()
    input_loop()

    # clearing the db when leaving the app
    clear_database()
