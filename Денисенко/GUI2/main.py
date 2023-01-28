from PyQt6.QtWidgets import QApplication, QTabWidget
from Modules import Calculator, CheckBoxes, Text


class MainWindow(QTabWidget):
    def __init__(self):
        super().__init__()

        # Создаем виджеты наших вкладок
        calculator_widget = Calculator()
        choice_widget = CheckBoxes()
        text_widget = Text()

        # Меняем заголовок окна
        self.setWindowTitle("Мусин Даниил Евгеньевич")

        # Добавляем наши виджеты по вкладкам в наше окно
        self.addTab(calculator_widget, "Кулькулятор")
        self.addTab(choice_widget, "Выбор без выбора")
        self.addTab(text_widget, "Какая-то фигня")


# Стартуем приложуху
app = QApplication([])

# Создаем и показываем главное окно
window = MainWindow()
window.show()

# Запускаем цикл событий.
app.exec()



