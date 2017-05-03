# -*- coding: utf-8 -*-

"""
    message_360.controllers.conference_controller

    This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.basic_auth import BasicAuth

class ConferenceController(BaseController):

    """A Controller to access Endpoints in the message_360 API."""


    def create_deaf_mute_participant(self,
                                     options=dict()):
        """Does a POST request to /conferences/deafMuteParticipant.{ResponseType}.

        Deaf Mute Participant

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    conference_sid -- string -- TODO: type description here.
                        Example: 
                    participant_sid -- string -- TODO: type description here.
                        Example: 
                    response_type -- string -- Response Type either json or
                        xml
                    muted -- bool -- TODO: type description here. Example: 
                    deaf -- bool -- TODO: type description here. Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(conference_sid=options.get("conference_sid"),
                                 participant_sid=options.get("participant_sid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/deafMuteParticipant.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'conferenceSid': options.get('conference_sid', None),
            'ParticipantSid': options.get('participant_sid', None),
            'Muted': options.get('muted', None),
            'Deaf': options.get('deaf', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_list_conference(self,
                               options=dict()):
        """Does a POST request to /conferences/listconference.{ResponseType}.

        List Conference

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    response_type -- string -- Response type format xml or
                        json
                    page -- int -- Which page of the overall response will be
                        returned. Zero indexed
                    page_size -- int -- Number of individual resources listed
                        in the response per page
                    friendly_name -- string -- Only return conferences with
                        the specified FriendlyName
                    status -- InterruptedCallStatusEnum -- TODO: type
                        description here. Example: 
                    date_created -- string -- TODO: type description here.
                        Example: 
                    date_updated -- string -- TODO: type description here.
                        Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/listconference.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'Page': options.get('page', None),
            'PageSize': options.get('page_size', None),
            'FriendlyName': options.get('friendly_name', None),
            'Status': options.get('status', None),
            'DateCreated': options.get('date_created', None),
            'DateUpdated': options.get('date_updated', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_view_conference(self,
                               options=dict()):
        """Does a POST request to /conferences/viewconference.{ResponseType}.

        View Conference

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    conferencesid -- string -- The unique identifier of each
                        conference resource
                    response_type -- string -- Response type format xml or
                        json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(conferencesid=options.get("conferencesid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/viewconference.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'conferencesid': options.get('conferencesid', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def add_participant(self,
                        options=dict()):
        """Does a POST request to /conferences/addParticipant.{ResponseType}.

        Add Participant in conference 

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    conferencesid -- string -- Unique Conference Sid
                    participantnumber -- string -- Particiant Number
                    tocountrycode -- int -- TODO: type description here.
                        Example: 
                    response_type -- string -- Response type format xml or
                        json
                    muted -- bool -- TODO: type description here. Example: 
                    deaf -- bool -- TODO: type description here. Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(conferencesid=options.get("conferencesid"),
                                 participantnumber=options.get("participantnumber"),
                                 tocountrycode=options.get("tocountrycode"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/addParticipant.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'conferencesid': options.get('conferencesid', None),
            'participantnumber': options.get('participantnumber', None),
            'tocountrycode': options.get('tocountrycode', None),
            'muted': options.get('muted', None),
            'deaf': options.get('deaf', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_list_participant(self,
                                options=dict()):
        """Does a POST request to /conferences/listparticipant.{ResponseType}.

        List Participant

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    conference_sid -- string -- unique conference sid
                    response_type -- string -- Response format, xml or json
                    page -- int -- page number
                    pagesize -- int -- TODO: type description here. Example: 
                    muted -- bool -- TODO: type description here. Example: 
                    deaf -- bool -- TODO: type description here. Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(conference_sid=options.get("conference_sid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/listparticipant.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ConferenceSid': options.get('conference_sid', None),
            'Page': options.get('page', None),
            'Pagesize': options.get('pagesize', None),
            'Muted': options.get('muted', None),
            'Deaf': options.get('deaf', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def create_view_participant(self,
                                options=dict()):
        """Does a POST request to /conferences/viewparticipant.{ResponseType}.

        View Participant

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    conference_sid -- string -- unique conference sid
                    participant_sid -- string -- TODO: type description here.
                        Example: 
                    response_type -- string -- Response type format xml or
                        json

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(conference_sid=options.get("conference_sid"),
                                 participant_sid=options.get("participant_sid"),
                                 response_type=options.get("response_type"))

        # Prepare query URL
        _query_builder = Configuration.get_base_uri()
        _query_builder += '/conferences/viewparticipant.{ResponseType}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'ResponseType': options.get('response_type', None)
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare form parameters
        _form_parameters = {
            'ConferenceSid': options.get('conference_sid', None),
            'ParticipantSid': options.get('participant_sid', None)
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters,
            Configuration.array_serialization)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, parameters=_form_parameters)
        BasicAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body