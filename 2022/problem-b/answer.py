num = int(input())

ways = 0

dict = {}

for _ in range(num):
  a = "".join(sorted(input()))
  if a in dict:
    dict[a] += 1
  else:
    dict[a] = 1
  
for key in dict:
  if dict[key] > 1:
    ways += dict[key] * (dict[key] - 1) / 2

print(int(ways))
