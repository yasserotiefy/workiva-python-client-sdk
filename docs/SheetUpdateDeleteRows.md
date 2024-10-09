# SheetUpdateDeleteRows

Delete rows from the sheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intervals** | [**List[Interval]**](Interval.md) |  | 
**force** | **bool** | Force the deletion of source links, xbrl facts, ESG connections, etc | [optional] 

## Example

```python
from openapi_client.models.sheet_update_delete_rows import SheetUpdateDeleteRows

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateDeleteRows from a JSON string
sheet_update_delete_rows_instance = SheetUpdateDeleteRows.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateDeleteRows.to_json())

# convert the object into a dict
sheet_update_delete_rows_dict = sheet_update_delete_rows_instance.to_dict()
# create an instance of SheetUpdateDeleteRows from a dict
sheet_update_delete_rows_from_dict = SheetUpdateDeleteRows.from_dict(sheet_update_delete_rows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


