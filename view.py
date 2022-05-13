# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 336)
        MainWindow.setMinimumSize(QtCore.QSize(601, 336))
        MainWindow.setMaximumSize(QtCore.QSize(601, 336))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_channel = QtWidgets.QFrame(self.centralwidget)
        self.frame_channel.setGeometry(QtCore.QRect(10, 160, 421, 61))
        self.frame_channel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_channel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_channel.setObjectName("frame_channel")
        self.display_current_channel = QtWidgets.QLCDNumber(self.frame_channel)
        self.display_current_channel.setGeometry(QtCore.QRect(70, 20, 64, 23))
        self.display_current_channel.setProperty("value", 0.0)
        self.display_current_channel.setProperty("intValue", 0)
        self.display_current_channel.setObjectName("display_current_channel")
        self.label_channel = QtWidgets.QLabel(self.frame_channel)
        self.label_channel.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label_channel.setObjectName("label_channel")
        self.button_c_up = QtWidgets.QPushButton(self.frame_channel)
        self.button_c_up.setGeometry(QtCore.QRect(180, 10, 101, 41))
        self.button_c_up.setObjectName("button_c_up")
        self.button_c_down = QtWidgets.QPushButton(self.frame_channel)
        self.button_c_down.setGeometry(QtCore.QRect(300, 10, 101, 41))
        self.button_c_down.setObjectName("button_c_down")
        self.frame_volume = QtWidgets.QFrame(self.centralwidget)
        self.frame_volume.setGeometry(QtCore.QRect(10, 220, 421, 61))
        self.frame_volume.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_volume.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_volume.setObjectName("frame_volume")
        self.display_current_volume = QtWidgets.QLCDNumber(self.frame_volume)
        self.display_current_volume.setGeometry(QtCore.QRect(70, 20, 64, 23))
        self.display_current_volume.setObjectName("display_current_volume")
        self.label_volume = QtWidgets.QLabel(self.frame_volume)
        self.label_volume.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label_volume.setObjectName("label_volume")
        self.button_v_up = QtWidgets.QPushButton(self.frame_volume)
        self.button_v_up.setGeometry(QtCore.QRect(180, 10, 101, 41))
        self.button_v_up.setObjectName("button_v_up")
        self.button_v_down = QtWidgets.QPushButton(self.frame_volume)
        self.button_v_down.setGeometry(QtCore.QRect(300, 10, 101, 41))
        self.button_v_down.setObjectName("button_v_down")
        self.frame_power = QtWidgets.QFrame(self.centralwidget)
        self.frame_power.setGeometry(QtCore.QRect(430, 160, 161, 121))
        self.frame_power.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_power.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_power.setObjectName("frame_power")
        self.label_power = QtWidgets.QLabel(self.frame_power)
        self.label_power.setGeometry(QtCore.QRect(50, 20, 61, 21))
        self.label_power.setObjectName("label_power")
        self.button_power = QtWidgets.QPushButton(self.frame_power)
        self.button_power.setGeometry(QtCore.QRect(30, 50, 101, 41))
        self.button_power.setObjectName("button_power")
        self.frame_values = QtWidgets.QFrame(self.centralwidget)
        self.frame_values.setGeometry(QtCore.QRect(10, 0, 581, 161))
        self.frame_values.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_values.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_values.setObjectName("frame_values")
        self.spinBox_min_c = QtWidgets.QSpinBox(self.frame_values)
        self.spinBox_min_c.setGeometry(QtCore.QRect(180, 50, 42, 22))
        self.spinBox_min_c.setObjectName("spinBox_min_c")
        self.spinBox_min_v = QtWidgets.QSpinBox(self.frame_values)
        self.spinBox_min_v.setGeometry(QtCore.QRect(180, 100, 42, 22))
        self.spinBox_min_v.setObjectName("spinBox_min_v")
        self.spinBox_max_c = QtWidgets.QSpinBox(self.frame_values)
        self.spinBox_max_c.setGeometry(QtCore.QRect(360, 50, 42, 22))
        self.spinBox_max_c.setMinimum(0)
        self.spinBox_max_c.setObjectName("spinBox_max_c")
        self.spinBox_max_v = QtWidgets.QSpinBox(self.frame_values)
        self.spinBox_max_v.setGeometry(QtCore.QRect(360, 100, 42, 22))
        self.spinBox_max_v.setMinimum(0)
        self.spinBox_max_v.setObjectName("spinBox_max_v")
        self.button_values = QtWidgets.QPushButton(self.frame_values)
        self.button_values.setGeometry(QtCore.QRect(420, 40, 141, 91))
        self.button_values.setObjectName("button_values")
        self.label_min_c = QtWidgets.QLabel(self.frame_values)
        self.label_min_c.setGeometry(QtCore.QRect(60, 50, 111, 21))
        self.label_min_c.setObjectName("label_min_c")
        self.label_min_v = QtWidgets.QLabel(self.frame_values)
        self.label_min_v.setGeometry(QtCore.QRect(60, 100, 111, 21))
        self.label_min_v.setObjectName("label_min_v")
        self.label_max_c = QtWidgets.QLabel(self.frame_values)
        self.label_max_c.setGeometry(QtCore.QRect(240, 50, 111, 21))
        self.label_max_c.setObjectName("label_max_c")
        self.label_max_v = QtWidgets.QLabel(self.frame_values)
        self.label_max_v.setGeometry(QtCore.QRect(240, 100, 111, 21))
        self.label_max_v.setObjectName("label_max_v")
        self.label_intro = QtWidgets.QLabel(self.frame_values)
        self.label_intro.setGeometry(QtCore.QRect(20, 10, 521, 16))
        self.label_intro.setObjectName("label_intro")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Television"))
        self.label_channel.setText(_translate("MainWindow", "Channel:"))
        self.button_c_up.setText(_translate("MainWindow", "Up"))
        self.button_c_down.setText(_translate("MainWindow", "Down"))
        self.label_volume.setText(_translate("MainWindow", "Volume:"))
        self.button_v_up.setText(_translate("MainWindow", "Up"))
        self.button_v_down.setText(_translate("MainWindow", "Down"))
        self.label_power.setText(_translate("MainWindow", "Power is:"))
        self.button_power.setText(_translate("MainWindow", "Off"))
        self.button_values.setText(_translate("MainWindow", "Enter"))
        self.label_min_c.setText(_translate("MainWindow", "Min Ch:"))
        self.label_min_v.setText(_translate("MainWindow", "Min Vol:"))
        self.label_max_c.setText(_translate("MainWindow", "Max Ch:"))
        self.label_max_v.setText(_translate("MainWindow", "Max Vol:"))
        self.label_intro.setText(_translate("MainWindow", "Television channel and volume configurations:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())