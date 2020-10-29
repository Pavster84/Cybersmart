# Cybersmart Automation

# Introduction
Create automation framework for the website https://hudson-poutine-83447.herokuapp.com/ using Python programming language with the pytest framework

Test the checkout functionality which consist of the following requirements
-	Submit a checkout request
-	Valid data for each field
-	All combinations must function

# Pytest pro's
- Used to create simple as well as complex functional test cases
- Compatible  with other test frameworks like unittest
- Supports fixtures and classes, to make it easier to create common test objects
- Supports parameterization

# Pre-requisite 
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
1. Easy to maintain
2. Reusability of code
3. Reduce or eliminate duplicate code
 
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
 This file is also used to cover all the combinations functions for selecting fields and the products using parameterisation tests with multiple data sets.
                          
- Tests package 
This is where the automation is executed using pytest, files names need to start with test. The class also inherits the baseClass in the Utilites package.
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
  
Currently the only method I created in the BaseClass.py was logger, which is used in the test file to audit the actions executed rather than use the print statement.

# Run all automation tests
Using the pycharm terminal in the tests directory, run the following "py.test --html-report.html"

# Run specific automation 
Using the pycharm terminal in the tests directory, run the following "py.test test_invalidCheckOut.py"

# Run tests and generate reports
"py.test --html-report.html"

# Improvements and work still required
- Generate HTML reports in the framework when the test is executed
- Integrate framework to Jenkins to corporate CI
- Create negative tests which cover the following;
  - No input and click 'Submit' button and verify validation message is produced
  - Invalid email
  - When no product is selected
  
# Questions
-	How this may be used in a wider team (think about different life cycles(Kanban/Scrum))?

The following automation will be used from e2e tests (UI testing). This could be used as part of the regression or smoke test when testing on various environments.
Future plans should also cater for API tests to give more test coverage.

-	What would be required to adopt in a Product Engineering team?

New functionalities to be discussed by the team collectively so that planning could be made on ensuring the acceptance criteria. As well an then planning of the automation tests from a QA perspective to ensure new or amending existing scripts are continuously updated in order to achieve confidence that everything is working as expected.

Another framework to consider for the engineering team is BDD framework using the 'Behave' package. This allows test cases to be created using simple test language (gherkin). This helps technical team members to understand the scenarios executed and help improve the communication between technical and non-technical members.

That automation of critical areas of the system will help the manual testers to perform more exploratory testing and black box design techniques.

Regression tests to run to ensure new code has not broken existing functionality so that the production team are satsifed that test coverage on key functionality has been tested. Reports of tests executed will then be given to the team to indicate results.


