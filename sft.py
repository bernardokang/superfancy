# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SFT.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import DB_manager, DB_manager_exr
#내가 만든 디비매니저 모듈을 임포트 한다


#딕타라는 딕트를 만들고 과목명이 ang인 경우 해시키값으로 ak를 쓰도록 하겠다
DICTA = {'subjectName':'ak', 'TD LABEL': 'pr44'}

#이렇게 새로운 모듈을 만들고(이것의 역할은 mysql 데이타베이스를 읽어 오는 것이다) 인스턴스로 접근 했다
print(DB_manager_exr.cnxor.mane(DICTA['subjectName']))



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
        self.progressBar.setProperty("value",*(DB_manager_exr.cnxor.mane(DICTA['subjectName'])))
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
        #이건 내가 직접 큐티 다큐멍 보고서 찾은 내용인데 플레이스 홀더 넣기!
        self.lineEdit.setPlaceholderText('add commit message')
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
        self.pushButton_2.clicked.connect(self.commit2)


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
        #(커밋메시지)텍스트도 같이 보낸다. 공란일 경우 ''가 보내진다
        text = self.lineEdit.text()
        self.dbu.addEntryToTable(text)
        self.UpdateTree()
        #메시지를 보냇으면 리셋해야지 또 쓰겡
        self.lineEdit.clear()


    #업데이트 설계
    def UpdateTree(self):
        col = self.dbu.getColumns()
        table = self.dbu.getTable()
        #큐티 다큐멘테이션을 참고해서 리셋을 찾았고
        self.progressBar.reset()
        #리셋후에는 값을 씌워줘야곘지? 이런 간단한 메카니점이었다니!
        self.progressBar.setProperty("value", *(DB_manager_exr.cnxor.mane(DICTA['subjectName'])))


    #탭에 선택된 텍스트를 출력해주옵니다
    # def commit2(self):
    #     self.text = str(self.comboBox.currentText())
    #     print(self.text)
    #     print(DICTA[self.text]) #딕트통신도 가능하다
    #     self.message = self.lineEdit.text()
    #     print(self.message)
    #     self.lineEdit.clear() #간단한 업데이트 기능!(초기화)







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

