def divide(a, b):
   if b == 0:
      raise ValueError('На ноль делить нельзя')
   return a / b


def modulo(a, b):
   if b == 0:
      raise ValueError('На ноль делить нельзя')
   return a % b
