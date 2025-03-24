from django.core.management import BaseCommand
import pyodbc
from config.settings import USER, SERVER, PASSWORD, PAD_DATABASE, DRIVER, DATABASE


class Command(BaseCommand):
    def handle(self, *args, **options):
        conectString = f'''DRIVER={DRIVER};
                              SERVER={SERVER};
                              DATABASE={PAD_DATABASE};
                              UID={USER};
                              PWD={PASSWORD};'''
        try:
            conn = pyodbc.connect(conectString)
            conn.autocommit =True
            conn.execute(f"CREATE DATABASE MyDjangoBase")
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            print("База данных создана успешно")