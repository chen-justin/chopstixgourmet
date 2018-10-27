import sqlite3
from sqlite3 import Error

def create_connection(db_file):
  try:
    conn = sqlite3.connect(db_file)
    return conn
  except Error as e:
    print(e)
  
  return None

def create_table(conn, create_table_sql):
  try:
    c = conn.cursor()
    c.execute(create_table_sql)
  except Error as e:
    print(e)

def create_menu_item(conn, menu_item):
  sql = "INSERT INTO menu_items(name, price) VALUES(?,?);"
  conn.execute(sql, menu_item)
  return conn.lastrowid

def create_menu_item_type(conn, menu_item_type):
  sql = "INSERT INTO menu_item_types(name) VALUES(?);"
  conn.execute(sql, menu_item_type)
  return conn.lastrowid
  

def main():
  database = "db/chopstix.db"
  conn = create_connection(database)
  create_menu_items_table = "CREATE TABLE IF NOT EXISTS menu_items (item_id integer PRIMARY KEY, name text NOT NULL, category text NOT NULL, description text, price integer NOT NULL);"
  with conn:
    conn.execute("DROP TABLE IF EXISTS menu_items")
    create_table(conn, create_menu_items_table)

    menu_items = [
      ("Chicken and Corn Soup", None, 225),
      ("Chicken Noodle or Rice Soup", None, 225),
      ("Chicken Wonton Soup", None, 225),
      ("Miso Soup",None, 225),
      ("Vegetarian Hot and Sour Soup", None, 225),
      ("Spicy Beef Soup","Beef broth with tender beef, carrots, and celery", 325),
      ("Teapot Soup","Mixed seafood and vegetables", 525),
      ("Ten Ingredient Wonton Soup",None, 725),
      ("Creamy Seafood Soup","Creamy soup with scallops, crabmeat, and shrimp.", 725)
    ]
    
    for item in menu_items:
      conn.execute("INSERT INTO menu_items(name, category, description, price) VALUES (?,?,?,?);", (item[0], "Soup", item[1], item[2]))
    
    salads = [
      ("Avocado Salad","Spring mix and avocado with Japanese wasabi and yuzu dressing.", 595),
      ("Japanese Green Salad","Garden greens with homemade ginger dressing.", 325),
      ("Pepper Tuna Salad","Spring mix and seared black pepper tuna with Japanese wasbi and yuzu dressing.", 995),
      ("Seaweed Salad",None, 525),
      ("Squid Salad",None, 595),
      ("Sunomono","Assorted Sashimi in vinegar sauce.", 895),
      ("Baby Octopus Salad",None, 525),
      ("Sammy Salad","Assorted fresh fish in spicy Chef's sauce.", 895),
      ("Spicy Lobster Salad",None, 825)
    ]

    for salad in salads:
      conn.execute("INSERT INTO menu_items(name, category, description, price) VALUES (?,?,?,?);", (salad[0],"Salad",salad[1],salad[2]))
    
    appetizers = [
      ("Vegetarian Spring Rolls",None, 350),
      ("Shrimp Egg Rolls",None, 350),
      ("Barbecue Spare Ribs",None, 695),
      ("Chicken Lettuce Wrap","Diced chicken, celery, water chestnuts, and sunflower seeds with a side of lettuce wraps.", 695),
      ("Dumpling","Pork filling; available steamed or pan-fried.", 525),
      ("Ebi Yaki","Skewered grilled shrimp with teriyaki sauce and vegetables.", 795),
      ("Scallop Yaki", "Skewered grilled scallops with teriyaki sauce and vegetables.", 795),
      ("Edamame", "Steamed Japanese soybeans.",450),
      ("Fried Calamari", None, 695),
      ("Gyoza", "Japanese style steamed chicken dumplings.", 525),
      ("Plump Mussels and Scallops in Spicy Sauce", None, 695),
      ("Shrimp Tempura", "Shrimp and vegetables fried with a light tempura batter.", 625),
      ("Shrimp Toasts", None, 675),
      ("Shumai", "Available steamed or fried",525),
      ("Skewered BBQ Beef", None, 595)
    ]

    for item in appetizers:
      conn.execute("INSERT INTO menu_items(name, category, description, price) VALUES (?,?,?,?);", (item[0],"Appetizer",item[1],item[2]))
    
    print("Successfully Created Database and Inserted Items")
if __name__ == '__main__':
  main()