class Book:
    def __init__(self, b_id, title, author, year):
        self.__id = b_id
        self.__title = title
        self.__author = author
        self.__year = year

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def __str__(self):
        return f"Book(id={self.get_id()}, title={self.get_title()},author={self.get_author()},year={self.get_year()})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.get_id() == other.get_id()# TODO compare against more atttributes if applicable
