# SheetUpdateUnhideColumns

Unhide columns in the sheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervals** | [**List[Interval]**](Interval.md) | The intervals of columns to unhide | 

## Example

```python
from openapi_client.models.sheet_update_unhide_columns import SheetUpdateUnhideColumns

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateUnhideColumns from a JSON string
sheet_update_unhide_columns_instance = SheetUpdateUnhideColumns.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateUnhideColumns.to_json())

# convert the object into a dict
sheet_update_unhide_columns_dict = sheet_update_unhide_columns_instance.to_dict()
# create an instance of SheetUpdateUnhideColumns from a dict
sheet_update_unhide_columns_from_dict = SheetUpdateUnhideColumns.from_dict(sheet_update_unhide_columns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


