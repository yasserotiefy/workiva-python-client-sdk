# CellFormatBorders

The borders applied to a cell. Borders may be set by setting `applyBorders`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | [**Border**](Border.md) |  | [optional] 
**bottom** | [**Border**](Border.md) |  | [optional] 
**left** | [**Border**](Border.md) |  | [optional] 
**right** | [**Border**](Border.md) |  | [optional] 

## Example

```python
from openapi_client.models.cell_format_borders import CellFormatBorders

# TODO update the JSON string below
json = "{}"
# create an instance of CellFormatBorders from a JSON string
cell_format_borders_instance = CellFormatBorders.from_json(json)
# print the JSON string representation of the object
print(CellFormatBorders.to_json())

# convert the object into a dict
cell_format_borders_dict = cell_format_borders_instance.to_dict()
# create an instance of CellFormatBorders from a dict
cell_format_borders_from_dict = CellFormatBorders.from_dict(cell_format_borders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


