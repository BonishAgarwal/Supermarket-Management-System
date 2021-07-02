#import smtplib
#from datetime import date
#today=date.today()
#a,b,c=str(today).split('-')
class manager(object):              # creating a manager class to input his username and password to access the system 
    def __init__(self,username,password):      #constructor defining the username and passsword    
        self._username=username
        self.password=password

    #validations for username and password

    @property                    #getter property for username
    def username(self):
        return self.__username

    @username.setter            #setter method for username
    def username(self,username):
        while True:
            if (username=="admin"):   #applying condition for checking out the correct username
                break

            else:
                username=str(input("Enter the correct username"))   #if not correct enter the username once again until correcct


    @property
    def password(self):       #getter property for password
        return self.__password

    @password.setter          #setter method for password
    def password(self,password):
        while True:
            if(password=="admin"):        #applying condition for checking out the correct password
                break
            else:
                password=input("Enter the  correct password")       #if not correct enter the password once again until correcct

username=str(input("Enter the username"))    #inputing our username
password=str(input("Enter the password"))    #inputing our password
s=manager(username,password)          #creating an object for manager class


class Node(object):               #creating a Node class 
    def __init__(self,dataval=None):        #assigning our data with its next and prev addresses
        self.dataval=dataval
        self.next=None
        self.prev=None


class admin(object):               #creaing an admin class 
    def __init__(self):
        self.headval=None               #assigning a pointer headval


    def add_item(self):          #method to store the items to sell in the supermatket
        while(True):
            #Enter the all the specific details of the particular product
            id=int(input("Enter the id:"))       #every product will have a different id   
            if (id==0):
                break
            category=str(input("Enter the category:"))    #signifies the type of product to be stored
            brand=str(input("Enter the brand:"))          #signifies the brand of that type of product
            stock=int(input("Enter the stock:"))          #signifies the stock for that particular item
            quantity=str(input("Enter the quantity:"))    #signifies the quantity of that product
            price=int(input("Enter the price:"))          #signifies the price of a particular quanity for a pariticular product
            expiry=str(input("Enter the expiry:"))        #Enter the expiry data of every product in a y-m-d format
            dic={"id":id,"category":category,"brand":brand,"stock":stock,"quantity":quantity,"price":price,"expiry":expiry}   #using dictionary as a toll to store the data
            newNode=Node(dic)     #passing the dictionary to the Node class
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

    """def mail(self):
        fromaddr = 'bagarwal@mitaoe.ac.in'  ##pass your username


        username = 'bagarwal@mitaoe.ac.in'   ##pass your username
        password = '9413769019'   ##pass your password
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()"""



#From now onwards we now start to print out the bills for our customer.
#customer gives us the specific details about what product he wants.
#And finally after the details given by the customer, we finally give him the bill containg all the purchased itmes with th final bill

    def bill_generation(self):             
            b=self.headval
            category=str(input("Enter the category1:"))   #customer giving us the details of the product he has to buy
            if(category=="None"):     #after he completes his pruchasing the final bill will be printed
                s1.final_bill()
            brand=str(input("Enter the brand1:"))
            stock=int(input("Enter the stock1:"))
            quantity=str(input("Enter the quantity1:"))
            printval=self.headval
            while printval.next is not None:
                if(category==printval.dataval["category"] and brand==printval.dataval["brand"] and quantity==printval.dataval["quantity"]):       #checking out the condtion to see whether the input data by the customer is present in the system or not
                    if(stock<=printval.dataval["stock"]):
                        bill.append(printval.dataval["price"]*stock)    #append the price for the particular product considering the amount of itmes he purchased 
                        printval.dataval["stock"] = printval.dataval["stock"] - stock
                        if(printval.dataval["stock"]==0):
                            print("stock is empty")
                        user.append(printval.dataval)
                        category=str(input("Enter the category:"))
                        if(category=="None"):
                            s1.final_bill()
                            break
                        brand=str(input("Enter the brand:"))
                        stock=int(input("Enter the stock:"))
                        quantity=str(input("Enter the quantity:"))
                        printval=printval.next
                            
                else:
                    printval=printval.next         #if not found increment the counter
            laste=printval
            while laste is not None:
                if(category==laste.dataval["category"] and brand==laste.dataval["brand"] and quantity==laste.dataval["quantity"]):     #checking out the condtion to see whether the input data by the customer is present in the system or not
                        if(stock<=laste.dataval["stock"]):
                            bill.append(laste.dataval["price"]*stock)        #append the price for the particular product considering the amount of itmes he purchased 
                            laste.dataval["stock"] = laste.dataval["stock"] - stock      #deducting the amount of purchased items from the stock
                            user.append(laste.dataval)
                            if(laste.dataval==b.dataval):            
                                s1.bill_generation()
                            category=str(input("Enter the category2:"))
                            if(category=="None"):
                                s1.final_bill()
                            brand=str(input("Enter the brand2:"))
                            stock=int(input("Enter the stock2:"))
                            quantity=str(input("Enter the quantity2:"))
                            laste=laste.prev   #incrementing the counter
                            
                else:
                    laste=laste.prev
            s1.bill_generation()    #after the loop ends returning back to the same method

 






    def final_bill(self):
        c=0
        for amount in bill:       #retreiving the amount from the bill list which contains the price of each product
            c=c+amount
        d=c+0.28*c           #GST added in the final amount
        print ("the finall bill is:",d)   #display the final amount
        #s1.mail()
        for i in range(0,len(user)):
            print(user[i])     #display the itmes bought by the customer
            print("\n")
        #s1.mail()
        #print (user)            
        bill.clear()          #function to clear out the list
        user.clear()          #function to clear out the list
        if(2000<=c<=3000):    
            d=((float(5*c))/100)
            print("the discount amount is:",d)  #discount if bought between this certain price
            e=c-d
            d=e+0.28*e                #GST added in the final amount
            print ("the finall bill is:",d)
            for i in range(0,len(user)):
                print(user[i])
                print("\n")
            #print (user)
            bill.clear()
            user.clear()

        if(3000<c<=5000):
            q=((float(10*c))/100)
            pri4nt("the discount amount is:",q)     #discount if bought between this certain price
            k=c-q
            d=k+0.28*k                 #GST added in the final amount
            print ("the finall bill is:",d)
            for i in range(0,len(user)):
                print(user[i])
                print("\n")
            #print (user)
            bill.clear()
            user.clear()

s1=admin()         #creating an object of admin class
bill=[]              #initializing a bill list which will store the price of items
user=[]              #initializing a user list to store the itmes bought by him

while True:
    choice=int(input("Enter the steps choice:"))
    if(choice==1):
        s1.add_item()
    if(choice==2):
        s1.display()
    if (choice==3):
        s1.bill_generation()
    if(choice==4):
        break