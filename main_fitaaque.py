from collections import defaultdict
import datetime
import os
import sys
import threading
import traceback
import time

from PyQt4 import QtCore, QtGui
from PyQt4.Qt import QStatusBar, QMessageBox
from PyQt4.QtCore import QTimer, Qt

import Library
from interface_ui import *
import numpy as np
import pyqtgraph as pg

pg.setConfigOptions(useOpenGL=True)


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionConexoes.triggered.connect(lambda: self.set_index(0))
        self.ui.actionConfiguracoes.triggered.connect(lambda: self.set_index(1))
        self.ui.actionGeral.triggered.connect(lambda: self.set_index(2))
        self.ui.actionArco.triggered.connect(lambda: self.set_index(3))
        self.ui.actionGaveta_1o.triggered.connect(lambda: self.set_index(4))
        self.ui.actionGaveta_2o.triggered.connect(lambda: self.set_index(5))
        self.ui.actionGaveta_3o.triggered.connect(lambda: self.set_index(6))
        self.ui.actionGaveta_4o.triggered.connect(lambda: self.set_index(7))
        self.ui.actionGaveta_5o.triggered.connect(lambda: self.set_index(8))
        self.ui.actionGaveta_6o.triggered.connect(lambda: self.set_index(9))
        self.ui.actionGaveta_7o.triggered.connect(lambda: self.set_index(10))
        self.ui.actionGaveta_8o.triggered.connect(lambda: self.set_index(11))
        self.ui.actionGaveta_9o.triggered.connect(lambda: self.set_index(12))
        self.ui.actionGaveta_10o.triggered.connect(lambda: self.set_index(13))
        self.ui.actionGaveta_1g.triggered.connect(lambda: self.set_index(14))
        self.ui.actionGaveta_2g.triggered.connect(lambda: self.set_index(15))
        self.ui.actionGaveta_3g.triggered.connect(lambda: self.set_index(16))
        self.ui.actionGaveta_4g.triggered.connect(lambda: self.set_index(17))
        self.ui.actionGaveta_5g.triggered.connect(lambda: self.set_index(18))
        self.ui.actionGaveta_6g.triggered.connect(lambda: self.set_index(19))
        self.ui.actionGaveta_7g.triggered.connect(lambda: self.set_index(20))
        self.ui.actionGaveta_8g.triggered.connect(lambda: self.set_index(21))
        self.ui.actionGaveta_9g.triggered.connect(lambda: self.set_index(22))
        self.ui.actionGaveta_10g.triggered.connect(lambda: self.set_index(23))
        self.ui.actionGrupo_1.triggered.connect(lambda: self.set_index(24))
        self.ui.actionGrupo_2.triggered.connect(lambda: self.set_index(25))
        self.ui.actionGrupo_3.triggered.connect(lambda: self.set_index(26))
        self.ui.actionGrupo_4.triggered.connect(lambda: self.set_index(27))

        self.ui.pB_Connect.clicked.connect(self.connect)
        self.ui.pB_Disconnect.clicked.connect(self.disconnect)

        self.ui.O_on1_1.clicked.connect(lambda: self.on_individual(0, 0))
        self.ui.O_on2_1.clicked.connect(lambda: self.on_individual(1, 0))
        self.ui.O_on3_1.clicked.connect(lambda: self.on_individual(2, 0))
        self.ui.O_on4_1.clicked.connect(lambda: self.on_individual(3, 0))
        self.ui.O_on5_1.clicked.connect(lambda: self.on_individual(4, 0))
        self.ui.O_on6_1.clicked.connect(lambda: self.on_individual(5, 0))
        self.ui.O_on7_1.clicked.connect(lambda: self.on_individual(6, 0))
        self.ui.O_on8_1.clicked.connect(lambda: self.on_individual(7, 0))

        self.ui.O_on1_2.clicked.connect(lambda: self.on_individual(0, 1))
        self.ui.O_on2_2.clicked.connect(lambda: self.on_individual(1, 1))
        self.ui.O_on3_2.clicked.connect(lambda: self.on_individual(2, 1))
        self.ui.O_on4_2.clicked.connect(lambda: self.on_individual(3, 1))
        self.ui.O_on5_2.clicked.connect(lambda: self.on_individual(4, 1))
        self.ui.O_on6_2.clicked.connect(lambda: self.on_individual(5, 1))
        self.ui.O_on7_2.clicked.connect(lambda: self.on_individual(6, 1))
        self.ui.O_on8_2.clicked.connect(lambda: self.on_individual(7, 1))

        self.ui.O_on1_3.clicked.connect(lambda: self.on_individual(0, 2))
        self.ui.O_on2_3.clicked.connect(lambda: self.on_individual(1, 2))
        self.ui.O_on3_3.clicked.connect(lambda: self.on_individual(2, 2))
        self.ui.O_on4_3.clicked.connect(lambda: self.on_individual(3, 2))
        self.ui.O_on5_3.clicked.connect(lambda: self.on_individual(4, 2))
        self.ui.O_on6_3.clicked.connect(lambda: self.on_individual(5, 2))
        self.ui.O_on7_3.clicked.connect(lambda: self.on_individual(6, 2))
        self.ui.O_on8_3.clicked.connect(lambda: self.on_individual(7, 2))

        self.ui.O_on1_4.clicked.connect(lambda: self.on_individual(0, 3))
        self.ui.O_on2_4.clicked.connect(lambda: self.on_individual(1, 3))
        self.ui.O_on3_4.clicked.connect(lambda: self.on_individual(2, 3))
        self.ui.O_on4_4.clicked.connect(lambda: self.on_individual(3, 3))
        self.ui.O_on5_4.clicked.connect(lambda: self.on_individual(4, 3))
        self.ui.O_on6_4.clicked.connect(lambda: self.on_individual(5, 3))
        self.ui.O_on7_4.clicked.connect(lambda: self.on_individual(6, 3))
        self.ui.O_on8_4.clicked.connect(lambda: self.on_individual(7, 3))

        self.ui.O_on1_5.clicked.connect(lambda: self.on_individual(0, 4))
        self.ui.O_on2_5.clicked.connect(lambda: self.on_individual(1, 4))
        self.ui.O_on3_5.clicked.connect(lambda: self.on_individual(2, 4))
        self.ui.O_on4_5.clicked.connect(lambda: self.on_individual(3, 4))
        self.ui.O_on5_5.clicked.connect(lambda: self.on_individual(4, 4))
        self.ui.O_on6_5.clicked.connect(lambda: self.on_individual(5, 4))
        self.ui.O_on7_5.clicked.connect(lambda: self.on_individual(6, 4))
        self.ui.O_on8_5.clicked.connect(lambda: self.on_individual(7, 4))

        self.ui.O_on1_6.clicked.connect(lambda: self.on_individual(0, 5))
        self.ui.O_on2_6.clicked.connect(lambda: self.on_individual(1, 5))
        self.ui.O_on3_6.clicked.connect(lambda: self.on_individual(2, 5))
        self.ui.O_on4_6.clicked.connect(lambda: self.on_individual(3, 5))
        self.ui.O_on5_6.clicked.connect(lambda: self.on_individual(4, 5))
        self.ui.O_on6_6.clicked.connect(lambda: self.on_individual(5, 5))
        self.ui.O_on7_6.clicked.connect(lambda: self.on_individual(6, 5))
        self.ui.O_on8_6.clicked.connect(lambda: self.on_individual(7, 5))

        self.ui.O_on1_7.clicked.connect(lambda: self.on_individual(0, 6))
        self.ui.O_on2_7.clicked.connect(lambda: self.on_individual(1, 6))
        self.ui.O_on3_7.clicked.connect(lambda: self.on_individual(2, 6))
        self.ui.O_on4_7.clicked.connect(lambda: self.on_individual(3, 6))
        self.ui.O_on5_7.clicked.connect(lambda: self.on_individual(4, 6))
        self.ui.O_on6_7.clicked.connect(lambda: self.on_individual(5, 6))
        self.ui.O_on7_7.clicked.connect(lambda: self.on_individual(6, 6))
        self.ui.O_on8_7.clicked.connect(lambda: self.on_individual(7, 6))

        self.ui.O_on1_8.clicked.connect(lambda: self.on_individual(0, 7))
        self.ui.O_on2_8.clicked.connect(lambda: self.on_individual(1, 7))
        self.ui.O_on3_8.clicked.connect(lambda: self.on_individual(2, 7))
        self.ui.O_on4_8.clicked.connect(lambda: self.on_individual(3, 7))
        self.ui.O_on5_8.clicked.connect(lambda: self.on_individual(4, 7))
        self.ui.O_on6_8.clicked.connect(lambda: self.on_individual(5, 7))
        self.ui.O_on7_8.clicked.connect(lambda: self.on_individual(6, 7))
        self.ui.O_on8_8.clicked.connect(lambda: self.on_individual(7, 7))

        self.ui.O_on1_9.clicked.connect(lambda: self.on_individual(0, 8))
        self.ui.O_on2_9.clicked.connect(lambda: self.on_individual(1, 8))
        self.ui.O_on3_9.clicked.connect(lambda: self.on_individual(2, 8))
        self.ui.O_on4_9.clicked.connect(lambda: self.on_individual(3, 8))
        self.ui.O_on5_9.clicked.connect(lambda: self.on_individual(4, 8))
        self.ui.O_on6_9.clicked.connect(lambda: self.on_individual(5, 8))
        self.ui.O_on7_9.clicked.connect(lambda: self.on_individual(6, 8))
        self.ui.O_on8_9.clicked.connect(lambda: self.on_individual(7, 8))

        self.ui.O_on1_10.clicked.connect(lambda: self.on_individual(0, 9))
        self.ui.O_on2_10.clicked.connect(lambda: self.on_individual(1, 9))
        self.ui.O_on3_10.clicked.connect(lambda: self.on_individual(2, 9))
        self.ui.O_on4_10.clicked.connect(lambda: self.on_individual(3, 9))
        self.ui.O_on5_10.clicked.connect(lambda: self.on_individual(4, 9))
        self.ui.O_on6_10.clicked.connect(lambda: self.on_individual(5, 9))
        self.ui.O_on7_10.clicked.connect(lambda: self.on_individual(6, 9))
        self.ui.O_on8_10.clicked.connect(lambda: self.on_individual(7, 9))

        self.ui.O_off1_1.clicked.connect(lambda: self.off_individual(0, 0))
        self.ui.O_off2_1.clicked.connect(lambda: self.off_individual(1, 0))
        self.ui.O_off3_1.clicked.connect(lambda: self.off_individual(2, 0))
        self.ui.O_off4_1.clicked.connect(lambda: self.off_individual(3, 0))
        self.ui.O_off5_1.clicked.connect(lambda: self.off_individual(4, 0))
        self.ui.O_off6_1.clicked.connect(lambda: self.off_individual(5, 0))
        self.ui.O_off7_1.clicked.connect(lambda: self.off_individual(6, 0))
        self.ui.O_off8_1.clicked.connect(lambda: self.off_individual(7, 0))

        self.ui.O_off1_2.clicked.connect(lambda: self.off_individual(0, 1))
        self.ui.O_off2_2.clicked.connect(lambda: self.off_individual(1, 1))
        self.ui.O_off3_2.clicked.connect(lambda: self.off_individual(2, 1))
        self.ui.O_off4_2.clicked.connect(lambda: self.off_individual(3, 1))
        self.ui.O_off5_2.clicked.connect(lambda: self.off_individual(4, 1))
        self.ui.O_off6_2.clicked.connect(lambda: self.off_individual(5, 1))
        self.ui.O_off7_2.clicked.connect(lambda: self.off_individual(6, 1))
        self.ui.O_off8_2.clicked.connect(lambda: self.off_individual(7, 1))

        self.ui.O_off1_3.clicked.connect(lambda: self.off_individual(0, 2))
        self.ui.O_off2_3.clicked.connect(lambda: self.off_individual(1, 2))
        self.ui.O_off3_3.clicked.connect(lambda: self.off_individual(2, 2))
        self.ui.O_off4_3.clicked.connect(lambda: self.off_individual(3, 2))
        self.ui.O_off5_3.clicked.connect(lambda: self.off_individual(4, 2))
        self.ui.O_off6_3.clicked.connect(lambda: self.off_individual(5, 2))
        self.ui.O_off7_3.clicked.connect(lambda: self.off_individual(6, 2))
        self.ui.O_off8_3.clicked.connect(lambda: self.off_individual(7, 2))

        self.ui.O_off1_4.clicked.connect(lambda: self.off_individual(0, 3))
        self.ui.O_off2_4.clicked.connect(lambda: self.off_individual(1, 3))
        self.ui.O_off3_4.clicked.connect(lambda: self.off_individual(2, 3))
        self.ui.O_off4_4.clicked.connect(lambda: self.off_individual(3, 3))
        self.ui.O_off5_4.clicked.connect(lambda: self.off_individual(4, 3))
        self.ui.O_off6_4.clicked.connect(lambda: self.off_individual(5, 3))
        self.ui.O_off7_4.clicked.connect(lambda: self.off_individual(6, 3))
        self.ui.O_off8_4.clicked.connect(lambda: self.off_individual(7, 3))

        self.ui.O_off1_5.clicked.connect(lambda: self.off_individual(0, 4))
        self.ui.O_off2_5.clicked.connect(lambda: self.off_individual(1, 4))
        self.ui.O_off3_5.clicked.connect(lambda: self.off_individual(2, 4))
        self.ui.O_off4_5.clicked.connect(lambda: self.off_individual(3, 4))
        self.ui.O_off5_5.clicked.connect(lambda: self.off_individual(4, 4))
        self.ui.O_off6_5.clicked.connect(lambda: self.off_individual(5, 4))
        self.ui.O_off7_5.clicked.connect(lambda: self.off_individual(6, 4))
        self.ui.O_off8_5.clicked.connect(lambda: self.off_individual(7, 4))

        self.ui.O_off1_6.clicked.connect(lambda: self.off_individual(0, 5))
        self.ui.O_off2_6.clicked.connect(lambda: self.off_individual(1, 5))
        self.ui.O_off3_6.clicked.connect(lambda: self.off_individual(2, 5))
        self.ui.O_off4_6.clicked.connect(lambda: self.off_individual(3, 5))
        self.ui.O_off5_6.clicked.connect(lambda: self.off_individual(4, 5))
        self.ui.O_off6_6.clicked.connect(lambda: self.off_individual(5, 5))
        self.ui.O_off7_6.clicked.connect(lambda: self.off_individual(6, 5))
        self.ui.O_off8_6.clicked.connect(lambda: self.off_individual(7, 5))

        self.ui.O_off1_7.clicked.connect(lambda: self.off_individual(0, 6))
        self.ui.O_off2_7.clicked.connect(lambda: self.off_individual(1, 6))
        self.ui.O_off3_7.clicked.connect(lambda: self.off_individual(2, 6))
        self.ui.O_off4_7.clicked.connect(lambda: self.off_individual(3, 6))
        self.ui.O_off5_7.clicked.connect(lambda: self.off_individual(4, 6))
        self.ui.O_off6_7.clicked.connect(lambda: self.off_individual(5, 6))
        self.ui.O_off7_7.clicked.connect(lambda: self.off_individual(6, 6))
        self.ui.O_off8_7.clicked.connect(lambda: self.off_individual(7, 6))

        self.ui.O_off1_8.clicked.connect(lambda: self.off_individual(0, 7))
        self.ui.O_off2_8.clicked.connect(lambda: self.off_individual(1, 7))
        self.ui.O_off3_8.clicked.connect(lambda: self.off_individual(2, 7))
        self.ui.O_off4_8.clicked.connect(lambda: self.off_individual(3, 7))
        self.ui.O_off5_8.clicked.connect(lambda: self.off_individual(4, 7))
        self.ui.O_off6_8.clicked.connect(lambda: self.off_individual(5, 7))
        self.ui.O_off7_8.clicked.connect(lambda: self.off_individual(6, 7))
        self.ui.O_off8_8.clicked.connect(lambda: self.off_individual(7, 7))

        self.ui.O_off1_9.clicked.connect(lambda: self.off_individual(0, 8))
        self.ui.O_off2_9.clicked.connect(lambda: self.off_individual(1, 8))
        self.ui.O_off3_9.clicked.connect(lambda: self.off_individual(2, 8))
        self.ui.O_off4_9.clicked.connect(lambda: self.off_individual(3, 8))
        self.ui.O_off5_9.clicked.connect(lambda: self.off_individual(4, 8))
        self.ui.O_off6_9.clicked.connect(lambda: self.off_individual(5, 8))
        self.ui.O_off7_9.clicked.connect(lambda: self.off_individual(6, 8))
        self.ui.O_off8_9.clicked.connect(lambda: self.off_individual(7, 8))

        self.ui.O_off1_10.clicked.connect(lambda: self.off_individual(0, 9))
        self.ui.O_off2_10.clicked.connect(lambda: self.off_individual(1, 9))
        self.ui.O_off3_10.clicked.connect(lambda: self.off_individual(2, 9))
        self.ui.O_off4_10.clicked.connect(lambda: self.off_individual(3, 9))
        self.ui.O_off5_10.clicked.connect(lambda: self.off_individual(4, 9))
        self.ui.O_off6_10.clicked.connect(lambda: self.off_individual(5, 9))
        self.ui.O_off7_10.clicked.connect(lambda: self.off_individual(6, 9))
        self.ui.O_off8_10.clicked.connect(lambda: self.off_individual(7, 9))

        self.ui.O_hold1_1.clicked.connect(lambda: self.hold_individual(0, 0))
        self.ui.O_hold2_1.clicked.connect(lambda: self.hold_individual(1, 0))
        self.ui.O_hold3_1.clicked.connect(lambda: self.hold_individual(2, 0))
        self.ui.O_hold4_1.clicked.connect(lambda: self.hold_individual(3, 0))
        self.ui.O_hold5_1.clicked.connect(lambda: self.hold_individual(4, 0))
        self.ui.O_hold6_1.clicked.connect(lambda: self.hold_individual(5, 0))
        self.ui.O_hold7_1.clicked.connect(lambda: self.hold_individual(6, 0))
        self.ui.O_hold8_1.clicked.connect(lambda: self.hold_individual(7, 0))

        self.ui.O_hold1_2.clicked.connect(lambda: self.hold_individual(0, 1))
        self.ui.O_hold2_2.clicked.connect(lambda: self.hold_individual(1, 1))
        self.ui.O_hold3_2.clicked.connect(lambda: self.hold_individual(2, 1))
        self.ui.O_hold4_2.clicked.connect(lambda: self.hold_individual(3, 1))
        self.ui.O_hold5_2.clicked.connect(lambda: self.hold_individual(4, 1))
        self.ui.O_hold6_2.clicked.connect(lambda: self.hold_individual(5, 1))
        self.ui.O_hold7_2.clicked.connect(lambda: self.hold_individual(6, 1))
        self.ui.O_hold8_2.clicked.connect(lambda: self.hold_individual(7, 1))

        self.ui.O_hold1_3.clicked.connect(lambda: self.hold_individual(0, 2))
        self.ui.O_hold2_3.clicked.connect(lambda: self.hold_individual(1, 2))
        self.ui.O_hold3_3.clicked.connect(lambda: self.hold_individual(2, 2))
        self.ui.O_hold4_3.clicked.connect(lambda: self.hold_individual(3, 2))
        self.ui.O_hold5_3.clicked.connect(lambda: self.hold_individual(4, 2))
        self.ui.O_hold6_3.clicked.connect(lambda: self.hold_individual(5, 2))
        self.ui.O_hold7_3.clicked.connect(lambda: self.hold_individual(6, 2))
        self.ui.O_hold8_3.clicked.connect(lambda: self.hold_individual(7, 2))

        self.ui.O_hold1_4.clicked.connect(lambda: self.hold_individual(0, 3))
        self.ui.O_hold2_4.clicked.connect(lambda: self.hold_individual(1, 3))
        self.ui.O_hold3_4.clicked.connect(lambda: self.hold_individual(2, 3))
        self.ui.O_hold4_4.clicked.connect(lambda: self.hold_individual(3, 3))
        self.ui.O_hold5_4.clicked.connect(lambda: self.hold_individual(4, 3))
        self.ui.O_hold6_4.clicked.connect(lambda: self.hold_individual(5, 3))
        self.ui.O_hold7_4.clicked.connect(lambda: self.hold_individual(6, 3))
        self.ui.O_hold8_4.clicked.connect(lambda: self.hold_individual(7, 3))

        self.ui.O_hold1_5.clicked.connect(lambda: self.hold_individual(0, 4))
        self.ui.O_hold2_5.clicked.connect(lambda: self.hold_individual(1, 4))
        self.ui.O_hold3_5.clicked.connect(lambda: self.hold_individual(2, 4))
        self.ui.O_hold4_5.clicked.connect(lambda: self.hold_individual(3, 4))
        self.ui.O_hold5_5.clicked.connect(lambda: self.hold_individual(4, 4))
        self.ui.O_hold6_5.clicked.connect(lambda: self.hold_individual(5, 4))
        self.ui.O_hold7_5.clicked.connect(lambda: self.hold_individual(6, 4))
        self.ui.O_hold8_5.clicked.connect(lambda: self.hold_individual(7, 4))

        self.ui.O_hold1_6.clicked.connect(lambda: self.hold_individual(0, 5))
        self.ui.O_hold2_6.clicked.connect(lambda: self.hold_individual(1, 5))
        self.ui.O_hold3_6.clicked.connect(lambda: self.hold_individual(2, 5))
        self.ui.O_hold4_6.clicked.connect(lambda: self.hold_individual(3, 5))
        self.ui.O_hold5_6.clicked.connect(lambda: self.hold_individual(4, 5))
        self.ui.O_hold6_6.clicked.connect(lambda: self.hold_individual(5, 5))
        self.ui.O_hold7_6.clicked.connect(lambda: self.hold_individual(6, 5))
        self.ui.O_hold8_6.clicked.connect(lambda: self.hold_individual(7, 5))

        self.ui.O_hold1_7.clicked.connect(lambda: self.hold_individual(0, 6))
        self.ui.O_hold2_7.clicked.connect(lambda: self.hold_individual(1, 6))
        self.ui.O_hold3_7.clicked.connect(lambda: self.hold_individual(2, 6))
        self.ui.O_hold4_7.clicked.connect(lambda: self.hold_individual(3, 6))
        self.ui.O_hold5_7.clicked.connect(lambda: self.hold_individual(4, 6))
        self.ui.O_hold6_7.clicked.connect(lambda: self.hold_individual(5, 6))
        self.ui.O_hold7_7.clicked.connect(lambda: self.hold_individual(6, 6))
        self.ui.O_hold8_7.clicked.connect(lambda: self.hold_individual(7, 6))

        self.ui.O_hold1_8.clicked.connect(lambda: self.hold_individual(0, 7))
        self.ui.O_hold2_8.clicked.connect(lambda: self.hold_individual(1, 7))
        self.ui.O_hold3_8.clicked.connect(lambda: self.hold_individual(2, 7))
        self.ui.O_hold4_8.clicked.connect(lambda: self.hold_individual(3, 7))
        self.ui.O_hold5_8.clicked.connect(lambda: self.hold_individual(4, 7))
        self.ui.O_hold6_8.clicked.connect(lambda: self.hold_individual(5, 7))
        self.ui.O_hold7_8.clicked.connect(lambda: self.hold_individual(6, 7))
        self.ui.O_hold8_8.clicked.connect(lambda: self.hold_individual(7, 7))

        self.ui.O_hold1_9.clicked.connect(lambda: self.hold_individual(0, 8))
        self.ui.O_hold2_9.clicked.connect(lambda: self.hold_individual(1, 8))
        self.ui.O_hold3_9.clicked.connect(lambda: self.hold_individual(2, 8))
        self.ui.O_hold4_9.clicked.connect(lambda: self.hold_individual(3, 8))
        self.ui.O_hold5_9.clicked.connect(lambda: self.hold_individual(4, 8))
        self.ui.O_hold6_9.clicked.connect(lambda: self.hold_individual(5, 8))
        self.ui.O_hold7_9.clicked.connect(lambda: self.hold_individual(6, 8))
        self.ui.O_hold8_9.clicked.connect(lambda: self.hold_individual(7, 8))

        self.ui.O_hold1_10.clicked.connect(lambda: self.hold_individual(0, 9))
        self.ui.O_hold2_10.clicked.connect(lambda: self.hold_individual(1, 9))
        self.ui.O_hold3_10.clicked.connect(lambda: self.hold_individual(2, 9))
        self.ui.O_hold4_10.clicked.connect(lambda: self.hold_individual(3, 9))
        self.ui.O_hold5_10.clicked.connect(lambda: self.hold_individual(4, 9))
        self.ui.O_hold6_10.clicked.connect(lambda: self.hold_individual(5, 9))
        self.ui.O_hold7_10.clicked.connect(lambda: self.hold_individual(6, 9))
        self.ui.O_hold8_10.clicked.connect(lambda: self.hold_individual(7, 9))

        self.ui.pB_on1.clicked.connect(lambda: self.on_group(0))
        self.ui.pB_on2.clicked.connect(lambda: self.on_group(1))
        self.ui.pB_on3.clicked.connect(lambda: self.on_group(2))
        self.ui.pB_hold1.clicked.connect(lambda: self.hold_group(0))
        self.ui.pB_hold2.clicked.connect(lambda: self.hold_group(1))
        self.ui.pB_hold3.clicked.connect(lambda: self.hold_group(2))
        self.ui.pB_off1.clicked.connect(lambda: self.off_group(0))
        self.ui.pB_off2.clicked.connect(lambda: self.off_group(1))
        self.ui.pB_off3.clicked.connect(lambda: self.off_group(2))
        self.ui.pB_ligar_tudo.clicked.connect(self.turn_all_on)
        self.ui.pB_emerg_geral.clicked.connect(self.shut_down)

        self.ui.pB_read_r0.clicked.connect(self.read_r0)
        self.ui.pB_read_t0.clicked.connect(self.read_t0)

        self.ui.pB_edit.clicked.connect(self.start_editing)
        self.ui.pB_save.clicked.connect(self.save)

        self.ui.pB_Quad.clicked.connect(lambda: self.config_local('Q'))
        self.ui.pB_Sext.clicked.connect(lambda: self.config_local('S'))
        self.ui.pB_Dip.clicked.connect(lambda: self.config_local('D'))
        self.ui.pB_Jaq.clicked.connect(lambda: self.config_local('J'))
        self.ui.pB_Vazio.clicked.connect(lambda: self.config_local('V'))
        self.ui.pB_G1.clicked.connect(lambda: self.config_group('1'))
        self.ui.pB_G2.clicked.connect(lambda: self.config_group('2'))
        self.ui.pB_G3.clicked.connect(lambda: self.config_group('3'))
        self.ui.pB_set_config.clicked.connect(self.set_configuration)
        self.ui.pB_escape_config.clicked.connect(self.escape_configuration)
        self.ui.pB_reset_chn.clicked.connect(self.reset_chn)

        self.ui.pB_n_est_aq.clicked.connect(self.enable_edit_stages)
        self.ui.pB_temp.clicked.connect(lambda: self.edit('temp'))
        self.ui.pB_taxa.clicked.connect(lambda: self.edit('taxa'))
        self.ui.pB_patamar.clicked.connect(lambda: self.edit('patamar'))
        self.ui.pB_escape.clicked.connect(self.escape_stages)
        self.ui.pB_t_entre_medidas.clicked.connect(self.set_meas_time)
        self.ui.pB_set_t0.clicked.connect(self.set_t0)

        self.init_timers()
        self.config_graph()
        self.ui.comboBox_live_1.currentIndexChanged.connect(lambda: self.refresh_axis_live_gvts(0))
        self.ui.comboBox_live_2.currentIndexChanged.connect(lambda: self.refresh_axis_live_gvts(1))
        self.ui.comboBox_live_3.currentIndexChanged.connect(lambda: self.refresh_axis_live_gvts(2))
        self.ui.comboBox_live_4.currentIndexChanged.connect(lambda: self.refresh_axis_live_gvts(3))
        self.ui.comboBox_live_5.currentIndexChanged.connect(lambda: self.refresh_axis_live_gvts(4))
        self.ui.comboBox_live_6.currentIndexChanged.connect(lambda: self.refresh_axis_live_gvts(5))
        self.ui.comboBox_live_7.currentIndexChanged.connect(lambda: self.refresh_axis_live_gvts(6))
        self.ui.comboBox_live_8.currentIndexChanged.connect(lambda: self.refresh_axis_live_gvts(7))
        self.ui.comboBox_live_9.currentIndexChanged.connect(lambda: self.refresh_axis_live_gvts(8))
        self.ui.comboBox_live_10.currentIndexChanged.connect(lambda: self.refresh_axis_live_gvts(9))
        self.ui.comboBox_live2_1.currentIndexChanged.connect(lambda: self.refresh_axis_live_grps(0))
        self.ui.comboBox_live2_2.currentIndexChanged.connect(lambda: self.refresh_axis_live_grps(1))
        self.ui.comboBox_live2_3.currentIndexChanged.connect(lambda: self.refresh_axis_live_grps(2))
        self.ui.comboBox_live2_4.currentIndexChanged.connect(lambda: self.refresh_axis_live_grps(3))

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Plastique'))
        QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())
        self.setStatusBar(QStatusBar())

        self.SOCKET_GVT = {0: Lib.fitaaque1, 1: Lib.fitaaque2, 2: Lib.fitaaque3, 3: Lib.fitaaque4, 4: Lib.fitaaque5, 5: Lib.fitaaque6, 6: Lib.fitaaque7, 7: Lib.fitaaque8, 8: Lib.fitaaque9, 9: Lib.fitaaque10}
        self.reading_thread = defaultdict()
        
    def config_graph(self):
        self.leg_gvt = []
        self.leg_grp = []

        for g in range(10):
            getattr(self.ui, 'graphic_gaveta_' + str(g + 1)).setLabel('left', text='Temperatura', units='°C', color='k')
            getattr(self.ui, 'graphic_gaveta_' + str(g + 1)).showGrid(True, True)
            self.leg_gvt.append(pg.LegendItem((40, 40), offset=(10, 10)))
            self.leg_gvt[g].setParentItem(getattr(self.ui, 'graphic_gaveta_' + str(g + 1)).graphicsItem())
            getattr(self.ui, 'graphic_gaveta_' + str(g + 1)).getAxis('left').setWidth(100)

        for i in range(4):
            getattr(self.ui, 'graphic_group_' + str(i + 1)).setLabel('left', text='Temperatura', units='°C', color='k')
            getattr(self.ui, 'graphic_group_' + str(i + 1)).showGrid(True, True)
            self.leg_grp.append(pg.LegendItem((40, 40), offset=(10, 10)))
            self.leg_grp[i].setParentItem(getattr(self.ui, 'graphic_group_' + str(i + 1)).graphicsItem())
            getattr(self.ui, 'graphic_group_' + str(i + 1)).getAxis('left').setWidth(100)

    def config_curves(self):
        Lib.graph.curves_grp = defaultdict(list)
        Lib.graph.curves_gvt = defaultdict(list)

        for g in range(10):
            for i in range(10):
                Lib.graph.curves_gvt[g].append(np.array([]))
                for j in range(8):
                    Lib.graph.curves_gvt[g][i] = np.append(Lib.graph.curves_gvt[g][i], getattr(self.ui, 'graphic_gaveta_' + str(g + 1)).plotItem.plot(np.array([]), np.array([])))
                    Lib.graph.curves_gvt[g][i][j].setPen(Lib.graph.pen[j], width=2)

        for a in range(4):
            for i in range(10):
                Lib.graph.curves_grp[a].append(np.array([]))
                for j in range(8):
                    Lib.graph.curves_grp[a][i] = np.append(Lib.graph.curves_grp[a][i],
                                                               getattr(self.ui, 'graphic_group_' + str(a + 1)).plotItem.plot(np.array([]), np.array([])))
                    Lib.graph.curves_grp[a][i][j].setPen(Lib.graph.pen[i], width=2)

    def set_index(self, index):
        self.ui.stackedWidget.setCurrentIndex(index)

    def connect(self):
        try:
            gvs_to_connect = []
            for i in range(10):
                if getattr(self.ui, 'connect_' + str(i + 1)).isChecked():
                    gvs_to_connect.append(i)

            for g in gvs_to_connect:
                if self.SOCKET_GVT[g].connect():
                    getattr(self.ui, 'led_sig_' + str(g + 1)).setEnabled(True)
                    getattr(self.ui, 'actionGaveta_' + str(g + 1) + 'o').setVisible(True)
                    getattr(self.ui, 'actionGaveta_' + str(g + 1) + 'g').setVisible(True)
                    getattr(self.ui, 'label_config' + str(g + 1)).setEnabled(True)
                    getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_1').setEnabled(True)
                    getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_2').setEnabled(True)
                    getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_3').setEnabled(True)
                    # Vitor
                    getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_4').setEnabled(True)
                    # Vitor
                    getattr(self.ui, 'groupBox_op' + str(g + 1)).setEnabled(True)
                    for chn in range(8):
                        getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setEnabled(True)
                    Lib.control.GAVETAS.append(g)
                    Lib.control.GAVETAS.sort()
        except Exception:
            traceback.print_exc(file=sys.stdout)
            return

    def disconnect(self):
        try:
            gvs_to_disconnect = []
            for i in range(10):
                if getattr(self.ui, 'connect_' + str(i + 1)).isChecked():
                    gvs_to_disconnect.append(i)

            for g in gvs_to_disconnect:
                if self.SOCKET_GVT[g].disconnect():
                    getattr(self.ui, 'led_sig_' + str(g + 1)).setEnabled(False)
                    getattr(self.ui, 'actionGaveta_' + str(g + 1) + 'o').setVisible(False)
                    getattr(self.ui, 'actionGaveta_' + str(g + 1) + 'g').setVisible(False)
                    getattr(self.ui, 'label_config' + str(g + 1)).setEnabled(False)
                    getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_1').setEnabled(False)
                    getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_2').setEnabled(False)
                    getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_3').setEnabled(False)
                    getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_4').setEnabled(False)
                    getattr(self.ui, 'groupBox_op' + str(g + 1)).setEnabled(False)
                    for chn in range(8):
                        getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setEnabled(False)
                        getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setText('S' + str(chn + 1))
                    Lib.control.GAVETAS.remove(g)
        except Exception:
            traceback.print_exc(file=sys.stdout)
            return

    def set_meas_time(self):
        for g in Lib.control.GAVETAS:
            if Lib.control.channels_on[g] != []:
                QtGui.QMessageBox.critical(self, 'Erro', 'Operação não concluída! Existe alguma saída ligada!', QtGui.QMessageBox.Ok)
                return
        try:
            t = int(self.ui.lineed_t_entre_medidas.text())
            if t == 0:
                QtGui.QMessageBox.critical(self, 'Erro', 'Insira um tempo válido!')
                return
            elif t == 1:
                QtGui.QMessageBox.information(self, 'Mensagem', 'Tempo configurado: %s segundo' % t, QtGui.QMessageBox.Ok)
            else:
                QtGui.QMessageBox.information(self, 'Mensagem', 'Tempo configurado: %s segundos' % t, QtGui.QMessageBox.Ok)
            Lib.control.meas_time = t
        except Exception:
            traceback.print_exc(file=sys.stdout)
            QtGui.QMessageBox.critical(self, 'Erro', 'Insira um tempo válido!', QtGui.QMessageBox.Ok)
            return

    def config_local(self, local):
        for g in Lib.control.GAVETAS:
            for chn in range(8):
                if getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).isChecked():
                    s = list(Lib.vars.name[g][chn])
                    if (g + 1) == 10:
                        s[5] = local
                    else:
                        s[4] = local
                    Lib.vars.name[g][chn] = ''.join(s)
                    getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setText(Lib.vars.name[g][chn])
                    getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setChecked(False)

                    if local == 'S':
                        getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setStyleSheet('background-color: rgb(143, 206, 133)')
                    elif local == 'Q':
                        getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setStyleSheet('background-color: rgb(255, 183, 94)')
                    elif local == 'D':
                        getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setStyleSheet('background-color: rgb(130, 202, 232)')
                    elif local == 'J':
                        getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setStyleSheet('background-color: rgb(255, 74, 77)')
                    elif local == 'V':
                        getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setStyleSheet('color: rgb(255, 255, 255); background-color: rgb(84, 84, 84)')

    def config_group(self, group):
        for g in Lib.control.GAVETAS:
            for chn in range(8):
                if getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).isChecked():
                    s = list(Lib.vars.name[g][chn])
                    if (g + 1) == 10:
                        s[6] = group
                    else:
                        s[5] = group
                    Lib.vars.name[g][chn] = ''.join(s)
                    getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setText(Lib.vars.name[g][chn])
                    getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setChecked(False)

    def set_configuration(self):
        self.ui.pB_Sext.setEnabled(False)
        self.ui.pB_Quad.setEnabled(False)
        self.ui.pB_Dip.setEnabled(False)
        self.ui.pB_Jaq.setEnabled(False)
        self.ui.pB_Vazio.setEnabled(False)
        self.ui.pB_G1.setEnabled(False)
        self.ui.pB_G2.setEnabled(False)
        self.ui.pB_G3.setEnabled(False)
        self.ui.pB_set_config.setEnabled(False)

        for g in Lib.control.GAVETAS:
            for chn in range(8):
                getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setChecked(False)
                getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setEnabled(False)
                if Lib.vars.name[g][chn] != 'G' + str(g + 1) + 'S' + str(chn + 1) + 'ab':
                    getattr(self.ui, 'label_G' + str(g + 1) + 'S' + str(chn + 1) + '_op').setText(Lib.vars.name[g][chn] + ':')
                    if (g + 1) == 10:
                        local = Lib.vars.name[g][chn][5]
                    else:
                        local = Lib.vars.name[g][chn][4]
                    if local == 'J':
                        Lib.control.PT100_channels[g].append(chn)
                        getattr(self.ui, 'O_nome' + str(chn + 1) + '_' + str(g + 1)).setStyleSheet('background-color: rgb(255, 74, 77)')
                        getattr(self.ui, 'label_G' + str(g + 1) + 'S' + str(chn + 1) + '_op').setStyleSheet('background-color: rgb(255, 74, 77)')
                        getattr(self.ui, 'label_gr' + str(chn + 1) + '_' + str(g + 1)).setStyleSheet('background-color: rgb(255, 74, 77)')
                        # for i in range(n_jaqs):
                        #    getattr(self.ui, 'comboBox_jaq' + str(i + 1)).addItem(Lib.vars.name[g][chn])
                    elif local == 'Q':
                        getattr(self.ui, 'O_nome' + str(chn + 1) + '_' + str(g + 1)).setStyleSheet('background-color: rgb(255, 183, 94)')
                        getattr(self.ui, 'label_G' + str(g + 1) + 'S' + str(chn + 1) + '_op').setStyleSheet('background-color: rgb(255, 183, 94)')
                        getattr(self.ui, 'label_gr' + str(chn + 1) + '_' + str(g + 1)).setStyleSheet('background-color: rgb(255, 183, 94)')
                        # for i in range(n_quads):
                        #    getattr(self.ui, 'comboBox_quad' + str(i + 1)).addItem(Lib.vars.name[g][chn])
                    elif local == 'D':
                        getattr(self.ui, 'O_nome' + str(chn + 1) + '_' + str(g + 1)).setStyleSheet('background-color: rgb(130, 202, 232)')
                        getattr(self.ui, 'label_G' + str(g + 1) + 'S' + str(chn + 1) + '_op').setStyleSheet('background-color: rgb(130, 202, 232)')
                        getattr(self.ui, 'label_gr' + str(chn + 1) + '_' + str(g + 1)).setStyleSheet('background-color: rgb(130, 202, 232)')
                        # for i in range(n_dips):
                        #    getattr(self.ui, 'comboBox_dip' + str(i + 1)).addItem(Lib.vars.name[g][chn])
                    elif local == 'S':
                        getattr(self.ui, 'O_nome' + str(chn + 1) + '_' + str(g + 1)).setStyleSheet('background-color: rgb(143, 206, 133)')
                        getattr(self.ui, 'label_G' + str(g + 1) + 'S' + str(chn + 1) + '_op').setStyleSheet('background-color: rgb(143, 206, 133)')
                        getattr(self.ui, 'label_gr' + str(chn + 1) + '_' + str(g + 1)).setStyleSheet('background-color: rgb(143, 206, 133)')
                        # for i in range(n_sexts):
                        #    getattr(self.ui, 'comboBox_sext' + str(i + 1)).addItem(Lib.vars.name[g][chn])
                    elif local == 'V':
                        getattr(self.ui, 'O_nome' + str(chn + 1) + '_' + str(g + 1)).setStyleSheet('color: rgb(255, 255, 255); background-color: rgb(84, 84, 84)')
                        getattr(self.ui, 'label_G' + str(g + 1) + 'S' + str(chn + 1) + '_op').setStyleSheet('color: rgb(255, 255, 255); background-color: rgb(84, 84, 84)')
                        getattr(self.ui, 'label_gr' + str(chn + 1) + '_' + str(g + 1)).setStyleSheet('color: rgb(255, 255, 255); background-color: rgb(84, 84, 84)')
                        # for i in range(n_vazios):
                        #    getattr(self.ui, 'comboBox_vazio' + str(i + 1)).addItem(Lib.vars.name[g][chn])
                try:
                    if (g + 1) == 10:
                        group = int(getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).text()[6]) - 1
                    else:
                        group = int(getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).text()[5]) - 1
                    if g not in Lib.control.group[group]:
                        Lib.control.group[group][g] = []
                    if chn not in Lib.control.group[group][g]:
                        Lib.control.group[group][g].append(chn)
                except ValueError:
                    traceback.print_exc(file=sys.stdout)
                    QtGui.QMessageBox.critical(self, 'Erro', 'Existe algum canal configurado sem grupo! Reinicie a configuração', QtGui.QMessageBox.Ok)
                    return
                except IndexError:
                    pass

    def escape_configuration(self):
        self.ui.pB_Sext.setEnabled(True)
        self.ui.pB_Quad.setEnabled(True)
        self.ui.pB_Dip.setEnabled(True)
        self.ui.pB_Jaq.setEnabled(True)
        self.ui.pB_Vazio.setEnabled(True)
        self.ui.pB_G1.setEnabled(True)
        self.ui.pB_G2.setEnabled(True)
        self.ui.pB_G3.setEnabled(True)
        self.ui.pB_set_config.setEnabled(True)
        self.ui.pB_edit.setEnabled(True)

        for g in Lib.control.GAVETAS:
            Lib.control.PT100_channels[g] = []
            Lib.vars.channels[g] = []

            for chn in range(8):
                getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setStyleSheet('')
                getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setEnabled(True)
                getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setChecked(False)
                getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setText('S' + str(chn + 1))
                getattr(self.ui, 'checkBox_saida' + str(chn + 1) + '_' + str(g + 1)).setChecked(False)
                getattr(self.ui, 'checkBox_saida' + str(chn + 1) + '_' + str(g + 1)).setEnabled(False)
                getattr(self.ui, 'groupBox_saida' + str(chn + 1) + '_' + str(g + 1)).setEnabled(False)
                getattr(self.ui, 'label_gr' + str(chn + 1) + '_' + str(g + 1)).setText('Saída ' + str(chn + 1))
                getattr(self.ui, 'label_G' + str(g + 1) + 'S' + str(chn + 1) + '_op').setText('Saída ' + str(chn + 1) + ':')
                getattr(self.ui, 'label_G' + str(g + 1) + 'S' + str(chn + 1) + '_op').setEnabled(False)
                getattr(self.ui, 'lineed_G' + str(g + 1) + 'S' + str(chn + 1)).setEnabled(False)
                Lib.vars.name[g][chn] = 'G' + str(g + 1) + 'S' + str(chn + 1) + 'ab'
                getattr(self.ui, 'O_nome' + str(chn + 1) + '_' + str(g + 1)).setStyleSheet('color: rgb(0, 0, 0)')
                getattr(self.ui, 'label_G' + str(g + 1) + 'S' + str(chn + 1) + '_op').setStyleSheet('color: rgb(0, 0, 0)')
                getattr(self.ui, 'label_gr' + str(chn + 1) + '_' + str(g + 1)).setStyleSheet('color: rgb(0, 0, 0)')

        for group in range(3):
            Lib.control.group[group] = defaultdict(list)

        for g in range(10):
            getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_1').setChecked(False)
            getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_1').setEnabled(False)
            getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_2').setChecked(False)
            getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_2').setEnabled(False)
            getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_3').setChecked(False)
            getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_3').setEnabled(False)
            getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_4').setChecked(False)
            getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_4').setEnabled(False)
            
    def reset_chn(self):
        for g in Lib.control.GAVETAS:
            for chn in range(8):
                if getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).isChecked():
                    getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setStyleSheet('')
                    getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setEnabled(True)
                    getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setChecked(False)
                    getattr(self.ui, 'pB_config_G' + str(g + 1) + 'S' + str(chn + 1)).setText('S' + str(chn + 1))
                    Lib.vars.name[g][chn] = 'G' + str(g + 1) + 'S' + str(chn + 1) + 'ab'              

    def read_r0(self):
        gvt = self.ui.spinBox_gvt_2.value() - 1
        chn = self.ui.spinBox_chn_2.value() - 1
        try:
            index = Lib.vars.channels[gvt].index(chn)
            self.ui.r0.setText(str('{:.2f}'.format(Lib.vars.r0[gvt][index])))
        except Exception:
            traceback.print_exc(file=sys.stdout)
            QtGui.QMessageBox.critical(self, 'Erro', 'Canal selecionado não ativo!', QtGui.QMessageBox.Ok)
            self.ui.r0.setText('')

    def read_t0(self):
        gvt = self.ui.spinBox_gvt_2.value() - 1
        chn = self.ui.spinBox_chn_2.value() - 1
        try:
            index = Lib.vars.channels[gvt].index(chn)
            self.ui.t0.setText(str('{:.2f}'.format(Lib.vars.t0[gvt][index])))
        except Exception:
            traceback.print_exc(file=sys.stdout)
            QtGui.QMessageBox.critical(self, 'Erro', 'Canal selecionado não ativo!', QtGui.QMessageBox.Ok)
            self.ui.t0.setText('')

    def set_t0(self):
        g = int(self.ui.comboBox_gvt.currentText()) - 1

        if g not in Lib.control.GAVETAS:
            QtGui.QMessageBox.critical(self, 'Erro', 'Gaveta não conectada!', QtGui.QMessageBox.Ok)
            return

        if self.ui.comboBox_chn.currentText() == 'Todas':
            t0 = [float(self.ui.lineed_t0.text())] * len(Lib.vars.channels[g])
        else:
            chn = int(self.ui.comboBox_chn.currentText()) - 1
            if chn not in Lib.vars.channels[g]:
                QtGui.QMessageBox.critical(self, 'Erro', 'Canal não ativo!', QtGui.QMessageBox.Ok)
                return
            t0 = self.SOCKET_GVT[g].read('O')
            index = Lib.vars.channels[g].index(chn)
            t0[index] = float(self.ui.lineed_t0.text())

        Lib.vars.t0[g] = t0
        try:
            self.SOCKET_GVT[g].set_t0(t0)
            QtGui.QMessageBox.information(self, 'Mensagem', 'Temperatura configurada!', QtGui.QMessageBox.Ok)
        except Exception:
            traceback.print_exc(file=sys.stdout)
            QtGui.QMessageBox.critical(self, 'Erro', 'A temperatura inicial não foi configurada corretamente!', QtGui.QMessageBox.Ok)

    def start_editing(self):
        group = int(self.ui.label_group.text()[-1]) - 1
        if Lib.control.group[group] == {}:
            QtGui.QMessageBox.critical(self, 'Erro', 'Configure e salve as saídas do grupo antes de editar!', QtGui.QMessageBox.Ok)
            return
        self.ui.lineed_n_est_aq.setEnabled(True)
        self.ui.pB_n_est_aq.setEnabled(True)
        self.ui.lineed_temp.setText('')
        self.ui.lineed_taxa.setText('')
        self.ui.lineed_patamar.setText('')
        self.reset(group)
        self.ui.pB_edit.setEnabled(False)

    def enable_edit_stages(self):
        try:
            int(self.ui.lineed_n_est_aq.text())
            self.ui.temp_label.setEnabled(True)
            self.ui.taxa_label.setEnabled(True)
            self.ui.patamar_label.setEnabled(True)
            self.ui.lineed_temp.setEnabled(True)
            self.ui.lineed_taxa.setEnabled(True)
            self.ui.lineed_patamar.setEnabled(True)
            self.ui.pB_temp.setEnabled(True)
            self.ui.pB_taxa.setEnabled(True)
            self.ui.pB_patamar.setEnabled(True)
            self.ui.lineed_n_est_aq.setEnabled(False)
            self.ui.pB_n_est_aq.setEnabled(False)
        except Exception:
            traceback.print_exc(file=sys.stdout)
            QtGui.QMessageBox.critical(self, 'Erro', 'Valor inválido, tente novamente', QtGui.QMessageBox.Ok)

    def edit(self, var):
        if var == 'temp':
            text = 'Temp%s(°C):'
        elif var == 'taxa':
            text = 'Taxa%s(°C/min):'
        elif var == 'patamar':
            text = 'Patamar%s(min):'

        group = int(self.ui.label_group.text()[-1]) - 1
        n_aq = getattr(Lib.config, 'n_aq_' + var)

        if n_aq[group] < int(self.ui.lineed_n_est_aq.text()):
            try:
                if var == 'temp':
                    for g in Lib.control.group[group]:
                        for chn in Lib.control.group[group][g]:
                            Lib.config.temp[g][chn].append(float(self.ui.lineed_temp.text()))
                            Lib.config.temp[g][chn].append(float(self.ui.lineed_temp.text()))
                else:
                    getattr(Lib.config, var)[group].append(float(getattr(self.ui, 'lineed_' + var).text()))
            except ValueError:
                traceback.print_exc(file=sys.stdout)
                QtGui.QMessageBox.critical(self, 'Erro', 'Valor inválido, tente novamente', QtGui.QMessageBox.Ok)
                return
            getattr(self.ui, 'lineed_' + var).setText('')
            getattr(self.ui, var + '_label').setText(text % (n_aq[group] + 1))
            n_aq[group] += 1
        else:
            try:
                if var == 'temp':
                    for g in Lib.control.group[group]:
                        for chn in Lib.control.group[group][g]:
                            Lib.config.temp[g][chn].append(float(self.ui.lineed_temp.text()))
                            Lib.config.temp[g][chn].append(float(self.ui.lineed_temp.text()))
                else:
                    getattr(Lib.config, var)[group].append(float(getattr(self.ui, 'lineed_' + var).text()))
            except ValueError:
                traceback.print_exc(file=sys.stdout)
                QtGui.QMessageBox.critical(self, 'Erro', 'Valor inválido, tente novamente', QtGui.QMessageBox.Ok)
                return
            # getattr(self.ui, 'lineed_' + var).setText('')
            getattr(self.ui, 'lineed_' + var).setEnabled(False)
            getattr(self.ui, 'pB_' + var).setEnabled(False)
            self.ui.pB_save.setEnabled(True)
            n_aq[group] = 1

    def save(self):
        if self.ui.lineed_temp.isEnabled() or self.ui.lineed_taxa.isEnabled() or self.ui.lineed_patamar.isEnabled():
            QtGui.QMessageBox.critical(self, 'Erro', 'Finalize a configuração antes de prossegir!', QtGui.QMessageBox.Ok)
            return

        group = int(self.ui.label_group.text()[-1]) - 1
        getattr(self.ui, 'actionGrupo_' + str(group + 1)).setVisible(True)
        getattr(self.ui, 'actionGrupo_4').setVisible(True)
        getattr(self.ui, 'groupBox_' + str(group + 1)).setEnabled(True)
        QtGui.QApplication.setOverrideCursor(Qt.WaitCursor)
        for g in Lib.control.group[group]:
            Lib.control.run_control_on[g] = False
            Lib.control.curves_on[g] = False
            self.SOCKET_GVT[g].reset_run_control()

            for chn in Lib.control.group[group][g]:
                Lib.vars.channels[g].append(chn)
                Lib.vars.channels[g].sort()
                self.SOCKET_GVT[g].get_initial_parameters(chn)
                getattr(self.ui, 'checkBox_saida' + str(chn + 1) + '_' + str(g + 1)).setEnabled(True)
                getattr(self.ui, 'groupBox_saida' + str(chn + 1) + '_' + str(g + 1)).setEnabled(True)
                getattr(self.ui, 'label_gr' + str(chn + 1) + '_' + str(g + 1)).setText(Lib.vars.name[g][chn])
                getattr(self.ui, 'label_G' + str(g + 1) + 'S' + str(chn + 1) + '_op').setEnabled(True)
                getattr(self.ui, 'lineed_G' + str(g + 1) + 'S' + str(chn + 1)).setEnabled(True)
                getattr(self.ui, 'O_nome' + str(chn + 1) + '_' + str(g + 1)).setText(Lib.vars.name[g][chn])

            self.SOCKET_GVT[g].set_active_channels(Lib.vars.channels[g])
            self.SOCKET_GVT[g].set_enabled_channels(Lib.vars.channels[g])
            self.SOCKET_GVT[g].set_PT100(Lib.control.PT100_channels[g])
            Lib.vars.t0[g] = self.SOCKET_GVT[g].read('O')
            Lib.vars.r0[g] = self.SOCKET_GVT[g].read('r')
            Lib.vars.a[g] = self.SOCKET_GVT[g].read('A')

        QtGui.QApplication.restoreOverrideCursor()
        self.ui.lineed_n_est_aq.setEnabled(False)
        self.ui.pB_n_est_aq.setEnabled(False)

        self.ui.temp_label.setEnabled(False)
        self.ui.taxa_label.setEnabled(False)
        self.ui.patamar_label.setEnabled(False)
        self.ui.pB_temp.setEnabled(False)
        self.ui.pB_taxa.setEnabled(False)
        self.ui.pB_patamar.setEnabled(False)
        self.ui.lineed_temp.setEnabled(False)
        self.ui.lineed_taxa.setEnabled(False)
        self.ui.lineed_patamar.setEnabled(False)

        self.ui.temp_label.setText('Temp1(°C):')
        self.ui.taxa_label.setText('Taxa1(°C/min):')
        self.ui.patamar_label.setText('Patamar1(min):')
        if group == 0 and Lib.control.group[1] != {}:
            QtGui.QMessageBox.information(self, 'Mensagem', 'Grupo 1 configurado!', QtGui.QMessageBox.Ok)
            self.ui.label_group.setText('Grupo 2')
            self.ui.pB_edit.setEnabled(True)
        elif group == 0 and Lib.control.group[1] == {} and Lib.control.group[2] != {}:
            QtGui.QMessageBox.information(self, 'Mensagem', 'Grupo 1 configurado!', QtGui.QMessageBox.Ok)
            self.ui.label_group.setText('Grupo 3')
            self.ui.pB_edit.setEnabled(True)
        elif group == 1 and Lib.control.group[2] != {}:
            QtGui.QMessageBox.information(self, 'Mensagem', 'Grupo 2 configurado!', QtGui.QMessageBox.Ok)
            self.ui.label_group.setText('Grupo 3')
            self.ui.pB_edit.setEnabled(True)
        else:
            for g in Lib.control.GAVETAS:
                if Lib.vars.channels[g] != []:
                    if Lib.control.PT100_channels[g] != []:
                        tmp = 0
                        for chn in Lib.control.PT100_channels[g]:
                            idx = Lib.vars.channels[g].index(chn)
                            tmp += Lib.vars.t0[g][idx]
                        t0_med = tmp / len(Lib.control.PT100_channels[g])

                        for chn in Lib.vars.channels[g]:
                            if chn not in Lib.control.PT100_channels[g]:
                                idx = Lib.vars.channels[g].index(chn)
                                Lib.vars.t0[g][idx] = t0_med
                    else:
                        QtGui.QMessageBox.information(self, 'Atenção', 'Não existe nenhum canal Pt100 na gaveta %s! As temperaturas iniciais deverão ser configuradas manualmente!' % (g + 1), QtGui.QMessageBox.Ok)
                        continue

                    self.SOCKET_GVT[g].set_parameters(Lib.vars.r0[g], Lib.vars.t0[g], Lib.vars.a[g])

            QtGui.QApplication.restoreOverrideCursor()
            self.ui.label_group.setText('Grupo 1')
            self.ui.lineed_n_est_aq.setText('')
            self.ui.lineed_temp.setText('')
            self.ui.lineed_taxa.setText('')
            self.ui.lineed_patamar.setText('')
            self.ui.GroupBox_t0.setEnabled(True)
            QtGui.QMessageBox.information(self, 'Mensagem', 'Todos os grupos estão configurados! Você pode verificar as temperaturas iniciais na tela de Operação Geral', QtGui.QMessageBox.Ok)
            self.config_curves()

    def escape_stages(self):
        self.ui.lineed_n_est_aq.setText('')
        self.ui.lineed_temp.setText('')
        self.ui.lineed_taxa.setText('')
        self.ui.lineed_patamar.setText('')
        self.ui.temp_label.setText('Temp1(°C):')
        self.ui.taxa_label.setText('Taxa1(°C/min):')
        self.ui.patamar_label.setText('Patamar1(min):')
        self.ui.lineed_n_est_aq.setEnabled(False)
        self.ui.pB_n_est_aq.setEnabled(False)
        self.ui.temp_label.setEnabled(False)
        self.ui.taxa_label.setEnabled(False)
        self.ui.patamar_label.setEnabled(False)
        self.ui.pB_temp.setEnabled(False)
        self.ui.pB_taxa.setEnabled(False)
        self.ui.pB_patamar.setEnabled(False)
        self.ui.lineed_temp.setEnabled(False)
        self.ui.lineed_taxa.setEnabled(False)
        self.ui.lineed_patamar.setEnabled(False)
        self.ui.pB_edit.setEnabled(True)
        self.ui.label_group.setText('Grupo 1')

        for g in Lib.control.GAVETAS:
            Lib.vars.channels[g] = []
            for chn in range(8):
                Lib.config.temp[g][chn] = []
                Lib.config.times[g][chn] = []
                Lib.vars.interpolation_points[g][chn] = []

        for i in range(3):
            Lib.config.taxa[i] = []
            Lib.config.patamar[i] = []

    def on_group(self, group):
        if Lib.control.meas_time == None:
            QtGui.QMessageBox.critical(self, 'Erro', 'Operação não concluída! Configure o tempo entre as medidas!', QtGui.QMessageBox.Ok)
            return

        for g in Lib.control.group[group]:
            for chn in Lib.control.group[group][g]:
                getattr(self.ui, 'O_off' + str(chn + 1) + '_' + str(g + 1)).setEnabled(True)
                Lib.control.channels_on[g].append(chn)
                Lib.control.channels_on[g].sort()
                Lib.vars.start_time[g][chn] = time.time()
                index = Lib.vars.channels[g].index(chn)
                Lib.measurements['Tempo'][g][chn] = np.append(Lib.measurements['Tempo'][g][chn], 0)
                Lib.measurements['Tensão'][g][chn] = np.append(Lib.measurements['Tensão'][g][chn], 0)
                Lib.measurements['Corrente'][g][chn] = np.append(Lib.measurements['Corrente'][g][chn], 0)
                Lib.measurements['Potência'][g][chn] = np.append(Lib.measurements['Potência'][g][chn], 0)
                Lib.measurements['Temperatura'][g][chn] = np.append(Lib.measurements['Temperatura'][g][chn], Lib.vars.t0[g][index])
                Lib.config.temp[g][chn].insert(0, Lib.vars.t0[g][index])

                self.calculate_send_points(chn, g, group)

            if not(Lib.control.run_control_on[g]):
                Lib.control.run_control_on[g] = self.SOCKET_GVT[g].run_control()
                Lib.vars.file[g] = self.open_file(g)
            if not(Lib.control.curves_on[g]):
                Lib.control.curves_on[g] = self.SOCKET_GVT[g].turn_on()
                Lib.control.GAVETAS_ON.append(g)
                self.reading_thread[g] = threading.Thread(target=Lib.reading_th, args=(g,))
                # Vitor
                self.reading_thread[g].setDaemon(True)
                # Vitor
                self.reading_thread[g].start()

        self.timer[group].start(1000)
        getattr(self.ui, 'pB_on' + str(group + 1)).setEnabled(False)
        getattr(self.ui, 'pB_off' + str(group + 1)).setEnabled(True)
        if not(Lib.control.measurements_ON):
            self.refresh_timer.start(500)
            Lib.control.measurements_ON = True

    def off_group(self, group):
        getattr(self.ui, 'groupBox_' + str(group + 1)).setEnabled(False)

        for g in list(Lib.control.group[group].keys()):
            enabled_chns = self.SOCKET_GVT[g].read_channels('E')
            if enabled_chns == 'NONE':
                pass
            else:
                gr = Lib.control.group[group][g][:]

                for chn in gr:
                    if chn in Lib.control.channels_on[g]:
                        getattr(self.ui, 'O_off' + str(chn + 1) + '_' + str(g + 1)).setEnabled(False)
                        try:
                            enabled_chns.remove(chn)
                            self.SOCKET_GVT[g].set_enabled_channels(enabled_chns)
                        except Exception:
                            traceback.print_exc(file=sys.stdout)
                            pass

                        if chn in Lib.control.PT100_channels[g]:
                            Lib.control.channels_off[g].append(chn)
                            Lib.control.channels_off[g].sort()
                        else:
                            self.turn_off(g, chn)

        self.timer[group].stop()
        getattr(self.ui, 'pB_on' + str(group + 1)).setEnabled(True)
        getattr(self.ui, 'pB_off' + str(group + 1)).setEnabled(False)
        getattr(self.ui, 'lineed_time' + str(group + 1)).setText('')

        for g in range(10):
            getattr(self.ui, 'O_lineed_time' + str(group + 1) + '_' + str(g + 1)).setText('')

    def hold_group(self, group):
        if getattr(self.ui, 'pB_hold' + str(group + 1)).isChecked():
            for g in Lib.control.group[group]:
                Lib.control.holded_channels[g] = self.SOCKET_GVT[g].read_channels('L')

                if Lib.control.holded_channels[g] == 'NONE':
                    Lib.control.holded_channels[g] = Lib.control.group[group][g][:]
                else:
                    Lib.control.holded_channels[g] = Lib.control.holded_channels[g] + Lib.control.group[group][g][:]
                for chn in Lib.control.group[group][g]:
                    Lib.vars.hold_start[g][chn] = time.time()

                Lib.control.holded_channels[g].sort()
                self.SOCKET_GVT[g].hold(Lib.control.holded_channels[g])
        else:
            for g in Lib.control.group[group]:
                Lib.control.holded_channels[g] = self.SOCKET_GVT[g].read_channels('L')
                aux_vect = Lib.control.holded_channels[g][:]
                for chn in aux_vect:
                    Lib.vars.total_time[g][chn] += (time.time() - Lib.vars.hold_start[g][chn])
                    Lib.control.holded_channels[g].remove(chn)

                Lib.control.holded_channels[g].sort()
                self.SOCKET_GVT[g].hold(Lib.control.holded_channels[g])

    def on_individual(self, chn, g):
        try:
            enabled_chns = self.SOCKET_GVT[g].read_channels('E')
            if enabled_chns == 'NONE':
                enabled_chns = [chn]
                if not(Lib.control.run_control_on[g]):
                    Lib.control.run_control_on[g] = self.SOCKET_GVT[g].run_control()
                    Lib.vars.file[g] = self.open_file(g)
                if not(Lib.control.curves_on[g]):
                    Lib.control.curves_on[g] = self.SOCKET_GVT[g].turn_on()
                    Lib.control.GAVETAS_ON.append(g)
                    self.reading_thread[g] = threading.Thread(target=Lib.reading_th, name=g, args=(g,))
                    # Vitor
                    self.reading_thread[g].setDaemon(True)
                    # Vitor
                    self.reading_thread[g].start()

                if not(Lib.control.measurements_ON):
                    self.refresh_timer.start(500)
                    Lib.control.measurements_ON = True
            else:
                enabled_chns.append(chn)
                enabled_chns.sort()

            if chn in Lib.control.channels_off[g]:
                Lib.control.channels_off[g].remove(chn)
            else:
                Lib.control.channels_on[g].append(chn)
                Lib.control.channels_on[g].sort()
            self.SOCKET_GVT[g].set_enabled_channels(enabled_chns)
            getattr(self.ui, 'O_on' + str(chn + 1) + '_' + str(g + 1)).setEnabled(False)
            getattr(self.ui, 'O_off' + str(chn + 1) + '_' + str(g + 1)).setEnabled(True)
        except Exception:
            traceback.print_exc(file=sys.stdout)
            QtGui.QMessageBox.critical(self, 'Erro', 'O canal não foi ligado corretamente', QtGui.QMessageBox.Ok)
            getattr(self.ui, 'O_on' + str(chn + 1) + '_' + str(g + 1)).setEnabled(True)
            getattr(self.ui, 'O_off' + str(chn + 1) + '_' + str(g + 1)).setEnabled(False)
            return

    def off_individual(self, chn, g):
        try:
            enabled_chns = self.SOCKET_GVT[g].read_channels('E')
            enabled_chns.remove(chn)
            self.SOCKET_GVT[g].set_enabled_channels(enabled_chns)

            if chn in Lib.control.PT100_channels[g]:
                pass
            else:
                Lib.control.channels_on[g].remove(chn)
                if Lib.control.channels_on[g] == []:
                    Lib.control.GAVETAS_ON.remove(g)
                    Lib.vars.file[g].close()

                getattr(self.ui, 'O_t0' + str(chn + 1) + '_' + str(g + 1)).setText('')
                getattr(self.ui, 'O_r0' + str(chn + 1) + '_' + str(g + 1)).setText('')
                getattr(self.ui, 'O_i' + str(chn + 1) + '_' + str(g + 1)).setText('')
                getattr(self.ui, 'O_v' + str(chn + 1) + '_' + str(g + 1)).setText('')
                getattr(self.ui, 'O_p' + str(chn + 1) + '_' + str(g + 1)).setText('')
                getattr(self.ui, 'O_temp' + str(chn + 1) + '_' + str(g + 1)).setText('')
                getattr(self.ui, 'O_fita' + str(chn + 1) + '_' + str(g + 1)).setText('')
                getattr(self.ui, 'O_pt100' + str(chn + 1) + '_' + str(g + 1)).setText('')
                getattr(self.ui, 'lineed_G' + str(g + 1) + 'S' + str(chn + 1)).setText('')

            getattr(self.ui, 'O_on' + str(chn + 1) + '_' + str(g + 1)).setEnabled(True)
            getattr(self.ui, 'O_off' + str(chn + 1) + '_' + str(g + 1)).setEnabled(False)
        except Exception:
            traceback.print_exc(file=sys.stdout)
            QtGui.QMessageBox.critical(self, 'Erro', 'O canal não foi desligado corretamente', QtGui.QMessageBox.Ok)
            getattr(self.ui, 'O_on' + str(chn + 1) + '_' + str(g + 1)).setEnabled(False)
            getattr(self.ui, 'O_off' + str(chn + 1) + '_' + str(g + 1)).setEnabled(True)
            return

    def hold_individual(self, chn, g):
        try:
            Lib.control.holded_channels[g] = self.SOCKET_GVT[g].read_channels('L')
            if getattr(self.ui, 'O_hold' + str(chn + 1) + '_' + str(g + 1)).isChecked():
                if Lib.control.holded_channels[g] == 'NONE':
                    Lib.control.holded_channels[g] = [chn]
                else:
                    Lib.control.holded_channels[g] = Lib.control.holded_channels[g] + [chn]
                    Lib.control.holded_channels[g].sort()
                Lib.vars.hold_start[g][chn] = time.time()
            else:
                Lib.control.holded_channels[g].remove(chn)
                Lib.vars.total_time[g][chn] += (time.time() - Lib.vars.hold_start[g][chn])
            self.SOCKET_GVT[g].hold(Lib.control.holded_channels[g])
        except Exception:
            traceback.print_exc(file=sys.stdout)
            if getattr(self.ui, 'O_hold' + str(chn + 1) + '_' + str(g + 1)).isChecked():
                QtGui.QMessageBox.critical(self, 'Erro', 'O canal não entrou em hold corretamente', QtGui.QMessageBox.Ok)
                getattr(self.ui, 'O_hold' + str(chn + 1) + '_' + str(g + 1)).setChecked(False)
            else:
                QtGui.QMessageBox.critical(self, 'Erro', 'O canal não saiu do hold corretamente', QtGui.QMessageBox.Ok)
                getattr(self.ui, 'O_hold' + str(chn + 1) + '_' + str(g + 1)).setChecked(True)
            return

    def turn_all_on(self):
        for group in Lib.control.group:
            if getattr(self.ui, 'groupBox_' + str(group + 1)).isEnabled() and getattr(self.ui, 'lineed_time' + str(group + 1)).text() == '':
                self.on_group(group)

    def shut_down(self):
        answ = QtGui.QMessageBox.question(self, 'Desligar tudo', 'Esse comando desligará todas as gavetas. Deseja continuar?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if answ == QtGui.QMessageBox.Yes:
            for group in Lib.control.group:
                if getattr(self.ui, 'groupBox_' + str(group + 1)).isEnabled():
                    self.off_group(group)
        else:
            pass

    def stop_interface(self):
        for group in Lib.control.group:
            self.timer[group].stop()
            getattr(self.ui, 'actionGrupo_' + str(group + 1)).setVisible(False)
            getattr(self.ui, 'actionGrupo_4').setVisible(False)
            getattr(self.ui, 'pB_on' + str(group + 1)).setEnabled(True)
            getattr(self.ui, 'pB_off' + str(group + 1)).setEnabled(False)
            getattr(self.ui, 'lineed_time' + str(group + 1)).setText('')
            getattr(self.ui, 'groupBox_' + str(group + 1)).setEnabled(False)
        for g in Lib.control.GAVETAS:
            self.SOCKET_GVT[g].end_curves()
            Lib.control.curves_on[g] = False
            Lib.control.run_control_on[g] = False
            for chn in range(8):
                getattr(self.ui, 'O_on' + str(chn + 1) + '_' + str(g + 1)).setEnabled(False)
                getattr(self.ui, 'O_off' + str(chn + 1) + '_' + str(g + 1)).setEnabled(False)
            try:
                del self.reading_thread[g]
            except Exception:
                traceback.print_exc(file=sys.stdout)
                pass

        Lib.control.measurements_ON = False
        self.refresh_timer.stop()
        self.escape_stages()

    def turn_off(self, g, chn):
        if chn in Lib.control.channels_off[g]:
            Lib.control.channels_off[g].remove(chn)
        try:
            enabled_chns = self.SOCKET_GVT[g].read_channels('E')
            enabled_chns.remove(chn)
            self.SOCKET_GVT[g].set_enabled_channels(enabled_chns)
        except Exception:
            pass

        Lib.control.channels_on[g].remove(chn)
        if Lib.control.channels_on[g] == []:
            Lib.control.GAVETAS_ON.remove(g)
            Lib.vars.file[g].close()

        getattr(self.ui, 'O_nome' + str(chn + 1) + '_' + str(g + 1)).setText('')
        getattr(self.ui, 'O_t0' + str(chn + 1) + '_' + str(g + 1)).setText('')
        getattr(self.ui, 'O_r0' + str(chn + 1) + '_' + str(g + 1)).setText('')
        getattr(self.ui, 'O_i' + str(chn + 1) + '_' + str(g + 1)).setText('')
        getattr(self.ui, 'O_v' + str(chn + 1) + '_' + str(g + 1)).setText('')
        getattr(self.ui, 'O_p' + str(chn + 1) + '_' + str(g + 1)).setText('')
        getattr(self.ui, 'O_temp' + str(chn + 1) + '_' + str(g + 1)).setText('')
        getattr(self.ui, 'O_fita' + str(chn + 1) + '_' + str(g + 1)).setText('')
        getattr(self.ui, 'O_pt100' + str(chn + 1) + '_' + str(g + 1)).setText('')
        getattr(self.ui, 'lineed_G' + str(g + 1) + 'S' + str(chn + 1)).setText('')

    def reset(self, group):
        Lib.vars.secs[group] = 0
        Lib.vars.mins[group] = 0
        Lib.vars.hours[group] = 0
        Lib.config.taxa[group] = []
        Lib.config.patamar[group] = []
        Lib.control.plot_group_grps[group][group] = False

        try:
            self.leg_grp[group].removeItem(Lib.graph.exp_grp[group][group].name())
            Lib.graph.exp_grp[group][group] = None
        except Exception:
            pass
        getattr(self.ui, 'graphic_group_' + str(group + 1)).plotItem.curves.clear()
        getattr(self.ui, 'graphic_group_' + str(group + 1)).clear()

        for g in Lib.control.group[group]:
            Lib.control.plot_group_gvts[g][group] = False
            Lib.control.holded_channels[g] = []
            getattr(self.ui, 'O_lineed_time' + str(group + 1) + '_' + str(g + 1)).setText('')

            try:
                self.leg_gvt[g].removeItem(Lib.graph.exp_gvt[g][group].name())
                Lib.graph.exp_gvt[g][group] = None
            except Exception:
                pass
            getattr(self.ui, 'graphic_gaveta_' + str(g + 1)).plotItem.curves.clear()
            getattr(self.ui, 'graphic_gaveta_' + str(g + 1)).clear()

            for chn in Lib.control.group[group][g]:
                Lib.measurements['Temperatura'][g][chn] = np.array([])
                Lib.measurements['Potência'][g][chn] = np.array([])
                Lib.measurements['Corrente'][g][chn] = np.array([])
                Lib.measurements['Tensão'][g][chn] = np.array([])
                Lib.measurements['Tempo'][g][chn] = np.array([])

                Lib.vars.start_time[g][chn] = None
                Lib.vars.hold_start[g][chn] = None
                Lib.vars.time_now[g][chn] = 0
                Lib.vars.total_time[g][chn] = None

                Lib.config.temp[g][chn] = []
                Lib.config.times[g][chn] = []

    def calculate_send_points(self, chn, g, group):
        d_temp = np.array([])
        temp = np.array(Lib.config.temp[g][chn][0:][::2])

        for i in range(len(temp)):
            if not(i == 0):
                d_temp = np.append(d_temp, abs((temp[i] - temp[i - 1])))

        taxa = np.array(Lib.config.taxa[group])
        t_temp_variando = np.divide(d_temp, taxa)
        t_temp_variando = list(t_temp_variando)

        for i, j in zip(t_temp_variando, Lib.config.patamar[group]):
            Lib.config.times[g][chn].append(i * 60)
            Lib.config.times[g][chn].append(j * 60)
        Lib.config.times[g][chn].insert(0, 0)

        for i in range(len(Lib.config.times[g][chn])):
            if not(i == 0):
                Lib.config.times[g][chn][i] += Lib.config.times[g][chn][i - 1]

        for i, j in zip(Lib.config.times[g][chn], Lib.config.temp[g][chn]):
            Lib.vars.interpolation_points[g][chn].append(str(i))
            Lib.vars.interpolation_points[g][chn].append(str(j))
        Lib.vars.total_time[g][chn] = Lib.config.times[g][chn][-1]
        
        if Lib.control.plot_group_gvts[g][group]:
            pass
        else:
            self.get_expected_plot_gvts(group, g, chn)
        
        if Lib.control.plot_group_grps[group][group]:
            pass
        else:
            self.get_expected_plot_grps(group, g, chn)
            # Vitor
            self.get_expected_plot_grps(3, g, chn)
            # Vitor
        self.SOCKET_GVT[g].interpolation_points(chn, Lib.vars.interpolation_points[g][chn])

    def Worker(self):
        try:
            all_off = []

            for g in Lib.control.GAVETAS_ON:
                if Lib.control.channels_on[g] == []:
                    all_off.append(True)
                else:
                    all_off.append(False)

                aux_vect = Lib.control.channels_on[g][:]
                for chn in aux_vect:
                    index = Lib.vars.channels[g].index(chn)
                    self.refresh_interface(g, chn, index)
                    if chn not in Lib.control.holded_channels[g]:
                        if Lib.vars.total_time[g][chn] < Lib.vars.time_now[g][chn]:
                            self.turn_off(g, chn)

                    if chn in Lib.control.channels_off[g]:
                        if float(Lib.vars.temperatures[g][index]) <= 50:
                            self.turn_off(g, chn)

            if False in all_off:
                pass
            else:
                self.stop_interface()
            QtGui.QApplication.processEvents()
        except IndexError:
            pass
        except Exception:
            traceback.print_exc(file=sys.stdout)
            print(g, index)
            pass

    def refresh_interface(self, g, chn, index):
    # Operação Geral
        if self.ui.comboBox_op_geral.currentText() == 'Temperatura (°C)':
            getattr(self.ui, 'lineed_G' + str(g + 1) + 'S' + str(chn + 1)).setText(str('{:.2f}'.format(Lib.vars.temperatures[g][index])))
        elif self.ui.comboBox_op_geral.currentText() == 'Potência (W)':
            getattr(self.ui, 'lineed_G' + str(g + 1) + 'S' + str(chn + 1)).setText(str('{:.2f}'.format(Lib.vars.powers[g][index])))
        elif self.ui.comboBox_op_geral.currentText() == 'Corrente (A)':
            getattr(self.ui, 'lineed_G' + str(g + 1) + 'S' + str(chn + 1)).setText(str('{:.2f}'.format(Lib.vars.currents[g][index])))
        elif self.ui.comboBox_op_geral.currentText() == 'Tensão (V)':
            getattr(self.ui, 'lineed_G' + str(g + 1) + 'S' + str(chn + 1)).setText(str('{:.2f}'.format(Lib.vars.voltages[g][index])))

    # Visualização arcos
        '''if (g + 1) == 10:
            local = Lib.vars.name[g][chn][5]
        else:
            local = Lib.vars.name[g][chn][4]
        if local == 'J':
            pass
            #for i in range(n_jaquetas):
                #if Lib.vars.name[g][chn] == getattr(self.ui, 'comboBox_jaq' + str(i + 1)).currentText():
                    #getattr(self.ui, 'lineed_jaq' + str(i + 1)).setText(str('{:.2f}'.format(Lib.vars.temperatures[g][index])))
        elif local == 'Q':
            for i in range(n_quads):
                if Lib.vars.name[g][chn] == getattr(self.ui, 'comboBox_quad' + str(i + 1)).currentText():
                    getattr(self.ui, 'lineed_quad' + str(i + 1)).setText(str('{:.2f}'.format(Lib.vars.temperatures[g][index])))
        elif local == 'D':
            for i in range(n_dips):
                if Lib.vars.name[g][chn] == getattr(self.ui, 'comboBox_dip' + str(i + 1)).currentText():
                    getattr(self.ui, 'lineed_dip' + str(i + 1)).setText(str('{:.2f}'.format(Lib.vars.temperatures[g][index])))
        elif local == 'V':
            for i in range(n_vazios):
                if Lib.vars.name[g][chn] == getattr(self.ui, 'comboBox_vazio' + str(i + 1)).currentText():
                    getattr(self.ui, 'lineed_vazio' + str(i + 1)).setText(str('{:.2f}'.format(Lib.vars.temperatures[g][index])))
        elif local == 'S':
            for i in range(n_sexts):
                if Lib.vars.name[g][chn] == getattr(self.ui, 'comboBox_sext' + str(i + 1)).currentText():
                    getattr(self.ui, 'lineed_sext' + str(i + 1)).setText(str('{:.2f}'.format(Lib.vars.temperatures[g][index])))'''

    # Operação por Gaveta
        getattr(self.ui, 'O_t0' + str(chn + 1) + '_' + str(g + 1)).setText(str('{:.2f}'.format(Lib.vars.t0[g][index])))
        getattr(self.ui, 'O_r0' + str(chn + 1) + '_' + str(g + 1)).setText(str('{:.2f}'.format(Lib.vars.r0[g][index])))
        getattr(self.ui, 'O_i' + str(chn + 1) + '_' + str(g + 1)).setText(str('{:.2f}'.format(Lib.vars.currents[g][index])))
        getattr(self.ui, 'O_v' + str(chn + 1) + '_' + str(g + 1)).setText(str('{:.2f}'.format(Lib.vars.voltages[g][index])))
        getattr(self.ui, 'O_p' + str(chn + 1) + '_' + str(g + 1)).setText(str('{:.2f}'.format(Lib.vars.powers[g][index])))
        getattr(self.ui, 'O_temp' + str(chn + 1) + '_' + str(g + 1)).setText(str('{:.2f}'.format(Lib.vars.temperatures[g][index])))
        getattr(self.ui, 'O_fita' + str(chn + 1) + '_' + str(g + 1)).setText(str('{:.2f}'.format(Lib.vars.temp_res[g][index])))
        getattr(self.ui, 'O_pt100' + str(chn + 1) + '_' + str(g + 1)).setText(str('{:.2f}'.format(Lib.vars.temp_pt100[g][index])))

    # Gráfico Gaveta
        if getattr(self.ui, 'checkBox_saida' + str(chn + 1) + '_' + str(g + 1)).isChecked():
            Lib.graph.curves_gvt[g][g][chn].setData(Lib.measurements['Tempo'][g][chn], Lib.measurements[getattr(self.ui, 'comboBox_live_' + str(g + 1)).currentText()][g][chn])
        else:
            Lib.graph.curves_gvt[g][g][chn].setData([], [])

    # Gráfico Grupo 1
        if getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_1').isChecked() and g in Lib.control.group[0] and chn in Lib.control.group[0][g]:
            Lib.graph.curves_grp[0][g][chn].setData(Lib.measurements['Tempo'][g][chn], Lib.measurements[self.ui.comboBox_live2_1.currentText()][g][chn])
        else:
            Lib.graph.curves_grp[0][g][chn].setData([], [])
    
    # Gráfico Grupo 2
        if getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_2').isChecked() and g in Lib.control.group[1] and chn in Lib.control.group[1][g]:
            Lib.graph.curves_grp[1][g][chn].setData(Lib.measurements['Tempo'][g][chn], Lib.measurements[self.ui.comboBox_live2_2.currentText()][g][chn])
        else:
            Lib.graph.curves_grp[1][g][chn].setData([], [])
    
    # Gráfico Grupo 3
        if getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_3').isChecked() and g in Lib.control.group[2] and chn in Lib.control.group[2][g]:
            Lib.graph.curves_grp[2][g][chn].setData(Lib.measurements['Tempo'][g][chn], Lib.measurements[self.ui.comboBox_live2_3.currentText()][g][chn])
        else:
            Lib.graph.curves_grp[2][g][chn].setData([], [])

    # Gráfico Todos Grupos
        # Vitor
        if getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_4').isChecked() and chn in Lib.control.channels_on[g]:
            Lib.graph.curves_grp[3][g][chn].setData(Lib.measurements['Tempo'][g][chn], Lib.measurements[self.ui.comboBox_live2_4.currentText()][g][chn])
        else:
            Lib.graph.curves_grp[3][g][chn].setData([], [])
        if getattr(self.ui, 'checkBox_gvt' + str(g + 1) + '_4').isChecked() and chn in Lib.control.channels_on[g]:
            Lib.graph.curves_grp[3][g][chn].setData(Lib.measurements['Tempo'][g][chn], Lib.measurements[self.ui.comboBox_live2_4.currentText()][g][chn])
        else:
            Lib.graph.curves_grp[3][g][chn].setData([], [])
        # Vitor

    def get_expected_plot_gvts(self, group, g, chn):
        try:
            if chn in Lib.control.group[0][g]:
                i = 0
            elif chn in Lib.control.group[1][g]:
                i = 1
            elif chn in Lib.control.group[2][g]:
                i = 2
            else:
                return
            if len(self.leg_gvt[g].items) == 1:
                if i == int(self.leg_gvt[g].items[0][1].text[1]) - 1:
                    return
            elif len(self.leg_gvt[g].items) == 2:
                if i == int(self.leg_gvt[g].items[1][1].text[1]) - 1:
                    return
            
            Lib.graph.exp_gvt[g][group] = getattr(self.ui, 'graphic_gaveta_' + str(g + 1)).plotItem.plot(name='G' + str(group + 1))
            Lib.graph.exp_gvt[g][group].setData(Lib.config.times[g][chn], Lib.config.temp[g][chn])
            Lib.graph.exp_gvt[g][group].setPen(Lib.graph.pen_esp[group], width=2)
            self.leg_gvt[g].addItem(Lib.graph.exp_gvt[g][group], 'G' + str(group + 1))
            Lib.control.plot_group_gvts[g][group] = True
        except Exception:
            traceback.print_exc(file=sys.stdout)
            Lib.graph.exp_gvt[g][group].setData([], [])
            self.leg_gvt[g].removeItem(Lib.graph.exp_gvt[g][group].name())
            Lib.graph.exp_gvt[g][group] = None

    def refresh_axis_live_gvts(self, g):
        var = getattr(self.ui, 'comboBox_live_' + str(g + 1)).currentText()
        getattr(self.ui, 'graphic_gaveta_' + str(g + 1)).setLabel('left', text=var, units=Lib.graph.unit[var])
        for group in Lib.control.group:
            for chn in Lib.control.group[group][g]:
                if var == 'Temperatura':
                    if Lib.control.plot_group_gvts[g][group]:
                        pass
                    else:
                        self.get_expected_plot_gvts(group, g, chn)
                else:
                    if Lib.control.plot_group_gvts[g][group]:
                        Lib.graph.exp_gvt[g][group].setData([], [])
                        self.leg_gvt[g].removeItem(Lib.graph.exp_gvt[g][group].name())
                        Lib.control.plot_group_gvts[g][group] = False

    def get_expected_plot_grps(self, group, g, chn):
        try:
            # Vitor
            if group < 3:
                Lib.graph.exp_grp[group][group] = getattr(self.ui, 'graphic_group_' + str(group + 1)).plotItem.plot(name='G' + str(group + 1))
                Lib.graph.exp_grp[group][group].setData(Lib.config.times[g][chn], Lib.config.temp[g][chn])
                Lib.graph.exp_grp[group][group].setPen(Lib.graph.pen_esp[group], width=2)
                self.leg_grp[group].addItem(Lib.graph.exp_grp[group][group], 'G' + str(group + 1))
                Lib.control.plot_group_grps[group][group] = True
            else:
                if len(self.leg_grp[group].items) > 2:
                    return
                if chn in Lib.control.group[0][g]:
                    i = 0
                elif chn in Lib.control.group[1][g]:
                    i = 1
                elif chn in Lib.control.group[2][g]:
                    i = 2
                else:
                    return
                if len(self.leg_grp[group].items) == 1:
                    if i == int(self.leg_grp[group].items[0][1].text[1]) - 1:
                        return
                elif len(self.leg_grp[group].items) == 2:
                    if i == int(self.leg_grp[group].items[1][1].text[1]) - 1:
                        return
                    Lib.control.plot_group_grps[group][group] = True
                Lib.graph.exp_grp[group][i] = getattr(self.ui, 'graphic_group_' + str(group + 1)).plotItem.plot(name='G' + str(i + 1))
                Lib.graph.exp_grp[group][i].setData(Lib.config.times[g][chn], Lib.config.temp[g][chn])
                Lib.graph.exp_grp[group][i].setPen(Lib.graph.pen_esp[i], width=2)
                self.leg_grp[group].addItem(Lib.graph.exp_grp[group][i], 'G' + str(i + 1))
        except Exception:
            traceback.print_exc(file=sys.stdout)
            Lib.graph.exp_grp[group][group].setData([], [])
            if group < 3:
                self.leg_grp[group].removeItem(Lib.graph.exp_grp[group][group].name())
                Lib.graph.exp_grp[group][group] = None
            else:
                for i in range(len(self.leg_grp[group].items)):
                    Lib.graph.exp_grp[group][i].setData([], [])
                    self.leg_grp[group].removeItem(self.leg_grp[group].items[i][1].text)
                Lib.control.plot_group_grps[group][group] = False
            # Vitor

    def refresh_axis_live_grps(self, group):
        var = getattr(self.ui, 'comboBox_live2_' + str(group + 1)).currentText()
        getattr(self.ui, 'graphic_group_' + str(group + 1)).setLabel('left', text=var, units=Lib.graph.unit[var])
        # Vitor
        if group < 3:
            _group_list = Lib.control.group[group]
        else:
            _group_list = Lib.control.channels_on
        for g in _group_list:
            for chn in _group_list[g]:
                if var == 'Temperatura':
                    if Lib.control.plot_group_grps[group][group]:
                        pass
                    else:
                        self.get_expected_plot_grps(group, g, chn)
                else:
                    if Lib.control.plot_group_grps[group][group]:
                        if group < 3:
                            Lib.graph.exp_grp[group][group].setData([], [])
                            self.leg_grp[group].removeItem(Lib.graph.exp_grp[group][group].name())
                            Lib.control.plot_group_grps[group][group] = False
                        else:
                            _remove_list = []
                            for i in range(len(self.leg_grp[group].items)):
                                Lib.graph.exp_grp[group][i].setData([], [])
                                _remove_list.append(self.leg_grp[group].items[i][1].text)
                            for item in _remove_list:
                                self.leg_grp[group].removeItem(item)
                            Lib.control.plot_group_grps[group][group] = False
        # Vitor

    def open_file(self, g):
        try:
            tmp = time.localtime()
            date = '{0:1d}-{1:1d}-{2:1d}'.format(tmp.tm_mday, tmp.tm_mon, tmp.tm_year)
            hour = '{0:1d}h{1:1d}m{2:1d}s'.format(tmp.tm_hour, tmp.tm_min, tmp.tm_sec)
            file_name = 'Gaveta' + str(g + 1) + '_' + date + '_' + hour + '.dat'
            file = open(file_name, 'w')
            for chn in Lib.vars.channels[g]:
                index = Lib.vars.channels[g].index(chn)
                file.writelines('Saida ' + str(chn + 1) + '\n')
                file.writelines('Nome: ' + Lib.vars.name[g][chn] + '\n')
                file.writelines('Temperatura Inicial (C): ' + str(Lib.vars.t0[g][index]) + '\n')
                file.writelines('Resistencia Inicial (Ohms): ' + str(Lib.vars.r0[g][index]) + '\n\n')
            file.write('\n\n\n')

            file.writelines('DateTime\tTemp1(C)\tTemp2(C)\tTemp3(C)\tTemp4(C)\tTemp5(C)\tTemp6(C)\tTemp7(C)\tTemp8(C)\tTemp Fita1(C)\tTemp Fita2(C)\tTemp Fita3(C)\tTemp Fita4(C)\tTemp Fita5(C)\tTemp Fita6(C)\tTemp Fita7(C)\tTemp Fita8(C)\tTemp Pt100 1(C)\tTemp Pt100 2(C)\tTemp Pt100 3(C)\tTemp Pt100 4(C)\tTemp Pt100 5(C)\tTemp Pt100 6(C)\tTemp Pt100 7(C)\tTemp Pt100 8(C)\tCorrente1(A)\tCorrente2(A)\tCorrente3(A)\tCorrente4(A)\tCorrente5(A)\tCorrente6(A)\tCorrente7(A)\tCorrente8(A)\tVoltagem1(V)\tVoltagem2(V)\tVoltagem3(V)\tVoltagem4(V)\tVoltagem5(V)\tVoltagem6(V)\tVoltagem7(V)\tVoltagem8(V)\tPotencia1(W)\tPotencia2(W)\tPotencia3(W)\tPotencia4(W)\tPotencia5(W)\tPotencia6(W)\tPotencia7(W)\tPotencia8(W)\n')
            return file
        except Exception:
            traceback.print_exc(file=sys.stdout)
            return None

    def init_timers(self):
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.Worker)
        self.timer = [QTimer(), QTimer(), QTimer()]
        self.timer[0].timeout.connect(lambda: self.clock(0))
        self.timer[1].timeout.connect(lambda: self.clock(1))
        self.timer[2].timeout.connect(lambda: self.clock(2))

    def clock(self, group):
        Lib.vars.secs[group] += 1
        if Lib.vars.secs[group] % 60 == 0:
            Lib.vars.mins[group] += 1
            Lib.vars.secs[group] = 0
            if Lib.vars.mins[group] % 60 == 0:
                Lib.vars.hours[group] += 1
                Lib.vars.mins[group] = 0
        getattr(self.ui, 'lineed_time' + str(group + 1)).setText('{:02d}'.format(Lib.vars.hours[group]) + ':' + '{:02d}'.format(Lib.vars.mins[group]) + ':' + '{:02d}'.format(Lib.vars.secs[group]))
        for g in Lib.control.GAVETAS:
            getattr(self.ui, 'O_lineed_time' + str(group + 1) + '_' + str(g + 1)).setText('{:02d}'.format(Lib.vars.hours[group]) + ':' + '{:02d}'.format(Lib.vars.mins[group]) + ':' + '{:02d}'.format(Lib.vars.secs[group]))


Lib = Library.Lib()

class Main(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        #self.setDaemon(True)
        self.start()

    def run(self):
        self.app = QtGui.QApplication(sys.argv)
        self.myapp = MainWindow()
        self.myapp.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    # Vitor
    # main()
    app = Main()
    # Vitor
