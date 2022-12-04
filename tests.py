from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тест на добавление книги
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин Колец')
        collector.add_new_book('Гарри Поттер')

        assert len(collector.get_books_rating()) == 2

    # Тест на добавление книги дважды

    def test_add_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Великий Гэтсби')
        collector.add_new_book('Великий Гэтсби')
        assert collector.favorites == []
        assert len(collector.books_rating()) == 1

    # Тест на присваивание рейтинга несуществующей книге
    def test_add_rating_to_unreal_book_fails(self):
        collector = BooksCollector()
        collector.add_new_book('похождения бравого солдата Швейка')
        collector.set_book_rating('швейк', 5)
        assert collector.favorites == []
        assert collector.books_rating == {'похождения бравого солдата Швейка': 1}


# Тест на невозможность присваивания рейтинга меньше 1
def test_cant_set_rating_less_than_one(self):
    collector = BooksCollector()
    collector.add_new_book('Charmed')
    collector.set_book_rating('Charmed', 0)
    assert collector.favorites == []
    assert collector.books_rating == {'Charmed': 1}


# Тест на невозможность присваивания рейтинга больше 10
def test_cant_set_rating_greater_than_ten(self):
    collector = BooksCollector()
    collector.add_new_book('Убить пересмешника')
    collector.set_book_rating('Убить пересмешника', 11)
    assert collector.favorites == []
    assert collector.books_rating == {'Убить пересмешника': 1}


# Тест на отсутсвие рейтинга у несуществующей книги
def test_unreal_book_has_no_rating(self):
    collector = BooksCollector()
    collector.add_new_book('Понедельник начинается в субботу')
    rating = collector.get_book_rating('Пикник на обочине')
    assert rating is None


# Тест на добавление книг в избранное
def test_add_to_favorites(self):
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение')
    collector.add_book_in_favorites('Гордость и предубежднеие')
    assert books_collector.favorites == ['Гордость и предубеждение']
    assert books_collector.books_rating == {'Гордость и предубеждение': 1}


# Тест на невозможность добалвения в избранное ,если книги нет в словаре
def test_add_to_favorites_fails_if_not_in_ratings(self):
    collector = BooksCollector()
    collector.add_book_in_favorites('Аэропорт')
    assert collector.favorites == []
    assert collector.books_rating == {}


# тест на удаление книг из избранного
def test_delete_from_favorites(self):
    collector = BooksCollector()
    collector.add_new_book('Трудно быть Богом')
    collector.add_book_in_favorites('Трудно быть Богом')
    collector.delete_book_from_favorites('Трудно быть Богом')
    assert books_collector.favorites == []
    assert books_collector.books_rating == {'Трудно быть Богом': 1}