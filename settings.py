# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import json
import os

global theme
global timer
global auto

global radiobuttons
radiobuttons = 0


class Ui_Settings_Dialog(object):
    def setupUi(self, Settings_Dialog):
        Settings_Dialog.setObjectName("Settings_Dialog")
        Settings_Dialog.resize(410, 398)
        Settings_Dialog.setWindowIcon(QtGui.QIcon('media/ico_settings.ico'))
        self.verticalLayout = QtWidgets.QVBoxLayout(Settings_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Settings_Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ico_theme = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.ico_theme.sizePolicy().hasHeightForWidth())
        self.ico_theme.setSizePolicy(sizePolicy)
        self.ico_theme.setMaximumSize(QtCore.QSize(30, 30))
        self.ico_theme.setObjectName("ico_theme")
        self.horizontalLayout_2.addWidget(self.ico_theme)
        self.label_theme = QtWidgets.QLabel(self.frame_5)
        self.label_theme.setObjectName("label_theme")
        self.horizontalLayout_2.addWidget(self.label_theme)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_light = QtWidgets.QLabel(self.frame_3)
        self.label_light.setObjectName("label_light")
        self.verticalLayout_2.addWidget(self.label_light)
        self.graphicsView_light = QtWidgets.QLabel(self.frame_3)
        self.graphicsView_light.setObjectName("graphicsView_light")
        self.verticalLayout_2.addWidget(self.graphicsView_light)
        self.radioButton_light = QtWidgets.QRadioButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_light.sizePolicy().hasHeightForWidth())
        self.radioButton_light.setSizePolicy(sizePolicy)
        self.radioButton_light.setText("")
        self.radioButton_light.setCheckable(True)
        self.radioButton_light.setObjectName("radioButton_light")
        self.verticalLayout_2.addWidget(self.radioButton_light)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_dark = QtWidgets.QLabel(self.frame_4)
        self.label_dark.setObjectName("label_dark")
        self.verticalLayout_4.addWidget(self.label_dark)
        self.graphicsView_dark = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_dark.sizePolicy().hasHeightForWidth())
        self.graphicsView_dark.setSizePolicy(sizePolicy)
        self.graphicsView_dark.setObjectName("graphicsView_dark")
        self.verticalLayout_4.addWidget(self.graphicsView_dark)
        self.radioButton_dark = QtWidgets.QRadioButton(self.frame_4)
        self.radioButton_dark.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly)
        self.radioButton_dark.setText("")
        self.radioButton_dark.setCheckable(True)
        self.radioButton_dark.setObjectName("radioButton_dark")
        self.verticalLayout_4.addWidget(self.radioButton_dark)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame)
        self.frame_6 = QtWidgets.QFrame(Settings_Dialog)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ico_autosave = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ico_autosave.sizePolicy().hasHeightForWidth())
        self.ico_autosave.setSizePolicy(sizePolicy)
        self.ico_autosave.setMaximumSize(QtCore.QSize(30, 30))
        self.ico_autosave.setObjectName("ico_autosave")
        self.horizontalLayout_3.addWidget(self.ico_autosave)
        self.label_timer = QtWidgets.QLabel(self.frame_7)
        self.label_timer.setObjectName("label_timer")
        self.horizontalLayout_3.addWidget(self.label_timer)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_auto_save = QtWidgets.QCheckBox(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_auto_save.sizePolicy().hasHeightForWidth())
        self.checkBox_auto_save.setSizePolicy(sizePolicy)
        self.checkBox_auto_save.setObjectName("checkBox_auto_save")
        self.horizontalLayout_5.addWidget(self.checkBox_auto_save)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ico_timer = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ico_timer.sizePolicy().hasHeightForWidth())
        self.ico_timer.setSizePolicy(sizePolicy)
        self.ico_timer.setMaximumSize(QtCore.QSize(30, 30))
        self.ico_timer.setObjectName("ico_timer")
        self.horizontalLayout_4.addWidget(self.ico_timer)
        self.label_time = QtWidgets.QLabel(self.frame_8)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout_4.addWidget(self.label_time)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.tb_minutes = QtWidgets.QTextEdit(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_minutes.sizePolicy().hasHeightForWidth())
        self.tb_minutes.setSizePolicy(sizePolicy)
        self.tb_minutes.setMaximumSize(QtCore.QSize(80, 30))
        self.tb_minutes.setObjectName("tb_minutes")
        self.horizontalLayout_4.addWidget(self.tb_minutes)
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout_5.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.frame_6)
        self.btn_save = QtWidgets.QPushButton(Settings_Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 32))
        self.btn_save.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.btn_save.setObjectName("btn_save")
        self.verticalLayout.addWidget(self.btn_save)

        self.retranslateUi(Settings_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Settings_Dialog)

        #?????????? ????????????????
        pixmap1 = QPixmap("media/dark_mode.jpg")
        self.graphicsView_dark.setPixmap(pixmap1)

        pixmap2 = QPixmap("media/light_mode.jpg")
        self.graphicsView_light.setPixmap(pixmap2)

        self.radioButton_dark.clicked.connect(lambda: self.radiobuttons(0))
        self.radioButton_light.clicked.connect(lambda: self.radiobuttons(1))

        self.checkBox_auto_save.clicked.connect(self.checkBox_auto_save_click)

        self.btn_save.clicked.connect(self.save)

        self.getSettings()
        self.setTheme()

        self.init()

        #??????????????
    def init(self):
        global theme
        global timer
        global auto

        if (theme == "light"):
            self.radioButton_light.setChecked(True)
        elif(theme == "dark"):
            self.radioButton_dark.setChecked(True)

        self.tb_minutes.append(timer)
        
        if(auto == "true"):
            self.checkBox_auto_save.setChecked(True)
        elif(auto == "false"):
            self.checkBox_auto_save.setChecked(False)

    def save(self):
        global theme
        global timer
        global auto

        if (self.checkBox_auto_save.isChecked()):
            auto = "true"
        else:
            auto = "false"
        
        if (self.radioButton_light.isChecked()):
            theme = "light"
        elif (self.radioButton_dark.isChecked()):
            theme = "dark"
        
        timer = self.tb_minutes.toPlainText()

        json_data = {'theme':theme, "timer":timer, "auto":auto}
        with open("settings.json", "w") as f:
            f.write(json.dumps(json_data))
        

    def checkBox_auto_save_click(self):
        if (self.checkBox_auto_save.isChecked()):
            self.tb_minutes.setDisabled(False)
        else:
            self.tb_minutes.setDisabled(True)

    def radiobuttons(self, value):
        if (value == 0):
            self.radioButton_dark.setChecked(True)
            self.radioButton_light.setChecked(False)
        elif(value == 1):
            self.radioButton_dark.setChecked(False)
            self.radioButton_light.setChecked(True)

    def getSettings(self):                  #?????????????????? ????????????????
        global theme
        global timer
        global auto
        if (os.path.exists("settings.json") == False):
            json_data = {'theme':'light', "timer":"10", "auto":"true"}
            with open("settings.json", "w") as f:
                f.write(json.dumps(json_data))
        with open("settings.json") as f:
            templates = json.load(f)
        theme = templates["theme"]
        timer = templates["timer"]
        auto = templates["auto"]
    
    def setTheme(self):
        global theme
        if(theme == "light"):
            self.frame.setStyleSheet(
                """
                background-color: #F5F5F5;
                """
            )

            self.frame_6.setStyleSheet(
                """
                background-color: #F5F5F5;
                """
            )

            self.btn_save.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                color: black;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                    color: black;
                }
                
                """
            )

            self.label_theme.setStyleSheet(
                """
                color: black;
                """
            )

            self.label_light.setStyleSheet(
                """
                color: black;
                """
            )

            self.label_dark.setStyleSheet(
                """
                color: black;
                """
            )

            self.label_timer.setStyleSheet(
                """
                color: black;
                """
            )

            self.checkBox_auto_save.setStyleSheet(
                """
                color: black;
                """
            )

            self.label_time.setStyleSheet(
                """
                color: black;
                """
            )

            self.label_5.setStyleSheet(
                """
                color: black;
                """
            )

            self.label_6.setStyleSheet(
                """
                color: black;
                """
            )

            self.tb_minutes.setStyleSheet(
                """
                color: black;
                """
            )

            pixmap1 = QPixmap("media/ico_theme.png")
            self.ico_theme.setPixmap(pixmap1)

            pixmap2 = QPixmap("media/ico_auto.png")
            self.ico_autosave.setPixmap(pixmap2)

            pixmap3 = QPixmap("media/ico_timer.png")
            self.ico_timer.setPixmap(pixmap3)

        elif(theme == "dark"):
            self.frame.setStyleSheet(
                """
                background-color: #1b1b1b;
                """
            )

            self.frame_6.setStyleSheet(
                """
                background-color: #1b1b1b;
                """
            )

            self.btn_save.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                color: white;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                    color: white;
                }
                
                """
            )

            self.label_theme.setStyleSheet(
                """
                color: white;
                """
            )

            self.label_light.setStyleSheet(
                """
                color: white;
                """
            )

            self.label_dark.setStyleSheet(
                """
                color: white;
                """
            )

            self.label_timer.setStyleSheet(
                """
                color: white;
                """
            )

            self.checkBox_auto_save.setStyleSheet(
                """
                color: white;
                """
            )

            self.label_time.setStyleSheet(
                """
                color: white;
                """
            )

            self.label_5.setStyleSheet(
                """
                color: white;
                """
            )

            self.label_6.setStyleSheet(
                """
                color: white;
                """
            )

            self.tb_minutes.setStyleSheet(
                """
                color: white;
                """
            )

            pixmap1 = QPixmap("media/dark_mode/ico_theme_dark.png")
            self.ico_theme.setPixmap(pixmap1)

            pixmap2 = QPixmap("media/dark_mode/ico_auto_dark.png")
            self.ico_autosave.setPixmap(pixmap2)

            pixmap3 = QPixmap("media/dark_mode/ico_timer_dark.png")
            self.ico_timer.setPixmap(pixmap3)


    def retranslateUi(self, Settings_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Settings_Dialog.setWindowTitle(_translate("Settings_Dialog", "??????????????????"))
        self.label_theme.setText(_translate("Settings_Dialog", "????????"))
        self.label_light.setText(_translate("Settings_Dialog", "??????????????"))
        self.label_dark.setText(_translate("Settings_Dialog", "????????????"))
        self.label_timer.setText(_translate("Settings_Dialog", "????????????????????????????"))
        self.checkBox_auto_save.setText(_translate("Settings_Dialog", "???????????????????????????? ????????????????"))
        self.label_time.setText(_translate("Settings_Dialog", "??????????"))
        self.label_5.setText(_translate("Settings_Dialog", "?????????????????? ????????????"))
        self.label_6.setText(_translate("Settings_Dialog", "??????????"))
        self.btn_save.setText(_translate("Settings_Dialog", "??????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings_Dialog = QtWidgets.QDialog()
    ui = Ui_Settings_Dialog()
    ui.setupUi(Settings_Dialog)
    Settings_Dialog.show()
    sys.exit(app.exec_())
