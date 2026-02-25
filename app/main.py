from fastapi import FastAPI, HTTPException
from app.database import users_collection, products_collection
from app.schemas import UserCreate, UserResponse, ProductCreate, ProductResponse

app = FastAPI(title="Atlas User & Product API")

# ================= USERS =================

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):

    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    users_collection.insert_one(user.dict())
    return user


@app.get("/users/{email}", response_model=UserResponse)
def get_user(email: str):

    user = users_collection.find_one({"email": email}, {"_id": 0})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# ================= PRODUCTS =================

@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate):

    if products_collection.find_one({"sku": product.sku}):
        raise HTTPException(status_code=400, detail="SKU already exists")

    products_collection.insert_one(product.dict())
    return product


@app.get("/products/{sku}", response_model=ProductResponse)
def get_product(sku: str):

    product = products_collection.find_one({"sku": sku}, {"_id": 0})

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product