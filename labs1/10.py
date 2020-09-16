import math
a, b = map(int, input().split())
print("Sum:", a+b, "\nDif b - a:", b-a, "\nProduct:", a*b, "\nQuotient:", a/b,
      "\nReminder:", a % b, "\nlog10 of a:", math.log10(a), "\nConcatenation:", str(a)+str(b))
