from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "category": "Electronics", "price": 499, "in_stock": True},
    {"id": 2, "name": "Mechanical Keyboard", "category": "Electronics", "price": 2499, "in_stock": True},
    {"id": 3, "name": "Pen Set", "category": "Stationery", "price": 49, "in_stock": True},
    {"id": 4, "name": "Notebook", "category": "Stationery", "price": 120, "in_stock": False},
    {"id": 5, "name": "USB Cable", "category": "Electronics", "price": 199, "in_stock": True},
    {"id": 6, "name": "Water Bottle", "category": "Accessories", "price": 299, "in_stock": True},
    {"id": 7, "name": "Backpack", "category": "Accessories", "price": 999, "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"total": len(products), "products": products}

@app.get("/products/category/{category}")
def get_by_category(category: str):
    return [p for p in products if p["category"].lower() == category.lower()]

@app.get("/products/instock")
def get_instock():
    available = [p for p in products if p["in_stock"]]
    return {"in_stock_products": available, "count": len(available)}

@app.get("/store/summary")
def store_summary():
    total_products = len(products)
    instock = len([p for p in products if p["in_stock"]])
    categories = list(set(p["category"] for p in products))

    return {
        "total_products": total_products,
        "products_in_stock": instock,
        "categories": categories
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    return [p for p in products if keyword.lower() in p["name"].lower()]

@app.get("/products/deals")
def product_deals():
    cheapest = min(products, key=lambda x: x["price"])
    expensive = max(products, key=lambda x: x["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }
