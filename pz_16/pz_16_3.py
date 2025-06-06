# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в бинарном формате.
import pickle
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Чтение книги: '{self.title}' автора {self.author}.")

def save_def(book_list, filename):
    with open(filename, 'wb') as file:
        pickle.dump(book_list, file)
    print("Книги успешно сохранены в файл.")

def load_def(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

if __name__ == "__main__":
    book1 = Book("1984", "Джордж Оруэлл", 328)
    book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 470)
    book3 = Book("Гарри Поттер", "Дж. К. Роулинг", 410)
    books = [book1, book2, book3]

    save_def(books, "books.pkl")

    loaded_books = load_def("books.pkl")

    for book in loaded_books:
        book.read()
