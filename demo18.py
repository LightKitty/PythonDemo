try:
    fh = open("testfile","w")
    fh.write("This is a test file")
except IOError:
    print "IOError"
else:
    print "success"
    fh.close()