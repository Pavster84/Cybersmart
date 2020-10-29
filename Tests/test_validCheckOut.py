import time

import pytest

from PageObjects.CheckoutPage import CheckOutPage
from Utilities.BaseClass import BaseClass
from PageObjects.ConfirmationPage import ConfirmationPage
from TestData.CheckOutData import CheckOutData

class TestCheckOutPage(BaseClass):

    def test_valid_submission(self, getData):
        log = self.getLogger()

        checkOutPage = CheckOutPage(self.driver)
        checkOutPage.set_company_name_txt_box(getData['companyName'])
        checkOutPage.set_admin_email_txt_box(getData['email'])
        checkOutPage.set_admin_first_name_txt_box(getData['firstName'])
        checkOutPage.set_admin_last_name_txt_box(getData['lastName'])
        log.info("Populated all the personal details")
        checkOutPage.get_dynamic_radio_btn(getData['product'])
        log.info("Selected product")

        time.sleep(1)

        checkOutPage.submit_form()
        log.info("Clicked submit form button and navigated to confirmation page")

        confirmationPage = ConfirmationPage(self.driver)
        confirmationPage.get_checkout_subscription_success_txt()

        time.sleep(1)

        self.driver.get('https://hudson-poutine-83447.herokuapp.com/')

    @pytest.fixture(params=CheckOutData.test_CheckOut_data)
    def getData(self, request):
        return request.param

