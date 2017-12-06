from PyQt5.QtWidgets import QWidget, QFormLayout, QGridLayout, QPushButton, QLabel
from gui.lineedit import HashEdit, AmountEdit

class Send(QWidget):
    def handleMax(self):
        print("Handle max!")

    def handleSend(self):
        print("Handle send!")

    def handlePreview(self):
        print("Handle preview!")

    def handleClear(self):
        print("Handle clear!")

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

        # Padding to float buttons
        padding = QLabel("\t")
        padding.setFixedWidth(40)

        clearbutton = QPushButton("Clear")
        clearbutton.clicked.connect(self.handleClear)
        clearbutton.setFixedWidth(btnwidth)

        previewbutton = QPushButton("Preview")
        previewbutton.clicked.connect(self.handlePreview)
        previewbutton.setFixedWidth(btnwidth)

        sendbutton = QPushButton("Send")
        sendbutton.clicked.connect(self.handleSend)
        sendbutton.setFixedWidth(btnwidth)

        btnrow.addWidget(padding, 0, 0)
        btnrow.addWidget(clearbutton, 0, 1)
        btnrow.addWidget(previewbutton, 0, 2)
        btnrow.addWidget(sendbutton, 0, 3)

        layout.addRow("", btnrow)
        self.setLayout(layout)
