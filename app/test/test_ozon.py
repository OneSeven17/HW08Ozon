from ozon import create_book, add_book, search_books


def test_create_book():

    data = {
    'title': 'Война и мир',
    'author': 'Толстой',
    'price': 1000,
    'tags': 'война, любовь',
     }

    result = create_book(data['title'], data['author'], data['price'], data['tags'])

    assert data == result

def test_add_one_book_to_empty_library():
    container = []
    book = create_book('Война и мир', 'Толстой', 1000, 'война, любовь')

    add_book(container, book)

    assert  len(container) == 1
    assert book in container

def test_search_title():
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
    add_book(books_list, war_and_piece)
    add_book(books_list, anna_karenina)
    add_book(books_list, idiot)
    add_book(books_list, crime_and_justice)

    founded_book = [{
        'title': 'Война и мир',
        'author': 'Толстой',
        'price': 1000,
        'tags': 'война, любовь',
    }]
    result = search_books(books_list, 'мир')
    assert founded_book == result

def test_search_author():
    books_list = []
    war_and_piece = create_book(
        'Война и мир',
        'Толстой',
        1000,
        'война, любовь'
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
    add_book(books_list, war_and_piece)
    add_book(books_list, idiot)
    add_book(books_list, crime_and_justice)

    founded_book = [{
        'title': 'Война и мир',
        'author': 'Толстой',
        'price': 1000,
        'tags': 'война, любовь',
    }]

    result = search_books(books_list, 'Толстой')
    assert founded_book == result

def test_search_tag():
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
    add_book(books_list, war_and_piece)
    add_book(books_list, anna_karenina)
    add_book(books_list, idiot)
    add_book(books_list, crime_and_justice)

    founded_book = [{
        'title': 'Анна Каренина',
        'author': 'Толстой',
        'price': 500,
        'tags': 'поезд, любовь',
    }]
    result = search_books(books_list, 'поезд')
    assert founded_book == result