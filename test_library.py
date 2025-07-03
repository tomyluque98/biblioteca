import unittest
from models import Book, Magazine
from utils import checkout_items, count_items, find_by_title, load_library_items
import tempfile
import os

class TestLibrary(unittest.TestCase):
    def test_book_creation_valid(self):
        b = Book("Python", 1, "Author", 100)
        self.assertEqual(b.title, "Python")

    def test_magazine_creation_invalid(self):
        with self.assertRaises(ValueError):
            Magazine("", -1, -5)

    def test_checkout(self):
        b = Book("Python", 1, "Author", 100)
        m = Magazine("Science", 2, 30)
        self.assertIn("checked out by", b.checkout("Alice"))
        self.assertIn("issue", m.checkout("Bob"))

    def test_checkout_items(self):
        items = [Book("A", 1, "X", 100), Magazine("B", 2, 5)]
        results = checkout_items(items, "User")
        self.assertEqual(len(results), 2)

    def test_count_items(self):
        items = [Book("A", 1, "X", 100), Magazine("B", 2, 5), Book("C", 3, "Y", 200)]
        counts = count_items(items)
        self.assertEqual(counts["book"], 2)
        self.assertEqual(counts["magazine"], 1)

    def test_find_by_title(self):
        items = [Book("Python Basics", 1, "X", 100), Magazine("Advanced Python", 2, 3)]
        found = find_by_title(items, "python")
        self.assertEqual(len(found), 2)

    def test_load_library_items(self):
        content = "book,Learn C++,1,John,300\nmagazine,Tech Today,2,15\ninvalid,line"
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
            f.write(content)
            path = f.name
        items = load_library_items(path)
        os.remove(path)
        self.assertEqual(len(items), 2)

if __name__ == '__main__':
    unittest.main()
