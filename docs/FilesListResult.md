# FilesListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`File`](ref:platform-files#file) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[File]**](File.md) |  | 
**next_link** | **str** | Pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.files_list_result import FilesListResult

# TODO update the JSON string below
json = "{}"
# create an instance of FilesListResult from a JSON string
files_list_result_instance = FilesListResult.from_json(json)
# print the JSON string representation of the object
print(FilesListResult.to_json())

# convert the object into a dict
files_list_result_dict = files_list_result_instance.to_dict()
# create an instance of FilesListResult from a dict
files_list_result_from_dict = FilesListResult.from_dict(files_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


