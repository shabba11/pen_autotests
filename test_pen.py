import pytest
from Pen import *
from errors import *


class TestGetColor:
    """
    Проверки функции get_color в классе Pen.
    """

    @pytest.mark.parametrize("color_test", [
        "blue",
        "yellow",
        "",
        None,
        5,
        2.1,
        True,
        False
    ])
    def test_get_color(self, color_test):
        # проверка возвращения правильного значения get_color если нет никакой базы данных
        # принимаются значения равные любому типу "str"
        what_color = Pen(color=color_test).get_color()
        assert what_color == str(color_test), equal_error(str(color_test), what_color)


class TestCheckPenState:
    """
    Проверка функции check_pen_state в классе Pen.
    """

    @pytest.mark.parametrize("pen_state_test", [
        1000,
        0,
        -1,
        1.2,
        0.6,
        -0.3,
        "number",
        True,
        False,
        None,
    ])
    def test_check_pen_state(self, pen_state_test):
        # проверка возвращения правильного значения ink_container_value

        # возвращение ответа от функции check_pen_state
        def check_function(value=1000):
            function = Pen(ink_container_value=value).check_pen_state()
            return function

        # проверки при передаваемом значении integer
        if isinstance(pen_state_test, int) and pen_state_test > 0:
            assert check_function(
                pen_state_test) is True, equal_error('True', check_function(pen_state_test))
        elif isinstance(pen_state_test, int) and pen_state_test <= 0:
            assert check_function(
                pen_state_test) is False, equal_error('False', check_function(pen_state_test))

        # проверки при передаваемом значении float
        if isinstance(pen_state_test, float) and pen_state_test > 0 and pen_state_test < 1:
            assert check_function(
                pen_state_test) is False, equal_error('True', check_function(pen_state_test))
        elif isinstance(pen_state_test, float) and pen_state_test >= 1:
            assert check_function(
                pen_state_test) is True, equal_error('True', check_function(pen_state_test))
        elif isinstance(pen_state_test, float) and pen_state_test <= 0:
            assert check_function(
                pen_state_test) is False, equal_error('True', check_function(pen_state_test))

        # проверки при передаваемом значении bool
        if isinstance(pen_state_test, bool) or pen_state_test is None or isinstance(pen_state_test, str):
            try:
                assert Pen(ink_container_value=pen_state_test) != Pen().ink_container_value(
                ), equal_error('True', check_function(pen_state_test))
                assert check_function(
                    pen_state_test) is True, equal_error('True', check_function(pen_state_test))
            except TypeError:
                pass
            except ValueError:
                pass


class TestCheckWrite:
    """
    Проверки функции write
    """
    @pytest.mark.parametrize("ink_container_value_test,size_letter_test,word_test",
                             [(0, 1.0, "Hello"),
                              (10, 1.0, "Hello"),
                              (15, 2.0, "HelloWorld!"),
                              ]
                             )
    def test_check_write_if_container_value_zero(self, ink_container_value_test, size_letter_test, word_test):
        # Проверки функции write при разных значениях ink_container_value, size_letter и word

        # Записываем возвращаемое значение функции в переменную
        check_function = Pen(
            ink_container_value=ink_container_value_test, size_letter=size_letter_test).write(word_test)

        # Записываем размер слова в переменную
        size_of_word_test = len(word_test) * size_letter_test

        # Записываем часть слова в переменную
        part_of_word_test = word_test[0: int(
            ink_container_value_test // size_letter_test)]

        # проверка исходя из логики вводимых данных
        if ink_container_value_test <= 0:
            assert check_function == "", equal_error("пустое значение - ''", check_function)
        elif size_of_word_test <= ink_container_value_test:
            assert check_function == word_test, equal_error(word_test, check_function)
        elif size_of_word_test > ink_container_value_test > 0:
            assert check_function == part_of_word_test, equal_error(part_of_word_test, check_function)


class TestDoSomething:
    """
    Проверка работы функции do_something_else
    """

    @pytest.mark.parametrize("color_test",
                             ["white",
                              None,
                              ]
                             )
    def test_do_something_else(self, color_test):
        # проверка функции do_something_else
        check_function = Pen(color=color_test).do_something_else()
        assert check_function == 'blue', equal_error('blue', check_function)
