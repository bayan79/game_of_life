class Cell:
    def __init__(self, fill_value='*', empty_value=' '):
        self._fill_value = fill_value
        self._empty_value = empty_value
        self.empty = True

    @property
    def filled(self):
        return not self.empty

    def change(self):
        self.empty = not self.empty

    def __str__(self):
        return self._empty_value if self.empty else self._fill_value

    def __repr__(self):
        return str(self)


class Row(list):

    def __str__(self):
        return ''.join(str(i) for i in self)

    def __repr__(self):
        return str(self)

    def _to_change(self):
        output = []
        for i, _ in enumerate(self):
            if 0 < i < len(self) - 1:
                #             текущее состояние
                #       левый сосед   |   правый сосед
                #                   \ | /
                #                    |||
                #                    111 110 101 100 011 010 001 000  начальное сосотояние
                # правило 50 (110010) 0   0   1   1   0   0   1   0   следующее состояние
                # правило 18 (10010)  0   0   0   1   0   0   1   0   следующее состояние (реализовано)
                # правило 30 (11110)  0   0   0   1   1   1   1   0   следующее состояние
                if self[i].empty:
                    if self[i - 1].filled | self[i + 1].filled:
                        output.append(i)
                else:
                    output.append(i)
        return output

    def change_all(self):
        to_change = self._to_change()
        for i, _ in enumerate(self):
            if i in to_change:
                self[i].change()


def main():
    center = 32
    r = Row(Cell() for _ in range(2 * center + 1))
    r[center].change()

    for _ in range(center):
        print(r)
        r.change_all()


if __name__ == '__main__':
    main()
