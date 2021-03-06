try:
    object().__dict__ = 1
except AttributeError as e:
    print e

class C(object):
    pass

c1 = C()
c2 = C()

c1.a = 2
c1.b = 3
c2.a = 4
c2.b = 5

def p():
    print sorted(c1.__dict__.items()), sorted(c2.__dict__.items())

p()

c1.__dict__ = c2.__dict__
p()

c1.a = 6
c2.b = 7
p()

print c1.a, c1.b, c2.a, c2.b
del c1.a
try:
    del c1.a
except AttributeError as e:
    # the error message CPython gives here is just "a" which I don't think we should copy.
    print "caught AttributeError"
p()

c1.__dict__ = d = {}
d['i'] = 5
p()
