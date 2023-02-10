from flask import render_template, redirect, request
import datetime

from app import app

from models.book import Book
from models.book_list import get_book_list, add_new_book, delete_book, update_checked_out, update_checked_in

@app.route("/")
def index():
    book_list = get_book_list()
    return render_template("index.html", book_list=book_list, title="Weekend Bookies")

@app.route("/book/<index>")
def inspect_book_by_index(index):
    book_list = get_book_list()
    return render_template("book.html", book=book_list[int(index)], title="Book Inspect")

@app.route("/book/add_new_book")
def new_book_page():
    return render_template("new_book.html")

@app.route("/book/added_new_book", methods=["POST"])
def create_new_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre)
    add_new_book(new_book)
    book_list = get_book_list()
    return redirect("/")

@app.route("/book/<index>/delete", methods=["POST"])
def delete_a_book(index):
    delete_book(int(index))
    return redirect("/")

@app.route("/book/<index>/update_checked_out", methods=["POST"])
def update_check_book(index):
    if 'checked_out' in request.form.keys():
        update_checked_out(int(index))
    else:
        update_checked_in(int(index))
    return redirect("/")