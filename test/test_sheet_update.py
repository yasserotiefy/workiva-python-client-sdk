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

from openapi_client.models.sheet_update import SheetUpdate

class TestSheetUpdate(unittest.TestCase):
    """SheetUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SheetUpdate:
        """Test SheetUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SheetUpdate`
        """
        model = SheetUpdate()
        if include_optional:
            return SheetUpdate(
                edit_cells = {"cells":[{"column":0,"row":0,"value":"Alpha One"},{"column":1,"row":0,"value":"Bravo One"},{"column":0,"row":1,"value":"Alpha Two"},{"column":1,"row":1,"value":"Bravo Two"}]},
                edit_range = {"range":{"startColumn":0,"startRow":0,"stopColumn":1,"stopRow":1},"values":[["Alpha One","Bravo One"],["Alpha Two","Bravo Two"]]},
                apply_formats = {"formats":[{"cellFormat":{"backgroundColor":"#d0e0f0"},"ranges":[{"startColumn":0,"startRow":0,"stopColumn":null,"stopRow":0}],"textFormat":{"bold":true},"valueFormat":{"valueFormatType":"TEXT"}}]},
                clear_formats = {"cellFormatFields":["*"],"ranges":[{"startColumn":0,"startRow":0,"stopColumn":null,"stopRow":0}],"textFormatFields":["*"],"valueFormatFields":["*"]},
                insert_rows = {"inheritFrom":"BEFORE","insertions":[{"count":2,"index":6}]},
                insert_columns = {"inheritFrom":"BEFORE","insertions":[{"count":1,"index":3}]},
                delete_rows = {"force":true,"intervals":[{"start":5,"end":7}]},
                delete_columns = {"force":true,"intervals":[{"start":2,"end":3}]},
                hide_rows = {"force":true,"intervals":[{"start":7,"end":9}]},
                hide_columns = {"force":true,"intervals":[{"start":4,"end":5}]},
                unhide_rows = {"intervals":[{"start":7,"end":9}]},
                unhide_columns = {"intervals":[{"start":4,"end":5}]},
                resize_rows = {"resizeIntervals":[{"size":24,"intervals":[{"start":0,"end":3}]}]},
                resize_rows_to_fit = {"intervals":[{"start":0,"end":3}]},
                resize_columns = {"resizeIntervals":[{"size":96,"intervals":[{"start":0,"end":3}]}]},
                resize_columns_to_fit = {"intervals":[{"start":0,"end":3}]},
                merge_ranges = {"force":true,"mergeType":"HORIZONTAL","ranges":[{"startRow":4,"startColumn":0,"stopRow":7,"stopColumn":1}]},
                unmerge_ranges = {"ranges":[{"startRow":4,"startColumn":0,"stopRow":7,"stopColumn":1}]},
                apply_borders = {"borders":[{"ranges":[{"startRow":0,"startColumn":0,"stopRow":3,"stopColumn":3}],"top":{"style":"SINGLE","weight":2,"color":"#000000"},"bottom":{"style":"SINGLE","weight":2,"color":"#000000"},"left":{"style":"SINGLE","weight":2,"color":"#000000"},"right":{"style":"SINGLE","weight":2,"color":"#000000"},"innerHorizontal":{"style":"DASHED1","weight":1,"color":"#808080"},"innerVertical":{"style":"DASHED1","weight":1,"color":"#808080"}}]},
                clear_borders = {"ranges":[{"startRow":0,"startColumn":0,"stopRow":3,"stopColumn":3}]}
            )
        else:
            return SheetUpdate(
        )
        """

    def testSheetUpdate(self):
        """Test SheetUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
