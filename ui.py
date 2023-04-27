from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QtCore.QSize(600, 500))
        MainWindow.setMaximumSize(QtCore.QSize(600, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(88, 88, 88);")
        self.centralwidget.setObjectName("centralwidget")
        self.dirichleOrNeymanWidget = QtWidgets.QWidget(self.centralwidget)
        self.dirichleOrNeymanWidget.setGeometry(QtCore.QRect(310, 250, 260, 220))
        self.dirichleOrNeymanWidget.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.dirichleOrNeymanWidget.setObjectName("dirichleOrNeymanWidget")
        self.dirichleOptionButton = QtWidgets.QRadioButton(self.dirichleOrNeymanWidget)
        self.dirichleOptionButton.setGeometry(QtCore.QRect(20, 70, 16, 20))
        self.dirichleOptionButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.dirichleOptionButton.setText("")
        self.dirichleOptionButton.setChecked(True)
        self.dirichleOptionButton.setAutoExclusive(True)
        self.dirichleOptionButton.setObjectName("dirichleOptionButton")
        self.neymanOptionLabel = QtWidgets.QLabel(self.dirichleOrNeymanWidget)
        self.neymanOptionLabel.setGeometry(QtCore.QRect(40, 110, 180, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.neymanOptionLabel.setFont(font)
        self.neymanOptionLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.neymanOptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.neymanOptionLabel.setObjectName("neymanOptionLabel")
        self.dirichleOptionLabel = QtWidgets.QLabel(self.dirichleOrNeymanWidget)
        self.dirichleOptionLabel.setGeometry(QtCore.QRect(40, 50, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dirichleOptionLabel.setFont(font)
        self.dirichleOptionLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.dirichleOptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.dirichleOptionLabel.setObjectName("dirichleOptionLabel")
        self.neymanOptionButton = QtWidgets.QRadioButton(self.dirichleOrNeymanWidget)
        self.neymanOptionButton.setGeometry(QtCore.QRect(20, 130, 16, 20))
        self.neymanOptionButton.setAutoFillBackground(False)
        self.neymanOptionButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.neymanOptionButton.setText("")
        self.neymanOptionButton.setAutoExclusive(True)
        self.neymanOptionButton.setObjectName("neymanOptionButton")
        self.equationTypeWIdget = QtWidgets.QWidget(self.centralwidget)
        self.equationTypeWIdget.setGeometry(QtCore.QRect(310, 20, 260, 220))
        self.equationTypeWIdget.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.equationTypeWIdget.setObjectName("equationTypeWIdget")
        self.waveOptionButton = QtWidgets.QRadioButton(self.equationTypeWIdget)
        self.waveOptionButton.setGeometry(QtCore.QRect(20, 160, 16, 20))
        self.waveOptionButton.setAutoFillBackground(False)
        self.waveOptionButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.waveOptionButton.setText("")
        self.waveOptionButton.setChecked(True)
        self.waveOptionButton.setAutoExclusive(True)
        self.waveOptionButton.setObjectName("waveOptionButton")
        self.chooseEquationTypeLabel = QtWidgets.QLabel(self.equationTypeWIdget)
        self.chooseEquationTypeLabel.setGeometry(QtCore.QRect(10, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chooseEquationTypeLabel.setFont(font)
        self.chooseEquationTypeLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.chooseEquationTypeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.chooseEquationTypeLabel.setObjectName("chooseEquationTypeLabel")
        self.thermalConductivityOptionLabel = QtWidgets.QLabel(self.equationTypeWIdget)
        self.thermalConductivityOptionLabel.setGeometry(QtCore.QRect(40, 80, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thermalConductivityOptionLabel.setFont(font)
        self.thermalConductivityOptionLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.thermalConductivityOptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.thermalConductivityOptionLabel.setObjectName("thermalConductivityOptionLabel")
        self.waveOptionLabel = QtWidgets.QLabel(self.equationTypeWIdget)
        self.waveOptionLabel.setGeometry(QtCore.QRect(40, 140, 180, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.waveOptionLabel.setFont(font)
        self.waveOptionLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.waveOptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.waveOptionLabel.setObjectName("waveOptionLabel")
        self.thermalOptionButton = QtWidgets.QRadioButton(self.equationTypeWIdget)
        self.thermalOptionButton.setGeometry(QtCore.QRect(20, 100, 16, 20))
        self.thermalOptionButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.thermalOptionButton.setText("")
        self.thermalOptionButton.setChecked(False)
        self.thermalOptionButton.setObjectName("thermalOptionButton")
        self.inputVieldsWidget = QtWidgets.QWidget(self.centralwidget)
        self.inputVieldsWidget.setGeometry(QtCore.QRect(25, 20, 271, 351))
        self.inputVieldsWidget.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.inputVieldsWidget.setObjectName("inputVieldsWidget")
        self.inputTItle = QtWidgets.QLabel(self.inputVieldsWidget)
        self.inputTItle.setGeometry(QtCore.QRect(0, -1, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputTItle.setFont(font)
        self.inputTItle.setAcceptDrops(False)
        self.inputTItle.setAlignment(QtCore.Qt.AlignCenter)
        self.inputTItle.setObjectName("inputTItle")
        self.aLabel = QtWidgets.QLabel(self.inputVieldsWidget)
        self.aLabel.setGeometry(QtCore.QRect(20, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aLabel.setFont(font)
        self.aLabel.setObjectName("aLabel")
        self.aInput = QtWidgets.QLineEdit(self.inputVieldsWidget)
        self.aInput.setGeometry(QtCore.QRect(132, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.aInput.setFont(font)
        self.aInput.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.aInput.setObjectName("aInput")
        self.lInput = QtWidgets.QLineEdit(self.inputVieldsWidget)
        self.lInput.setGeometry(QtCore.QRect(132, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lInput.setFont(font)
        self.lInput.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.lInput.setObjectName("lInput")
        self.lLabel = QtWidgets.QLabel(self.inputVieldsWidget)
        self.lLabel.setGeometry(QtCore.QRect(20, 120, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lLabel.setFont(font)
        self.lLabel.setObjectName("lLabel")
        self.uInput = QtWidgets.QLineEdit(self.inputVieldsWidget)
        self.uInput.setGeometry(QtCore.QRect(132, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.uInput.setFont(font)
        self.uInput.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.uInput.setObjectName("uInput")
        self.uLabel = QtWidgets.QLabel(self.inputVieldsWidget)
        self.uLabel.setGeometry(QtCore.QRect(20, 180, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uLabel.setFont(font)
        self.uLabel.setObjectName("uLabel")
        self.heterogeneityInput = QtWidgets.QLineEdit(self.inputVieldsWidget)
        self.heterogeneityInput.setGeometry(QtCore.QRect(132, 240, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.heterogeneityInput.setFont(font)
        self.heterogeneityInput.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.heterogeneityInput.setObjectName("heterogeneityInput")
        self.heterogeneityLabel = QtWidgets.QLabel(self.inputVieldsWidget)
        self.heterogeneityLabel.setGeometry(QtCore.QRect(20, 240, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.heterogeneityLabel.setFont(font)
        self.heterogeneityLabel.setObjectName("heterogeneityLabel")
        self.waveEquationWidget = QtWidgets.QWidget(self.inputVieldsWidget)
        self.waveEquationWidget.setEnabled(True)
        self.waveEquationWidget.setGeometry(QtCore.QRect(19, 300, 231, 31))
        self.waveEquationWidget.setObjectName("waveEquationWidget")
        self.uDerivativeInput = QtWidgets.QLineEdit(self.waveEquationWidget)
        self.uDerivativeInput.setEnabled(True)
        self.uDerivativeInput.setGeometry(QtCore.QRect(112, 0, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.uDerivativeInput.setFont(font)
        self.uDerivativeInput.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.uDerivativeInput.setObjectName("uDerivativeInput")
        self.uDerivativeLabel = QtWidgets.QLabel(self.waveEquationWidget)
        self.uDerivativeLabel.setGeometry(QtCore.QRect(0, 0, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uDerivativeLabel.setFont(font)
        self.uDerivativeLabel.setObjectName("uDerivativeLabel")
        self.waveEquationWidget.raise_()
        self.inputTItle.raise_()
        self.aLabel.raise_()
        self.aInput.raise_()
        self.lInput.raise_()
        self.lLabel.raise_()
        self.uInput.raise_()
        self.uLabel.raise_()
        self.heterogeneityInput.raise_()
        self.heterogeneityLabel.raise_()
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(25, 395, 271, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.calculateButton.setFont(font)
        self.calculateButton.setStyleSheet("background-color: rgb(90, 93, 129);")
        self.calculateButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslate_ui(MainWindow)
        self.thermalOptionButton.clicked.connect(self.waveEquationWidget.hide) # type: ignore
        self.waveOptionButton.clicked.connect(self.waveEquationWidget.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Уравнения мат физики"))
        self.neymanOptionLabel.setText(_translate("MainWindow", "Нейман"))
        self.dirichleOptionLabel.setText(_translate("MainWindow", "Дирихле"))
        self.chooseEquationTypeLabel.setText(_translate("MainWindow", "Выберите тип уравнения"))
        self.thermalConductivityOptionLabel.setText(_translate("MainWindow", "Теплопроводность"))
        self.waveOptionLabel.setText(_translate("MainWindow", "Волновое"))
        self.inputTItle.setText(_translate("MainWindow", "Введите условие задачи"))
        self.aLabel.setText(_translate("MainWindow", "A^2"))
        self.lLabel.setText(_translate("MainWindow", "L"))
        self.uLabel.setText(_translate("MainWindow", "u(x, 0)"))
        self.heterogeneityLabel.setText(_translate("MainWindow", "F(x, t)"))
        self.uDerivativeLabel.setText(_translate("MainWindow", "du/dx (x, 0)"))
        self.calculateButton.setText(_translate("MainWindow", "Вычислить"))