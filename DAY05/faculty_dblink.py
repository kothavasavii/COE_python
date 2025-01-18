import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)
mycursor = mydb.cursor()

# Create the faculty  table with id, name,gender, age, experience, and salary
mycursor.execute("""
    CREATE TABLE faculty (
        id INT PRIMARY KEY,
        name VARCHAR(20),
        gender char,
        age INT,
        experience INT,
        salary DECIMAL(10, 2)
    )
""")

# inserting into table
id=input("Enter your id:")
name=input("Enter your name:")
gender=input("Enter your gender:")
age=input("Enter your age:")
experience=input("Enter your experience:")
salary=input("Enter your salary:")
mycursor.execute("insert into faculty values(%s,%s,%s,%s,%s,%s)",(id,name,gender,age,experience, salary))

# updating into faculty table
mycursor.execute("update faculty set salary=80000 where experience>15")
print("updated successfully")

# deleting from table
mycursor.execute("delete from faculty where experience<=5")

# accessing data from table
mycursor.execute("select * from faculty")
f = mycursor.fetchall();
for std in f:
    print(std)
mydb.commit()
