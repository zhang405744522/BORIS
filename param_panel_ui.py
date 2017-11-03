# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'param_panel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1037, 890)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lbSubjects = QtGui.QLabel(Dialog)
        self.lbSubjects.setObjectName(_fromUtf8("lbSubjects"))
        self.verticalLayout_4.addWidget(self.lbSubjects)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pbSelectAllSubjects = QtGui.QPushButton(Dialog)
        self.pbSelectAllSubjects.setObjectName(_fromUtf8("pbSelectAllSubjects"))
        self.horizontalLayout_3.addWidget(self.pbSelectAllSubjects)
        self.pbUnselectAllSubjects = QtGui.QPushButton(Dialog)
        self.pbUnselectAllSubjects.setObjectName(_fromUtf8("pbUnselectAllSubjects"))
        self.horizontalLayout_3.addWidget(self.pbUnselectAllSubjects)
        self.pbReverseSubjectsSelection = QtGui.QPushButton(Dialog)
        self.pbReverseSubjectsSelection.setObjectName(_fromUtf8("pbReverseSubjectsSelection"))
        self.horizontalLayout_3.addWidget(self.pbReverseSubjectsSelection)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.lwSubjects = QtGui.QListWidget(Dialog)
        self.lwSubjects.setObjectName(_fromUtf8("lwSubjects"))
        self.verticalLayout_4.addWidget(self.lwSubjects)
        self.lbBehaviors = QtGui.QLabel(Dialog)
        self.lbBehaviors.setObjectName(_fromUtf8("lbBehaviors"))
        self.verticalLayout_4.addWidget(self.lbBehaviors)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pbSelectAllBehaviors = QtGui.QPushButton(Dialog)
        self.pbSelectAllBehaviors.setObjectName(_fromUtf8("pbSelectAllBehaviors"))
        self.horizontalLayout_4.addWidget(self.pbSelectAllBehaviors)
        self.pbUnselectAllBehaviors = QtGui.QPushButton(Dialog)
        self.pbUnselectAllBehaviors.setObjectName(_fromUtf8("pbUnselectAllBehaviors"))
        self.horizontalLayout_4.addWidget(self.pbUnselectAllBehaviors)
        self.pbReverseBehaviorsSelection = QtGui.QPushButton(Dialog)
        self.pbReverseBehaviorsSelection.setObjectName(_fromUtf8("pbReverseBehaviorsSelection"))
        self.horizontalLayout_4.addWidget(self.pbReverseBehaviorsSelection)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.lwBehaviors = QtGui.QListWidget(Dialog)
        self.lwBehaviors.setObjectName(_fromUtf8("lwBehaviors"))
        self.verticalLayout_4.addWidget(self.lwBehaviors)
        self.cbIncludeModifiers = QtGui.QCheckBox(Dialog)
        self.cbIncludeModifiers.setObjectName(_fromUtf8("cbIncludeModifiers"))
        self.verticalLayout_4.addWidget(self.cbIncludeModifiers)
        self.cbExcludeBehaviors = QtGui.QCheckBox(Dialog)
        self.cbExcludeBehaviors.setObjectName(_fromUtf8("cbExcludeBehaviors"))
        self.verticalLayout_4.addWidget(self.cbExcludeBehaviors)
        self.frm_time = QtGui.QFrame(Dialog)
        self.frm_time.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frm_time.setFrameShadow(QtGui.QFrame.Raised)
        self.frm_time.setObjectName(_fromUtf8("frm_time"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frm_time)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.rb_full = QtGui.QRadioButton(self.frm_time)
        self.rb_full.setChecked(True)
        self.rb_full.setObjectName(_fromUtf8("rb_full"))
        self.horizontalLayout_5.addWidget(self.rb_full)
        self.rb_interval = QtGui.QRadioButton(self.frm_time)
        self.rb_interval.setObjectName(_fromUtf8("rb_interval"))
        self.horizontalLayout_5.addWidget(self.rb_interval)
        self.rb_limit = QtGui.QRadioButton(self.frm_time)
        self.rb_limit.setObjectName(_fromUtf8("rb_limit"))
        self.horizontalLayout_5.addWidget(self.rb_limit)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.frm_time_interval = QtGui.QFrame(self.frm_time)
        self.frm_time_interval.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frm_time_interval.setFrameShadow(QtGui.QFrame.Raised)
        self.frm_time_interval.setObjectName(_fromUtf8("frm_time_interval"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frm_time_interval)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.frm_time_interval)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbStartTime = QtGui.QLabel(self.frm_time_interval)
        self.lbStartTime.setObjectName(_fromUtf8("lbStartTime"))
        self.horizontalLayout.addWidget(self.lbStartTime)
        self.teStartTime = QtGui.QTimeEdit(self.frm_time_interval)
        self.teStartTime.setObjectName(_fromUtf8("teStartTime"))
        self.horizontalLayout.addWidget(self.teStartTime)
        self.dsbStartTime = QtGui.QDoubleSpinBox(self.frm_time_interval)
        self.dsbStartTime.setDecimals(3)
        self.dsbStartTime.setMaximum(1000000.0)
        self.dsbStartTime.setObjectName(_fromUtf8("dsbStartTime"))
        self.horizontalLayout.addWidget(self.dsbStartTime)
        self.lbEndTime = QtGui.QLabel(self.frm_time_interval)
        self.lbEndTime.setObjectName(_fromUtf8("lbEndTime"))
        self.horizontalLayout.addWidget(self.lbEndTime)
        self.teEndTime = QtGui.QTimeEdit(self.frm_time_interval)
        self.teEndTime.setObjectName(_fromUtf8("teEndTime"))
        self.horizontalLayout.addWidget(self.teEndTime)
        self.dsbEndTime = QtGui.QDoubleSpinBox(self.frm_time_interval)
        self.dsbEndTime.setDecimals(3)
        self.dsbEndTime.setMaximum(1000000.0)
        self.dsbEndTime.setObjectName(_fromUtf8("dsbEndTime"))
        self.horizontalLayout.addWidget(self.dsbEndTime)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.frm_time_interval)
        self.verticalLayout_4.addWidget(self.frm_time)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pbCancel = QtGui.QPushButton(Dialog)
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.horizontalLayout_2.addWidget(self.pbCancel)
        self.pbOK = QtGui.QPushButton(Dialog)
        self.pbOK.setObjectName(_fromUtf8("pbOK"))
        self.horizontalLayout_2.addWidget(self.pbOK)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Parameters", None))
        self.lbSubjects.setText(_translate("Dialog", "Subjects", None))
        self.pbSelectAllSubjects.setText(_translate("Dialog", "Select all", None))
        self.pbUnselectAllSubjects.setText(_translate("Dialog", "Unselect all", None))
        self.pbReverseSubjectsSelection.setText(_translate("Dialog", "Reverse selection", None))
        self.lbBehaviors.setText(_translate("Dialog", "Behaviors", None))
        self.pbSelectAllBehaviors.setText(_translate("Dialog", "Select all", None))
        self.pbUnselectAllBehaviors.setText(_translate("Dialog", "Unselect all", None))
        self.pbReverseBehaviorsSelection.setText(_translate("Dialog", "Reverse selection", None))
        self.cbIncludeModifiers.setText(_translate("Dialog", "Include modifiers", None))
        self.cbExcludeBehaviors.setText(_translate("Dialog", "Exclude behaviors without events", None))
        self.rb_full.setText(_translate("Dialog", "Full observation(s)", None))
        self.rb_interval.setText(_translate("Dialog", "Limit to time interval", None))
        self.rb_limit.setText(_translate("Dialog", "Limit to observed events", None))
        self.label.setText(_translate("Dialog", "Time interval", None))
        self.lbStartTime.setText(_translate("Dialog", "Start time", None))
        self.teStartTime.setDisplayFormat(_translate("Dialog", "hh:mm:ss.zzz", None))
        self.lbEndTime.setText(_translate("Dialog", "End time", None))
        self.teEndTime.setDisplayFormat(_translate("Dialog", "hh:mm:ss.zzz", None))
        self.pbCancel.setText(_translate("Dialog", "Cancel", None))
        self.pbOK.setText(_translate("Dialog", "OK", None))

