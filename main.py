'''
Author: splendidwave 1578399592@qq.com
Date: 2022-10-13 15:35:40
Description: 主函数
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

import sys
import os
import platform
import cv2
import numpy as np
import configparser
import matplotlib.pyplot as plt;

# IMPORT / GUI AND MODULES AND WIDGETS 导入高清模组
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS 定义为全局窗口
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # 默认配置载入 修改需要改3个地方，1读取设置初始值（app_functions），2显示到ui(show_settings),3.保存按钮（save_settings）
        self.config = configparser.ConfigParser()
        AppFunctions.read_settings_file(self)
        

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX 
        # 是否使用title bar 针对windows系统
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME 不予显示副标题
        # ///////////////////////////////////////////////////////////////
        title = "PyImage Helper"
        # description = "PyDracula APP - Theme with colors based on Dracula for Python."
        # APPLY TEXTS
        self.setWindowTitle(title)
        # widgets.titleRightInfo.setText(description)

        # 图片变量
        self.image = None
        # 摄像头变量
        self.camera_open = False # 摄像头是否打开
        self.camera_timer = QTimer() # 摄像头定时器
        self.camera_timer.timeout.connect(self.update_frame)

        # TOGGLE MENU
        # 触发菜单
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        #widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # 添加功能需要改3个地方 1按钮槽绑定功能函数 2判断按钮类型 3添加对应的ui_function
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        # widgets.btn_save.clicked.connect(self.buttonClick)

        # Home page Button
        widgets.btn_home_open.clicked.connect(self.buttonClick)
        widgets.btn_home_shot.clicked.connect(self.buttonClick)
        widgets.btn_home_show.clicked.connect(self.buttonClick)

        # Widgets page Button
        # 基础操作
        widgets.btn_widgets_resize.clicked.connect(self.widgets_buttonClick) # 缩放 完成
        widgets.btn_widgets_hist.clicked.connect(self.widgets_buttonClick) # 直方图 完成
        widgets.btn_widgets_histequal.clicked.connect(self.widgets_buttonClick) # 直方图均衡化 完成

        # 加噪
        widgets.btn_widgets_pepper_and_salt.clicked.connect(self.widgets_buttonClick) # 椒盐噪声 完成
        widgets.btn_widgets_gauss_noisy.clicked.connect(self.widgets_buttonClick) # 高斯噪声 完成
        widgets.btn_widgets_speckle_noisy.clicked.connect(self.widgets_buttonClick) # 散斑噪声 完成
        widgets.btn_widgets_poisson_noisy.clicked.connect(self.widgets_buttonClick) # 泊松噪声 完成

        # 灰度变换
        widgets.btn_widgets_gray.clicked.connect(self.widgets_buttonClick) # 灰度化 完成
        widgets.btn_widgets_Thresholding.clicked.connect(self.widgets_buttonClick) # 二值化 完成
        widgets.btn_widgets_flip.clicked.connect(self.widgets_buttonClick) # 反转 完成
        widgets.btn_widgets_log.clicked.connect(self.widgets_buttonClick) # 对数 完成
        widgets.btn_widgets_gamma.clicked.connect(self.widgets_buttonClick) # 伽马 完成 
        widgets.btn_widgets_contrast_stretch.clicked.connect(self.widgets_buttonClick) # 对比度拉伸 完成
        widgets.btn_widgets_8bits_layering.clicked.connect(self.widgets_buttonClick) # 8bit 完成

        # 滤波
        widgets.btn_widgets_mean_filtering.clicked.connect(self.widgets_buttonClick) # 均值 完成
        widgets.btn_widgets_gauss_filtering.clicked.connect(self.widgets_buttonClick)   # 高斯 完成
        widgets.btn_widgets_median_filtering.clicked.connect(self.widgets_buttonClick) # 中值 完成
        

        # Setting page(new page) Button
        widgets.btn_settings_save.clicked.connect(self.buttonClick)
        widgets.btn_settings_save_2.clicked.connect(self.buttonClick)
        widgets.btn_settings_reset_1.clicked.connect(self.buttonClick)
        widgets.btn_settings_reset_2.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # # EXTRA RIGHT BOX
        # def openCloseRightBox():
        #     UIFunctions.toggleRightBox(self, True)
        # widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        UIFunctions.show_settings(self)


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # home page botton
        if btnName == "btn_home_open":
            UIFunctions.open_image_file(self)
            
        if btnName == "btn_home_shot":
            UIFunctions.open_camera(self)

        if btnName == "btn_home_show":
            UIFunctions.home_page_show(self)

        if "btn_settings_save" in btnName:
            UIFunctions.save_settings(self)

        if btnName == "btn_settings_reset_1":
            AppFunctions.set_general(self)
            UIFunctions.show_settings(self)

        if btnName == "btn_settings_reset_2":
            AppFunctions.set_nosiy(self)
            UIFunctions.show_settings(self)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

    # widgets page button clicked
    def widgets_buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if not isinstance(self.image, np.ndarray):
            QMessageBox.information(None, '提示', '请先打开一副图吧!  ',QMessageBox.Ok)
            return None

        # widgets page botton
        # 缩放
        if btnName == "btn_widgets_resize":
            UIFunctions.resize_image(self)

        # 直方图
        if btnName == "btn_widgets_hist":
            UIFunctions.show_image_hist(self)

        # 直方图均衡
        if btnName == "btn_widgets_histequal":
            UIFunctions.histequal_image(self)

        # 加噪
        # 椒盐噪声
        if btnName == "btn_widgets_pepper_and_salt":
            UIFunctions.add_pepper_and_salt(self)

        # 高斯噪声
        if btnName == "btn_widgets_gauss_noisy":
            UIFunctions.add_gauss_noisy(self)

        # 泊松噪声
        if btnName == "btn_widgets_poisson_noisy":
            UIFunctions.add_poisson_noisy(self)

        # 散斑噪声
        if btnName == "btn_widgets_speckle_noisy":
            UIFunctions.add_speckle_noisy(self)


        # 灰度变化
        # 灰度化
        if btnName == "btn_widgets_gray":
            UIFunctions.gray_image(self)

        # 二值化 利用OTSU算法
        if btnName == "btn_widgets_Thresholding":
            UIFunctions.thresholding_image(self)

        # 图像反转
        if btnName == "btn_widgets_flip":
            UIFunctions.inverse_image(self)

        # 对数变换
        if btnName == "btn_widgets_log":
            UIFunctions.log_image(self)
        
        # 伽马变换
        if btnName == "btn_widgets_gamma":
            UIFunctions.gamma_image(self)

        # 对比度拉伸
        if btnName == "btn_widgets_contrast_stretch":
            UIFunctions.contrast_stretch_image(self)

        # 8比特分层
        if btnName == "btn_widgets_8bits_layering":
            UIFunctions.bits_layering_image(self)

        # 空间滤波
        # 空间均值滤波
        if btnName == "btn_widgets_mean_filtering":
            UIFunctions.mean_filtering_image(self)

        # 空间高斯滤波
        if btnName == "btn_widgets_gauss_filtering":
            UIFunctions.gauss_filtering_image(self)

        # 空间中值滤波
        if btnName == "btn_widgets_median_filtering":
            UIFunctions.median_filtering_image(self)


        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')




    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    # 摄像头定时中断
    def update_frame(self):
        ret, frame = self.vid.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0], QImage.Format_RGB888)
        self.ui.pic_preshow_label.setPixmap(QPixmap.fromImage(image))
        


if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
