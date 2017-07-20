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
        json_data = self.jsonFile()
        self.ui.setFixedSize(1000, 600)
        name_list = []
        for i in enumerate(json_data):
            device_name = i[1]["Subsystem"]
            name_list += [device_name]

        name_set = []
        for name in name_list:
            if name not in name_set:
                name_set += [name]

        for name in name_set:
            device_label = QtGui.QPushButton(name, self)
            self.ui.verticalLayout.addWidget(device_label)
        

    def ui_filename(self):
        return 'sector.ui'

    def ui_filepath(self):
         return path.join(path.dirname(path.realpath(__file__)), self.ui_filename())


    def jsonFile(self):
        filename = "ntwk_JSON.json"
        if not path.isabs(filename):
            filename = path.join(path.dirname(__file__), filename)
        with open(filename) as file:
            obj = json.load(file)
        return obj

    
    

intelclass = MyDisplay
