# -*- coding: utf-8 -*-

"""
    ytel.models.message_model

    This file was automatically generated for ytel by APIMATIC v2.0 ( https://apimatic.io )
"""
import ytel.models.template_data_model

class MessageModel(object):

    """Implementation of the 'Message' model.

    TODO: type model description here.

    Attributes:
        api_version (string): TODO: type description here.
        message_sid (string): TODO: type description here.
        mfrom (string): TODO: type description here.
        to (string): TODO: type description here.
        message_price (string): TODO: type description here.
        body (string): TODO: type description here.
        date_sent (string): TODO: type description here.
        status (string): TODO: type description here.
        template_id (string): TODO: type description here.
        template_data (TemplateDataModel): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "api_version":'ApiVersion',
        "message_sid":'MessageSid',
        "mfrom":'From',
        "to":'To',
        "message_price":'MessagePrice',
        "body":'Body',
        "date_sent":'DateSent',
        "status":'Status',
        "template_id":'TemplateId',
        "template_data":'TemplateData'
    }

    def __init__(self,
                 api_version=None,
                 message_sid=None,
                 mfrom=None,
                 to=None,
                 message_price=None,
                 body=None,
                 date_sent=None,
                 status=None,
                 template_id=None,
                 template_data=None):
        """Constructor for the MessageModel class"""

        # Initialize members of the class
        self.api_version = api_version
        self.message_sid = message_sid
        self.mfrom = mfrom
        self.to = to
        self.message_price = message_price
        self.body = body
        self.date_sent = date_sent
        self.status = status
        self.template_id = template_id
        self.template_data = template_data


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        api_version = dictionary.get('ApiVersion')
        message_sid = dictionary.get('MessageSid')
        mfrom = dictionary.get('From')
        to = dictionary.get('To')
        message_price = dictionary.get('MessagePrice')
        body = dictionary.get('Body')
        date_sent = dictionary.get('DateSent')
        status = dictionary.get('Status')
        template_id = dictionary.get('TemplateId')
        template_data = ytel.models.template_data_model.TemplateDataModel.from_dictionary(dictionary.get('TemplateData')) if dictionary.get('TemplateData') else None

        # Return an object of this model
        return cls(api_version,
                   message_sid,
                   mfrom,
                   to,
                   message_price,
                   body,
                   date_sent,
                   status,
                   template_id,
                   template_data)

