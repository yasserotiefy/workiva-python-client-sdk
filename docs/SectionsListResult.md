# SectionsListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`Section`](ref:platform-documents#section) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Section]**](Section.md) |  | 
**next_link** | **str** | Pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.sections_list_result import SectionsListResult

# TODO update the JSON string below
json = "{}"
# create an instance of SectionsListResult from a JSON string
sections_list_result_instance = SectionsListResult.from_json(json)
# print the JSON string representation of the object
print(SectionsListResult.to_json())

# convert the object into a dict
sections_list_result_dict = sections_list_result_instance.to_dict()
# create an instance of SectionsListResult from a dict
sections_list_result_from_dict = SectionsListResult.from_dict(sections_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


