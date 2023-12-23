# main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # Basic data (model) example - list of names
        self.names = ["Alice", "Bob", "Charlie", "David"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # Create a label for each name
            temp_label = Label(text=name)
            # Add the label to the "labels_box" layout widget
            self.root.ids.labels_box.add_widget(temp_label)


DynamicLabelsApp().run()
