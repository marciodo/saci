from os import path
from pydm import Display
from PyQt4 import QtCore, QtGui
from pydm.widgets.embedded_display import PyDMEmbeddedDisplay
from pydm.widgets.related_display_button import PyDMRelatedDisplayButton
from pydm.widgets.label import PyDMLabel
import json

class MyDisplay(Display):
    def __init__(self, parent=None, args=[]):
        super(MyDisplay, self).__init__(parent=parent, args=args)
        self.ui.setFixedSize(1000, 600)
        self.filenames = ['Network', 'Event']

        self.button_group = QButtonGroup(self)
        for (i, filename) in enumerate(self.filenames):
            button = QPushButton(self)
            self.layout.addWidget(button)
            self.button_group.addButton(button, i)
            self.button_group.buttonClicked[int].connect(self.switch_filename)

    @pyqtSlot(int)
    def switch_filename(self, id):
        self.embedded_display.filename = self.filenames[id]
       
    def ui_filename(self):
        return 'ntwk_main.ui'

    def ui_filepath(self):
         return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())


intelclass = MyDisplay
