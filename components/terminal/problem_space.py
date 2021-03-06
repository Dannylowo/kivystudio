from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

class ProblemSpace(BoxLayout):
    
    text = StringProperty('Hello '*39)

Builder.load_string('''
<ProblemSpace>:
    ScrollView:
        Label:
            text: root.text
            text_size: self.width, None
            size_hint_y: None
            height: self.texture_size[1]
            valign: 'top'
            halign: 'right'

''')