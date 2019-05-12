from flask import Flask, render_template, url_for, request, redirect, flash, jsonify


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem#, User

engine = create_engine('sqlite:///catalog.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


#shows all restaurants list
@app.route('/')
@app.route('/restaurants/')
def allRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)


#create new restaurant
@app.route('/restaurants/new/', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'])
        session.add(newRestaurant)
        session.commit()
        return redirect(url_for('allRestaurants'))
    else:
        return render_template('newRestaurant.html')

#edit restaurant entries
@app.route('/restaurants/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRestaurant.name = request.form['name']
            return redirect(url_for('allRestaurants'))
        else:
            return render_template('editRestaurant.html', restaurant=editedRestaurant)

#delete restaurant
@app.route('/restaurants/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurantToDelete = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurantToDelete)
        session.commit()
        return redirect(url_for('allRestaurants', restaurant_id=restaurant_id))
    else:
        return render_template('deleteRestaurant.html', restaurant=restaurantToDelete)


#shows menu item in each restaurant selected
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return render_template('menu.html', restaurant=restaurant, items=items)

#add new menu item to restaurant
@app.route('/restaurants/<int:restaurant_id>/menu/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], description=request.form['description'],
                            price=request.form['price'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("Menu Item added")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newMenuItem.html', restaurant_id=restaurant_id)
    return render_template('newMenuItem.html', restaurant=restaurant)


#edit menu item entries
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['price']:
            editedItem.name = request.form['price']
        if request.form['description']:
            editedItem.name = request.form['description']
        session.add(editedItem)
        session.commit()
        flash("Menu Item has been edited")

        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editMenuItem.html', restaurant_id=restaurant_id,
                                    menu_id=menu_id, item=editedItem)

#delete menu items
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Menu Item deleted")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item=itemToDelete)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 9090)
