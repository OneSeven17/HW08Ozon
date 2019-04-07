from app.ozon import create_book, add_book, search_books


def test_create_book():

    data = {
    'id': 'id',
    'title': 'Война и мир',
    'author': 'Толстой',
    'price': 1000,
    'tags': 'война, любовь',
    'url': 'url',
     }

    result = create_book(data['id'], data['title'], data['author'], data['price'], data['tags'], data['url'])

    assert data == result

def test_add_one_book_to_empty_library():
    container = []
    book = create_book('Война и мир', 'Толстой', 1000, 'война, любовь', 'http://forkidsandmum.ru/pictures/books_covers/1010257708.jpg')

    add_book(container, book)

    assert len(container) == 1
    assert book in container

def test_search_title():
    books_list = []
    war_and_piece = create_book(
        'Война и мир',
        'Толстой',
        1000,
        'война, любовь',
        'http://forkidsandmum.ru/pictures/books_covers/1010257708.jpg'
    )
    anna_karenina = create_book(
        'Анна Каренина',
        'Толстой',
        500,
        'поезд, любовь',
        'https://img.yakaboo.ua/media/catalog/product/cache/1/image/234c7c011ba026e66d29567e1be1d1f7/c/o/cover1_229_52.jpg'
    )

    idiot = create_book(
        'Идиот',
        'Достоевский',
        700,
        'роман, любовь, драма, достоевский',
        'https://ozon-st.cdn.ngenix.net/multimedia/1022171034.jpg'
    )

    crime_and_justice = create_book(
        'Преступление и наказание',
        'Достоевский',
        700,
        'роман, достоевский, драма',
        'https://biblio.by/media/catalog/product/cache/1/image/1200x1200/9df78eab33525d08d6e5fb8d27136e95/2/7/2785.jpg'
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
        'url': 'http://forkidsandmum.ru/pictures/books_covers/1010257708.jpg'
    }]
    result = search_books(books_list, 'мир')
    assert founded_book == result

def test_search_author():
    books_list = []
    war_and_piece = create_book(
        'Война и мир',
        'Толстой',
        1000,
        'война, любовь',
        'http://forkidsandmum.ru/pictures/books_covers/1010257708.jpg'
    )

    idiot = create_book(
        'Идиот',
        'Достоевский',
        700,
        'роман, любовь, драма, достоевский',
        'https://ozon-st.cdn.ngenix.net/multimedia/1022171034.jpg'
    )

    crime_and_justice = create_book(
        'Преступление и наказание',
        'Достоевский',
        700,
        'роман, достоевский, драма',
        'https://biblio.by/media/catalog/product/cache/1/image/1200x1200/9df78eab33525d08d6e5fb8d27136e95/2/7/2785.jpg'
    )
    add_book(books_list, war_and_piece)
    add_book(books_list, idiot)
    add_book(books_list, crime_and_justice)

    founded_book = [{
        'title': 'Война и мир',
        'author': 'Толстой',
        'price': 1000,
        'tags': 'война, любовь',
        'url': 'http://forkidsandmum.ru/pictures/books_covers/1010257708.jpg'
    }]

    result = search_books(books_list, 'Толстой')
    assert founded_book == result

def test_search_tag():
    books_list = []
    war_and_piece = create_book(
        'Война и мир',
        'Толстой',
        1000,
        'война, любовь',
        'http://forkidsandmum.ru/pictures/books_covers/1010257708.jpg'
    )
    anna_karenina = create_book(
        'Анна Каренина',
        'Толстой',
        500,
        'поезд, любовь',
        'https://img.yakaboo.ua/media/catalog/product/cache/1/image/234c7c011ba026e66d29567e1be1d1f7/c/o/cover1_229_52.jpg'
    )

    idiot = create_book(
        'Идиот',
        'Достоевский',
        700,
        'роман, любовь, драма, достоевский',
        'https://ozon-st.cdn.ngenix.net/multimedia/1022171034.jpg'
    )

    crime_and_justice = create_book(
        'Преступление и наказание',
        'Достоевский',
        700,
        'роман, достоевский, драма',
        'https://biblio.by/media/catalog/product/cache/1/image/1200x1200/9df78eab33525d08d6e5fb8d27136e95/2/7/2785.jpg'
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
        'url': 'https://img.yakaboo.ua/media/catalog/product/cache/1/image/234c7c011ba026e66d29567e1be1d1f7/c/o/cover1_229_52.jpg'
    }]
    result = search_books(books_list, 'поезд')
    assert founded_book == result