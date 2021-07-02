#ATTRIBUTES:
#quantity
#price
#category list: list
#brand list :list
#brand quantity with price :dictionary
#bill number
#present time
#expiry of product
#discount if
import datetime
now=datetime.datetime.now().strftime("%Y-%m")
class admin(object):
    def __init__(self,username,password):
        self.username=username
        self.password=password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self,username):
        while True:
            if (username=="Bonish"):
                break

            else:
                username=str(input("Enter the correct username"))


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,password):
        while True:
            if(password=="bonish@123"):
                break
            else:
                password=input("Enter the  correct password")
username=str(input("Enter the username"))
password=str(input("Enter the password"))
s=admin(username,password)
class product(object):
    def __init__(self,id,category,brand,quantity,price,expiry):
        self.id=id
        self.category=category
        self.brand=brand
        self.quantity=quantity
        self.price=price
        self.expiry=expiry

    def add_items(self):

        x.append(product(input("Enter the id:"),
                        str(input("Enter the category:")),
                        str(input("Enter the brand_name:")),
                        str(input("Enter the quantity of brand:")),
                        input("Enter the price:"),
                        str(input("Enter the expiry:"))))
        newnode=node(x)



    def display(self):
        for s in x:
            #print s.id,s.category,s.brand,s.quantity,s.price,s.expiry
            print("id:",s.id)
            print("category:",s.category)
            print("brand:",s.brand)
            print("quantity:",s.quantity)
            print("price:",s.price)
            print("expiry:",s.expiry)


    def bill_payment(self):
        while True:
            choice=input("Enter the choices for bill making")
            if choice==1:
                a=str(input("Enter the category"))
                b=str(input("Enter the brand name"))
                c=str(input("Enter the quantity"))
                for j in x:
                    if(j.category==a and j.brand==b and j.quantity==c):
                        for i in range(0,len(j.expiry)):
                            if(expiry[3]<now[3]):
                                bill.append(j.price)
                                j.display()
                                break
                            if(expiry[3]==now[3]):
                                if(expiry[5]<now[5]):
                                    bill.append(j.price)
                                    j.display()
                                    break
                                if(expiry[5]==now[5]):
                                    if(expiry[6]<now[6]):
                                        bill.append(j.price)
                                        j.display()
                                        break
                                    else:
                                        print("product is expired")

                        #bill.append(j.price)
                        #j.display()
                  #  else:
                   #     print("not found")

            if choice==2:
                break

    def bill_amount(self):
        c=0
        for i in bill:

            c=c+i
        print (c)
        if(2000<=c<=3000):
            d=((float(5*c))/100)
            print("the discount amount is:",d)
            e=c-d
            print("the amount after discount is:",e)
        if(3000<c<=5000):
            q=((float(10*c))/100)
            print("the discount amount is:",q)
            k=c-q
            print("the amount after discount is:",k)









x=[]
bill=[]
s=product(id,"bonish","h","10 g",20,10)
print("1. Add products")
print("3. Make the bill for the customer")
print("4. Final printing of the amount")
print("5. Storing the data into a file")
print("6. Finally terimating the program")

while True:
    choice=int(input("Enter the steps choice:"))
    if(choice==1):
        s.add_items()



    if choice==2:
        s.display()
    if choice==3:
        s.bill_payment()
    if choice==4:
        s.bill_amount()

    if(choice==6):
        break