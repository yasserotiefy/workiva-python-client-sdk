# SheetUpdateResizeRows

Resize rows to the specified size

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resize_intervals** | [**List[ResizeRowIntervals]**](ResizeRowIntervals.md) |  | 

## Example

```python
from openapi_client.models.sheet_update_resize_rows import SheetUpdateResizeRows

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateResizeRows from a JSON string
sheet_update_resize_rows_instance = SheetUpdateResizeRows.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateResizeRows.to_json())

# convert the object into a dict
sheet_update_resize_rows_dict = sheet_update_resize_rows_instance.to_dict()
# create an instance of SheetUpdateResizeRows from a dict
sheet_update_resize_rows_from_dict = SheetUpdateResizeRows.from_dict(sheet_update_resize_rows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


