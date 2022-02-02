import sys
import time
import copy
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import uic
import os


flag = True
import numpy as np
try:
    from Solver import Solver
except ModuleNotFoundError:
    flag = False

class Ui(qtw.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        
        #Window
        self.setFixedSize(900,700)
        self.setWindowTitle("Sudoku Solve")
        
        #Checking If Model Module is imported
        if not flag:
            qtw.QMessageBox.critical(self, "Solver", "SudokuSolver.py File Not Found")
            sys.exit()
            
        #Load Uic
        try:
            uic.loadUi("layout.ui", self)
        except FileNotFoundError:
            try:
                uic.loadUi(os.path.join(sys._MEIPASS,"layout.ui"), self)
            except:
                # For PyInstaller
                qtw.QMessageBox.critical(self, "Sudoku Solver", f"{sys._MEIPASS} layout.ui File Not Found", qtw.QMessageBox.Ok)
                sys.exit()
            
        #Assigning Qpushbutton From Uic File
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
        self.solve_button = self.findChild(qtw.QPushButton, 'pushButton')
        self.file_menu = self.findChild(qtw.QMenu,"menuFiles")
        self.about_menu = self.findChild(qtw.QMenu,"menuAbout")
        
        #Button Behaviour
        self.reset_button.clicked.connect(self.reset)
        self.solve_button.clicked.connect(self.solve)
        self.file_menu.addAction("Open", self.open)
        self.file_menu.addAction("Save", self.save)
        self.about_menu.addAction("Rules",self.rules)
        self.about_menu.addAction("About",lambda : qtw.QMessageBox.information(self,"About",f"This is a software to solve Sudoku Written in Python with PyQt5 Module\nCreated By - Ajeem Ahmad \nContact Email : Ahmedazim7804@gmail.com",qtw.QMessageBox.Ok))
        
        #Dock
        self.dock = qtw.QDockWidget("Console")
        self.text_edit = qtw.QTextEdit()
        self.submit_button = qtw.QPushButton("Submit",clicked=self.submit)
        dock_widget = qtw.QWidget()
        dock_widget.setLayout(qtw.QVBoxLayout())
        gb1 = qtw.QGroupBox("Text")
        gb1.setFixedSize(qtc.QSize(300,200))
        gb2 = qtw.QGroupBox("Buttons")
        
        if True:
            self.b1 = qtw.QPushButton("1",clicked=self.change_2,enabled=False,shortcut=qtg.QKeySequence('1'))
            self.b2 = qtw.QPushButton("2",clicked=self.change_2,enabled=False,shortcut=qtg.QKeySequence('2'))
            self.b3 = qtw.QPushButton("3",clicked=self.change_2,enabled=False,shortcut=qtg.QKeySequence('3'))
            self.b4 = qtw.QPushButton("4",clicked=self.change_2,enabled=False,shortcut=qtg.QKeySequence('4'))
            self.b5 = qtw.QPushButton("5",clicked=self.change_2,enabled=False,shortcut=qtg.QKeySequence('5'))
            self.b6 = qtw.QPushButton("6",clicked=self.change_2,enabled=False,shortcut=qtg.QKeySequence('6'))
            self.b7 = qtw.QPushButton("7",clicked=self.change_2,enabled=False,shortcut=qtg.QKeySequence('7'))
            self.b8 = qtw.QPushButton("8",clicked=self.change_2,enabled=False,shortcut=qtg.QKeySequence('8'))
            self.b9 = qtw.QPushButton("9",clicked=self.change_2,enabled=False,shortcut=qtg.QKeySequence('9'))
            self.b0 = qtw.QPushButton("",clicked=self.change_2,enabled=False,shortcut=qtg.QKeySequence('0'))
            self.b_start = qtw.QPushButton("Start",clicked=self.start)
            self.b_back = qtw.QPushButton("Back",clicked=self.back,enabled=False,shortcut=qtg.QKeySequence("Backspace"))
            self.turn = 0
            
        gb2.setLayout(qtw.QGridLayout())
        gb2.layout().addWidget(self.b_start,3,0);gb2.layout().addWidget(self.b_back,3,2);gb2.layout().addWidget(self.b1,0,0);gb2.layout().addWidget(self.b2,0,1);gb2.layout().addWidget(self.b3,0,2);gb2.layout().addWidget(self.b4,1,0);gb2.layout().addWidget(self.b5,1,1);gb2.layout().addWidget(self.b6,1,2);gb2.layout().addWidget(self.b7,2,0);gb2.layout().addWidget(self.b8,2,1);gb2.layout().addWidget(self.b9,2,2);gb2.layout().addWidget(self.b0,3,1)
        gb1.setLayout(qtw.QVBoxLayout())
        gb1.layout().addWidget(self.text_edit)
        gb1.layout().addWidget(self.submit_button)
        gb2.setLayout(qtw.QGridLayout())
        dock_widget.layout().addWidget(gb1)
        dock_widget.layout().addWidget(gb2)
        self.dock.setWidget(dock_widget)
        self.dock.setFeatures(qtw.QDockWidget.DockWidgetFloatable | qtw.QDockWidget.DockWidgetMovable)
        self.addDockWidget(qtc.Qt.RightDockWidgetArea,self.dock)
        
        #List and Array
        self.list_all = [self.button_1_1, self.button_1_2, self.button_1_3, self.button_2_1, self.button_2_2, self.button_2_3 ,self.button_3_1, self.button_3_2, self.button_3_3,
                         self.button_1_4, self.button_1_5, self.button_1_6, self.button_2_4, self.button_2_5, self.button_2_6 ,self.button_3_4, self.button_3_5 ,self.button_3_6,
                         self.button_1_7, self.button_1_8, self.button_1_9, self.button_2_7, self.button_2_8, self.button_2_9 ,self.button_3_7, self.button_3_8, self.button_3_9,
                         self.button_4_1, self.button_4_2, self.button_4_3, self.button_5_1, self.button_5_2, self.button_5_3 ,self.button_6_1, self.button_6_2, self.button_6_3,
                         self.button_4_4, self.button_4_5, self.button_4_6, self.button_5_4, self.button_5_5, self.button_5_6 ,self.button_6_4, self.button_6_5, self.button_6_6,
                         self.button_4_7, self.button_4_8, self.button_4_9, self.button_5_7, self.button_5_8, self.button_5_9 ,self.button_6_7, self.button_6_8, self.button_6_9,
                         self.button_7_1, self.button_7_2, self.button_7_3, self.button_8_1, self.button_8_2, self.button_8_3 ,self.button_9_1, self.button_9_2, self.button_9_3,
                         self.button_7_4, self.button_7_5, self.button_7_6, self.button_8_4, self.button_8_5, self.button_8_6 ,self.button_9_4, self.button_9_5, self.button_9_6,
                         self.button_7_7, self.button_7_8, self.button_7_9, self.button_8_7, self.button_8_8, self.button_8_9 ,self.button_9_7, self.button_9_8, self.button_9_9]
                         
        self.array = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0]
                               ], dtype=int)
                               
        #Changing Font
        for i in self.list_all:
            i.clicked.connect(self.change)
            i.setFont(qtg.QFont("Times", 26))
            i.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)

    def change(self): #Function To change numbers on clicking on buttons
        sender = self.sender()
        self.turn = self.list_all.index(sender)
        index = self.list_all.index(sender)
        row = index//9
        column = index%9
        if sender.text() != "9":
            if sender.text() == "":
                sender.setText("1")
                self.array[row][column] = 1
            else:
                sender.setText(str(int(sender.text()) + 1))
                self.array[row][column] += 1
        else:
            sender.setText("")
            self.array[row][column] = 0

    def solve(self): # Main Function to solve Sudoku
    
        if len(np.where(self.array != 0)[0]) < 20:
            if qtw.QMessageBox.critical(self,"Sudoku","You Have Given Less than 20 prefilled digits,\nIt can take minutes or can Show Unexpected Results\nand in extreme case program can become not responding\nDo You Want To Continue ?",qtw.QMessageBox.No,qtw.QMessageBox.Yes) == qtw.QMessageBox.No:
                return False
                
        b = copy.copy(self.array)
        start = time.time()
        
        self.array = Solver(self.array).solve()
        
        if type(self.array) == str:
            qtw.QMessageBox.critical(self,"Sudoku Solver",f"Same Elements in {self.array}")
            self.array = b
            return
            
        lst = [self.array[i][j] for i in range(9) for j in range(9)]
        for i in range(81):
            self.list_all[i].setText(str(lst[i]))
        start = time.time() - start
        qtw.QMessageBox.about(self,"Sudoku Solver",f"Sudoku Solved \nTime - {start}")

    def reset(self): # Function to reset Everything
        self.turn = 0
        for i in self.list_all:
            i.setText("")
        self.array = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0, 0]
                               ], dtype=int)

    def open(self): # Function for open Sudoku from txt file
        filename, _ = qtw.QFileDialog.getOpenFileName(self, "Select File To Open", qtc.QDir.homePath(),'Text Files (*.txt)')
        if filename:
            self.reset()
            with open(filename, 'r') as fh:
                fh = fh.read()
                for i in range(81):
                    if int(fh[i]) == 0:continue
                    else: self.list_all[i].setText(str(fh[i]))

                n = 0
                for i in range(9):
                    for j in range(9):
                        self.array[i][j] = fh[n]
                        n += 1

    def save(self): # Function for saving Solved or Unsolved Sudoku
        filename, _ = qtw.QFileDialog.getSaveFileName(self, "Select File To Save", qtc.QDir.homePath(),'Text Files (*.txt)')
        with open(filename,'w') as fh:
            fh.write("")
        with open(filename,'a') as fh:
            for i in self.list_all:
                fh.write(i.text())

    def rules(self): # Function to display Rules on clicking Rules in About Menu
        qtw.QMessageBox.information(self,"Rules",f"Rules For Sudoku : \n\n1. The objective is to fill a 9x9 grid so that each column, each row, and each of the nine 3x3 boxes contains the digits from 1 to 9.\n2. Each column must contain all of the numbers 1 through 9 and no two numbers in the same column of a Sudoku puzzle can be the same.\n3. Each row must contain all of the numbers 1 through 9 and no two numbers in the same row of a Sudoku puzzle can be the same.\n4. Each block must contain all of the numbers 1 through 9 and no two numbers in the same block of a Sudoku puzzle can be the same.")

    def submit(self):
        self.reset()
        text = self.text_edit.toPlainText()
        for i in range(81):
            if int(text[i]) == 0:continue
            else:self.list_all[i].setText(str(text[i]))
        n = 0
        for i in range(9):
            for j in range(9):
                self.array[i][j] = int(text[n])
                n += 1

    def change_2(self):
        sender = self.sender()
        if self.turn > 80:
            self.turn = 0
        text = sender.text()
        self.list_all[self.turn].setText(text)
        if text == "":
            self.array[int(self.turn // 9)][int(self.turn % 9)] = 0
        else:
            self.array[int(self.turn//9)][int(self.turn%9)] = int(text)
        self.turn += 1


    def start(self):
        self.b9.setEnabled(True);self.b8.setEnabled(True);self.b7.setEnabled(True);self.b6.setEnabled(True);self.b5.setEnabled(True);self.b4.setEnabled(True);self.b3.setEnabled(True);self.b2.setEnabled(True);self.b1.setEnabled(True);self.b0.setEnabled(True);self.b_back.setEnabled(True)

    def back(self):
        if self.turn == 0:
            return
        self.turn -= 1
        self.list_all[self.turn].setText("")
        self.array[int(self.turn // 9)][int(self.turn % 9)] = 0


app = qtw.QApplication(sys.argv)
mw = Ui()
mw.show()
sys.exit(app.exec())
