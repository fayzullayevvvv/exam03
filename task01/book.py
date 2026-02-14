from datetime import datetime


class Book:
    def __init__(self, id: int, title: str, author: str, pages: int):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("id musbat butun son bo'lishi kerak")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title bo'sh bo'lmasligi kerak")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("author bo'sh bo'lmasligi kerak")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("pages 0 dan katta bo'lishi kerak")

        self.id = id
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False
        self.borrower = None
        self.borrow_history = []
        self.archived = False

    def borrow(self, user: str) -> None:
        if self.archived == True:
            raise RuntimeError
        elif self.is_borrowed == True:
            raise RuntimeError
        else:
            self.is_borrowed = True
            self.borrower = user
            self.borrow_history.append((user, datetime.now()))

    def return_book(self) -> None:
        if self.is_borrowed == False:
            raise RuntimeError
        else:
            self.borrower = None
            self.is_borrowed = False

    def change_title(self, new_title: str) -> None:
        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError()
        if self.archived:
            raise RuntimeError()

        self.title = new_title

    def archive(self) -> None:
        if self.is_borrowed == True:
            raise RuntimeError
        else:
            self.archived = True

    def info(self) -> dict:
        if self.archived == True:
            status = "archived"
        elif self.is_borrowed == True:
            status = "borrowed"
        else:
            status = "available"

        result = {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "status": status,
            "borrower": self.borrower,
            "times_borrowed": len(self.borrow_history),
        }

        return result

    def __str__(self):
        return f"<Book {self.title}>"

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', borrowed={self.is_borrowed})"

    def __eq__(self, other):
        return self.id == other

    def __len__(self):
        return self.pages

    def __bool__(self):
        if self.archived == True:
            return False
        else:
            return True
