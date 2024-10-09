# CellFormatIndent

Indentation of content in the cell

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** | The size of the indent | 
**unit** | **str** | The unit of the size | 

## Example

```python
from openapi_client.models.cell_format_indent import CellFormatIndent

# TODO update the JSON string below
json = "{}"
# create an instance of CellFormatIndent from a JSON string
cell_format_indent_instance = CellFormatIndent.from_json(json)
# print the JSON string representation of the object
print(CellFormatIndent.to_json())

# convert the object into a dict
cell_format_indent_dict = cell_format_indent_instance.to_dict()
# create an instance of CellFormatIndent from a dict
cell_format_indent_from_dict = CellFormatIndent.from_dict(cell_format_indent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


