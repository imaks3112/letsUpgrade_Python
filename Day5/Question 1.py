data = [
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 2, 1, 1, 5, 0, 0, 0, 0],
     [0, 0, 2, 1, 1, 2, 2, 0, 0, 1],
     [0, 0, 1, 2, 2, 0, 1, 0, 0, 2],
     [1, 0, 1, 1, 1, 2, 1, 0, 2, 1],
]

pattern = '115'

for item in data:
    line = ''
    for number in item:
        line += str(number)
    if pattern in line:
        print (" it's a match: %s" % item)
    else:
         print (" it's Gone: %s" % item)