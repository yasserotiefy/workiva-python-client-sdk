# TestPhase

Describes details of a test phase, including its ID and name

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the test phase | [optional] 
**name** | **str** | The name of the test phase | [optional] 
**attachments** | [**List[GraphAttachment]**](GraphAttachment.md) | An optional array of partial information about the attachments on the test phase. To include in the response, provide the query string &#x60;$expand&#x3D;attachments&#x60;. | [optional] [readonly] 
**matrices** | [**List[Matrix]**](Matrix.md) | An optional array of partial information about the matrices on the test phase. To include in the response, provide the query string, &#x60;$expand&#x3D;matrices&#x60;. | [optional] [readonly] 

## Example

```python
from openapi_client.models.test_phase import TestPhase

# TODO update the JSON string below
json = "{}"
# create an instance of TestPhase from a JSON string
test_phase_instance = TestPhase.from_json(json)
# print the JSON string representation of the object
print(TestPhase.to_json())

# convert the object into a dict
test_phase_dict = test_phase_instance.to_dict()
# create an instance of TestPhase from a dict
test_phase_from_dict = TestPhase.from_dict(test_phase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


