with open("input.txt", 'r') as f:
  a = [i.rstrip() for i in f.readlines()]


def p1():
  linecount = len(a)
  counts = [0]*len(a[0])
  for line in a:
    for j in range(len(line)):
      counts[j] += int(line[j])
  epsilon = ''
  gamma = ''
  for i in counts:
      if i/linecount > 0.5:
          gamma += '1'
          epsilon += '0'
      elif i/linecount < 0.5:
          gamma +='0'
          epsilon += '1'
  return int(gamma, 2)*int(epsilon,2)


def p2():
  linecount = len(a)
  b = a.copy()

  
print(1, p1())
print(2, p2())

