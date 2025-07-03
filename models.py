from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title: str, item_id: int):
        if not title.strip():
            raise ValueError("El titulo no debe estar vacio!!")
        if item_id <= 0:
            raise ValueError("El ID del item debe ser un numero positivo!!")
        self.title = title
        self.item_id = item_id

    @abstractmethod
    def checkout(self, user: str) -> str:
        pass

class Book(LibraryItem):
    def __init__(self, title: str, item_id: int, author: str, pages: int):
        super().__init__(title, item_id)
        if not author.strip():
            raise ValueError("El autor no debe estar vacio!!")
        if pages <= 0:
            raise ValueError("La cantidad de páginas debe ser positiva")
        self.author = author
        self.pages = pages

    def checkout(self, user: str) -> str:
        return f"Libro '{self.title}' prestado a {user}."

class Magazine(LibraryItem):
    def __init__(self, title: str, item_id: int, issue_number: int):
        super().__init__(title, item_id)
        if issue_number <= 0:
            raise ValueError("El numero de edición debe ser positivo")
        self.issue_number = issue_number

    def checkout(self, user: str) -> str:
        return f"Revista '{self.title}' (Edición {self.issue_number}) prestada a {user}."

