mammals = {
    'лошадь',
    'кит',
    'тигр',
    'слон',
    'морж',
}
aquatic = {
    'креветка',
    'кальмар',
    'морж',
    'осьминог',
    'кит',
}

# >>> mammals | aquatic
# {'кит', 'слон', 'тигр', 'морж', 'лошадь', 'осьминог', 'креветка', 'кальмар'}
# >>>
# >>> mammals & aquatic
# {'кит', 'морж'}
# >>>
# >>> mammals - aquatic
# {'слон', 'тигр', 'лошадь'}
# >>>
# >>> aquatic - mammals
# {'креветка', 'кальмар', 'осьминог'}
# >>>
# >>> mammals ^ aquatic
# {'слон', 'тигр', 'осьминог', 'креветка', 'кальмар', 'лошадь'}
# >>>
# >>> (mammals | aquatic) - (mammals & aquatic)
# {'слон', 'тигр', 'лошадь', 'осьминог', 'креветка', 'кальмар'}
# >>> 
# >>> mammals.isdisjoint(aquatic)
# False

reptiles = {
    'змея',
    'черепаха',
    'варан',
    'полоз',
}

# >>> reptiles.isdisjoint(mammals)
# True
# >>>
# >>> mammals.isdisjoint(reptiles)
# True

