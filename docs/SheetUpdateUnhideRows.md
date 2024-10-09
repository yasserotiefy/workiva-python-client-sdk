# SheetUpdateUnhideRows

Unhide rows in the sheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervals** | [**List[Interval]**](Interval.md) | The intervals of rows to unhide | 

## Example

```python
from openapi_client.models.sheet_update_unhide_rows import SheetUpdateUnhideRows

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateUnhideRows from a JSON string
sheet_update_unhide_rows_instance = SheetUpdateUnhideRows.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateUnhideRows.to_json())

# convert the object into a dict
sheet_update_unhide_rows_dict = sheet_update_unhide_rows_instance.to_dict()
# create an instance of SheetUpdateUnhideRows from a dict
sheet_update_unhide_rows_from_dict = SheetUpdateUnhideRows.from_dict(sheet_update_unhide_rows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


