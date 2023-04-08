from .base import BaseElement


class Button(BaseElement):

    def click(self):
        self.find_element().click()
