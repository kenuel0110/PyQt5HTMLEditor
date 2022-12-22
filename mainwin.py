# -*- coding: utf-8 -*-

#PyQt5
#PyQtWebEngine
#PyQt5-sip
#PILLow
#plyer 
#pywin32
#docx2python
#json


from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import QPrintDialog
from PyQt5 import QtWidgets, QtCore, QtGui
from settings import Ui_Settings_Dialog
from plyer import notification
from PyQt5.QtWidgets import *
from win32com import client
from PyQt5.QtCore import *
from PIL import ImageColor
from PyQt5.QtGui import *
from threading import *
import platform
import json
import uuid
import time
import sys
import os

#from docx2python import docx2python

global openBrowserValue
openBrowserValue = False

global PC_system

global filePath

global outFilePathHTML

global outFilePathHTMLDoc

global theme
global timer
global auto

global firstSave
firstSave = "FirstOpen"

global name
name = ""

global oldPath
oldPath = ""

global selectionStart
global selectionEnd

global font
font = "Times New Roman"

IMAGE_EXTENSIONS = ['.jpg','.png','.bmp']   #формат поддержеваемых изображений

def platform_check():               #Проверка операционой системы
    global PC_system
    PC_system = platform.system()

platform_check()

def hexuuid():
    return uuid.uuid4().hex

def splitext(p):
    return os.path.splitext(p)[1].lower()

class TextEdit(QTextEdit):                  #кастомный QTextEdit для поддержки drag and drop с отображением изображения

    def canInsertFromMimeData(self, source):

        if source.hasImage():
            return True
        else:
            return super(TextEdit, self).canInsertFromMimeData(source)

    def insertFromMimeData(self, source):

        cursor = self.textCursor()
        document = self.document()

        if source.hasUrls():

            for u in source.urls():
                file_ext = splitext(str(u.toLocalFile()))
                if u.isLocalFile() and file_ext in IMAGE_EXTENSIONS:
                    image = QImage(u.toLocalFile())
                    document.addResource(QTextDocument.ImageResource, u, image)
                    cursor.insertImage(u.toLocalFile())

                else:
                    #если нет изображения, то цикл вылетает и qt продолжает работать
                    break

            else:
                # если с изображением всё хорошо, то  вылетает тут
                return


        elif source.hasImage():
            image = source.imageData()
            uuid = hexuuid()
            document.addResource(QTextDocument.ImageResource, uuid, image)
            cursor.insertImage(uuid)
            return

        super(TextEdit, self).insertFromMimeData(source)

class HyperLinks():         #класс формирования гипер ссылки
    link = ""
    startPos = 0
    endPos = 0

global linksList
linksList = []

class Ui_HTML_Editor(object):
    def setupUi(self, HTML_Editor):
        HTML_Editor.setObjectName("HTML_Editor")
        HTML_Editor.resize(960, 600)
        HTML_Editor.setWindowIcon(QtGui.QIcon('media/iconApp.ico'))
        
        self.mainwidget = QtWidgets.QWidget(HTML_Editor)
        self.mainwidget.setObjectName("mainwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.mainwidget)
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, 5)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.main_frame_text = QtWidgets.QFrame(self.mainwidget)
        self.main_frame_text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame_text.setFrameShadow(QtWidgets.QFrame.Raised)


        ###########################___Text_Editor____###########################
        self.main_frame_text.setObjectName("main_frame_text")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame_text)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.panel_text_frame = QtWidgets.QFrame(self.main_frame_text)
        self.panel_text_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.panel_text_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.panel_text_frame.setObjectName("panel_text_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.panel_text_frame)
        self.horizontalLayout.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_new = QtWidgets.QPushButton(self.panel_text_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_new.setObjectName("btn_new")
        self.horizontalLayout.addWidget(self.btn_new)
        
        self.btn_open = QtWidgets.QPushButton(self.panel_text_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_open.sizePolicy().hasHeightForWidth())
        self.btn_open.setSizePolicy(sizePolicy)
        self.btn_open.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout.addWidget(self.btn_open)
        
        self.btn_save = QtWidgets.QPushButton(self.panel_text_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)

        self.btn_print = QtWidgets.QPushButton(self.panel_text_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_print.setObjectName("btn_print")
        self.horizontalLayout.addWidget(self.btn_print)

        self.btn_settings = QtWidgets.QPushButton(self.panel_text_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QtCore.QSize(50, 50))
        self.btn_settings.setObjectName("btn_settings")
        self.horizontalLayout.addWidget(self.btn_settings)

        self.line7 = QtWidgets.QFrame(self.panel_text_frame)
        self.line7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line7.setObjectName("line7")
        self.horizontalLayout.addWidget(self.line7)

        self.copy_cut_paste_frame = QtWidgets.QFrame(self.panel_text_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copy_cut_paste_frame.sizePolicy().hasHeightForWidth())
        self.copy_cut_paste_frame.setSizePolicy(sizePolicy)
        self.copy_cut_paste_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.copy_cut_paste_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.copy_cut_paste_frame.setObjectName("copy_cut_paste_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.copy_cut_paste_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_paste = QtWidgets.QPushButton(self.copy_cut_paste_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_paste.sizePolicy().hasHeightForWidth())
        self.btn_paste.setSizePolicy(sizePolicy)
        self.btn_paste.setMinimumSize(QtCore.QSize(24, 24))
        self.btn_paste.setMaximumSize(QtCore.QSize(27, 27))
        self.btn_paste.setObjectName("btn_paste")
        self.verticalLayout_3.addWidget(self.btn_paste)
        self.btn_copy = QtWidgets.QPushButton(self.copy_cut_paste_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_copy.sizePolicy().hasHeightForWidth())
        self.btn_copy.setSizePolicy(sizePolicy)
        self.btn_copy.setMinimumSize(QtCore.QSize(24, 24))
        self.btn_copy.setMaximumSize(QtCore.QSize(27, 27))
        self.btn_copy.setObjectName("btn_copy")
        self.verticalLayout_3.addWidget(self.btn_copy)
        self.btn_cut = QtWidgets.QPushButton(self.copy_cut_paste_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cut.sizePolicy().hasHeightForWidth())
        self.btn_cut.setSizePolicy(sizePolicy)
        self.btn_cut.setMinimumSize(QtCore.QSize(24, 24))
        self.btn_cut.setMaximumSize(QtCore.QSize(27, 27))
        self.btn_cut.setObjectName("btn_cut")
        self.verticalLayout_3.addWidget(self.btn_cut)
        self.horizontalLayout.addWidget(self.copy_cut_paste_frame)
        self.line = QtWidgets.QFrame(self.panel_text_frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.font_panel_frame = QtWidgets.QFrame(self.panel_text_frame)
        self.font_panel_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.font_panel_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.font_panel_frame.setObjectName("font_panel_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.font_panel_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cb_frame = QtWidgets.QFrame(self.font_panel_frame)
        self.cb_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cb_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cb_frame.setObjectName("cb_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.cb_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.fontComboBox = QtWidgets.QFontComboBox(self.cb_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())

        self.fontComboBox.setSizePolicy(sizePolicy)
        self.fontComboBox.setMinimumSize(QtCore.QSize(170, 30))
        self.fontComboBox.setObjectName("fontComboBox")

        self.horizontalLayout_2.addWidget(self.fontComboBox)
        self.sizeBox = QtWidgets.QComboBox(self.cb_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.sizeBox.setMinimumSize(QtCore.QSize(50, 30))
        self.sizeBox.setObjectName("sizeBox")
        self.horizontalLayout_2.addWidget(self.sizeBox)

        self.verticalLayout_4.addWidget(self.cb_frame)
        self.BUI_frame = QtWidgets.QFrame(self.font_panel_frame)
        self.BUI_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BUI_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BUI_frame.setObjectName("BUI_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.BUI_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_Bold = QtWidgets.QPushButton(self.BUI_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Bold.sizePolicy().hasHeightForWidth())
        self.btn_Bold.setSizePolicy(sizePolicy)
        self.btn_Bold.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_Bold.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_Bold.setObjectName("btn_Bold")
        self.horizontalLayout_3.addWidget(self.btn_Bold)
        self.btn_underline = QtWidgets.QPushButton(self.BUI_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_underline.sizePolicy().hasHeightForWidth())
        self.btn_underline.setSizePolicy(sizePolicy)
        self.btn_underline.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_underline.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_underline.setObjectName("btn_underline")
        self.horizontalLayout_3.addWidget(self.btn_underline)
        self.btn_italic = QtWidgets.QPushButton(self.BUI_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_italic.sizePolicy().hasHeightForWidth())
        self.btn_italic.setSizePolicy(sizePolicy)
        self.btn_italic.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_italic.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_italic.setObjectName("btn_italic")
        self.horizontalLayout_3.addWidget(self.btn_italic)

        self.line_5 = QtWidgets.QFrame(self.BUI_frame)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_3.addWidget(self.line_5)

        self.btn_make_link = QtWidgets.QPushButton(self.BUI_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_make_link.sizePolicy().hasHeightForWidth())
        self.btn_make_link.setSizePolicy(sizePolicy)
        self.btn_make_link.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_make_link.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_make_link.setObjectName("btn_make_link")
        self.horizontalLayout_3.addWidget(self.btn_make_link)

       # self.btn_window_link = QtWidgets.QPushButton(self.BUI_frame)
       # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
       # sizePolicy.setHorizontalStretch(0)
       # sizePolicy.setVerticalStretch(0)
       # sizePolicy.setHeightForWidth(self.btn_window_link.sizePolicy().hasHeightForWidth())
       # self.btn_window_link.setSizePolicy(sizePolicy)
       # self.btn_window_link.setMinimumSize(QtCore.QSize(30, 30))
       # self.btn_window_link.setMaximumSize(QtCore.QSize(30, 30))
       # self.btn_window_link.setObjectName("btn_window_link")
       # self.horizontalLayout_3.addWidget(self.btn_window_link)

        self.line_2 = QtWidgets.QFrame(self.BUI_frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.btn_sizeUP = QtWidgets.QPushButton(self.BUI_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sizeUP.sizePolicy().hasHeightForWidth())
        self.btn_sizeUP.setSizePolicy(sizePolicy)
        self.btn_sizeUP.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_sizeUP.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_sizeUP.setObjectName("btn_sizeUP")
        self.horizontalLayout_3.addWidget(self.btn_sizeUP)
        self.btn_sizeDOWN = QtWidgets.QPushButton(self.BUI_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sizeDOWN.sizePolicy().hasHeightForWidth())
        self.btn_sizeDOWN.setSizePolicy(sizePolicy)
        self.btn_sizeDOWN.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_sizeDOWN.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_sizeDOWN.setObjectName("btn_sizeDOWN")
        self.horizontalLayout_3.addWidget(self.btn_sizeDOWN)
        self.btn_font_color = QtWidgets.QPushButton(self.BUI_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_font_color.sizePolicy().hasHeightForWidth())
        self.btn_font_color.setSizePolicy(sizePolicy)
        self.btn_font_color.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_font_color.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_font_color.setObjectName("btn_font_color")
        self.horizontalLayout_3.addWidget(self.btn_font_color)
        self.verticalLayout_4.addWidget(self.BUI_frame)
        self.horizontalLayout.addWidget(self.font_panel_frame)

        self.line_4 = QtWidgets.QFrame(self.panel_text_frame)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)

        self.aligns_frame = QtWidgets.QFrame(self.panel_text_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aligns_frame.sizePolicy().hasHeightForWidth())
        self.aligns_frame.setSizePolicy(sizePolicy)
        self.aligns_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.aligns_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.aligns_frame.setObjectName("aligns_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.aligns_frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btn_leftAlign = QtWidgets.QPushButton(self.aligns_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_leftAlign.sizePolicy().hasHeightForWidth())
        self.btn_leftAlign.setSizePolicy(sizePolicy)
        self.btn_leftAlign.setMinimumSize(QtCore.QSize(24, 24))
        self.btn_leftAlign.setMaximumSize(QtCore.QSize(27, 27))
        self.btn_leftAlign.setText("")
        self.btn_leftAlign.setObjectName("btn_leftAlign")
        self.verticalLayout_9.addWidget(self.btn_leftAlign)
        self.btn_centerAlign = QtWidgets.QPushButton(self.aligns_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_centerAlign.sizePolicy().hasHeightForWidth())
        self.btn_centerAlign.setSizePolicy(sizePolicy)
        self.btn_centerAlign.setMinimumSize(QtCore.QSize(24, 24))
        self.btn_centerAlign.setMaximumSize(QtCore.QSize(27, 27))
        self.btn_centerAlign.setText("")
        self.btn_centerAlign.setObjectName("btn_centerAlign")
        self.verticalLayout_9.addWidget(self.btn_centerAlign)
        self.btn_rightAlign = QtWidgets.QPushButton(self.aligns_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_rightAlign.sizePolicy().hasHeightForWidth())
        self.btn_rightAlign.setSizePolicy(sizePolicy)
        self.btn_rightAlign.setMinimumSize(QtCore.QSize(24, 24))
        self.btn_rightAlign.setMaximumSize(QtCore.QSize(27, 27))
        self.btn_rightAlign.setText("")
        self.btn_rightAlign.setObjectName("btn_rightAlign")
        self.verticalLayout_9.addWidget(self.btn_rightAlign)
        self.horizontalLayout.addWidget(self.aligns_frame)



        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.panel_text_frame)

        self.textEdit = TextEdit()  #QtWidgets.QTextEdit(self.main_frame_text) #использование камтомного текстЭдит

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.horizontalLayout_5.addWidget(self.main_frame_text)
        self.btn_openclose_HTML = QtWidgets.QPushButton(self.mainwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_openclose_HTML.sizePolicy().hasHeightForWidth())
        self.btn_openclose_HTML.setSizePolicy(sizePolicy)
        self.btn_openclose_HTML.setMinimumSize(QtCore.QSize(0, 400))
        self.btn_openclose_HTML.setObjectName("btn_openclose_HTML")
        self.horizontalLayout_5.addWidget(self.btn_openclose_HTML)
        self.main_frame_HTML = QtWidgets.QFrame(self.mainwidget)
        self.main_frame_HTML.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame_HTML.setFrameShadow(QtWidgets.QFrame.Raised)


        ######################_____Заполнение_ComboBox______###################
        self.sizeBox.addItems(["8","9","10","11","12","14","16","18","20","22","24","26","28","36","48","72"])
        self.sizeBox.setEditable(True)
        self.validator = QRegExpValidator(QRegExp("[0-2]|[1-9]"))     #Ограничение ввода в КомбоБокс "1[0-2]|[1-9]"
        self.sizeBox.setValidator(self.validator)

        ########################## ______WEB_Viwer______ ###########################
        self.main_frame_HTML.setObjectName("main_frame_HTML")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame_HTML)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.panel_HTML_frame = QtWidgets.QFrame(self.main_frame_HTML)
        self.panel_HTML_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.panel_HTML_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.panel_HTML_frame.setObjectName("panel_HTML_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.panel_HTML_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_backward_HTML = QtWidgets.QPushButton(self.panel_HTML_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_backward_HTML.sizePolicy().hasHeightForWidth())
        self.btn_backward_HTML.setSizePolicy(sizePolicy)
        self.btn_backward_HTML.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_backward_HTML.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_backward_HTML.setObjectName("btn_backward_HTML")
        self.horizontalLayout_4.addWidget(self.btn_backward_HTML)
        self.btn_forward_HTML = QtWidgets.QPushButton(self.panel_HTML_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_forward_HTML.sizePolicy().hasHeightForWidth())
        self.btn_forward_HTML.setSizePolicy(sizePolicy)
        self.btn_forward_HTML.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_forward_HTML.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_forward_HTML.setObjectName("btn_forward_HTML")
        self.horizontalLayout_4.addWidget(self.btn_forward_HTML)
        self.line_3 = QtWidgets.QFrame(self.panel_HTML_frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        self.comboBox_scale_web = QtWidgets.QComboBox(self.panel_HTML_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_scale_web.sizePolicy().hasHeightForWidth())
        self.comboBox_scale_web.setSizePolicy(sizePolicy)
        self.comboBox_scale_web.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_scale_web.setObjectName("comboBox_scale_web")
        self.horizontalLayout_4.addWidget(self.comboBox_scale_web)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.panel_HTML_frame)

        self.HTML_Viewer = QWebEngineView(self.main_frame_HTML)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HTML_Viewer.sizePolicy().hasHeightForWidth())
        self.HTML_Viewer.setSizePolicy(sizePolicy)
        self.HTML_Viewer.setMinimumSize(QtCore.QSize(400, 0))

        self.HTML_Viewer.setObjectName("HTML_Viewer")
        self.verticalLayout.addWidget(self.HTML_Viewer)

        self.horizontalLayout_5.addWidget(self.main_frame_HTML)


        ###############################__Перед_отображением__######################
        self.main_frame_HTML.setHidden(True)
        self.comboBox_scale_web.setEditable(False)
        self.loadPage("index.html")
        self.fontComboBox.setCurrentFont(QtGui.QFont(font))
        self.textEdit.setReadOnly(True)

        self.btn_Bold.setCheckable(True)
        self.btn_italic.setCheckable(True)
        self.btn_underline.setCheckable(True)

        self.textEdit.setAutoFormatting(QTextEdit.AutoAll)
        
        self.comboBox_scale_web.addItems(['200%','190%','180%','170%','160%','150%','140%','130%','120%','110%','100%','80%','60%','40%','30%'])
        self.comboBox_scale_web.setCurrentIndex(10)
        self.comboBox_scale_web.setToolTip("Масштаб")

        self.getSettings()
        self.apply_theme()
        self.addThread(False)


        #Список объектов для которых нужно отключать сигналы
        self._format_actions = [
                self.fontComboBox,
                self.sizeBox,
                self.btn_Bold,
                self.btn_italic,
                self.btn_underline,
            ]

        

        #####################__Коннекты__###################
        self.btn_openclose_HTML.clicked.connect(self.openClose_HTML)
        self.btn_paste.clicked.connect(self.btn_paste_clicked)
        self.btn_cut.clicked.connect(self.btn_cut_clicked)
        self.btn_copy.clicked.connect(self.btn_copy_clicked)
        self.btn_sizeUP.clicked.connect(self.btn_sizeUP_clicked)
        self.btn_sizeDOWN.clicked.connect(self.btn_sizeDOWN_clicked)
        self.btn_font_color.clicked.connect(self.btn_font_color_clicked)
        self.btn_new.clicked.connect(self.btn_new_clicked)
        self.btn_open.clicked.connect(self.btn_open_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.btn_backward_HTML.clicked.connect(self.btn_backward_HTML_clicked)
        self.btn_forward_HTML.clicked.connect(self.btn_forward_HTML_clicked)
        self.btn_print.clicked.connect(self.file_print)

        self.btn_leftAlign.clicked.connect(lambda: self.textEdit.setAlignment(Qt.AlignLeft))
        self.btn_centerAlign.clicked.connect(lambda: self.textEdit.setAlignment(Qt.AlignCenter))
        self.btn_rightAlign.clicked.connect(lambda: self.textEdit.setAlignment(Qt.AlignRight))

        self.btn_settings.clicked.connect(self.open_settings)

        self.btn_Bold.toggled.connect(lambda x: self.textEdit.setFontWeight(QFont.Bold if x else QFont.Normal))
        self.btn_italic.toggled.connect(self.textEdit.setFontItalic)
        self.btn_underline.toggled.connect(self.textEdit.setFontUnderline)

        self.sizeBox.currentTextChanged.connect(self.sizeBox_textChange)
        self.fontComboBox.currentFontChanged.connect(self.textEdit.setCurrentFont)
        self.textEdit.selectionChanged.connect(self.textEdit_selectionChanged)

        self.btn_make_link.clicked.connect(self.makeLink)

        self.comboBox_scale_web.activated.connect(self.zoomCB)

        ##############
        HTML_Editor.setCentralWidget(self.mainwidget)

        self.retranslateUi(HTML_Editor)
        QtCore.QMetaObject.connectSlotsByName(HTML_Editor)
    
    def loadPage(self, HTML):                   #функция отображения страницы
        self.mainpage = self.HTML_Viewer.page()  
        self.mainpage.load(QUrl.fromLocalFile(os.path.abspath(f"{HTML}")))
        self.HTML_Viewer.show()

    def addThread(self, close):
        global auto
        if (os.path.exists("auto_saves") == False):
            os.mkdir("auto_saves")
        
        exit_flag = False
        if (auto == "true"):
            exit_flag = False
        elif(auto == "false"):
            exit_flag = True
        print(exit_flag)
        t1 = Thread(target = self.autoSave, args = (lambda : exit_flag, ))
        t1.start()

    def autoSave(self, exit_flag):
        print("ON")
        global timer
        global filePath
        global firstSave
        global name
        if (firstSave == "False"):
            print("ON_OFF")
            i = 0
            while (i <= int(timer) * 60):
                time.sleep(1)
                print("wait")
                if (i == int(timer) * 60):
                    i = 0
                    stringDate = time.datetime.now().strftime("D_%mm_%dd_%Y_T_%HH_%MM")
                    if (name != ""):
                        mf = open(f"auto_saves/{name}_{stringDate}.html", 'w+')
                        mf.write(self.textEdit.toHtml())
                        mf.close()
                        notification_func("Автосохранение", f"Сохранено в 'auto_saves/{name}_{stringDate}.html'")
                    else:
                        mf = open(f"auto_saves/{stringDate}.html", 'w+')
                        mf.write(self.textEdit.toHtml())
                        mf.close()
                        notification_func("Автосохранение", f"Сохранено в 'auto_saves/{stringDate}.html'")
                else:
                    print(i)
                    i+=1
                if (exit_flag == True):
                    print("OFF")
                    break


    
    def textEdit_selectionChanged(self):            #получение координат выделния
        global selectionStart
        global selectionEnd
        cursor = self.textEdit.textCursor()
        selectionStart = cursor.selectionStart()
        selectionEnd = cursor.selectionEnd()
        self.update_format()
    
    def makeLink(self):
        global firstSave
        if(firstSave != "FirstOpen"):
            text, ok = QInputDialog.getText(HTML_Editor, "Создать ссылку", "Введите ссылку")
            if ok:
                global selectionStart
                global selectionEnd
                global linksList
                print(text)
                cursor = self.textEdit.textCursor()
                cursor.setPosition(selectionStart)
                cursor.setPosition(selectionEnd, QtGui.QTextCursor.KeepAnchor)
                textSelected = cursor.selectedText()
                cursor.removeSelectedText()
                linkHtml = f'<a href="{text}">{textSelected}</a>'
                cursor.insertHtml(linkHtml)
                link = HyperLinks()
                link.link = text
                link.startPos = selectionStart
                link.endPos = selectionEnd
                linksList.append(link)

    def open_settings(self):

        settings_diolog = QtWidgets.QDialog()
        settings = Ui_Settings_Dialog()
        settings.setupUi(settings_diolog)
        settings_diolog.exec_()
        
        self.getSettings()
        self.apply_theme()
        self.addThread(False)

    def closeEvent(self, event):
        print("Close")
        self.addThread(True)


    def getSettings(self):                  #получение настроек
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

    def apply_theme(self):                              #применение тем
        global theme
        if (theme == "light"):
            ########################____Set_Style_____######################

            self.mainwidget.setStyleSheet(
                """
                background-color: #F5F5F5;
                """
            )

            self.panel_text_frame.setStyleSheet(
                """
                QFrame
                {
                    background-color: #E0E0E1;
                }
                """
            )

            self.btn_new.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_open.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_save.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_print.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_settings.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_paste.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_cut.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_copy.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_font_color.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_Bold.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_underline.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_italic.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_make_link.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

        # self.btn_window_link.setStyleSheet(
        #     """
        #     QPushButton
        #     {
        #     border-style: none;
        #     background-color: #D9D9D9;
        #     }
        #     QPushButton:pressed
        #     {
        #         background-color: #C4C4C4;
        #     }
        #     """
        # )

            self.btn_sizeDOWN.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_sizeUP.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_leftAlign.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_centerAlign.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.btn_rightAlign.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            
            self.textEdit.setStyleSheet(
                """
                QTextEdit
                {
                    border: 1px solid lightgray;
                }
                """
            )

            self.fontComboBox.setStyleSheet(
                "color: black;"
            )

            self.sizeBox.setStyleSheet(
                "color: black;"
            )

            ###########################_____Добавление_иконок_для_кнопок_____#################################
            self.btn_new.setIcon(QIcon("media/ico_btn_new.png"))
            self.btn_new.setIconSize(QSize(60,60))
            self.btn_new.setToolTip("Создание файла")
            
            self.btn_open.setIcon(QIcon("media/ico_btn_open.png"))
            self.btn_open.setIconSize(QSize(60,60))
            self.btn_open.setToolTip("Открытие файла")

            self.btn_save.setIcon(QIcon("media/ico_btn_save.png"))
            self.btn_save.setIconSize(QSize(60,60))
            self.btn_save.setToolTip("Сохранение файла")
            
            self.btn_print.setIcon(QIcon("media/ico_btn_print.png"))
            self.btn_print.setIconSize(QSize(60,60))
            self.btn_print.setToolTip("Печать")

            self.btn_settings.setIcon(QIcon("media/ico_btn_settings.png"))
            self.btn_settings.setIconSize(QSize(60,60))
            self.btn_settings.setToolTip("Настройки")

            self.btn_paste.setIcon(QIcon("media/ico_btn_paste.png"))
            self.btn_paste.setIconSize(QSize(20,20))
            self.btn_paste.setToolTip("Вставить")

            self.btn_cut.setIcon(QIcon("media/ico_btn_cut.png"))
            self.btn_cut.setIconSize(QSize(20,20))
            self.btn_cut.setToolTip("Вырезать")

            self.btn_copy.setIcon(QIcon("media/ico_btn_copy.png"))
            self.btn_copy.setIconSize(QSize(20,20))
            self.btn_copy.setToolTip("Копировать")

            self.btn_Bold.setIcon(QIcon("media/ico_btn_bold.png"))
            self.btn_Bold.setIconSize(QSize(20,20))
            self.btn_Bold.setToolTip("Полужирный")

            self.btn_underline.setIcon(QIcon("media/ico_btn_underline.png"))
            self.btn_underline.setIconSize(QSize(20,20))
            self.btn_underline.setToolTip("Подчёркивание")

            self.btn_italic.setIcon(QIcon("media/ico_btn_italic.png"))
            self.btn_italic.setIconSize(QSize(20,20))
            self.btn_italic.setToolTip("Курсив")

            self.btn_make_link.setIcon(QIcon("media/ico_btn_make_link.png"))
            self.btn_make_link.setIconSize(QSize(20,20))
            self.btn_make_link.setToolTip("Создать ссылку")

            #self.btn_window_link.setIcon(QIcon("media/ico_btn_window_link.png"))
            #self.btn_window_link.setIconSize(QSize(20,20))
            #self.btn_window_link.setToolTip("Окно ссылок")

            self.btn_font_color.setIcon(QIcon("media/ico_btn_colorFont.png"))
            self.btn_font_color.setIconSize(QSize(20,20))
            self.btn_font_color.setToolTip("Выбор цвета")

            self.btn_sizeUP.setIcon(QIcon("media/ico_btn_upscaleFont.png"))
            self.btn_sizeUP.setIconSize(QSize(20,20))
            self.btn_sizeUP.setToolTip("Увеличение шрифта")

            self.btn_sizeDOWN.setIcon(QIcon("media/ico_btn_downscaleFont.png"))
            self.btn_sizeDOWN.setIconSize(QSize(20,20))
            self.btn_sizeDOWN.setToolTip("Уменьшение шрифта")


            self.btn_leftAlign.setIcon(QIcon("media/ico_btn_align_left.png"))
            self.btn_leftAlign.setIconSize(QSize(20,20))
            self.btn_leftAlign.setToolTip("Выравнивание по левому краю")

            self.btn_centerAlign.setIcon(QIcon("media/ico_btn_align_center.png"))
            self.btn_centerAlign.setIconSize(QSize(20,20))
            self.btn_centerAlign.setToolTip("Выравнивание по центру")

            self.btn_rightAlign.setIcon(QIcon("media/ico_btn_align_right.png"))
            self.btn_rightAlign.setIconSize(QSize(20,20))
            self.btn_rightAlign.setToolTip("Выравнивание по правому краю")


            #######################__Стили_Браузера__##########################
            self.panel_HTML_frame.setStyleSheet(
                """
                QFrame
                {
                    background-color: #E0E0E1;
                }
                """
            )

            self.btn_openclose_HTML.setStyleSheet(
                """
                QPushButton
                {
                    border: 1px solid lightgray;
                    background-color: #E0E0E1;
                }
                QPushButton:pressed
                {
                    background-color: #D9D9D9;
                }
                """
            )
            self.btn_forward_HTML.setStyleSheet(
                """
                QPushButton
                {
                    border: 0px solid lightgray;
                    background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )
            self.btn_backward_HTML.setStyleSheet(
                """
                QPushButton
                {
                    border: 0px solid lightgray;
                    background-color: #D9D9D9;
                }
                QPushButton:pressed
                {
                    background-color: #C4C4C4;
                }
                """
            )

            self.comboBox_scale_web.setStyleSheet(
                """
                    color: black;
                """
            )
            
            #########################______Иконки_кнопок_Браузера_____###############
            self.btn_openclose_HTML.setIcon(QIcon("media/ico_arrowLeft.png"))
            self.btn_openclose_HTML.setIconSize(QSize(25,25))
            self.btn_openclose_HTML.setToolTip("Открытие предпросмотра")

            self.btn_backward_HTML.setIcon(QIcon("media/ico_btn_back.png"))
            self.btn_backward_HTML.setIconSize(QSize(20,20))
            self.btn_backward_HTML.setToolTip("Назад")

            self.btn_forward_HTML.setIcon(QIcon("media/ico_btn_forward.png"))
            self.btn_forward_HTML.setIconSize(QSize(20,20))
            self.btn_forward_HTML.setToolTip("Вперёд")

            
        
        elif (theme == "dark"):
            ########################____Set_Style_____######################

            self.mainwidget.setStyleSheet(
                """
                background-color: #1b1b1b;
                """
            )

            self.panel_text_frame.setStyleSheet(
                """
                QFrame
                {
                    background-color: #323232;
                }
                """
            )

            self.btn_new.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_open.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_save.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_print.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_settings.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_paste.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_cut.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_copy.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_font_color.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_Bold.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_underline.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_italic.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_make_link.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

        # self.btn_window_link.setStyleSheet(
        #     """
        #     QPushButton
        #     {
        #     border-style: none;
        #     background-color: #D9D9D9;
        #     }
        #     QPushButton:pressed
        #     {
        #         background-color: #C4C4C4;
        #     }
        #     """
        # )

            self.btn_sizeDOWN.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_sizeUP.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_leftAlign.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_centerAlign.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            self.btn_rightAlign.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )

            
            self.textEdit.setStyleSheet(
                """
                QTextEdit
                {
                    border: 0px solid lightgray;
                }
                """
            )

            self.fontComboBox.setStyleSheet(
                "color: White;"
            )

            self.sizeBox.setStyleSheet(
                "color: White;"
            )

            ###########################_____Добавление_иконок_для_кнопок_____#################################
            self.btn_new.setIcon(QIcon("media/dark_mode/ico_btn_new_dark.png"))
            self.btn_new.setIconSize(QSize(60,60))
            self.btn_new.setToolTip("Создание файла")
            
            self.btn_open.setIcon(QIcon("media/dark_mode/ico_btn_open_dark.png"))
            self.btn_open.setIconSize(QSize(60,60))
            self.btn_open.setToolTip("Открытие файла")

            self.btn_save.setIcon(QIcon("media/dark_mode/ico_btn_save_dark.png"))
            self.btn_save.setIconSize(QSize(60,60))
            self.btn_save.setToolTip("Сохранение файла")
            
            self.btn_print.setIcon(QIcon("media/dark_mode/ico_btn_print_dark.png"))
            self.btn_print.setIconSize(QSize(60,60))
            self.btn_print.setToolTip("Печать")

            self.btn_settings.setIcon(QIcon("media/dark_mode/ico_btn_settings_dark.png"))
            self.btn_settings.setIconSize(QSize(60,60))
            self.btn_settings.setToolTip("Настройки")

            self.btn_paste.setIcon(QIcon("media/dark_mode/ico_btn_paste_dark.png"))
            self.btn_paste.setIconSize(QSize(20,20))
            self.btn_paste.setToolTip("Вставить")

            self.btn_cut.setIcon(QIcon("media/dark_mode/ico_btn_cut_dark.png"))
            self.btn_cut.setIconSize(QSize(20,20))
            self.btn_cut.setToolTip("Вырезать")

            self.btn_copy.setIcon(QIcon("media/dark_mode/ico_btn_copy_dark.png"))
            self.btn_copy.setIconSize(QSize(20,20))
            self.btn_copy.setToolTip("Копировать")

            self.btn_Bold.setIcon(QIcon("media/dark_mode/ico_btn_bold_dark.png"))
            self.btn_Bold.setIconSize(QSize(20,20))
            self.btn_Bold.setToolTip("Полужирный")

            self.btn_underline.setIcon(QIcon("media/dark_mode/ico_btn_underline_dark.png"))
            self.btn_underline.setIconSize(QSize(20,20))
            self.btn_underline.setToolTip("Подчёркивание")

            self.btn_italic.setIcon(QIcon("media/dark_mode/ico_btn_italic_dark.png"))
            self.btn_italic.setIconSize(QSize(20,20))
            self.btn_italic.setToolTip("Курсив")

            self.btn_make_link.setIcon(QIcon("media/dark_mode/ico_btn_make_link_dark.png"))
            self.btn_make_link.setIconSize(QSize(20,20))
            self.btn_make_link.setToolTip("Создать ссылку")

            #self.btn_window_link.setIcon(QIcon("media/ico_btn_window_link.png"))
            #self.btn_window_link.setIconSize(QSize(20,20))
            #self.btn_window_link.setToolTip("Окно ссылок")

            self.btn_font_color.setIcon(QIcon("media/dark_mode/ico_btn_colorFont_dark.png"))
            self.btn_font_color.setIconSize(QSize(20,20))
            self.btn_font_color.setToolTip("Выбор цвета")

            self.btn_sizeUP.setIcon(QIcon("media/dark_mode/ico_btn_upscaleFont_dark.png"))
            self.btn_sizeUP.setIconSize(QSize(20,20))
            self.btn_sizeUP.setToolTip("Увеличение шрифта")

            self.btn_sizeDOWN.setIcon(QIcon("media/dark_mode/ico_btn_downscaleFont_dark.png"))
            self.btn_sizeDOWN.setIconSize(QSize(20,20))
            self.btn_sizeDOWN.setToolTip("Уменьшение шрифта")


            self.btn_leftAlign.setIcon(QIcon("media/dark_mode/ico_btn_align_left_dark.png"))
            self.btn_leftAlign.setIconSize(QSize(20,20))
            self.btn_leftAlign.setToolTip("Выравнивание по левому краю")

            self.btn_centerAlign.setIcon(QIcon("media/dark_mode/ico_btn_align_center_dark.png"))
            self.btn_centerAlign.setIconSize(QSize(20,20))
            self.btn_centerAlign.setToolTip("Выравнивание по центру")

            self.btn_rightAlign.setIcon(QIcon("media/dark_mode/ico_btn_align_right_dark.png"))
            self.btn_rightAlign.setIconSize(QSize(20,20))
            self.btn_rightAlign.setToolTip("Выравнивание по правому краю")


            #######################__Стили_Браузера__##########################
            self.panel_HTML_frame.setStyleSheet(
                """
                QFrame
                {
                    background-color: #323232;
                }
                """
            )

            self.btn_openclose_HTML.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )
            self.btn_forward_HTML.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )
            self.btn_backward_HTML.setStyleSheet(
                """
                QPushButton
                {
                border-style: none;
                background-color: #2c2c2c;
                }
                QPushButton:pressed
                {
                    background-color: #3f3f3f;
                }
                """
            )
            
            #########################______Иконки_кнопок_Браузера_____###############
            self.btn_openclose_HTML.setIcon(QIcon("media/dark_mode/ico_arrowLeft_dark.png"))
            self.btn_openclose_HTML.setIconSize(QSize(25,25))
            self.btn_openclose_HTML.setToolTip("Открытие предпросмотра")

            self.btn_backward_HTML.setIcon(QIcon("media/dark_mode/ico_btn_back_dark.png"))
            self.btn_backward_HTML.setIconSize(QSize(20,20))
            self.btn_backward_HTML.setToolTip("Назад")

            self.btn_forward_HTML.setIcon(QIcon("media/dark_mode/ico_btn_forward_dark.png"))
            self.btn_forward_HTML.setIconSize(QSize(20,20))
            self.btn_forward_HTML.setToolTip("Вперёд")

            self.comboBox_scale_web.setStyleSheet(
                """
                    color: White;
                """
            )

    
    #Изменение маштаба браузера
    def zoomCB(self):
            cbSizeData = self.comboBox_scale_web.currentText()
            zoomScale = int(self.comboBox_scale_web.findText(cbSizeData))

            if zoomScale == 14:
                self.mainpage.setZoomFactor(0.3)

            if zoomScale == 13:
                self.mainpage.setZoomFactor(0.4)

            if zoomScale == 12:
                self.mainpage.setZoomFactor(0.6)
            
            if zoomScale == 11:
                self.mainpage.setZoomFactor(0.8)

            if zoomScale == 10:
                self.mainpage.setZoomFactor(1.0)

            elif zoomScale == 9:
                self.mainpage.setZoomFactor(1.4)
            
            elif zoomScale == 8:
                self.mainpage.setZoomFactor(1.8)

            elif zoomScale == 7:
                self.mainpage.setZoomFactor(2.2)

            elif zoomScale == 6:
                self.mainpage.setZoomFactor(2.6)

            elif zoomScale == 5:
                self.mainpage.setZoomFactor(3.0)

            elif zoomScale == 4:
                self.mainpage.setZoomFactor(3.4)

            elif zoomScale == 3:
                self.mainpage.setZoomFactor(3.8)
            
            elif zoomScale == 2:
                self.mainpage.setZoomFactor(4.2)


            elif zoomScale == 1:
                self.mainpage.setZoomFactor(4.6)

            elif zoomScale == 0:
                self.mainpage.setZoomFactor(5)

    def sizeBox_textChange(self):                   #ограничение на три символа
        global font
        global selectionStart
        global selectionEnd
        string = self.sizeBox.currentText()
        len_Str = len(string)
        if (len_Str <= 3):
            #cursor = self.textEdit.textCursor()
            #cursor.setPosition(selectionStart)
            #cursor.select(QtGui.QTextCursor.BlockUnderCursor)
            #cursor.removeSelectedText()
            self.textEdit.setFontPointSize(float(string))
            #cursor.setPosition(selectionEnd)
            #cursor.select(QtGui.QTextCursor.BlockUnderCursor)
            #cursor.removeSelectedText()
            #self.textEdit.textCursor().insertHtml(f"</font>")
            #self.textEdit.setFont(QtGui.QFont(font, int(string)))
        
        else:
            remove = string[:len_Str-1]
            self.sizeBox.setCurrentText(remove)
            #cursor = self.textEdit.textCursor()
            #cursor.setPosition(selectionStart)
            #self.textEdit.textCursor().insertHtml(f"<font face = '{font}' size = '{string}'>")
            #cursor.setPosition(selectionEnd)
            #self.textEdit.textCursor().insertHtml(f"</font>")
            self.textEdit.setFontPointSize(float(string))
            #self.textEdit.setFont(QtGui.QFont(font, int(string)))

    def btn_backward_HTML_clicked(self):
        self.HTML_Viewer.back()

    def btn_forward_HTML_clicked(self):
        self.HTML_Viewer.forward()
    
    def file_print(self):
        global firstSave
        if (firstSave != "FirstOpen"):
            dlg = QPrintDialog()
            if dlg.exec_():
                self.textEdit.print_(dlg.printer())

    def btn_new_clicked(self):              #создание файла
        text, ok = QInputDialog.getText(HTML_Editor, "Создать", "Введите имя файла")
        if ok:
            path = QFileDialog.getExistingDirectory(HTML_Editor, "Создать")
            if (path != ""):
                global filePath
                global firstSave
                global name
                name = text
                filePath = f"{path}/{text}.html"
                mf = open(filePath, 'w')
                #mf.write("<HTML><HEAD></HEAD><BODY></BODY></HTML>")
                mf.close()
                self.textEdit.setReadOnly(False)
                self.loadPage(filePath)
                firstSave = "False"
                self.sizeBox.setCurrentText("14")
    
    def btn_open_clicked(self):     #открытие
        path = QFileDialog.getOpenFileName(HTML_Editor, "Открыть", "", "MS Word DOCX(*.docx);;MS Word DOC(*.doc);;HTML (*.html);;Текст(*txt)")
        global oldPath
        global filePath
        global firstSave
        global outFilePathHTML
        global outFilePathHTMLDoc

        filePath = str(path[0])
        fileType = str(path[1])
        if (oldPath != filePath):
            firstSave = "True"
            oldPath = filePath

        outFilePathHTML = filePath[:len(filePath)-4] + "html"
        outFilePathHTMLDoc = filePath[:len(filePath)-3] + "html"
        if (filePath != ''):
            if (firstSave == "FirstOpen"):
                firstSave = "True"
            if (fileType == "MS Word DOCX(*.docx)"):
                word = client.Dispatch('Word.Application')
                wb = word.Documents.Open(filePath)
                wb.SaveAs2(outFilePathHTML, FileFormat=8)
                wb.Close()
                mf = open(outFilePathHTML, 'r+')
                self.textEdit.setText(mf.read())
                mf.close()
                self.textEdit.setReadOnly(False)
                self.loadPage(outFilePathHTML)

            elif (fileType == "MS Word DOC(*.doc)"):
                word = client.Dispatch('Word.Application')
                wb = word.Documents.Open(filePath)
                wb.SaveAs2(outFilePathHTMLDoc, FileFormat=8)
                wb.Close()
                mf = open(outFilePathHTMLDoc, 'r+')
                self.textEdit.setText(mf.read())
                mf.close()
                self.textEdit.setReadOnly(False)
                self.loadPage(outFilePathHTMLDoc)

            elif (fileType == "HTML (*.html)"):
                mf = open(filePath, 'r+')
                self.textEdit.setText(mf.read())
                mf.close()
                self.textEdit.setReadOnly(False)
                self.loadPage(filePath)

            elif (fileType == "Текст(*txt)"):
                mf = open(filePath, 'r+')
                self.textEdit.setText(mf.read())
                mf.close()
                self.textEdit.setReadOnly(False)
                self.loadPage(filePath)
    
    def btn_save_clicked(self):         #сохранение
        global firstSave
        global filePath
        if (firstSave == "True"):
            path = QFileDialog.getSaveFileName(HTML_Editor, "Сохранить", "","HTML (*.html);;Текст(*txt)")
            filePath = str(path[0])
            if (filePath != ''):
                mf = open(filePath, 'w+')
                mf.write(self.textEdit.toHtml())
                mf.close()
                self.textEdit.setReadOnly(False)
                self.loadPage(filePath)
                firstSave = "False"
        elif (firstSave == "False"):
            mf = open(filePath, 'w+')
            mf.write(self.textEdit.toHtml())
            mf.close()
            self.textEdit.setReadOnly(False)
            self.loadPage(filePath)                                                                                         

    def btn_font_color_clicked(self):           #функция изменения цвета
        color = QtWidgets.QColorDialog.getColor()
        self.textEdit.setTextColor(color)
        currentColor = color.name()
        convert = str(ImageColor.getcolor(currentColor, "HSV"))   #Конвертер HSV
        convertString = convert.replace('(', '').replace(')', '')
        convertItem = convertString.split(",")

        self.btn_font_color.setStyleSheet(f"background-color: {currentColor};")
        if (int(convertItem[2]) <= 130):
            self.btn_font_color.setIcon(QIcon("media/ico_btn_colorFont_Light.png"))
        elif (int(convertItem[2]) > 130):
            self.btn_font_color.setIcon(QIcon("media/ico_btn_colorFont.png"))

    #увеличение шрифта
    def btn_sizeUP_clicked(self):
        string = self.sizeBox.currentText()
        self.sizeBox.setCurrentText(str(int(string) + 2))
    
    #уменьшение шрифта
    def btn_sizeDOWN_clicked(self):
        string = self.sizeBox.currentText()
        if (int(string) > 2):
            self.sizeBox.setCurrentText(str(int(string) - 2))
        else:
            self.sizeBox.setCurrentText("1")

    #копировать
    def btn_copy_clicked(self):
        self.textEdit.copy()
        self.notification_func(" ", "Скопировано")
    
    #вставить
    def btn_paste_clicked(self):
        self.textEdit.paste()
        self.notification_func(" ", "Вставлено")
    
    #вырезать
    def btn_cut_clicked(self):
        self.textEdit.cut()
        self.notification_func(" ", "Вырезано")

    #открытие внутренего "браузера"
    def openClose_HTML(self):
            global openBrowserValue
            global theme
            if (openBrowserValue == False):
                if (theme == "light"):
                    self.btn_openclose_HTML.setIcon(QIcon("media/ico_arrowRight.png"))
                    self.main_frame_HTML.setHidden(False)
                    openBrowserValue = True
                elif (theme == "dark"):
                    self.btn_openclose_HTML.setIcon(QIcon("media/dark_mode/ico_arrowRight_dark.png"))
                    self.main_frame_HTML.setHidden(False)
                    openBrowserValue = True
            elif (openBrowserValue == True):
                if (theme == "light"):
                    self.btn_openclose_HTML.setIcon(QIcon("media/ico_arrowLeft.png"))
                    self.main_frame_HTML.setHidden(True)
                    openBrowserValue = False
                elif (theme == "dark"):
                    self.btn_openclose_HTML.setIcon(QIcon("media/dark_mode/ico_arrowLeft_dark.png"))
                    self.main_frame_HTML.setHidden(True)
                    openBrowserValue = False
    

    #блокировка событий/сигналов
    def block_signals(self, objects, b):
        for o in objects:
            o.blockSignals(b)

    #Обновление данных шрифта
    def update_format(self):
        #Блокировка сигналов
        self.block_signals(self._format_actions, True)

        self.fontComboBox.setCurrentFont(self.textEdit.currentFont())
        # изменяем значение размера шрифта в КБ
        self.sizeBox.setCurrentText(str(int(self.textEdit.fontPointSize())))

        self.btn_italic.setChecked(self.textEdit.fontItalic())
        self.btn_underline.setChecked(self.textEdit.fontUnderline())
        self.btn_Bold.setChecked(self.textEdit.fontWeight() == QFont.Bold)

        #не сделано выравнивание
        #self.alignl_action.setChecked(self.editor.alignment() == Qt.AlignLeft)
        #self.alignc_action.setChecked(self.editor.alignment() == Qt.AlignCenter)
        #self.alignr_action.setChecked(self.editor.alignment() == Qt.AlignRight)
        #self.alignj_action.setChecked(self.editor.alignment() == Qt.AlignJustify)

        self.block_signals(self._format_actions, False)
    
    ##################___Функция_уведомлений___####################
    def notification_func(self, Header, notify_text):
        global PC_system
        if (PC_system == 'Windows'):
            notification.notify(
            title= Header,
            message= notify_text,
            app_icon='media/notify_ico.ico')

        elif (PC_system == 'Linux'):
            command = f"notify-send '{Header}' '{notify_text}'"
            os.system(command)

        elif (PC_system == "Darwin"):
            command = f"osascript -e 'display notification '{notify_text}' with title '{Header}'"
            os.system(command)

        else:
            pass            


    def retranslateUi(self, HTML_Editor):
        _translate = QtCore.QCoreApplication.translate
        HTML_Editor.setWindowTitle(_translate("HTML_Editor", "Html редактор"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HTML_Editor = QtWidgets.QMainWindow()
    #HTML_Editor.statusBar().showMessage('Готов')
    ui = Ui_HTML_Editor()
    ui.setupUi(HTML_Editor)
    HTML_Editor.show()
    sys.exit(app.exec_())
