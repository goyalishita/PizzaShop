# PizzaShop
Django application to store information about different types of Pizza


Technology used-
Django - python Framework
Bootstrap - CSS Framework 
MongoDB - DB 


Features- 
Pizza can be of Multiple types: Regular or Square; Multiple sizes and Toppings - Onion, Tomato, etc. 
Errors & Validation - The API should return proper 40x codes when any kind of wrong input is sent to the API, the server should not return 500 errors
The user should not be able to create a pizza of any other type which isn't present in the database.


Steps to run the project-
1. Install Pyhton
2. Install django, djongo
3. Install mongoDB community Edition
4. Run the command "py manage.py makemigrations"
5. Run the command "py manage.py migrate"
6. Run the command "py manage.py runserver"
7. copy and paste the url in chrome and use the pizza shop

Steps to connect mongodb and Django:
1. In settings.py of project folder paste this database setting and remove the previous database settings code.
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'PizzaDB',
    }
}
2. In MongoDB Compass, connect to localhost and craete a database named 'PizzaDB'

Rest APIs-
1. Get All Types of Pizza- 
   http://127.0.0.1:8000/
   Request Type - Get
   Params - NULL
   Response - If valid, 200 Ok and returns all the stored pizzas 


2. Get Filtered Pizza by Type-
   http://127.0.0.1:8000/Type/{type}
   Request Type - Get
   Params - Type either square or circle
   Response - If valid, 200 Ok and returns filtered type pizzas
            - If Invalid, 404 not found

3. Get Filtered Pizza by Size-
   http://127.0.0.1:8000/Size/{size}
   Request Type - Get
   Params - size either 4 or 6
   Response - If valid, 200 Ok and returns all filtered pizzas
            - If Invalid, 404 not found


4. Get Filtered Pizza by Toppings-
   http://127.0.0.1:8000/Toppings/{toppings}
   Request Type - Get
   Params - Type of toppings
   Response - If valid, 200 Ok and returns all filtered pizzas
            - If Invalid, 404 not found


5. Delete Pizza By Id-
   http://127.0.0.1:8000/Delete/{Id}
   Request Type - Delete
   Response - 200 Ok 


6. Edit Pizza By id-
   http://127.0.0.1:8000/Edit/{Id}
   Request Type - Patch
   Response - 200 Ok, If valid
            - If Invalid, 404 not found


7. Registers the user-
   http://127.0.0.1:8000/Register
   Request Type - Post
   Body - Username, password, FirstName, LastName
   Response - 200 Ok


8. Login the user-
   http://127.0.0.1:8000/Login
   Request Type - Post
   Body - Username, password
   Response - 200 Ok


9. Logout the user-
   http://127.0.0.1:8000/Logout
   Request Type - Post
   Response - 200 Ok