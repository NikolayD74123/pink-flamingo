# -*- coding: utf-8 -*-

# Прохоренок Python 3 и PyQ  глава 19 
#  листинг 19.2 (1.2)
# =====================================================================

from PyQt4 import QtCore, QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setWindowTitle(u'Первая программа на PyQt -    PyQt ')
window.resize(300, 70)
label = QtGui.QLabel(u"<center>'Привет, мир!'</center>")

btnQuit = QtGui.QPushButton(u'&Закрыть окно')
vbox = QtGui.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window.setLayout(vbox)
QtCore.QObject.connect(btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))



window.show()
sys.exit(app.exec_())

















