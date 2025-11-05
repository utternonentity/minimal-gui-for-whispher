from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 620)
        MainWindow.setMinimumSize(QtCore.QSize(460, 620))
        MainWindow.setMaximumSize(QtCore.QSize(460, 620))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "#centralwidget{"
            "background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #243B53, stop:1 #1F6F8B);"
            "padding: 24px;"
            "}"
        )

        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        self.card = QtWidgets.QFrame(self.centralwidget)
        self.card.setObjectName("card")
        self.card.setStyleSheet(
            "#card{" "background-color: rgba(255,255,255,0.92);" "border-radius: 28px;" "}"
        )
        self.card.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.card.setFrameShadow(QtWidgets.QFrame.Raised)

        self.cardLayout = QtWidgets.QVBoxLayout(self.card)
        self.cardLayout.setContentsMargins(36, 40, 36, 36)
        self.cardLayout.setSpacing(24)

        self.headerLayout = QtWidgets.QVBoxLayout()
        self.headerLayout.setSpacing(8)

        self.title_label = QtWidgets.QLabel(self.card)
        title_font = QtGui.QFont()
        title_font.setFamily("Segoe UI Semibold")
        title_font.setPointSize(18)
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
        self.choose_file_bt.setMinimumHeight(48)
        choose_font = QtGui.QFont()
        choose_font.setPointSize(11)
        choose_font.setBold(True)
        choose_font.setWeight(75)
        self.choose_file_bt.setFont(choose_font)
        self.choose_file_bt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_file_bt.setStyleSheet(
            "QPushButton{"
            "background-color: #00B8D9;"
            "color: white;"
            "border-radius: 18px;"
            "}"
            "QPushButton:hover{background-color: #00A3C4;}"
            "QPushButton:pressed{background-color: #008EA9;}"
        )
        self.cardLayout.addWidget(self.choose_file_bt)

        self.file_info = QtWidgets.QFrame(self.card)
        self.file_info.setObjectName("file_info")
        self.file_info.setStyleSheet(
            "#file_info{" "background-color: #F0F4F8;" "border-radius: 16px;" "padding: 16px;" "}"
        )
        self.file_info_layout = QtWidgets.QVBoxLayout(self.file_info)
        self.file_info_layout.setContentsMargins(16, 16, 16, 16)
        self.file_info_layout.setSpacing(6)

        self.file_name_label = QtWidgets.QLabel(self.file_info)
        file_label_font = QtGui.QFont()
        file_label_font.setPointSize(9)
        file_label_font.setBold(True)
        file_label_font.setWeight(75)
        self.file_name_label.setFont(file_label_font)
        self.file_name_label.setStyleSheet("color: #243B53;")
        self.file_info_layout.addWidget(self.file_name_label)

        self.file_name_value = QtWidgets.QLabel(self.file_info)
        value_font = QtGui.QFont()
        value_font.setPointSize(9)
        self.file_name_value.setFont(value_font)
        self.file_name_value.setStyleSheet("color: #52606D;")
        self.file_name_value.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.file_info_layout.addWidget(self.file_name_value)

        self.cardLayout.addWidget(self.file_info)

        self.progress_container = QtWidgets.QFrame(self.card)
        self.progress_container.setObjectName("progress_container")
        self.progress_container.setStyleSheet(
            "#progress_container{" "background-color: #F7FAFC;" "border-radius: 16px;" "padding: 20px;" "}"
        )
        self.progressLayout = QtWidgets.QVBoxLayout(self.progress_container)
        self.progressLayout.setContentsMargins(12, 12, 12, 12)
        self.progressLayout.setSpacing(12)

        self.progress_title = QtWidgets.QLabel(self.progress_container)
        progress_title_font = QtGui.QFont()
        progress_title_font.setPointSize(10)
        progress_title_font.setBold(True)
        progress_title_font.setWeight(75)
        self.progress_title.setFont(progress_title_font)
        self.progress_title.setStyleSheet("color: #243B53;")
        self.progressLayout.addWidget(self.progress_title)

        self.progressBar = QtWidgets.QProgressBar(self.progress_container)
        self.progressBar.setMinimumHeight(24)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setStyleSheet(
            "QProgressBar{"
            "background-color: #D9E2EC;"
            "border: none;"
            "border-radius: 12px;"
            "color: #243B53;"
            "font-weight: 600;"
            "}"
            "QProgressBar::chunk{"
            "border-radius: 12px;"
            "background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #2D9CDB, stop:1 #27AE60);"
            "}"
        )
        self.progressLayout.addWidget(self.progressBar)

        self.status_label = QtWidgets.QLabel(self.progress_container)
        status_font = QtGui.QFont()
        status_font.setPointSize(9)
        self.status_label.setFont(status_font)
        self.status_label.setStyleSheet("color: #52606D;")
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
            "border-radius: 12px;"
            "padding: 12px;"
            "color: #334E68;"
            "}"
        )
        self.transcription_preview.setReadOnly(True)
        self.transcription_preview.setPlaceholderText("")
        self.transcription_preview.setMinimumHeight(140)
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
        self.choose_file_bt.setText(_translate("MainWindow", "Выбрать аудиозапись"))
        self.file_name_label.setText(_translate("MainWindow", "Выбранный файл"))
        self.file_name_value.setText(_translate("MainWindow", "Файл не выбран"))
        self.progress_title.setText(_translate("MainWindow", "Ход обработки"))
        self.status_label.setText(_translate("MainWindow", "Ожидание выбора файла"))
        self.preview_title.setText(_translate("MainWindow", "Предварительный просмотр"))
        self.report_hint.setText(
            _translate(
                "MainWindow",
                "После завершения обработки в папке исходного файла появятся отчёт в формате TXT и красиво оформленный документ DOCX."
            )
        )
