from flask import Flask, render_template, url_for, request


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///catalog.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
@app.route('/restaurants/<int:restaurant_id>/menu/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant_id)
    # output = ''
    # for item in items:
    #     output += item.name
    #     output += '</br>'
    #     output += item.price
    #     output += '</br>'
    #     output += item.description
    #     output += '</br>'
    #     output += '</br>'
    # return output
    return render_template('menu.html', restaurant=restaurant, items=items)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 9090)
