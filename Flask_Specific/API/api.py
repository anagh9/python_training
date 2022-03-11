from restaurants import *
import logging


@app.route('/restaurants', methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def get_restaurants():
    cache.set("restaurants", Restaurants.get_all_restaurants())
    app.logger.info(
        f"{request.method} {request.path} {request.url} Restaurant data retrieved from cache")
    return jsonify({'restaurants': Restaurants.get_all_restaurants()})


@app.route('/restaurants/<int:id>', methods=['GET'])
@cache.cached(timeout=10, query_string=True)
def get_restaurant_by_id(id):
    return jsonify({'restaurant': Restaurants.get_restaurant(id)})


@app.route('/restaurants', methods=['POST'])
def add_restaurants():
    request_data = request.get_json()
    Restaurants.add_restaurant(request_data["name"], request_data["chef_name"], request_data["location"], request_data["category"], request_data["price_range"],
                               request_data["rating"], request_data["address"], request_data["phone"], request_data["website"], request_data["email"])

    return jsonify({'message': 'Restaurant added successfully!'})


@app.route('/restaurants/<int:id>', methods=['PUT'])
def update_restaurants(id):
    request_data = request.get_json()
    Restaurants.update_restaurant(id, request_data["name"], request_data["chef_name"], request_data["location"], request_data["category"],
                                  request_data["price_range"], request_data["rating"], request_data["address"], request_data["phone"], request_data["website"], request_data["email"])

    return jsonify({'message': 'Restaurant updated successfully!'})


@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurants(id):
    Restaurants.delete_restaurant(id)

    return jsonify({'message': 'Restaurant deleted successfully!'})


if __name__ == '__main__':
    app.run(host='localhost', port=5555, debug=True)
