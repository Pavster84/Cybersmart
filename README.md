# Cybersmart Automation

# Introduction
Create automation framework for the website https://hudson-poutine-83447.herokuapp.com/ using Python programming language with the pytest framework

Test the checkout functionality which consist of the following requirements
-	Submit a checkout request
-	Valid data for each field
-	All combinations must function

# Pytest pro's
- Used to create simple as well as complex functional test cases
- Compatibale with oter test frameworks like unittest
- Supports fixtures and classes, to make it easier to create common test objects
- Supports parameterization

# Pre-requiste 
- Download python 3.x.x
- Pycharm community editor needed to develop the automation tests
- Chromedriver from selenium needs to be installed

# Python packages installed
- Pytest
- Selenium

# Creating the automation framework
Create the following packages below;

- PageObjects package
This contains all the web elements, as well as the get and set methods. This is where the constructor is also used.

Advantages of using page object mechanism
 - Easy to maintain
 - Reusability of code
 - Reduce or eliminate duplicate code
 
 Example below of example of the code in CheckoutPage.py
 
 class CheckOutPage:

    # create constructor which accepts driver argument and performs connection to local driver
    def __init__(self, driver):
        self.driver = driver

    companyNameTxtBox = (By.CSS_SELECTOR, "#id_company_name")

    def set_company_name_txt_box(self, companyName):
        self.driver.find_element(*CheckOutPage.companyNameTxtBox).send_keys(companyName)

 - TestData packages
 Filename: CheckOutData.py
 This file is used to implement data driven mechanism by removing the hard code where the test will be running.
 This file is also used to cover all the combinations must functions and all products selected using parameterisation tests with multiple data sets(see below).
 
 test_CheckOut_data = [{'companyName':'CyberSafe', 'email':'pav@mailinator.com', 'firstName':'Pavan', 'lastName': 'Rai', 'product': 'id_product_0'},
                          {'companyName': 'CyberSafe Ltd', 'email': 'Rob@mailinator.com', 'firstName': 'Rob','lastName': 'Smith', 'product': 'id_product_1'},
                          {'companyName': 'CyberSafe Ltd', 'email': 'Chris@mailinator.com', 'firstName': 'Chris','lastName': 'Jones', 'product': 'id_product_2'},
                          {'companyName': 'Opus RS', 'email': 'Kate@mailinator.com', 'firstName': 'Kate', 'lastName': 'Mason', 'product': 'id_product_3'}]
                          
- Tests package 
This is where the automation is executed using pytest, files names need to start with test. The class also inherits the baseClass.
This covers pytest.fixture which helps get data from the TestData package to get the data using data driven approach. Code below will indicate this.

  checkOutPage.set_admin_last_name_txt_box(getData['lastName'])
  
    @pytest.fixture(params=CheckOutData.test_CheckOut_data)
    def getData(self, request):
        return request.param
        
  Filename: confttest.py will be used across multiple test cases, this is where the set up and tear down of tests will occur. This file also indicates what browser user may want the test to run on.
  If no browser is provided then by default chrome is selected.
  
  Filename: logfile.log is an audit of all the actions logged when the test was executed. This is driven by the BaseClass which is store in the 'Utilities' package
  Example of the logging below;
  
  2020-10-29 18:41:18,931 :INFO : test_valid_submission :Clicked submit form button and navigated to confirmation page
  
  - Utilites
  This is where the BaseClass.py is created to move fixture redundant code. Any repeated code which is used in multiple test cases would be put in methods so this could be shared across all the test files.
  
  Currently the only method I created in the BaseClass.py was logger, which is used in the test file to audit the actions executed rather than you the print statement.

