# SheetUpdateHideRows

Hide rows in the sheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervals** | [**List[Interval]**](Interval.md) | The intervals of rows to hide | 
**force** | **bool** | Force the hiding of footnotes | [optional] 

## Example

```python
from openapi_client.models.sheet_update_hide_rows import SheetUpdateHideRows

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateHideRows from a JSON string
sheet_update_hide_rows_instance = SheetUpdateHideRows.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateHideRows.to_json())

# convert the object into a dict
sheet_update_hide_rows_dict = sheet_update_hide_rows_instance.to_dict()
# create an instance of SheetUpdateHideRows from a dict
sheet_update_hide_rows_from_dict = SheetUpdateHideRows.from_dict(sheet_update_hide_rows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


