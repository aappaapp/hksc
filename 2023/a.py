i = input()

a, b = i.split(" ")
num = 0
for x in range(int(a), int(b) + 1):
  s = (str(x))
  if s == s[::-1]:
    num += 1

print(num)
