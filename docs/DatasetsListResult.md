# DatasetsListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of partial [`Dataset`](ref:platform-spreadsheets#dataset) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Dataset]**](Dataset.md) |  | 
**next_link** | **str** | Pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.datasets_list_result import DatasetsListResult

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetsListResult from a JSON string
datasets_list_result_instance = DatasetsListResult.from_json(json)
# print the JSON string representation of the object
print(DatasetsListResult.to_json())

# convert the object into a dict
datasets_list_result_dict = datasets_list_result_instance.to_dict()
# create an instance of DatasetsListResult from a dict
datasets_list_result_from_dict = DatasetsListResult.from_dict(datasets_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

