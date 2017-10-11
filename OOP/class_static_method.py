__author__ = 'narendra'

class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):

        print "executing static_foo(%s)"%x

class B(object):
    def ss(self):
        print "sss"
a=A()
print a
print A
a.foo(1)
A().foo(1)
a.class_foo(1)
A.class_foo(1)

a.static_foo(1)
A.static_foo('hi')

print a.foo
print a.class_foo
print a.static_foo

b = B()
A.foo(a,2)
# A.foo(b,3)

A.class_foo(b)