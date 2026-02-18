stock_count=10
def show_statue():
    print(f"the available amount are {stock_count} ")
def add_stock(amount):
    global stock_count
    stock_count += amount
    print("added successfully")
def main():
    print("system of simple inventory")
    while True:
        print('''1 show stock  
2 add new stock
3 quite ''')
        choice=input("choice a process: ")
        if choice == "1":
            show_statue()
        elif choice == "2":
            q=int(input("enter the amount you want to added"))
            add_stock(q)
        elif choice=="3":
            print("close the program")
            break
        else:
            print("wrong choice")
if __name__ =="__main__":
    main()
