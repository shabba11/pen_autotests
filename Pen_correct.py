class Pen(object):
    # меняем функцию чтобы проще было записать стандартные переменные
    def __init__(self, ink_container_value=1000, size_letter=1.0, color='blue'):
        # the amount of ink
        self.ink_container_value = int(ink_container_value)
        # size of the letter (font)
        self.size_letter = float(size_letter)
        # ink color
        self.color = str(color)

    def write(self, word):
        if not self.check_pen_state():
            return ''
        size_of_word = len(word) * self.size_letter
        if size_of_word <= self.ink_container_value:
            self.ink_container_value -= size_of_word
            return word
        else:    # не хватает else
            part_of_word = word[0: int(
                self.ink_container_value // self.size_letter)]  # не хватает количество букв исходя из размера слова
            self.ink_container_value = 0
            return part_of_word

    def get_color(self):
        # при вызове функции по логике должен возвращаться цвет записанный в класс
        return self.color

    def check_pen_state(self):
        return self.ink_container_value > 0

    def do_something_else(self):
        return "blue"  # поменял выводимое значение с get_color. Есть ощущения что вывод перепутали с этой функцией
