from service import Service


class UI:
    def __init__(self, service: Service):
        self.__service = service

    def print_menu(self):
        print("1. Add books")
        print("5. Print all books")
        ...

    def print_all(self):
        for book in self.__service.get_all():
            print(book)

    def add(self):

        b_id = int(input("Enter id: "))
        title = input("Enter title: ")
        author = input("Enter author: ")
        year = int(input("Enter year: "))
        self.__service.add(b_id, title, author, year)

    def run(self):

        while True:
            self.print_menu()
            command = input("Enter option: ")
            match command:
                case '5':
                    self.print_all()

                case '1':
                    self.add()
