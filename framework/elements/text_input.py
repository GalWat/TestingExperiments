from .base import BaseElement


class TextInput(BaseElement):

    def send_keys(self, *values):
        self.find_element().send_keys(values)
