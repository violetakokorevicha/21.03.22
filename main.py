import cmath 
a = int(ipnut('First number'))
b = int(ipnut('Second number'))
c = int(ipnut('Third number')
d = (b**2) - (4*a*c)
sol1 = (- b - cmath.sqrt(d)) / (2*a)
sol2 = (- b + cmath.sqrt(d)) / (2*a)
print('Solijums ir {0} un {1}'. format(sol1, sol2))
if d > 0:
  print('2 saknes')
if d == 0:
  print(' viena sakne')
if d < 0:
  print('neviena sakne')


