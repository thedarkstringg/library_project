app_name = 'library'
version = '0.1.0'
is_active = True
book_count = 0

#Task 1
print(f"App name: '{app_name}', version: {version}")

def create_book(title, year, author, genre = "Unknown"):
    book = {"title": title, "year": year, "author": author, "genre": genre, "is_read": False}
    return book

def is_classic(book):
    if book["year"] < 1950:
        return True
    else:
          return False

# Task 2    
book1 = create_book("Holes", 1998, "Unknown")

print(is_classic(book1))

library = []

def add_book(book):
    library.append(book)

def remove_book(title):
    for book in library:
        if book["title"] == title:
            library.remove(book)
            return
    print(f"Book with title '{title}' not found in library.")

def all_genres():
    genre=set()
    for book in library:
        genre.add(book["genre"])
    return genre

#Task 3
classic_books= [book["title"] for book in library if book["year"] < 1950]

authors = [book["authors"] for book in library]

def book_iterator(genre_filter=None):
    for book in library:
        if genre_filter is None or book["genre"] == genre_filter:
            yield book

#Task 4
import json
def save_library(filename = "file.json"):
    with open_file(filename, "w", encoding = "utf-8") as file:
        json.dump(library, file, indeint=2)
try: 
    with open ("file.json", "r", encoding="utf-8") as file:
        library = json.load(file)
except FileNotFoundError:
    print("No existing library found. Starting with an empty library.")

#Task 5
import os
from datetime import timedelta
import datetime
import sys
import math

now = datetime.datetime.now()

print(f"Current date and time: {now}")

week_later = now + timedelta(days=7)
print(week_later)

#Task 6
class Book:
    def __init__(self, title, year, author, genre, is_read):
        self.title = title
        self.year = year
        self.author = author
        self.genre = genre
        self.is_read = is_read
    def mark_read(self):
        self.is_read = True
    def is_classic(self):
        if self.year< 1950:
            return True
book1 = Book("Holes", "1998", "Stephen Curry", "Adventure", True)