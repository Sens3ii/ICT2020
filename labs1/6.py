a = int(input())
tax = float(a/10)
tip = float(a*0.18)
overall = a + tax + tip
print("Tax:", f'{tax:.2f}')
print("Tip:", f'{tip:.2f}')
print("Overall:", f'{overall:.2f}')
