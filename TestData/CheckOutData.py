from PageObjects.CheckoutPage import CheckOutPage
from selenium import webdriver

from Utilities.BaseClass import BaseClass


class CheckOutData:

  # #id_product

    test_CheckOut_data = [{'companyName':'CyberSafe', 'email':'pav@mailinator.com', 'firstName':'Pavan', 'lastName': 'Rai', 'product': 'id_product_0'},
                          {'companyName': 'CyberSafe Ltd', 'email': 'Rob@mailinator.com', 'firstName': 'Rob','lastName': 'Smith', 'product': 'id_product_1'},
                          {'companyName': 'CyberSafe Ltd', 'email': 'Chris@mailinator.com', 'firstName': 'Chris','lastName': 'Jones', 'product': 'id_product_2'},
                          {'companyName': 'Opus RS', 'email': 'Kate@mailinator.com', 'firstName': 'Kate', 'lastName': 'Mason', 'product': 'id_product_3'}]
