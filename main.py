from pymongo import MongoClient
from typing import List
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
import class_Product
import class_User
import class_Cart


# Database connection

app = FastAPI()
CONNECTION_STRING = 'mongodb+srv://denis:1234@cluster0.pl9bfps.mongodb.net/?retryWrites=true&w=majority'
#CONNECTION_STRING = 'mongodb://localhost:27017'
connection = MongoClient(CONNECTION_STRING)
db = connection.onlineshop

# creating of collection

collection = db.products
user_collection = db.users
order_collection = db.orders

# product functions --------------------------------------------------------------------------------------

@app.get('/products')
def get_products():
    products = collection.find()
    return {'products': list(products)}


@app.get('/products/{product_id}')
def get_product_by_ID(product_id: ObjectId):
    product = collection.find_one({'_id': product_id})
    if product:
        return {'product': product}
    else:
        return {'message': 'Product not found'}


@app.post('/products')
def create_product(product: class_Product.Product):
    dict_product = {'id': product.id, 'title': product.title, 'description': product.description, 'price': product.price}
    inserted_product = collection.insert_one(dict_product)
    return {'message': 'Product created', 'product_id': str(inserted_product.inserted_id)}


@app.put('/products/{product_id}')
def update_product(product_id: ObjectId, updated_product: class_Product.Product):
    result = collection.update_one({'_id': product_id}, {'$set': updated_product})
    if result.modified_count == 1:
        return {'message': 'Product updated'}
    else:
        return {'message': 'Product not found'}


@app.delete('/products/{product_id}')
def delete_product(product_id: ObjectId):
    result = collection.delete_one({'_id': product_id})
    if result.deleted_count == 1:
        return {'message': 'Product deleted'}
    else:
        return {'message': 'Product not found'}

# user funktions ---------------------------------------------------------------------------------------------------

@app.get('/users')
def get_users():
    users = user_collection.find()
    return {'users': users}


@app.get('/users/{user_id}')
def get_user_by_ID(user_id: ObjectId):
    user = user_collection.find_one({'_id': user_id})
    if user:
        return {'user': user}
    else:
        return {'message': 'user not found'}


@app.post('/users')
def create_user(user: class_User.User):
    dict_user = {'id': user.id, 'name': user.name, 'email': user.email}
    inserted_user = user_collection.insert_one(dict_user)
    return {'message': 'user created', 'user_id': str(inserted_user.inserted_id)}


@app.put('/users/{user_id}')
def update_user(user_id: ObjectId, updated_user: class_User.User):
    result = user_collection.update_one({'id': user_id}, {'$set': updated_user})
    if result.modified_count == 1:
        return {'message': 'user updated'}
    else:
        return {'message': 'user not found'}


@app.delete('/users/{user_id}')
def delete_user(user_id: ObjectId):
    result = user_collection.delete_one({'id': user_id})
    if result.deleted_count == 1:
        return {'message': 'user deleted'}
    else:
        return {'message': 'user not found'}

# cart functions ----------------------------------------------------------------------------------------------

@app.post('/orders')
def create_order(user_id: ObjectId, product_id: ObjectId):
    dict_order = {'user_id': user_id, 'product_id': product_id}
    inserted_order = order_collection.insert_one(dict_order)
    return {'message': 'order created', 'order_id': str(inserted_order.inserted_id)}


@app.get('/orders')
def get_orders():
    orders = order_collection.find()
    return {'orders': orders}

@app.get('/orders/{user_id}')
def get_orders_by_user(user_id: ObjectId):
    orders = order_collection.find({'_id': user_id})
    if orders:
        return {'order': orders}
    else:
        return {'message': 'Cart not found'}

@app.delete('/orders/{order_id}')
def delete_order(user_id: ObjectId):
    result = user_collection.delete_one({'_id': user_id})
    if result.deleted_count == 1:
        return {'message': 'user deleted'}
    else:
        return {'message': 'user not found'}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)











