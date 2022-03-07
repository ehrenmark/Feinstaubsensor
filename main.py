import manage_sqlite
import csv_reader

if __name__ == "__main__":
    while True:
        print("1. Herunterladen von aktuellen Daten und importieren dieser in der Datenbank")
        print("2. Höchst-, Tiefst- und Durchschnittswerte anzeigen lassen.")

        print("9. Beenden")
        task = input("Wählen sie eine Aufgabe aus, geben sie dazu die Nummer an: ")

        if (task == "1"):
            sql = manage_sqlite.Feinstaub_Datenbank()
            csv = csv_reader.CSV_import(["csv_dht22", "csv_sds011"])
            csv_data = csv.read_files()
            sql.insert_multiple_sds011_entries(csv_data["csv_sds011"])
            sql.insert_multiple_dht22_entries(csv_data["csv_dht22"])
            sql.close()
            continue

        if (task == "2"):
            sql = manage_sqlite.Feinstaub_Datenbank()
            data = sql.get_daily_data()
            sql.close()
            continue

        if (task == "9"):
            break

    # Testdaten zum einfügen in die Datenbank
    # sql.insert_single_sds011_entry(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, "2022-02-18 13:16:34")
    # sql.inser_single_dht22_entry(2, 2, 2, 2, 2, 2, "2022-02-18 13:16:34")