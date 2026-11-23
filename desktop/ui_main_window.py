# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 390)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setObjectName(u"main_layout")
        self.model_form = QFormLayout()
        self.model_form.setObjectName(u"model_form")
        self.model_label = QLabel(self.centralwidget)
        self.model_label.setObjectName(u"model_label")

        self.model_form.setWidget(0, QFormLayout.LabelRole, self.model_label)

        self.model_box = QComboBox(self.centralwidget)
        self.model_box.setObjectName(u"model_box")

        self.model_form.setWidget(0, QFormLayout.FieldRole, self.model_box)


        self.main_layout.addLayout(self.model_form)

        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.form_page = QWidget()
        self.form_page.setObjectName(u"form_page")
        self.feature_form = QFormLayout(self.form_page)
        self.feature_form.setObjectName(u"feature_form")
        self.age_label = QLabel(self.form_page)
        self.age_label.setObjectName(u"age_label")

        self.feature_form.setWidget(0, QFormLayout.LabelRole, self.age_label)

        self.age_input = QLineEdit(self.form_page)
        self.age_input.setObjectName(u"age_input")

        self.feature_form.setWidget(0, QFormLayout.FieldRole, self.age_input)

        self.income_label = QLabel(self.form_page)
        self.income_label.setObjectName(u"income_label")

        self.feature_form.setWidget(1, QFormLayout.LabelRole, self.income_label)

        self.income_input = QLineEdit(self.form_page)
        self.income_input.setObjectName(u"income_input")

        self.feature_form.setWidget(1, QFormLayout.FieldRole, self.income_input)

        self.amount_label = QLabel(self.form_page)
        self.amount_label.setObjectName(u"amount_label")

        self.feature_form.setWidget(2, QFormLayout.LabelRole, self.amount_label)

        self.amount_input = QLineEdit(self.form_page)
        self.amount_input.setObjectName(u"amount_input")

        self.feature_form.setWidget(2, QFormLayout.FieldRole, self.amount_input)

        self.term_label = QLabel(self.form_page)
        self.term_label.setObjectName(u"term_label")

        self.feature_form.setWidget(3, QFormLayout.LabelRole, self.term_label)

        self.term_input = QLineEdit(self.form_page)
        self.term_input.setObjectName(u"term_input")

        self.feature_form.setWidget(3, QFormLayout.FieldRole, self.term_input)

        self.loans_label = QLabel(self.form_page)
        self.loans_label.setObjectName(u"loans_label")

        self.feature_form.setWidget(4, QFormLayout.LabelRole, self.loans_label)

        self.loans_input = QLineEdit(self.form_page)
        self.loans_input.setObjectName(u"loans_input")

        self.feature_form.setWidget(4, QFormLayout.FieldRole, self.loans_input)

        self.late_label = QLabel(self.form_page)
        self.late_label.setObjectName(u"late_label")

        self.feature_form.setWidget(5, QFormLayout.LabelRole, self.late_label)

        self.late_input = QLineEdit(self.form_page)
        self.late_input.setObjectName(u"late_input")

        self.feature_form.setWidget(5, QFormLayout.FieldRole, self.late_input)

        self.employment_label = QLabel(self.form_page)
        self.employment_label.setObjectName(u"employment_label")

        self.feature_form.setWidget(6, QFormLayout.LabelRole, self.employment_label)

        self.employment_input = QLineEdit(self.form_page)
        self.employment_input.setObjectName(u"employment_input")

        self.feature_form.setWidget(6, QFormLayout.FieldRole, self.employment_input)

        self.tabs.addTab(self.form_page, "")
        self.line_page = QWidget()
        self.line_page.setObjectName(u"line_page")
        self.line_layout = QVBoxLayout(self.line_page)
        self.line_layout.setObjectName(u"line_layout")
        self.order_label = QLabel(self.line_page)
        self.order_label.setObjectName(u"order_label")

        self.line_layout.addWidget(self.order_label)

        self.features_input = QLineEdit(self.line_page)
        self.features_input.setObjectName(u"features_input")

        self.line_layout.addWidget(self.features_input)

        self.line_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.line_layout.addItem(self.line_spacer)

        self.tabs.addTab(self.line_page, "")

        self.main_layout.addWidget(self.tabs)

        self.predict_button = QPushButton(self.centralwidget)
        self.predict_button.setObjectName(u"predict_button")

        self.main_layout.addWidget(self.predict_button)

        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")

        self.main_layout.addWidget(self.clear_button)

        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setWordWrap(True)

        self.main_layout.addWidget(self.result_label)

        self.probability_bar = QProgressBar(self.centralwidget)
        self.probability_bar.setObjectName(u"probability_bar")
        self.probability_bar.setValue(0)

        self.main_layout.addWidget(self.probability_bar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0435\u0434\u0438\u0442\u043d\u044b\u0439 \u0441\u043a\u043e\u0440\u0438\u043d\u0433", None))
        self.model_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.age_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442 \u0437\u0430\u0451\u043c\u0449\u0438\u043a\u0430, \u043b\u0435\u0442", None))
        self.age_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, 35", None))
        self.income_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434 \u0437\u0430\u0451\u043c\u0449\u0438\u043a\u0430, \u0434\u0435\u043d. \u0435\u0434.", None))
        self.income_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, 60000", None))
        self.amount_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043a\u0440\u0435\u0434\u0438\u0442\u0430, \u0434\u0435\u043d. \u0435\u0434.", None))
        self.amount_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, 25000", None))
        self.term_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a \u043a\u0440\u0435\u0434\u0438\u0442\u0430, \u043c\u0435\u0441\u044f\u0446\u0435\u0432", None))
        self.term_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, 24", None))
        self.loans_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0445 \u043a\u0440\u0435\u0434\u0438\u0442\u043e\u0432", None))
        self.loans_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, 2", None))
        self.late_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043d\u044b\u0445 \u043f\u043b\u0430\u0442\u0435\u0436\u0435\u0439", None))
        self.late_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, 1", None))
        self.employment_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0443\u0434\u043e\u0432\u043e\u0439 \u0441\u0442\u0430\u0436, \u043b\u0435\u0442", None))
        self.employment_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, 10", None))
        self.tabs.setTabText(self.tabs.indexOf(self.form_page), QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043f\u043e\u043b\u044f\u043c", None))
        self.order_label.setText(QCoreApplication.translate("MainWindow", u"1. \u0412\u043e\u0437\u0440\u0430\u0441\u0442 \u0437\u0430\u0451\u043c\u0449\u0438\u043a\u0430, \u043b\u0435\u0442\n"
"2. \u0414\u043e\u0445\u043e\u0434 \u0437\u0430\u0451\u043c\u0449\u0438\u043a\u0430, \u0434\u0435\u043d. \u0435\u0434.\n"
"3. \u0421\u0443\u043c\u043c\u0430 \u043a\u0440\u0435\u0434\u0438\u0442\u0430, \u0434\u0435\u043d. \u0435\u0434.\n"
"4. \u0421\u0440\u043e\u043a \u043a\u0440\u0435\u0434\u0438\u0442\u0430, \u043c\u0435\u0441\u044f\u0446\u0435\u0432\n"
"5. \u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0445 \u043a\u0440\u0435\u0434\u0438\u0442\u043e\u0432\n"
"6. \u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u0441\u0440\u043e\u0447\u0435\u043d\u043d\u044b\u0445 \u043f\u043b\u0430\u0442\u0435\u0436\u0435\u0439\n"
"7. \u0422\u0440\u0443\u0434\u043e\u0432\u043e\u0439 \u0441\u0442\u0430\u0436, \u043b\u0435\u0442", None))
        self.features_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0437\u043d\u0430\u043a\u0438 \u0447\u0435\u0440\u0435\u0437 \u0437\u0430\u043f\u044f\u0442\u0443\u044e", None))
        self.tabs.setTabText(self.tabs.indexOf(self.line_page), QCoreApplication.translate("MainWindow", u"\u041e\u0434\u043d\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u043e\u0439", None))
        self.predict_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.result_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u0437\u0434\u0435\u0441\u044c", None))
        self.probability_bar.setFormat(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u0430\u043d\u043d\u043e\u0433\u043e \u043a\u043b\u0430\u0441\u0441\u0430: %p%", None))
    # retranslateUi

