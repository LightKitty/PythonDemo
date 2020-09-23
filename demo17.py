fo = open("foo.txt","r+")
print "File name: ", fo.name
print "Is closed: ", fo.closed
print "Mode: ", fo.mode
print "Softspace: ", fo.softspace
str = fo.read(10)
print "str: ",str
fo.write("Nice to meet you!")
fo.close()