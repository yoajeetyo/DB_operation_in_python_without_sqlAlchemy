from mysql.connector import connection
import logging

logging.basicConfig(filename="trackLogs.txt",
                    filemode="a",
                    format='%(asctime)s %(funcName)s %(levelname)s %(message)s',
                    datefmt='%y-%m-%d %H:%M:%S')


class DbOperations:
    def createTable(self):
        self.dbConnection = None
        try:
            self.dbConnection = connection.MySQLConnection(user='root', password='password',
                                                      host='localhost', port='3306',
                                                      database='rock')

            self.mycourser = self.dbConnection.cursor()
            self.query = """CREATE TABLE employee (  empID int,
                                                first_Name varchar(255),
                                                last_Name varchar(255),
                                                address varchar(255),
                                                city varchar(255),
                                                phone_no bigint,
                                                destination varchar(25),
                                                department varchar(30)
                                            );"""
            self.mycourser.execute(self.query)
            self.dbConnection.commit()

            logging.warning("log warning msg")

        except Exception as e:
            print(e)
            logging.error("log error msg")
        finally:
            if self.dbConnection!= None:
                self.dbConnection.close()
                logging.info("log information msg")

    def inserIntoTable(self):
        self.dbConnection = None
        try:
            self.dbConnection = connection.MySQLConnection(user='root', password='password',
                                                      host='localhost', port='3306',
                                                      database='rock')

            self.empID= int(input("Enter Employee id :"))
            self.first_Name = input("Enter first name :")
            self.last_Name = input("Enter last name :")
            self.address = input("Enter address :")
            self.city = input("Enter city name :")
            self.phone_no = int(input("Enter Phone no :"))
            self.destination = input("Enter Destination :")
            self.department = input("Enter Department :")

            self.mycourser = self.dbConnection.cursor()
            self.query = """INSERT INTO employee (empID,
                            first_Name,
                            last_Name,
                            address,
                            city,
                            phone_no,
                            destination,
                            department)""" + f"""VALUES
                            ({self.empID},
                            "{self.first_Name}",
                            "{self.last_Name}",
                            "{self.address}",
                            "{self.city}",
                             {self.phone_no},
                            "{self.destination}",
                            "{self.department}")"""
            self.mycourser.execute(self.query)
            self.dbConnection.commit()
            logging.warning("log warning msg")
        except Exception as e:
            print(e)
            logging.error("log error msg")
        finally:
            if self.dbConnection != None:
                self.dbConnection.close()
                logging.info("log information msg")
    def viewData(self):
        self.dbConnection = None
        try:
            self.dbConnection = connection.MySQLConnection(user='root', password='password',
                                                      host='localhost', port='3306',
                                                      database='rock')

            self.dataBaseName = input("Enter the Table name you want to see : ")

            self.mycoursor = self.dbConnection.cursor()
            self.query = f"""SELECT * FROM {self.dataBaseName}"""
            self.mycoursor.execute(self.query)
            self.data = self.mycoursor.fetchall()
            for datas in self.data:
                print(datas)
            logging.warning("log warning msg")
        except Exception as e:
            print(e)
            logging.error("log error msg")
        finally:
            if self.dbConnection!=None:
                self.dbConnection.close()
                logging.info("log information msg")
    def updateData(self):
        self.dbConnection = None
        try:
            self.dbConnection = connection.MySQLConnection(user='root', password='password',
                                                      host='localhost', port='3306',
                                                      database='rock')



            self.choose = input("""Which data you want to update ? Choose between 
                                employee first name,
                                employee Last name,
                                employee Address,
                                employee city,
                                employee phone no,
                                employee Destination,
                                employee department :""")

            if self.choose.__eq__("employee first name"):
                self.empF_name = input("Enter updated employee first name :")
                self.id = int(input("Enter the id of the employee :"))
                self.mycoursor = self.dbConnection.cursor()
                self.query = f"""UPDATE employee SET first_Name="{self.empF_name}" WHERE empId={self.id}"""
                self.mycoursor.execute(self.query)
                self.dbConnection.commit()

            elif self.choose.__eq__("employee Last name"):
                self.empl_name = input("Enter updated employee last name :")
                self.id = int(input("Enter the id of the employee :"))
                self.mycoursor = self.dbConnection.cursor()
                self.query = f"""UPDATE employee SET last_Name="{self.empl_name}" WHERE empId={self.id}"""
                self.mycoursor.execute(self.query)
                self.dbConnection.commit()

            elif self.choose.__eq__("employee Address"):
                self.address = input("Enter updated employee Address :")
                self.id = int(input("Enter the id of the employee :"))
                self.mycoursor = self.dbConnection.cursor()
                self.query = f"""UPDATE employee SET address="{self.address}" WHERE empId={self.id}"""
                self.mycoursor.execute(self.query)
                self.dbConnection.commit()

            elif self.choose.__eq__("employee city"):
                self.city = input("Enter updated employee city :")
                self.id = int(input("Enter the id of the employee :"))
                self.mycoursor = self.dbConnection.cursor()
                self.query = f"""UPDATE employee SET city="{self.city}" WHERE empId={self.id}"""
                self.mycoursor.execute(self.query)
                self.dbConnection.commit()

            elif self.choose.__eq__("employee phone no"):
                self.emp_phone = input("Enter updated employee Phone No :")
                self.id = int(input("Enter the id of the employee :"))
                self.mycoursor = self.dbConnection.cursor()
                self.query = f"""UPDATE employee SET phone_no ="{self.empl_name}" WHERE empId={self.id}"""
                self.mycoursor.execute(self.query)
                self.dbConnection.commit()

            elif self.choose.__eq__("employee Destination"):
                self.emp_dest = input("Enter updated employee Destination :")
                self.id = int(input("Enter the id of the employee :"))
                self.mycoursor = self.dbConnection.cursor()
                self.query = f"""UPDATE employee SET destination ="{self.emp_dest}" WHERE empId={self.id}"""
                self.mycoursor.execute(self.query)
                self.dbConnection.commit()

            elif self.choose.__eq__("employee department"):
                self.emp_dept = input("Enter updated employee department :")
                self.id = int(input("Enter the id of the employee :"))
                self.mycoursor = self.dbConnection.cursor()
                self.query = f"""UPDATE employee SET department ="{self.emp_dept}" WHERE empId={self.id}"""
                self.mycoursor.execute(self.query)
                self.dbConnection.commit()

            else:
                print("Choose anyone at a time from the above options")

            logging.warning("log warning msg")

        except Exception as e:
            print(e)
            logging.error("log error msg")
        finally:
            if self.dbConnection!= None:
                self.dbConnection.close()
                logging.info("log information msg")
    def deleteData(self):
        self.dbConnection = None
        try:
            self.dbConnection = connection.MySQLConnection(user='root', password='password',
                                                      host='localhost', port='3306',
                                                      database='rock')
            self.empID = int(input("Enter employee Id to delete :"))
            self.mycoursor = self.dbConnection.cursor()
            self.query = f"""DELETE FROM employee WHERE empID ={self.empID}"""
            self.mycoursor.execute(self.query)
            self.dbConnection.commit()
            logging.warning("log warning msg")
        except Exception as e:
            print(e)
            logging.error("log error msg")
        finally:
            if self.dbConnection!= None:
                self.dbConnection.close()
                logging.info("log info msg")

dboperations = DbOperations()
# dboperations.createTable()
# dboperations.inserIntoTable()
# dboperations.viewData()
# dboperations.updateData()
dboperations.deleteData()