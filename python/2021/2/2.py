with open("input.txt", 'r') as f:
    a = [i.rstrip() for i in f.readlines()]


def p1():
  forward = 0 
  down = 0
  for line in a:
      cmd, num = line.split()
      num = int(num)
      if cmd == "forward":
          forward += num
      elif cmd=="down":
          down += num
      elif cmd == 'up':
          down -= num
      else:
          raise ValueError
  return down*forward


def p2():
    forward = 0
    down = 0
    aim = 0
    for line in a:
        cmd, num = line.split()
        num = int(num)
        if cmd == "down":
            aim+= num
        elif cmd =="up":
            aim-=num
        elif cmd == "forward":
            forward += num
            down += aim*num
    return down*forward


print(1, p1())
print(2, p2())

