# SheetUpdateResizeRowsToFit

Auto-size rows to fit content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervals** | [**List[Interval]**](Interval.md) | The intervals of rows to resize | 

## Example

```python
from openapi_client.models.sheet_update_resize_rows_to_fit import SheetUpdateResizeRowsToFit

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateResizeRowsToFit from a JSON string
sheet_update_resize_rows_to_fit_instance = SheetUpdateResizeRowsToFit.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateResizeRowsToFit.to_json())

# convert the object into a dict
sheet_update_resize_rows_to_fit_dict = sheet_update_resize_rows_to_fit_instance.to_dict()
# create an instance of SheetUpdateResizeRowsToFit from a dict
sheet_update_resize_rows_to_fit_from_dict = SheetUpdateResizeRowsToFit.from_dict(sheet_update_resize_rows_to_fit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


