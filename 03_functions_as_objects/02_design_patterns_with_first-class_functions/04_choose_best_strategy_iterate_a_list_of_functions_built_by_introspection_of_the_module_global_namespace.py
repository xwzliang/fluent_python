# Although previous example works and is easy to read, there is some duplication that could lead to a subtle bug: to add a new promotion strategy, we need to code the function and remember to add it to the promos list, or else the new promotion will work when explicitly passed as an argument to Order, but will not be considered by best_promotion.

# This example is a somewhat hackish way of using globals to help best_promo automatically find the other available *_promo functions.

moduleName = "02_commercial_order_class_with_discount_strategies_implemented_as_functions"
# Import all from module except __name__
module = __import__(moduleName, globals(), locals(), ['*'])
for k in dir(module):
    if k != '__name__':
        locals()[k] = getattr(module, k)


promos = [globals()[name] for name in globals()
        if name.endswith('_promo')
        and name != 'best_promo']

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
