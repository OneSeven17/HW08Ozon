import os

from flask import Flask, render_template, request, url_for

from ozon import create_book, add_book, search_books
from werkzeug.utils import redirect

from app.ozon import search_book_by_id, remove_book_by_id, create_empty_book, change_book


def start():
    app = Flask(__name__)

    books_list = []

    war_and_piece = create_book(
        'Война и мир',
        'Толстой',
        1000,
        'война, любовь'
    )

    anna_karenina = create_book(
        'Анна Каренина',
        'Толстой',
        500,
        'поезд, любовь'
    )

    idiot = create_book(
        'Идиот',
        'Достоевский',
        700,
        'роман, любовь, драма, достоевский'
    )

    crime_and_justice = create_book(
        'Преступление и наказание',
        'Достоевский',
        700,
        'роман, достоевский, драма'
    )

    books_list = add_book(books_list, war_and_piece)
    books_list = add_book(books_list, anna_karenina)
    books_list = add_book(books_list, idiot)
    books_list = add_book(books_list, crime_and_justice)

    @app.route('/')
    def index():
        search = request.args.get('search')
        if search:

            results = search_books(books_list, search)
            return render_template('index.html', books=results, search=search)
        return render_template('index.html', books=books_list)

    @app.route('/books/<id>')
    def book_details(id):
        result = search_book_by_id(books_list, id)
        return render_template('book-details.html', book=result)

    @app.route('/books/<id>/edit') # id = 0 новый объект, id <> 0  существующий объект
    def book_edit(id):
        book = None
        if id == 'new':
            book = create_empty_book()
        else:
            book = search_book_by_id(books_list, id)
        return render_template('book-edit.html', book=book)

    @app.route('/books/<id>/save', methods=['POST'])
    def book_save(id):
        nonlocal books_list
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        tags = request.form['tags']
        if id == 'new':
            book = create_book(title=title, author=author, price=price, tags=tags)
            books_list = add_book(books_list, book)
        else:
            books_list = remove_book_by_id(books_list, id)
            book = change_book(id=id, title=title, author=author, price=price, tags=tags)
            books_list = add_book(books_list, book)
        return redirect(url_for('book_details', id=book['id']))

    @app.route('/books/<id>/remove', methods=['POST']) # routing, mapping url
    def book_remove(id):
        nonlocal books_list
        books_list = remove_book_by_id(books_list, id)
        return redirect(url_for('index'))

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9871, debug=True)


if __name__ == '__main__':
    start()