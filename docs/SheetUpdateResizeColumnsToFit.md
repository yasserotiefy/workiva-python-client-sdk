# SheetUpdateResizeColumnsToFit

Auto-size columns to fit content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervals** | [**List[Interval]**](Interval.md) | The intervals of columns to resize | 

## Example

```python
from openapi_client.models.sheet_update_resize_columns_to_fit import SheetUpdateResizeColumnsToFit

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateResizeColumnsToFit from a JSON string
sheet_update_resize_columns_to_fit_instance = SheetUpdateResizeColumnsToFit.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateResizeColumnsToFit.to_json())

# convert the object into a dict
sheet_update_resize_columns_to_fit_dict = sheet_update_resize_columns_to_fit_instance.to_dict()
# create an instance of SheetUpdateResizeColumnsToFit from a dict
sheet_update_resize_columns_to_fit_from_dict = SheetUpdateResizeColumnsToFit.from_dict(sheet_update_resize_columns_to_fit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


