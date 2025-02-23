# SpreadsheetsListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`Spreadsheet`](ref:platform-spreadsheets#spreadsheet) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Spreadsheet]**](Spreadsheet.md) |  | 
**next_link** | **str** | Pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.spreadsheets_list_result import SpreadsheetsListResult

# TODO update the JSON string below
json = "{}"
# create an instance of SpreadsheetsListResult from a JSON string
spreadsheets_list_result_instance = SpreadsheetsListResult.from_json(json)
# print the JSON string representation of the object
print(SpreadsheetsListResult.to_json())

# convert the object into a dict
spreadsheets_list_result_dict = spreadsheets_list_result_instance.to_dict()
# create an instance of SpreadsheetsListResult from a dict
spreadsheets_list_result_from_dict = SpreadsheetsListResult.from_dict(spreadsheets_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


