import time
import pdb, sys
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import uic


class Ui(qtw.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("C:\\Users\\M\\Desktop\\sudoku.ui", self)
        self.setFixedSize(700, 700)
        if True:
            self.button_1_1 = self.findChild(qtw.QPushButton, "pushButton_1_1")
            self.button_1_2 = self.findChild(qtw.QPushButton, "pushButton_1_2")
            self.button_1_3 = self.findChild(qtw.QPushButton, "pushButton_1_3")
            self.button_1_4 = self.findChild(qtw.QPushButton, "pushButton_1_4")
            self.button_1_5 = self.findChild(qtw.QPushButton, "pushButton_1_5")
            self.button_1_6 = self.findChild(qtw.QPushButton, "pushButton_1_6")
            self.button_1_7 = self.findChild(qtw.QPushButton, "pushButton_1_7")
            self.button_1_8 = self.findChild(qtw.QPushButton, "pushButton_1_8")
            self.button_1_9 = self.findChild(qtw.QPushButton, "pushButton_1_9")
            self.button_2_1 = self.findChild(qtw.QPushButton, "pushButton_2_1")
            self.button_2_2 = self.findChild(qtw.QPushButton, "pushButton_2_2")
            self.button_2_3 = self.findChild(qtw.QPushButton, "pushButton_2_3")
            self.button_2_4 = self.findChild(qtw.QPushButton, "pushButton_2_4")
            self.button_2_5 = self.findChild(qtw.QPushButton, "pushButton_2_5")
            self.button_2_6 = self.findChild(qtw.QPushButton, "pushButton_2_6")
            self.button_2_7 = self.findChild(qtw.QPushButton, "pushButton_2_7")
            self.button_2_8 = self.findChild(qtw.QPushButton, "pushButton_2_8")
            self.button_2_9 = self.findChild(qtw.QPushButton, "pushButton_2_9")
            self.button_3_1 = self.findChild(qtw.QPushButton, "pushButton_3_1")
            self.button_3_2 = self.findChild(qtw.QPushButton, "pushButton_3_2")
            self.button_3_3 = self.findChild(qtw.QPushButton, "pushButton_3_3")
            self.button_3_4 = self.findChild(qtw.QPushButton, "pushButton_3_4")
            self.button_3_5 = self.findChild(qtw.QPushButton, "pushButton_3_5")
            self.button_3_6 = self.findChild(qtw.QPushButton, "pushButton_3_6")
            self.button_3_7 = self.findChild(qtw.QPushButton, "pushButton_3_7")
            self.button_3_8 = self.findChild(qtw.QPushButton, "pushButton_3_8")
            self.button_3_9 = self.findChild(qtw.QPushButton, "pushButton_3_9")
            self.button_4_1 = self.findChild(qtw.QPushButton, "pushButton_4_1")
            self.button_4_2 = self.findChild(qtw.QPushButton, "pushButton_4_2")
            self.button_4_3 = self.findChild(qtw.QPushButton, "pushButton_4_3")
            self.button_4_4 = self.findChild(qtw.QPushButton, "pushButton_4_4")
            self.button_4_5 = self.findChild(qtw.QPushButton, "pushButton_4_5")
            self.button_4_6 = self.findChild(qtw.QPushButton, "pushButton_4_6")
            self.button_4_7 = self.findChild(qtw.QPushButton, "pushButton_4_7")
            self.button_4_8 = self.findChild(qtw.QPushButton, "pushButton_4_8")
            self.button_4_9 = self.findChild(qtw.QPushButton, "pushButton_4_9")
            self.button_5_1 = self.findChild(qtw.QPushButton, "pushButton_5_1")
            self.button_5_2 = self.findChild(qtw.QPushButton, "pushButton_5_2")
            self.button_5_3 = self.findChild(qtw.QPushButton, "pushButton_5_3")
            self.button_5_4 = self.findChild(qtw.QPushButton, "pushButton_5_4")
            self.button_5_5 = self.findChild(qtw.QPushButton, "pushButton_5_5")
            self.button_5_6 = self.findChild(qtw.QPushButton, "pushButton_5_6")
            self.button_5_7 = self.findChild(qtw.QPushButton, "pushButton_5_7")
            self.button_5_8 = self.findChild(qtw.QPushButton, "pushButton_5_8")
            self.button_5_9 = self.findChild(qtw.QPushButton, "pushButton_5_9")
            self.button_6_1 = self.findChild(qtw.QPushButton, "pushButton_6_1")
            self.button_6_2 = self.findChild(qtw.QPushButton, "pushButton_6_2")
            self.button_6_3 = self.findChild(qtw.QPushButton, "pushButton_6_3")
            self.button_6_4 = self.findChild(qtw.QPushButton, "pushButton_6_4")
            self.button_6_5 = self.findChild(qtw.QPushButton, "pushButton_6_5")
            self.button_6_6 = self.findChild(qtw.QPushButton, "pushButton_6_6")
            self.button_6_7 = self.findChild(qtw.QPushButton, "pushButton_6_7")
            self.button_6_8 = self.findChild(qtw.QPushButton, "pushButton_6_8")
            self.button_6_9 = self.findChild(qtw.QPushButton, "pushButton_6_9")
            self.button_7_1 = self.findChild(qtw.QPushButton, "pushButton_7_1")
            self.button_7_2 = self.findChild(qtw.QPushButton, "pushButton_7_2")
            self.button_7_3 = self.findChild(qtw.QPushButton, "pushButton_7_3")
            self.button_7_4 = self.findChild(qtw.QPushButton, "pushButton_7_4")
            self.button_7_5 = self.findChild(qtw.QPushButton, "pushButton_7_5")
            self.button_7_6 = self.findChild(qtw.QPushButton, "pushButton_7_6")
            self.button_7_7 = self.findChild(qtw.QPushButton, "pushButton_7_7")
            self.button_7_8 = self.findChild(qtw.QPushButton, "pushButton_7_8")
            self.button_7_9 = self.findChild(qtw.QPushButton, "pushButton_7_9")
            self.button_8_1 = self.findChild(qtw.QPushButton, "pushButton_8_1")
            self.button_8_2 = self.findChild(qtw.QPushButton, "pushButton_8_2")
            self.button_8_3 = self.findChild(qtw.QPushButton, "pushButton_8_3")
            self.button_8_4 = self.findChild(qtw.QPushButton, "pushButton_8_4")
            self.button_8_5 = self.findChild(qtw.QPushButton, "pushButton_8_5")
            self.button_8_6 = self.findChild(qtw.QPushButton, "pushButton_8_6")
            self.button_8_7 = self.findChild(qtw.QPushButton, "pushButton_8_7")
            self.button_8_8 = self.findChild(qtw.QPushButton, "pushButton_8_8")
            self.button_8_9 = self.findChild(qtw.QPushButton, "pushButton_8_9")
            self.button_9_1 = self.findChild(qtw.QPushButton, "pushButton_9_1")
            self.button_9_2 = self.findChild(qtw.QPushButton, "pushButton_9_2")
            self.button_9_3 = self.findChild(qtw.QPushButton, "pushButton_9_3")
            self.button_9_4 = self.findChild(qtw.QPushButton, "pushButton_9_4")
            self.button_9_5 = self.findChild(qtw.QPushButton, "pushButton_9_5")
            self.button_9_6 = self.findChild(qtw.QPushButton, "pushButton_9_6")
            self.button_9_7 = self.findChild(qtw.QPushButton, "pushButton_9_7")
            self.button_9_8 = self.findChild(qtw.QPushButton, "pushButton_9_8")
            self.button_9_9 = self.findChild(qtw.QPushButton, "pushButton_9_9")
        self.reset_button = self.findChild(qtw.QPushButton, 'pushButton_2')
        self.reset_button.clicked.connect(self.reset)
        self.solve_button = self.findChild(qtw.QPushButton, 'pushButton')
        self.solve_button.clicked.connect(self.solve)
        self.file_menu = self.findChild(qtw.QMenu, "menuFiles")
        self.about_menu = self.findChild(qtw.QMenu, "menuAbout")
        self.about_menu.addAction("Rules", self.rules)
        self.about_menu.addAction("About", self.about)
        self.file_menu.addAction("Open", self.open)
        self.file_menu.addAction("Save", self.save)
        self.list_all = [self.button_1_1, self.button_1_2, self.button_1_3, self.button_1_4, self.button_1_5,
                         self.button_1_6, self.button_1_7, self.button_1_8, self.button_1_9
            , self.button_2_1, self.button_2_2, self.button_2_3, self.button_2_4, self.button_2_5, self.button_2_6,
                         self.button_2_7, self.button_2_8, self.button_2_9,
                         self.button_3_1, self.button_3_2, self.button_3_3, self.button_3_4, self.button_3_5,
                         self.button_3_6, self.button_3_7, self.button_3_8, self.button_3_9
            , self.button_4_1, self.button_4_2, self.button_4_3, self.button_4_4, self.button_4_5, self.button_4_6,
                         self.button_4_7, self.button_4_8, self.button_4_9
            , self.button_5_1, self.button_5_2, self.button_5_3, self.button_5_4, self.button_5_5, self.button_5_6,
                         self.button_5_7, self.button_5_8, self.button_5_9
            , self.button_6_1, self.button_6_2, self.button_6_3, self.button_6_4, self.button_6_5, self.button_6_6,
                         self.button_6_7, self.button_6_8, self.button_6_9
            , self.button_7_1, self.button_7_2, self.button_7_3, self.button_7_4, self.button_7_5, self.button_7_6,
                         self.button_7_7, self.button_7_8, self.button_7_9
            , self.button_8_1, self.button_8_2, self.button_8_3, self.button_8_4, self.button_8_5, self.button_8_6,
                         self.button_8_7, self.button_8_8, self.button_8_9
            , self.button_9_1, self.button_9_2, self.button_9_3, self.button_9_4, self.button_9_5, self.button_9_6,
                         self.button_9_7, self.button_9_8, self.button_9_9]
        self.list_prefill = []
        self.list_main = []
        # Dict
        self.dict_all = {self.button_1_1: {"row": 1, "column": 1, "grid": 1},
                         self.button_1_2: {"row": 1, "column": 2, "grid": 1},
                         self.button_1_3: {"row": 1, "column": 3, "grid": 1},
                         self.button_1_4: {"row": 2, "column": 1, "grid": 1},
                         self.button_1_5: {"row": 2, "column": 2, "grid": 1},
                         self.button_1_6: {"row": 2, "column": 3, "grid": 1},
                         self.button_1_7: {"row": 3, "column": 1, "grid": 1},
                         self.button_1_8: {"row": 3, "column": 2, "grid": 1},
                         self.button_1_9: {"row": 3, "column": 3, "grid": 1},
                         self.button_2_1: {"row": 1, "column": 4, "grid": 2},
                         self.button_2_2: {"row": 1, "column": 5, "grid": 2},
                         self.button_2_3: {"row": 1, "column": 6, "grid": 2},
                         self.button_2_4: {"row": 2, "column": 4, "grid": 2},
                         self.button_2_5: {"row": 2, "column": 5, "grid": 2},
                         self.button_2_6: {"row": 2, "column": 6, "grid": 2},
                         self.button_2_7: {"row": 3, "column": 4, "grid": 2},
                         self.button_2_8: {"row": 3, "column": 5, "grid": 2},
                         self.button_2_9: {"row": 3, "column": 6, "grid": 2},
                         self.button_3_1: {"row": 1, "column": 7, "grid": 3},
                         self.button_3_2: {"row": 1, "column": 8, "grid": 3},
                         self.button_3_3: {"row": 1, "column": 9, "grid": 3},
                         self.button_3_4: {"row": 2, "column": 7, "grid": 3},
                         self.button_3_5: {"row": 2, "column": 8, "grid": 3},
                         self.button_3_6: {"row": 2, "column": 9, "grid": 3},
                         self.button_3_7: {"row": 3, "column": 7, "grid": 3},
                         self.button_3_8: {"row": 3, "column": 8, "grid": 3},
                         self.button_3_9: {"row": 3, "column": 9, "grid": 3},
                         self.button_4_1: {"row": 4, "column": 1, "grid": 4},
                         self.button_4_2: {"row": 4, "column": 2, "grid": 4},
                         self.button_4_3: {"row": 4, "column": 3, "grid": 4},
                         self.button_4_4: {"row": 5, "column": 1, "grid": 4},
                         self.button_4_5: {"row": 5, "column": 2, "grid": 4},
                         self.button_4_6: {"row": 5, "column": 3, "grid": 4},
                         self.button_4_7: {"row": 6, "column": 1, "grid": 4},
                         self.button_4_8: {"row": 6, "column": 2, "grid": 4},
                         self.button_4_9: {"row": 6, "column": 3, "grid": 4},
                         self.button_5_1: {"row": 4, "column": 4, "grid": 5},
                         self.button_5_2: {"row": 4, "column": 5, "grid": 5},
                         self.button_5_3: {"row": 4, "column": 6, "grid": 5},
                         self.button_5_4: {"row": 5, "column": 4, "grid": 5},
                         self.button_5_5: {"row": 5, "column": 5, "grid": 5},
                         self.button_5_6: {"row": 5, "column": 6, "grid": 5},
                         self.button_5_7: {"row": 6, "column": 4, "grid": 5},
                         self.button_5_8: {"row": 6, "column": 5, "grid": 5},
                         self.button_5_9: {"row": 6, "column": 6, "grid": 5},
                         self.button_6_1: {"row": 4, "column": 7, "grid": 6},
                         self.button_6_2: {"row": 4, "column": 8, "grid": 6},
                         self.button_6_3: {"row": 4, "column": 9, "grid": 6},
                         self.button_6_4: {"row": 5, "column": 7, "grid": 6},
                         self.button_6_5: {"row": 5, "column": 8, "grid": 6},
                         self.button_6_6: {"row": 5, "column": 9, "grid": 6},
                         self.button_6_7: {"row": 6, "column": 7, "grid": 6},
                         self.button_6_8: {"row": 6, "column": 8, "grid": 6},
                         self.button_6_9: {"row": 6, "column": 9, "grid": 6},
                         self.button_7_1: {"row": 7, "column": 1, "grid": 7},
                         self.button_7_2: {"row": 7, "column": 2, "grid": 7},
                         self.button_7_3: {"row": 7, "column": 3, "grid": 7},
                         self.button_7_4: {"row": 8, "column": 1, "grid": 7},
                         self.button_7_5: {"row": 8, "column": 2, "grid": 7},
                         self.button_7_6: {"row": 8, "column": 3, "grid": 7},
                         self.button_7_7: {"row": 9, "column": 1, "grid": 7},
                         self.button_7_8: {"row": 9, "column": 2, "grid": 7},
                         self.button_7_9: {"row": 9, "column": 3, "grid": 7},
                         self.button_8_1: {"row": 7, "column": 4, "grid": 8},
                         self.button_8_2: {"row": 7, "column": 5, "grid": 8},
                         self.button_8_3: {"row": 7, "column": 6, "grid": 8},
                         self.button_8_4: {"row": 8, "column": 4, "grid": 8},
                         self.button_8_5: {"row": 8, "column": 5, "grid": 8},
                         self.button_8_6: {"row": 8, "column": 6, "grid": 8},
                         self.button_8_7: {"row": 9, "column": 4, "grid": 8},
                         self.button_8_8: {"row": 9, "column": 5, "grid": 8},
                         self.button_8_9: {"row": 9, "column": 6, "grid": 8},
                         self.button_9_1: {"row": 7, "column": 7, "grid": 9},
                         self.button_9_2: {"row": 7, "column": 8, "grid": 9},
                         self.button_9_3: {"row": 7, "column": 9, "grid": 9},
                         self.button_9_4: {"row": 8, "column": 7, "grid": 9},
                         self.button_9_5: {"row": 8, "column": 8, "grid": 9},
                         self.button_9_6: {"row": 8, "column": 9, "grid": 3},
                         self.button_9_7: {"row": 9, "column": 7, "grid": 9},
                         self.button_9_8: {"row": 9, "column": 8, "grid": 9},
                         self.button_9_9: {"row": 9, "column": 9, "grid": 9}}
        if True:
            self.list_row_1 = [self.button_1_1, self.button_1_2, self.button_1_3, self.button_2_1, self.button_2_2,
                               self.button_2_3, self.button_3_1, self.button_3_2, self.button_3_3]
            self.list_row_2 = [self.button_1_4, self.button_1_5, self.button_1_6, self.button_2_4, self.button_2_5,
                               self.button_2_6, self.button_3_4, self.button_3_5, self.button_3_6]
            self.list_row_3 = [self.button_1_7, self.button_1_8, self.button_1_9, self.button_2_7, self.button_2_8,
                               self.button_2_9, self.button_3_7, self.button_3_8, self.button_3_9]
            self.list_row_4 = [self.button_4_1, self.button_4_2, self.button_4_3, self.button_5_1, self.button_5_2,
                               self.button_5_3, self.button_6_1, self.button_6_2, self.button_6_3]
            self.list_row_5 = [self.button_4_4, self.button_4_5, self.button_4_6, self.button_5_4, self.button_5_5,
                               self.button_5_6, self.button_6_4, self.button_6_5, self.button_6_6]
            self.list_row_6 = [self.button_4_7, self.button_4_8, self.button_4_9, self.button_5_7, self.button_5_8,
                               self.button_5_9, self.button_6_7, self.button_6_8, self.button_6_9]
            self.list_row_7 = [self.button_7_1, self.button_7_2, self.button_7_3, self.button_8_1, self.button_8_2,
                               self.button_8_3, self.button_9_1, self.button_9_2, self.button_9_3]
            self.list_row_8 = [self.button_7_4, self.button_7_5, self.button_7_6, self.button_8_4, self.button_8_5,
                               self.button_8_6, self.button_9_4, self.button_9_5, self.button_9_6]
            self.list_row_9 = [self.button_7_7, self.button_7_8, self.button_7_9, self.button_8_7, self.button_8_8,
                               self.button_8_9, self.button_9_7, self.button_9_8, self.button_9_9]
            self.list_column_1 = [self.button_1_1, self.button_1_4, self.button_1_7, self.button_4_1, self.button_4_4,
                                  self.button_4_7, self.button_7_1, self.button_7_4, self.button_7_7]
            self.list_column_2 = [self.button_1_2, self.button_1_5, self.button_1_8, self.button_4_2, self.button_4_5,
                                  self.button_4_8, self.button_7_2, self.button_7_5, self.button_7_8]
            self.list_column_3 = [self.button_1_3, self.button_1_6, self.button_1_9, self.button_4_3, self.button_4_6,
                                  self.button_4_9, self.button_7_3, self.button_7_6, self.button_7_9]
            self.list_column_4 = [self.button_2_1, self.button_2_4, self.button_2_7, self.button_5_1, self.button_5_4,
                                  self.button_5_7, self.button_8_1, self.button_8_4, self.button_8_7]
            self.list_column_5 = [self.button_2_2, self.button_2_5, self.button_2_8, self.button_5_2, self.button_5_5,
                                  self.button_5_8, self.button_8_2, self.button_8_5, self.button_8_8]
            self.list_column_6 = [self.button_2_3, self.button_2_6, self.button_2_9, self.button_5_3, self.button_5_6,
                                  self.button_5_9, self.button_8_3, self.button_8_6, self.button_8_9]
            self.list_column_7 = [self.button_3_1, self.button_3_4, self.button_3_7, self.button_6_1, self.button_6_4,
                                  self.button_6_7, self.button_9_1, self.button_9_4, self.button_9_7]
            self.list_column_8 = [self.button_3_2, self.button_3_5, self.button_3_8, self.button_6_2, self.button_6_5,
                                  self.button_6_8, self.button_9_2, self.button_9_5, self.button_9_8]
            self.list_column_9 = [self.button_3_3, self.button_3_6, self.button_3_9, self.button_6_3, self.button_6_6,
                                  self.button_6_9, self.button_9_3, self.button_9_6, self.button_9_9]
            self.list_grid_1 = [self.button_1_1, self.button_1_2, self.button_1_3, self.button_1_4, self.button_1_5,
                                self.button_1_6, self.button_1_7, self.button_1_8, self.button_1_9]
            self.list_grid_2 = [self.button_2_1, self.button_2_2, self.button_2_3, self.button_2_4, self.button_2_5,
                                self.button_2_6, self.button_2_7, self.button_2_8, self.button_2_9]
            self.list_grid_3 = [self.button_3_1, self.button_3_2, self.button_3_3, self.button_3_4, self.button_3_5,
                                self.button_3_6, self.button_3_7, self.button_3_8, self.button_3_9]
            self.list_grid_4 = [self.button_4_1, self.button_4_2, self.button_4_3, self.button_4_4, self.button_4_5,
                                self.button_4_6, self.button_4_7, self.button_4_8, self.button_4_9]
            self.list_grid_5 = [self.button_5_1, self.button_5_2, self.button_5_3, self.button_5_4, self.button_5_5,
                                self.button_5_6, self.button_5_7, self.button_5_8, self.button_5_9]
            self.list_grid_6 = [self.button_6_1, self.button_6_2, self.button_6_3, self.button_6_4, self.button_6_5,
                                self.button_6_6, self.button_6_7, self.button_6_8, self.button_6_9]
            self.list_grid_7 = [self.button_7_1, self.button_7_2, self.button_7_3, self.button_7_4, self.button_7_5,
                                self.button_7_6, self.button_7_7, self.button_7_8, self.button_7_9]
            self.list_grid_8 = [self.button_8_1, self.button_8_2, self.button_8_3, self.button_8_4, self.button_8_5,
                                self.button_8_6, self.button_8_7, self.button_8_8, self.button_8_9]
            self.list_grid_9 = [self.button_9_1, self.button_9_2, self.button_9_3, self.button_9_4, self.button_9_5,
                                self.button_9_6, self.button_9_7, self.button_9_8, self.button_9_9]
        self.list_rows = [self.list_row_1, self.list_row_2, self.list_row_3, self.list_row_4, self.list_row_5,
                          self.list_row_6, self.list_row_7, self.list_row_8, self.list_row_9]
        self.list_columns = [self.list_column_1, self.list_column_2, self.list_column_3, self.list_column_4,
                             self.list_column_5, self.list_column_6, self.list_column_7, self.list_column_8,
                             self.list_column_9]
        self.list_grids = [self.list_grid_1, self.list_grid_2, self.list_grid_3, self.list_grid_4, self.list_grid_5,
                           self.list_grid_6, self.list_grid_7, self.list_grid_8, self.list_grid_9]
        self.flag = ""
        for i in self.list_all:
            i.clicked.connect(self.change)
            i.setFont(qtg.QFont("Times", 26))
            i.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)

    def change(self):
        sender = self.sender()
        if sender.text() == "":
            sender.setText("1")
        elif int(sender.text()) != 9:
            sender.setText(str(int(sender.text()) + 1))
        else:
            sender.setText("")
        if sender not in self.list_prefill:
            self.list_prefill.append(sender)

    def prevalues(self):
        for i in self.list_main:
            self.dict_all[i]['val'] = []
            if self.condition_rules(self.dict_all[i]['row'], self.dict_all[i]['column'], self.dict_all[i]["grid"], i):
                self.dict_all[i]['val'].append(i)
            else:
                self.dict_all[i]['val'] = [1,2,3,4,5,6,7,8,9]


    def solve(self):
        if len(self.list_prefill) < 25:
            if qtw.QMessageBox.warning(self, "Warning","At least 25 Prefilled numbers required \n Otherwise program can fail \n Do You Want to Continue",qtw.QMessageBox.Yes | qtw.QMessageBox.No) == True:
                pass
            else:
                return False

        self.condition_check()
        self.list_main = list(set(self.list_all) - set(self.list_prefill))
        self.prevalues()
        start_time = time.time()
        self.solve_main()
        qtw.QMessageBox.about(self, "Sudoku", "Sudoku Solved\nTime--- %s seconds ---" % (time.time() - start_time))
        self.flag = False

    def solve_main(self):
        if len(self.list_main) == 0:
            self.flag = True

        if self.flag:
            return

        i = self.list_main[0]

        for j in self.dict_all[i]['val']:
            i.setText(str(j))
            if self.condition_rules(self.dict_all[i]['row'], self.dict_all[i]['column'], self.dict_all[i]['grid'], i):
                self.list_main.remove(i)
                self.solve_main()
                if self.flag:
                    return
                self.list_main.insert(0, i)
                i.setText("")
            else:
                i.setText("")
        else:
            return False

    def condition_check(self):
        for i in self.list_prefill:
            if self.condition_rules(self.dict_all[i]['row'], self.dict_all[i]['column'], self.dict_all[i]["grid"], i):
                continue
            else:
                self.reset()

    def condition_rules(self, r, c, g, s):
        for i in range(9):  # FOR ROWS
            if self.list_rows[r - 1][i] == s:
                continue
            elif self.list_rows[r - 1][i].text() == s.text():
                return False

        for i in range(9):  # FOR COLUMNS
            if self.list_columns[c - 1][i] == s:
                continue
            elif self.list_columns[c - 1][i].text() == s.text():
                return False

        for i in range(9):  # FOR GRIDS
            if self.list_grids[g - 1][i] == s:
                continue
            elif self.list_grids[g - 1][i].text() == s.text():
                return False

        return True

    def reset(self):
        for i in self.list_all:
            i.setText("")
        self.list_prefill = []

    def about(self):
        pass

    def rules(self):
        pass

    def open(self):
        filename, _ = qtw.QFileDialog.getOpenFileName(self, "Select File To Open", qtc.QDir.homePath(),
                                                      'Text Files (*.txt)')
        if filename:
            self.reset()
            with open(filename, 'r') as fh:
                fh = fh.read()
                fh_list = []
                count = -1
                for i in fh:
                    if i.isspace():
                        continue
                    else:
                        fh_list.append(i)
                for i in range(9):
                    for j in range(9):
                        count += 1
                        if fh_list[count] == "0":
                            continue
                        else:
                            self.list_rows[i][j].setText(fh_list[count])
                            self.list_prefill.append(self.list_rows[i][j])

    def save(self):
        save_lst = []
        for i in range(9):
            for j in range(9):
                save_lst.append(self.list_rows[i][j].text())

        for n, i in enumerate(save_lst):
            if i == "":
                save_lst[n] == "0"
        filename, _ = qtw.QFileDialog.getSaveFileName(self, "Select File To Save", qtc.QDir.homePath(),
                                                      'Text Files (*.txt)')
        if filename:
            with open(filename, 'a') as fh:
                for i in save_lst:
                    if i == "":
                        fh.write(str("0"))
                    else:
                        fh.write(str(i))


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = Ui()
    mw.show()
    sys.exit(app.exec())
