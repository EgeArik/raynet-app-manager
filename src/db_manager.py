import sqlite3 

class DataBaseManager : 

    def __init__(self,db_name) : 
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        print(f"[Sistem] veri tabanına bağlanıldı {db_name}")

    def __del__(self): 
        self.connection.close()

        print(f"[Sistem]  Veri tabanı bağlantısı kapatıldı")    



