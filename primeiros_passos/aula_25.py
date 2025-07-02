"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
<- Contagem de complexidade (ruim)
"""

speed_car = 61  # Velocidade do carro
car_location = 100  # Local que o carro está na estrada

# Constantes
RADAR_1 = 60  # Velocidade máxima do radar 1
LOCATION_1 = 100  # Local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

speed_is_in_interval = speed_car > RADAR_1
is_in_range_x_right = car_location + RADAR_RANGE >= LOCATION_1
is_in_range_x_left = car_location - RADAR_RANGE <= LOCATION_1
is_illegal_speed = speed_car > RADAR_1
is_illegal = is_in_range_x_left and is_in_range_x_right and is_illegal_speed

if speed_is_in_interval:
    print("Carro passou da velocidade do RADAR_1")
if is_illegal:
    print("Carro multado em RADAR_1")
