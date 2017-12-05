from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QFormLayout, \
    QLineEdit, QHBoxLayout, QRadioButton, QLabel, QCheckBox, QMainWindow, QStyleOptionFrame, QStyle, QGridLayout, QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from .lineedit import HashEdit, AmountEdit

import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(400, 400, 900, 400)
        self.setWindowTitle("Electrum IOTA Wallet")
        self.setWindowIcon(QIcon('icons/logo.png'))
        self.pane = TabbedPane(self)
        self.setCentralWidget(self.pane)
        self.show()


class TabbedPane(QTabWidget):

    def __init__(self, parent=None):
        super(TabbedPane, self).__init__(parent)
        self.historytab = QWidget()
        self.sendtab = QWidget()
        self.receivetab = QWidget()

        self.addTab(self.historytab, QIcon('icons/tab_history.png'), "History")
        self.addTab(self.sendtab, QIcon('icons/tab_send.png'), "Send")
        self.addTab(self.receivetab, QIcon('icons/tab_receive.png'), "Receive")
        self.historytabUI()
        self.sendtabUI()
        self.receivetabUI()

    def historytabUI(self):
        layout = QFormLayout()

        self.setTabText(0, "History")
        self.historytab.setLayout(layout)

    def sendtabUI(self):
        layout = QFormLayout()
        sendObj = Send()
        layout.addWidget(sendObj)
        self.setTabText(1, "Send")
        self.sendtab.setLayout(layout)

    def receivetabUI(self):
        layout = QHBoxLayout()

        self.setTabText(2, "Receive")
        self.receivetab.setLayout(layout)


class History(QWidget):
    def __init__(self, parent=None):
        pass

class Send(QWidget):
    def handleMax(self):
        print("Handle max!")

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        layout = QFormLayout()
        layout.setSpacing(12)
        address = HashEdit(90)
        tag = HashEdit(27)

        layout.addRow("Pay to", address)
        layout.addRow("Tag", tag)
        row1 = QGridLayout()
        row1.addWidget(AmountEdit(lambda: 'IOTA'), 0, 0)

        maxbutton = QPushButton("Max")
        maxbutton.clicked.connect(self.handleMax)
        maxbutton.setFixedWidth(100)
        row1.addWidget(maxbutton, 0, 1)



        layout.addRow("Amount", row1)

        btnrow = QGridLayout()
        btnwidth = 80

        padding = QLabel("\t")
        padding.setFixedWidth(40)

        clearbutton = QPushButton("Clear")
        clearbutton.setFixedWidth(btnwidth)

        previewbutton = QPushButton("Preview")
        previewbutton.setFixedWidth(btnwidth)

        sendbutton = QPushButton("Send")
        sendbutton.setFixedWidth(btnwidth)

        btnrow.addWidget(padding, 0, 0)
        btnrow.addWidget(clearbutton, 0, 1)
        btnrow.addWidget(previewbutton, 0, 2)
        btnrow.addWidget(sendbutton, 0, 3)

        layout.addRow("", btnrow)
        self.setLayout(layout)




class Recieve(QWidget):
    def __init__(self, parent=None):
        pass
