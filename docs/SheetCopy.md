# SheetCopy

Details about the destination spreadsheet and, optionally, the destination sheet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spreadsheet** | **str** | The unique identifier of the spreadsheet to copy a sheet into | 
**sheet_index** | **int** | The integer index of where within the siblings to place the new sheet; 0 by default. To place the sheet at the end of its siblings, use the special value -1. | [optional] [default to 0]
**sheet_parent** | **str** | The ID of the parent sheet to copy the sheet into. To place the sheet at the top level of the spreadsheet, use the default null. | [optional] 
**sheet_name** | **str** | The name of the new sheet, if different than the source sheet. | [optional] 

## Example

```python
from openapi_client.models.sheet_copy import SheetCopy

# TODO update the JSON string below
json = "{}"
# create an instance of SheetCopy from a JSON string
sheet_copy_instance = SheetCopy.from_json(json)
# print the JSON string representation of the object
print(SheetCopy.to_json())

# convert the object into a dict
sheet_copy_dict = sheet_copy_instance.to_dict()
# create an instance of SheetCopy from a dict
sheet_copy_from_dict = SheetCopy.from_dict(sheet_copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


