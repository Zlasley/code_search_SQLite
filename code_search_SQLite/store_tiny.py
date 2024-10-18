""" Module providing function for creatin a SQL DB"""
import sqlite333

# Creates a connection to sqlite3 database
connect = sqlite3.connect('tiny_store.sqlite3')
cursor = connect.cursor()

# SQL query for the ten most expensive items per unit price
expensive_items = '''
    SELECT *
    FROM "Product"
    ORDER BY UnitPrice
    DESC LIMIT 10;'''

# SQL query for the average age of an employee when hired
avg_hire_age = '''
    SELECT AVG(HireDate - BirthDate)
    FROM Employee;'''

# SQL query for ten most expensive times between Product and Supplier
ten_most_expensive = '''
    SELECT p.ProductName, p.UnitPrice, s.CompanyName
    FROM Product p, Supplier s WHERE p.SupplierId = s.Id
    ORDER BY p.UnitPrice DESC LIMIT 10;'''

# SQL query for the largest category of unique products
largest_category = '''
    SELECT c.CategoryName, COUNT(DISTINCT p.Id)
    FROM Category c, Product p
    WHERE c.Id = p.CategoryId
    GROUP BY 1 ORDER BY 2 DESC LIMIT 1;'''

expensive = cursor.execute(expensive_items).fetchall()
# [(9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97, 29, 0, 0, 1)
# (18, 'Carnarvon Tigers', 7, 8, '16 kg pkg.', 62.5, 42, 0, 0, 0)
# (20, "Sir Rodney's Marmalade", 8, 3, '30 gift boxes', 81, 40, 0, 0, 0)
# (28, 'R▒ssle Sauerkraut', 12, 7, '25 - 825 g cans', 45.6, 26, 0, 0, 1)
# (29,'Th▒ringer Rostbratwurst',12, 6,'50 bags x 30 sausgs.',123.79, 0, 0, 0,1)
# (38, 'C▒te de Blaye', 18, 1, '12 - 75 cl bottles', 263.5, 17, 0, 15, 0)
# (43, 'Ipoh Coffee', 20, 1, '16 - 500 g tins', 46, 17, 10, 25, 0)
# (51, 'Manjimup Dried Apples', 24, 7, '50 - 300 g pkgs.', 53, 20, 0, 10, 0)
# (59, 'Raclette Courdavault', 28, 4, '5 kg pkg.', 55, 79, 0, 0, 0)
# (62, 'Tarte au sucre', 29, 3, '48 pies', 49.3, 17, 0, 0, 0)]

avg_age = cursor.execute(avg_hire_age).fetchall()
# [(37.22222222222222,)]

most_expensive = cursor.execute(ten_most_expensive).fetchall()
# [('Th▒ringer Rostbratwurst', 123.79, "For▒ts d'▒rables")
# ('Mishi Kobe Niku', 97, 'PB Kn▒ckebr▒d AB')
# ("Sir Rodney's Marmalade", 81, 'Leka Trading')
# ('Carnarvon Tigers', 62.5, 'Aux joyeux eccl▒siastiques')
# ('R▒ssle Sauerkraut', 45.6, 'Gai p▒turage')
# ('Schoggi Schokolade', 43.9, 'Escargots Nouveaux')
# ('Northwoods Cranberry Sauce', 40, 'Specialty Biscuits, Ltd.')
# ('Alice Mutton', 39, 'Svensk Sj▒f▒da AB')
# ('Queso Manchego La Pastora', 38, 'Plutzer Lebensmittelgro▒m▒rkte AG')
# ('Gumb▒r Gummib▒rchen', 31.23, 'Pasta Buttini s.r.l.')]

lrg_category = cursor.execute(largest_category).fetchall()
# [('Confections',)]

print(expensive, avg_age, most_expensive, lrg_category)

connect.commit()
