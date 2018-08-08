#!/usr/bin/env python
# -*- coding: utf-8
from PyQt5.QtWidgets import (QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QLabel,QDialog,QWidget,QCheckBox)
from PyQt5.QtGui import QFont,QPixmap
from PyQt5.QtCore import Qt
import sys
import ctypes.wintypes
WM_NCACTIVATE = 0x0086
##样式设置
title_label_style = '''
QLabel{
    color: #FFFFFF;
	font-weight: bold;
	font-size: 15px;
	font-family: "Times New Roman", Times, serif;}
'''
close_button_style = '''
QPushButton{
    background: transparent;
    color: #D6D6D7;
    font-size: 16px;}
QPushButton:hover{
    background: #E81123;
    color: #FFFFF;}
'''
msg_label_style = '''
QLabel{
    color: #000000;
	font-size: 15px;
	font-family: "Times New Roman", Times, serif;}
'''
button_style = '''
QPushButton{
    border-bottom: 1px solid #404040;
	border-radius: 5px;
	background: #CAE1FF;
	color: #000;
	font-size: 15px;
	text-transform: uppercase;
	font-family: sans-serif;}
QPushButton:hover{
    background: #6CA6CD;
	color: #000000;}
'''
MsgBox_style = '''
MsgBox[active="true"] {
    background: #FFFFFF;}
MsgBox[active="false"] {
    background: #051B3D;}

'''
class MsgBox(QDialog):
    def __init__(self, *args, **kwargs):
        super(MsgBox, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Dialog)
        self.setObjectName("MsgBox")
        self.setProperty("active", False)
        self.setStyleSheet(MsgBox_style)
        self.createGUI()
        self.connects()
    def createGUI(self):
        m_layout = QVBoxLayout()
        m_layout.setSpacing(10)
        m_layout.setContentsMargins(0, 0, 0, 0)
        #########标题栏##########
        title_group = QWidget(self)
        title_group.setStyleSheet("background: #1E90FF;")
        title_group.setFixedHeight(30)
        self.title_label = QLabel(title_group)
        self.title_label.setStyleSheet(title_label_style)
        self.title_label.setObjectName('title_label')
        self.title_label.setFixedHeight(30)

        close_button_font = self.font() or QFont()
        close_button_font.setFamily('Webdings')
        self.close_button = QPushButton('r', title_group, font=close_button_font)
        self.close_button.setStyleSheet(close_button_style)
        self.close_button.setFixedSize(30,30)

        title_layout = QHBoxLayout(title_group)
        title_layout.setContentsMargins(0, 0, 0, 0)
        title_layout.addSpacing(10)
        title_layout.addWidget(self.title_label,alignment=Qt.AlignLeft)
        title_layout.addWidget(self.close_button,alignment=Qt.AlignTop)

        #########提示内容##########
        msg_group = QWidget(self)
        msg_group.setStyleSheet("background: #FFFFFF;")
        self.img_label = QLabel(msg_group)
        self.img_label.setFixedSize(40,40)
        self.img_label.setScaledContents(True)

        self.msg_label = QLabel(msg_group)
        self.msg_label.setStyleSheet(msg_label_style)
        self.msg_label.setMaximumSize(600, 480)
        self.msg_label.setMinimumSize(200, 80)
        # self.msg_label.setWordWrap(True)
        self.msg_label.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
        msg_layout = QHBoxLayout(msg_group)
        msg_layout.setContentsMargins(0, 0, 0, 0)
        msg_layout.setSpacing(10)
        msg_layout.addSpacing(10)
        msg_layout.addWidget(self.img_label)
        msg_layout.addWidget(self.msg_label)
        msg_layout.addSpacing(5)
        ##########################

        #########按钮栏##########
        button_group = QWidget(self)
        button_group.setStyleSheet("background: #EBEBEB;")
        button_group.setFixedHeight(30)
        self.cancel_button = QPushButton('取消', button_group)
        self.cancel_button.setStyleSheet(button_style)
        self.cancel_button.setFixedSize(60, 25)
        self.ok_button = QPushButton('确认',button_group)
        self.ok_button.setStyleSheet(button_style)
        self.ok_button.setFixedSize(60, 25)
        self.checkbox = QCheckBox(button_group)
        button_layout = QHBoxLayout(button_group)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setDirection(1)
        button_layout.setSpacing(5)
        button_layout.addSpacing(10)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.ok_button)
        button_layout.addStretch(1)
        button_layout.addWidget(self.checkbox,alignment=Qt.AlignLeft)
        button_layout.addSpacing(5)
        self.checkbox.hide()
        ######主布局
        m_layout.addWidget(title_group)
        m_layout.addWidget(msg_group)
        m_layout.addWidget(button_group)
        self.setLayout(m_layout)

    def connects(self):
        self.close_button.clicked.connect(self.reject)
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def about(self,title,msg):
        self.title_label.setText(str(title))
        self.msg_label.setText(msg)
        self.img_label.setPixmap(QPixmap('imgs/about.png'))
        self.checkbox.hide()
        self.ok_button.setFocus()

    def question(self,title,msg,checkbox=False):
        self.title_label.setText(str(title))
        self.msg_label.setText(msg)
        self.img_label.setPixmap(QPixmap('imgs/question.png'))
        self.cancel_button.setFocus()
        if checkbox:
            self.checkbox.setText(checkbox)
            self.checkbox.show()
    def information(self,title,msg):
        self.title_label.setText(str(title))
        self.msg_label.setText(msg)
        self.img_label.setPixmap(QPixmap('imgs/information.png'))
        self.cancel_button.hide()

    def warning(self, title, msg):
        self.title_label.setText(str(title))
        self.msg_label.setText(msg)
        self.img_label.setPixmap(QPixmap('imgs/warning.png'))
        self.cancel_button.hide()
    def error(self, title, msg):
        self.title_label.setText(str(title))
        self.msg_label.setText(msg)
        self.img_label.setPixmap(QPixmap('imgs/error.png'))
        self.cancel_button.hide()
    def critical(self, title, msg):
        self.title_label.setText(str(title))
        self.msg_label.setText(msg)
        self.img_label.setPixmap(QPixmap('imgs/critical.png'))
        self.cancel_button.hide()


    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)
    ###窗口闪烁效果####
    def activeAnimation(self, actived):
        """边框闪烁动画
        :param actived: 是否激活
        """
        # 修改控件的自定义属性
        self.setProperty('active', actived)
        # 刷新它的样式
        self.style().polish(self)

    def nativeEvent(self, eventType, message):
        retval, result = QDialog.nativeEvent(self, eventType, message)
        if eventType == 'windows_generic_MSG':
            msg = ctypes.wintypes.MSG.from_address(message.__int__())
            if msg.message == WM_NCACTIVATE:
                # 绘制模态窗口的边框效果
                self.activeAnimation(msg.wParam == 1)
        return retval, result

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('test')
        self.resize(400, 300)
        wl = QVBoxLayout(self)
        btn1 = QPushButton('question')
        btn2 = QPushButton('about')
        btn3 = QPushButton('information')
        btn4 = QPushButton('warning')
        btn5 = QPushButton('error')
        btn6 = QPushButton('critical')
        btn1.clicked.connect(self.do_btn1)
        btn2.clicked.connect(self.do_btn2)
        btn3.clicked.connect(self.do_btn3)
        btn4.clicked.connect(self.do_btn4)
        btn5.clicked.connect(self.do_btn5)
        btn6.clicked.connect(self.do_btn6)
        for btn in (btn1, btn2, btn3, btn4, btn5,btn6):
            wl.addWidget(btn)
    def do_btn1(self):
        msgb = MsgBox(self)
        msgb.question('询问', '是否删除该文件？' ,checkbox='不再提醒')
        if msgb.exec_():
            if msgb.checkbox.isChecked():
                print("确认操作，并且不再提示")
            else:
                print("确认操作，下次还会提示")
        else:
            print("取消操作")
    def do_btn2(self):
        msgb = MsgBox(self)
        msgb.about('关于', '1.此demo为自定义类QMessageBox的提示框。\n2.使用QDialog实现的自定义模态窗。')
        if msgb.exec_():
            print("确认操作")
        else:
            print("取消操作")

    def do_btn3(self):
        msgb = MsgBox(self)
        msgb.information('消息', '此处应有内容')
        if msgb.exec_():
            print("确认操作")
        else:
            print("取消操作")

    def do_btn4(self):
        msgb = MsgBox(self)
        msgb.warning('警告', '此处应有内容')
        if msgb.exec_():
            print("确认操作")
        else:
            print("取消操作")
        del msgb

    def do_btn5(self):
        msgb = MsgBox(self)
        msgb.error('错误', '用户密码有误！')
        if msgb.exec_():
            print("确认操作")
        else:
            print("取消操作")
        del msgb

    def do_btn6(self):
        msgb = MsgBox(self)
        msgb.critical('天呐', '问题有点严重！')
        if msgb.exec_():
            print("确认操作")
        else:
            print("取消操作")
        del msgb


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     msgb = MsgBox()
#     # msgb.setInfo('警告','内容内容内容内容内容内容','title.png',False)
#     msgb.about('警告', '内容内容内容内容内容内容')
#     msgb.show()
#
#     # with open('main.css', 'r') as css:
#     #     StyleSheet = css.read()
#     # # app.setStyle("cleanlooks")
#     sys.exit(app.exec_())
