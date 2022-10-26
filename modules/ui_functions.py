'''
Author: splendidwave 1578399592@qq.com
Date: 2022-10-13 15:35:40
Description: ui功能函数
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
from re import L
from main import *

# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class UIFunctions(MainWindow):
    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_restore.png"))
            self.ui.frame_size_grip.hide()
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons/images/icons/icon_maximize.png"))
            self.ui.frame_size_grip.show()
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleLeftBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.toggleLeftBox.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.ui.settingsTopBtn.styleSheet()
                    self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))
                
        UIFunctions.start_box_animation(self, width, widthRightBox, "left")

    # TOGGLE RIGHT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleRightBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraRightBox.width()
            widthLeftBox = self.ui.extraLeftBox.width()
            maxExtend = Settings.RIGHT_BOX_WIDTH
            color = Settings.BTN_RIGHT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.settingsTopBtn.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.settingsTopBtn.setStyleSheet(style + color)
                if widthLeftBox != 0:
                    style = self.ui.toggleLeftBox.styleSheet()
                    self.ui.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

            UIFunctions.start_box_animation(self, widthLeftBox, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0 

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = 240
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = 240
        else:
            right_width = 0       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file, useCustomTheme):
        if useCustomTheme:
            str = open(file, 'r').read()
            self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))
        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            #STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus(self):
                    UIFunctions.maximize_restore(self)
                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            # CUSTOM GRIPS
            self.left_grip = CustomGrip(self, Qt.LeftEdge, True)
            self.right_grip = CustomGrip(self, Qt.RightEdge, True)
            self.top_grip = CustomGrip(self, Qt.TopEdge, True)
            self.bottom_grip = CustomGrip(self, Qt.BottomEdge, True)

        else:
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.bgApp.setGraphicsEffect(self.shadow)

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # MINIMIZE
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    def resize_grips(self):
        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            self.left_grip.setGeometry(0, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
            self.top_grip.setGeometry(0, 0, self.width(), 10)
            self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)

    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS



    # START - Home_page_btn_function
    # 主页面按钮功能实现
    # ///////////////////////////////////////////////////////////////

    # 显示图片参数
    def show_image_info(self,path=None):
        if path:
            # self.image = cv2.imread(path)
            self.image = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
            imageSize = os.path.getsize(path)
            imageSize /= 1024 # 除以1024是代表Kb
            self.ui.home_info_label2_size_output.setText(str(imageSize)+" KB")
        else:
            self.ui.home_info_label2_size_output.setText("未选择保存格式，未知大小")
            self.ui.filePathlineEdit.setText("来自内存")
        self.ui.home_info_label2_pix_output.setText(str(self.image.shape[1])+" * "+str(self.image.shape[0]))


    # 从文件中打开图片
    def open_image_file(self):
        if self.camera_open:
            QMessageBox.information(None, '提示', '请先点击shot关闭摄像头',QMessageBox.Ok)
            return None
        get_filename_path, ok = QFileDialog.getOpenFileName(self,"选取图片",self.config.get('General','file_open_path'))
        if ok:
            UIFunctions.show_image_info(self,get_filename_path)
            self.ui.filePathlineEdit.setText(str(get_filename_path))
            #image = QPixmap(get_filename_path).scaled(self.ui.pic_preshow_label.width(), self.ui.pic_preshow_label.height())
            image = QPixmap(get_filename_path)
            self.ui.pic_preshow_label.setPixmap(image)
            self.ui.pic_preshow_label.setScaledContents(False)
        
    # 从摄像头中拍摄图片
    def open_camera(self):
        if self.camera_open:
            ret, self.image = self.vid.read()
            self.ui.pic_preshow_label.setScaledContents(True)
            self.camera_timer.stop()
            self.vid.release()
            UIFunctions.show_image_info(self)
        else:
            self.vid = cv2.VideoCapture(0)
            self.camera_timer.start(30)
        self.camera_open = ~self.camera_open

    # 打开一个窗口展示当前预览
    def home_page_show(self):
        win_name = "home_preview"
        UIFunctions.wait_key(self,self.image,win_name)
    # ///////////////////////////////////////////////////////////////
    # END - 主界面按钮功能实现

    # START - widgets_page_btn_function
    # 功能页面按钮功能实现
    # ///////////////////////////////////////////////////////////////
    # 通用:等待函数
    def wait_key(self,img,win_name,show=True):
        if show:
            cv2.namedWindow(win_name,cv2.WINDOW_AUTOSIZE)
            cv2.imshow(win_name,img)
        k = cv2.waitKey(0)
        if k == 27: #esc
            cv2.destroyAllWindows()
        elif k == ord('q'):
            cv2.destroyWindow(win_name)
        elif k == ord('s'):
            save_name,ok = QInputDialog.getText(self,"输入窗口","请输入文件名，需要后缀",QLineEdit.Normal,win_name+'.png')
            if ok and save_name != "":
                save_name = self.config.get('General','file_open_path') + '\\' + save_name 
                cv2.imwrite(save_name,img)
                QMessageBox.information(None, '提示', '保存成功',QMessageBox.Ok)
                UIFunctions.wait_key(self,img,win_name)
        elif k == ord('h'):
            image = UIFunctions.cvToQImage(self,img)
            self.ui.pic_preshow_label.setPixmap(QPixmap.fromImage(image))
            self.image = img
            UIFunctions.show_image_info(self)
            UIFunctions.wait_key(self,img,win_name)

    # 通用:返回灰度图
    def trun_gray(self,img):
        try:
            depth = img.shape[2]
            if depth == 3:
                return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        except IndexError:
            return img
    
    # 通用:归一化映射函数
    def normImg(self,x):
        return  cv2.normalize(x,None,0,255,cv2.NORM_MINMAX)

    # 缩放功能
    def resize_image(self,s="1920*1080"):
        size,ok = QInputDialog.getText(self,"输入窗口","请输入缩放的宽高，使用*分隔",QLineEdit.Normal,s)
        if ok and size != "":
            width,height = map(int,size.split('*'))
            size = (width,height)
            win_name = "resize"+str(size)
            img = cv2.resize(self.image,size)
            UIFunctions.wait_key(self,img,win_name)

    # 展示直方图
    def show_image_hist(self):
        if len(self.image.shape) == 2:
            # hist = cv2.calcHist([self.image],[0],None,[256],[0,256])
            plt.hist(self.image.ravel(),256); 
        else:
            color = ('b','g','r')
            for i,col in enumerate(color): 
                histr = cv2.calcHist([self.image],[i],None,[256],[0,256]) 
                plt.plot(histr,color = col) 
                plt.xlim([0,256])
        plt.show()

    # 自适应直方图均衡化
    def histequal_image(self):
        # 创建一个自适应均衡化的对象，并应用于图像
        claheg = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        if len(self.image.shape) == 2:
            cl = claheg.apply(self.image)
        else:
            imgr = self.image[:,:,0]
            imgg = self.image[:,:,1]
            imgb = self.image[:,:,2]
            claher = cv2.createCLAHE(clipLimit=3, tileGridSize=(8,8))
            claheb = cv2.createCLAHE(clipLimit=1, tileGridSize=(8,8))
            cllr = claher.apply(imgr)
            cllg = claheg.apply(imgg)
            cllb = claheb.apply(imgb)
            cl = np.dstack((cllr,cllg,cllb))
        win_name = "histequal"
        UIFunctions.wait_key(self,cl,win_name)

    # 加椒盐噪声
    def add_pepper_and_salt(self):
        # 获取数量和椒盐比
        amount = float(self.config.get("Noisy","noise_ratio"))
        p_vs_s = float(self.config.get("Noisy","pepper_vs_salt"))
        noisy_img = np.copy(self.image)
        num_pepper = np.ceil(amount * noisy_img.size * p_vs_s)
        num_salt = np.ceil(amount * noisy_img.size * (1. - p_vs_s))
        #设置添加pepper噪声
        coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in self.image.shape]
        noisy_img[tuple(coords)] = 0
        #设置添加salt噪声
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in self.image.shape]
        noisy_img[tuple(coords)] = 255
        # 展示
        win_name = "pepper&salt"
        UIFunctions.wait_key(self,noisy_img,win_name)

    # 加高斯噪声
    def add_gauss_noisy(self):
        img = self.image
        #获取均值和标准差
        mean = float(self.config.get("Noisy","guass_mean"))
        sigma = float(self.config.get("Noisy","guass_sigma"))
        #生成高斯分布的噪声
        gauss = np.random.normal(mean,sigma,img.shape)
        #给图片添加高斯噪声
        noisy_img = img + gauss
        #设置图片添加高斯噪声之后的像素值的范围
        noisy_img = np.uint8(np.clip(noisy_img,a_min=0,a_max=255))
        # 展示
        win_name = "gauss_noisy"
        UIFunctions.wait_key(self,noisy_img,win_name)

    # 加泊松噪声
    def add_poisson_noisy(self):
        img = self.image
        lam = float(self.config.get("Noisy","poisson_lambda"))
        # 生成泊松分布的噪声
        poisson = np.random.poisson(lam=lam,size=img.shape).astype(dtype='uint8')
        noisy_img = img + poisson
        noisy_img = np.uint8(np.clip(noisy_img,a_min=0,a_max=255))
        # 展示
        win_name = "poisson_noisy"
        UIFunctions.wait_key(self,noisy_img,win_name)

    # 加散斑噪声
    def add_speckle_noisy(self):
        img = self.image
        speckle = np.random.randn(*img.shape)
        #给图片添加speckle噪声
        noisy_img = img + img * speckle
        #归一化图像的像素值
        noisy_img = np.uint8(np.clip(noisy_img,a_min=0,a_max=255))
        # 展示
        win_name = "speckle_noisy"
        UIFunctions.wait_key(self,noisy_img,win_name)

    # 灰度化
    def gray_image(self):
        gray = UIFunctions.trun_gray(self,self.image)
        win_name = "gray"
        UIFunctions.wait_key(self,gray,win_name)

    # 二值化
    def thresholding_image(self):
        img = UIFunctions.trun_gray(self,self.image)
        # value, ok = QInputDialog.getInt(self, "输入窗口", "请输入阈值(整数):", 100, 0, 255, 1)
        ret,binary = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        win_name = "thresholding"
        UIFunctions.wait_key(self,binary,win_name)
        
    # 灰度反转
    def inverse_image(self):
        img = UIFunctions.trun_gray(self,self.image)
        value_max = np.max(img)
        inverse = value_max - img
        win_name = "inverse"
        UIFunctions.wait_key(self,inverse,win_name)

    # 对数变换
    def log_image(self):
        img = UIFunctions.trun_gray(self,self.image)
        log = np.uint8(UIFunctions.normImg(self,np.log(1.0 + img)))
        win_name = "log"
        UIFunctions.wait_key(self,log,win_name)

    # 伽马变换
    def gamma_image(self):
        img = UIFunctions.trun_gray(self,self.image)
        items = ('0.125', '0.25', '0.5', '1.0', '2.0', '4.0')
        item,ok = QInputDialog.getItem(self,"gamma值","选择gamma值",items,3,True)
        if ok:
            win_name = "gamma=" + item
            item = float(item)
            gamma = np.power(img, item)
            gamma = np.uint8(UIFunctions.normImg(self,gamma))
            UIFunctions.wait_key(self,gamma,win_name)

    # 对比度拉伸
    def contrast_stretch_image(self):
        img = UIFunctions.trun_gray(self,self.image)
        cs = np.uint8(UIFunctions.normImg(self,img))
        win_name = "contrast_stretch"
        UIFunctions.wait_key(self,cs,win_name)

    # 8bit分层
    def bits_layering_image(self):
        img = UIFunctions.trun_gray(self,self.image)
        height, width = img.shape[:2]
        height, width = int(height/max(height,width)*300),int(width/max(height,width)*300)
        size = (width,height)
        # origin = cv2.resize(img,size)
        # blls = [origin]
        img = cv2.resize(img,size)
        blls = [img]
        for i in range(8):
            layer = np.copy(img)
            era1 = 2**i
            era2 = 2 ** (i+1)
            # for row in range(layer.shape[0]):
            #     for col in range(layer.shape[1]):
            #         layer[row][col]=np.where((layer[row][col]>=era1) and (layer[row][col]<era2),255,0)
            layer = np.where((layer>=era1) * (layer<era2),255,0)
            # layer = cv2.resize(layer,size)
            blls.append(layer)
        for i in range(3):
            for j in range(2):
                vs1 = np.hstack((blls[0],blls[1],blls[2]))
                vs2 = np.hstack((blls[3],blls[4],blls[5]))
                vs3 = np.hstack((blls[6],blls[7],blls[8]))
            bl = np.uint8(np.vstack((vs1,vs2,vs3)))
        win_name = "8bitslayering"
        UIFunctions.wait_key(self,bl,win_name)


    # 空间滤波
    # 均值滤波
    def mean_filtering_image(self):
        img = self.image.copy()
        mean_f = cv2.blur(img,(3,3))
        win_name = "mean_filtering"
        UIFunctions.wait_key(self,mean_f,win_name)

    # 高斯滤波
    def gauss_filtering_image(self):
        img = self.image.copy()
        gauss_f = result=cv2.GaussianBlur(img,(3,3),0,0)
        win_name = "gauss_filtering"
        UIFunctions.wait_key(self,gauss_f,win_name)

    # 中值滤波
    def median_filtering_image(self):
        img = self.image.copy()
        median_f = cv2.medianBlur(img,3)
        win_name = "median_filtering"
        UIFunctions.wait_key(self,median_f,win_name)

    # 锐化
    # sobel
    def sobel_image(self):
        img = cv2.Sobel(self.image, cv2.CV_64F, 0, 1, ksize=5)
        win_name = "sobel"
        UIFunctions.wait_key(self,img,win_name)

    # laplace
    def laplace_image(self):
        img = cv2.Laplacian(self.image, cv2.CV_64F)
        win_name = "laplace"
        UIFunctions.wait_key(self,img,win_name)

    # Scharr 
    def scharr_image(self):
        img = cv2.Scharr(self.image, cv2.CV_64F, 0, 1)
        win_name = "scharr"
        UIFunctions.wait_key(self,img,win_name)

    # canny
    def canny_image(self):
        def CannyThreshold(lowThreshold):
            img = cv2.Canny(self.image, lowThreshold, 200)
            cv2.imshow(win_name,img)
            UIFunctions.wait_key(self,img,win_name,show=False)
        win_name = "canny"
        cv2.namedWindow(win_name)
        cv2.createTrackbar('Min threshold', 'canny', 0, 160, CannyThreshold)
        CannyThreshold(0)

    # 形态学处理
    # 腐蚀        
    def erode_image(self):
        k = np.ones((3, 3), np.uint8)
        items = ('1', '2', '3', '4')
        item,ok = QInputDialog.getItem(self,"迭代次数","选择迭代次数",items,0,False)
        if ok:
            win_name = "erode" + item
            item = int(item)
            img = cv2.erode(self.image, k, iterations=item)
            UIFunctions.wait_key(self,img,win_name)

    # 膨胀
    def dilate_image(self):
        k = np.ones((3, 3), np.uint8)
        items = ('1', '2', '3', '4')
        item,ok = QInputDialog.getItem(self,"迭代次数","选择迭代次数",items,0,False)
        if ok:
            win_name = "dilate" + item
            item = int(item)
            img = cv2.dilate(self.image, k, iterations=item)
            UIFunctions.wait_key(self,img,win_name)

    # 开操作
    def open_image(self):
        k = np.ones((3, 3), np.uint8)
        img = cv2.morphologyEx(self.image,cv2.MORPH_OPEN,k)
        win_name = "open"
        UIFunctions.wait_key(self,img,win_name)

    # 闭操作
    def close_image(self):
        k = np.ones((3, 3), np.uint8)
        img = cv2.morphologyEx(self.image,cv2.MORPH_CLOSE,k)
        win_name = "close"
        UIFunctions.wait_key(self,img,win_name)

    # 机器学习
    # k-mean
    def kmean(self):
        img = self.image.copy()
        items = ('2', '3', '4', '5', '6', '7')
        item,ok = QInputDialog.getItem(self,"区域分割","选择需要分成几块",items,2,False)
        if ok:
            Z = img.reshape((-1,3))      
            Z = np.float32(Z)
            c = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            ret, label, center = cv2.kmeans(Z, int(item), None, c, 10, cv2.KMEANS_RANDOM_CENTERS)
            center = np.uint8(center)
            res = center[label.flatten()]
            img = res.reshape((img.shape))
            win_name = "test"
            UIFunctions.wait_key(self,img,win_name)

    # 人脸识别
    def facefind(self):
        img = self.image.copy()
        gray = UIFunctions.trun_gray(self,img)
        # 加载人脸特征，该文件在 python安装目录\Lib\site-packages\cv2\data 下
        face_cascade = cv2.CascadeClassifier(r'modules\haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(20, 20))
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        win_name = "face"
        UIFunctions.wait_key(self,img,win_name)

    # 傅里叶变换
    # 频谱展示
    def fre_spectrum(self):
        img = UIFunctions.trun_gray(self,self.image)
        # 进行傅里叶变换，时域变频域
        img_float32 = np.float32(img)
        dft = cv2.dft(img_float32,flags = cv2.DFT_COMPLEX_OUTPUT)
        # 将零零频率分量移动到频谱的中心
        dft_shift = np.fft.fftshift(dft)
        # 数值映射
        magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
        magnitude_spectrum = np.uint8(UIFunctions.normImg(self,magnitude_spectrum))

        win_name = "magnitude_spectrum"
        UIFunctions.wait_key(self,magnitude_spectrum,win_name)
        # plt.imshow(magnitude_spectrum,cmap="gray")
        # plt.title("magnitude_spectrum")
        # plt.xticks([]),plt.yticks([])
        # plt.show()




    # 高通滤波
    def hf_filtering(self):
        img = UIFunctions.trun_gray(self,self.image)            
        # 得到中心像素
        rows, cols = img.shape[:2]
        mid_row, mid_col = int(rows / 2), int(cols / 2)
        radius, ok = QInputDialog.getInt(self, "输入窗口", "请输入滤波半径(值越小滤波越少):", int(mid_col/2), 0, 9999, 10)
        if ok:
            # 进行傅里叶变换，时域变频域
            dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
            dft_shift = np.fft.fftshift(dft)

            # 构建掩模,两个通道,初始值为1
            mask = np.ones((rows, cols, 2), np.uint8)
            mask[mid_row - radius:mid_row + radius, mid_col - radius:mid_col + radius] = 0

            # 滤波并反变换回去
            fshift = dft_shift*mask
            ishift = np.fft.ifftshift(fshift)
            iimg = cv2.idft(ishift)
            iimg= cv2.magnitude(iimg[:, :,0], iimg[:, :,1])
            iimg = np.uint8(UIFunctions.normImg(self,iimg))
            
            win_name = "hf"
            UIFunctions.wait_key(self,iimg,win_name)

    # 低通滤波
    def lf_filtering(self):
        img = UIFunctions.trun_gray(self,self.image)            
        # 得到中心像素
        rows, cols = img.shape[:2]
        mid_row, mid_col = int(rows / 2), int(cols / 2)

        radius, ok = QInputDialog.getInt(self, "输入窗口", "请输入滤波半径(值越大滤波越少):", int(mid_col/2), 0, 9999, 10)
        if ok:
            # 进行傅里叶变换，时域变频域
            dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
            dft_shift = np.fft.fftshift(dft)

            # 构建掩模,两个通道,初始值为0
            mask = np.zeros((rows, cols, 2), np.uint8)
            mask[mid_row - radius:mid_row + radius, mid_col - radius:mid_col + radius] = 1
            
            # 滤波并反变换回去
            fshift = dft_shift*mask
            ishift = np.fft.ifftshift(fshift)
            iimg = cv2.idft(ishift)
            iimg= cv2.magnitude(iimg[:, :,0], iimg[:, :,1])
            iimg = np.uint8(UIFunctions.normImg(self,iimg))
            win_name = "lf"
            UIFunctions.wait_key(self,iimg,win_name)


    # 其他功能
    # 转为字符画
    def character_image(self):
        img = UIFunctions.trun_gray(self,self.image)
        rows, cols = img.shape[:2]
        rows = rows//2
        img = cv2.resize(img,(cols,rows))
        lstChars = self.config.get('General','file_character_list')
        output = self.config.get('General','file_save_path') + "\\character.txt"
        g2c = 256/len(lstChars)
        
        txt = ""
        for i in range(rows):
            for j in range(cols):
                txt += lstChars[int(img[i,j]/g2c)]
            txt += '\n'

        with open(output, 'w') as f:
            f.write(txt)
        QMessageBox.information(None, '提示', 'character.txt输出成功',QMessageBox.Ok)

    # 九宫格
    def ninegrid_image(self):
        # 切片函数
        def cut_image(img,width):
            box_list = []
            if len(img.shape) == 2:
                for i in range(0, 3):
                    for j in range(0, 3):
                        box = img[i * width:(i+1) * width, j * width : (j + 1) * width]
                        box_list.append(box)
            elif len(img.shape) == 3:
                for i in range(0, 3):
                    for j in range(0, 3):
                        box = img[i * width:(i+1) * width, j * width : (j + 1) * width,:]
                        box_list.append(box)
            return box_list

        img = self.image.copy()
        value, ok = QInputDialog.getInt(self, "输入窗口", "请输入裁剪后的边值像素(正方形):", 300, 0, 2000, 100)
        if ok:
            value = int(value)*3
            img = cv2.resize(img,(value,value))
            box_list = cut_image(img,value//3)
            for i,box in enumerate(box_list):
                save_name = self.config.get('General','file_save_path') + '\\ninegrid_image\\' + str(i+1)+'.png'
                cv2.imwrite(save_name,box)
            QMessageBox.information(None, '提示', 'ninegrid_image输出成功',QMessageBox.Ok)

    # 图片蒙太奇
    def montage_image(self):
        # 小图片路径
        smallPicPath = str(self.config.get('General','file_montage_path'))
        small_pic_files = os.listdir(smallPicPath)
        # 查看小图片demo 给出建议的缩放
        demo_path = smallPicPath + "\\" + small_pic_files[0]
        demo = cv2.imread(demo_path)
        h, w = demo.shape[:2]
        s = str(w)+'*'+str(h)

        size,ok = QInputDialog.getText(self,"输入窗口","请输入小图的宽高，使用*分隔",QLineEdit.Normal,s)
        if ok:
            w,h = map(int,size.split("*"))

            # 原图像处理
            img = self.image.copy()
            img = cv2.resize(img, (w*50, h*50))
            cv2.imwrite("v1.jpg", img)
            # 新图片处理
            big_pic = np.zeros((h*50, w*50, 3))
            # 建立字典存放每个小图片的直方图
            small_Pic_hist_Dic = {}
            n = 0
            
            # 预处理图片 
            print("正在预处理图片")
            for file in small_pic_files:
                picPath = smallPicPath + "\\" + file
                small_img = cv2.imread(picPath)
                small_img = cv2.resize(small_img, (w, h))
                hist = []
                for i in range(3):
                    ht = cv2.calcHist([small_img],[i],None,[256],[0,256])
                    hist.append(ht)
                small_Pic_hist_Dic[picPath] = hist
                # 更改之后写入文件
                cv2.imwrite(picPath, small_img)
                n += 1
                print(n)

            # 遍历找到最匹配值并替代
            for i in range(0, h*50, h):
                for j in range(0, w*50, w):        
                    part_img = img[i:i+h,j:j+w,:]
                    hist = []
                    for k in range(3):
                        ht = cv2.calcHist([part_img],[k],None,[256],[0,256])
                        hist.append(ht)

                    sim = 0.0
                    for key in small_Pic_hist_Dic:
                        match0 = cv2.compareHist(hist[0],small_Pic_hist_Dic[key][0],cv2.HISTCMP_CORREL)
                        match1 = cv2.compareHist(hist[1],small_Pic_hist_Dic[key][1],cv2.HISTCMP_CORREL)
                        match2 = cv2.compareHist(hist[2],small_Pic_hist_Dic[key][2],cv2.HISTCMP_CORREL)
                        match = match0 + match1 + match2
                        if match > sim:
                            sim = match
                            rename = key

                    big_pic[i:i+h,j:j+w,:] = cv2.imread(rename)
            cv2.imwrite("v2.jpg", big_pic)

            # 融合两图，结果更好看
            image1 = cv2.imread('v1.jpg')
            image2 = cv2.imread('v2.jpg')
            dst = cv2.addWeighted(image1,0.2,image2,0.8,3)
            # dst = cv2.addWeighted(img,0.2,big_pic,0.8,3)
            os.remove("v1.jpg")
            os.remove("v2.jpg")
            win_name = "montage"
            UIFunctions.wait_key(self,dst,win_name)
        

    # 图片像素化
    def pixel_image(self):
        img = self.image.copy()
        rows, cols = img.shape[:2]
        img = cv2.resize(img,(cols//10,rows//10))
        img = cv2.resize(img,(cols,rows),interpolation=cv2.INTER_NEAREST)
        win_name = "pixel"
        UIFunctions.wait_key(self,img,win_name)

    # 幻影坦克
    def mirage_tank_image(self):
        inside_pic = np.uint8(self.image.copy() * 0.35)
        h,w = inside_pic.shape[:2]
        get_filename_path, ok = QFileDialog.getOpenFileName(self,"选取表图",self.config.get('General','file_open_path'))
        if ok:
            out_pic = cv2.imread(get_filename_path)
            # 调整表图大小 与里图一致
            out_pic = cv2.resize(out_pic,(w,h))
            # 如果强度小于100 拉到100
            out_pic[out_pic<100] = 100
            # 转变为灰度图
            inside_pic = UIFunctions.trun_gray(self,inside_pic)
            out_pic = UIFunctions.trun_gray(self,out_pic)
            # 建立新的画布 
            new_pic = np.zeros((h,w,4), np.uint8)
            # print(new_pic.shape)
            # 遍历图片 套用公式
            for i in range(h):
                for j in range(w):
                    alpha = 255 - (out_pic[i,j]-inside_pic[i,j])
                    if alpha == 0:
                        alpha = 1
                    p_new = np.uint8(255*inside_pic[i,j]/alpha)
                    new_pic[i,j,0] = p_new
                    new_pic[i,j,1] = p_new
                    new_pic[i,j,2] = p_new
                    new_pic[i,j,3] = alpha
            # 统一有点问题
            # alpha = 255 - (out_pic - inside_pic)
            # alpha[alpha==0] = 1
            # p_new = np.uint8(255*inside_pic/alpha)
            # new_pic = cv2.merge((p_new,p_new,p_new,alpha))

            win_name = "tank"
            UIFunctions.wait_key(self,new_pic,win_name)
    # ///////////////////////////////////////////////////////////////
    # END  功能页面按钮功能实现



    # START - 初始设置页面功能
    # ///////////////////////////////////////////////////////////////

    # 设置页面初始化展示
    def show_settings(self):
        # 设置界面
        self.ui.set_file_svae_path.setText(self.config.get('General','file_save_path'))
        self.ui.set_file_open_path.setText(self.config.get('General','file_open_path'))
        self.ui.set_file_character_list.setText(self.config.get('General','file_character_list'))
        self.ui.set_file_montage_path.setText(self.config.get('General','file_montage_path'))
        # 噪声页面
        self.ui.set_noisy_ratio.setText(self.config.get("Noisy","noise_ratio"))
        self.ui.set_pepper_vs_salt.setText(self.config.get("Noisy","pepper_vs_salt"))
        self.ui.set_guass_mean.setText(self.config.get("Noisy","guass_mean"))
        self.ui.set_guass_sigma.setText(self.config.get("Noisy","guass_sigma"))
        self.ui.set_poisson_lambda.setText(self.config.get("Noisy","poisson_lambda"))

    # 保存
    def save_settings(self):
        # 读取
        self.config.set("General","file_save_path",self.ui.set_file_svae_path.text())
        self.config.set("General","file_open_path",self.ui.set_file_open_path.text())
        self.config.set("General","file_character_list",self.ui.set_file_character_list.text())
        self.config.set("General","file_montage_path",self.ui.set_file_montage_path.text())

        self.config.set("Noisy","noise_ratio",self.ui.set_noisy_ratio.text())
        self.config.set("Noisy","pepper_vs_salt",self.ui.set_pepper_vs_salt.text())
        self.config.set("Noisy","guass_mean",self.ui.set_guass_mean.text())
        self.config.set("Noisy","guass_sigma",self.ui.set_guass_sigma.text())
        self.config.set("Noisy","poisson_lambda",self.ui.set_guass_sigma.text())

        # 写入
        self.config.set("General","init","True")

        with open("settings.ini","w") as f:
            self.config.write(f)

        QMessageBox.information(None, '提示', '保存成功',QMessageBox.Ok)


    # ///////////////////////////////////////////////////////////////
    # END - 初始设置页面功能



    # START - 其他功能
    # ///////////////////////////////////////////////////////////////
    # CV 和 qimage互换
    def cvToQImage(self,data):
        # 8-bits unsigned, NO. OF CHANNELS=1
        if data.dtype == np.uint8:
            channels = 1 if len(data.shape) == 2 else data.shape[2]
        if channels == 3: # CV_8UC3
            # Copy input Mat
            # Create QImage with same dimensions as input Mat
            img = QImage(data, data.shape[1], data.shape[0], data.strides[0], QImage.Format_RGB888)
            return img.rgbSwapped()
        elif channels == 1:
            # Copy input Mat
            # Create QImage with same dimensions as input Mat
            img = QImage(data, data.shape[1], data.shape[0], data.strides[0], QImage.Format_Indexed8)
            return img
        else:
            qDebug("ERROR: numpy.ndarray could not be converted to QImage. Channels = %d" % data.shape[2])
            return QImage()

 
    def QImage2CV(self,qtpixmap):

        qimg = qtpixmap.toImage()
        temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
        temp_shape += (4,)
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
        result = result[..., :3]

        return result

    def test(self):
        pass

    # END 其他功能