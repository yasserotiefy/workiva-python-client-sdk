# SheetUpdateEditCells

Edit a list of cells

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cells** | [**List[CellEdit]**](CellEdit.md) | The cells to edit | 
**options** | [**SheetUpdateEditCellsOptions**](SheetUpdateEditCellsOptions.md) |  | [optional] 

## Example

```python
from openapi_client.models.sheet_update_edit_cells import SheetUpdateEditCells

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateEditCells from a JSON string
sheet_update_edit_cells_instance = SheetUpdateEditCells.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateEditCells.to_json())

# convert the object into a dict
sheet_update_edit_cells_dict = sheet_update_edit_cells_instance.to_dict()
# create an instance of SheetUpdateEditCells from a dict
sheet_update_edit_cells_from_dict = SheetUpdateEditCells.from_dict(sheet_update_edit_cells_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


