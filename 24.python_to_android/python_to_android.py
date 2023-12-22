from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class MainApp(App):
    """
    MainApp is the entry point of the Kivy application.
    It inherits from App and overrides the build method.
    """

    def build(self):
        """
        Builds the UI components of the app.
        It creates a vertical BoxLayout with a label and a button.

        Returns:
            The root widget of the app, in this case, a BoxLayout.
        """

        # Set the background color of the app to #89CFF0
        Window.clearcolor = get_color_from_hex('#89CFF0')

        # Set the background color similar to the Tkinter app
        self.root_widget = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.root_widget.bg_color = get_color_from_hex('#F4C2C2')

        # Create a Label widget with blue color
        self.label = Label(text='Hello World!',
                           size_hint=(.5, .5),
                           pos_hint={'center_x': .5, 'center_y': .5},
                           color=get_color_from_hex('#FFFFFF'),  
                           font_size='20sp',  # Adjust the font size as needed
                           bold=True)  # Make the text bold

        # Create a horizontal BoxLayout for centering the button
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

        # Create a Button widget with smaller size and green color
        button = Button(text='Click Me', 
                        size_hint=(None, None), 
                        size=(100, 50), 
                        background_color=get_color_from_hex('#89CFF0'),  # Green color in hexadecimal
                        color=get_color_from_hex('#FFFFFF'))  # White text color
        button.bind(on_press=self.on_button_press)

        # Add the button to the button_layout, centering it horizontally
        button_layout.add_widget(Label())  # Spacer
        button_layout.add_widget(button)
        button_layout.add_widget(Label())  # Spacer

        # Add the label and button layout to the main layout
        self.root_widget.add_widget(self.label)
        self.root_widget.add_widget(button_layout)

        return self.root_widget

    def on_button_press(self, instance):
        """
        Callback method for button press event.
        It changes the text of the label.

        Args:
            instance: The instance of the widget that triggered the event.
        """
        self.label.text = 'Button Pressed!'

if __name__ == '__main__':
    app = MainApp()
    app.run()
