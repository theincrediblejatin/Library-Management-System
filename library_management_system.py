class Library :
    
    def __init__(self , listofBooks) :
        self.books=listofBooks

    def listOfavailableBooks(self) :
        print("Books present in libraray are : ")
        for items in self.books :
            print(" *", items)
    
    def borrowBook(self) :
        a=input("Enter the name of book you want to borrow : ")
        if a in self.books :
            print("You have been issued this book. Enjoy !")
            self.books.remove(a)
        else :
            print("This book is not availble.")
        

    def returnaBook(self) :
        b=input("Enter the name og the book you want to return : ")
        print("Thanks for returning this book.")
        self.books.append(b)


books=Library(["HC Verma", "SL Arora", "Maths", "Chemistry"])

while (True) :
    wlcMsg=('''\n====Welcome====
        1. List all the available books
        2. Request a book
        3. Return a book
        4. Exit the library \n''') 

    print(wlcMsg)

    choice = int(input("Enter your choice : "))

    if choice==1 :
        books.listOfavailableBooks()
    elif choice==2 :
        books.borrowBook()
    elif choice==3 :
        books.returnaBook()
    elif choice==4 :
        exit()
    else :
        print("Invalid Input")