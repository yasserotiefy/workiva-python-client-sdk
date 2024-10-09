# SheetUpdateClearFormats

Clear formats from ranges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ranges** | [**List[Range]**](Range.md) | The ranges to clear formats | 
**text_format_fields** | **List[str]** | List of TextFormat fields to clear. Use \&quot;*\&quot; to clear all fields. | [optional] 
**value_format_fields** | **List[str]** | List of ValueFormat fields to clear. Use \&quot;*\&quot; to clear all fields. | [optional] 
**cell_format_fields** | **List[str]** | List of CellFormat fields to clear. Use \&quot;*\&quot; to clear all fields. | [optional] 

## Example

```python
from openapi_client.models.sheet_update_clear_formats import SheetUpdateClearFormats

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateClearFormats from a JSON string
sheet_update_clear_formats_instance = SheetUpdateClearFormats.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateClearFormats.to_json())

# convert the object into a dict
sheet_update_clear_formats_dict = sheet_update_clear_formats_instance.to_dict()
# create an instance of SheetUpdateClearFormats from a dict
sheet_update_clear_formats_from_dict = SheetUpdateClearFormats.from_dict(sheet_update_clear_formats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


