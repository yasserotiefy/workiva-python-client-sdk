# ErrorResponse

Error response that indicates that the service is not able to process the incoming request. The reason is provided in the error message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | One of a server-defined set of error codes. | [optional] 
**message** | **str** | A human-readable representation of the error. | [optional] 
**target** | **str** | The target of the error. | [optional] 
**details** | [**List[ErrorDetails]**](ErrorDetails.md) |  | [optional] 
**documentation_url** | **str** | Link to some documentation relevant to the issue or endpoint in use. | [optional] 

## Example

```python
from openapi_client.models.error_response import ErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse from a JSON string
error_response_instance = ErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse.to_json())

# convert the object into a dict
error_response_dict = error_response_instance.to_dict()
# create an instance of ErrorResponse from a dict
error_response_from_dict = ErrorResponse.from_dict(error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


