from ui import Ui_MainWindow as ui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from PyQt5.QtGui import QTextDocument
from PyQt5.QtCore import pyqtSignal
from threading import Thread
from datetime import datetime as dt
from time import sleep
from pyautogui import position
from glob import glob
from imageGrab import *
from sql import *


class rtxt_app(QMainWindow, ui):
    # создание сигнала для прогресс бара (для избежания ошибки из-за потоков)
    progressChanged = pyqtSignal(int)

    def __init__(self):
        # инициалиция основных переменных и подключение функций к кнопкам
        super().__init__()
        self.setupUi(self)
        self.flag = True
        self.ishotkey = False
        self.x1, self.y1, self.x2, self.y2 = (0, 0, 1920, 1080)
        self.images_folder = 'C:/'
        self.screnhot_path = 'screenhot.png'
        self.sql_path = ''
        self.tableWidget.setColumnCount(3)
        self.progressChanged.connect(self.progressBar.setValue)
        self.screenshot_butt.clicked.connect(self.read_screenhot)
        self.screenshorPath_butt.clicked.connect(self.path_f)
        self.xy1_butt.clicked.connect(self.xy1)
        self.xy2_butt.clicked.connect(self.xy2)
        self.hotkey_butt.clicked.connect(self.hotkey)
        self.save_butt.clicked.connect(self.save_txt)
        self.imagePath_butt.clicked.connect(self.path_images)
        self.analyze_butt.clicked.connect(self.analyze_images)
        self.csvsSave_butt.clicked.connect(self.csvSave_f)
        self.sqlSave_butt.clicked.connect(self.sqlSave_f)
        self.clean_sql.clicked.connect(self.clear_sql)

    def read_screenhot(self):
        # функция для чтения картинок
        self.statusbar.showMessage('')
        try:
            screenshot(filepath=self.screnhot_path, coordinates=(
                self.x1, self.y1, self.x2, self.y2))
            lang = self.language_comboBox.currentText()
            self.text_editor.setPlainText(
                processimage(self.screnhot_path, lang=lang))
            self.statusbar.showMessage('')
        except (SystemError, TypeError, ValueError) as er:  # отлавливание ошибок из-за координат
            if type(er) is SystemError or type(er) is ValueError:
                self.statusbar.showMessage(
                    'ОШИБКА: xy1 должен быть меньше чем xy2')
            else:
                self.statusbar.showMessage(
                    'ОШИБКА: попробуйте сделать скриншот снова')

    def deletetags(self, txt):
        # вспомогательная функция для удаления xml тегов в строке
        text_document = QTextDocument()
        text_document.setHtml(txt)
        text_without_tags = text_document.toPlainText()
        return text_without_tags

    def check_type(self, data):
        # функция для множественного анализа, определяет тип данных
        try:
            date = dt.strptime(data, '%Y-%m-%d')
            return 'date'
        except ValueError:
            pass
        try:
            x = int(data)
            return 'int'
        except ValueError:
            pass
        try:
            x = float(data)
            return 'float'
        except ValueError:
            pass
        return 'str'

    def get_tableData(self):
        # функция для получения данных из таблицы
        num_rows = self.tableWidget.rowCount()
        items = [(self.tableWidget.item(row, 1).text(),
                  self.tableWidget.item(row, 2).text())
                 for row in range(num_rows)]
        return items

    def xy1(self):
        # функция для запуска потока определения кординат
        self.xy1_butt.setEnabled(False)
        self.thread1 = Thread(
            target=lambda: self.xy_thread(1))  # создание потока
        self.thread1.daemon = True
        self.thread1.start()

    def xy2(self):
        self.xy2_butt.setEnabled(False)
        self.thread2 = Thread(target=lambda: self.xy_thread(2))
        self.thread2.daemon = True
        self.thread2.start()

    def xy_thread(self, arg):
        # поток определения координат
        x, y = 0, 0
        while self.flag:
            x, y = position()
            sleep(0.01)
        self.flag = True
        if arg == 1:
            self.xy1_label.setText(
                f'<html><head/><body><p align="center">x={x}, y={y}</p></body></html>')
            self.x1, self.y1 = x, y
            self.xy1_butt.setEnabled(True)
        else:
            self.xy2_label.setText(
                f'<html><head/><body><p align="center">x={x}, y={y}</p></body></html>')
            self.x2, self.y2 = x, y
            self.xy2_butt.setEnabled(True)

    def keyPressEvent(self, event):
        # функция для горячих клавиш
        try:
            if chr(event.key()) == self.deletetags(self.hotkey_butt.text()):
                self.flag = False

            if self.ishotkey:
                self.hotkey_butt.setText(chr(event.key()))
                self.hotkey_butt.setEnabled(True)
                self.ishotkey = False
                self.text_editor.setEnabled(True)
                self.statusbar.showMessage('')
        except ValueError:
            if self.ishotkey:
                self.statusbar.showMessage('ОШИБКА: неверная клавиша')

    def path_f(self):
        # функция для выбора пути сохранения скриншота
        fname = QFileDialog.getExistingDirectory(self, 'Выбрать папку', '.')
        if fname:
            self.screnhot_path = fname + '/screenhot.png'
            self.screenhotPath_label.setText(
                f'<html><head/><body><p align="center">{self.screnhot_path}</p></body></html>')

    def hotkey(self):
        # функция для создания новой горячей клавиши
        self.text_editor.setEnabled(False)
        self.hotkey_butt.setEnabled(False)
        self.hotkey_butt.setText('...')
        self.ishotkey = True

    def save_txt(self):
        # функция для выбора пути сохранения текстового файла
        fname = QFileDialog.getSaveFileName(
            self, 'сохранить тестовый файл', 'text.txt')
        if fname[0]:
            with open(fname[0], 'w', encoding='utf-8') as txt:
                txt.write(self.text_editor.toPlainText())
            self.statusbar.showMessage(
                'УСПЕХ: файл сохранён в папке с программой')

    def path_images(self):
        # функция для выбора пути к изображениям (для множественного анализа)
        folder_path = QFileDialog.getExistingDirectory(
            self, 'Выбрать папку', '.')
        if folder_path:
            self.images_folder = folder_path
            self.imagePath_label.setText(
                f'<html><head/><body><p align="center">{self.images_folder}</p></body></html>')

    def update_table(self, ditt):
        # функция для обновления данных в таблице
        row_count = sum([len(j) for i, j in ditt.items()])
        self.tableWidget.setRowCount(row_count)
        id = 1
        for type, sp in ditt.items():
            for data in sp:
                if data:
                    row = id - 1
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(str(id)))
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(type))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(data))
                    id += 1

    def analyze_images(self):
        # функция для запуска потока анализа изображений
        self.progressBar.setValue(0)
        self.analyze_butt.setEnabled(False)
        self.tableWidget.setEnabled(False)
        self.thread3 = Thread(target=self.analyze_thread)
        self.thread3.daemon = True
        self.thread3.start()

    def analyze_thread(self):
        # поток анализа изображений
        self.progressChanged.emit(0)
        dict_types = {
            'date': [],
            'int': [],
            'str': [],
            'float': []
        }
        lang = self.language_comboBox.currentText()
        images = glob(f'{self.images_folder}/*.png')
        for index, i in enumerate(images):
            self.statusbar.showMessage(i)
            # обработка изображения
            text = processimage(i, lang=lang).strip().split()
            for j in text:
                if j:
                    text_type = self.check_type(j)
                    dict_types[text_type].append(j)
            progress = (index + 1) / len(images) * 100  # расчёт единицы прогресса
            # вызов сигнала для избежания ошибки
            self.progressChanged.emit(int(progress))
        self.statusbar.showMessage(
            f'УСПЕХ: анализ завершён, обработано {len(images)} элементов')
        self.update_table(dict_types)
        self.analyze_butt.setEnabled(True)
        self.tableWidget.setEnabled(True)
        # обновление табличных данных

    def csvSave_f(self):
        # функция сохранения файла в формате csv
        fname = QFileDialog.getSaveFileName(
            self, 'сохранить csv файл', 'text.csv')
        if fname[0]:
            csv_writer(self.get_tableData(), fname[0])

    def sqlSave_f(self):
        # функция сохранения файла в sql БД
        if not self.sql_path:
            self.sql_path, t = QFileDialog.getOpenFileName(self, 'Выберите файл SQLite', '',
                                                        'SQLite Databases (*.sqlite);;All Files (*)')
        if self.sql_path:
            try:
                sql_writer(self.get_tableData(), database=self.sql_path)
                self.statusbar.showMessage('УСПЕХ: данные в БД обновлены')
            except:
                self.statusbar.showMessage('ОШИБКА: проверьте состояние БД')

    def clear_sql(self):
        # функция удаления всех записей из sql БД
        if not self.sql_path:
            self.sql_path, t = QFileDialog.getOpenFileName(self, 'Выберите файл SQLite', '',
                                                        'SQLite Databases (*.sqlite);;All Files (*)')
        if self.sql_path:
            confirm_dialog = QMessageBox()
            confirm_dialog.setIcon(QMessageBox.Question)
            confirm_dialog.setWindowTitle("Подтверждение")
            confirm_dialog.setText("Вы уверены, что хотите удалить все данные БД?")
            confirm_dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            result = confirm_dialog.exec_()
            if result == QMessageBox.Ok:
                try:
                    clear_database(database=self.sql_path)
                    self.statusbar.showMessage('УСПЕХ: данные в БД обновлены')
                except:
                    self.statusbar.showMessage('ОШИБКА: проверьте состояние БД')
