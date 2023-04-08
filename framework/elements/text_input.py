from .base import BaseElement


class TextInput(BaseElement):

    def fill(self, *values):
        self.find_element().send_keys(values)

    def clear(self):
        self.find_element().clear()

    def clear_and_fill(self, *values):
        self.clear()
        self.fill(*values)
