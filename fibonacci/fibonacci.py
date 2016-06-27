import sys
import getopt

__author__ = "Aaron S. West"

def usage():
    print sys.argv[0]
    usage = """
    Required parameters:
    -n              : the number of Fibonacci numbers to generate
    """
    print 'usage: ' + sys.argv[0] + ' -n <integer>'
    print usage

def main(argv):
    iterations = 0

   # Test input args.
    try:
      opts, args = getopt.getopt(argv,"hn:",["help"])
    except getopt.GetoptError:
       usage()
       sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-n':
            iterations = int(arg)

    # Ensure iteration count. Exit with an appropriate message if not.
    if iterations == 0:
        sys.exit("Iteration count (-n) is required. See 'python " + sys.argv[0] + " -h'")

    fib_generator(iterations)

def fib_generator(cnt):
    seq = []
    seq.append(0)
    seq.append(1)

    while len(seq)<cnt:
        seq.append(seq[len(seq)-1] + seq[len(seq)-2])

    fibfile = open("fib.txt", "w")
    fibfile.writelines(str(seq))
    fibfile.close()
    #print seq

if __name__ == "__main__":
    main(sys.argv[1:])
