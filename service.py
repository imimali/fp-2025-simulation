from repository import Repository
from book import Book

class Service:

    def __init__(self,repo: Repository):
        self.__repo=repo
        self.__title_filter = ""
        self.__year_filter = -1

    def get_all(self):
        return self.__repo.get_all()

    def add(self,b_id, title,author,year):
        book =Book(b_id,title,author, year)
        # TODO validate if applicable
        self.__repo.add(book)

    def books_by_year_digit(self,digit):
        result =[]
        for book in self.get_all():
            if digit in str(book.get_year()):
                result.append(book)

        return result

    def delete_books_by_year_digit(self,digit):
        books_by_digit = self.books_by_year_digit(digit)
        for book in books_by_digit:
            self.__repo.delete_book(book)

    def get_all_filtered(self):
        result = []
        for book in self.get_all():
            if self.__title_filter in book.get_title() and book.get_year()< self.__year_filter:
                result.append(book)

        return result

    def set_filter(self,new_title_filter,new_year_filter):
        self.__year_filter=new_year_filter
        self.__title_filter=new_title_filter

    def get_filters(self):
        return (self.__year_filter,self.__title_filter)
