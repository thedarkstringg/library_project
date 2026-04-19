app_name = 'library'
version = '0.1.0'
is_active = True
book_count = 0

print(f"App name: '{app_name}', version: {version}")

def create_book(title, year, author, genre = "Unknown"):
    book = {"title": title, "year": year, "author": author, "genre": genre, "is_read": False}
    return book

def is_classic(book):
    if book["year"] < 1950:
        return True
    else:
          return False