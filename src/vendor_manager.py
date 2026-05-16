class VendorManager : 

    def __init__(self,db_manager):
        self.db =  db_manager

    def create_table(self):
        query = """

        CREATE TABLE IF NOT EXISTS "Vendors" (

	    "vendor_id"	INTEGER,

	    "vendor_name"	TEXT,

	    "country"	TEXT,

	    PRIMARY KEY("vendor_id")

        );
        """

        self.db.cursor.execute(query)
        
        self.db.connection.commit()


    def add_vendors(self,vendor_name,country):

        query = """

        INSERT INTO Vendors(vendor_name,country)
        Values(?, ?) 
        """
        #Buraki Values kısmı yalnızca Insert komutlarında(bir şeyler eklerken)
        self.db.cursor.execute(query,(vendor_name,country))

        self.db.connection.commit()

    def get_all_vendors(self) :

        query = """

        SELECT * FROM Vendors
        """

        self.db.cursor.execute(query)
        vendor = self.db.cursor.fetchall()

        print("\n--- UYGULAMALAR ---")
        for x in vendor:
            print(x)


    def delete_vendors(self,vendor_id):

        query = "DELETE FROM Vendors WHERE vendor_id = ?"

        self.db.cursor.execute(query,(vendor_id,)) # sona virgül koy ki tek elemanlı tupple olduğu anlaşılsın

        self.db.connection.commit()

        print(f"{vendor_id} ID'li Üretici başarıyla silindi")

    def update_vendors(self,vendor_id,new_vendor_name,new_vendor_country):

        query = """
        UPDATE Vendors
        SET vendor_name = ? , country = ?
        WHERE vendor_id = ?

        """
        self.db.cursor.execute(query,(new_vendor_name,new_vendor_country,vendor_id,)) # Burada ? işaretlerinde ki değerlerin gelme sırasına dikkat et 
        #Yukarıda name , country, id olarak gittiği için execute komutuna da o sırayla yazmalısın.
        self.db.connection.commit()

