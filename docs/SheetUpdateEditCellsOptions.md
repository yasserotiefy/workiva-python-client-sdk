# SheetUpdateEditCellsOptions

Edit cells options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_entered_in_scaling** | **bool** | Whether or not to apply &#x60;enteredIn&#x60; scaling  | [optional] [default to False]
**skip_edit_merge_children** | **bool** | Whether or not to skip edits to merge child cells  | [optional] [default to False]

## Example

```python
from openapi_client.models.sheet_update_edit_cells_options import SheetUpdateEditCellsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateEditCellsOptions from a JSON string
sheet_update_edit_cells_options_instance = SheetUpdateEditCellsOptions.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateEditCellsOptions.to_json())

# convert the object into a dict
sheet_update_edit_cells_options_dict = sheet_update_edit_cells_options_instance.to_dict()
# create an instance of SheetUpdateEditCellsOptions from a dict
sheet_update_edit_cells_options_from_dict = SheetUpdateEditCellsOptions.from_dict(sheet_update_edit_cells_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


