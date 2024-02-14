import pygame
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QLabel, QApplication, \
    QPushButton, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt5.QtGui import QPixmap, QFont

from satisticks import static1, static2, static3, static4


class ONE(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Главное говно')

        # Открывает окно на весь экран
        screen_geometry = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen_geometry.width(),
                         screen_geometry.height())

        # Добавляем фон
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        pixmap = QPixmap('foto/fon.png')
        self.background_label.setPixmap(pixmap.scaled(self.width(),
                                                      self.height()))

        # Создаем layout для объединения кнопок по горизонтали
        horizontal_layout1 = QHBoxLayout()

        mat_but = QPushButton('Математика', self)
        mat_but.setFixedSize(425, 250)
        mat_but.setStyleSheet(
            "background-color: rgb(255, 204, 153); color: rgb(0, 0, 0);")
        mat_but.setFont(QFont("Arial", 32))
        mat_but.clicked.connect(self.clicked2)
        horizontal_layout1.addWidget(mat_but)

        cl_but = QPushButton('Кликер', self)
        cl_but.setFixedSize(425, 250)
        cl_but.setStyleSheet(
            "background-color: rgb(230, 230, 250); color: rgb(0, 0, 0);")
        cl_but.setFont(QFont("Arial", 32))
        cl_but.clicked.connect(self.clicked)
        horizontal_layout1.addWidget(cl_but)

        # Создаем layout для объединения оставшихся кнопок по горизонтали
        horizontal_layout2 = QHBoxLayout()

        Hone_but = QPushButton('Соты', self)
        Hone_but.setFixedSize(425, 250)
        Hone_but.setStyleSheet(
            "background-color: rgb(212, 162, 153); color: rgb(0, 0, 0);")
        Hone_but.setFont(QFont("Arial", 32))
        horizontal_layout2.addWidget(Hone_but)
        Hone_but.clicked.connect(self.clicked4)

        Sub_but = QPushButton('Последовательность', self)
        Sub_but.setFixedSize(425, 250)
        Sub_but.setStyleSheet(
            "background-color: rgb(175, 238, 238); color: rgb(0, 0, 0);")
        Sub_but.setFont(QFont("Arial", 32))
        Sub_but.clicked.connect(self.cliked3)
        horizontal_layout2.addWidget(Sub_but)

        combobox = QComboBox(self)
        combobox.setFixedSize(self.width() - 25, 100)
        combobox.setStyleSheet(
            "background-color: rgb(125, 100, 45); color: rgb(0, 0, 0);")
        combobox.setFont(QFont("Arial", 20))
        combobox.addItem("Статистика Математики")
        combobox.addItem("Статистика Кликера")
        combobox.addItem("Статистика Сот")
        combobox.addItem("Статистика Последовательности")
        combobox.currentIndexChanged.connect(self.combobox_changed)

        # Создаем layout для объединения двух предыдущих layout'ов вертикально
        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(horizontal_layout1)
        vertical_layout.addLayout(horizontal_layout2)
        vertical_layout.addWidget(combobox)

        # Устанавливаем layout для QWidget
        self.setLayout(vertical_layout)

        self.exites = QPushButton("Выйти", self)
        self.exites.setGeometry(10, 20, 150, 50)
        self.exites.setStyleSheet(
            "background-color: rgb(255, 108, 47); color: rgb(0, 0, 0);")
        self.exites.setFont(QFont("Arial", 20))
        self.exites.clicked.connect(self.exet)

    # переход в файл с сотами
    def clicked4(self):
        self.close()
        from Honeycombs import Honeycomb
        sota = Honeycomb()
        sota.Run()

    # выход из программы
    def exet(self):
        pygame.quit()
        self.close()

    # переход в файл с последовательность
    def cliked3(self):
        self.close()
        from Colorposled import VisualMemoryTest
        my_game = VisualMemoryTest()
        my_game.run()

    # Переход в файл Klicker
    def clicked(self):
        self.close()
        from Klicker import ReactionTimeTest
        reaction_time_test = ReactionTimeTest()
        reaction_time_test.run()

    # Переход в файл mateha
    def clicked2(self):
        from mateha import Evaluator
        self.cal = Evaluator()
        self.cal.showFullScreen()
        self.close()

    # Обработчик события выбранного элемента в combobox
    def combobox_changed(self, index):
        if index == 0:
            self.cal1 = static1()
            self.cal1.show()
        elif index == 1:
            self.cal2 = static2()
            self.cal2.show()
        elif index == 2:
            self.cal3 = static3()
            self.cal3.show()
        elif index == 3:
            self.cal4 = static4()
            self.cal4.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = ONE()
    window.showFullScreen()
    sys.exit(app.exec())
