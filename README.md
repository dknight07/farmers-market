# Farmers Market app v1.0

This code base serves to build the Farmers Market  application.

## Code characteristics

* Implemented on Python 3.x
* Well organized directories with lots of comments
    * app
        * commands
        * templates
        * tests
        * dockerfile
        * requirements
    * tests
* Includes test framework (`unittest`)


# Running the app in your local

    # Start the Flask development web server in Local
    export FLASK_APP=app.py
    set FLASK_APP=app.py 
    flask run


Point your web browser to http://localhost:5000/

# Running the app in docker container by publishing the image

    # Build the Dockerfile
    docker build -t farmers-app:latest .
    
    # Run the App
    docker run -it -d -p 5000:5000 farmers-app


Point your web browser to http://localhost:5000/
List of Products :
```
+--------------|--------------|---------+
| Product Code |     Name     |  Price  |
+--------------|--------------|---------+
|     CH1      |   Chai       |  $3.11  |
|     AP1      |   Apples     |  $6.00  |
|     CF1      |   Coffee     | $11.23  |
|     MK1      |   Milk       |  $4.75  |
|     OM1      |   Oatmeal    |  $3.69  |
+--------------|--------------|---------+
```
Enter the Comma Separated product codes and checkout.


## Running the automated unit tests

    # Start the Flask development web server
    python -m unittest farmers_test.TestFarmersMarket



## Trouble shooting

If you make changes in the templates or the app.py please stop and rerun the server.



## Authors

- Hemanth Batchu