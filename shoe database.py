import mysql.connector
import datetime

db = input('Enter the name of your database: ')
mydb = mysql.connector.connect(host='localhost', user='root', passwd="My_sql@123")
mycursor = mydb.cursor()

sql = 'CREATE DATABASE IF NOT EXISTS %s' % (db,)
mycursor.execute(sql)
print('Database created successfully')

mycursor = mydb.cursor()
mycursor.execute('USE ' + db)

Tname = input('Name of the table to be created for shoes: ')
query = 'CREATE TABLE IF NOT EXISTS ' + Tname + '(Shoebrand VARCHAR(30), Size INT, Colour VARCHAR(15), Price INT)'
mycursor.execute(query)
print('Table ' + Tname + ' created successfully')

tablename = input('Name of the table to be created for customers: ')
query1 = 'CREATE TABLE IF NOT EXISTS ' + tablename + ' (Cname VARCHAR(30), Cid VARCHAR(5), Phonenumber VARCHAR(10), Age INT)'
mycursor.execute(query1)
print('Table ' + tablename + ' created successfully')

print('*' * 75)
print('\t\t\t\t\t\t WELCOME TO SHOE STORE')
print('\t\t\t\t\t\t', datetime.datetime.now())
print('*' * 75)
print('\n')
print('=' * 75)
print('1. Login')
print('2. Exit')
print('=' * 75)
print('\n')

pchoice = int(input('Enter your choice: '))
if pchoice == 1:
    password = input('Enter your Password: ')

    if password == 'abc@123':
        while password == 'abc@123':
            print('\n' + '=' * 75)
            print('\t\t\t\t\t WELCOME')
            print('=' * 75)
            print('1. Add Customer details')
            print('2. Add Shoe details')
            print('3. Display one Customer details')
            print('4. Display all Customer details')
            print('5. Display all Shoe details')
            print('6. Display a record from shoe details')
            print('7. Modify a record from customers details')
            print('8. Delete particular record from Customer details')
            print('9. Delete all records from Shoe details')
            print('10. Logout')
            choice = int(input('Enter Your Choice: '))

            if choice == 1:
                print('\n')
                print('*' * 75)
                Cname = input('Enter Customer name: ')
                Cid = input('Enter customer id: ')
                Phonenumber = int(input('Enter the contact number: '))
                Age = int(input('Enter customer\'s age: '))
                sql_insert = "INSERT INTO " + tablename + " VALUES ('" + Cname + "', '" + Cid + "', '" + str(Phonenumber) + "', " + str(Age) + ")"
                mycursor.execute(sql_insert)
                mydb.commit()
                print('\nRecord added')
                print('*' * 75)

            elif choice == 2:
                print('\n')
                print('*' * 75)
                Shoebrand = input('Enter Shoe brand: ')
                Size = int(input('Enter the shoe size: '))
                Colour = input('Enter the colour of shoe: ')
                Prize = int(input('Enter the shoe price: '))
                sql_insert = "INSERT INTO " + Tname + " VALUES ('" + Shoebrand + "', " + str(Size) + ", '" + Colour + "', " + str(Prize) + ")"
                mycursor.execute(sql_insert)
                mydb.commit()
                print('\nRecord added')
                print('*' * 75)

            elif choice == 3:
                print('\n')
                print('*' * 75)
                try:
                    ci = input('Enter the customer id of the customer to be displayed: ')
                    q = "SELECT * FROM " + tablename + " WHERE Cid = '" + ci + "'"
                    mycursor.execute(q)
                    myrecord = mycursor.fetchone()
                    print("\n\nRecord of customer with Cid: " + ci)
                    print(myrecord)
                    c = mycursor.rowcount
                    if c == -1:
                        print('No such record to display')
                        print('*' * 75)
                except Exception as e:
                    print('Sorry!\nSomething went wrong')
                    print(e)
                    print('*' * 75)

            elif choice == 4:
                try:
                    query = "SELECT * FROM " + tablename
                    mycursor.execute(query)
                    rec = mycursor.fetchall()
                    print('=' * 75)
                    for r in rec:
                        print(r)
                    print('=' * 75)
                except Exception as e:
                    print('Sorry!\nSomething went wrong')
                    print(e)
                    print('*' * 75)

            elif choice == 5:
                try:
                    query = "SELECT * FROM " + Tname
                    mycursor.execute(query)
                    rec = mycursor.fetchall()
                    print('=' * 75)
                    for r in rec:
                        print(r)
                    print('=' * 75)
                except:
                    print('Sorry!\nSomething went wrong')
                    print('*' * 75)

            elif choice == 6:
                print('\n')
                print('*' * 75)
                try:
                    sb = input('Enter the brand of the shoe to be displayed: ')
                    q = "SELECT * FROM " + Tname + " WHERE Shoebrand = '" + sb + "'"
                    mycursor.execute(q)
                    myrecord = mycursor.fetchone()
                    print('\n\nRecord of shoe with brand: ' + sb + ' is: ')
                    print(myrecord)
                    c = mycursor.rowcount
                    if c == -1:
                        print('No such record to display')
                        print('*' * 75)
                except Exception as e:
                    print('Sorry!\nSomething went wrong')
                    print(e)
                    print('*' * 75)

            elif choice == 7:
                try:
                    m = input('Enter the id of customer to be modified: ')
                    want = "SELECT * FROM " + tablename + " WHERE Cid = '" + m + "'"
                    mycursor.execute(want)
                    record = mycursor.fetchone()
                    c = mycursor.rowcount
                    if c == -1:
                        print("Customer with customer id " + m + " does not exist")
                    else:
                        cn = record[0]
                        ci = record[1]
                        pn = record[2]
                        ag = record[3]
                        print('Name: ', cn, '\n', 'Phone: ', pn, '\n', 'Age: ', ag)
                        print('Type value to be modified below')
                        print('Just press Enter for no Change')
                        name = input('Enter Name: ')
                        if len(name) > 0:
                            cn = name
                        n = input('Enter phone number: ')
                        if len(n) > 0:
                            pn = n
                        a = input('Enter Age of customer: ')
                        if len(a) > 0:
                            ag = int(a)
                        query = "UPDATE " + tablename + " SET Cname='" + cn + "', Phonenumber='" + pn + "', Age=" + str(ag) + " WHERE Cid='" + m + "'"
                        mycursor.execute(query)
                        mydb.commit()
                        print('Record modified')
                except Exception as e:
                    print('Sorry \nSomething went wrong')
                    print(e)

            elif choice == 8:
                try:
                    c = input('Enter Customer id of the customer to be deleted: ')
                    q = "DELETE FROM " + tablename + " WHERE Cid = '" + c + "'"
                    mycursor.execute(q)
                    mydb.commit()
                    cnt = mycursor.rowcount
                    if cnt > 0:
                        print('Deletion done')
                    else:
                        print('Nothing is deleted')
                except Exception as e:
                    print('Sorry!\nSomething went wrong')
                    print(e)

            elif choice == 9:
                print('\n' + '*' * 75)
                try:
                    ch = input('Do you want to delete all the records (y/n): ')
                    if ch.upper() == 'Y':
                        mycursor.execute('DELETE FROM ' + Tname)
                        mydb.commit()
                        print('All the records are deleted')
                        print('*' * 75)
                    else:
                        print("Please enter a valid choice")
                except Exception as e:
                    print('Sorry!\nSomething went wrong')
                    print(e)
                    print('*' * 75)

            elif choice == 10:
                print('Thank you for visit \nVisit again')
                break
            else:
                print('Please enter a valid choice')
    else:
        print('Sorry! \n Wrong password \n Try again')
elif pchoice == 2:
    print('Bye')
