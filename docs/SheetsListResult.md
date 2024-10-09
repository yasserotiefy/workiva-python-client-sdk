# SheetsListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`Sheet`](ref:platform-spreadsheets#sheet) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Sheet]**](Sheet.md) |  | 
**next_link** | **str** | Pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.sheets_list_result import SheetsListResult

# TODO update the JSON string below
json = "{}"
# create an instance of SheetsListResult from a JSON string
sheets_list_result_instance = SheetsListResult.from_json(json)
# print the JSON string representation of the object
print(SheetsListResult.to_json())

# convert the object into a dict
sheets_list_result_dict = sheets_list_result_instance.to_dict()
# create an instance of SheetsListResult from a dict
sheets_list_result_from_dict = SheetsListResult.from_dict(sheets_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


