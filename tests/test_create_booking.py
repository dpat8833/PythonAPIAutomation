"""
Author:Dibyajyoti Pattnaik
Objective: Create and verify POST request
TC#1 - Verify the status code, headers
TC#2 - Verify the body booing_id
TC#3 - Verify if the json schema is valid
"""
import allure
import pytest
import json

from src.constants.apiconstants import url_create_booking
from src.helpers.utils import common_headers
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manager import create_booking_payload
from src.helpers.common_verification import verify_http_code, verify_key


class TestIntegration(object):
    # @pytest.mark.run(order=1)
    @pytest.fixture(scope="module")
    def setup(self):
        print("Before")

    def test_create_booking_tc1(self):
        # Here I will call the function to make a request
        response = post_request(url_create_booking(), header=common_headers(), auth=None,
                                payload=create_booking_payload(), in_json=False)
        assert True == True
        verify_http_code(response, 200)
        booking_id = response.json()["bookingid"]
        verify_key(response, booking_id)

    @pytest.fixture(scope="module")
    def teardown(self):
        print("After")

    # @pytest.mark.run(order=2)
    # def test_create_booking_tc2(self):
    #     assert True == False
    #
    # @pytest.mark.run(order=3)
    # def test_create_booking_tc3(self):
    #     assert True == True
