from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem #, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Menu for Pepperwood
restaurant1 = Restaurant(name = "Pepperwood")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(name = "Iced Tea", description = "Cool n Refreshing", price = "$3.50", course = "Beverage", restaurant = restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(name = "French Fries", description = "Simple, salt n desi spice", price = "$5.99", course = "Appetizer", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Chicken Burger", description = "Juicy grilled chicken patty with fresh greens", price = "$5.50", course = "Entree", restaurant = restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Chocolate Cake", description = "Fresh baked and served with ice cream", price = "$3.99", course = "Dessert", restaurant = restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name = "Veggie Burger", description = "Made with juicy patty and fresh greens", price = "$9.99", course = "Main", restaurant = restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name = "Paneer Tikka", description = "Soft pockets of joy", price = "$2.99", course = "starter", restaurant = restaurant1)

session.add(menuItem5)
session.commit()




#Menu for Dosa Corner
restaurant2 = Restaurant(name = "Dosa Corner")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name = "Chicken Dosa", description = "With your choice of Chicken - Tikka, Tandoor, Grilled, Fried", price = "$13.99", course = "Entree", restaurant = restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Paneer Dosa", description = "With your choice of Paneer - Tikka, Tandoor, Grilled, Fried", price = "$15", course = "Entree", restaurant = restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Veg Dosa", description = "Veg ladden magic", price = "15", course = "Entree", restaurant = restaurant2)

session.add(menuItem3)
session.commit()




#Menu for Brownie Science
restaurant3 = Restaurant(name = "Brownie Science")

session.add(restaurant3)
session.commit()


menuItem1 = MenuItem(name = "Simple", description = "With chocolate sauce and ice cream", price = "$8.99", course = "Dessert", restaurant = restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Make Your Own", description = "with sauce and toppings of choice", price = "$10.99", course = "Dessert", restaurant = restaurant3)

session.add(menuItem2)
session.commit()




#Menu for Messy
restaurant4 = Restaurant(name = "Messy ")

session.add(restaurant4)
session.commit()


menuItem1 = MenuItem(name = "Chicken and Mushroom pie", description = "Where juicy meets spice", price = "$2.99", course = "Dessert", restaurant = restaurant4)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Mushroom risotto", description = "Portabello mushrooms in a creamy risotto", price = "$5.99", course = "Entree", restaurant = restaurant4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Honey Boba Shaved Snow", description = "Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", price = "$4.50", course = "Dessert", restaurant = restaurant4)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name = "Cauliflower Manchurian", description = "Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions", price = "$6.95", course = "Appetizer", restaurant = restaurant4)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name = "Aloo Gobi Burrito", description = "Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom", price = "$7.95", course = "Entree", restaurant = restaurant4)

session.add(menuItem5)
session.commit()



#Menu for Tony's Bistro
restaurant1 = Restaurant(name = "Tony\'s Bistro ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(name = "Shellfish Tower", description = "Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower", price = "$13.95", course = "Entree", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name = "Chicken and Rice", description = "Chicken... and rice", price = "$4.95", course = "Entree", restaurant = restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name = "Mom's Spaghetti", description = "Spaghetti with some incredible tomato sauce made by mom", price = "$6.95", course = "Entree", restaurant = restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name = "Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)", description = "Milk, cream, salt, ..., Liquid nitrogen magic", price = "$3.95", course = "Dessert", restaurant = restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(name = "Tonkatsu Ramen", description = "Noodles in a delicious pork-based broth with a soft-boiled egg", price = "$7.95", course = "Entree", restaurant = restaurant1)

session.add(menuItem5)
session.commit()



print "added menu items!"
