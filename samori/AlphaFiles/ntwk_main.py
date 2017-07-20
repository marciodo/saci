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
        self.ui.pushButton.clicked.connect(self.button_pushed)

    def button_pushed(self):
        self.ui.PyDMEmbeddedDisplay.filename = 'ntwk_sector.py'
            
    def ui_filename(self):
        return 'ntwk_main.ui'

    def ui_filepath(self):
         return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())


intelclass = MyDisplay
