fruits = ['banana','apple','mango']
for index in range(len(fruits)):
    print 'fruit now is: ',fruits[index]

for fruit in fruits:
    print fruit

for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j=num/i
            print '%d 等于 %d * %d' % (num,i,j)
            break
    else:
        print num, '是一个质数'

for letter in 'Python':
    if letter == 'h':
        pass
        continue
    print letter

var = 10
while var >0:
    var = var -1
    if var == 5:
        continue
    print var

print "Good bye!"