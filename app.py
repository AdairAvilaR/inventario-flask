from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping(): 
    return jsonify({"message": "pong!"})

@app.route('/products')
def  getProducts():
    return jsonify({"products": products, "message": "product's list"}) 

@app.route('/products/<string:product_name>') 
def getproduct(product_name):   
    ProductsFound = [product for product in products if product ['name'] == product_name]   
    if (len(ProductsFound) > 0):
       return jsonify({"product": ProductsFound[0]})    
    return jsonify({"message": "product not found"})

@app.route('/products', methods=['POST'])  
def addproduct():  
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "product added succesfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editproduct(product_name):
    productfound = [product for product in products if product['name'] == product_name]
    if (len(productfound) > 0): 
        productfound[0]['name'] = request.json['name']  
        productfound[0]['price'] = request.json['price']    
        productfound[0]['quantity'] = request.json['quantity']  
        return jsonify ({   
            "message": "product updated",   
            "product": productfound[0]  
            })      
    return jsonify({"message": "product not found"})    

@app.route('/products/<string:product_name>', methods=['DELETE'])   
def deleteproduct(product_name):    
    produductsfound =  [product for product in products if products ['name'] == product_name]    
    if len(produductsfound) > 0:    
        products.remove(produductsfound)[0]    
        return jsonify({
            "message": "product deleted",
            "products": products
        })  
    return jsonify({"message": "product not found"})


if __name__ == '__main__':

    app.run(debug=True, port=4000)