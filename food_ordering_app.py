# for admin
items=["Tandoori Chicken","Vegan Burger","Truffle Cake"]
quantity=[4,1,500]
price=[240,320,900]
discount=[0.1,0.2,0.3]
id=[1,2,3]
amount_left=[]

def edit():
    x=int(input("Enter the item id you want to edit: "))
    items[x]=input("Enter the new item: ")
    price[x]=input("Enter the new price: ")
    discount[x]=input("Enter the new discount: ")
    
def view():
    print("Food items: "+str(items))
    print("Food ids: "+str(id))

def remove():
    x=int(input("Enter the food id you want to remove: "))
    items.pop(x-1)
    quantity.pop(x-1)
    discount.pop(x-1)
    food_id.pop(x-1)
    price.pop(x-1)


    
#for user
a=0
print("Welcome to our food ordering app!! Register and enjoy")
p=input("Full Name: ")
q=input("Phone Number: ")
r=input("Email: ")
s=input("Address: ")
t=input("Password: ")


x=[p,q,r,s,t]
def login():
    print("Login to the application")
    m=input("Phone Number: ")
    n=input("Password: ")

    if m==q and n==t:
        print("Place New Order")
        print("Order History")
        print("Update Profile")
    else:
        print("Error try again!!")

login()

def new():
    print("food items:"+str(items))
    print("food ids:"+str(id))
    print("Price:"+str(price))
    
    l=[]
    for i in range(0,2):
        ele = int(input("Enter food id :"))
        l.append(ele) 
    print(l)
    
    sum=price[l[0]-1]*(1-discount[l[0]-1])+price[l[1]-1]*(1-discount[l[1]-1])
    print("Your total price: "+str(sum))
    
    print("Type Proceed or Cancel")
    s=input("Enter: ")
    if s=="Proceed":
        print("Order Placed, Thank You!")
    elif s=="Cancel":
        print("Cancelled")
    
    print("Your Order History:")
    print(items[l[0]-1])
    print(str(price[l[0]-1]))
    print(items[l[1]-1])
    print(str(price[l[1]-1]))
        
    
new()

def update():
    p=input("Update Full Name: ")
    q=input("Update Phone Number: ")
    r=input("Update Email: ")
    s=input("Update Address: ")
    t=input("Update Password: ")
    print(p,q,r,s,t)