from book import Book

class RepositoryException(Exception):
    pass

class Repository:
    def __init__(self,file_path):
        self.__file_path=file_path
        self.__elements=[]
        self.__read_from_file()

    def __read_from_file(self):
        with open(self.__file_path,'r') as f:
            lines = f.readlines()
            for line in lines:
                b_id,title,author,year_str=line.strip().split(',')
                self.__elements.append(Book(int(b_id),title,author,int(year_str)))

    def __write_to_file(self):
        with open(self.__file_path, 'w') as f:
            for book in self.__elements:
                line = f"{book.get_id()},{book.get_title()},{book.get_author()},{book.get_year()}\n"
                f.write(line)

    def add(self, book):
        self.__elements.append(book)
        self.__write_to_file()

    def delete_book(self, book_to_delete):
        try:
            self.__elements.remove(book_to_delete)
            self.__write_to_file()
        except ValueError:
            raise RepositoryException("Book not found")


    def get_all(self):
        return self.__elements