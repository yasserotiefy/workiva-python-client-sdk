# RecordsListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`Record`](ref:platform-graph#record) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Record]**](Record.md) |  | [optional] 
**next_link** | **str** | Pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.records_list_result import RecordsListResult

# TODO update the JSON string below
json = "{}"
# create an instance of RecordsListResult from a JSON string
records_list_result_instance = RecordsListResult.from_json(json)
# print the JSON string representation of the object
print(RecordsListResult.to_json())

# convert the object into a dict
records_list_result_dict = records_list_result_instance.to_dict()
# create an instance of RecordsListResult from a dict
records_list_result_from_dict = RecordsListResult.from_dict(records_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


