#1zad
'''while True:
    try:
        n=int(input('Enter n :'))
        if n<0:
            raise Exception("Sorry, no numbers below zero") 
        break
    except ValueError:
        print("integer needed!!")
    except Exception:
        print('input error')
        
while True:
    try:        
        k=int(input('enter k :'))
        if k>0:
            break
    except ValueError as err:
        print(err)
list1=[]
list2=[]
i=0
while i<n:
    num=int(input(f'Enter number {i+1} : '))
    if num>k:
        list1.append(num)
    elif num<=k and num>0:
        list2.append(num)
    i+=1
pr=1
print(list1)
print(list2)
if len(list1)>0:
    for i in range(1,len(list1),2):
        pr=pr*list1[i]
    ind_min=list1.index(min(list1))
    print(pr)
    print(ind_min)
else:
    print('list1 is empty !')
if len(list2)>0:
    raz=max(list2)-min(list2)
    print(raz)
else:
    print('list2 is empty !')'''
    
#2zad
class Book:
    def __init__ (self,name,code, price, year, author):
        self.book_name= name
        self.book_code=code
        self.book_price=price
        self.book_year=year
        self.book_author=author
    def __str__(self):
        return str.format("Name {} code {} price {} year {} author{} ",self.book_name, self.book_code , self.book_price, self.book_year,self.book_author)

books=[Book("Lord",2034,5.64,1995,"George"),Book("Ford",1034,8.64,2000,"Seorge"),Book("Psichologi",3034,15.64,1998,"Aristotel"),Book("The Quinn",5034,55.64,2020,"Jack")]

def sort_name(b_li):
    result_books= sorted(b_li, key= lambda x: x.book_name, reverse=True)
    for l in result_books:
        print(l)
def author(author,b_list):
    for b in b_list:
        if b.book_author==author:
            print(b)
def search_book(code):
    for i in range(len(books)):
        currentbook = books[i]
        if currentbook.book_code == code:
            print(currentbook.book_year)
            return
    print("The book is not found!")
sort_name(books)
author("George",books)
search_book(1034)



