# JSONPatchOperation

Represents a single JSON Patch operation. For more information, refer to the [PATCH Update documentation](ref:platform-patch-updates). 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | 
**path** | **str** |  | 
**value** | **object** |  | [optional] 
**var_from** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.json_patch_operation import JSONPatchOperation

# TODO update the JSON string below
json = "{}"
# create an instance of JSONPatchOperation from a JSON string
json_patch_operation_instance = JSONPatchOperation.from_json(json)
# print the JSON string representation of the object
print(JSONPatchOperation.to_json())

# convert the object into a dict
json_patch_operation_dict = json_patch_operation_instance.to_dict()
# create an instance of JSONPatchOperation from a dict
json_patch_operation_from_dict = JSONPatchOperation.from_dict(json_patch_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


