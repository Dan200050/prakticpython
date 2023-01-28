from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog


class Text(QWidget):
    def __init__(self):
        super().__init__()

        button = QPushButton('ВыБрАтЬ фАйЛ')
        button.clicked.connect(self.open_file)

        # Поле для текста
        self.label = QLabel()

        widgets = [button, self.label]

        # Создаем макет, на котором виджеты располагаются вертикально
        layout = QVBoxLayout(self)

        for widget in widgets:
            layout.addWidget(widget)

    def open_file(self):
        dialog = QFileDialog()

        # Делаем так, чтобы можно было выбрать только файлы txt
        dialog.setNameFilter("*.txt (*.txt)")

        # Запускаем новое окно
        if dialog.exec():

            # Названия выбранных файлов
            filenames = dialog.selectedFiles()

            # Берем первый файл, открываем и читаем
            with open(filenames[0], 'r') as file:
                text = file.read()

            # Записываем его содержимое в наше поле для текста
            self.label.setText(text)
