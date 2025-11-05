from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 640)
        MainWindow.setMinimumSize(QtCore.QSize(620, 560))
        base_font = QtGui.QFont()
        base_font.setFamily("Segoe UI")
        MainWindow.setFont(base_font)
        MainWindow.setStyleSheet("QMainWindow{background-color: #F5F7FA;}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(32, 32, 32, 32)
        self.mainLayout.setSpacing(24)

        self.card = QtWidgets.QFrame(self.centralwidget)
        self.card.setObjectName("card")
        self.card.setStyleSheet(
            "#card{"
            "background-color: #FFFFFF;"
            "border-radius: 24px;"
            "border: 1px solid #E4E7EB;"
            "}"
        )
        self.card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card.setFrameShadow(QtWidgets.QFrame.Raised)

        self.cardLayout = QtWidgets.QVBoxLayout(self.card)
        self.cardLayout.setContentsMargins(36, 40, 36, 36)
        self.cardLayout.setSpacing(28)

        self.headerLayout = QtWidgets.QVBoxLayout()
        self.headerLayout.setSpacing(10)

        self.title_label = QtWidgets.QLabel(self.card)
        title_font = QtGui.QFont()
        title_font.setFamily("Segoe UI Semibold")
        title_font.setPointSize(20)
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet("color: #102A43;")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.headerLayout.addWidget(self.title_label)

        self.subtitle_label = QtWidgets.QLabel(self.card)
        subtitle_font = QtGui.QFont()
        subtitle_font.setPointSize(10)
        self.subtitle_label.setFont(subtitle_font)
        self.subtitle_label.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle_label.setStyleSheet("color: #486581;")
        self.subtitle_label.setWordWrap(True)
        self.headerLayout.addWidget(self.subtitle_label)

        self.cardLayout.addLayout(self.headerLayout)

        self.choose_file_bt = QtWidgets.QPushButton(self.card)
        self.choose_file_bt.setMinimumHeight(50)
        choose_font = QtGui.QFont()
        choose_font.setPointSize(11)
        choose_font.setBold(True)
        choose_font.setWeight(75)
        self.choose_file_bt.setFont(choose_font)
        self.choose_file_bt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_file_bt.setStyleSheet(
            "QPushButton{"
            "background-color: #0366D6;"
            "color: white;"
            "border-radius: 16px;"
            "padding: 12px 24px;"
            "}"
            "QPushButton:hover{background-color: #0256B3;}"
            "QPushButton:pressed{background-color: #014A99;}"
            "QPushButton:disabled{background-color: #A7B6C2; color: #F0F4F8;}"
        )
        self.cardLayout.addWidget(self.choose_file_bt)

        self.file_info = QtWidgets.QFrame(self.card)
        self.file_info.setObjectName("file_info")
        self.file_info.setStyleSheet(
            "#file_info{"
            "background-color: #F0F4F8;"
            "border-radius: 18px;"
            "padding: 18px;"
            "}"
        )
        self.file_info_layout = QtWidgets.QGridLayout(self.file_info)
        self.file_info_layout.setContentsMargins(4, 4, 4, 4)
        self.file_info_layout.setHorizontalSpacing(12)
        self.file_info_layout.setVerticalSpacing(8)

        info_label_font = QtGui.QFont()
        info_label_font.setPointSize(9)
        info_label_font.setBold(True)
        info_label_font.setWeight(75)

        info_value_font = QtGui.QFont()
        info_value_font.setPointSize(9)

        self.file_name_label = QtWidgets.QLabel(self.file_info)
        self.file_name_label.setFont(info_label_font)
        self.file_name_label.setStyleSheet("color: #243B53;")
        self.file_info_layout.addWidget(self.file_name_label, 0, 0, 1, 1)

        self.file_name_value = QtWidgets.QLabel(self.file_info)
        self.file_name_value.setFont(info_value_font)
        self.file_name_value.setStyleSheet("color: #52606D;")
        self.file_name_value.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.file_info_layout.addWidget(self.file_name_value, 0, 1, 1, 1)

        self.file_path_label = QtWidgets.QLabel(self.file_info)
        self.file_path_label.setFont(info_label_font)
        self.file_path_label.setStyleSheet("color: #243B53;")
        self.file_info_layout.addWidget(self.file_path_label, 1, 0, 1, 1)

        self.file_path_value = QtWidgets.QLabel(self.file_info)
        self.file_path_value.setFont(info_value_font)
        self.file_path_value.setStyleSheet("color: #52606D;")
        self.file_path_value.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.file_path_value.setWordWrap(True)
        self.file_info_layout.addWidget(self.file_path_value, 1, 1, 1, 1)

        self.file_details_label = QtWidgets.QLabel(self.file_info)
        self.file_details_label.setFont(info_label_font)
        self.file_details_label.setStyleSheet("color: #243B53;")
        self.file_info_layout.addWidget(self.file_details_label, 2, 0, 1, 1)

        self.file_details_value = QtWidgets.QLabel(self.file_info)
        self.file_details_value.setFont(info_value_font)
        self.file_details_value.setStyleSheet("color: #52606D;")
        self.file_details_value.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.file_info_layout.addWidget(self.file_details_value, 2, 1, 1, 1)

        self.cardLayout.addWidget(self.file_info)

        self.progress_container = QtWidgets.QFrame(self.card)
        self.progress_container.setObjectName("progress_container")
        self.progress_container.setStyleSheet(
            "#progress_container{"
            "background-color: #F7FAFC;"
            "border-radius: 18px;"
            "padding: 20px;"
            "}"
        )
        self.progressLayout = QtWidgets.QVBoxLayout(self.progress_container)
        self.progressLayout.setContentsMargins(8, 8, 8, 8)
        self.progressLayout.setSpacing(14)

        self.progress_title = QtWidgets.QLabel(self.progress_container)
        progress_title_font = QtGui.QFont()
        progress_title_font.setPointSize(10)
        progress_title_font.setBold(True)
        progress_title_font.setWeight(75)
        self.progress_title.setFont(progress_title_font)
        self.progress_title.setStyleSheet("color: #243B53;")
        self.progressLayout.addWidget(self.progress_title)

        self.progressBar = QtWidgets.QProgressBar(self.progress_container)
        self.progressBar.setMinimumHeight(26)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setStyleSheet(
            "QProgressBar{"
            "background-color: #D9E2EC;"
            "border: none;"
            "border-radius: 13px;"
            "color: #243B53;"
            "font-weight: 600;"
            "}"
            "QProgressBar::chunk{"
            "border-radius: 13px;"
            "background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #2D9CDB, stop:1 #27AE60);"
            "}"
        )
        self.progressLayout.addWidget(self.progressBar)

        self.status_label = QtWidgets.QLabel(self.progress_container)
        status_font = QtGui.QFont()
        status_font.setPointSize(9)
        self.status_label.setFont(status_font)
        self.status_label.setStyleSheet("color: #52606D;")
        self.status_label.setWordWrap(True)
        self.progressLayout.addWidget(self.status_label)

        self.cardLayout.addWidget(self.progress_container)

        self.preview_title = QtWidgets.QLabel(self.card)
        preview_font = QtGui.QFont()
        preview_font.setPointSize(10)
        preview_font.setBold(True)
        preview_font.setWeight(75)
        self.preview_title.setFont(preview_font)
        self.preview_title.setStyleSheet("color: #243B53;")
        self.cardLayout.addWidget(self.preview_title)

        self.transcription_preview = QtWidgets.QTextEdit(self.card)
        preview_text_font = QtGui.QFont()
        preview_text_font.setPointSize(9)
        self.transcription_preview.setFont(preview_text_font)
        self.transcription_preview.setStyleSheet(
            "QTextEdit{"
            "background-color: #FFFFFF;"
            "border: 1px solid #D9E2EC;"
            "border-radius: 14px;"
            "padding: 14px;"
            "color: #334E68;"
            "}"
        )
        self.transcription_preview.setReadOnly(True)
        self.transcription_preview.setMinimumHeight(180)
        self.cardLayout.addWidget(self.transcription_preview)

        self.report_hint = QtWidgets.QLabel(self.card)
        report_hint_font = QtGui.QFont()
        report_hint_font.setPointSize(9)
        self.report_hint.setFont(report_hint_font)
        self.report_hint.setStyleSheet("color: #829AB1;")
        self.report_hint.setWordWrap(True)
        self.cardLayout.addWidget(self.report_hint)

        self.cardLayout.addStretch(1)

        self.mainLayout.addWidget(self.card)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Транскрибация аудио"))
        self.title_label.setText(_translate("MainWindow", "Транскрибация аудио"))
        self.subtitle_label.setText(
            _translate(
                "MainWindow",
                "Выберите файл, и приложение автоматически подготовит текстовый отчёт и документ Word."
            )
        )
        self.choose_file_bt.setText(_translate("MainWindow", "Выбрать файл"))
        self.file_name_label.setText(_translate("MainWindow", "Имя"))
        self.file_name_value.setText(_translate("MainWindow", "Файл не выбран"))
        self.file_path_label.setText(_translate("MainWindow", "Расположение"))
        self.file_path_value.setText(_translate("MainWindow", "—"))
        self.file_details_label.setText(_translate("MainWindow", "Формат и размер"))
        self.file_details_value.setText(_translate("MainWindow", "—"))
        self.progress_title.setText(_translate("MainWindow", "Ход обработки"))
        self.status_label.setText(_translate("MainWindow", "Ожидание выбора файла"))
        self.preview_title.setText(_translate("MainWindow", "Предварительный просмотр"))
        self.transcription_preview.setPlaceholderText(_translate("MainWindow", "Текст появится здесь после завершения обработки."))
        self.report_hint.setText(
            _translate(
                "MainWindow",
                "Готовый результат сохраняется рядом с исходным файлом: текст в формате TXT и отчёт в DOCX."
            )
        )
