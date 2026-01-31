import unittest
from book import Book
from repository import Repository
from service import Service
class DomainTests(unittest.TestCase):
    def testDomain(self):
        book = Book(1,"The Master and Margarita","Mihail Bulgakov",1932)
        self.assertEqual(book.get_id(),1)
        self.assertEqual(book.get_title(),"The Master and Margarita")
        self.assertEqual(book.get_author(),"Mihail Bulgakov")
        self.assertEqual(book.get_year(),1932)


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.repo = Repository("test_books.txt")

    def tearDown(self):
        with open('test_books.txt',"w") as f:
            f.writelines("""1,Master and Margarita,Mihail Bulgakov,1932
2,Satantango,Krasznahorkai,1990""")

    def testGetAll(self):
        books = self.repo.get_all()
        self.assertEqual(len(books),2)
        self.assertEqual(books[0].get_title(),"Master and Margarita")
        self.assertEqual(books[1].get_title(), "Satantango")

        self.assertEqual(books[0].get_id(),1)
        self.assertEqual(books[1].get_id(),2)

        self.assertEqual(books[0].get_year(),1932)
        self.assertEqual(books[1].get_year(),1990)

    def testAdd(self):
        book = Book(3,"Flowers for Algernon", "Dan Keyes",2000)
        self.repo.add(book)
        books = self.repo.get_all()
        self.assertEqual(len(books),3)
        self.assertEqual(books[2].get_title(),"Flowers for Algernon")
        self.assertEqual(books[2].get_year(),2000)


    # TODO test read and write to file, multiple test cases, etc.


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = Service(Repository("test_books.txt"))

    def tearDown(self):
            with open('test_books.txt', "w") as f:
                f.writelines("""1,Master and Margarita,Mihail Bulgakov,1932
2,Satantango,Krasznahorkai,1990""")

    def testGetAll(self):
        books = self.service.get_all()
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].get_title(), "Master and Margarita")
        self.assertEqual(books[1].get_title(), "Satantango")

        self.assertEqual(books[0].get_id(), 1)
        self.assertEqual(books[1].get_id(), 2)

        self.assertEqual(books[0].get_year(), 1932)
        self.assertEqual(books[1].get_year(), 1990)


    def testAdd(self):
        self.service.add(3, "Flowers for Algernon", "Dan Keyes", 2000)
        books = self.service.get_all()
        self.assertEqual(len(books), 3)
        self.assertEqual(books[2].get_title(), "Flowers for Algernon")
        self.assertEqual(books[2].get_year(), 2000)








