# Spreadsheet

Details about the spreadsheet, including its ID, name, and milestone dates. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the spreadsheet | [optional] [readonly] 
**name** | **str** | The name of the spreadsheet | [optional] [readonly] 
**template** | **bool** | Whether the spreadsheet is a template | [optional] [readonly] 
**created** | [**Action**](Action.md) |  | [optional] 
**modified** | [**Action**](Action.md) |  | [optional] 
**sheets** | [**List[Sheet]**](Sheet.md) | An array of partial information about the sheets in this spreadsheet. Optionally included in the response when the $expand query parameter is provided. | [optional] [readonly] 

## Example

```python
from openapi_client.models.spreadsheet import Spreadsheet

# TODO update the JSON string below
json = "{}"
# create an instance of Spreadsheet from a JSON string
spreadsheet_instance = Spreadsheet.from_json(json)
# print the JSON string representation of the object
print(Spreadsheet.to_json())

# convert the object into a dict
spreadsheet_dict = spreadsheet_instance.to_dict()
# create an instance of Spreadsheet from a dict
spreadsheet_from_dict = Spreadsheet.from_dict(spreadsheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


