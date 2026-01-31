from service import Service


class UI:
    def __init__(self, service: Service):
        self.__service = service

    def print_menu(self):
        print("1. Add books")
        print("2. Delete books by year digit")
        print("3. Set filters")
        print("4. Undo last deletion")
        print("5. Print all books")
        ...

    def print_all(self):
        for book in self.__service.get_all():
            print(book)

    def read_valid_number(self, message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Invalid number, try again")

    def read_valid_digit(self, message):
        while True:
            try:
                result = input(message)
                if not result.isdigit():
                    raise ValueError
                return result
            except ValueError:
                print("Invalid number, try again")

    def add(self):

        b_id = self.read_valid_number("Enter id: ")
        title = input("Enter title: ")
        author = input("Enter author: ")
        year = self.read_valid_number("Enter year: ")
        self.__service.add(b_id, title, author, year)

    def delete_by_digit(self):
        digit = self.read_valid_digit("Enter digit: ")
        self.__service.delete_books_by_year_digit(digit)

    def print_all_filtered(self):
        year_filter, title_filter = self.__service.get_filters()
        print(f"Current filters: year={year_filter}, title={title_filter}")
        for book in self.__service.get_all_filtered():
            print(book)

    def set_filters(self):
        year_filter = self.read_valid_number("Enter year filter: ")
        title_filter = input("Enter title filter: ")
        self.__service.set_filter(title_filter, year_filter)

    def undo(self):
        try:
            self.__service.perform_undo()
        except ValueError:
            print('Nothing to undo')

    def run(self):

        while True:
            self.print_all_filtered()
            self.print_menu()
            command = input("Enter option: ")
            match command:
                case '5':
                    self.print_all()

                case '1':
                    self.add()

                case '2':
                    self.delete_by_digit()

                case '3':
                    self.set_filters()

                case '4':
                    self.undo()
