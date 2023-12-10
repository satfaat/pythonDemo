from syntax.math.calc import Calculate


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

calc = Calculate(num1, num2)

print(f'Yor answer is {calc.add()}')
