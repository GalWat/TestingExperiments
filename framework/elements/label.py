from .base import BaseElement


class Label(BaseElement):

    @property
    def text(self):
        return self.find_element().text
