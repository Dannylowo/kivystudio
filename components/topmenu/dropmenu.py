from kivy.uix.dropdown import DropDown
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from kivystudio.behaviors import HoverBehavior
from kivystudio.widgets.dropdown import DropDownBase

import os
filepath = os.path.dirname(__file__)
Builder.load_file(os.path.join(filepath,'dropmenu.kv'))


class MenuButton(HoverBehavior, ButtonBehavior, BoxLayout):
    pass


class FileTopMenu(DropDownBase):
    
    def __init__(self, **k):
        super(FileTopMenu, self).__init__(**k)

    def open_file(self):
        pass

    def open_folder(self):
        pass
    
    def open_recent(self):
        pass

    def exit_window(self):
        pass

    def save(self):
        pass

    def save_all(self):
        pass

    def save_as(self):
        pass


class EditTopMenu(DropDownBase):
    def __init__(self, **k):
        super(FileTopMenu, self).__init__(**k)

class ViewTopMenu(DropDownBase):
    def __init__(self, **k):
        super(FileTopMenu, self).__init__(**k)

class HelpTopMenu(DropDownBase):
    def __init__(self, **k):
        super(FileTopMenu, self).__init__(**k)
