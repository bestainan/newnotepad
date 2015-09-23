# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore
class main(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        win = QtGui.QWidget()
        #win.resize(200,200)
        #win.move(0,0)
        self.setGeometry(300, 300, 500, 500)
        self.move(0,0)
        self.setWindowTitle(u'第一个窗口')
        self.setWindowIcon(QtGui.QIcon('icon/13146314.jpg'))
        self.setToolTip('This is a <b>QWidget</b> widget')
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))


if __name__ =='__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    main = main()
    main.show()
    sys.exit(app.exec_())