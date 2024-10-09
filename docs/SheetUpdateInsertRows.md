# SheetUpdateInsertRows

Insert rows into the sheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insertions** | [**List[Insertion]**](Insertion.md) | List of row insertions | 
**inherit_from** | [**InheritFrom**](InheritFrom.md) |  | 

## Example

```python
from openapi_client.models.sheet_update_insert_rows import SheetUpdateInsertRows

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateInsertRows from a JSON string
sheet_update_insert_rows_instance = SheetUpdateInsertRows.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateInsertRows.to_json())

# convert the object into a dict
sheet_update_insert_rows_dict = sheet_update_insert_rows_instance.to_dict()
# create an instance of SheetUpdateInsertRows from a dict
sheet_update_insert_rows_from_dict = SheetUpdateInsertRows.from_dict(sheet_update_insert_rows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


