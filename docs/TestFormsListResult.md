# TestFormsListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`TestForm`](ref:platform-testforms#testform) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TestForm]**](TestForm.md) | A list of &#x60;Matrix&#x60; objects | 
**next_link** | **str** | The pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.test_forms_list_result import TestFormsListResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestFormsListResult from a JSON string
test_forms_list_result_instance = TestFormsListResult.from_json(json)
# print the JSON string representation of the object
print(TestFormsListResult.to_json())

# convert the object into a dict
test_forms_list_result_dict = test_forms_list_result_instance.to_dict()
# create an instance of TestFormsListResult from a dict
test_forms_list_result_from_dict = TestFormsListResult.from_dict(test_forms_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


