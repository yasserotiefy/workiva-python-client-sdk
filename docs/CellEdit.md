# CellEdit

A single cell edit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row** | **int** | The row of the cell to edit | 
**column** | **int** | The column of the cell to edit | 
**value** | **object** | String, numeric, or boolean value | 

## Example

```python
from openapi_client.models.cell_edit import CellEdit

# TODO update the JSON string below
json = "{}"
# create an instance of CellEdit from a JSON string
cell_edit_instance = CellEdit.from_json(json)
# print the JSON string representation of the object
print(CellEdit.to_json())

# convert the object into a dict
cell_edit_dict = cell_edit_instance.to_dict()
# create an instance of CellEdit from a dict
cell_edit_from_dict = CellEdit.from_dict(cell_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


