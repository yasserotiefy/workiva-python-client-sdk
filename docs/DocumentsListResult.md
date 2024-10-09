# DocumentsListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`Document`](ref:platform-documents#document) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Document]**](Document.md) |  | 
**next_link** | **str** | Pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.documents_list_result import DocumentsListResult

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsListResult from a JSON string
documents_list_result_instance = DocumentsListResult.from_json(json)
# print the JSON string representation of the object
print(DocumentsListResult.to_json())

# convert the object into a dict
documents_list_result_dict = documents_list_result_instance.to_dict()
# create an instance of DocumentsListResult from a dict
documents_list_result_from_dict = DocumentsListResult.from_dict(documents_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


