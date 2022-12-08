
from main import BooksCollector

class TestBooksCollector:
    def test_add_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и Мир')
        assert collector.books_rating == {'Война и Мир': 1}

    def test_add_book_twice_false(self):
        collector = BooksCollector()
        collector.add_new_book('Великий Гэтсби')
        collector.add_new_book('Великий Гэтсби')
        assert collector.books_rating == {'Великий Гэтсби': 1}

    def test_add_rating_to_unreal_book_fails(self):
        collector = BooksCollector()
        collector.set_book_rating('швейк', 5)
        assert collector.books_rating == {}

    def test_cant_set_rating_less_than_one_fail(self):
        collector = BooksCollector()
        collector.add_new_book('Charmed')
        collector.set_book_rating('Charmed', 0)
        assert collector.books_rating == {'Charmed': 1}

    def test_cant_set_rating_more_than_ten_fail(self):
        collector = BooksCollector()
        collector.add_new_book('Убить пересмешника')
        collector.set_book_rating('Убить пересмешника', 11)
        assert collector.books_rating == {'Убить пересмешника': 1}

    def test_unreal_book_has_no_rating(self):
        collector = BooksCollector()
        rating = collector.get_book_rating('Пикник на обочине')
        assert rating == None
    def test_add_book_to_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        assert collector.favorites == ['Гордость и предубеждение']

    def test_add_to_favorites_if_not_in_ratings_fails(self):
            collector = BooksCollector()
            collector.add_book_in_favorites('Аэропорт')
            assert collector.favorites == []
            assert collector.books_rating == {}

    def test_delete_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Трудно быть Богом')
        collector.add_book_in_favorites('Трудно быть Богом')
        collector.delete_book_from_favorites('Трудно быть Богом')
        assert collector.favorites == []



