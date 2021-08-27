class human:
    def walk(self):
        print('walk')

class doctor(human):
    def heal(self):
        print('heal')

class builder(human):
    def build(self):
        print('build')


d = doctor()
d.heal()
d.walk()
b = builder()
b.walk()
b.build()