class Book:
    def __init__(self, book_name, book_code, book_price, book_year, book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_price = book_price
        self.book_year = book_year
        self.book_author = book_author

    def __str__(self):
        return f'{self.book_code} {self.book_name} {self.book_price} \
{self.book_author} {self.book_year}'

    def __repr__(self):
        return f'{self.book_code} {self.book_name} {self.book_price} \
{self.book_author} {self.book_year}'

    def __lt__(self, other):
        return self.book_name < other.book_name


books = [
    Book('A1', 121, 12.34, 2022, 'BC'),
    Book('A1', 124, 34.22, 2021, 'BB'),
    Book('A2', 125, 20, 2022, 'BC'),
    Book('A3', 120, 7.43, 2021, 'AC'),
]


def sort_name(books):
    print(sorted(books, reverse=True))


def author(books, author):
    for book in books:
        if book.book_author == author:
            print(book)


def search_book(books, code):
    for book in books:
        if book.book_code == code:
            print(book.book_year)
            return
    print('The book is not found!')


sort_name(books)
author(books, 'BC')
author(books, 'XY')
search_book(books, 119)
search_book(books, 121)
