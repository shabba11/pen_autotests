import pytest
from Pen import *


class TestGetColor:
    '''
    Проверки функции get_color в классе Pen.
    '''
    
    @pytest.mark.parametrize("color_test", [
        None,
        "blue",
        "оранжевый",
        "yellow",
        "white",
        "RED",
        "12345",
        "1.2",
        "!@#$%",
        "",
        5,
        2.1,
        True,
        False
        ])
    def test_get_color(self, color_test):
        #проверка возвращения правильного значения get_color если нет никакой базы данных и принимаются любые значения
        if color_test == True or color_test == False or color_test == None:
            assert Pen(color=color_test).get_color() == Pen().color, f"Ошибка в функции get_color. При указании переменной '{color_test}' возвращается значение '{Pen(color=color_test).get_color()}'. Должно возвращаться значение '{Pen().color}'"
        else:
            what_color = Pen(color=color_test).get_color()
            assert isinstance(what_color, str), f"Ошибка в функции get_color. Возвращается значение не равное классу 'str'. Возвращаемое значение {type(what_color)}"
            assert what_color == str(color_test), f"Ошибка в функции get_color. Возвращается значение {what_color} вместо {color_test} или ошибка в самой функции 'get_color'"

class TestCheckPenState:
    '''
    Проверка функции check_pen_state в классе Pen.
    '''
    
    @pytest.mark.parametrize("pen_state_test", [
        1000,
        0,
        -1,
        1,
        -500,
        1.2,
        0.3,
        0.6,
        500.21,
        -0.3,
        -0.6,
        "number",
        True,
        False,
        None,
        ])
    def test_check_pen_state(self, pen_state_test):
    #проверка возвращения правильного значения ink_container_value
        def check_function(value):
            function = Pen(ink_container_value=value).check_pen_state()
            return function

        if isinstance(pen_state_test, int) and pen_state_test > 0:
            assert check_function(pen_state_test) == True, f"При указании переменной ink_container_value={pen_state_test} возникает ошибка. Возвращаемое значение функции: '{check_function(pen_state_test)}'. Значение ink_container_value = {Pen(ink_container_value=pen_state_test).ink_container_value}"
        if isinstance(pen_state_test, int) and pen_state_test <= 0:
            assert check_function(pen_state_test) == False, f"При указании переменной ink_container_value={pen_state_test} возникает ошибка. Возвращаемое значение функции: '{check_function(pen_state_test)}'. Значение ink_container_value = {Pen(ink_container_value=pen_state_test).ink_container_value}"
        if isinstance(pen_state_test, float) and pen_state_test > 0:
            assert check_function(pen_state_test) == True, f"При указании переменной ink_container_value={pen_state_test} возникает ошибка. Возвращаемое значение функции: '{check_function(pen_state_test)}'. Значение ink_container_value = {Pen(ink_container_value=pen_state_test).ink_container_value}"
        if isinstance(pen_state_test, float) and pen_state_test <= 0:
            assert check_function(pen_state_test) == False, f"При указании переменной ink_container_value={pen_state_test} возникает ошибка. Возвращаемое значение функции: '{check_function(pen_state_test)}'. Значение ink_container_value = {Pen(ink_container_value=pen_state_test).ink_container_value}"
        if isinstance(pen_state_test, bool) or pen_state_test == None or isinstance(pen_state_test, str):
            try:
                assert Pen(ink_container_value=pen_state_test) != Pen().ink_container_value(), f"При указании переменной ink_container_value={pen_state_test} возникает ошибка. Значение ink_container_value = {Pen(ink_container_value=pen_state_test).ink_container_value}"
                assert check_function(pen_state_test) == True, f"При указании переменной ink_container_value={pen_state_test} возникает ошибка. Возвращаемое значение функции: '{check_function(pen_state_test)}'. Значение ink_container_value = {Pen(ink_container_value=pen_state_test).ink_container_value}"
            except TypeError:
                pass
            except ValueError:
                pass
        

class TestCheckWrite:

    pytest.mark.parametrize
    def test_check_write(self):
        


