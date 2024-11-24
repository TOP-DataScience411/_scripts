def gcd(num1, num2):
    breakpoint()
    if num1 % num2 == 0:
        return num2
    else:
        return gcd(num2, num1 % num2)


# >>> gcd(15, 12)
# 
# > recursion2.py(3) gcd()
#   -> if num1 % num2 == 0:
# 
# (Pdb) args
# num1 = 15
# num2 = 12
# 
# (Pdb) ll
#   1     def gcd(num1, num2):
#   2         breakpoint()
#   3  ->     if num1 % num2 == 0:
#   4             return num1
#   5         else:
#   6             return gcd(num2, num1 % num2)
# 
# (Pdb) num1 % num2
# 3
# 
# (Pdb) step
# 
# > recursion2.py(6) gcd()
#   -> return gcd(num2, num1 % num2)
# 
# (Pdb) step
# 
# --Call--
# > recursion2.py(1) gcd()
#   -> def gcd(num1, num2):
# 
# (Pdb) args
# num1 = 12
# num2 = 3
# 
# (Pdb) step
# 
# > recursion2.py(2) gcd()
#   -> breakpoint()
# 
# (Pdb) next
# 
# > recursion2.py(3) gcd()
#   -> if num1 % num2 == 0:
# 
# (Pdb) num1 % num2
# 0
# 
# (Pdb) step
# 
# > recursion2.py(4) gcd()
#   -> return num1
# 
# (Pdb) num1
# 12
# 
# (Pdb) step
# 
# --Return--
# > recursion2.py(4) gcd()-->12
#   -> return num1
# 
# (Pdb) args
# num1 = 12
# num2 = 3
# 
# (Pdb) step
# 
# --Return--
# > recursion2.py(6) gcd()-->12
#   -> return gcd(num2, num1 % num2)
# 
# (Pdb) args
# num1 = 15
# num2 = 12
# 
# (Pdb) step
# 12
# 
# --Return--
# > <stdin>(1) <module>()-->None
# 
# (Pdb) quit
# bdb.BdbQuit
# >>>


