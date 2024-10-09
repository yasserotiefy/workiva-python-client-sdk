# CellFormat

Cell Formats. Fields that are omitted will be ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indent** | [**CellFormatIndent**](CellFormatIndent.md) |  | [optional] 
**horizontal_align** | **str** | The horizontal alignment of the content in the cell | [optional] 
**vertical_align** | **str** | The vertical alignment of the content in the cell | [optional] 
**text_rotation** | **str** | The text orientation | [optional] 
**background_color** | **str** | A hex color code | [optional] [default to '#000000']
**leader_dots** | **str** | The leader dot pattern to show on the cell | [optional] 
**borders** | [**CellFormatBorders**](CellFormatBorders.md) |  | [optional] 

## Example

```python
from openapi_client.models.cell_format import CellFormat

# TODO update the JSON string below
json = "{}"
# create an instance of CellFormat from a JSON string
cell_format_instance = CellFormat.from_json(json)
# print the JSON string representation of the object
print(CellFormat.to_json())

# convert the object into a dict
cell_format_dict = cell_format_instance.to_dict()
# create an instance of CellFormat from a dict
cell_format_from_dict = CellFormat.from_dict(cell_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


