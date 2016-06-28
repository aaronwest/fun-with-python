import sys
import getopt

__author__ = "Aaron S. West"

def usage():
    print sys.argv[0]
    usage = """
    Required parameters:
    -s              : the start number
    -e              : the end number
    """
    print 'usage: ' + sys.argv[0] + ' -s <integer> -e <integer>'
    print usage

def main(argv):
    startNumber = 0
    endNumber = 0

   # Test input args.
    try:
      opts, args = getopt.getopt(argv,"hs:e:",["help"])
    except getopt.GetoptError:
       usage()
       sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-s':
            startNumber = int(arg)
        elif opt == '-e':
            endNumber = int(arg)

    # Ensure iteration count. Exit with an appropriate message if not.
    if startNumber == 0 or endNumber == 0:
        sys.exit("Start and end number (-s, -e) are required. See 'python " + sys.argv[0] + " -h'")

    for i in fib_generator(startNumber, endNumber):
        print i

def F():
    # print "F start"
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

def fib_generator(startNumber, endNumber):
    for cur in F():
        # print "SubFib " + str(cur)
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur

if __name__ == "__main__":
    main(sys.argv[1:])
