# TestPhasesListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`TestPhase`](ref:platform-testforms#testphase) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TestPhase]**](TestPhase.md) | A list of &#x60;TestPhase&#x60; objects | 
**next_link** | **str** | The pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.test_phases_list_result import TestPhasesListResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestPhasesListResult from a JSON string
test_phases_list_result_instance = TestPhasesListResult.from_json(json)
# print the JSON string representation of the object
print(TestPhasesListResult.to_json())

# convert the object into a dict
test_phases_list_result_dict = test_phases_list_result_instance.to_dict()
# create an instance of TestPhasesListResult from a dict
test_phases_list_result_from_dict = TestPhasesListResult.from_dict(test_phases_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

