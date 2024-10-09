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

from openapi_client.models.test_phase import TestPhase

class TestTestPhase(unittest.TestCase):
    """TestPhase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestPhase:
        """Test TestPhase
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestPhase`
        """
        model = TestPhase()
        if include_optional:
            return TestPhase(
                id = 'bac770b8-1673-11ec-9621-0242ac130002',
                name = 'Walkthrough',
                attachments = [{"id":"7366eb18-f4a4-459c-a2e4-d619df97499e","fileName":"status.pdf"}],
                matrices = [{"id":"f9b7f2ec-aada-4412-a549-494f9639a3ab","name":"Purchase Orders"},{"id":"4f241ab3-cb2c-47e0-9a11-63156768494f","name":"Back Orders"}]
            )
        else:
            return TestPhase(
        )
        """

    def testTestPhase(self):
        """Test TestPhase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()