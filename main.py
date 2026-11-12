products = [
    {"name": "Ноутбук", "price": 85000, "stock": 4},
    {"name": "Мышь", "price": 2500, "stock": 15},
    {"name": "Монитор", "price": 32000, "stock": 0},
    {"name": "Клавиатура", "price": 7000, "stock": 8},
]

Product = dict[str, str | int]


def show_products(products):
    for product in products:
        print(
        f"{product['name']} — "
        f"{product['price']} руб. — "
        f"{product['stock']} шт."
    )


def search_products(products: list[Product], query: str) -> list[Product]:
    return [
        product
        for product in products
        if query.lower() in product["name"].lower()
    ]


if __name__ == "__main__":
    show_products(products)
