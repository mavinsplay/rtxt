from core import *
from sys import exit, argv


if __name__ == '__main__':
    # инициализация приложения
    ui = QApplication(argv)
    ex = rtxt_app()
    ex.show()
    exit(ui.exec_())