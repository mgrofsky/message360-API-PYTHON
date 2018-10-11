# -*- coding: utf-8 -*-

"""
    ytelapiv3

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from ytelapiv3.api_helper import APIHelper


class LetterControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(LetterControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.letter

    # Retrieve a list of letter objects. The letter objects are sorted by creation date, with the most recently created letters appearing first.
    def test_test_list_letters(self):
        # Parameters for the API call
        page = None
        pagesize = None
        lettersid = None
        date_created = None

        # Perform the API call through the SDK function
        result = self.controller.create_list_letters(page, pagesize, lettersid, date_created)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)
