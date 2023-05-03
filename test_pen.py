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

        # записываем значение функции get_color в переменную what_color
        what_color = Pen(color=color_test).get_color()

        # проверяем значение функции с передаваемой переменной с типом str
        assert what_color == str(color_test), equal_error(str(color_test), what_color)


class TestCheckPenState:
    """
    Проверки функции check_pen_state в классе Pen.
    """


    @pytest.mark.parametrize("pen_state_test", [
        1000,
        0,
        -1,
        1.2,
        0.6,
        -0.3
    ])
    def test_check_pen_state_int(self, pen_state_test):
        # проверки при передаваемом значении integer или float

        # записываем значение функции check_pen_state в переменную function
        function = Pen(ink_container_value=pen_state_test).check_pen_state()

        # проверяем значение функции при значении > или <= 0
        if pen_state_test > 0 and pen_state_test < 1:
            assert function is False, equal_error('True', function)
        elif pen_state_test >= 1:
            assert function is True, equal_error('True', function)
        elif pen_state_test <= 0:
            assert function is False, equal_error('False', function)



    @pytest.mark.parametrize("pen_state_test", [
        True,
        False,
        None,
        "number"
    ])
    def test_check_pen_state_bool(self, pen_state_test):
        # проверки при передаваемом значении bool, None и str

        # записываем класс в переменную
        class_pen_test = Pen(ink_container_value=pen_state_test)

        # записываем значение ink_container_value в переменную value_container_test
        value_container_test = class_pen_test.ink_container_value

        # записываем значение функции check_pen_state в переменную function_test
        function_test = class_pen_test.check_pen_state()

        # проверяем значение функции. При типе bool, None и str должен возвращаться True 
        # (при условии что должно записываться стандартное значение ink_container_value = 1000 при попытке отправить эти типы)
        try:
            assert function_test == True and value_container_test == 1000, equal_error(True, function_test)

        # пропускаем ошибки TypeError и ValueError если должна возвращаться ошибка по документации при попытке отправить типы bool, None и str
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
