#sys提供了与 Python 解释器交互以及与系统相关的功能。
import sys
#dlib主要用于估计人脸的关键点位置
import dlib
#imutils用于简化图像处理任务。提供了一系列便捷的函数，可以更轻松地进行常见的图像处理和计算机视觉操作。
import imutils
#QtWidgets模块包含了一整套UI元素控件，用于建立符合系统风格的界面；，用于创建GUI应用程序的各种控件和窗口部件
from PyQt5 import QtWidgets
#QtCore模块涵盖了包的核心的非GUI功能，QThread提供了一个线程类，通过这个类就可以创建子线程，pyqtSignal是一个自定义信号类，用于在对象之间进行信号和槽的通信
from PyQt5.QtCore import QThread, pyqtSignal
#QtGui涵盖了多种基本图形功能的类(字体， 图形，图标，颜色)，QImage用于加载，保存，处理图像，QPixmap用于在屏幕上显示图像
from PyQt5.QtGui import QImage, QPixmap
#QMainWindow包含菜单栏，工具栏，状态栏，标题栏等，是GUI程序的主窗口。QGraphicsPixmapItem用于显示图像的图形项类
#QGraphicsScene用于管理图形项的容器。QMessageBox用于显示消息对话框，可用于显示警告、错误。QFileDialog用于显示文件对话框，可以让用户选择文件或目录，用于打开或保存文件。
from PyQt5.QtWidgets import QMainWindow, QGraphicsPixmapItem, QGraphicsScene, QMessageBox, QFileDialog
#用于加载和播放声音的pygame模块
from pygame import mixer
#windows的音频播放系统
import winsound
from src.UI import Ui_MainWindow
from src.utils import *

#MainWindow将界面上的各种控件与对应的操作方法进行了连接和关联，如点击这个按钮干什么
class MainWindow(QMainWindow, Ui_MainWindow):
    #构造函数：构造函数初始化主窗口。
    def __init__(self, parent=None):
        #调用父类（QMainWindow）的构造函数。
        super(MainWindow, self).__init__(parent)

        #创建类AdjustCamera_Thread的实例，并将其赋值给self.adjust_camera_Thread
        self.adjust_camera_Thread = AdjustCamera_Thread()
        #创建类Start_Thread的实例，并将其赋值给self.start_Thread
        self.start_Thread = Start_Thread()
        #调用类中的 setupUi 方法，对界面进行设置。
        self.setupUi(self)

        #连接槽
        #当下拉列表 Cam_Select 的选项改变时，连接到槽函数 change_Cam_Select。
        self.Cam_Select.currentIndexChanged.connect(self.change_Cam_Select)
        #当按钮 Button_OpenVideo 被点击时，连接到槽函数 open_Video。
        self.Button_OpenVideo.clicked.connect(self.open_Video)
        #当按钮 Button_Start 被点击时，连接到槽函数 start。
        self.Button_Start.clicked.connect(self.start)
        #当按钮 Button_End 被点击时，连接到槽函数 end。
        self.Button_End.clicked.connect(self.end)
        #当按钮 Button_AdjustCamera_Location 被点击时，连接到槽函数 adjust_camera_location。
        self.Button_AdjustCamera_Location.clicked.connect(self.adjust_camera_location)
        #当复选框 offDuty_Check 被点击时，连接到槽函数 change_OffDuty_Check_Status。
        self.offDuty_Check.clicked.connect(self.change_OffDuty_Check_Status)
        #当滑动条 offDuty_Time 的值改变时，连接到槽函数 change_OffDuty_Value。
        self.offDuty_Time.valueChanged.connect(self.change_OffDuty_Value)
        #当按钮 video 被点击时，连接到槽函数 set_open_video。
        self.video.clicked.connect(self.set_open_video)
        #当按钮 cam 被点击时，连接到槽函数 set_open_video。
        self.cam.clicked.connect(self.set_open_video)
        #当按钮 show_eye 被点击时，连接到槽函数 set_show_setting。
        self.show_eye.clicked.connect(self.set_show_setting)
        #当按钮 show_head 被点击时，连接到槽函数 set_show_setting。
        self.show_head.clicked.connect(self.set_show_setting)
        #当按钮 show_mouth 被点击时，连接到槽函数 set_show_setting。
        self.show_mouth.clicked.connect(self.set_show_setting)
        #当按钮 show_key_point 被点击时，连接到槽函数 set_show_setting。
        self.show_key_point.clicked.connect(self.set_show_setting)

        #连接线程和信号
        #将 start_Thread 的信号 msg 连接到槽函数 show_Message。
        self.start_Thread.msg.connect(self.show_Message)
        #将 start_Thread 的信号 picture 连接到槽函数 show_Image。
        self.start_Thread.picture.connect(self.show_Image)
        #将 start_Thread 的信号 window 连接到槽函数 pop_window。
        self.start_Thread.window.connect(self.pop_window)
        #将 adjust_camera_Thread 的信号 picture 连接到槽函数 show_Image。
        self.adjust_camera_Thread.picture.connect(self.show_Image)
        #将 adjust_camera_Thread 的信号 msg 连接到槽函数 show_Message。
        self.adjust_camera_Thread.msg.connect(self.show_Message)
        #将 adjust_camera_Thread 的信号 window 连接到槽函数 pop_window。
        self.adjust_camera_Thread.window.connect(self.pop_window)

    def set_show_setting(self):
        isChecked = self.sender().isChecked()
        if self.sender() == self.show_eye:
            self.start_Thread.set_show_eye(isChecked)
        elif self.sender() == self.show_mouth:
            self.start_Thread.set_show_mouth(isChecked)
        elif self.sender() == self.show_head:
            self.start_Thread.set_show_Head(isChecked)
        else:
            self.start_Thread.set_show_key_point(isChecked)

    #根据按钮 video 的选中状态来设置是否打开视频。
    def set_open_video(self):
        #如果按钮 video 被选中。
        if self.video.isChecked():
            #调用start_Thread对象的set_open_video 方法，将 True 作为参数输入，表示打开视频。
            self.start_Thread.set_open_video(True)
        #反之，不打开视频
        else:
            self.start_Thread.set_open_video(False)

    def change_OffDuty_Check_Status(self):
        self.start_Thread.change_OffDuty_Check_Status(self.offDuty_Check.isChecked())

    def change_OffDuty_Value(self):
        self.start_Thread.change_OffDuty_Value(self.offDuty_Time.value())

    #调用 start_Thread 对象的 start 方法，开始执行线程。
    def start(self):
        self.start_Thread.start()

    #调用 adjust_camera_Thread 对象的 start 方法，开始执行线程。
    def adjust_camera_location(self):
        self.adjust_camera_Thread.start()

    #用于结束 adjust_camera_Thread 和 start_Thread。
    def end(self):
        self.adjust_camera_Thread.close()
        self.start_Thread.close()

    #用于改变摄像头选择
    def change_Cam_Select(self):
        #调用 adjust_camera_Thread 对象的 change_cam_select 方法，将当前选中摄像头的索引作为参数传入。
        self.adjust_camera_Thread.change_cam_select(self.Cam_Select.currentIndex())
        #调用 start_Thread 对象的 change_cam_select 方法，将当前选中摄像头的索引作为参数传入。
        self.start_Thread.change_cam_select(self.Cam_Select.currentIndex())
        #将字符串 “切换摄像头” 连接上当前选中摄像头的索引，并将结果追加到 output_Window 中。
        self.output_Window.append("切换摄像头" + str(self.Cam_Select.currentIndex()))

    #用于打开视频文件
    def open_Video(self):
        #打开文件对话框，让用户选择一个视频文件，返回选择的文件路径。
        filePath = QFileDialog.getOpenFileName(self, "打开视频文件", "", 'Video files(*.mp4)')
        #将字符串 “视频文件”、选中的文件路径和 “加载成功” 拼接起来，并将结果追加到 output_Window 中。
        self.output_Window.append("视频文件" + filePath[0] + "加载成功")
        #调用 start_Thread 对象的 set_filePath 方法，将选中的文件路径作为参数传入。
        self.start_Thread.set_filePath(filePath[0])
        #将 video 复选框的状态设置为选中。
        self.video.setChecked(True)

    #用于显示信息
    def show_Message(self, msg):
        #将传入的消息字符串追加到 output_Window 中。
        self.output_Window.append(msg)

    #用于显示图像。
    def show_Image(self, image):
        #获取图像的高度。
        height = image.shape[0]
        #获取图像的宽度
        width = image.shape[1]
        #使用图像数据、宽度、高度和 RGB888 格式创建一个 QImage 对象。
        frame = QImage(image, width, height, QImage.Format_RGB888)
        #从 QImage 对象创建一个 QPixmap 对象。
        pix = QPixmap.fromImage(frame)
        #创建一个 QGraphicsPixmapItem 对象，并传入 QPixmap 对象作为参数。
        item = QGraphicsPixmapItem(pix)
        #创建一个 QGraphicsScene 对象。
        scene = QGraphicsScene()
        #将 QGraphicsPixmapItem 对象添加到 QGraphicsScene 对象中。
        scene.addItem(item)
        #将 QGraphicsScene 对象设置为 graphicsView 的场景。
        self.graphicsView.setScene(scene)

    #用于弹出警告窗口，显示传入的信息。
    def pop_window(self, info):
        #弹出一个警告窗口，标题为 “提示”，内容为传入的信息字符串。
        QMessageBox.warning(self, "提示", info, QMessageBox.Yes)

    #用于退出应用。
    def exit(self):
        #如果 cap 不为 None，释放 cap 对象。
        if self.cap is not None:
            self.cap.release()
        #退出应用程序。
        sys.exit(app.exec_())


class AdjustCamera_Thread(QThread):
    #定义一个 pyqtSignal 信号对象，用于发送图像数据。
    picture = pyqtSignal(object)
    #定义一个 pyqtSignal 信号对象，用于发送消息字符串。
    msg = pyqtSignal(str)
    #定义一个 pyqtSignal 信号对象，用于发送窗口消息字符串。
    window = pyqtSignal(str)

    #定义构造函数
    def __init__(self):
        super(AdjustCamera_Thread, self).__init__()
        #初始化所有属性
        self.detector = None #脸部位置检测器：能够检测图片或视频中是否存在人脸，并定位出位置。一般来说，就是用矩形框框出人脸的区域
        self.predictor = None #脸部特征位置检测器：在获得人脸位置后，进一步检测人脸的特征点，如眼睛、鼻子、嘴巴等，以便更精细地识别人脸。
        self.cap = None #视频流
        self.camSelect = 0 #摄像头选择
        self.isClose = False #线程状态
        #调用 load_Model 方法加载面部特征检测模型。
        self.load_Model()

    #用于加载面部特征检测模型
    def load_Model(self):
        # 初始化DLIB的人脸检测器（HOG），然后创建面部标志物预测
        print("[INFO] loading facial landmark predictor...")
        # 使用dlib.get_frontal_face_detector() 获得脸部位置检测器
        self.detector = dlib.get_frontal_face_detector()
        # 使用dlib.shape_predictor获得脸部特征位置检测器
        self.predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        #在消息信号中发送 “脸部特征检测模型加载成功” 的消息字符串。
        self.msg.emit("脸部特征检测模型加载成功")

    #用于改变摄像头选择。
    def change_cam_select(self, camSelect):
        self.camSelect = camSelect

    #用于结束线程运行
    def close(self):
        self.isClose = True

    #表示线程的运行逻辑
    def run(self):
        #设置 isClose 属性为 False。线程正在运行
        self.isClose = False
        #在窗口消息信号中发送提示消息。
        self.window.emit("请调整摄像头位置，使人脸位于显示框内。调整后请按关闭结束")
        #使用 cv2.VideoCapture 打开视频流，并将该流绑定到 cap 属性。
        self.cap = cv2.VideoCapture(self.camSelect, cv2.CAP_DSHOW)
        #进入循环，读取视频帧并处理
        while True:
            #不断读取视频帧。ret表示是否读到视频帧，frame表示读到的视频帧。
            ret, frame = self.cap.read()
            #用于将读取的视频帧缩小至指定宽度（这里是720），以便更快地进行处理。
            frame = imutils.resize(frame, width=720)
            #将当前帧转换为灰度图像，以便进行面部特征检测。
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #创建自适应直方图均衡对象。
            clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8, 8))
            #对灰度图像进行自适应直方图均衡，增强图像质量。
            gray = clahe.apply(gray)
            #使用detector(gray, 0) 进行脸部位置检测
            rects = self.detector(gray, 0)
            #对每一个检测到的脸部，进行特征检测
            for rect in rects:
                #使用predictor(gray, rect)获得脸部特征位置的信息（68个特征点的位置）
                shape = self.predictor(gray, rect)
                #将脸部特征信息转换为数组array的格式
                shape = face_utils.shape_to_np(shape)
                #使用 get_head_pose 函数计算头部姿态（pitch、yaw、roll）和投影图像等信息。
                reprojectdst, euler_angle = get_head_pose(shape)
                #从头部姿态矩阵中提取 pitch、yaw、roll 旋转角度信息。
                pitch = euler_angle[0, 0]
                yaw = euler_angle[1, 0]
                roll = euler_angle[2, 0]
                #在读取的视频帧上绘制正方体的12条轴线。
                for start, end in line_pairs:
                    start_point = (int(reprojectdst[start][0]), int(reprojectdst[start][1]))
                    end_point = (int(reprojectdst[end][0]), int(reprojectdst[end][1]))
                    cv2.line(frame, start_point, end_point, (0, 0, 255), 2)
                #实时显示计算结果（绘制 pitch、yaw、roll 的文本标签）
                cv2.putText(frame, "pitch: {:5.2f}".format(pitch), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),
                            2)
                cv2.putText(frame, "yaw: {:5.2f}".format(yaw), (180, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                cv2.putText(frame, "roll: {:5.2f}".format(roll), (350, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255),
                            2)
            #发送图像数据信号，将当前帧的数据传递给主线程，用于在界面上显示视频。
            self.picture.emit(frame)
            #线程关闭，退出循环
            if self.isClose:
                break
        #释放视频流。
        self.cap.release()
        self.window.emit("摄像头位置调整结束")

# 继承自QThread类，表示这是一个线程类，可以在后台运行。
class Start_Thread(QThread):
    # 声明信号，用来发送图像数据，字符串消息，窗口消息。
    picture = pyqtSignal(object)
    msg = pyqtSignal(str)
    window = pyqtSignal(str)

    # 初始化各种变量和参数。
    def __init__(self):
        super(Start_Thread, self).__init__()
        self.offDutyTime = 0 # 脱岗时间
        self.predictor = None # 预测器
        self.detector = None # 检测器
        self.filePath = None
        self.cap = None
        self.camSelect = 0
        self.isClose = False
        self.isOffDutyCheck = False
        self.isOpenVideo = False
        self.isShowEye = True
        self.isShowMouth = True
        self.isShowHead = False
        self.isShowKeyPoint = False

        # 加载面部特征模型
        self.load_Model()

    #定义了一个加载模型的方法
    def load_Model(self):
        # 初始化DLIB的人脸检测器（HOG），然后创建面部标志物预测
        print("[INFO] loading facial landmark predictor...")
        # 使用dlib.get_frontal_face_detector() 获得脸部位置检测器
        self.detector = dlib.get_frontal_face_detector()
        # 使用dlib.shape_predictor获得脸部特征位置检测器
        self.predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
        # 发送消息，提示脸部特征检测模型加载成功。
        self.msg.emit("脸部特征检测模型加载成功")

    # 眼部检测功能开关
    def set_show_eye(self, isShowEye):
        self.isShowEye = isShowEye

    # 嘴部检测功能开关
    def set_show_mouth(self, isShowMouth):
        self.isShowMouth = isShowMouth

    # 头部检测功能开关
    def set_show_Head(self, isShowHead):
        self.isShowHead = isShowHead

    # 显示关键点开关
    def set_show_key_point(self, isShowKeyPoint):
        self.isShowKeyPoint = isShowKeyPoint

    # 检测脱岗状态开关
    def change_OffDuty_Check_Status(self, isOffDutyCheck):
        self.isOffDutyCheck = isOffDutyCheck

    # 检测脱岗时间
    def change_OffDuty_Value(self, offDutyTime):
        self.offDutyTime = offDutyTime

    # 选择摄像头
    def change_cam_select(self, camSelect):
        self.camSelect = camSelect

    # 打开视频文件开关
    def set_filePath(self, filePath):
        self.isOpenVideo = True
        self.filePath = filePath

    # 打开摄像头开关
    def set_open_video(self, isOpenVideo):
        self.isOpenVideo = isOpenVideo

    # 关闭检测开关
    def close(self):
        self.isClose = True

    # 用于播放音乐的方法
    @staticmethod
    def playMusic():
        mixer.init()
        mixer.music.load('warning.mp3')
        mixer.music.play()

    # 在循环中进行视频帧的处理、面部特征的检测以及疲劳状态的判断。
    def run(self):
        self.window.emit("开始程序") # 向窗口发送消息
        self.isClose = False # 线程状态设置为运行

        # 打开相机/视频
        if self.isOpenVideo:
            if self.filePath is None:
                self.window.emit("未加载视频，请加载视频后再点击")
                return

            self.cap = cv2.VideoCapture(self.filePath)
            self.msg.emit("视频读取成功")
        else:
            self.cap = cv2.VideoCapture(self.camSelect, cv2.CAP_DSHOW)
            self.msg.emit("相机打开成功")

        # 初始化数据参数（测试次数、测试EAR、MAR和HAR的和、测试次数魔法值）
        test_time = 0
        TEST_TIMES = 100
        ear_sum = 0
        mar_sum = 0
        har_sum = 0

        Detected_TIME_LIMIT = 60
        closed_times = 0
        yawning_times = 0
        pitch_times = 0
        warning_time = 0

        # 阈值（EAR、MAR、HAR、per clos阈值）
        EAR_THRESH = 0
        MAR_THRESH = 0
        HAR_THRESH = 0
        FATIGUE_THRESH = 0.4
        PITCH_THRESH = 6
        offDutyTime = 0

        self.msg.emit("程序正在计算面部特征阈值，请您耐心等待")
        self.window.emit("程序正在计算面部特征阈值，请您耐心等待")

        # 从视频流循环帧
        while True:
            # 进行循环，读取图片，对图片做维度扩大，进行灰度化处理,以及进行拉普拉斯滤波增强对比
            ret, frame = self.cap.read()
            if not ret:
                if self.isOpenVideo:
                    self.window.emit("视频播放结束")
                print('视频结束')
                break

            # 调整当前帧维度（大小）-减少计算量，灰度化-更高效精确，图像增强-图像细节更加清晰明显，
            frame = imutils.resize(frame, width=720) # 将宽度调整为720像素，高度按比例缩放
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 灰度化
            clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8, 8)) # 使用限制对比度自适应直方图均衡化算法（CLAHE）
            # CLAHE算法可以使得图像对比度适应性地进行增强，而不会影响整体的亮度平衡。
            gray = clahe.apply(gray)

            # 使用detector(gray, 0) 检测人脸位置
            rects = self.detector(gray, 0)
            # 脱岗检测（没检测到人脸）
            if not rects:
                # 脱岗检测按钮打开
                if self.isOffDutyCheck:
                    # 脱岗时间+1
                    offDutyTime += 1
                    if offDutyTime >= self.offDutyTime * 30:
                        self.msg.emit("您已经脱岗，请立刻回到岗位")
                        self.window.emit("您已经脱岗，请立刻回到岗位")
                        offDutyTime = 0
            else:
                offDutyTime = 0

            # 面部特征检测
            for rect in rects:
                # 使用predictor(gray, rect)获得脸部特征位置的信息
                shape = self.predictor(gray, rect)

                # 显示关键点
                if self.isShowKeyPoint:
                    # 获取关键点的坐标
                    for point in shape.parts():
                        point_position = (point.x, point.y)# 每个点的坐标
                        cv2.circle(frame, point_position, 3, (255, 8, 0), -1)# 绘制关键点

                # 将脸部特征信息转换为数组array的格式
                shape = face_utils.shape_to_np(shape)
                # 提取左眼、右眼坐标、嘴巴坐标
                leftEye = shape[lStart:lEnd]
                rightEye = shape[rStart:rEnd]
                mouth = shape[mStart:mEnd]
                # 构造函数计算左右眼的EAR平均值、计算嘴巴MAR值
                leftEAR = eye_aspect_ratio(leftEye)
                rightEAR = eye_aspect_ratio(rightEye)
                ear = (leftEAR + rightEAR) / 2.0
                mar = mouth_aspect_ratio(mouth)

                # 获取头部姿态
                reprojectdst, euler_angle = get_head_pose(shape)
                # 取pitch（har）、yaw、roll旋转角度
                pitch = euler_angle[0, 0]
                yaw = euler_angle[1, 0]
                roll = euler_angle[2, 0]
                har = pitch

                # 绘制正方体12轴
                if self.isShowHead:
                    for start, end in line_pairs:
                        start_point = (int(reprojectdst[start][0]), int(reprojectdst[start][1]))
                        end_point = (int(reprojectdst[end][0]), int(reprojectdst[end][1]))
                        cv2.line(frame, start_point, end_point, (0, 0, 255), 2)

                # 实时显示计算结果
                cv2.putText(frame, "ear: {}".format(ear), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "mar: {}".format(mar), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "pitch: {:5.2f}".format(pitch), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0),2)
                cv2.putText(frame, "yaw: {:5.2f}".format(yaw), (180, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                cv2.putText(frame, "roll: {:5.2f}".format(roll), (350, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                # 计算100次ear、mar和har数据求平均值，得到当前使用者眼部、嘴部、头部俯仰的阈值
                if test_time < TEST_TIMES:
                    test_time += 1
                    ear_sum += ear
                    mar_sum += mar
                    har_sum += har

                    if test_time == TEST_TIMES:
                        EAR_THRESH = ear_sum / TEST_TIMES
                        MAR_THRESH = mar_sum / TEST_TIMES
                        HAR_THRESH = har_sum / TEST_TIMES
                        print('眼睛长宽比ear 100次取平均的阈值:{:.2f} '.format(EAR_THRESH))
                        print('嘴部长宽比mar 100次取平均的阈值:{:.2f} '.format(MAR_THRESH))
                        print('头部俯仰角pitch 100次取平均的阈值:{:.2f} '.format(HAR_THRESH))
                        self.msg.emit('眼睛长宽比ear 100次取平均的阈值:{:.2f}'.format(EAR_THRESH))
                        self.msg.emit('嘴部长宽比mar 100次取平均的阈值:{:.2f}'.format(MAR_THRESH))
                        self.msg.emit('头部俯仰角pitch 100次取平均的阈值:{:.2f}'.format(HAR_THRESH))
                    continue

                # 画图：嘴巴、眼睛关键点标注,用矩形框标注人脸
                if self.isShowEye:
                    leftEyeHull = cv2.convexHull(leftEye)
                    rightEyeHull = cv2.convexHull(rightEye)
                    cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                    cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

                if self.isShowMouth:
                    mouthHull = cv2.convexHull(mouth)
                    cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)

                left = rect.left()
                top = rect.top()
                right = rect.right()
                bottom = rect.bottom()
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 3)

                # 疲劳状态检测
                '''
                    计算检测时间内，异常状态的次数
                    异常状态定义:
                    1.EAR 眼睛长宽比 小于0.75倍阈值标记为异常
                    2.MAR 嘴巴长宽比 大于1.6倍阈值标记为异常
                    3.HAR 头部旋转角度 跟阈值差大于标准值标记为异常
                '''
                # EAR_THRESH MAR_THRESH PITCH_THRESH为前面计算的阈值
                if Detected_TIME_LIMIT > 0:
                    Detected_TIME_LIMIT -= 1
                    if ear < 0.75 * EAR_THRESH:
                        closed_times += 1
                    if mar > 1.6 * MAR_THRESH:
                        yawning_times += 1
                    if abs(har - HAR_THRESH) > PITCH_THRESH:
                        pitch_times += 1

                else:
                    # 重置Detected_TIME_LIMIT
                    Detected_TIME_LIMIT = 60
                    isEyeTired = False
                    isYawnTired = False
                    isHeadTired = False

                    # 判断是否疲劳,大于阈值则疲劳
                    if closed_times / Detected_TIME_LIMIT > FATIGUE_THRESH:
                        self.msg.emit("闭眼时长较长")
                        isEyeTired = True

                    if yawning_times / Detected_TIME_LIMIT > FATIGUE_THRESH:
                        self.msg.emit("张嘴时长较长")
                        isYawnTired = True

                    if pitch_times / Detected_TIME_LIMIT > FATIGUE_THRESH:
                        self.msg.emit("低头时长较长")
                        isHeadTired = True

                    # 重置次数
                    closed_times = 0
                    yawning_times = 0
                    pitch_times = 0

                    isWarning = False
                    # 疲劳状态判断
                    if isEyeTired and isYawnTired:
                        warning_time += 2
                        isWarning = True
                    elif isHeadTired and isEyeTired:
                        warning_time += 2
                        isWarning = True
                    elif isEyeTired:
                        warning_time += 1
                        isWarning = True
                    elif isYawnTired:
                        warning_time += 1
                        isWarning = True
                    elif isHeadTired:
                        warning_time += 1
                        isWarning = True
                    else:
                        warning_time = 0

                    if warning_time >= 3:
                        warning_time = 0
                        self.msg.emit("您已经疲劳，请注意休息")
                        self.window.emit("您已经疲劳，请注意休息")
                        self.playMusic()
                    else:
                        if isWarning:
                            winsound.Beep(440, 1000)

            # 窗口显示 show with opencv
            self.picture.emit(frame)

            if self.isClose:
                break

        self.cap.release()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    #sys.exit用于退出python解释器（程序）
    sys.exit(app.exec_())
