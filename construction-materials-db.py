import sqlite3


def connect_to_database(database_name):
    con = sqlite3.connect(database_name)
    cursor = con.cursor()
    return con, cursor


def create_table(cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS waybill (waybillNo TEXT, quantity FLOAT, unit TEXT, class TEXT, date TEXT, description TEXT)")


def insert_data(cursor, waybill_no, quantity, unit, classification, date, description):
    cursor.execute("INSERT INTO waybill VALUES (?, ?, ?, ?, ?, ?)",
                   (waybill_no, quantity, unit, classification, date, description))


def get_user_input():
    waybill_no = input("Enter Waybill Number: ")
    quantity = float(input("Enter Quantity: "))
    unit = input("Enter Unit: ")
    classification = input("Enter Classification: ")
    date = input("Enter Date (DD.MM.YYYY): ")
    description = input("Enter Description: ")
    return waybill_no, quantity, unit, classification, date, description


def main():
    database_name = "waybillTable.db"

    try:
        con, cursor = connect_to_database(database_name)

        create_table(cursor)

        waybill_info = get_user_input()
        insert_data(cursor, *waybill_info)

        con.commit()
        con.close()
        print("Waybill information successfully added to the database.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
