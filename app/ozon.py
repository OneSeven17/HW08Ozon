import uuid


def create_book(title, author, price, tags, url):
    return {
    'id': str(uuid.uuid4()),
    'title': title,
    'author': author,
    'price': price,
    'tags': tags,
    'url': url,
    }

def create_empty_book():
    return {
    'id': 'new',
    'title': '',
    'author': '',
    'price': '',
    'tags': '',
    'url': '',
    }

def add_book(container, book):
    copy = container[:]
    copy.append(book)
    return copy


def search_books(container, search): # search - это строка поиска
    search_lowercased = search.strip().lower() #1. search.strip() 2. (результат search.strip вызывается для .lower)
    result = []
    for book in container:
        if search_lowercased in book['title'].lower():
            result.append(book)
            continue # не дает идти дальше на 28 строку

        if search_lowercased in book['author'].lower():
            result.append(book)
            continue

        if search_lowercased in book['tags'].lower():
            result.append(book)
            continue # сейчас она не нужна, но может пригодиться если будем добавлять новое условие
    return result

def search_book_by_id(container, book_id):
    for book in container:
        if book['id'] == book_id:
            return book

def remove_book_by_id(books_list, id):
    result=[]
    for book in books_list:  # фильтрация
        if book['id'] != id:
            result.append(book)
    return result


def change_book(id, title, author, price, tags):
    return {
    'id': id,
    'title': title,
    'author': author,
    'price': price,
    'tags': tags,
    }
