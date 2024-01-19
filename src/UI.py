#导入pyqt5模块
from PyQt5 import QtCore, QtGui, QtWidgets
##QtCore模块包含了一些核心的非图形功能，例如事件循环和信号槽机制。
#QtGui模块包含了一些基本的图形功能，例如字体、颜色和绘图工具。
#QtWidgets模块包含了一些GUI元素，例如窗口、标签、按钮、复选框等，用于创建用户界面。

#用于设计主窗口。创建各个控件，标签，线，按钮，复选框等，并指定了它们的字体，位置等属性
class Ui_MainWindow(object):
    #定义setupUi方法，该方法接收一个MainWindow对象作为参数。
    def setupUi(self, MainWindow):
        #给这个实例命了个名字（唯一标识符）。方便类外界访问。
        MainWindow.setObjectName("MainWindow")
        #设置MainWindow对象的大小为1052x643像素。
        MainWindow.resize(1052, 643)
        #创建一个QWidget对象，作为MainWindow对象的子控件
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 创建一个QLabel标签对象，作为self.centralwidget的子控件，赋给label
        self.label = QtWidgets.QLabel(self.centralwidget)
        # 设置self.label的位置和大小为左上角坐标(10, 10)、宽度101像素、高度31像素。
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        #创建字体对象
        font = QtGui.QFont()
        #设置字体类型
        font.setFamily("宋体")
        #设置字体大小
        font.setPointSize(15)
        #是否加粗
        font.setBold(True)
        #加粗程度
        font.setWeight(75)
        #设置标签label的字体字样
        self.label.setFont(font)
        #给这个实例命了个名字（唯一标识符）。方便类外界访问。
        self.label.setObjectName("label")

        #创建一个QFrame类（横向线框）的实例，该QFrame将会作为界面元素添加到self.centralwidget中。
        self.line = QtWidgets.QFrame(self.centralwidget)
        #设置self.line的几何属性，包括其在父组件中的位置和大小。坐标，宽度，高度
        self.line.setGeometry(QtCore.QRect(274, 1, 20, 641))
        #设置self.line的外观形状为垂直线。
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        #设置self.line的外观阴影效果为sunken（凹陷）。
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        #给这个实例命了个名字（唯一标识符）。方便类外界访问。
        self.line.setObjectName("line")

        #创建标签label_2。
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        #创建line_2水平线
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(80, 50, 201, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        #创建一个名为 Cam_Select 的下拉框，并将其添加到名为 centralwidget 的父级部件中。
        self.Cam_Select = QtWidgets.QComboBox(self.centralwidget)
        #设置下拉框在父级部件中的位置和大小
        self.Cam_Select.setGeometry(QtCore.QRect(10, 80, 111, 31))
        # 设置下拉框的字体为黑体，字号为10。
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Cam_Select.setFont(font)
        #向下拉框中添加一个空选项。
        self.Cam_Select.addItem("")
        self.Cam_Select.addItem("")
        self.Cam_Select.addItem("")
        # 给这个实例命了个名字（唯一标识符）。方便类外界访问。
        self.Cam_Select.setObjectName("Cam_Select")

        #创建一个名为Button_OpenVideo的按钮，并其添加到名为 centralwidget 的级部件中。
        self.Button_OpenVideo = QtWidgets.QPushButton(self.centralwidget)
        #设置了 Button_OpenVideo 按钮在 centralwidget 部件中的位置和大小。
        self.Button_OpenVideo.setGeometry(QtCore.QRect(150, 80, 111, 31))
        #按钮的字体样式为黑体，字号为10。
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Button_OpenVideo.setFont(font)
        #给这个实例命了个名字（唯一标识符）。方便类外界访问。
        self.Button_OpenVideo.setObjectName("Button_OpenVideo")

        #创建Button_Start按钮
        self.Button_Start = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Start.setGeometry(QtCore.QRect(150, 160, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Button_Start.setFont(font)
        self.Button_Start.setObjectName("Button_Start")

        #创建line_4水平线
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 30, 271, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        #创建label_5文本标签
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 200, 71, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        #创建了一个名为 offDuty_Check 的复选框，并将其添加到 centralwidget 部件。
        self.offDuty_Check = QtWidgets.QCheckBox(self.centralwidget)
        self.offDuty_Check.setGeometry(QtCore.QRect(10, 220, 87, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.offDuty_Check.setFont(font)
        self.offDuty_Check.setObjectName("offDuty_Check")

        #创建label_6标签
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        #创建了一个名为 offDuty_Time 的数值调节框，并将其添加到 centralwidget 部件中。
        self.offDuty_Time = QtWidgets.QSpinBox(self.centralwidget)
        self.offDuty_Time.setGeometry(QtCore.QRect(210, 220, 46, 31))
        self.offDuty_Time.setObjectName("offDuty_Time")

        #创建line_5水平线
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(80, 200, 201, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        #创建label_9标签
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 300, 71, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        #创建了一个名为 output_Window 的文本浏览框，并将其添加到 centralwidget 部件。
        self.output_Window = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_Window.setGeometry(QtCore.QRect(11, 331, 261, 301))
        self.output_Window.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 119));")
        self.output_Window.setObjectName("output_Window")

        #创建了一个名为 graphicsView 的图形视图，并将其添加到 centralwidget 部件中。
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(300, 50, 730, 550))
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setObjectName("graphicsView")

        #创建line_7水平线
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(80, 300, 201, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        #创建Button_End按钮
        self.Button_End = QtWidgets.QPushButton(self.centralwidget)
        self.Button_End.setGeometry(QtCore.QRect(150, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Button_End.setFont(font)
        self.Button_End.setObjectName("Button_End")

        #创建Button_AdjustCamera_Location按钮
        self.Button_AdjustCamera_Location = QtWidgets.QPushButton(self.centralwidget)
        self.Button_AdjustCamera_Location.setGeometry(QtCore.QRect(10, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.Button_AdjustCamera_Location.setFont(font)
        self.Button_AdjustCamera_Location.setObjectName("Button_AdjustCamera_Location")

        #创建widget部件，并将其添加到centralwidget部件中
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 160, 141, 31))
        self.widget.setObjectName("widget")

        #创建了一个名为 video 的复选框，并将其添加到widget部件中
        self.video = QtWidgets.QCheckBox(self.widget)
        self.video.setGeometry(QtCore.QRect(10, 0, 87, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.video.setFont(font)
        self.video.setChecked(False)
        self.video.setAutoExclusive(True)
        self.video.setObjectName("video")

        #创建cam复选框
        self.cam = QtWidgets.QCheckBox(self.widget)
        self.cam.setGeometry(QtCore.QRect(70, 0, 87, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.cam.setFont(font)
        #设置了 cam 复选框的初始选中状态为选中。
        self.cam.setChecked(True)
        #设置了 cam 复选框的自动排他性，即当一个复选框被选中时，其他复选框会自动取消选中。
        self.cam.setAutoExclusive(True)
        self.cam.setObjectName("cam")

        #设置show_key_point复选框
        self.show_key_point = QtWidgets.QCheckBox(self.centralwidget)
        self.show_key_point.setGeometry(QtCore.QRect(10, 270, 87, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.show_key_point.setFont(font)
        self.show_key_point.setObjectName("show_key_point")

        #设置line_6线
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(80, 250, 201, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        #设置label_8标签
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 250, 71, 16))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        #创建show_head复选框
        self.show_head = QtWidgets.QCheckBox(self.centralwidget)
        self.show_head.setGeometry(QtCore.QRect(220, 270, 61, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.show_head.setFont(font)
        self.show_head.setObjectName("show_head")

        #创建show_eye复选框
        self.show_eye = QtWidgets.QCheckBox(self.centralwidget)
        self.show_eye.setGeometry(QtCore.QRect(90, 270, 51, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.show_eye.setFont(font)
        self.show_eye.setObjectName("show_eye")
        self.show_eye.setChecked(True)

        #创建show_mouth复选框
        self.show_mouth = QtWidgets.QCheckBox(self.centralwidget)
        self.show_mouth.setGeometry(QtCore.QRect(160, 270, 51, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.show_mouth.setFont(font)
        self.show_mouth.setObjectName("show_mouth")
        self.show_mouth.setChecked(True)

        #将 MainWindow 的中心部件设置为 centralwidget。
        MainWindow.setCentralWidget(self.centralwidget)
        #为 actionExit 操作对象设置一个唯一对象名称。
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        #调用 retranslateUi 方法为 MainWindow 设置界面的文本。
        self.retranslateUi(MainWindow)
        #调用 QtCore.QMetaObject.connectSlotsByName 方法将对象和槽函数进行连接。
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #这段代码是用于设置界面的文本和按钮的显示文字
    def retranslateUi(self, MainWindow):
        #_translate 是一个用于翻译文本的函数，用于为界面的各个元素设置文本
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "参数设置"))
        self.label_2.setText(_translate("MainWindow", "视频设置"))
        self.Cam_Select.setItemText(0, _translate("MainWindow", "摄像头0"))
        self.Cam_Select.setItemText(1, _translate("MainWindow", "摄像头1"))
        self.Cam_Select.setItemText(2, _translate("MainWindow", "摄像头2"))
        self.Button_OpenVideo.setText(_translate("MainWindow", "打开视频文件"))
        self.Button_Start.setText(_translate("MainWindow", "开始"))
        self.label_5.setText(_translate("MainWindow", "脱岗检测"))
        self.offDuty_Check.setText(_translate("MainWindow", "脱岗检测"))
        self.label_6.setText(_translate("MainWindow", "脱离时间(s)："))
        self.label_9.setText(_translate("MainWindow", "状态输出"))
        self.Button_End.setText(_translate("MainWindow", "结束"))
        self.Button_AdjustCamera_Location.setText(_translate("MainWindow", "调整摄像头位置"))
        self.video.setText(_translate("MainWindow", "视频"))
        self.cam.setText(_translate("MainWindow", "摄像头"))
        self.show_key_point.setText(_translate("MainWindow", "关键点"))
        self.label_8.setText(_translate("MainWindow", "显示设置"))
        self.show_head.setText(_translate("MainWindow", "头部"))
        self.show_eye.setText(_translate("MainWindow", "眼睛"))
        self.show_mouth.setText(_translate("MainWindow", "嘴巴"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
