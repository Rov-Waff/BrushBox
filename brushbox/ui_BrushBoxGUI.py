# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BrushBoxGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_BrushBoxGUI(object):
    def setupUi(self, BrushBoxGUI):
        if not BrushBoxGUI.objectName():
            BrushBoxGUI.setObjectName(u"BrushBoxGUI")
        BrushBoxGUI.resize(400, 300)
        self.verticalLayout = QVBoxLayout(BrushBoxGUI)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(BrushBoxGUI)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pte_token = QPlainTextEdit(BrushBoxGUI)
        self.pte_token.setObjectName(u"pte_token")

        self.horizontalLayout.addWidget(self.pte_token)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(BrushBoxGUI)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.pte_content = QPlainTextEdit(BrushBoxGUI)
        self.pte_content.setObjectName(u"pte_content")

        self.horizontalLayout_3.addWidget(self.pte_content)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(BrushBoxGUI)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_group_id = QLineEdit(BrushBoxGUI)
        self.le_group_id.setObjectName(u"le_group_id")

        self.horizontalLayout_2.addWidget(self.le_group_id)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(BrushBoxGUI)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.sb_count = QSpinBox(BrushBoxGUI)
        self.sb_count.setObjectName(u"sb_count")

        self.horizontalLayout_4.addWidget(self.sb_count)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_dojob = QPushButton(BrushBoxGUI)
        self.btn_dojob.setObjectName(u"btn_dojob")

        self.horizontalLayout_5.addWidget(self.btn_dojob)

        self.pb_process = QProgressBar(BrushBoxGUI)
        self.pb_process.setObjectName(u"pb_process")
        self.pb_process.setValue(0)

        self.horizontalLayout_5.addWidget(self.pb_process)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(BrushBoxGUI)

        QMetaObject.connectSlotsByName(BrushBoxGUI)
    # setupUi

    def retranslateUi(self, BrushBoxGUI):
        BrushBoxGUI.setWindowTitle(QCoreApplication.translate("BrushBoxGUI", u"BrushBox", None))
        self.label.setText(QCoreApplication.translate("BrushBoxGUI", u"Token", None))
        self.label_3.setText(QCoreApplication.translate("BrushBoxGUI", u"\u5185\u5bb9", None))
        self.label_2.setText(QCoreApplication.translate("BrushBoxGUI", u"\u7fa4ID", None))
        self.label_4.setText(QCoreApplication.translate("BrushBoxGUI", u"\u6b21\u6570", None))
        self.btn_dojob.setText(QCoreApplication.translate("BrushBoxGUI", u"\u8fdb\u884c", None))
    # retranslateUi
