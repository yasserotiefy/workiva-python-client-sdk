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

from openapi_client.models.matrix_column import MatrixColumn

class TestMatrixColumn(unittest.TestCase):
    """MatrixColumn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MatrixColumn:
        """Test MatrixColumn
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatrixColumn`
        """
        model = MatrixColumn()
        if include_optional:
            return MatrixColumn(
                id = 'fbd818ec-4fd1-42ad-9112-3c80e71dc2dc',
                name = 'PO #',
                external_id = 'TA05',
                testable = True
            )
        else:
            return MatrixColumn(
        )
        """

    def testMatrixColumn(self):
        """Test MatrixColumn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()