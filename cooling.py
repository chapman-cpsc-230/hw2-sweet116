T = float(input('enter the temperature of tea'))

T_a= float(input('enter the ambient air temperature'))

k = 0.055

rateofcooling = -k * (T - T_a)

print('The rate of cooling is', rateofcooling, 'degrees per minute')
