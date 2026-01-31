from repository import Repository
from service import Service
from ui import UI
if __name__ == '__main__':
    repo = Repository("books.txt")
    serice = Service(repo)
    ui = UI(serice)
    ui.run()