# SheetUpdateHideColumns

Hide columns in the sheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervals** | [**List[Interval]**](Interval.md) | The intervals of columns to hide | 
**force** | **bool** | Force the hiding of footnotes | [optional] 

## Example

```python
from openapi_client.models.sheet_update_hide_columns import SheetUpdateHideColumns

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateHideColumns from a JSON string
sheet_update_hide_columns_instance = SheetUpdateHideColumns.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateHideColumns.to_json())

# convert the object into a dict
sheet_update_hide_columns_dict = sheet_update_hide_columns_instance.to_dict()
# create an instance of SheetUpdateHideColumns from a dict
sheet_update_hide_columns_from_dict = SheetUpdateHideColumns.from_dict(sheet_update_hide_columns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


