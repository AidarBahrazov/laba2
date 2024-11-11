def get_number():
 for x in range(30):
  if x % 2 != 0:
   yield x

gen = get_number()

print("Первое значение:", next(gen))
for _ in range(3):
 next(gen)
print("Пятое значение:", next(gen))

y = None
while True:
 try:
  y = next(gen)
 except StopIteration:
  break
print("Последнее значение:", y)
