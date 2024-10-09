# ApplyFormats

Apply formats to a list of ranges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ranges** | [**List[Range]**](Range.md) | The ranges to format | 
**text_format** | [**TextFormat**](TextFormat.md) |  | [optional] 
**value_format** | [**ValueFormat**](ValueFormat.md) |  | [optional] 
**cell_format** | [**CellFormat**](CellFormat.md) |  | [optional] 

## Example

```python
from openapi_client.models.apply_formats import ApplyFormats

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyFormats from a JSON string
apply_formats_instance = ApplyFormats.from_json(json)
# print the JSON string representation of the object
print(ApplyFormats.to_json())

# convert the object into a dict
apply_formats_dict = apply_formats_instance.to_dict()
# create an instance of ApplyFormats from a dict
apply_formats_from_dict = ApplyFormats.from_dict(apply_formats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


