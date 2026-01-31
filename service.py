from repository import Repository
from book import Book

class Service:

    def __init__(self,repo: Repository):
        self.__repo=repo

    def get_all(self):
        return self.__repo.get_all()

    def add(self,b_id, title,author,year):
        book =Book(b_id,title,author, year)
        self.__repo.add(book)