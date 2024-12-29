from datetime import date, datetime as dt, timedelta as td


class Product:
    default_date_format = '%d.%m.%Y'
    
    def __init__(self, name, produced, expiration_days):
        self.name = name
        self.produced = dt.strptime(produced, self.default_date_format).date()
        self.expired = self.produced + td(days=expiration_days)
    
    # self < other -> self.__lt__(other)
    def __lt__(self, other):
        if type(other) is date:
            return self.produced < other
        elif type(other) is self.__class__:
            return self.produced < other.produced
        else:
            raise TypeError
    
    def is_expired(self):
        return dt.now().date() >= self.expired
    
    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name!r}, {self.produced:{self.default_date_format}}–{self.expired:{self.default_date_format}}>'
    
    def __str__(self):
        return self.name


class Fridge(list):
    def __init__(self, products):
        self.extend(products)
    
    def clear_expired(self):
        expired = []
        for product in self:
            if product.is_expired():
                expired.append(product)
        for product in expired:
            self.remove(product)


products = [
    Product('мясо', '19.12.2024', 2),
    Product('яйца', '14.12.2024', 30),
    Product('огурцы солёные', '14.09.2024', 365),
    Product('картофель', '21.11.2024', 16),
]

fridge = Fridge(products)

# >>> fridge
# [<Product: 'мясо', 19.12.2024–21.12.2024>, <Product: 'яйца', 14.12.2024–13.01.2025>, <Product: 'огурцы солёные', 14.09.2024–14.09.2025>, <Product: 'картофель', 21.11.2024–07.12.2024>]
# >>>
# >>> print(*fridge, sep='\n')
# мясо
# яйца
# огурцы солёные
# картофель
# >>>
# >>>
# >>> fridge.clear_expired()
# >>>
# >>> fridge
# [<Product: 'яйца', 14.12.2024–13.01.2025>, <Product: 'огурцы солёные', 14.09.2024–14.09.2025>]
# >>>
# >>> print(*fridge, sep='\n')
# яйца
# огурцы солёные

