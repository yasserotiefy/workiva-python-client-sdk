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

from openapi_client.models.cell_format import CellFormat

class TestCellFormat(unittest.TestCase):
    """CellFormat unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CellFormat:
        """Test CellFormat
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CellFormat`
        """
        model = CellFormat()
        if include_optional:
            return CellFormat(
                indent = openapi_client.models.cell_format_indent.CellFormat_indent(
                    value = 0, 
                    unit = 'INCHES', ),
                horizontal_align = 'LEFT',
                vertical_align = 'TOP',
                text_rotation = 'HORIZONTAL',
                background_color = '#000000',
                leader_dots = 'NARROW',
                borders = openapi_client.models.cell_format_borders.CellFormat_borders(
                    top = {"style":"SINGLE","weight":2,"color":"#000000"}, 
                    bottom = {"style":"SINGLE","weight":2,"color":"#000000"}, 
                    left = {"style":"SINGLE","weight":2,"color":"#000000"}, 
                    right = {"style":"SINGLE","weight":2,"color":"#000000"}, )
            )
        else:
            return CellFormat(
        )
        """

    def testCellFormat(self):
        """Test CellFormat"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()