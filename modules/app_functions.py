'''
Author: splendidwave 1578399592@qq.com
Date: 2022-10-13 15:35:40
Description: 应用函数
Copyright (c) 2022 by splendidwave, This project can be used freely for all uses. 
'''
# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *

# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")

    # 设立初始值
    def set_general(self):
        self.config.set("General","file_save_path",os.getcwd()+'\\save')
        self.config.set("General","file_open_path",os.getcwd())

    # 噪声设置初始值
    def set_nosiy(self):
        self.config.set("Noisy","noise_ratio","0.04")
        self.config.set("Noisy","pepper_vs_salt","0.5")
        self.config.set("Noisy","guass_mean","0")
        self.config.set("Noisy","guass_sigma","25")
        self.config.set("Noisy","poisson_lambda","0.5")

    # 阅读配置文件
    def read_settings_file(self):
        self.config.read('settings.ini',encoding='utf-8')
        if self.config.get('General','init') == 'False':
            AppFunctions.set_general(self)
            AppFunctions.set_nosiy(self)
        else:
            # 有内容读取
            pass