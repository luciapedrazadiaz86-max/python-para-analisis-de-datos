# variables
a_0 = 0.15        # absortividad de onda corta de la capa [adim, 0-1]
alpha_c = 0.08    # albedo de la capa [adim, 0-1]
alpha_g = 0.10    # albedo de la superficie [adim, 0-1]
epsilon = 0.4     # emisividad de la capa en onda larga [adim, 0-1]
sigma = 5.67e-8   # constante de Stefan-Boltzmann [W m^-2 K^-4]
S = 343           # flujo solar medio incidente [W m^-2]

# temperatura de la superficie
num1 = S*(1-alpha_c)*(2-a_0)*(1-alpha_g*(1-a_0))
T_g4 = num1/(sigma*(2-epsilon)) 
T_g = T_g4**(1/4)

# temperatura de la capa
num2 = (1-alpha_g)*(1-a_0)*(1-alpha_c)*S
T_c4 = (1/epsilon)*(T_g4 - num2/sigma)
T_c = T_c4**(1/4)

print(f'T_g:{T_g:.2f} K')
print(f'T_c:{T_c:.2f} K')

