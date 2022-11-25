def scope_demo():
    def do_local():
        def do_inner():
            nonlocal spam
            spam = 'inner'
        spam = 'local scope'
        do_inner()
        print(f'inner spam: {spam}')

    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal scope'

    def do_global():
        global spam
        spam = 'global scope'

    spam = 'test'
    do_local()
    print(f'local spam: {spam}')
    do_nonlocal()
    print(f'nonlocal spam: {spam}')
    do_global()
    print(f'global spam: {spam}')


scope_demo()
print(f'global spam(outside): {spam}')
