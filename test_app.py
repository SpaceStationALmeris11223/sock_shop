#import the functions and methods you want to test
from app import get_available_products
# get_product_by_id, get_all_categories

#test the get available prducts funct
def test_get_available_products():
    #verify that we can retrive prodcucts
    #call rt==the get_available_products
    products = get_available_products()

    #test using an assertion if three prodcuts were 
    assert len(products) == 3

    #test that prodcut have all the required fields( price, descrtiption, category, etc)
    assert all('id' in p and 'image' in p and 'category' in p
    for p in products)
        #bugfix catergory in product was changed to category in p

    # test that the available in the "funny category equals 2"
    assert len(get_available_products('funny')) == 2


#test the get product by id function
def test_get_product_by_id():
    #get a product form the collection of product with product id 1
    product = get_product_by_id(1)

    #test that the prodcut exist adn that the id is 1 and the name is meme lord
    assert product and product['id'] == 1 and product['name'] == 'Meme Lord'
        #Bugfix [id] was chanegd to ['id']
    #test that invaild proudcut id is handled gracefully instead of throwing an error
    assert get_product_by_id(999) is None

#test the get all categories funtion
def test_get_all_categories():
    #get the categories of socks
    categories = get_all_categories()

    #test that there are two categoreis in the list
    assert len(categories) == 2
    assert 'funny' in categories and 'school' in categories
