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

from openapi_client.models.sheets_list_result import SheetsListResult

class TestSheetsListResult(unittest.TestCase):
    """SheetsListResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SheetsListResult:
        """Test SheetsListResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SheetsListResult`
        """
        model = SheetsListResult()
        if include_optional:
            return SheetsListResult(
                data = [
                    openapi_client.models.sheet.Sheet(
                        id = '27f1b61c04ae4b0991bc73c631914e1d', 
                        name = 'Q1', 
                        parent = openapi_client.models.sheet.Sheet(
                            id = '27f1b61c04ae4b0991bc73c631914e1d', 
                            name = 'Q1', 
                            index = 1, 
                            children = [
                                
                                ], 
                            dataset = openapi_client.models.dataset.Dataset(
                                sheet = '27f1b61c04ae4b0991bc73c631914e1d', 
                                range = 'A1:B2', 
                                values = [[1,4],[2,""]], ), ), 
                        index = 1, 
                        children = [
                            
                            ], 
                        dataset = openapi_client.models.dataset.Dataset(
                            sheet = '27f1b61c04ae4b0991bc73c631914e1d', 
                            range = 'A1:B2', 
                            values = [[1,4],[2,""]], ), )
                    ],
                next_link = '<opaque_url>'
            )
        else:
            return SheetsListResult(
                data = [
                    openapi_client.models.sheet.Sheet(
                        id = '27f1b61c04ae4b0991bc73c631914e1d', 
                        name = 'Q1', 
                        parent = openapi_client.models.sheet.Sheet(
                            id = '27f1b61c04ae4b0991bc73c631914e1d', 
                            name = 'Q1', 
                            index = 1, 
                            children = [
                                
                                ], 
                            dataset = openapi_client.models.dataset.Dataset(
                                sheet = '27f1b61c04ae4b0991bc73c631914e1d', 
                                range = 'A1:B2', 
                                values = [[1,4],[2,""]], ), ), 
                        index = 1, 
                        children = [
                            
                            ], 
                        dataset = openapi_client.models.dataset.Dataset(
                            sheet = '27f1b61c04ae4b0991bc73c631914e1d', 
                            range = 'A1:B2', 
                            values = [[1,4],[2,""]], ), )
                    ],
        )
        """

    def testSheetsListResult(self):
        """Test SheetsListResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()