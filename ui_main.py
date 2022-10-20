# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 560)
        MainWindow.setMinimumSize(QSize(940, 560))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.styleSheet.setFont(font1)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/logo.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 14"
                        "7, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, "
                        "147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/cil-bell.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px "
                        "solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid;"
                        " border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255,"
                        " 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(3"
                        "3, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb("
                        "255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollB"
                        "ar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol"
                        "-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-i"
                        "mage: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-po"
                        "sition: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 1"
                        "0px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton"
                        " {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setBold(True)
        font2.setItalic(False)
        self.titleLeftApp.setFont(font2)
        self.titleLeftApp.setStyleSheet(u"font: bold 14px;")
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleLeftDescription.setFont(font3)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 10, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font1)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font1)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font1)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-settings.png);")

        self.verticalLayout_8.addWidget(self.btn_new)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font1)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-bell.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setSizeIncrement(QSize(0, 0))
        self.extraLeftBox.setStyleSheet(u"")
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setSizeIncrement(QSize(0, 0))
        self.extraContent.setStyleSheet(u"")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font1)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font1)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font1)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setStyleSheet(u"")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.extraCenter)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.scrollArea = QScrollArea(self.extraCenter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet(u"background: transparent;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 51, 322))
        self.scrollAreaWidgetContents.setAutoFillBackground(False)
        self.scrollAreaWidgetContents.setStyleSheet(u"background: transparent;")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"background: transparent;")

        self.horizontalLayout_11.addWidget(self.textBrowser)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_10.addWidget(self.scrollArea)


        self.verticalLayout_12.addWidget(self.extraCenter)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFont(font1)
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(True)
        font4.setItalic(False)
        self.titleRightInfo.setFont(font4)
        self.titleRightInfo.setLayoutDirection(Qt.LeftToRight)
        self.titleRightInfo.setStyleSheet(u"font: bold 16px;")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font5)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setLayoutDirection(Qt.LeftToRight)
        self.home.setStyleSheet(u"")
        self.horizontalLayout_14 = QHBoxLayout(self.home)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.scrollArea_2 = QScrollArea(self.home)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 28, 17))
        self.horizontalLayout_7 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pic_preshow_label = QLabel(self.scrollAreaWidgetContents_2)
        self.pic_preshow_label.setObjectName(u"pic_preshow_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pic_preshow_label.sizePolicy().hasHeightForWidth())
        self.pic_preshow_label.setSizePolicy(sizePolicy3)
        self.pic_preshow_label.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.pic_preshow_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.pic_preshow_label)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_14.addWidget(self.scrollArea_2)

        self.home_info = QFrame(self.home)
        self.home_info.setObjectName(u"home_info")
        self.home_info.setFrameShape(QFrame.StyledPanel)
        self.home_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.home_info)
        self.verticalLayout_22.setSpacing(90)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.input_way = QGroupBox(self.home_info)
        self.input_way.setObjectName(u"input_way")
        self.verticalLayout = QVBoxLayout(self.input_way)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filePathlineEdit = QLineEdit(self.input_way)
        self.filePathlineEdit.setObjectName(u"filePathlineEdit")
        self.filePathlineEdit.setMinimumSize(QSize(0, 30))
        self.filePathlineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout.addWidget(self.filePathlineEdit)

        self.btn_home_open = QPushButton(self.input_way)
        self.btn_home_open.setObjectName(u"btn_home_open")
        self.btn_home_open.setMinimumSize(QSize(150, 30))
        self.btn_home_open.setFont(font1)
        self.btn_home_open.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home_open.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home_open.setIcon(icon3)

        self.verticalLayout.addWidget(self.btn_home_open)

        self.btn_home_shot = QPushButton(self.input_way)
        self.btn_home_shot.setObjectName(u"btn_home_shot")
        self.btn_home_shot.setMinimumSize(QSize(150, 30))
        self.btn_home_shot.setFont(font1)
        self.btn_home_shot.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home_shot.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-camera.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home_shot.setIcon(icon4)

        self.verticalLayout.addWidget(self.btn_home_shot)

        self.btn_home_show = QPushButton(self.input_way)
        self.btn_home_show.setObjectName(u"btn_home_show")
        self.btn_home_show.setMinimumSize(QSize(150, 30))
        self.btn_home_show.setFont(font1)
        self.btn_home_show.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home_show.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-satelite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home_show.setIcon(icon5)

        self.verticalLayout.addWidget(self.btn_home_show)


        self.verticalLayout_22.addWidget(self.input_way)

        self.pic_info = QGroupBox(self.home_info)
        self.pic_info.setObjectName(u"pic_info")
        self.pic_info.setStyleSheet(u"")
        self.pic_info.setFlat(False)
        self.pic_info.setCheckable(False)
        self.verticalLayout_23 = QVBoxLayout(self.pic_info)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.home_info_pix = QFrame(self.pic_info)
        self.home_info_pix.setObjectName(u"home_info_pix")
        self.home_info_pix.setFrameShape(QFrame.StyledPanel)
        self.home_info_pix.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.home_info_pix)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.home_info_label2_pix = QLabel(self.home_info_pix)
        self.home_info_label2_pix.setObjectName(u"home_info_label2_pix")
        self.home_info_label2_pix.setMinimumSize(QSize(0, 30))
        self.home_info_label2_pix.setFont(font4)
        self.home_info_label2_pix.setStyleSheet(u"font: bold 13px;")

        self.horizontalLayout_6.addWidget(self.home_info_label2_pix)

        self.home_info_label2_pix_output = QLabel(self.home_info_pix)
        self.home_info_label2_pix_output.setObjectName(u"home_info_label2_pix_output")
        self.home_info_label2_pix_output.setMinimumSize(QSize(0, 30))
        self.home_info_label2_pix_output.setFont(font4)
        self.home_info_label2_pix_output.setStyleSheet(u"font: bold 13px;")

        self.horizontalLayout_6.addWidget(self.home_info_label2_pix_output)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_23.addWidget(self.home_info_pix)

        self.home_info_size = QFrame(self.pic_info)
        self.home_info_size.setObjectName(u"home_info_size")
        self.home_info_size.setFrameShape(QFrame.StyledPanel)
        self.home_info_size.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.home_info_size)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.home_info_label2_size = QLabel(self.home_info_size)
        self.home_info_label2_size.setObjectName(u"home_info_label2_size")
        self.home_info_label2_size.setMinimumSize(QSize(0, 30))
        self.home_info_label2_size.setFont(font4)
        self.home_info_label2_size.setStyleSheet(u"font: bold 13px;")

        self.horizontalLayout_8.addWidget(self.home_info_label2_size)

        self.home_info_label2_size_output = QLabel(self.home_info_size)
        self.home_info_label2_size_output.setObjectName(u"home_info_label2_size_output")
        self.home_info_label2_size_output.setEnabled(True)
        self.home_info_label2_size_output.setMinimumSize(QSize(0, 30))
        self.home_info_label2_size_output.setFont(font4)
        self.home_info_label2_size_output.setStyleSheet(u"font: bold 13px;")

        self.horizontalLayout_8.addWidget(self.home_info_label2_size_output)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout_23.addWidget(self.home_info_size)


        self.verticalLayout_22.addWidget(self.pic_info)

        self.verticalLayout_22.setStretch(0, 1)
        self.verticalLayout_22.setStretch(1, 1)

        self.horizontalLayout_14.addWidget(self.home_info)

        self.horizontalLayout_14.setStretch(0, 2)
        self.horizontalLayout_14.setStretch(1, 1)
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.groupBox = QGroupBox(self.widgets)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 111, 201))
        self.verticalLayout_17 = QVBoxLayout(self.groupBox)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.btn_widgets_resize = QPushButton(self.groupBox)
        self.btn_widgets_resize.setObjectName(u"btn_widgets_resize")
        self.btn_widgets_resize.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_17.addWidget(self.btn_widgets_resize)

        self.btn_widgets_hist = QPushButton(self.groupBox)
        self.btn_widgets_hist.setObjectName(u"btn_widgets_hist")
        self.btn_widgets_hist.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_17.addWidget(self.btn_widgets_hist)

        self.btn_widgets_histequal = QPushButton(self.groupBox)
        self.btn_widgets_histequal.setObjectName(u"btn_widgets_histequal")
        self.btn_widgets_histequal.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_17.addWidget(self.btn_widgets_histequal)

        self.groupBox_2 = QGroupBox(self.widgets)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(340, 10, 111, 201))
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_16.setSpacing(15)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, -1, 9)
        self.btn_widgets_mean_filtering = QPushButton(self.groupBox_2)
        self.btn_widgets_mean_filtering.setObjectName(u"btn_widgets_mean_filtering")
        self.btn_widgets_mean_filtering.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_16.addWidget(self.btn_widgets_mean_filtering)

        self.btn_widgets_gauss_filtering = QPushButton(self.groupBox_2)
        self.btn_widgets_gauss_filtering.setObjectName(u"btn_widgets_gauss_filtering")
        self.btn_widgets_gauss_filtering.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_16.addWidget(self.btn_widgets_gauss_filtering)

        self.btn_widgets_median_filtering = QPushButton(self.groupBox_2)
        self.btn_widgets_median_filtering.setObjectName(u"btn_widgets_median_filtering")
        self.btn_widgets_median_filtering.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_16.addWidget(self.btn_widgets_median_filtering)

        self.groupBox_3 = QGroupBox(self.widgets)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(160, 10, 131, 421))
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_10.setSpacing(15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btn_widgets_gray = QPushButton(self.groupBox_3)
        self.btn_widgets_gray.setObjectName(u"btn_widgets_gray")
        self.btn_widgets_gray.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_10.addWidget(self.btn_widgets_gray)

        self.btn_widgets_Thresholding = QPushButton(self.groupBox_3)
        self.btn_widgets_Thresholding.setObjectName(u"btn_widgets_Thresholding")
        self.btn_widgets_Thresholding.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_10.addWidget(self.btn_widgets_Thresholding)

        self.btn_widgets_flip = QPushButton(self.groupBox_3)
        self.btn_widgets_flip.setObjectName(u"btn_widgets_flip")
        self.btn_widgets_flip.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_10.addWidget(self.btn_widgets_flip)

        self.btn_widgets_log = QPushButton(self.groupBox_3)
        self.btn_widgets_log.setObjectName(u"btn_widgets_log")
        self.btn_widgets_log.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_10.addWidget(self.btn_widgets_log)

        self.btn_widgets_gamma = QPushButton(self.groupBox_3)
        self.btn_widgets_gamma.setObjectName(u"btn_widgets_gamma")
        self.btn_widgets_gamma.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_10.addWidget(self.btn_widgets_gamma)

        self.btn_widgets_contrast_stretch = QPushButton(self.groupBox_3)
        self.btn_widgets_contrast_stretch.setObjectName(u"btn_widgets_contrast_stretch")
        self.btn_widgets_contrast_stretch.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_10.addWidget(self.btn_widgets_contrast_stretch)

        self.btn_widgets_8bits_layering = QPushButton(self.groupBox_3)
        self.btn_widgets_8bits_layering.setObjectName(u"btn_widgets_8bits_layering")
        self.btn_widgets_8bits_layering.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_10.addWidget(self.btn_widgets_8bits_layering)

        self.btn_widgets_test = QPushButton(self.widgets)
        self.btn_widgets_test.setObjectName(u"btn_widgets_test")
        self.btn_widgets_test.setGeometry(QRect(730, 370, 91, 31))
        self.btn_widgets_test.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")
        self.groupBox_4 = QGroupBox(self.widgets)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(20, 220, 111, 211))
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.btn_widgets_pepper_and_salt = QPushButton(self.groupBox_4)
        self.btn_widgets_pepper_and_salt.setObjectName(u"btn_widgets_pepper_and_salt")
        self.btn_widgets_pepper_and_salt.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_18.addWidget(self.btn_widgets_pepper_and_salt)

        self.btn_widgets_gauss_noisy = QPushButton(self.groupBox_4)
        self.btn_widgets_gauss_noisy.setObjectName(u"btn_widgets_gauss_noisy")
        self.btn_widgets_gauss_noisy.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_18.addWidget(self.btn_widgets_gauss_noisy)

        self.btn_widgets_poisson_noisy = QPushButton(self.groupBox_4)
        self.btn_widgets_poisson_noisy.setObjectName(u"btn_widgets_poisson_noisy")
        self.btn_widgets_poisson_noisy.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_18.addWidget(self.btn_widgets_poisson_noisy)

        self.btn_widgets_speckle_noisy = QPushButton(self.groupBox_4)
        self.btn_widgets_speckle_noisy.setObjectName(u"btn_widgets_speckle_noisy")
        self.btn_widgets_speckle_noisy.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.verticalLayout_18.addWidget(self.btn_widgets_speckle_noisy)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.horizontalLayout_9 = QHBoxLayout(self.new_page)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tabWidget = QTabWidget(self.new_page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background: rgb(40,44,52);\n"
"border: 0px;")
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.tab_general.setStyleSheet(u"background: rgb(40,44,52);\n"
"border: 0px;")
        self.verticalLayout_25 = QVBoxLayout(self.tab_general)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(9, 30, 10, 0)
        self.frame = QFrame(self.tab_general)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background: transparent")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setSpacing(12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, -1, 20, -1)
        self.set_label_1 = QLabel(self.frame)
        self.set_label_1.setObjectName(u"set_label_1")
        self.set_label_1.setFont(font4)
        self.set_label_1.setStyleSheet(u"font: bold 15px;")

        self.horizontalLayout_12.addWidget(self.set_label_1)

        self.set_file_svae_path = QLineEdit(self.frame)
        self.set_file_svae_path.setObjectName(u"set_file_svae_path")
        self.set_file_svae_path.setMinimumSize(QSize(0, 30))
        self.set_file_svae_path.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_12.addWidget(self.set_file_svae_path)


        self.verticalLayout_25.addWidget(self.frame)

        self.frame_2 = QFrame(self.tab_general)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background: transparent")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_13.setSpacing(12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(20, -1, 20, -1)
        self.set_label_2 = QLabel(self.frame_2)
        self.set_label_2.setObjectName(u"set_label_2")
        self.set_label_2.setFont(font4)
        self.set_label_2.setStyleSheet(u"font: bold 15px;")

        self.horizontalLayout_13.addWidget(self.set_label_2)

        self.set_file_open_path = QLineEdit(self.frame_2)
        self.set_file_open_path.setObjectName(u"set_file_open_path")
        self.set_file_open_path.setMinimumSize(QSize(0, 30))
        self.set_file_open_path.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_13.addWidget(self.set_file_open_path)


        self.verticalLayout_25.addWidget(self.frame_2)

        self.frame_13 = QFrame(self.tab_general)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background: transparent")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.btn_settings_reset_1 = QPushButton(self.frame_13)
        self.btn_settings_reset_1.setObjectName(u"btn_settings_reset_1")
        self.btn_settings_reset_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings_reset_1.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.horizontalLayout_24.addWidget(self.btn_settings_reset_1)

        self.btn_settings_save = QPushButton(self.frame_13)
        self.btn_settings_save.setObjectName(u"btn_settings_save")
        self.btn_settings_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings_save.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.horizontalLayout_24.addWidget(self.btn_settings_save)


        self.verticalLayout_25.addWidget(self.frame_13)

        self.verticalLayout_25.setStretch(0, 4)
        self.verticalLayout_25.setStretch(1, 4)
        self.verticalLayout_25.setStretch(2, 1)
        self.tabWidget.addTab(self.tab_general, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"background: rgb(40,44,52);\n"
"border: 0px;")
        self.verticalLayout_24 = QVBoxLayout(self.tab_2)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 30, 10, 0)
        self.frame_11 = QFrame(self.tab_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background: transparent")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.groupBox_6 = QGroupBox(self.frame_11)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"background: transparent")
        self.verticalLayout_19 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_3 = QFrame(self.groupBox_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background: transparent")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_15.setSpacing(12)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(20, -1, 20, -1)
        self.set_noisy_ratio_label = QLabel(self.frame_3)
        self.set_noisy_ratio_label.setObjectName(u"set_noisy_ratio_label")
        self.set_noisy_ratio_label.setFont(font4)
        self.set_noisy_ratio_label.setStyleSheet(u"font: bold 15px;")

        self.horizontalLayout_15.addWidget(self.set_noisy_ratio_label)

        self.set_noisy_ratio = QLineEdit(self.frame_3)
        self.set_noisy_ratio.setObjectName(u"set_noisy_ratio")
        self.set_noisy_ratio.setMinimumSize(QSize(0, 30))
        self.set_noisy_ratio.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_15.addWidget(self.set_noisy_ratio)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 1)

        self.verticalLayout_19.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background: transparent")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_16.setSpacing(12)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(20, -1, 20, -1)
        self.set_pepper_vs_salt_label = QLabel(self.frame_4)
        self.set_pepper_vs_salt_label.setObjectName(u"set_pepper_vs_salt_label")
        self.set_pepper_vs_salt_label.setFont(font4)
        self.set_pepper_vs_salt_label.setStyleSheet(u"font: bold 15px;")

        self.horizontalLayout_16.addWidget(self.set_pepper_vs_salt_label)

        self.set_pepper_vs_salt = QLineEdit(self.frame_4)
        self.set_pepper_vs_salt.setObjectName(u"set_pepper_vs_salt")
        self.set_pepper_vs_salt.setMinimumSize(QSize(0, 30))
        self.set_pepper_vs_salt.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_16.addWidget(self.set_pepper_vs_salt)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 1)

        self.verticalLayout_19.addWidget(self.frame_4)


        self.horizontalLayout_21.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.frame_11)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"background: transparent")
        self.verticalLayout_21 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_7 = QFrame(self.groupBox_7)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background: transparent")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_19.setSpacing(12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(20, -1, 20, -1)
        self.set_poisson_lambda_label = QLabel(self.frame_7)
        self.set_poisson_lambda_label.setObjectName(u"set_poisson_lambda_label")
        self.set_poisson_lambda_label.setFont(font4)
        self.set_poisson_lambda_label.setStyleSheet(u"font: bold 15px;")
        self.set_poisson_lambda_label.setTextFormat(Qt.AutoText)

        self.horizontalLayout_19.addWidget(self.set_poisson_lambda_label)

        self.set_poisson_lambda = QLineEdit(self.frame_7)
        self.set_poisson_lambda.setObjectName(u"set_poisson_lambda")
        self.set_poisson_lambda.setMinimumSize(QSize(0, 30))
        self.set_poisson_lambda.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_19.addWidget(self.set_poisson_lambda)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 1)

        self.verticalLayout_21.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.groupBox_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background: transparent")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_20.setSpacing(12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(20, -1, 20, -1)

        self.verticalLayout_21.addWidget(self.frame_8)

        self.verticalLayout_21.setStretch(0, 1)
        self.verticalLayout_21.setStretch(1, 1)

        self.horizontalLayout_21.addWidget(self.groupBox_7)

        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 1)

        self.verticalLayout_24.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.tab_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background: transparent")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.groupBox_5 = QGroupBox(self.frame_12)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"background: transparent")
        self.groupBox_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_20 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_5 = QFrame(self.groupBox_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background: transparent")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_17.setSpacing(12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(20, -1, 20, -1)
        self.set_guass_mean_label = QLabel(self.frame_5)
        self.set_guass_mean_label.setObjectName(u"set_guass_mean_label")
        self.set_guass_mean_label.setFont(font4)
        self.set_guass_mean_label.setStyleSheet(u"font: bold 15px;")

        self.horizontalLayout_17.addWidget(self.set_guass_mean_label)

        self.set_guass_mean = QLineEdit(self.frame_5)
        self.set_guass_mean.setObjectName(u"set_guass_mean")
        self.set_guass_mean.setMinimumSize(QSize(0, 30))
        self.set_guass_mean.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_17.addWidget(self.set_guass_mean)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 1)

        self.verticalLayout_20.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.groupBox_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background: transparent")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_18.setSpacing(12)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(20, -1, 20, -1)
        self.set_guass_sigma_label = QLabel(self.frame_6)
        self.set_guass_sigma_label.setObjectName(u"set_guass_sigma_label")
        self.set_guass_sigma_label.setFont(font4)
        self.set_guass_sigma_label.setStyleSheet(u"font: bold 15px;")

        self.horizontalLayout_18.addWidget(self.set_guass_sigma_label)

        self.set_guass_sigma = QLineEdit(self.frame_6)
        self.set_guass_sigma.setObjectName(u"set_guass_sigma")
        self.set_guass_sigma.setMinimumSize(QSize(0, 30))
        self.set_guass_sigma.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_18.addWidget(self.set_guass_sigma)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 1)

        self.verticalLayout_20.addWidget(self.frame_6)

        self.verticalLayout_20.setStretch(0, 1)
        self.verticalLayout_20.setStretch(1, 1)

        self.horizontalLayout_22.addWidget(self.groupBox_5)

        self.frame_10 = QFrame(self.frame_12)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background: transparent")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.frame_10)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 1)

        self.verticalLayout_24.addWidget(self.frame_12)

        self.frame_9 = QFrame(self.tab_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background: transparent")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.btn_settings_reset_2 = QPushButton(self.frame_9)
        self.btn_settings_reset_2.setObjectName(u"btn_settings_reset_2")
        self.btn_settings_reset_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings_reset_2.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.horizontalLayout_23.addWidget(self.btn_settings_reset_2)

        self.btn_settings_save_2 = QPushButton(self.frame_9)
        self.btn_settings_save_2.setObjectName(u"btn_settings_save_2")
        self.btn_settings_save_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings_save_2.setStyleSheet(u"border-radius:7px;\n"
"background-color: rgb(52, 59, 72);\n"
"")

        self.horizontalLayout_23.addWidget(self.btn_settings_save_2)


        self.verticalLayout_24.addWidget(self.frame_9)

        self.verticalLayout_24.setStretch(0, 4)
        self.verticalLayout_24.setStretch(1, 4)
        self.verticalLayout_24.setStretch(2, 1)
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_9.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font1)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font1)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font1)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyImage Helper", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u77e5\u9053\u5199\u5565", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Help", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u5b9a", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u5b9a", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u5b9a", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\" bgcolor=\"#2c313a\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyIamge Helper</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600; color:#ff79c6;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-"
                        "size:11pt; color:#ffffff;\">\u5de6\u4fa7\u4e3a\u5207\u6362\u9875\u9762\u680f\uff0c\u4ece\u4e0a\u5230\u4e0b\u5206\u522b\u4e3a\u663e\u793a\u540d\u79f0(</span><span style=\" font-size:11pt; color:#ffaaff;\">Hide</span><span style=\" font-size:11pt; color:#ffffff;\">)\uff0c\u4e3b\u9875(</span><span style=\" font-size:11pt; color:#ffaaff;\">Home Page</span><span style=\" font-size:11pt; color:#ffffff;\">)\uff0c\u529f\u80fd\u9875(</span><span style=\" font-size:11pt; color:#ffaaff;\">Widget Page</span><span style=\" font-size:11pt; color:#ffffff;\">)\uff0c\u8bbe\u7f6e\u9875(</span><span style=\" font-size:11pt; color:#ffaaff;\">Setting Page</span><span style=\" font-size:11pt; color:#ffffff;\">)</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -"
                        "qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffaaff;\">Home Page</span><span style=\" font-size:11pt; color:#ffffff;\">\u53ef\u4ee5\u9884\u89c8\u56fe\u7247\uff0c\u9009\u62e9\u6587\u4ef6\u6216\u8005\u4f7f\u7528\u6444\u50cf\u5934\u62cd\u6444</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffaaff;\">Widget Page</span><span style=\" font-size:11pt; color:#ffffff;\">\u53ef\u4ee5\u5bf9\u56fe\u50cf\u8fdb\u884c\u64cd\u4f5c\uff0c\u7ed3\u679c\u4f1a\u4ee5\u5f39\u7a97\u7684\u5f62\u5f0f\u663e\u793a</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#ffffff;\">\u5728\u5f39\u7a97\u7684\u7a97\u53e3\u4e0b\u6309</span><span style=\" font-size:11pt; color:#ffaaff;\">ESC</span><span style=\" font-size:11pt; color:#ffffff;\">\u53ef\u4ee5\u5173\u95ed\u6240\u6709\u7a97\u53e3\uff0c\u6309</span><span style=\" font-size:11pt; color:#ffaaff;\">q</span><span style=\" font-size:11pt; color:#ffffff;\">\u53ef\u4ee5\u5173\u95ed\u5f53\u524d\u7a97\u53e3\uff0c\u6309</span><span style=\" font-size:11pt; color:#ffaaff;\">s</span><span style=\" font-size:11pt; color:#ffffff;\">\u53ef\u4ee5\u4fdd\u5b58\u56fe\u7247,\u6309</span><span style=\" font-size:11pt; color:#ffaaff;\">h</span><span style=\" font-size:11pt; color:#ffffff;\">\u53ef\u4ee5\u5c06\u5f53\u524d\u56fe\u7247\u8f6c\u79fb\u5230home page\u9884\u89c8</span></p></body></"
                        "html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"PyImage Helper", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.pic_preshow_label.setText("")
        self.input_way.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u65b9\u5f0f", None))
        self.filePathlineEdit.setText("")
        self.filePathlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84\u5c55\u793a", None))
        self.btn_home_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.btn_home_shot.setText(QCoreApplication.translate("MainWindow", u"Shot ", None))
        self.btn_home_show.setText(QCoreApplication.translate("MainWindow", u"Show", None))
        self.pic_info.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u4fe1\u606f", None))
        self.home_info_label2_pix.setText(QCoreApplication.translate("MainWindow", u"\u50cf\u7d20\uff1a", None))
        self.home_info_label2_pix_output.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))
        self.home_info_label2_size.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f\uff1a", None))
        self.home_info_label2_size_output.setText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u64cd\u4f5c", None))
        self.btn_widgets_resize.setText(QCoreApplication.translate("MainWindow", u"\u7f29\u653e", None))
        self.btn_widgets_hist.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u76f4\u65b9\u56fe", None))
        self.btn_widgets_histequal.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u65b9\u56fe\u5747\u8861\u5316", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u7a7a\u95f4\u6ee4\u6ce2", None))
        self.btn_widgets_mean_filtering.setText(QCoreApplication.translate("MainWindow", u"\u5747\u503c\u6ee4\u6ce2", None))
        self.btn_widgets_gauss_filtering.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u6ee4\u6ce2", None))
        self.btn_widgets_median_filtering.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u503c\u6ee4\u6ce2", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7070\u5ea6\u53d8\u6362", None))
        self.btn_widgets_gray.setText(QCoreApplication.translate("MainWindow", u"\u7070\u5ea6\u5316", None))
        self.btn_widgets_Thresholding.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\u503c\u5316", None))
        self.btn_widgets_flip.setText(QCoreApplication.translate("MainWindow", u"\u7070\u5ea6\u53cd\u8f6c", None))
        self.btn_widgets_log.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u6570\u53d8\u6362", None))
        self.btn_widgets_gamma.setText(QCoreApplication.translate("MainWindow", u"\u4f3d\u9a6c\u77eb\u6b63", None))
        self.btn_widgets_contrast_stretch.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u6bd4\u5ea6\u62c9\u4f38", None))
        self.btn_widgets_8bits_layering.setText(QCoreApplication.translate("MainWindow", u"8\u6bd4\u7279\u5206\u5c42", None))
        self.btn_widgets_test.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u6309\u94ae", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u566a\u58f0", None))
        self.btn_widgets_pepper_and_salt.setText(QCoreApplication.translate("MainWindow", u"\u6912\u76d0\u566a\u58f0", None))
        self.btn_widgets_gauss_noisy.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u566a\u58f0", None))
        self.btn_widgets_poisson_noisy.setText(QCoreApplication.translate("MainWindow", u"\u6cca\u677e\u566a\u58f0", None))
        self.btn_widgets_speckle_noisy.setText(QCoreApplication.translate("MainWindow", u"\u6563\u6591\u566a\u58f0", None))
        self.set_label_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u9ed8\u8ba4\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.set_file_svae_path.setText("")
        self.set_file_svae_path.setPlaceholderText("")
        self.set_label_2.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u9ed8\u8ba4\u6253\u5f00\u8def\u5f84\uff1a", None))
        self.set_file_open_path.setText("")
        self.set_file_open_path.setPlaceholderText("")
        self.btn_settings_reset_1.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.btn_settings_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8bbe\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), QCoreApplication.translate("MainWindow", u"\u901a\u7528\u8bbe\u7f6e", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u6912\u76d0\u566a\u58f0", None))
        self.set_noisy_ratio_label.setText(QCoreApplication.translate("MainWindow", u"\u566a\u58f0\u50cf\u7d20\u6bd4\u4f8b\uff1a", None))
        self.set_noisy_ratio.setText("")
        self.set_noisy_ratio.setPlaceholderText("")
        self.set_pepper_vs_salt_label.setText(QCoreApplication.translate("MainWindow", u"\u6912\u566a/\u76d0\u566a\uff1a", None))
        self.set_pepper_vs_salt.setText("")
        self.set_pepper_vs_salt.setPlaceholderText("")
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u6cca\u677e\u566a\u58f0", None))
        self.set_poisson_lambda_label.setText(QCoreApplication.translate("MainWindow", u"lambda:", None))
        self.set_poisson_lambda.setText("")
        self.set_poisson_lambda.setPlaceholderText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u566a\u58f0", None))
        self.set_guass_mean_label.setText(QCoreApplication.translate("MainWindow", u"\u5747\u503c\uff1a", None))
        self.set_guass_mean.setText("")
        self.set_guass_mean.setPlaceholderText("")
        self.set_guass_sigma_label.setText(QCoreApplication.translate("MainWindow", u"\u6807\u51c6\u5dee\uff1a", None))
        self.set_guass_sigma.setText("")
        self.set_guass_sigma.setPlaceholderText("")
        self.btn_settings_reset_2.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.btn_settings_save_2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8bbe\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u566a\u58f0\u8bbe\u7f6e", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.0", None))
    # retranslateUi

