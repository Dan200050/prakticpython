from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QPushButton, QMessageBox

__all__ = ['CheckBoxes']


class CheckBoxes(QWidget):
    def __init__(self):
        super().__init__()

        # Создаем чекбоксики
        self.first_checkbox = QCheckBox('Я ГУЛЬ')
        self.second_checkbox = QCheckBox('ZXC')
        self.third_checkbox = QCheckBox('Котик <3')

        # И кнопку
        button = QPushButton('АААА Я КНОПКА')
        button.clicked.connect(self.check)

        widgets = [self.first_checkbox, self.second_checkbox, self.third_checkbox, button]

        layout = QVBoxLayout(self)

        for widget in widgets:
            layout.addWidget(widget)

    def check(self):
        checkboxes = [self.first_checkbox, self.second_checkbox, self.third_checkbox]
        result = []

        # Проходимся по все чекбоксам, и если он с галочкой, то записываем его названия в массив result
        for checkbox in checkboxes:
            if checkbox.checkState() == Qt.CheckState.Checked:
                result.append(checkbox.text())

        # Если были выбраны чекбоксы, то соединяем их названия и выводим
        text = f"Вы выбрали: {', '.join(result)}" if result else "Быдло ниче не выбрало"

        self.show_message(text)

    @staticmethod
    def show_message(message):
        dialog = QMessageBox()

        # Заголовок нового окна
        dialog.setWindowTitle("Иду по тропинке в голове ля-ля-ля")

        # Заполняем сообщением
        dialog.setText(message)

        # Показываем
        dialog.exec()




