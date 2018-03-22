# -*- coding: utf-8 -*-

"""
    ytel.models.error_model

    This file was automatically generated for ytel by APIMATIC v2.0 ( https://apimatic.io )
"""


class ErrorModel(object):

    """Implementation of the 'Error' model.

    TODO: type model description here.

    Attributes:
        code (string): TODO: type description here.
        message (string): TODO: type description here.
        more_info (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code":'Code',
        "message":'Message',
        "more_info":'MoreInfo'
    }

    def __init__(self,
                 code=None,
                 message=None,
                 more_info=None):
        """Constructor for the ErrorModel class"""

        # Initialize members of the class
        self.code = code
        self.message = message
        self.more_info = more_info


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
        code = dictionary.get('Code')
        message = dictionary.get('Message')
        more_info = dictionary.get('MoreInfo')

        # Return an object of this model
        return cls(code,
                   message,
                   more_info)

