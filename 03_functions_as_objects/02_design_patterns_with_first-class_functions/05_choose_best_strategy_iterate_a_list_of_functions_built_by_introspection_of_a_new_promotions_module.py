import inspect

moduleName = "02_commercial_order_class_with_discount_strategies_implemented_as_functions"
promotions = __import__(moduleName)
for k in dir(promotions):
    if k != '__name__':
        locals()[k] = getattr(promotions, k)


promos = [func for name, func in
        inspect.getmembers(promotions, inspect.isfunction) if name!='namedtuple']
# print(promos)
# for name, func in inspect.getmembers(promotions, inspect.isfunction):
    # print(name, func)

def best_promo(order):
    """Select best discount available"""
    return max(promo(order) for promo in promos)


class test_best_promo:
    """
    >>> joe = Customer('John Doe', 0)
    >>> ann = Customer('Ann Smith', 1100)
    >>> cart = [LineItem('banana', 4, .5),
    ... 	    LineItem('apple', 10, 1.5),
    ... 	    LineItem('watermellon', 5, 5.0)]
    >>> Order(joe, cart, fidelity_promo)
    <Order total: 42.00 due: 42.00>
    >>> Order(ann, cart, fidelity_promo)
    <Order total: 42.00 due: 39.90>
    >>> banana_cart = [LineItem('banana', 30, .5), 
    ... 		   LineItem('apple', 10, 1.5)]
    >>> Order(joe, banana_cart, bulk_item_promo)
    <Order total: 30.00 due: 28.50>
    >>> long_order = [LineItem(str(item_code), 1, 1.0)
    ... 		  for item_code in range(10)]
    >>> Order(joe, long_order, large_order_promo)
    <Order total: 10.00 due: 9.30>

    test for best_promo
    >>> Order(joe, cart, large_order_promo)
    <Order total: 42.00 due: 42.00>
    >>> Order(joe, long_order, best_promo)
    <Order total: 10.00 due: 9.30>
    >>> Order(joe, banana_cart, best_promo)
    <Order total: 30.00 due: 28.50>
    >>> Order(ann, cart, best_promo)
    <Order total: 42.00 due: 39.90>
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
