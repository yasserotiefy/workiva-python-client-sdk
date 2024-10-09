# EffectiveFormats

Formats that could be directly applied or applied through inheritance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_format** | [**TextFormat**](TextFormat.md) |  | [optional] 
**value_format** | [**ValueFormat**](ValueFormat.md) |  | [optional] 
**cell_format** | [**CellFormat**](CellFormat.md) |  | [optional] 

## Example

```python
from openapi_client.models.effective_formats import EffectiveFormats

# TODO update the JSON string below
json = "{}"
# create an instance of EffectiveFormats from a JSON string
effective_formats_instance = EffectiveFormats.from_json(json)
# print the JSON string representation of the object
print(EffectiveFormats.to_json())

# convert the object into a dict
effective_formats_dict = effective_formats_instance.to_dict()
# create an instance of EffectiveFormats from a dict
effective_formats_from_dict = EffectiveFormats.from_dict(effective_formats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


