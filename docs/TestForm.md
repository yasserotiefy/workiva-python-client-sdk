# TestForm

Describes details of a test form including its ID, name, and test phases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the test form | [optional] 
**name** | **str** | The name of the test form | [optional] 
**test_phases** | [**List[TestPhase]**](TestPhase.md) | An optional array of partial information about the phases on the test form. To include in the response, provide the query parameter &#x60;$expand&#x3D;testPhases&#x60;. To include the phases&#39; matrix digests, provide the parameter &#x60;$expand&#x3D;testPhases,testPhases.matrices&#x60;. | [optional] [readonly] 
**attachments** | [**List[GraphAttachment]**](GraphAttachment.md) | An optional array of partial information about the attachments on the test form. To include in the response, provide the query parameter &#x60;$expand&#x3D;attachments&#x60;. | [optional] [readonly] 

## Example

```python
from openapi_client.models.test_form import TestForm

# TODO update the JSON string below
json = "{}"
# create an instance of TestForm from a JSON string
test_form_instance = TestForm.from_json(json)
# print the JSON string representation of the object
print(TestForm.to_json())

# convert the object into a dict
test_form_dict = test_form_instance.to_dict()
# create an instance of TestForm from a dict
test_form_from_dict = TestForm.from_dict(test_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


