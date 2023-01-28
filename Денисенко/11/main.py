import json

import requests
from PyQt6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QPushButton, QWidget, QMessageBox


class MainWindow(QWidget):
    GITHUB_API = 'https://api.github.com/users/'
    REQUIRED_FIELDS = ['company', 'created_at', 'email', 'id', 'name', 'url']

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Москва метро Люблино. Работаем')

        self.user = QLineEdit()
        button = QPushButton('НАЖМИ МЕНЯ')
        button.clicked.connect(self.find_user)

        widgets = [self.user, button]

        layout = QVBoxLayout(self)

        for widget in widgets:
            layout.addWidget(widget)

    def find_user(self):
        user = self.user.text()

        try:
            response = requests.get(f'{self.GITHUB_API}{user}')
        except requests.exceptions.RequestException as e:
            print(e)
            self.show_message('Какие-то беды :)')
            return

        if response.status_code != 200:
            self.show_message('Не нашлось такого фраера или беды на серваке')
            return

        data = response.json()
        required_data = {field: data.get(field) for field in self.REQUIRED_FIELDS}

        with open("data_file.json", "w") as write_file:
            json.dump(required_data, write_file)

        self.show_message("Проверяй результат!")



    @staticmethod
    def show_message(message):
        dialog = QMessageBox()
        dialog.setWindowTitle("АУФ")
        dialog.setText(message)
        dialog.exec()


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
