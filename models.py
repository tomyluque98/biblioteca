from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title: str, item_id: int):
        if not title.strip():
            raise ValueError("Title must not be empty.")
        if item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")
        self.title = title
        self.item_id = item_id

    @abstractmethod
    def checkout(self, user: str) -> str:
        pass

class Book(LibraryItem):
    def __init__(self, title: str, item_id: int, author: str, pages: int):
        super().__init__(title, item_id)
        if not author.strip():
            raise ValueError("Author must not be empty.")
        if pages <= 0:
            raise ValueError("Pages must be positive.")
        self.author = author
        self.pages = pages

    def checkout(self, user: str) -> str:
        return f"Book '{self.title}' checked out by {user}."

class Magazine(LibraryItem):
    def __init__(self, title: str, item_id: int, issue_number: int):
        super().__init__(title, item_id)
        if issue_number <= 0:
            raise ValueError("Issue number must be positive.")
        self.issue_number = issue_number

    def checkout(self, user: str) -> str:
        return f"Magazine '{self.title}' issue {self.issue_number} checked out by {user}."
