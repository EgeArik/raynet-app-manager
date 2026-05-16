class ApplicationManager:

    def __init__(self, db_manager):

        self.db = db_manager

    # TABLO OLUŞTUR
    def create_table(self):
        "query = SORGU "

        query = """ 
        CREATE TABLE IF NOT EXISTS "Applications" (
	        "app_id"	INTEGER,

	        "app_name"	TEXT,

	        "category"	TEXT,

	        "vendor_id"	INTEGER,

	        PRIMARY KEY("app_id"),

	        FOREIGN KEY("vendor_id") REFERENCES "Vendors"("vendor_id")
        );
        """

        self.db.cursor.execute(query) 
        """SQL komutunu SQLite’a gönderiyor."""
        

        self.db.connection.commit()
        """SQL komutunu kaydediyor"""

    # CREATE
    def add_app(self, app_name, category, vendor_id):

        query = """
        INSERT INTO Applications(app_name, category, vendor_id)
        VALUES (?, ?, ?)
        """

        self.db.cursor.execute(
            query,
            (app_name, category, vendor_id)
        )

        self.db.connection.commit()

        print(f"{app_name} başarıyla eklendi.")

    # READ
    def get_all_apps(self):

        query = "SELECT * FROM Applications"

        self.db.cursor.execute(query)

        apps = self.db.cursor.fetchall()

        print("\n--- UYGULAMALAR ---")

        for app in apps:

            print(app)

    # DELETE
    def delete_app(self, app_id):

        query = "DELETE FROM Applications WHERE app_id = ?"

        self.db.cursor.execute(query, (app_id,))

        self.db.connection.commit()

        print(f"{app_id} ID'li uygulama silindi.")

    #UPDATE
    def update_apps(self,app_id,new_app_name,new_vendor_id):
        query = """
        UPDATE Applications
        SET app_name = ? , vendor_id = ?
        WHERE app_id = ?
        """
        self.db.cursor.execute(query,(new_app_name,new_vendor_id,app_id,)) 
        self.db.connection.commit()
