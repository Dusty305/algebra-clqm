import Algebra
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

NATURAL = 0
INTEGER = 1
RATIONAL = 2
POLYNOM = 3

INPUT_ERROR = 0
CALCULATION_ERROR = 1
CONVERTION_ERROR = 2

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Страница сейчас
        self.currentIndex = NATURAL
        # Когда errorHandle в getNumber, и не надо exec
        self.errorFlag = False
        # Сама операция (только если не унарная)
        self.operation = None
        # Количество операндов, нужно для выполнения операции
        self.nOfOperands = 0
        self.types = list()

        self.setObjectName("self")
        self.resize(500, 600)
        self.setMinimumSize(QtCore.QSize(500, 600))
        self.setMaximumSize(QtCore.QSize(500, 700))

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -1, 500, 580))
        self.stackedWidget.setMinimumSize(QtCore.QSize(500, 580))
        self.stackedWidget.setMaximumSize(QtCore.QSize(500, 580))
        self.stackedWidget.setObjectName("stackedWidget")

        self.createNaturalPage()
        self.createIntegerPage()
        self.createRationalPage()
        self.createPolynomPage()
        self.currentLineEdit = self.n_input

        self.createMenuBar()

        self.setActions()

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(self.currentIndex)
        QtCore.QMetaObject.connectSlotsByName(self)

    def createNaturalPage(self):
        self.Natural = QtWidgets.QWidget()
        self.Natural.setObjectName("Natural")

        bold_font = QtGui.QFont()
        bold_font.setPointSize(11)
        bold_font.setBold(True)
        bold_font.setWeight(75)

        label_font = QtGui.QFont()
        label_font.setPointSize(14)
        label_font.setBold(False)
        label_font.setWeight(50)
        label_font.setStrikeOut(False)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.n_input = QtWidgets.QLineEdit(self.Natural)
        self.n_input.setGeometry(QtCore.QRect(50, 30, 400, 81))
        self.n_input.setObjectName("n_input")
        self.n_label = QtWidgets.QLabel(self.Natural)
        self.n_label.setGeometry(QtCore.QRect(50, 120, 211, 21))
        self.n_label.setFont(label_font)
        self.n_label.setObjectName("n_label")
        self.n_add = QtWidgets.QPushButton(self.Natural)
        self.n_add.setGeometry(QtCore.QRect(50, 160, 50, 40))
        self.n_add.setFont(bold_font)
        self.n_add.setObjectName("n_add")
        self.n_incr = QtWidgets.QPushButton(self.Natural)
        self.n_incr.setGeometry(QtCore.QRect(350, 240, 100, 45))
        self.n_incr.setObjectName("n_incr")
        self.n_sub = QtWidgets.QPushButton(self.Natural)
        self.n_sub.setGeometry(QtCore.QRect(140, 160, 50, 40))
        self.n_sub.setFont(bold_font)
        self.n_sub.setObjectName("n_sub")
        self.n_cmp = QtWidgets.QPushButton(self.Natural)
        self.n_cmp.setGeometry(QtCore.QRect(50, 240, 100, 45))
        self.n_cmp.setObjectName("n_cmp")
        self.n_is_zero = QtWidgets.QPushButton(self.Natural)
        self.n_is_zero.setGeometry(QtCore.QRect(200, 240, 100, 45))
        self.n_is_zero.setObjectName("n_is_zero")
        self.n_mul_d = QtWidgets.QPushButton(self.Natural)
        self.n_mul_d.setGeometry(QtCore.QRect(200, 320, 100, 45))
        self.n_mul_d.setObjectName("n_mul_d")
        self.n_mod = QtWidgets.QPushButton(self.Natural)
        self.n_mod.setGeometry(QtCore.QRect(400, 160, 50, 40))
        self.n_mod.setFont(font)
        self.n_mod.setObjectName("n_mod")
        self.n_sub_dn = QtWidgets.QPushButton(self.Natural)
        self.n_sub_dn.setGeometry(QtCore.QRect(350, 320, 100, 45))
        self.n_sub_dn.setObjectName("n_sub_dn")
        self.n_mul_k = QtWidgets.QPushButton(self.Natural)
        self.n_mul_k.setGeometry(QtCore.QRect(50, 320, 100, 45))
        self.n_mul_k.setObjectName("n_mul_k")
        self.n_div_dk = QtWidgets.QPushButton(self.Natural)
        self.n_div_dk.setGeometry(QtCore.QRect(50, 400, 100, 45))
        self.n_div_dk.setObjectName("n_div_dk")
        self.n_mul = QtWidgets.QPushButton(self.Natural)
        self.n_mul.setGeometry(QtCore.QRect(226, 160, 50, 40))
        self.n_mul.setFont(bold_font)
        self.n_mul.setObjectName("n_mul")
        self.n_div = QtWidgets.QPushButton(self.Natural)
        self.n_div.setGeometry(QtCore.QRect(314, 160, 50, 40))
        self.n_div.setFont(font)
        self.n_div.setObjectName("n_div")
        self.n_gcf = QtWidgets.QPushButton(self.Natural)
        self.n_gcf.setGeometry(QtCore.QRect(200, 400, 100, 45))
        self.n_gcf.setObjectName("n_gcf")
        self.n_lcm = QtWidgets.QPushButton(self.Natural)
        self.n_lcm.setGeometry(QtCore.QRect(350, 400, 100, 45))
        self.n_lcm.setObjectName("n_lcm")
        self.z_ntoz = QtWidgets.QPushButton(self.Natural)
        self.z_ntoz.setGeometry(QtCore.QRect(50, 480, 100, 45))
        self.z_ntoz.setObjectName("z_ntoz")
        self.stackedWidget.addWidget(self.Natural)

    def createIntegerPage(self):
        self.Integer = QtWidgets.QWidget()
        self.Integer.setObjectName("Integer")

        bold_font = QtGui.QFont()
        bold_font.setPointSize(11)
        bold_font.setBold(True)
        bold_font.setWeight(75)

        label_font = QtGui.QFont()
        label_font.setPointSize(14)
        label_font.setBold(False)
        label_font.setWeight(50)
        label_font.setStrikeOut(False)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.z_input = QtWidgets.QLineEdit(self.Integer)
        self.z_input.setGeometry(QtCore.QRect(50, 30, 400, 81))
        self.z_input.setObjectName("z_input")
        self.z_label = QtWidgets.QLabel(self.Integer)
        self.z_label.setGeometry(QtCore.QRect(50, 120, 151, 21))
        self.z_label.setFont(label_font)
        self.z_label.setObjectName("z_label")
        self.z_zton = QtWidgets.QPushButton(self.Integer)
        self.z_zton.setGeometry(QtCore.QRect(50, 320, 100, 45))
        self.z_zton.setObjectName("z_zton")
        self.z_change_sign = QtWidgets.QPushButton(self.Integer)
        self.z_change_sign.setGeometry(QtCore.QRect(350, 240, 100, 45))
        self.z_change_sign.setObjectName("z_change_sign")
        self.z_div = QtWidgets.QPushButton(self.Integer)
        self.z_div.setGeometry(QtCore.QRect(314, 160, 50, 40))
        self.z_div.setFont(font)
        self.z_div.setObjectName("z_div")
        self.z_mod = QtWidgets.QPushButton(self.Integer)
        self.z_mod.setGeometry(QtCore.QRect(400, 160, 50, 40))
        self.z_mod.setFont(font)
        self.z_mod.setObjectName("z_mod")
        self.z_add = QtWidgets.QPushButton(self.Integer)
        self.z_add.setGeometry(QtCore.QRect(50, 160, 50, 40))
        self.z_add.setFont(bold_font)
        self.z_add.setObjectName("z_add")
        self.z_mul = QtWidgets.QPushButton(self.Integer)
        self.z_mul.setGeometry(QtCore.QRect(226, 160, 50, 40))
        self.z_mul.setFont(bold_font)
        self.z_mul.setObjectName("z_mul")
        self.z_abs = QtWidgets.QPushButton(self.Integer)
        self.z_abs.setGeometry(QtCore.QRect(50, 240, 100, 45))
        self.z_abs.setObjectName("z_abs")
        self.z_sub = QtWidgets.QPushButton(self.Integer)
        self.z_sub.setGeometry(QtCore.QRect(140, 160, 50, 40))
        self.z_sub.setFont(bold_font)
        self.z_sub.setObjectName("z_sub")
        self.z_sign = QtWidgets.QPushButton(self.Integer)
        self.z_sign.setGeometry(QtCore.QRect(200, 240, 100, 45))
        self.z_sign.setObjectName("z_sign")
        self.r_to_rational = QtWidgets.QPushButton(self.Integer)
        self.r_to_rational.setGeometry(QtCore.QRect(200, 320, 100, 45))
        self.r_to_rational.setObjectName("r_to_rational")
        self.stackedWidget.addWidget(self.Integer)

    def createRationalPage(self):
        self.Rational = QtWidgets.QWidget()
        self.Rational.setObjectName("Rational")

        bold_font = QtGui.QFont()
        bold_font.setPointSize(11)
        bold_font.setBold(True)
        bold_font.setWeight(75)

        label_font = QtGui.QFont()
        label_font.setPointSize(14)
        label_font.setBold(False)
        label_font.setWeight(50)
        label_font.setStrikeOut(False)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.r_input = QtWidgets.QLineEdit(self.Rational)
        self.r_input.setGeometry(QtCore.QRect(50, 30, 400, 81))
        self.r_input.setObjectName("r_input")
        self.r_label = QtWidgets.QLabel(self.Rational)
        self.r_label.setGeometry(QtCore.QRect(50, 120, 171, 21))
        self.r_label.setFont(label_font)
        self.r_label.setObjectName("r_label")
        self.r_mul = QtWidgets.QPushButton(self.Rational)
        self.r_mul.setGeometry(QtCore.QRect(285, 160, 50, 40))
        self.r_mul.setFont(bold_font)
        self.r_mul.setObjectName("r_mul")
        self.r_to_int = QtWidgets.QPushButton(self.Rational)
        self.r_to_int.setGeometry(QtCore.QRect(350, 240, 100, 45))
        self.r_to_int.setObjectName("r_to_int")
        self.r_add = QtWidgets.QPushButton(self.Rational)
        self.r_add.setGeometry(QtCore.QRect(50, 160, 50, 40))
        self.r_add.setFont(bold_font)
        self.r_add.setObjectName("r_add")
        self.r_reduce = QtWidgets.QPushButton(self.Rational)
        self.r_reduce.setGeometry(QtCore.QRect(50, 240, 100, 45))
        self.r_reduce.setObjectName("r_reduce")
        self.r_sub = QtWidgets.QPushButton(self.Rational)
        self.r_sub.setGeometry(QtCore.QRect(165, 160, 50, 40))
        self.r_sub.setFont(bold_font)
        self.r_sub.setObjectName("r_sub")
        self.r_is_int = QtWidgets.QPushButton(self.Rational)
        self.r_is_int.setGeometry(QtCore.QRect(200, 240, 100, 45))
        self.r_is_int.setObjectName("r_is_int")
        self.r_div = QtWidgets.QPushButton(self.Rational)
        self.r_div.setGeometry(QtCore.QRect(400, 160, 50, 40))
        self.r_div.setFont(font)
        self.r_div.setObjectName("r_div")
        self.stackedWidget.addWidget(self.Rational)

    def createPolynomPage(self):
        self.Polynom = QtWidgets.QWidget()
        self.Polynom.setObjectName("Polynom")

        bold_font = QtGui.QFont()
        bold_font.setPointSize(11)
        bold_font.setBold(True)
        bold_font.setWeight(75)

        label_font = QtGui.QFont()
        label_font.setPointSize(14)
        label_font.setBold(False)
        label_font.setWeight(50)
        label_font.setStrikeOut(False)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.p_input = QtWidgets.QLineEdit(self.Polynom)
        self.p_input.setGeometry(QtCore.QRect(50, 30, 400, 81))
        self.p_input.setObjectName("p_input")
        self.p_label = QtWidgets.QLabel(self.Polynom)
        self.p_label.setGeometry(QtCore.QRect(50, 120, 221, 21))
        self.p_label.setFont(label_font)
        self.p_label.setObjectName("p_label")
        self.p_add = QtWidgets.QPushButton(self.Polynom)
        self.p_add.setGeometry(QtCore.QRect(50, 160, 50, 40))
        self.p_add.setFont(bold_font)
        self.p_add.setObjectName("p_add")
        self.p_mul_q = QtWidgets.QPushButton(self.Polynom)
        self.p_mul_q.setGeometry(QtCore.QRect(50, 240, 100, 45))
        self.p_mul_q.setObjectName("p_mul_q")
        self.p_sub = QtWidgets.QPushButton(self.Polynom)
        self.p_sub.setGeometry(QtCore.QRect(140, 160, 50, 40))
        self.p_sub.setFont(bold_font)
        self.p_sub.setObjectName("p_sub")
        self.p_div = QtWidgets.QPushButton(self.Polynom)
        self.p_div.setGeometry(QtCore.QRect(314, 160, 50, 40))
        self.p_div.setFont(font)
        self.p_div.setObjectName("p_div")
        self.p_high_c = QtWidgets.QPushButton(self.Polynom)
        self.p_high_c.setGeometry(QtCore.QRect(350, 240, 100, 45))
        self.p_high_c.setObjectName("p_high_c")
        self.p_mul_xk = QtWidgets.QPushButton(self.Polynom)
        self.p_mul_xk.setGeometry(QtCore.QRect(200, 240, 100, 45))
        self.p_mul_xk.setObjectName("p_mul_xk")
        self.p_mul = QtWidgets.QPushButton(self.Polynom)
        self.p_mul.setGeometry(QtCore.QRect(226, 160, 50, 40))
        self.p_mul.setFont(bold_font)
        self.p_mul.setObjectName("p_mul")
        self.p_power = QtWidgets.QPushButton(self.Polynom)
        self.p_power.setGeometry(QtCore.QRect(50, 320, 100, 45))
        self.p_power.setObjectName("p_power")
        self.p_nmr = QtWidgets.QPushButton(self.Polynom)
        self.p_nmr.setGeometry(QtCore.QRect(200, 400, 100, 45))
        self.p_nmr.setObjectName("p_nmr")
        self.p_mod = QtWidgets.QPushButton(self.Polynom)
        self.p_mod.setGeometry(QtCore.QRect(400, 160, 50, 40))
        self.p_mod.setFont(font)
        self.p_mod.setObjectName("p_mod")
        self.p_fac = QtWidgets.QPushButton(self.Polynom)
        self.p_fac.setGeometry(QtCore.QRect(350, 320, 100, 45))
        self.p_fac.setObjectName("p_fac")
        self.p_derivative = QtWidgets.QPushButton(self.Polynom)
        self.p_derivative.setGeometry(QtCore.QRect(50, 400, 100, 45))
        self.p_derivative.setObjectName("p_derivative")
        self.p_gcf = QtWidgets.QPushButton(self.Polynom)
        self.p_gcf.setGeometry(QtCore.QRect(200, 320, 100, 45))
        self.p_gcf.setObjectName("p_gcf")
        self.stackedWidget.addWidget(self.Polynom)
        self.setCentralWidget(self.centralwidget)

    def createMenuBar(self):
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        # self.about = QtWidgets.QMenu(self.menu_bar)
        self.others = QtWidgets.QMenu(self.menu_bar)
        self.classes = QtWidgets.QMenu(self.menu_bar)
        self.setMenuBar(self.menu_bar)

    def setActions(self):
        # MENU BAR ACTIONS
        self.to_wNatural = QtWidgets.QAction(self)
        self.to_wNatural.triggered.connect(lambda: self.changePage(NATURAL))
        self.to_wInteger = QtWidgets.QAction(self)
        self.to_wInteger.triggered.connect(lambda: self.changePage(INTEGER))
        self.to_wRational = QtWidgets.QAction(self)
        self.to_wRational.triggered.connect(lambda: self.changePage(RATIONAL))
        self.to_wPolynom = QtWidgets.QAction(self)
        self.to_wPolynom.triggered.connect(lambda: self.changePage(POLYNOM))

        self.help = QtWidgets.QAction(self)
        self.help.triggered.connect(self.open_help)
        self.about = QtWidgets.QAction(self)
        self.about.triggered.connect(self.open_about)

        self.classes.addAction(self.to_wNatural)
        self.classes.addAction(self.to_wInteger)
        self.classes.addAction(self.to_wRational)
        self.classes.addAction(self.to_wPolynom)
        self.others.addAction(self.help)
        self.others.addAction(self.about)

        self.menu_bar.addAction(self.classes.menuAction())
        self.menu_bar.addAction(self.others.menuAction())

        # NATURAL BUTTONS ACTIONS
        self.n_input.returnPressed.connect(lambda: self.execOperation(self.getNumber(self.types)))

        self.n_add.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).__add__, 2, [Algebra.Natural]))
        self.n_sub.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).__sub__, 2, [Algebra.Natural]))
        self.n_mul.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).__mul__, 2, [Algebra.Natural]))
        self.n_div.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).__truediv__, 2, [Algebra.Natural]))
        self.n_mod.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).__mod__, 2, [Algebra.Natural]))
        self.n_cmp.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).compare, 2, [Algebra.Natural]))
        self.n_mul_k.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).mul_k, 2, [int]))
        self.n_incr.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).increment, 1))
        self.n_mul_d.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).mul_d, 2, [int]))
        self.n_sub_dn.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).sub_dn, 3, [int, Algebra.Natural]))
        self.n_div_dk.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).div_dk, 2, [Algebra.Natural]))
        self.n_gcf.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).gcf, 2, [Algebra.Natural]))
        self.n_lcm.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).lcm, 2, [Algebra.Natural]))
        self.n_is_zero.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Natural]).is_zero, 1))
        self.z_ntoz.clicked.connect(
            lambda: self.toAnotherType(self.getNumber([Algebra.Natural]), INTEGER))

        # INTEGER BUTTONS ACTIONS
        self.z_input.returnPressed.connect(
            lambda: self.execOperation(self.getNumber(self.types)))

        self.z_zton.clicked.connect(
            lambda: self.toAnotherType(self.getNumber([Algebra.Integer]), NATURAL))
        self.z_change_sign.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Integer]).change_sign, 1))
        self.z_div.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Integer]).__truediv__, 2, [Algebra.Integer]))
        self.z_mod.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Integer]).__mod__, 2, [Algebra.Integer]))
        self.z_add.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Integer]).__add__, 2, [Algebra.Integer]))
        self.z_mul.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Integer]).__mul__, 2, [Algebra.Integer]))
        self.z_abs.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Integer]).__abs__, 1))
        self.z_sub.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Integer]).__sub__, 2, [Algebra.Integer]))
        self.z_sign.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Integer]).sign, 1))
        self.r_to_rational.clicked.connect(
            lambda: self.toAnotherType(self.getNumber([Algebra.Integer]), RATIONAL))

        # RATIONAL BUTTONS ACTIONS
        self.r_input.returnPressed.connect(
            lambda: self.execOperation(self.getNumber(self.types)))

        self.r_mul.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Rational]).__mul__, 2, [Algebra.Rational]))
        self.r_add.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Rational]).__add__, 2, [Algebra.Rational]))
        self.r_reduce.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Rational]).reduce, 1))
        self.r_sub.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Rational]).__sub__, 2, [Algebra.Rational]))
        self.r_is_int.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Rational]).is_int, 1))
        self.r_div.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Rational]).__truediv__, 2, [Algebra.Rational]))
        self.r_to_int.clicked.connect(
            lambda: self.toAnotherType(self.getNumber([Algebra.Rational]), INTEGER))

        # POLYNOM BUTTONS ACTIONS
        self.p_input.returnPressed.connect(lambda: self.execOperation(self.getNumber(self.types)))

        self.p_add.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).__add__, 2, [Algebra.Polynom]))
        self.p_sub.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).__sub__, 2, [Algebra.Polynom]))
        self.p_mul.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).__mul__, 2, [Algebra.Polynom]))
        self.p_div.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).__truediv__, 2, [Algebra.Polynom]))
        self.p_mod.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).__mod__, 2, [Algebra.Polynom]))
        self.p_mul_q.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).mul_q, 2, [Algebra.Rational]))
        self.p_high_c.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).higher_coef, 1))
        self.p_mul_xk.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).mul_xk, 2, [int]))
        self.p_power.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).power, 1))
        self.p_nmr.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).nmr, 1))
        self.p_fac.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).fac, 1))
        self.p_derivative.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).derivate, 1))
        self.p_gcf.clicked.connect(
            lambda: self.handleOperation(self.getNumber([Algebra.Polynom]).gcf, 2, [Algebra.Polynom]))

    def open_help(self):
        webbrowser.open(
            "https://docs.google.com/document/d/1bI2HqqG6HD9MqF5VXyMlmQ4HzDjcNjzlJ-XzVP2vOlA/edit?usp=sharing")

    def open_about(self):
        webbrowser.open(
            "https://docs.google.com/document/d/1UQml9XQd2H7PG7L-zd97Js5zGSWCsT7vJ1h2A91Pz2k/edit?usp=sharing")

    def toAnotherType(self, number, page):
        if self.errorFlag:
            self.errorFlag = False
            return

        question = QtWidgets.QMessageBox()

        question.setWindowTitle("Перейти к другой странице")
        if page == NATURAL:
            question.setText("Перейти к странице с натуральными числами?")
        elif page == INTEGER:
            question.setText("Перейти к странице с целыми числами?")
        elif page == RATIONAL:
            question.setText("Перейти к странице с дробными числами?")
        else:
            question.setText("Перейти к странице с многочленами (полиномами)?")

        question.setIcon(QtWidgets.QMessageBox.Warning)
        question.setStandardButtons(QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Cancel)

        question.buttonClicked.connect(lambda x: self.btnClicked(x, number, page))

        question.exec_()

    def btnClicked(self, btn, number, page):
        try:
            if btn.text() == "OK":
                if page == NATURAL:
                    self.operation = Algebra.Integer.to_natural(number)
                elif page == INTEGER and self.currentIndex == NATURAL:
                    self.operation = Algebra.Integer.natural_to_integer(number)
                elif page == INTEGER and self.currentIndex == RATIONAL:
                    self.operation = Algebra.Rational.to_integer(number)
                elif page == RATIONAL:
                    self.operation = Algebra.Rational.integer_to_rational(number)
                self.changePage(page)
                self.currentLineEdit.setText(str(self.operation))
        except Exception as exc:
            self.errorHandle(CONVERTION_ERROR, repr(exc))

    # types - это массив типов чисел, которые должны быть введены
    def getNumber(self, types):
        numbers = list(str(self.currentLineEdit.text()).split())

        # Если нужно ввести полином, то в конструктор нужно будет передать не строку, а массив
        if len(types) == 1 and types[0] is Algebra.Polynom:
            numbers = [numbers]

        result = list()
        try:
            # Если был нажат enter без операций
            if len(types) == 0:
                self.currentLineEdit.clear()
                return self.classOfCurrentPage()()
            elif len(types) != len(numbers):
                raise Exception("wrong amount of variables was entered")
            # Каждое число преобразуем
            for i in range(len(types)):
                result.append(types[i](numbers[i]))
            # Возвращаем объект, а не список, если у нас нужно было ввести всего 1 элемент
            self.currentLineEdit.clear()
            return result if len(types) > 1 else result[0]
        except Exception as exc:
            self.errorHandle(INPUT_ERROR, repr(exc))
            self.errorFlag = True
            # Чтобы не вылетела ошибка, возвращаем пустой объект
            # ExecOperation или handleOperation не запустятся из-за флага в любом случае
            return self.classOfCurrentPage()()

    def handleOperation(self, operand, nOfOperands, types = []):
        if self.errorFlag:
            self.errorFlag = False
            return
        self.nOfOperands = nOfOperands
        self.operation = operand
        # Если унарная операция, то выполняем сразу
        if nOfOperands == 1:
            self.execOperation(operand)
        # Если нужно, чтобы ввели ещё переменные
        else:
            # Нужно для ввода 2ого/3его операнда
            self.types = types

    def execOperation(self, operand):
        if not self.operation is None and not self.errorFlag:
            try:
                if self.nOfOperands == 1:
                    output = str(self.operation())
                elif self.nOfOperands == 2:
                    output = str(self.operation(operand))
                elif self.nOfOperands == 3:
                    output = str(self.operation(operand[0], operand[1]))
                self.currentLineEdit.setText(output)
            except Exception as exc:
                self.errorHandle(CALCULATION_ERROR, repr(exc))
        else:
            self.currentLineEdit.clear()
        self.resetVariables()
        self.errorFlag = False

    def classOfCurrentPage(self):
        if self.currentIndex == 0:
            return Algebra.Natural
        elif self.currentIndex == 1:
            return Algebra.Integer
        elif self.currentIndex == 2:
            return Algebra.Rational
        else:
            return Algebra.Polynom

    def resetVariables(self):
        self.operation = None
        self.types = list()
        self.firstEntered = False
        # Сама операция (только если не унарная)
        self.operation = None
        # Количество операндов, нужно для выполнения операции
        self.nOfOperands = 0
        self.types = list()

    def errorHandle(self, code, errorText):
        error = QtWidgets.QMessageBox()
        self.resetVariables()

        error.setWindowTitle("Ошибка")
        if code is INPUT_ERROR:
            error.setText("Ошибка при вводе числа.")
        else:
            error.setText("Ошибка.")

        error.setIcon(QtWidgets.QMessageBox.Warning)
        error.setStandardButtons(QtWidgets.QMessageBox.Ok)

        error.setDetailedText(errorText)

        error.exec_()

    def changePage(self, index):
        self.stackedWidget.setCurrentIndex(index)
        self.currentIndex = index
        if index == NATURAL:
            self.currentLineEdit = self.n_input
        elif index == INTEGER:
            self.currentLineEdit = self.z_input
        elif index == RATIONAL:
            self.currentLineEdit = self.r_input
        else:
            self.currentLineEdit = self.p_input

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Algebra-CLQM"))
        self.n_label.setText(_translate("self", "Натуральные числа (n)"))
        self.n_add.setText(_translate("self", "+"))
        self.n_incr.setText(_translate("self", "+1"))
        self.n_sub.setText(_translate("self", "-"))
        self.n_cmp.setText(_translate("self", ">, <, ="))
        self.n_is_zero.setText(_translate("self", "= 0"))
        self.n_mul_d.setText(_translate("self", "*d"))
        self.n_mod.setText(_translate("self", "%"))
        self.n_sub_dn.setText(_translate("self", "- (d * n)"))
        self.n_mul_k.setText(_translate("self", "*10^k"))
        self.n_div_dk.setText(_translate("self", "- (n * 10^k)"))
        self.n_mul.setText(_translate("self", "*"))
        self.n_div.setText(_translate("self", "/"))
        self.n_gcf.setText(_translate("self", "НОД"))
        self.n_lcm.setText(_translate("self", "НОК"))
        self.z_ntoz.setText(_translate("self", "К целому"))
        self.z_label.setText(_translate("self", "Целые числа (z)"))
        self.z_zton.setText(_translate("self", "К натуральному"))
        self.z_change_sign.setText(_translate("self", "* (-1)"))
        self.z_div.setText(_translate("self", "/"))
        self.z_mod.setText(_translate("self", "%"))
        self.z_add.setText(_translate("self", "+"))
        self.z_mul.setText(_translate("self", "*"))
        self.z_abs.setText(_translate("self", "abs"))
        self.z_sub.setText(_translate("self", "-"))
        self.z_sign.setText(_translate("self", "+, -, 0"))
        self.r_to_rational.setText(_translate("self", "К рациональному"))
        self.r_label.setText(_translate("self", "Рационалые числа"))
        self.r_mul.setText(_translate("self", "*"))
        self.r_to_int.setText(_translate("self", "К целому"))
        self.r_add.setText(_translate("self", "+"))
        self.r_reduce.setText(_translate("self", "Сократить"))
        self.r_sub.setText(_translate("self", "-"))
        self.r_is_int.setText(_translate("self", "Целое?"))
        self.r_div.setText(_translate("self", "/"))
        self.p_label.setText(_translate("self", "Многочлены (полиномы)"))
        self.p_add.setText(_translate("self", "+"))
        self.p_mul_q.setText(_translate("self", "* q"))
        self.p_sub.setText(_translate("self", "-"))
        self.p_div.setText(_translate("self", "/"))
        self.p_high_c.setText(_translate("self", "Ст. коэффициент"))
        self.p_mul_xk.setText(_translate("self", "* x^k"))
        self.p_mul.setText(_translate("self", "*"))
        self.p_power.setText(_translate("self", "Степень"))
        self.p_nmr.setText(_translate("self", "Кр. корни\n"
                                              "в простые"))
        self.p_mod.setText(_translate("self", "%"))
        self.p_fac.setText(_translate("self", "НОД / НОК"))
        self.p_derivative.setText(_translate("self", "Производная"))
        self.p_gcf.setText(_translate("self", "НОД"))
        self.others.setTitle(_translate("self", "Другое"))
        self.classes.setTitle(_translate("self", "Классы"))

        # ВОЗМОЖНО стоит убрать action_2...? Нигде не используется
        # (вроде привязаны к label)

        self.to_wNatural.setText(_translate("self", "Натуральные числа"))
        self.to_wInteger.setText(_translate("self", "Целые числа"))
        self.to_wRational.setText(_translate("self", "Рациональные числа"))
        self.to_wPolynom.setText(_translate("self", "Полиномы (многочлены)"))
        self.help.setText("Помощь")
        self.about.setText("О проекте")

def application():
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()