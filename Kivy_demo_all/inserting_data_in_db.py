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
    cursror = db.cursor()
    sql = " CREATE TABLE IF NOT EXISTS demo (RFID VARCHAR(64) PRIMARY KEY NOT NULL, " \
          "AssetSN VARCHAR(64) NULL ," \
          "DataCenter VARCHAR(64) NULL," \
          "Description VARCHAR(64) NULL," \
          "DeviceModel VARCHAR(64) NULL, " \
          "Floor VARCHAR(64) NULL, " \
          "Manufacturer VARCHAR(64) NULL, " \
          "AssetUnitUsage VARCHAR(64) NULL," \
          "Room VARCHAR(64) NULL," \
          "SerialNumber VARCHAR(64) NULL," \
          "RackNo VARCHAR(100) NULL, " \
          "Cols VARCHAR(64) NULL, " \
          "Supplier VARCHAR(64) NULL, " \
          "Address VARCHAR(64) NULL," \
          "MacAddress1 VARCHAR(64) NULL," \
          "MacAddress2 VARCHAR(64) NULL, " \
          "EquipmentCategory VARCHAR(64) NULL," \
          "Weight VARCHAR(64) NULL, " \
          "InventoryCode VARCHAR(64) NULL, " \
          "LifeCycle VARCHAR(64) NULL," \
          "Power VARCHAR(64) NULL, " \
          "LastMaintenanceStaff VARCHAR(64) NULL, " \
          "MaintenanceCycle VARCHAR(64) NULL," \
          "Current VARCHAR(64) NULL, " \
          "NextMaintenanceStaff VARCHAR(64) NULL," \
          "Principal VARCHAR(64) NULL, " \
          "Voltage VARCHAR(64) NULL," \
          "LastUpdatedTime VARCHAR(64) NULL, " \
          "MaintenanceContact VARCHAR(64) NULL," \
          "FirstUseTime VARCHAR(64) NULL," \
          "NextUpdateTime VARCHAR(64) NULL);"

    cursror.execute(sql)
    insert = "insert into demo values(0,'uks','WERedGE2450', 1,2,'NETWORKINRACK', 'HDFC', '2nd floor', 'Network', '2nd', '15-02-a0-c2', 'ITRoom','Dell','SN123456','TECHLAB', '15-c2-15-00', " \
             "'Server', '3 years', 'None', '3000 usd', 'TECHLAB',  28,300,1,230,'2021-01-01', 'INV012', 'sagar', 'datta', '2021-01-01', '2021-02-01')"

    #cursror.execute(insert)
    db.commit()
