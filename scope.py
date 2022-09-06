def check_scope():
    def do_local():
        test = "test local"
    def do_non_local():
        nonlocal test
        test = "nonlocal test"
    def do_global():
        global test
        test = "global test"

    test = "outside test"
    do_local()
    print("test value after do local " +test)
    do_non_local()
    print("test value after do non local " + test)
    do_global()
    print("test value after do global " + test)
check_scope()
print("test value after main " + test)