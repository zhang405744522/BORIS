# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boris.ui'
#
# Created: Wed Mar 12 13:59:30 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 606)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbLogoBoris = QtGui.QLabel(self.centralwidget)
        self.lbLogoBoris.setText("")
        self.lbLogoBoris.setScaledContents(False)
        self.lbLogoBoris.setAlignment(QtCore.Qt.AlignCenter)
        self.lbLogoBoris.setObjectName("lbLogoBoris")
        self.verticalLayout_3.addWidget(self.lbLogoBoris)
        self.lbLogoUnito = QtGui.QLabel(self.centralwidget)
        self.lbLogoUnito.setText("")
        self.lbLogoUnito.setTextFormat(QtCore.Qt.AutoText)
        self.lbLogoUnito.setAlignment(QtCore.Qt.AlignCenter)
        self.lbLogoUnito.setWordWrap(True)
        self.lbLogoUnito.setObjectName("lbLogoUnito")
        self.verticalLayout_3.addWidget(self.lbLogoUnito)
        self.lbFocalSubject = QtGui.QLabel(self.centralwidget)
        self.lbFocalSubject.setObjectName("lbFocalSubject")
        self.verticalLayout_3.addWidget(self.lbFocalSubject)
        self.lbCurrentStates = QtGui.QLabel(self.centralwidget)
        self.lbCurrentStates.setObjectName("lbCurrentStates")
        self.verticalLayout_3.addWidget(self.lbCurrentStates)
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setEnabled(True)
        self.toolBox.setObjectName("toolBox")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 352, 403))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.verticalLayout_3.addWidget(self.toolBox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 22))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuObservations = QtGui.QMenu(self.menubar)
        self.menuObservations.setObjectName("menuObservations")
        self.menuExport_events = QtGui.QMenu(self.menuObservations)
        self.menuExport_events.setObjectName("menuExport_events")
        self.menuAnalyze = QtGui.QMenu(self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        self.menuPlayback = QtGui.QMenu(self.menubar)
        self.menuPlayback.setObjectName("menuPlayback")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setToolTip("")
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dwConfiguration = QtGui.QDockWidget(MainWindow)
        self.dwConfiguration.setFloating(False)
        self.dwConfiguration.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dwConfiguration.setObjectName("dwConfiguration")
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.twConfiguration = QtGui.QTableWidget(self.dockWidgetContents_3)
        self.twConfiguration.setFocusPolicy(QtCore.Qt.NoFocus)
        self.twConfiguration.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.twConfiguration.setAlternatingRowColors(True)
        self.twConfiguration.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.twConfiguration.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.twConfiguration.setObjectName("twConfiguration")
        self.twConfiguration.setColumnCount(6)
        self.twConfiguration.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.twConfiguration.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twConfiguration.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.twConfiguration.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.twConfiguration.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.twConfiguration.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.twConfiguration.setHorizontalHeaderItem(5, item)
        self.verticalLayout_4.addWidget(self.twConfiguration)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.dwConfiguration.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dwConfiguration)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dwObservations = QtGui.QDockWidget(MainWindow)
        self.dwObservations.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dwObservations.setFloating(False)
        self.dwObservations.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dwObservations.setObjectName("dwObservations")
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.twEvents = QtGui.QTableWidget(self.dockWidgetContents_2)
        self.twEvents.setEnabled(True)
        self.twEvents.setFocusPolicy(QtCore.Qt.NoFocus)
        self.twEvents.setAutoScroll(False)
        self.twEvents.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
        self.twEvents.setTabKeyNavigation(False)
        self.twEvents.setProperty("showDropIndicator", False)
        self.twEvents.setDragDropOverwriteMode(False)
        self.twEvents.setAlternatingRowColors(True)
        self.twEvents.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.twEvents.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.twEvents.setObjectName("twEvents")
        self.twEvents.setColumnCount(0)
        self.twEvents.setRowCount(0)
        self.verticalLayout.addWidget(self.twEvents)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.dwObservations.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dwObservations)
        self.dwSubjects = QtGui.QDockWidget(MainWindow)
        self.dwSubjects.setFloating(False)
        self.dwSubjects.setObjectName("dwSubjects")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.twSubjects = QtGui.QTableWidget(self.dockWidgetContents)
        self.twSubjects.setFocusPolicy(QtCore.Qt.NoFocus)
        self.twSubjects.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.twSubjects.setAlternatingRowColors(True)
        self.twSubjects.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.twSubjects.setObjectName("twSubjects")
        self.twSubjects.setColumnCount(3)
        self.twSubjects.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.twSubjects)
        self.dwSubjects.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dwSubjects)
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPause = QtGui.QAction(MainWindow)
        self.actionPause.setObjectName("actionPause")
        self.actionPlay = QtGui.QAction(MainWindow)
        self.actionPlay.setObjectName("actionPlay")
        self.actionOpen_video_file = QtGui.QAction(MainWindow)
        self.actionOpen_video_file.setObjectName("actionOpen_video_file")
        self.actionReset = QtGui.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionFaster = QtGui.QAction(MainWindow)
        self.actionFaster.setEnabled(True)
        self.actionFaster.setObjectName("actionFaster")
        self.actionSlower = QtGui.QAction(MainWindow)
        self.actionSlower.setEnabled(True)
        self.actionSlower.setObjectName("actionSlower")
        self.actionJumpForward = QtGui.QAction(MainWindow)
        self.actionJumpForward.setObjectName("actionJumpForward")
        self.actionLoad_configuration = QtGui.QAction(MainWindow)
        self.actionLoad_configuration.setObjectName("actionLoad_configuration")
        self.actionDelete_selected_observations = QtGui.QAction(MainWindow)
        self.actionDelete_selected_observations.setObjectName("actionDelete_selected_observations")
        self.actionDelete_all_observations = QtGui.QAction(MainWindow)
        self.actionDelete_all_observations.setObjectName("actionDelete_all_observations")
        self.actionSort_observations = QtGui.QAction(MainWindow)
        self.actionSort_observations.setObjectName("actionSort_observations")
        self.actionLoad_observations_file = QtGui.QAction(MainWindow)
        self.actionLoad_observations_file.setObjectName("actionLoad_observations_file")
        self.actionSelect_observations = QtGui.QAction(MainWindow)
        self.actionSelect_observations.setObjectName("actionSelect_observations")
        self.actionConfigure_states_and_events = QtGui.QAction(MainWindow)
        self.actionConfigure_states_and_events.setEnabled(False)
        self.actionConfigure_states_and_events.setObjectName("actionConfigure_states_and_events")
        self.actionEdit_event = QtGui.QAction(MainWindow)
        self.actionEdit_event.setObjectName("actionEdit_event")
        self.actionLoad_configuration_file = QtGui.QAction(MainWindow)
        self.actionLoad_configuration_file.setObjectName("actionLoad_configuration_file")
        self.actionMedia_file_information = QtGui.QAction(MainWindow)
        self.actionMedia_file_information.setObjectName("actionMedia_file_information")
        self.actionStart_live_observation = QtGui.QAction(MainWindow)
        self.actionStart_live_observation.setObjectName("actionStart_live_observation")
        self.actionNew_project = QtGui.QAction(MainWindow)
        self.actionNew_project.setObjectName("actionNew_project")
        self.actionTime_budget = QtGui.QAction(MainWindow)
        self.actionTime_budget.setObjectName("actionTime_budget")
        self.actionSave_project = QtGui.QAction(MainWindow)
        self.actionSave_project.setObjectName("actionSave_project")
        self.actionOpen_project = QtGui.QAction(MainWindow)
        self.actionOpen_project.setObjectName("actionOpen_project")
        self.actionSet_offset = QtGui.QAction(MainWindow)
        self.actionSet_offset.setObjectName("actionSet_offset")
        self.actionEdit_project = QtGui.QAction(MainWindow)
        self.actionEdit_project.setObjectName("actionEdit_project")
        self.actionSave_project_as = QtGui.QAction(MainWindow)
        self.actionSave_project_as.setObjectName("actionSave_project_as")
        self.actionVisualize_data = QtGui.QAction(MainWindow)
        self.actionVisualize_data.setObjectName("actionVisualize_data")
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionNew_observation = QtGui.QAction(MainWindow)
        self.actionNew_observation.setObjectName("actionNew_observation")
        self.actionSave_observation = QtGui.QAction(MainWindow)
        self.actionSave_observation.setObjectName("actionSave_observation")
        self.actionClose_observation = QtGui.QAction(MainWindow)
        self.actionClose_observation.setObjectName("actionClose_observation")
        self.actionEdit_current_observation = QtGui.QAction(MainWindow)
        self.actionEdit_current_observation.setEnabled(False)
        self.actionEdit_current_observation.setObjectName("actionEdit_current_observation")
        self.actionOpen_observation_2 = QtGui.QAction(MainWindow)
        self.actionOpen_observation_2.setObjectName("actionOpen_observation_2")
        self.actionAdd_event = QtGui.QAction(MainWindow)
        self.actionAdd_event.setObjectName("actionAdd_event")
        self.actionDeselectCurrentSubject = QtGui.QAction(MainWindow)
        self.actionDeselectCurrentSubject.setObjectName("actionDeselectCurrentSubject")
        self.actionNext = QtGui.QAction(MainWindow)
        self.actionNext.setIconVisibleInMenu(False)
        self.actionNext.setObjectName("actionNext")
        self.actionPrevious = QtGui.QAction(MainWindow)
        self.actionPrevious.setObjectName("actionPrevious")
        self.actionJumpTo = QtGui.QAction(MainWindow)
        self.actionJumpTo.setEnabled(True)
        self.actionJumpTo.setObjectName("actionJumpTo")
        self.actionJumpBackward = QtGui.QAction(MainWindow)
        self.actionJumpBackward.setObjectName("actionJumpBackward")
        self.actionEdit_observation = QtGui.QAction(MainWindow)
        self.actionEdit_observation.setObjectName("actionEdit_observation")
        self.actionCheckUpdate = QtGui.QAction(MainWindow)
        self.actionCheckUpdate.setObjectName("actionCheckUpdate")
        self.actionExportEventTabular = QtGui.QAction(MainWindow)
        self.actionExportEventTabular.setObjectName("actionExportEventTabular")
        self.actionExportEventString = QtGui.QAction(MainWindow)
        self.actionExportEventString.setObjectName("actionExportEventString")
        self.actionClose_project = QtGui.QAction(MainWindow)
        self.actionClose_project.setObjectName("actionClose_project")
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionCheckUpdate)
        self.menuFile.addAction(self.actionNew_project)
        self.menuFile.addAction(self.actionOpen_project)
        self.menuFile.addAction(self.actionEdit_project)
        self.menuFile.addAction(self.actionSave_project)
        self.menuFile.addAction(self.actionSave_project_as)
        self.menuFile.addAction(self.actionClose_project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuExport_events.addAction(self.actionExportEventTabular)
        self.menuExport_events.addAction(self.actionExportEventString)
        self.menuObservations.addAction(self.actionNew_observation)
        self.menuObservations.addAction(self.actionOpen_observation_2)
        self.menuObservations.addAction(self.actionEdit_observation)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionClose_observation)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionAdd_event)
        self.menuObservations.addAction(self.actionEdit_event)
        self.menuObservations.addAction(self.actionSort_observations)
        self.menuObservations.addAction(self.actionSelect_observations)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionDelete_selected_observations)
        self.menuObservations.addAction(self.actionDelete_all_observations)
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionLoad_observations_file)
        self.menuObservations.addAction(self.menuExport_events.menuAction())
        self.menuObservations.addSeparator()
        self.menuObservations.addAction(self.actionMedia_file_information)
        self.menuAnalyze.addAction(self.actionTime_budget)
        self.menuAnalyze.addAction(self.actionVisualize_data)
        self.menuPlayback.addAction(self.actionJumpForward)
        self.menuPlayback.addAction(self.actionJumpBackward)
        self.menuPlayback.addAction(self.actionJumpTo)
        self.menuPlayback.addSeparator()
        self.menuPlayback.addAction(self.actionPlay)
        self.menuPlayback.addAction(self.actionPause)
        self.menuPlayback.addAction(self.actionPrevious)
        self.menuPlayback.addAction(self.actionNext)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuObservations.menuAction())
        self.menubar.addAction(self.menuPlayback.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionPlay)
        self.toolBar.addAction(self.actionPause)
        self.toolBar.addAction(self.actionReset)
        self.toolBar.addAction(self.actionJumpBackward)
        self.toolBar.addAction(self.actionJumpForward)
        self.toolBar.addAction(self.actionFaster)
        self.toolBar.addAction(self.actionSlower)
        self.toolBar.addAction(self.actionPrevious)
        self.toolBar.addAction(self.actionNext)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "BORIS", None, QtGui.QApplication.UnicodeUTF8))
        self.lbFocalSubject.setText(QtGui.QApplication.translate("MainWindow", "lbFocalSubject", None, QtGui.QApplication.UnicodeUTF8))
        self.lbCurrentStates.setText(QtGui.QApplication.translate("MainWindow", "lbCurrentStates", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("MainWindow", "Page", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuObservations.setTitle(QtGui.QApplication.translate("MainWindow", "Observations", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExport_events.setTitle(QtGui.QApplication.translate("MainWindow", "Export events", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAnalyze.setTitle(QtGui.QApplication.translate("MainWindow", "Analyze", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlayback.setTitle(QtGui.QApplication.translate("MainWindow", "Playback", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.dwConfiguration.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Configuration of behaviours", None, QtGui.QApplication.UnicodeUTF8))
        self.twConfiguration.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.twConfiguration.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Code", None, QtGui.QApplication.UnicodeUTF8))
        self.twConfiguration.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.twConfiguration.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.twConfiguration.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "Modifiers", None, QtGui.QApplication.UnicodeUTF8))
        self.twConfiguration.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "Excluded", None, QtGui.QApplication.UnicodeUTF8))
        self.dwObservations.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Events", None, QtGui.QApplication.UnicodeUTF8))
        self.dwSubjects.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Subjects", None, QtGui.QApplication.UnicodeUTF8))
        self.twSubjects.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.twSubjects.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.twSubjects.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Current state(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDocumentation.setText(QtGui.QApplication.translate("MainWindow", "Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause.setText(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPause.setToolTip(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlay.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_video_file.setText(QtGui.QApplication.translate("MainWindow", "Open media file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFaster.setText(QtGui.QApplication.translate("MainWindow", "Faster", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSlower.setText(QtGui.QApplication.translate("MainWindow", "Slower", None, QtGui.QApplication.UnicodeUTF8))
        self.actionJumpForward.setText(QtGui.QApplication.translate("MainWindow", "Jump forward", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_configuration.setText(QtGui.QApplication.translate("MainWindow", "Load configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_selected_observations.setText(QtGui.QApplication.translate("MainWindow", "Delete selected events", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_all_observations.setText(QtGui.QApplication.translate("MainWindow", "Delete all events", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSort_observations.setText(QtGui.QApplication.translate("MainWindow", "Sort events", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_observations_file.setText(QtGui.QApplication.translate("MainWindow", "Import events", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_observations.setText(QtGui.QApplication.translate("MainWindow", "Select events from interval", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigure_states_and_events.setText(QtGui.QApplication.translate("MainWindow", "Configure states and events", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_event.setText(QtGui.QApplication.translate("MainWindow", "Edit event", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_configuration_file.setText(QtGui.QApplication.translate("MainWindow", "Load state and events configuration file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMedia_file_information.setText(QtGui.QApplication.translate("MainWindow", "Media file information", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart_live_observation.setText(QtGui.QApplication.translate("MainWindow", "Start observation without media file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_project.setText(QtGui.QApplication.translate("MainWindow", "New project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTime_budget.setText(QtGui.QApplication.translate("MainWindow", "Time budget", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_project.setText(QtGui.QApplication.translate("MainWindow", "Save project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_project.setText(QtGui.QApplication.translate("MainWindow", "Open project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_project.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_offset.setText(QtGui.QApplication.translate("MainWindow", "Set time offset", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_project.setText(QtGui.QApplication.translate("MainWindow", "Edit project", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_project_as.setText(QtGui.QApplication.translate("MainWindow", "Save project as ...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVisualize_data.setText(QtGui.QApplication.translate("MainWindow", "Visualize data ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_observation.setText(QtGui.QApplication.translate("MainWindow", "New observation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_observation.setText(QtGui.QApplication.translate("MainWindow", "Save current observation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_observation.setText(QtGui.QApplication.translate("MainWindow", "Close observation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_current_observation.setText(QtGui.QApplication.translate("MainWindow", "Edit current observation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_observation_2.setText(QtGui.QApplication.translate("MainWindow", "Open observation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_event.setText(QtGui.QApplication.translate("MainWindow", "Add event", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeselectCurrentSubject.setText(QtGui.QApplication.translate("MainWindow", "Deselect current subject", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext.setToolTip(QtGui.QApplication.translate("MainWindow", "Next media file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrevious.setText(QtGui.QApplication.translate("MainWindow", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrevious.setToolTip(QtGui.QApplication.translate("MainWindow", "Previous media file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionJumpTo.setText(QtGui.QApplication.translate("MainWindow", "Jump to specific time", None, QtGui.QApplication.UnicodeUTF8))
        self.actionJumpBackward.setText(QtGui.QApplication.translate("MainWindow", "Jump backward", None, QtGui.QApplication.UnicodeUTF8))
        self.actionJumpBackward.setToolTip(QtGui.QApplication.translate("MainWindow", "Jump backward", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_observation.setText(QtGui.QApplication.translate("MainWindow", "Edit observation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheckUpdate.setText(QtGui.QApplication.translate("MainWindow", "Check for updates", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportEventTabular.setText(QtGui.QApplication.translate("MainWindow", "Tabular format", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExportEventString.setText(QtGui.QApplication.translate("MainWindow", "Behavioural strings format", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose_project.setText(QtGui.QApplication.translate("MainWindow", "Close project", None, QtGui.QApplication.UnicodeUTF8))

