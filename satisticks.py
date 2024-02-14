from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel


class static1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 100, 300, 400)
        self.setWindowTitle('Рейтинг по математике')
        self.setFixedSize(self.size())

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        pixmap = QPixmap('foto/statik.jpg')
        self.background_label.setPixmap(pixmap.scaled(self.width(),
                                                      self.height()))

        numbers = []
        with open("res_txt/errors_math.txt", "r") as file:
            for line in file:
                numbers.append(int(line.strip()))

        numbers = sorted(set(numbers))

        vbox = QVBoxLayout()
        for i in range(min(len(numbers), 10)):
            label = QLabel(f"{i+1} место: {numbers[i]}")
            label.setAlignment(Qt.AlignCenter)
            vbox.addWidget(label)
            font = label.font()
            font.setPointSize(20)
            font.setFamily("Times New Roman")
            label.setFont(font)
            label.setStyleSheet("color: black;")

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)


class static2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 100, 300, 400)
        self.setWindowTitle('Рейтинг в кликере')
        self.setFixedSize(self.size())

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        pixmap = QPixmap('foto/statik.jpg')
        self.background_label.setPixmap(pixmap.scaled(self.width(),
                                                      self.height()))

        numbers = []
        with open("res_txt/Klicker_res.txt", "r") as file:
            for line in file:
                numbers.append(int(line.strip()))

        numbers = sorted(set(numbers))

        vbox = QVBoxLayout()
        for i in range(min(len(numbers), 10)):
            label = QLabel(f"{i + 1} место: {numbers[i]}")
            label.setAlignment(Qt.AlignCenter)
            vbox.addWidget(label)
            font = label.font()
            font.setPointSize(20)
            font.setFamily("Times New Roman")
            label.setFont(font)
            label.setStyleSheet("color: black;")

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)


class static3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 100, 300, 400)
        self.setWindowTitle('Рейтинг в последовательности')
        self.setFixedSize(self.size())

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        pixmap = QPixmap('foto/statik.jpg')
        self.background_label.setPixmap(
            pixmap.scaled(self.width(), self.height()))

        numbers = set()
        with open("res_txt/sota_res.txt", "r") as file:
            for line in file:
                numbers.add(int(line.strip()))

        numbers = sorted(numbers, reverse=True)[:10]

        vbox = QVBoxLayout()
        for i in range(len(numbers)):
            label = QLabel(f"{i + 1} место: {numbers[i]}")
            label.setAlignment(Qt.AlignCenter)
            vbox.addWidget(label)
            font = label.font()
            font.setPointSize(20)
            font.setFamily("Times New Roman")
            label.setFont(font)
            label.setStyleSheet("color: black;")

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)


class static4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 100, 300, 400)
        self.setWindowTitle('Рейтинг в последовательности')
        self.setFixedSize(self.size())

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        pixmap = QPixmap('foto/statik.jpg')
        self.background_label.setPixmap(
            pixmap.scaled(self.width(), self.height()))

        numbers = set()
        with open("res_txt/score.txt", "r") as file:
            for line in file:
                numbers.add(int(line.strip()))

        numbers = sorted(numbers, reverse=True)[:10]

        vbox = QVBoxLayout()
        for i in range(len(numbers)):
            label = QLabel(f"{i + 1} место: {numbers[i]}")
            label.setAlignment(Qt.AlignCenter)
            vbox.addWidget(label)
            font = label.font()
            font.setPointSize(20)
            font.setFamily("Times New Roman")
            label.setFont(font)
            label.setStyleSheet("color: black;")

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)
