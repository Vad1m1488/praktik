print('Введите число от 1 до 100')
i = int(input())
if 1 <= i <= 100:
   if not i%6 and not i%10:
       print("Fizz Buzz")
   elif not i%6:
       print("Fizz")
   elif not i%10:
       print("Buzz")