"""
$ python3 02_decorators_run_at_import_time.py
running register(<function f1 at 0x7efddea730d0>)
running register(<function f2 at 0x7efddea738c8>)
running main()
registry -> [<function f1 at 0x7efddea730d0>, <function f2 at 0x7efddea738c8>]
running f1()
running f2()
running f3()

if when import this module, output will be 
running register(<function f1 at 0x10063b1e0>) 
running register(<function f2 at 0x10063b268>)
and this module.registry will be
[<function f1 at 0x10063b1e0>, <function f2 at 0x10063b268>]
"""
registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()
