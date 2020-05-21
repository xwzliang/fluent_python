promos = []


def promotion(promo_func):
    # promotion decorator returns promo_func unchanged, after adding it to the promos list.
    promos.append(promo_func)
    return promo_func


# Any function decorated by @promotion will be added to promos.
@promotion
def fidelity(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


def best_promo(
    order,
):  # No changes needed to best_promos, because it relies on the promos list.
    """Select best discount available"""
    return max(promo(order) for promo in promos)


# This solution has several advantages:
# The promotion strategy functions don't have to use special names (i.e., they don't need to use the _promo suffix).
# The @promotion decorator highlights the purpose of the decorated function, and also makes it easy to temporarily disable a promotion: just comment out the decorator.
# Promotional discount strategies may be defined in other modules, anywhere in the system, as long as the @promotion decorator is applied to them.
