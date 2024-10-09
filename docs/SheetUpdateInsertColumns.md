# SheetUpdateInsertColumns

Insert columns into the sheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insertions** | [**List[Insertion]**](Insertion.md) | List of column insertions | 
**inherit_from** | [**InheritFrom**](InheritFrom.md) |  | 

## Example

```python
from openapi_client.models.sheet_update_insert_columns import SheetUpdateInsertColumns

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateInsertColumns from a JSON string
sheet_update_insert_columns_instance = SheetUpdateInsertColumns.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateInsertColumns.to_json())

# convert the object into a dict
sheet_update_insert_columns_dict = sheet_update_insert_columns_instance.to_dict()
# create an instance of SheetUpdateInsertColumns from a dict
sheet_update_insert_columns_from_dict = SheetUpdateInsertColumns.from_dict(sheet_update_insert_columns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


