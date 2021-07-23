import sys

import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Data Sheet')

class Admin(object):              # creating a manager class to input his username and password to access the system 
    def __init__(self,username,password):      #constructor defining the username and passsword    
        self._username=username
        self._password=password

    #validations for username and password

    @property                    #getter property for username
    def username(self):
        return self._username

    @username.setter            #setter method for username
    def username(self,username):
        i=0
        flag=True
        while (i<5):
            if (username=="admin"):   #applying condition for checking out the correct username
                flag=True
                break

            else:
                flag=False
                i+=1
                username=str(input("Enter the correct username"))   #if not correct enter the username once again until correcct
        
        if(flag==False):
            print("The username is not valid. Please start the program again")
            sys.exit()

    @property
    def password(self):       #getter property for password
        return self._password

    @password.setter          #setter method for password
    def password(self,password):
        i=0
        flag=True
        while (i<5):
            if(password=="admin"):        #applying condition for checking out the correct password
                flag=True
                break
            else:
                flag=False
                i+=1
                password=input("Enter the  correct password")       #if not correct enter the password once again until correcct
        if(flag==False):
            print("The password is not valid. Please start the program again")
            sys.exit()

        
username=str(input("Enter the username"))    #inputing our username
password=str(input("Enter the password"))    #inputing our password
s=Admin(username,password)          #creating an object for manager class
s.username = username
s.password = password


print("********** Welcome to Supermarket Management System **********")

      
class Node(object):               #creating a Node class 
    def __init__(self,dataval=None):        #assigning our data with its next and prev addresses
        self.dataval=dataval
        self.next=None
        self.prev=None


class Cashier(object):               #creaing an admin class 
    def __init__(self):
        self.headval=None               #assigning a pointer headval
        

    def add_item(self):          #method to store the items to sell in the supermatket
        sheet1.write(0, 0, 'id')
        sheet1.write(0, 1, 'category')
        sheet1.write(0, 2, 'brand')
        sheet1.write(0, 3, 'quantity')
        sheet1.write(0, 4, 'stock')
        sheet1.write(0, 5, 'price')
        sheet1.write(0, 6, 'expiry')
        row=1
        
        while(True):
            #Enter the all the specific details of the particular product
            try:
                id=int(input("Enter the id:"))       #every product will have a different id   
            except:
                print("Please enter a valid id of the product. Enter it again.")
                id=int(input("Enter the id:"))
            
            if (id==0):
                break
            
            category=str(input("Enter the category of the product:"))    #signifies the type of product to be stored
            brand=str(input("Enter the brand of that category:"))          #signifies the brand of that type of product
            quantity=str(input("Enter the quantity of the product:"))    #signifies the quantity of that product

            try:
                stock=int(input("Enter the stock:"))          #signifies the stock for that particular item
            except:
                print("The stock should be in numeric. Please enter it again")
                stock=int(input("Enter the stock:"))

            try:
                price=int(input("Enter the price of the product:"))          #signifies the price of a particular quanity for a pariticular product
            except:
                print("The price should be in numeric. Please enter it again")
                price=int(input("Enter the price of the product:"))

            expiry=str(input("Enter the expirydate of the product:"))        #Enter the expiry data of every product in a y-m-d format

            sheet1.write(row, 0, id)
            sheet1.write(row, 1, category)
            sheet1.write(row, 2, brand)
            sheet1.write(row, 3, quantity)
            sheet1.write(row, 4, stock)
            sheet1.write(row, 5, price)
            sheet1.write(row, 6, expiry)

            wb.save('xlwt example.xls')

            row+=1


            item_node={"id":id,"category":category,"brand":brand,"stock":stock,"quantity":quantity,"price":price,"expiry":expiry}   #using item_nodetionary as a toll to store the data
            newNode=Node(item_node)     #passing the item_nodetionary to the Node class

            if self.headval is None:
                self.headval=newNode  

            else:
                last=self.headval       #code for assigning the next to the particular node i.e. storing the address of the nect item
                while last.next is not None:
                    last=last.next
                newNode.prev=last
                last.next=newNode
                newNode.next=None

    def display(self):     #method to display all the products feeded in our system
        printval=self.headval          #assigining printval as the headval
        while printval:
            print(printval.dataval)
            printval=printval.next         #incrementing the pointer to display the result



#From now onwards we now start to print out the bills for our customer.
#customer gives us the specific details about what product he wants.
#And finally after the details given by the customer, we finally give him the bill containg all the purchased itmes with th final bill

    def bill_generation(self, bill):   
            flag=True     
            b=self.headval
            category=str(input("Enter the category of the product you want:"))   #customer giving us the details of the product he has to buy
            if(category=="None"):     #after he completes his pruchasing the final bill will be printed
                return bill
            brand=str(input("Enter the brand of the product you want:"))

            quantity=str(input("Enter the quantity of the willing product:"))
            try:
                stock=int(input("Enter the stock:"))          #signifies the stock for that particular item
            except:
                print("The stock should be in numeric. Please enter it again")
                stock=int(input("Enter the stock:"))

            printval=self.headval
            while printval.next is not None:
                if(category==printval.dataval["category"] and brand==printval.dataval["brand"] and quantity==printval.dataval["quantity"]):       #checking out the condtion to see whether the input data by the customer is present in the system or not
                    # print("The amount of stock available for this product is - ", printval.dataval["stock"])
                    
                    if(stock<=printval.dataval["stock"]):
                        bill.append(printval.dataval["price"]*stock)    #append the price for the particular product considering the amount of itmes he purchased 
                        printval.dataval["stock"] = printval.dataval["stock"] - stock
                        user.append(printval.dataval)
                        category=str(input("Enter the category of the product you want:"))
                        if(category=="None"):
                            flag=False
                            break
                        brand=str(input("Enter the brand of the product you want:"))
                        quantity=str(input("Enter the quantity of the willing product:"))

                        try:
                            stock=int(input("Enter the stock you want for that product:"))          #signifies the stock for that particular item
                        except:
                            print("The stock should be in numeric. Please enter it again")
                            stock=int(input("Enter the stock you want for that product:"))

                        printval=printval.next
                    else:
                        print("The amount of stock you want is not available at the moment") 
                        printval=printval.next                           
                else:
                    printval=printval.next         #if not found increment the counter

            if flag==False:
                return bill

            laste=printval
            while laste is not None:
                if(category==laste.dataval["category"] and brand==laste.dataval["brand"] and quantity==laste.dataval["quantity"]):     #checking out the condtion to see whether the input data by the customer is present in the system or not
                        if(stock<=laste.dataval["stock"]):
                            bill.append(laste.dataval["price"]*stock)        #append the price for the particular product considering the amount of itmes he purchased 
                            laste.dataval["stock"] = laste.dataval["stock"] - stock      #deducting the amount of purchased items from the stock
                            user.append(laste.dataval)
                            if(laste.dataval==b.dataval):            
                                cashier_object.bill_generation(bill)
                            category=str(input("Enter the category of the product you want:"))
                            if(category=="None"):
                                flag=False
                                break
                            brand=str(input("Enter the brand of the product you want:"))

                            try:
                                stock=int(input("Enter the stock you want for that product:"))          #signifies the stock for that particular item
                            except:
                                print("The stock should be in numeric. Please enter it again")
                                stock=int(input("Enter the stock:"))

                            quantity=str(input("Enter the quantity of the willing product:"))
                            laste=laste.prev   #incrementing the counter
                            
                else:
                    laste=laste.prev

            if flag==False:
                return bill
            else:
                cashier_object.bill_generation(bill)    #after the loop ends returning back to the same method

 
    def display_total_bill(self, user):
        for i in range(0,len(user)):
            print(user[i])     #display the itmes bought by the customer
            print("\n")         

        bill.clear()
        user.clear()


    def final_bill(self, bill, user):
        final_bill = cashier_object.bill_generation(bill)
        c=0
        for amount in final_bill:       #retreiving the amount from the bill list which contains the price of each product
            c=c+amount
        final_amount=c+0.28*c           #GST added in the final amount
        print ("the finall bill is:",final_amount)   #display the final amount

        cashier_object.display_total_bill(user)
        
        if(2000<=c<=3000):    
            final_amount=((float(5*c))/100)
            print("the discount amount is:",final_amount)  #discount if bought between this certain price
            e=c-final_amount
            final_amount=e+0.28*e                #GST added in the final amount
            print ("the finall bill is:",final_amount)
            
            cashier_object.display_total_bill(user)


        if(3000<c<=5000):
            final_amount=((float(10*c))/100)
            print("the discount amount is:",final_amount)     #discount if bought between this certain price
            k=c-final_amount
            final_amount=k+0.28*k                 #GST added in the final amount
            print ("the finall bill is:",final_amount)

            cashier_object.display_total_bill(user)
            

cashier_object=Cashier()         #creating an object of admin class
bill=[]              #initializing a bill list which will store the price of items
user=[]              #initializing a user list to store the itmes bought by him

while True:
    choice=int(input("Enter the steps choice:"))
    if(choice==1):
        cashier_object.add_item()
    if(choice==2):
        cashier_object.display()
    if (choice==3):
        cashier_object.final_bill(bill, user)
    if(choice==4):
        break