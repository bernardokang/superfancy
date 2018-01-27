# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SFT.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import DB_manager
#내가 만든 디비매니저 모듈을 임포트 한다



class Ui_Form(QtWidgets.QWidget):

    def __init__(self, database, tableName):
        QtWidgets.QWidget.__init__(self) #엑시멀코드 수정사항
        self.dbu = DB_manager.DatabaseUtility(database, tableName)
        self.setupUi(self) #셀프를 빼먹지 말것
        #여기 깔리는 순서가 상관이 있는지는 모르겠다마는
        self.UpdateTree()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(368, 125)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #푸시버튼 연결
        self.pushButton.clicked.connect(self.commit)








    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Super Facny Progress BAR"))
        self.label.setText(_translate("Form", "SUPER FANCY PROGRESS!"))
        self.pushButton.setText(_translate("Form", "COMMIT"))
        self.comboBox.setItemText(0, _translate("Form", "VFX LABEL"))
        self.comboBox.setItemText(1, _translate("Form", "TD LABEL"))
        self.pushButton_2.setText(_translate("Form", "MESSAGE"))

    #푸시버튼 설계
    def commit(self):
        self.dbu.addEntryToTable()
        self.UpdateTree()



    #업데이트 설계
    def UpdateTree(self):
        col = self.dbu.getColumns()
        table = self.dbu.getTable()


if __name__ == "__main__":
    import sys

    db = "IU_KISS"
    tableName = "PALME"
    import sys


    app = QtWidgets.QApplication(sys.argv)
    # Form = QtWidgets.QWidget()
    ui = Ui_Form(db, tableName)
    # ui.setupUi(Form)
    ui.show()
    sys.exit(app.exec_())

