import sqlite3, os
# from EntityRecognition import EntityRecognition
from itertools import chain
import os
import yaml

class YMLRead():
    def __init__(self, table_name, database_path, database_name):
        super().__init__()
        self.table_name = table_name
        self.database_path = database_path
        self.database_name = database_name

    def read_rules(self, item):
        if(item):
            con = sqlite3.connect(f"{os.path.basename(self.database_path)}{'.db'}")
            cur = con.cursor()
            # print("table name ", self.table_name)
            # print("database name ", self.database_name)
            # print("database path", self.database_path)
            query_keyword = ''
            # path = r'/home/daus/Documents/TA/dronetimeline/rules/' + item + '.yml'
            path = r'/Users/illank86/Documents/Project/droneProject/rules/' + item + ".yml"
            with open(path, "r") as stream:
                try:
                    data = yaml.safe_load(stream)
                    data = data["detection"]["keywords"]
                    for keyword in data:
                        query_keyword += f"OR message='{keyword}'"
                    print("ini query keyword ", query_keyword)
                except yaml.YAMLError as exc:
                    print(exc)
            

        else:
            print("Nothing")