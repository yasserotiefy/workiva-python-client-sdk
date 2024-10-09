# Sheet

Details about the sheet, including its ID and name. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the sheet | [optional] 
**name** | **str** | The name of the sheet | [optional] 
**parent** | [**Sheet**](Sheet.md) |  | [optional] 
**index** | **int** | The integer index of the sheet relative to its parent sheet or to the spreadsheet, if no parent sheet. To position a sheet at the end of its siblings, use the special value -1. | [optional] 
**children** | [**List[Sheet]**](Sheet.md) | An array of partial information about any child sheets | [optional] [readonly] 
**dataset** | [**Dataset**](Dataset.md) |  | [optional] 

## Example

```python
from openapi_client.models.sheet import Sheet

# TODO update the JSON string below
json = "{}"
# create an instance of Sheet from a JSON string
sheet_instance = Sheet.from_json(json)
# print the JSON string representation of the object
print(Sheet.to_json())

# convert the object into a dict
sheet_dict = sheet_instance.to_dict()
# create an instance of Sheet from a dict
sheet_from_dict = Sheet.from_dict(sheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


