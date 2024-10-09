# SheetUpdateApplyBorders

Apply list of border format requests to the sheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**borders** | [**List[ApplyBorders]**](ApplyBorders.md) | The list of border formats to apply to the sheet | 

## Example

```python
from openapi_client.models.sheet_update_apply_borders import SheetUpdateApplyBorders

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateApplyBorders from a JSON string
sheet_update_apply_borders_instance = SheetUpdateApplyBorders.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateApplyBorders.to_json())

# convert the object into a dict
sheet_update_apply_borders_dict = sheet_update_apply_borders_instance.to_dict()
# create an instance of SheetUpdateApplyBorders from a dict
sheet_update_apply_borders_from_dict = SheetUpdateApplyBorders.from_dict(sheet_update_apply_borders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


