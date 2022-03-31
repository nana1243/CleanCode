class NumberSequence:
    """아래는 오류가 남.
    >>>list(zip(NumberSequence(10))).
    The problem lies in the fact that
    NumberSequence does not support iteration.
    이를 지원하기 위해서는 __iter__를 사용해야한다.
    """

    def __init__(self, start=0):
        self.current = start

    def next(self):
        current = self.current
        self.current += 1
        return current

    def __iter__(self):
        return self


seq = NumberSequence()
t1 = seq.next()
t2 = seq.next()
print(t1, t2)
