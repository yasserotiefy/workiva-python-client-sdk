# SheetUpdateApplyFormats

Apply list of format requests to the sheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formats** | [**List[ApplyFormats]**](ApplyFormats.md) | The list of formats to apply to the sheet | 

## Example

```python
from openapi_client.models.sheet_update_apply_formats import SheetUpdateApplyFormats

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateApplyFormats from a JSON string
sheet_update_apply_formats_instance = SheetUpdateApplyFormats.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateApplyFormats.to_json())

# convert the object into a dict
sheet_update_apply_formats_dict = sheet_update_apply_formats_instance.to_dict()
# create an instance of SheetUpdateApplyFormats from a dict
sheet_update_apply_formats_from_dict = SheetUpdateApplyFormats.from_dict(sheet_update_apply_formats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


