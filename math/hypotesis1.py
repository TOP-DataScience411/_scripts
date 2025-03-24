from numpy import array


tension = array([227, 258, 271, 288, 292, 301, 322, 331, 372, 413])
capacity = array([371, 379, 388, 396, 395, 406, 460, 408, 409, 411, 419, 424, 441, 397])
lifetime = array([312, 329, 248, 321, 418, 267, 193, 375, 358])

alpha = 0.05

r_stat_crit_tension = 2.294
r_stat_crit_capacity = 2.461

r_stat_obs_tension_min = (
    abs(tension.min() - tension.mean()) 
  / 
    (tension.std() * (9/10)**0.5)
)
r_stat_obs_tension_max = (
    abs(tension.max() - tension.mean()) 
  / 
    (tension.std() * (9/10)**0.5)
)
r_stat_obs_capacity_min = (
    abs(capacity.min() - capacity.mean()) 
  / 
    (capacity.std() * (13/14)**0.5)
)
r_stat_obs_capacity_max = (
    abs(capacity.max() - capacity.mean()) 
  / 
    (capacity.std() * (13/14)**0.5)
)

print(
    f'минимальный элемент {tension.min()} ряда нагрузки '
    f'{"является" if r_stat_obs_tension_min < r_stat_crit_tension else "не является"} '
    f'элементом генеральной совокупности'
)
print(
    f'максимальный элемент {tension.min()} ряда нагрузки '
    f'{"является" if r_stat_obs_tension_max < r_stat_crit_tension else "не является"} '
    f'элементом генеральной совокупности'
)
print(
    f'минимальный элемент {capacity.min()} ряда несущей способности '
    f'{"является" if r_stat_obs_capacity_min < r_stat_crit_capacity else "не является"} '
    f'элементом генеральной совокупности'
)
print(
    f'максимальный элемент {capacity.min()} ряда несущей способности '
    f'{"является" if r_stat_obs_capacity_max < r_stat_crit_capacity else "не является"} '
    f'элементом генеральной совокупности'
)


f_stat_crit = 2.83

f_stat_obs = (
    capacity.var() / tension.var() 
    if tension.var() < capacity.var() else 
    tension.var() / capacity.var()
)

print(
    f'дисперсия нагрузки в генеральной совокупности '
    f'{"равна" if f_stat_obs <= f_stat_crit else "не равна"} '
    f'дисперсии несущей способности в генеральной совокупности'
)

