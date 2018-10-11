# -*- coding: utf-8 -*-

"""
    ytelapiv3

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class AddressController(BaseController):

    """A Controller to access Endpoints in the ytelapiv3 API."""


    def create_delete_address(self,
                              addressid):
        """Does a POST request to /address/deleteaddress.json.

        To delete Address to your address book

        Args:
            addressid (string): The identifier of the address to be deleted.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/address/deleteaddress.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'addressid': addressid
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_verify_address(self,
                              addressid):
        """Does a POST request to /address/verifyaddress.json.

        Validates an address given.

        Args:
            addressid (string): The identifier of the address to be verified.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/address/verifyaddress.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'addressid': addressid
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_view_address(self,
                            addressid):
        """Does a POST request to /address/viewaddress.json.

        View Address Specific address Book by providing the address id

        Args:
            addressid (string): The identifier of the address to be
                retrieved.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/address/viewaddress.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'addressid': addressid
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_list_addresses(self,
                              page=None,
                              pagesize=None,
                              addressid=None,
                              date_created=None):
        """Does a POST request to /address/listaddress.json.

        List All Address 

        Args:
            page (int, optional): The page count to retrieve from the total
                results in the collection. Page indexing starts at 1.
            pagesize (int, optional): How many results to return, default is
                10, max is 100, must be an integer
            addressid (string, optional): addresses Sid
            date_created (string, optional): date created address.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/address/listaddress.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'page': page,
            'pagesize': pagesize,
            'addressid': addressid,
            'dateCreated': date_created
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_address(self,
                       name,
                       address,
                       country,
                       state,
                       city,
                       zip,
                       description=None,
                       email=None,
                       phone=None):
        """Does a POST request to /address/createaddress.json.

        To add an address to your address book, you create a new address
        object. You can retrieve and delete individual addresses as well as
        get a list of addresses. Addresses are identified by a unique random
        ID.

        Args:
            name (string): Name of user
            address (string): Address of user.
            country (string): Must be a 2 letter country short-name code (ISO
                3166)
            state (string): Must be a 2 letter State eg. CA for US. For Some
                Countries it can be greater than 2 letters.
            city (string): City Name.
            zip (string): Zip code of city.
            description (string, optional): Description of addresses.
            email (string, optional): Email Id of user.
            phone (string, optional): Phone number of user.

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/address/createaddress.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Name': name,
            'Address': address,
            'Country': country,
            'State': state,
            'City': city,
            'Zip': zip,
            'Description': description,
            'email': email,
            'Phone': phone
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body