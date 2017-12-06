from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QFormLayout, \
    QLineEdit, QHBoxLayout, QRadioButton, QLabel, QCheckBox, QMainWindow, QStyleOptionFrame, QStyle, QGridLayout, QPushButton
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from .tab.send import Send
from .tab.receive import Receive
from .tab.history import History

import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(400, 400, 900, 350)
        self.setMinimumSize(500, 300)
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
