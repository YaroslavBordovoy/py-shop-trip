from app.customer import Customer
from app.shop import Shop


def buy_products(customer: Customer, shops: list[Shop]) -> list:
    """
    We calculate the cost of all goods separately and their total cost.
    We check whether the number is an integer.
    """
    shops_prices = []

    for i in range(len(shops)):
        milk_price = customer.product_cart["milk"] * shops[i].products["milk"]
        bread_price = (customer.product_cart["bread"]
                       * shops[i].products["bread"])
        butter_price = (customer.product_cart["butter"]
                        * shops[i].products["butter"])

        milk_price = int(milk_price) if milk_price.is_integer() else milk_price
        bread_price = int(bread_price) if bread_price.is_integer() \
            else bread_price
        butter_price = int(butter_price) if butter_price.is_integer() \
            else butter_price

        total_price = milk_price + bread_price + butter_price
        shops_prices.append([milk_price,
                             bread_price,
                             butter_price,
                             total_price])

    return shops_prices
