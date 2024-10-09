# File

Details about the file, including its ID, name, kind, and milestone dates. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the file | [optional] [readonly] 
**name** | **str** | Name of the file | [optional] 
**container** | **str** | The unique identifier of the container that houses the file, such as a folder. If empty, the root folder is the container.  | [optional] [default to '']
**kind** | **str** | Kind of the file | [optional] 
**type** | **str** | Type of the file | [optional] [readonly] 
**template** | **bool** |  | [optional] [readonly] 
**created** | [**Action**](Action.md) |  | [optional] 
**modified** | [**Action**](Action.md) |  | [optional] 

## Example

```python
from openapi_client.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print(File.to_json())

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_from_dict = File.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


