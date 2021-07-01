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
        port =3306
    )
    cursror = db.cursor()
    sql = " CREATE TABLE IF NOT EXISTS taginfo (id INT AUTO_INCREMENT PRIMARY KEY, RFIDPhysicalNo VARCHAR(64) UNIQUE, DeviceMOdel VARCHAR(64)" \
          ",AssettUnitStage INT , RackNo VARCHAR(64), Address VARCHAR(64), DataCenter VARCHAR(64), Floor VARCHAR(64), Room VARCHAR(64)," \
          "cols VARCHAR(64),MacAddr1 VARCHAR(64), Description VARCHAR(100), Manufacturer VARCHAR(64), SerialNumber VARCHAR(64), Supplier VARCHAR(64), MacAddr2 VARCHAR(64)," \
          "EquipmentCategory VARCHAR(64), Lifecycle VARCHAR(64), MaintenanceCycle VARCHAR(64), Principal VARCHAR(64), MaintanceContact VARCHAR(64), Weight INT, Power INT, Current INT," \
          "Voltage INT, FirstUseTime DATE, IneventoryCode VARCHAR(64), LastMaintenanceStaff VARCHAR(64),NextMaintenanceStaff VARCHAR(64), LastUpdateTime VARCHAR(64)," \
          "NextUpdatedTime VARCHAR(64));"
    cursror.execute(sql)
    insert = "insert into taginfo values(1,'ASTHDFC1','WERedGE2450', 2,'NETWORKINRACK','Chandrivalii', 'HDFC', '2nd floor', 'Network', '2nd', '15-02-a0-c2', 'ITRoom','Dell','SN123456','TECHLAB', '15-c2-15-00', " \
             "'Server', '3 years', 'None', '3000 usd', 'TECHLAB',  28,300,1,230,'2021-01-01', 'INV012', 'sagar', 'datta', '2021-01-01', '2021-02-01')"

    cursror.execute(insert)
    db.commit()