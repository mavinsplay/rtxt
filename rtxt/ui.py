from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QLabel, QPushButton, QFrame, QPlainTextEdit, QComboBox
from PyQt5.QtWidgets import QStatusBar, QGridLayout, QSizePolicy, QProgressBar
from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject, QSize
from PyQt5.QtGui import QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 560)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setGeometry(QRect(0, 0, 941, 541))
        self.screenhot_tab = QWidget()
        self.screenhot_tab.setObjectName(u"screenhot_tab")
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.screenhot_tab.setFont(font)
        self.gridLayoutWidget = QWidget(self.screenhot_tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 371, 501))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.gridLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 1, 1, 3)

        self.hotkey_label = QLabel(self.gridLayoutWidget)
        self.hotkey_label.setObjectName(u"hotkey_label")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hotkey_label.sizePolicy().hasHeightForWidth())
        self.hotkey_label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.hotkey_label, 7, 1, 1, 1)

        self.line_3 = QFrame(self.gridLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 4, 2, 1, 1)

        self.line_4 = QFrame(self.gridLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 3, 1, 1, 3)

        self.label_coordinatedeterm = QLabel(self.gridLayoutWidget)
        self.label_coordinatedeterm.setObjectName(u"label_coordinatedeterm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.label_coordinatedeterm.sizePolicy().hasHeightForWidth())
        self.label_coordinatedeterm.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_coordinatedeterm, 2, 1, 1, 3)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 1, 1, 3)

        self.xy1_label = QLabel(self.gridLayoutWidget)
        self.xy1_label.setObjectName(u"xy1_label")

        self.gridLayout.addWidget(self.xy1_label, 4, 1, 1, 1)

        self.screenshot_butt = QPushButton(self.gridLayoutWidget)
        self.screenshot_butt.setObjectName(u"screenshot_butt")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.screenshot_butt.sizePolicy().hasHeightForWidth())
        self.screenshot_butt.setSizePolicy(sizePolicy3)
        self.screenshot_butt.setSizeIncrement(QSize(0, 0))

        self.gridLayout.addWidget(self.screenshot_butt, 0, 1, 1, 3)

        self.xy1_butt = QPushButton(self.gridLayoutWidget)
        self.xy1_butt.setObjectName(u"xy1_butt")

        self.gridLayout.addWidget(self.xy1_butt, 6, 1, 1, 1)

        self.screenshorPath_butt = QPushButton(self.gridLayoutWidget)
        self.screenshorPath_butt.setObjectName(u"screenshorPath_butt")

        self.gridLayout.addWidget(self.screenshorPath_butt, 8, 1, 1, 3)

        self.xy2_label = QLabel(self.gridLayoutWidget)
        self.xy2_label.setObjectName(u"xy2_label")

        self.gridLayout.addWidget(self.xy2_label, 4, 3, 1, 1)

        self.xy2_butt = QPushButton(self.gridLayoutWidget)
        self.xy2_butt.setObjectName(u"xy2_butt")

        self.gridLayout.addWidget(self.xy2_butt, 6, 3, 1, 1)

        self.hotkey_butt = QPushButton(self.gridLayoutWidget)
        self.hotkey_butt.setObjectName(u"hotkey_butt")

        self.gridLayout.addWidget(self.hotkey_butt, 7, 3, 1, 1)

        self.screenhotPath_label = QLabel(self.gridLayoutWidget)
        self.screenhotPath_label.setObjectName(u"screenhotPath_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.screenhotPath_label.sizePolicy().hasHeightForWidth())
        self.screenhotPath_label.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.screenhotPath_label, 9, 1, 1, 3)

        self.verticalLayoutWidget = QWidget(self.screenhot_tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(380, 0, 551, 501))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.text_editor = QPlainTextEdit(self.verticalLayoutWidget)
        self.text_editor.setObjectName(u"text_editor")

        self.verticalLayout.addWidget(self.text_editor)

        self.save_butt = QPushButton(self.verticalLayoutWidget)
        self.save_butt.setObjectName(u"save_butt")

        self.verticalLayout.addWidget(self.save_butt)

        self.line_5 = QFrame(self.screenhot_tab)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(370, -20, 20, 541))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.tab_widget.addTab(self.screenhot_tab, "")
        self.multiple_reading = QWidget()
        self.multiple_reading.setObjectName(u"multiple_reading")
        self.gridLayoutWidget_2 = QWidget(self.multiple_reading)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(460, 0, 471, 501))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.csvsSave_butt = QPushButton(self.gridLayoutWidget_2)
        self.csvsSave_butt.setObjectName(u"csvsSave_butt")

        self.gridLayout_2.addWidget(self.csvsSave_butt, 1, 0, 1, 1)

        self.sqlSave_butt = QPushButton(self.gridLayoutWidget_2)
        self.sqlSave_butt.setObjectName(u"sqlSave_butt")

        self.gridLayout_2.addWidget(self.sqlSave_butt, 1, 1, 1, 1)

        self.tableWidget = QTableWidget(self.gridLayoutWidget_2)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 2)

        self.gridLayoutWidget_3 = QWidget(self.multiple_reading)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 0, 431, 501))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.imagePath_butt = QPushButton(self.gridLayoutWidget_3)
        self.imagePath_butt.setObjectName(u"imagePath_butt")

        self.gridLayout_3.addWidget(self.imagePath_butt, 3, 0, 1, 2)

        self.progressBar = QProgressBar(self.gridLayoutWidget_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_3.addWidget(self.progressBar, 6, 0, 1, 2)

        self.process_label = QLabel(self.gridLayoutWidget_3)
        self.process_label.setObjectName(u"process_label")
        sizePolicy4.setHeightForWidth(
            self.process_label.sizePolicy().hasHeightForWidth())
        self.process_label.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.process_label, 5, 0, 1, 2)

        self.language_comboBox = QComboBox(self.gridLayoutWidget_3)
        self.language_comboBox.addItem("eng")
        self.language_comboBox.addItem("rus")
        self.language_comboBox.setObjectName(u"language_comboBox")

        self.gridLayout_3.addWidget(self.language_comboBox, 1, 1, 1, 1)

        self.imagePath_label = QLabel(self.gridLayoutWidget_3)
        self.imagePath_label.setObjectName(u"imagePath_label")
        sizePolicy2.setHeightForWidth(
            self.imagePath_label.sizePolicy().hasHeightForWidth())
        self.imagePath_label.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.imagePath_label, 4, 0, 1, 2)

        self.language_label = QLabel(self.gridLayoutWidget_3)
        self.language_label.setObjectName(u"language_label")

        self.gridLayout_3.addWidget(self.language_label, 1, 0, 1, 1)

        self.clean_sql = QPushButton(self.gridLayoutWidget_3)
        self.clean_sql.setObjectName(u"clean_sql")

        self.gridLayout_3.addWidget(self.clean_sql, 7, 0, 1, 2)

        self.analyze_butt = QPushButton(self.gridLayoutWidget_3)
        self.analyze_butt.setObjectName(u"analyze_butt")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.analyze_butt.sizePolicy().hasHeightForWidth())
        self.analyze_butt.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.analyze_butt, 0, 0, 1, 2)

        self.line_6 = QFrame(self.multiple_reading)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(440, -50, 21, 631))
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.tab_widget.addTab(self.multiple_reading, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tab_widget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # настройка пользовательского интерфейса

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"RTXT\t v 1.0", None))
        self.hotkey_butt.setText(
            QCoreApplication.translate("MainWindow", u"Q", None))
        self.label_coordinatedeterm.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\">\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0438" +
            u"\u0442\u044c \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b</p></body></html>", None))
        self.xy1_label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\">x=0, y=0</p></body></html>", None))
        self.xy2_label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\">x=1920, y=1080</p></body></html>", None))
        self.screenshot_butt.setText(QCoreApplication.translate(
            "MainWindow", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u0442\u044c \u043e\u0431\u043b\u0430\u0441" +
            u"\u0442\u044c \u044d\u043a\u0440\u0430\u043d\u0430", None))
        self.xy2_butt.setText(QCoreApplication.translate(
            "MainWindow", u"xy 2", None))
        self.hotkey_label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\">\u0433\u043e\u0440\u044f\u0447\u0430" +
            u"\u044f \u043a\u043b\u0430\u0432\u0438\u0448\u0430</p><p align=\"center\">\u043e\u043f\u0440. \u043a" +
            u"\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442:</p><p align=\"center\"><br/></p></body></html>", None))
        self.xy1_butt.setText(QCoreApplication.translate(
            "MainWindow", u"xy 1", None))
        self.save_butt.setText(QCoreApplication.translate(
            "MainWindow", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a \u0442\u0435" +
            u"\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.screenhot_tab), QCoreApplication.translate(
            "MainWindow", u"\u0442\u0435\u043a\u0441\u0442 \u043d\u0430 \u044d\u043a\u0440\u0430\u043d\u0435", None))
        self.csvsSave_butt.setText(QCoreApplication.translate(
            "MainWindow", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 csv", None))
        self.sqlSave_butt.setText(QCoreApplication.translate(
            "MainWindow", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 sql", None))
        self.imagePath_butt.setText(QCoreApplication.translate(
            "MainWindow", u"\u0432\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0443\u0442\u044c \u043a \u0438\u0437" +
            u"\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c", None))
        self.process_label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">\u043f\u0440" +
            u"\u043e\u0446\u0435\u0441\u0441 \u0447\u0442\u0435\u043d\u0438\u044f</span></p></body></html>", None))
        self.imagePath_label.setText(QCoreApplication.translate(
            "MainWindow",
            u"<html><head/><body><p align=\"center\">C:\</p></body></html>",
            None))
        self.language_label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">\u0432" +
            u"\u044b\u0431\u0440\u0430\u0442\u044c \u044f\u0437\u044b\u043a \u043f\u0440\u043e\u0432\u0435\u0440" +
            u"\u043a\u0438:</span></p></body></html>", None))
        self.clean_sql.setText(QCoreApplication.translate(
            "MainWindow", u"\u043e\u0447\u0438\u0441\u0442\u0438\u0442\u044c sql \u0411\u0414", None))
        self.analyze_butt.setText(QCoreApplication.translate(
            "MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043c\u043d\u043e\u0436" +
            u"\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0430\u043d\u0430\u043b\u0438\u0437", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.multiple_reading), QCoreApplication.translate(
            "MainWindow", u"\u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b" +
            u"\u0439 \u0430\u043d\u0430\u043b\u0438\u0437", None))
        self.screenhotPath_label.setText(QCoreApplication.translate("MainWindow",
                                                                    u"<html><head/><body>" +
                                                                    u"<p align=\"center\">screenhot.png" +
                                                                    u"</p></body></html>",
                                                                    None))
        self.screenshorPath_butt.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0443\u0442\u044c \u0434" +
                                                                    u"\u043b\u044f \u0441\u043e\u0445\u0440\u0430" +
                                                                    u"\u043d\u0435\u043d\u0438\u044f \u0441\u043a" +
                                                                    u"\u0440\u0438\u043d\u0448\u043e\u0442\u043e\u0432",
                                                                    None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"id", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"type", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"data", None))

        # заполение элементов текстом и первичная настройка таблицы
