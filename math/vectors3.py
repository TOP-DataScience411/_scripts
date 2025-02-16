from numpy import array, dot


t = array([3.2, 4.4])
r = array([9.1, 3])

beta = dot(t, r) / dot(r, r)

t_coll_r = (beta * r).round(1)
t_orth_r = t - t_coll_r

# >>> t_coll_r
# array([4.2, 1.4])
# >>>
# >>> t_orth_r
# array([-1.,  3.])

# >>> dot(t_coll_r, t_orth_r)
# np.float64(0.0)

