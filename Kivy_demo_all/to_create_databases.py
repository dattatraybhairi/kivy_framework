import mysql.connector

if __name__ == '__main__':
    DB_USERNAME = "vacus"
    DB_PASSWORD = "vacus321"
    DB_NAME = "vacus"

    db = mysql.connector.connect(
        user=DB_USERNAME,
        password=DB_PASSWORD,
        database=DB_NAME,
        host="localhost",
        port=3306
    )

    print("db objects is created ", db)
    cursror = db.cursor()
    print("cursor object is created", cursror)

    sql = " CREATE TABLE IF NOT EXISTS demo (assettag VARCHAR(20) PRIMARY KEY," \
          "DeviceMOdel VARCHAR(64)," \
          "AssettUnitStage VARCHAR(64)" \
          ",RackNo VARCHAR(64)," \
          "Address VARCHAR(64), " \
          "DataCenter VARCHAR(64), " \
          "Floor VARCHAR(64), " \
          "Room VARCHAR(64)," \
          "MacAddr1 VARCHAR(64)," \
          " Description VARCHAR(100)," \
          " Manufacturer VARCHAR(64)," \
          " SerialNumber VARCHAR(64), " \
          "Supplier VARCHAR(64), " \
          "MacAddr2 VARCHAR(64)," \
          "EquipmentCategory VARCHAR(64)," \
          " Lifecycle VARCHAR(64)," \
          " MaintenanceCycle VARCHAR(64), " \
          "Principal VARCHAR(64)," \
          " MaintanceContact VARCHAR(64), " \
          "Weight INT," \
          " Power INT, Current INT," \
          "Voltage INT, " \
          "FirstUseTime DATE, " \
          "IneventoryCode VARCHAR(64), " \
          "LastMaintenanceStaff VARCHAR(64)," \
          "NextMaintenanceStaff VARCHAR(64), " \
          "LastUpdateTime VARCHAR(64)," \
          "NextUpdatedTime varchar(64));"

    cursror.execute(sql)
    db.commit()
