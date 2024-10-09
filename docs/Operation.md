# Operation

Details about the operation, including its ID, status, milestone dates, and the url of the resource upon successful completion of the operation. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the operation | [optional] [readonly] 
**status** | **str** | The current status of the operation | [optional] [readonly] 
**created** | [**Action**](Action.md) |  | [optional] 
**updated** | [**Action**](Action.md) |  | [optional] 
**resource_url** | **str** | The link to the resulting resource | [optional] [readonly] 
**original_request** | **str** | This is the Request ID that initiated this async operation. Giving this ID to support can help track issues with your operations. | [optional] [readonly] 
**details** | [**List[OperationDetail]**](OperationDetail.md) | A list of additional details about the operation | [optional] [readonly] 

## Example

```python
from openapi_client.models.operation import Operation

# TODO update the JSON string below
json = "{}"
# create an instance of Operation from a JSON string
operation_instance = Operation.from_json(json)
# print the JSON string representation of the object
print(Operation.to_json())

# convert the object into a dict
operation_dict = operation_instance.to_dict()
# create an instance of Operation from a dict
operation_from_dict = Operation.from_dict(operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


