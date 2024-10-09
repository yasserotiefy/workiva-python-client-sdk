# SheetUpdate

An update to a sheet. Only a single field on the SheetUpdate may be set per request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit_cells** | [**SheetUpdateEditCells**](SheetUpdateEditCells.md) |  | [optional] 
**edit_range** | [**SheetUpdateEditRange**](SheetUpdateEditRange.md) |  | [optional] 
**apply_formats** | [**SheetUpdateApplyFormats**](SheetUpdateApplyFormats.md) |  | [optional] 
**clear_formats** | [**SheetUpdateClearFormats**](SheetUpdateClearFormats.md) |  | [optional] 
**insert_rows** | [**SheetUpdateInsertRows**](SheetUpdateInsertRows.md) |  | [optional] 
**insert_columns** | [**SheetUpdateInsertColumns**](SheetUpdateInsertColumns.md) |  | [optional] 
**delete_rows** | [**SheetUpdateDeleteRows**](SheetUpdateDeleteRows.md) |  | [optional] 
**delete_columns** | [**SheetUpdateDeleteColumns**](SheetUpdateDeleteColumns.md) |  | [optional] 
**hide_rows** | [**SheetUpdateHideRows**](SheetUpdateHideRows.md) |  | [optional] 
**hide_columns** | [**SheetUpdateHideColumns**](SheetUpdateHideColumns.md) |  | [optional] 
**unhide_rows** | [**SheetUpdateUnhideRows**](SheetUpdateUnhideRows.md) |  | [optional] 
**unhide_columns** | [**SheetUpdateUnhideColumns**](SheetUpdateUnhideColumns.md) |  | [optional] 
**resize_rows** | [**SheetUpdateResizeRows**](SheetUpdateResizeRows.md) |  | [optional] 
**resize_rows_to_fit** | [**SheetUpdateResizeRowsToFit**](SheetUpdateResizeRowsToFit.md) |  | [optional] 
**resize_columns** | [**SheetUpdateResizeColumns**](SheetUpdateResizeColumns.md) |  | [optional] 
**resize_columns_to_fit** | [**SheetUpdateResizeColumnsToFit**](SheetUpdateResizeColumnsToFit.md) |  | [optional] 
**merge_ranges** | [**SheetUpdateMergeRanges**](SheetUpdateMergeRanges.md) |  | [optional] 
**unmerge_ranges** | [**SheetUpdateUnmergeRanges**](SheetUpdateUnmergeRanges.md) |  | [optional] 
**apply_borders** | [**SheetUpdateApplyBorders**](SheetUpdateApplyBorders.md) |  | [optional] 
**clear_borders** | [**SheetUpdateClearBorders**](SheetUpdateClearBorders.md) |  | [optional] 

## Example

```python
from openapi_client.models.sheet_update import SheetUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdate from a JSON string
sheet_update_instance = SheetUpdate.from_json(json)
# print the JSON string representation of the object
print(SheetUpdate.to_json())

# convert the object into a dict
sheet_update_dict = sheet_update_instance.to_dict()
# create an instance of SheetUpdate from a dict
sheet_update_from_dict = SheetUpdate.from_dict(sheet_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


