from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QComboBox, QLabel

__all__ = ['Calculator']


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем виджеты с полем для ввода чисел и делаем так,
        # чтобы при любом изменении числа вызывалась функция calculate
        self.first_number = InputNumber()
        self.first_number.textChanged.connect(self.calculate)

        self.second_number = InputNumber()
        self.second_number.textChanged.connect(self.calculate)

        # Создаем виджет для выбора арифметического знака
        self.operator = ArithmeticOperator()
        self.operator.currentTextChanged.connect(self.calculate)

        # Создаем виджет для выбора результата
        self.result = Result()

        # Список всех виджетов на странице
        widgets = [self.first_number, self.operator, self.second_number, QLabel('='), self.result]

        # Создаем макет, на котором виджеты располагаются горизонтально
        layout = QHBoxLayout(self)

        # Заполняем макет нашими виджетами
        for widget in widgets:
            layout.addWidget(widget)

        # Отображаем макет
        self.setLayout(layout)

    def calculate(self):
        # Значение текущего арифметического знака
        current_operator = self.operator.currentText()

        # Значения чисел
        first = self.first_number.text()
        second = self.second_number.text()

        # Если хотя бы одного числа нет то ниче не делаем
        if not first or not second:
            return

        # Соотносим текущий знак и соответствующую ему функцию, которую нам надо применить
        func = None
        if current_operator == '+':
            func = self.add
        elif current_operator == '-':
            func = self.sub
        elif current_operator == '*':
            func = self.mul
        elif current_operator == '/':
            func = self.div

        # Применяем полученную функцию и записываем результат
        self.result.setText(str(func(int(first), int(second))))

    @staticmethod
    def add(first, second):
        return first + second

    @staticmethod
    def sub(first, second):
        return first - second

    @staticmethod
    def mul(first, second):
        return first * second

    @staticmethod
    def div(first, second):
        return first / second


class InputNumber(QLineEdit):
    def __init__(self):
        super().__init__()

        # Добавляем валидатор, чтобы в текстовое поле можно было вводить только цифры
        validator = QIntValidator()
        self.setValidator(validator)


class ArithmeticOperator(QComboBox):

    # Список арифметических операторов
    ARITHMETIC_OPERATORS = ['+', '-', '*', '/']

    def __init__(self):
        super().__init__()

        # Заполняем всплывающее меню нашими операторами
        self.addItems(self.ARITHMETIC_OPERATORS)


class Result(QLineEdit):
    def __init__(self):
        super().__init__()

        # Делаем так, чтобы поле нельзя было редактировать и оно не выделялось
        self.setReadOnly(True)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
