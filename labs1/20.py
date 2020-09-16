R = 8.314
P = float(input())
V = float(input())
T = float(input())
n = float((P*(V/1000))/(R*(T+273.15)))
print(f'{n:.2f}', "moles")
