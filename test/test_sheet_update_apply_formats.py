# coding: utf-8

"""
    Platform API

    Use the Workiva Platform API to programmatically manage items in the Workiva platform, such as files, folders, tasks, comments, documents, spreadsheets, and presentations. 

    The version of the OpenAPI document: v1
    Contact: platformsupport@workiva.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.sheet_update_apply_formats import SheetUpdateApplyFormats

class TestSheetUpdateApplyFormats(unittest.TestCase):
    """SheetUpdateApplyFormats unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SheetUpdateApplyFormats:
        """Test SheetUpdateApplyFormats
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SheetUpdateApplyFormats`
        """
        model = SheetUpdateApplyFormats()
        if include_optional:
            return SheetUpdateApplyFormats(
                formats = [
                    {"cellFormat":{"backgroundColor":"#d0e0f0"},"ranges":[{"startColumn":0,"startRow":0,"stopColumn":null,"stopRow":0}],"textFormat":{"bold":true},"valueFormat":{"valueFormatType":"TEXT"}}
                    ]
            )
        else:
            return SheetUpdateApplyFormats(
                formats = [
                    {"cellFormat":{"backgroundColor":"#d0e0f0"},"ranges":[{"startColumn":0,"startRow":0,"stopColumn":null,"stopRow":0}],"textFormat":{"bold":true},"valueFormat":{"valueFormatType":"TEXT"}}
                    ],
        )
        """

    def testSheetUpdateApplyFormats(self):
        """Test SheetUpdateApplyFormats"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()