import sys
import random

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
    QLabel, QDesktopWidget, QVBoxLayout, QHBoxLayout


class Evaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadNextExample()

    def initUI(self):
        # Открывает окно на весь экран
        screen_geometry = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen_geometry.width(),
                         screen_geometry.height())

        # Добавляем фон
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        pixmap = QPixmap('foto/mat.jpg')
        self.background_label.setPixmap(pixmap.scaled(self.width(),
                                                      self.height()))

        # фото замка
        self.pixmap = QPixmap('foto/key.png')
        self.image = QLabel(self)
        self.image.setGeometry(200, 80, 400, 700)
        resized_pixmap = self.pixmap.scaled(500, 800)
        self.image.setPixmap(resized_pixmap)

        # создаём виджеты
        self.example = QLineEdit(self)
        self.example.setGeometry(self.width() - 450, self.height() - 300, 400,
                                 120)
        self.example.setAlignment(Qt.AlignCenter)
        self.example.setEnabled(False)
        self.example.setStyleSheet("color: black;")
        self.example.setFont(QFont("Arial", 32))

        self.otvet = QLineEdit(self)
        self.otvet.setGeometry(self.width() - 450, self.height() - 140, 400,
                               120)
        self.otvet.setText("")
        self.otvet.setStyleSheet("color: black;")
        self.otvet.setFont(QFont("Arial", 32))

        self.counter = QLineEdit(self)
        self.counter.setText("Счёт ошибок: 0")
        self.counter.setGeometry(self.width() - 350, 30, 300, 50)
        self.counter.setStyleSheet("color: rgb(0, 0, 0);")
        self.counter.setFont(QFont("Arial", 20))
        self.counter.setEnabled(False)

        self.proverka = QPushButton('Проверить', self)
        self.proverka.setGeometry(self.width() - 680, self.height() - 220, 200,
                                  80)
        self.proverka.setStyleSheet("color: black;")
        self.proverka.setFont(QFont("Arial", 20))

        self.res_fields = []

        # Создание горизонтальной группы
        res_layout = QHBoxLayout()

        for i in range(6):
            res_field = QLineEdit("", self)
            res_field.setFixedSize(80, 80)
            res_field.setEnabled(False)
            res_field.setStyleSheet("color: rgb(0, 0, 0);")
            res_field.setFont(QFont("Arial", 32))
            res_field.setAlignment(Qt.AlignCenter)
            self.res_fields.append(res_field)

            # Добавление поля в группу
            res_layout.addWidget(res_field)

        widget = QWidget(self)
        widget.setLayout(res_layout)

        self.proverka.clicked.connect(self.checkAnswer)

        self.ex = QPushButton('Вернуться на главный экран', self)
        self.ex.setGeometry(10, self.height() - 90, 400,
                            80)
        self.ex.setStyleSheet("color: black;")
        self.ex.setFont(QFont("Arial", 20))
        self.ex.clicked.connect(self.exi)

    # загрузка нового математического задания
    def loadNextExample(self):
        operations_1 = ["*", "/"]
        operations_2 = ["+", "-"]

        operand_1 = random.randint(0, 9)
        operation_1 = random.choice(operations_1)
        operand_2 = random.randint(0, 9)

        if operation_1 == "*":
            result = operand_1 * operand_2
        else:
            if operand_2 == 0:
                operand_2 = 1
            result = operand_1 // operand_2

        operation_2 = random.choice(operations_2)
        operand_3 = random.randint(0, 9)

        if operation_2 == "+":
            result += operand_3
        else:
            result -= operand_3

        self.current_example = (f"{operand_1} {operation_1} {operand_2} "
                                f"{operation_2} {operand_3} =")
        self.current_reward = str(result)

        self.example.setText(self.current_example)

    # проверка ответа пользователя на текущее задание
    def checkAnswer(self):
        user_response = self.otvet.text()

        if user_response == self.current_reward:
            self.updateResult(user_response)
        else:
            self.counter.setText(
                "Счёт ошибок: " + str(
                    int(self.counter.text().split(": ")[1]) + 1))

        self.loadNextExample()
        self.otvet.clear()

    # обновление результата ответа пользователя
    def updateResult(self, result):
        empty_res_fields = [res_field for res_field in self.res_fields if
                            res_field.text() == ""]

        if empty_res_fields:
            empty_res_fields[0].setText(result)

            if len(empty_res_fields) == 1:  # Если все ответы заполнены
                self.openNewWindow()
                self.close()

    # Окрытие окна после открытия замка
    def openNewWindow(self):
        self.new_window = NEW_sait()
        self.new_window.setErrorsCount(int(
            self.counter.text().split(": ")[1]))  # передача количества ошибок
        self.new_window.showFullScreen()
        self.close()

    # выход на главный экран
    def exi(self):
        from main import ONE
        self.parent = ONE()
        self.parent.showFullScreen()
        self.close()


class NEW_sait(QWidget):
    def __init__(self):
        super().__init__()

        # Открывает окно на весь экран
        screen_geometry = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen_geometry.width(),
                         screen_geometry.height())

        # Добавляем фон
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        pixmap = QPixmap('foto/mat.jpg')
        self.background_label.setPixmap(pixmap.scaled(self.width(),
                                                      self.height()))

        self.error_label = QLabel("", self)
        self.error_label.setStyleSheet("color: black;")
        self.error_label.setFont(QFont("Arial", 20))

        # Создаем вертикальную раскладку
        vlayout = QVBoxLayout()

        self.error_label.setAlignment(Qt.AlignCenter)
        vlayout.addWidget(self.error_label)

        button2 = QPushButton("Попробовать снова")
        button2.setFixedSize(250, 100)
        button2.setStyleSheet(
            "background-color: rgb(255, 204, 153); color: rgb(0, 0, 0);")
        button2.setFont(QFont("Arial", 18))
        vlayout.addWidget(button2)

        button1 = QPushButton("Вернуться на главный экран")
        button1.setFixedSize(350, 100)
        button1.setStyleSheet(
            "background-color: rgb(255, 204, 153); color: rgb(0, 0, 0);")
        button1.setFont(QFont("Arial", 18))
        vlayout.addWidget(button1)

        # Выравниваем кнопки по центру
        vlayout.setAlignment(Qt.AlignCenter)

        # Устанавливаем созданную вертикальную раскладку в основной макет
        self.setLayout(vlayout)

        button2.clicked.connect(self.retryClicked)
        button1.clicked.connect(self.heger)

    def setErrorsCount(self, count):
        self.error_label.setText("Ваше количество ошибок: " + str(count))
        with open('res_txt/errors_math.txt', 'a') as file:
            file.write(str(count) + '\n')

    def retryClicked(self):
        self.evaluator_window = Evaluator()
        self.evaluator_window.showFullScreen()
        self.close()

    def heger(self):
        from main import ONE
        self.evaluator_window = ONE()
        self.evaluator_window.showFullScreen()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Evaluator()
    ex.showFullScreen()
    sys.exit(app.exec_())
