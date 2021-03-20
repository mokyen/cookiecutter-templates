# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . import icons_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_toggle_status_bar = QAction(MainWindow)
        self.action_toggle_status_bar.setObjectName("action_toggle_status_bar")
        self.action_toggle_status_bar.setCheckable(True)
        self.action_toggle_status_bar.setChecked(False)
        self.action_view_log = QAction(MainWindow)
        self.action_view_log.setObjectName("action_view_log")
        self.action_close = QAction(MainWindow)
        self.action_close.setObjectName("action_close")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "QStatusBar{\n"
            'color: "#B3FFFFFF";\n'
            'background-color: "#121212";\n'
            "}\n"
            "QWidget{\n"
            'background-color: "#121212";\n'
            "}\n"
            "QLabel{\n"
            'color: "#FFFFFFFF";\n'
            "}\n"
            "QLabel#title_label{\n"
            'color: "#FFFFFFFF";\n'
            "}\n"
            "QPushButton {\n"
            "     border: none;\n"
            '	color: "#BEFFFFFF";\n'
            "    }\n"
            "QPushButton:hover {\n"
            '    background-color: "#383838";\n'
            "}\n"
            "QPushButton:checked {\n"
            '    background-color: "#242424";\n'
            "}\n"
            "QPlainTextEdit{\n"
            '	color: "#FFFFFFFF";\n'
            "}"
        )
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titlebar = QFrame(self.centralwidget)
        self.titlebar.setObjectName("titlebar")
        self.titlebar.setMinimumSize(QSize(0, 30))
        self.titlebar.setMaximumSize(QSize(16777215, 16777215))
        self.titlebar.setStyleSheet("")
        self.titlebar.setFrameShape(QFrame.NoFrame)
        self.titlebar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.titlebar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title_label = QLabel(self.titlebar)
        self.title_label.setObjectName("title_label")
        self.title_label.setMaximumSize(QSize(16777215, 20))
        self.title_label.setStyleSheet("")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.title_label)

        self.minimize_btn = QPushButton(self.titlebar)
        self.minimize_btn.setObjectName("minimize_btn")
        self.minimize_btn.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(":/icons/16x16/window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon)
        self.minimize_btn.setIconSize(QSize(10, 10))
        self.minimize_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.titlebar)
        self.maximize_btn.setObjectName("maximize_btn")
        self.maximize_btn.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(":/icons/16x16/window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon1)
        self.maximize_btn.setIconSize(QSize(10, 10))
        self.maximize_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.maximize_btn)

        self.exit_btn = QPushButton(self.titlebar)
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(":/icons/16x16/window-close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon2)
        self.exit_btn.setIconSize(QSize(10, 10))
        self.exit_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.exit_btn)

        self.verticalLayout.addWidget(self.titlebar)

        self.wrapper = QFrame(self.centralwidget)
        self.wrapper.setObjectName("wrapper")
        self.wrapper.setFrameShape(QFrame.NoFrame)
        self.wrapper.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.wrapper)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.wrapper)
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setMinimumSize(QSize(60, 0))
        self.sidebar.setMaximumSize(QSize(60, 16777215))
        self.sidebar.setStyleSheet("")
        self.sidebar.setFrameShape(QFrame.NoFrame)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_btn = QPushButton(self.sidebar)
        self.sidebar_buttons = QButtonGroup(MainWindow)
        self.sidebar_buttons.setObjectName("sidebar_buttons")
        self.sidebar_buttons.addButton(self.main_btn)
        self.main_btn.setObjectName("main_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_btn.sizePolicy().hasHeightForWidth())
        self.main_btn.setSizePolicy(sizePolicy)
        self.main_btn.setMinimumSize(QSize(60, 60))
        self.main_btn.setStyleSheet("")
        icon3 = QIcon()
        icon3.addFile(":/icons/16x16/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.main_btn.setIcon(icon3)
        self.main_btn.setCheckable(True)
        self.main_btn.setChecked(True)
        self.main_btn.setAutoExclusive(True)
        self.main_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.main_btn)

        self.log_btn = QPushButton(self.sidebar)
        self.sidebar_buttons.addButton(self.log_btn)
        self.log_btn.setObjectName("log_btn")
        sizePolicy.setHeightForWidth(self.log_btn.sizePolicy().hasHeightForWidth())
        self.log_btn.setSizePolicy(sizePolicy)
        self.log_btn.setMinimumSize(QSize(60, 60))
        icon4 = QIcon()
        icon4.addFile(":/icons/16x16/clipboard-list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.log_btn.setIcon(icon4)
        self.log_btn.setCheckable(True)
        self.log_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.log_btn)

        self.verticalSpacer = QSpacerItem(20, 345, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.settings_btn = QPushButton(self.sidebar)
        self.sidebar_buttons.addButton(self.settings_btn)
        self.settings_btn.setObjectName("settings_btn")
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        self.settings_btn.setMinimumSize(QSize(60, 60))
        icon5 = QIcon()
        icon5.addFile(":/icons/16x16/wrench.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon5)
        self.settings_btn.setIconSize(QSize(16, 16))
        self.settings_btn.setCheckable(True)
        self.settings_btn.setFlat(True)

        self.verticalLayout_2.addWidget(self.settings_btn)

        self.horizontalLayout.addWidget(self.sidebar)

        self.content = QFrame(self.wrapper)
        self.content.setObjectName("content")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy1)
        self.content.setStyleSheet('background-color: "#242424";')
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.stacked_widget = QStackedWidget(self.content)
        self.stacked_widget.setObjectName("stacked_widget")
        sizePolicy1.setHeightForWidth(self.stacked_widget.sizePolicy().hasHeightForWidth())
        self.stacked_widget.setSizePolicy(sizePolicy1)
        self.stacked_widget.setStyleSheet("")
        self.main_widget = QWidget()
        self.main_widget.setObjectName("main_widget")
        self.stacked_widget.addWidget(self.main_widget)
        self.log_widget = QWidget()
        self.log_widget.setObjectName("log_widget")
        self.gridLayout = QGridLayout(self.log_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.log_textedit = QPlainTextEdit(self.log_widget)
        self.log_textedit.setObjectName("log_textedit")
        font = QFont()
        font.setFamily("Arial")
        self.log_textedit.setFont(font)
        self.log_textedit.setFrameShape(QFrame.NoFrame)
        self.log_textedit.setUndoRedoEnabled(False)
        self.log_textedit.setReadOnly(True)
        self.log_textedit.setTextInteractionFlags(
            Qt.LinksAccessibleByMouse | Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )
        self.log_textedit.setBackgroundVisible(False)
        self.log_textedit.setCenterOnScroll(True)

        self.gridLayout.addWidget(self.log_textedit, 0, 0, 1, 1)

        self.stacked_widget.addWidget(self.log_widget)
        self.settings_widget = QWidget()
        self.settings_widget.setObjectName("settings_widget")
        self.stacked_widget.addWidget(self.settings_widget)

        self.horizontalLayout_2.addWidget(self.stacked_widget)

        self.horizontalLayout.addWidget(self.content)

        self.verticalLayout.addWidget(self.wrapper)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setFont(font)
        self.statusbar.setStyleSheet("")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_view = QMenu(self.menubar)
        self.menu_view.setObjectName("menu_view")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_close)
        self.menu_view.addAction(self.action_toggle_status_bar)
        self.menu_view.addSeparator()
        self.menu_view.addAction(self.action_view_log)
        self.menu_help.addAction(self.action_about)

        self.retranslateUi(MainWindow)
        self.action_toggle_status_bar.toggled.connect(self.statusbar.setVisible)

        self.stacked_widget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", "About", None))
        self.action_toggle_status_bar.setText(
            QCoreApplication.translate("MainWindow", "Status Bar", None)
        )
        self.action_view_log.setText(QCoreApplication.translate("MainWindow", "View Log", None))
        self.action_close.setText(QCoreApplication.translate("MainWindow", "Close", None))
        self.title_label.setText(
            QCoreApplication.translate("MainWindow", "<strong>MY</strong>GUI", None)
        )
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.exit_btn.setText("")
        self.main_btn.setText("")
        # if QT_CONFIG(tooltip)
        self.log_btn.setToolTip(QCoreApplication.translate("MainWindow", "Console Log", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.log_btn.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.log_btn.setText("")
        self.settings_btn.setText("")
        self.log_textedit.setDocumentTitle("")
        self.log_textedit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Log Messages", None)
        )
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menu_view.setTitle(QCoreApplication.translate("MainWindow", "View", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", "Help", None))

    # retranslateUi
