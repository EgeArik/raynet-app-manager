import os

from src.db_manager import DataBaseManager
from src.app_manager import ApplicationManager
from src.vendor_manager import VendorManager


def show_menu():

    print("\n--- RAYNET APP MANAGER ---\n")

    print("1 - Uygulamaları Listele")
    print("2 - Yeni Uygulama Ekle")
    print("3 - Uygulama Sil")
    print("4 - Uygulama  Güncelle")
    print("5 - Üreticileri Listele")
    print("6 - Yeni Üretici Ekle")
    print("7 - Üretici Sil")
    print("8 - Üretici Güncelle")
    print("0 - Çıkış")

    return input("\nSeçim yapınız: ")


# VERİ TABANI BAĞLANTISI
db = DataBaseManager("database/raynet-manager.db")

# MANAGER NESNELERİ
app_manager = ApplicationManager(db)
vendor_manager = VendorManager(db)

# TABLOLARI OLUŞTUR
app_manager.create_table()
vendor_manager.create_table()


while True:

    os.system("cls")

    choice = show_menu()

    # 1 - UYGULAMALAR LİSTELE
    if choice == "1":
        os.system("cls")

        app_manager.get_all_apps()

        input("\nAna menüye dönmek için Enter bas...")

    # 2 - UYGULAMA EKLE
    elif choice == "2":
        os.system("cls")

        app_name = input("Uygulama adı: ")
        category = input("Kategori: ")
        vendor_id = input("Vendor ID: ")

        app_manager.add_app(app_name, category, vendor_id)

        input("\nBaşarıyla eklendi. Ana menüye dönmek için Enter bas...")

    # 3 - UYGULAMA SİL
    elif choice == "3":
        os.system("cls")

        app_id = input("Silinecek uygulama ID: ")

        app_manager.delete_app(app_id)

        input("\nBaşarıyla silindi. Ana menüye dönmek için Enter bas...")


    # 8 - UYGLAMA GÜNCELLE
    elif choice == "4":
        os.system("cls")

        app_id = input("Güncellenecek Uygulama ID: ")
        new_app_name = input("Yeni uygulama ismi: ")
        new_vendor_id = input("Yeni üretici ID: ") # Tabi ki burda aynı vendor idye güncellemeye çalışınca hata alacağız. ID'yi kullanıcıdan istemek mantıklı değil...

        app_manager.update_apps(app_id, new_app_name, new_vendor_id)

        input("\nBaşarıyla güncellendi. Ana menüye dönmek için Enter bas...")

    # 4 - ÜRETİCİ LİSTELE
    elif choice == "5":
        os.system("cls")

        vendor_manager.get_all_vendors()

        input("\nAna menüye dönmek için Enter bas...")


    # 5 - ÜRETİCİ EKLE
    elif choice == "6":
        os.system("cls")

        vendor_name = input("Üretici adı: ")
        country = input("Ülke: ")

        vendor_manager.add_vendors(vendor_name, country)

        input("\nBaşarıyla eklendi. Ana menüye dönmek için Enter bas...")

    # 6 - ÜRETİCİ SİL
    elif choice == "7":
        os.system("cls")

        vendor_id = input("Silinecek üretici ID: ")

        vendor_manager.delete_vendors(vendor_id)

        input("\nBaşarıyla silindi. Ana menüye dönmek için Enter bas...")

    # 7 - ÜRETİCİ GÜNCELLE
    elif choice == "8":
        os.system("cls")

        vendor_id = input("Güncellenecek üretici ID: ")
        new_vendor_name = input("Yeni üretici ismi: ")
        new_vendor_country = input("Yeni ülke: ")

        vendor_manager.update_vendors(
            vendor_id,
            new_vendor_name,
            new_vendor_country
        )

        input("\nBaşarıyla güncellendi. Ana menüye dönmek için Enter bas...")

    # 0 - ÇIKIŞ
    elif choice == "0":
        print("\nSistem kapatılıyor...")
        break

    else:
        input("\nHatalı seçim. Ana menüye dönmek için Enter bas...")