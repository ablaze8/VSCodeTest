class Test:
    def __init__(self):
        self.x = range(36,47)

    def test(self, p):
        return (p, float(p)/float(p-1), (p%2 == 0))

if __name__ == "__main__":
    print "Hello from main!"
    t = Test()
    all = map(t.test, t.x)
    print all
    print sorted(all, key = lambda tup : tup[1])
    print "done"
    print "exiting"

