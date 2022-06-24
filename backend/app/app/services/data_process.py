from functools import reduce

from sqlalchemy.orm import Session

from app import crud


def get_order_prices(db: Session):
    """
    Task 1
    Right now the orders.csv doesn't have total order cost information.
    We need to use the data in these files to emit an order_prices.csv file with the following columns:
    id the numeric id of the order
    euros the total cost of the order
    """
    prices_cache = {}
    order_prices = []

    products = crud.product.get_multi(db=db)
    orders = crud.order.get_multi(db=db)

    for product in products:
        prices_cache[str(product.id)] = product.cost

    for order in orders:
        order_prices.append(
            {'id': order.id,
             'euros': reduce(lambda a, b: a + b,
                             list(prices_cache[product_id] for product_id in order.products.split()))
             }
        )

    return order_prices


def get_product_customers(db: Session):
    """
    Task 2
    The marketing department wants to know which customers are interested in each product;
    they've asked for a product_customers.csv file that, for each product, gives the list of
    customers who have purchased this product:

    id the numeric product id
    customer_ids a space-separated list of customer ids of the customers who have purchased this product
    """
    product_customers = {}

    products = crud.product.get_multi(db=db)
    orders = crud.order.get_multi(db=db)

    for product in products:
        product_customers[str(product.id)] = set()

    for order in orders:
        list(map(lambda product__id: product_customers[str(product__id)].add(str(order.customer)),
                 order.products.split()))

    result = []
    for product_id in product_customers.keys():
        result.append({
            'id': product_id,
            'customer_ids': ' '.join(product_customers[str(product_id)])
        })

    return result


def get_customer_ranking(db: Session):
    """
    Task 3
    To evaluate our customers, we need a customer_ranking.csv containing the following columns, ranked in descending order by total_euros:

    id numeric id of the customer
    firstname customer first name
    lastname customer last name
    total_euros total euros this customer has spent on products
    """
    prices_cache = {}
    customer_ranking = {}

    customers = crud.customer.get_multi(db=db)
    orders = crud.order.get_multi(db=db)
    products = crud.product.get_multi(db=db)

    for product in products:
        prices_cache[str(product.id)] = product.cost

    for order in orders:
        if order.customer not in customer_ranking.keys():
            customer = filter(lambda cust: (cust.id == order.customer), customers).__next__()

            customer_ranking[order.customer] = {
                'id': customer.id,
                'firstname': customer.firstname,
                'lastname': customer.lastname,
                'total_euros': 0
            }
        customer_ranking[order.customer]['total_euros'] += (
            reduce(lambda a, b: a + b, list(prices_cache[product_id] for product_id in order.products.split())))

    return sorted(list(customer_ranking.values()), key=lambda customer_rank: customer_rank['total_euros'], reverse=True)
