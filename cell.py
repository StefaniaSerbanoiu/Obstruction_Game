class Cell:
    def __init__(self):
        self._is_free = True
        self._is_o = False
        self._is_x = False
        self._blocked = False
        self._content = " "

    @property
    def is_free(self):
        return self._is_free

    @property
    def is_o(self):
        return self._is_o

    @property
    def is_x(self):
        return self._is_x

    @property
    def content(self):
        return self._content

    @property
    def blocked(self):
        return self._blocked

    @is_free.setter
    def is_free(self, value):
        self._is_free = value

    @is_o.setter
    def is_o(self, value):
        self._is_o = value

    @is_x.setter
    def is_x(self, value):
        self._is_x = value

    @content.setter
    def content(self, value):
        self._content = value

    @blocked.setter
    def blocked(self, value):
        self._blocked = value

    def __str__(self):
        if self.is_free:
            return ' '
        elif self.is_x is True:
            return 'X'
        elif self.blocked is True:
            return "-"
        else:
            return 'O'
