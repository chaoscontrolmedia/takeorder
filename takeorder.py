
#A program for taking orders. Version 2
MENU = {
    "chicken" : 10.99,
    "steak" : 11.99, 
    "mashed potatoes" : 6.99, 
    "veggies" : 5.99, 
    "rice" : 7.99,
    }


name = 'Restaurant'
#Update: Took print statement out of function so that user doesn't get asked the question again if they aren't done with their order.
print(f"Hello, welcome to {name}. What can I get you?")
def get_order():
    
    current_order = []
    
    while True:
        
        order = input() 
        if order in MENU:
            current_order.append(order)
        else:
            print("I'm sorry, we don't serve that")
            
        if is_order_complete():
            #this will be a list
            return current_order
            
        else:
            print("Ok, what else?")
            
            
     
            

def is_order_complete():
    print("Anything else? y/n")
    choice = input()
    if choice == "n":
        return True 
    elif choice == "y":
        return False
       
        
    else: 
        raise Exception("invalid input")
       






def output_order(order_list):
    print("Ok, so you want:")
    
    #total = []

    for order in order_list:

        #total.append(MENU[order])

        #x = sum(total)

        print(f'An order of {order} for {(MENU[order])}')
    #I can't get list comprehension to work with print statements. Does it only work with lists/dictionaries?
    #z = print(f'An order of {order} for {(MENU[order])}' for order in order_list)
    #print(z)
       

    #list comprehension: expression for item in iterable if condition == True
    total2 = [MENU[order] for order in order_list]
    y = sum(total2)



    print(f'Your total comes out to {y}.')
    

    

def main():
    order = get_order()
    output_order(order)
    print("Please drive through the second window.")
    print('Hsave a nice day.')

if __name__ == "__main__":
    main()










'''
#A program for taking orders. Version 1.
MENU = {"chicken", "steak", "mashed potatoes", "veggies", "rice"}



def get_order():
    current_order = []
    while True:
        print("What can I get you?")
        order = input()
        if order in MENU:
            current_order.append(order)
        else:
            print("I'm sorry, we don't serve that")
            continue 
        if is_order_complete():
            return current_order
            

def is_order_complete():
    print("Anything else? y/n")
    choice = input()
    if choice == "n":
        return True 
    elif choice == "y":
        return False
    else: 
        raise Exception("invalid input")

def output_order(order_list):
    print("Ok, so you want")
    for order in order_list:
        print(order)

'''







'''

def y():
    x = (MENU['chicken'])
    y = (MENU['chicken'])
    sum = x + y
    count = 0

 

    for v in MENU.values():
    #for value in MENU.values():
        #print(value)


        #x = sum((v))
   
        
        

        print(v)
        
        
    
#y()


def x():
    dict ={'a' :12 ,'b' :13 ,'c':14} 
    dict= sum(dict.values()) 
    print(dict)
#x()

def main():
    order = get_order()
    output_order(order)
    print("Please drive through the second window")




if __name__ == "__main__":
    main()
'''

