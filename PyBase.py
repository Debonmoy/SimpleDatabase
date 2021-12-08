# Simple Database made in Python
# PyBase Version 1.0.1

# Note: There is a bug in delete entry feature, will be fixing it asap.


# Importing the modules
import json
from typing import Any, Union
import os
import sys

# Creating our base class
class PyBase:
    def __init__(self, filename: str) -> None:
        self.__filename = filename
        self.__db = {}
        self.__load_db()

# Loading databse function
    def __load_db(self):
        if os.path.isfile(self.__filename):
            self.__db = json.load(open(self.__filename))

    def __save(self):
        json.dump(self.__db, open(self.__filename, 'w'))
    
# Creating table in database function
    def create_table(self, table_name:Union[str, int, float]) -> None:
        self.__db[table_name] = {}
        self.__save()

# Deleting table in database function
    def delete_table(self, table_name:Union[str, int, float]) -> bool:
        if table_name in self.__db.keys():
            del self.__db[table_name]
            self.__save()
            return True
        return False

# Inserting a data into a table in database function
    def insert(self, table_name: Union[str, int, float], key: Union[str, int, float], value:Any) -> None:
        if not table_name in self.__db.keys():
            self.__db[table_name] = {}
        self.__db[table_name][key] = value
        self.__save()

# Getiing the database function
    def get(self, table_name: Union[str, int, float], key: Union[str, int, float], value:Any) -> Any:
        if table_name in self.__db.keys():
            return self.__db[table_name].get(key)
        return None

    def delete(self, table_name: Union[str, int, float], key: Union[str, int, float], value:Any) -> bool:
        if table_name in self.__db.keys():
            table = self.__db[table_name]
            if key in table.keys():
                del table[key]
                self.__save
                return True
        return False

# Main Function
def main():
    db = PyBase('database.json')
    print('========================================')
    print('             Welcome to Pybase          ')
    print('         Database created in Python     ')
    print('========================================\n')
    print('What do you want to do?')
    print('1. Create Table')
    print('2. Delete Table')
    print('3. Insert Entry')
    print('4. Delete Entry')
    print('5. Show Data ')

    ch = int(input('[*] Your Option: '))

# Create Table Option
    if ch == 1:
        name = str(input('[*] Enter table name: '))
        db.create_table(name)
        print('Do you want to add data?(y/n)')
        ch = input('[*] Your Option: ')
        if ch == 'y':
            print()
            n = int(input('[*] How many data do you want to add? (int only): '))
            for i in range (n):
                data = input('[*] Add your data: ')
                db.insert(name, i, data)
        print('Bye, Have a nice day...')
        sys.exit()

# Delete table option
    if ch == 2:
        option = str(input('[*] Name of the table to delete: '))
        db.delete_table(option)

# Insert entry in an existing table
    if ch == 3:
        name = str(input('[*] Enter the name of the table: '))
        # Print out the contents
        output = open('database.json', 'r')
        json_output = json.load(output)
        final_output = json.dumps(json_output, indent=4)
        output.close()
        print(final_output)
        # Add the new data
        no = int(input('[*] Enter Sl. No.: '))
        data = str(input('[*] Enter your data: '))
        db.insert(name, no, data)
        print('\nYour data was added!')

# Delete entry in an existing table
    if ch == 4:
        name = str(input('[*] Enter the name of the table: '))
        # Print out the contents
        output = open('database.json', 'r')
        json_output = json.load(output)
        final_output = json.dumps(json_output, indent=4)
        output.close()
        print(final_output)
        # Delete the data
        no = int(input('[*] Enter the index of the data to be deleted: '))
        data = str(input('[*] Enter the data to be deleted: '))
        db.delete(name, no, data)
# Show database option
    if ch == 5:
        output = open('database.json', 'r')
        json_output = json.load(output)
        final_output = json.dumps(json_output, indent=4)
        output.close()
        print(final_output)
    
main()