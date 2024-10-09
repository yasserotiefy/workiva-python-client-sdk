# ApplyBorders

Apply borders to ranges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ranges** | [**List[Range]**](Range.md) | The ranges to apply borders | 
**top** | [**Border**](Border.md) |  | [optional] 
**bottom** | [**Border**](Border.md) |  | [optional] 
**left** | [**Border**](Border.md) |  | [optional] 
**right** | [**Border**](Border.md) |  | [optional] 
**inner_horizontal** | [**Border**](Border.md) |  | [optional] 
**inner_vertical** | [**Border**](Border.md) |  | [optional] 

## Example

```python
from openapi_client.models.apply_borders import ApplyBorders

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyBorders from a JSON string
apply_borders_instance = ApplyBorders.from_json(json)
# print the JSON string representation of the object
print(ApplyBorders.to_json())

# convert the object into a dict
apply_borders_dict = apply_borders_instance.to_dict()
# create an instance of ApplyBorders from a dict
apply_borders_from_dict = ApplyBorders.from_dict(apply_borders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


