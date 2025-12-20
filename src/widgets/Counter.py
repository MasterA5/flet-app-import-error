from flet import *

class Counter(Container):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.content = Text(str(self.count), size=50, color=Colors.WHITE)

    def add_count(self, e):
        self.count += 1
        self.content.value = str(self.count)
        self.update()