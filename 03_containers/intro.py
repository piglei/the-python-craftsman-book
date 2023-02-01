class Foo:
    def __init__(self, value):
        self.value = value


foo = Foo('bar')
print(foo.__dict__, type(foo.__dict__))


names = ('foo', 'bar')
names[1] = 'x'
