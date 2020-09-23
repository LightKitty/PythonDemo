import time
ticks = time.time()
print "ticks: ", ticks

localtime = time.localtime(time.time())
print "local time is ", localtime

import math

content = dir(math)

print content

print locals()

reload(math)