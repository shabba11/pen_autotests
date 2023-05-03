# Проверки класса Pen

#### Для запуска тестов:

##### 1. Активируем окружение: 'python -m venv venv
##### 2. Устанавливаем пакеты: 'python -m install -r requirements.txt'
##### 3. Запускаем тесты: 'python -m pytest'

#### P.S. Тесты делались исходя из названий функций и переменных. Но для тестирования не хватает документации ("Что должен делать класс и функции в ней?", "Какие должны быть входные и выходные данные"). Исходя из этого внизу составлен TO DO.

#### TO DO:

##### 1.Раздобыть "Требования":
###### 1.1 Какие значения должен принимать класс: ink_container_value, color, size_letter
###### 1.2 Какие значения должна принимать функция write в переменной word. Какие выходные данные должны быть у этой функции. Что должна делать эта функция.
###### 1.3 Какие выходные данные должны быть у функции get_color. Что должна делать эта функция.
###### 1.4 Какие выходные данные у функции check_pen_state. Что должна делать эта функция.
###### 1.5 Какие выходные данные у функции do_comething_else. Что должна делать эта функция.
##### 2.Исправить тесты под действительные требования.

#### Возможно правильно написанный код находится [здесь](https://github.com/shabba11/pen_autotests/blob/main/Pen_correct.py "Я правильно написанный код")

#### DONE:

#### GITHUB:
##### 1.Удалил .vscode, __pycache__ и venv
##### 2.Исправил requirements.txt

#### CODE:
##### 1.К сожалению  в VSCode не отображалась подсказка. Запустил в PyCharm и исправил ошибку E712
##### 2.Ограничение на длинну строки исправил сделав отдельный файл с функцией и уменьшив количество ненужного текста.
##### 3.Текст ошибок исправлен
##### 4.Исправил if на elif там где это нужно.
##### 5.test_get_color:
##### a.Не стал разбивать код на 2 автотеста, так как появилось предусловие исходя из комментария в пункте 'c'. При передаваемом значении разного типа в переменную color, возвращается '<значение>'. Исходя из этого откорректировал Pen_correct.py
##### b.Вынес создание Pen в начало
##### c.В ответ на вопрос: "Почему color_test=False должен возвращать "blue"?" - Так как не было документации в которой было бы указано что принимаются любые значения переменной(а логика была в том что при переменной не равной типу str - возвращается стандартное значение "blue"). Соответственно код исправил исходя из комментария этого пункта с новыми данными. 
##### d.Исправил. Этой части кода теперь нет.
##### 6. TestCheckPenState:
##### a.Сделал два автотеста. Избавился от isinstance
##### b.Согласен. Функция бесполезна. Удалил
##### c.Ответ в пункте b.
##### d.Исправил и прописал переменную в каждом тесте.
##### e.Добавил комментарий и логику своих действий.