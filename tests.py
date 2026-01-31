import unittest
from book import Book
from repository import Repository, RepositoryException
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


    def testDelete(self):
        book = Book(1, "Master and Margarita", "Mihail Bulgakov", 1932)
        self.repo.delete_book(book)
        self.assertEqual(len(self.repo.get_all()),1)
        self.assertEqual(self.repo.get_all()[0].get_id(),2)

        book = Book(12222, "Master and Margarita", "Mihail Bulgakov", 1932)
        with self.assertRaises(RepositoryException):
            self.repo.delete_book(book)







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

    def testFilterByDigit(self):
        filtered = self.service.books_by_year_digit("1")
        self.assertEqual(len(filtered),2)

        filtered = self.service.books_by_year_digit("7")
        self.assertEqual(len(filtered),0)

        filtered = self.service.books_by_year_digit("2")
        self.assertEqual(len(filtered),1)
        self.assertEqual(filtered[0].get_id(),1)

    def testDeleteByDigit_DeleteAll(self):
        self.service.delete_books_by_year_digit("1")
        self.assertEqual(len(self.service.get_all()),0)

    def testDeleteByDigit_DeleteOne(self):
        self.service.delete_books_by_year_digit("2")
        books = self.service.get_all()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].get_id(),2)

    def testDeleteByDigit_DeleteNothing(self):
        self.service.delete_books_by_year_digit('7')
        self.assertEqual(len(self.service.get_all()),2)

    def testGetAllFiltered(self):
        self.service.set_filter("", 2050)
        self.assertEqual(len(self.service.get_all_filtered()),2)

        self.service.set_filter("a", 2050)
        self.assertEqual(len(self.service.get_all_filtered()), 2)

        self.service.set_filter("Satan", 2050)
        self.assertEqual(len(self.service.get_all_filtered()), 1)

        self.service.set_filter("", 1980)
        self.assertEqual(len(self.service.get_all_filtered()), 1)

        self.service.set_filter("asdfasdf", 1980)
        self.assertEqual(len(self.service.get_all_filtered()), 0)

    def testRecordForUndo(self):
        self.service.record_for_undo()
        previous_values = self.service.get_all().copy()
        self.assertEqual(self.service.get_undo_stack()[0],previous_values)
        self.service.add(99,"A","B",1111)
        self.assertEqual(self.service.get_undo_stack()[0], previous_values)

    def testPerformUndo(self):
        self.service.record_for_undo()
        previous_values = self.service.get_all().copy()
        self.service.record_for_undo()
        self.service.add(99, "A", "B", 1111)

        self.service.perform_undo()
        self.assertEqual(self.service.get_undo_stack()[0], previous_values)

        self.service.perform_undo()
        with self.assertRaises(ValueError):
            self.service.perform_undo()




class SomeTest(unittest.TestCase):
    def setUp(self):
        print('setting up')
    def tearDown(self):
        print('tearing down')

    def testSomething(self):
        print('test 1 running')

    def testSomethingElse(self):
        print('test 2 running')











