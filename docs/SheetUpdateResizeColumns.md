# SheetUpdateResizeColumns

Resize columns to the specified size

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resize_intervals** | [**List[ResizeColumnIntervals]**](ResizeColumnIntervals.md) |  | 

## Example

```python
from openapi_client.models.sheet_update_resize_columns import SheetUpdateResizeColumns

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateResizeColumns from a JSON string
sheet_update_resize_columns_instance = SheetUpdateResizeColumns.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateResizeColumns.to_json())

# convert the object into a dict
sheet_update_resize_columns_dict = sheet_update_resize_columns_instance.to_dict()
# create an instance of SheetUpdateResizeColumns from a dict
sheet_update_resize_columns_from_dict = SheetUpdateResizeColumns.from_dict(sheet_update_resize_columns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


