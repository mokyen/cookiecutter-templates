# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './gui.ui',
# licensing of './gui.ui' applies.
#
# Created: Wed Oct  9 17:50:43 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu_View = QtWidgets.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.console = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.console.sizePolicy().hasHeightForWidth())
        self.console.setSizePolicy(sizePolicy)
        self.console.setMinimumSize(QtCore.QSize(95, 113))
        self.console.setMaximumSize(QtCore.QSize(524287, 524287))
        self.console.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.console.setObjectName("console")
        self.dockWidgetContents = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_8.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.text_edit = QtWidgets.QPlainTextEdit(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_edit.sizePolicy().hasHeightForWidth())
        self.text_edit.setSizePolicy(sizePolicy)
        self.text_edit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.text_edit.setReadOnly(True)
        self.text_edit.setMaximumBlockCount(200)
        self.text_edit.setCenterOnScroll(True)
        self.text_edit.setObjectName("text_edit")
        self.gridLayout_8.addWidget(self.text_edit, 0, 0, 1, 1)
        self.console.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.console)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionToggleConsole = QtWidgets.QAction(MainWindow)
        self.actionToggleConsole.setCheckable(True)
        self.actionToggleConsole.setChecked(True)
        self.actionToggleConsole.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionToggleConsole.setObjectName("actionToggleConsole")
        self.actionE_xit = QtWidgets.QAction(MainWindow)
        self.actionE_xit.setObjectName("actionE_xit")
        self.actionDebugMode = QtWidgets.QAction(MainWindow)
        self.actionDebugMode.setCheckable(True)
        self.actionDebugMode.setChecked(True)
        self.actionDebugMode.setObjectName("actionDebugMode")
        self.menuFile.addAction(self.actionE_xit)
        self.menu_View.addAction(self.actionToggleConsole)
        self.menu_View.addAction(self.actionDebugMode)
        self.menu_Help.addAction(self.actionAbout)
        self.menu_Help.addAction(self.actionDocumentation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionToggleConsole, QtCore.SIGNAL("triggered(bool)"), self.console.setVisible)
        QtCore.QObject.connect(self.console, QtCore.SIGNAL("visibilityChanged(bool)"), self.actionToggleConsole.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "{{ cookiecutter.repo_name }}", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "&File", None, -1))
        self.menu_View.setTitle(QtWidgets.QApplication.translate("MainWindow", "&View", None, -1))
        self.menu_Help.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Help", None, -1))
        self.console.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Console", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.actionDocumentation.setText(QtWidgets.QApplication.translate("MainWindow", "Documentation", None, -1))
        self.actionToggleConsole.setText(QtWidgets.QApplication.translate("MainWindow", "Console", None, -1))
        self.actionToggleConsole.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+`", None, -1))
        self.actionE_xit.setText(QtWidgets.QApplication.translate("MainWindow", "E&xit", None, -1))
        self.actionE_xit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.actionDebugMode.setText(QtWidgets.QApplication.translate("MainWindow", "Debug Mode", None, -1))

