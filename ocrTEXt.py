import easyocr

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView


class OCRPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Extracted Text"

    def set_text(self, text):
        self.content = Label(text=text)


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        # File chooser widget
        self.file_chooser = FileChooserIconView()
        self.add_widget(self.file_chooser)

        # Button to trigger OCR
        self.ocr_button = Button(text="Extract Text", size_hint_y=0.1)
        self.ocr_button.bind(on_press=self.do_ocr)
        self.add_widget(self.ocr_button)

        # OCR Popup
        self.ocr_popup = OCRPopup()

    def do_ocr(self, instance):
        # Get selected image file
        filename = self.file_chooser.selection[0]
        print("filename:",filename)

        # Perform OCR
        try:
            reader = easyocr.Reader(['en'])
            result = reader.readtext(filename)
            print("result:::",result)
            text = "\n".join([r[1] for r in result])
        except Exception as e:
            text = str(e)

        # Display result in popup
        self.ocr_popup.set_text(text)
        self.ocr_popup.open()


class OCRApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    OCRApp().run()
