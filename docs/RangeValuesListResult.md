# RangeValuesListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a single [`RangeValues`](ref:platform-spreadsheets#rangevalues) object, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RangeValues]**](RangeValues.md) |  | 
**next_link** | **str** | Pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.range_values_list_result import RangeValuesListResult

# TODO update the JSON string below
json = "{}"
# create an instance of RangeValuesListResult from a JSON string
range_values_list_result_instance = RangeValuesListResult.from_json(json)
# print the JSON string representation of the object
print(RangeValuesListResult.to_json())

# convert the object into a dict
range_values_list_result_dict = range_values_list_result_instance.to_dict()
# create an instance of RangeValuesListResult from a dict
range_values_list_result_from_dict = RangeValuesListResult.from_dict(range_values_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


