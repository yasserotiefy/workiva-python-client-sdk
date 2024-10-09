# SheetData

Details about the section, including its ID and name. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**Range**](Range.md) |  | [optional] 
**merges** | [**List[Range]**](Range.md) | Merged ranges that intersect with the request range | [optional] 
**row_metadata** | [**List[RowMetadata]**](RowMetadata.md) | Metadata about the rows in the request range | [optional] 
**column_metadata** | [**List[ColumnMetadata]**](ColumnMetadata.md) | Metadata about the columns in the request range | [optional] 
**cells** | **List[List[CellData]]** | Cell data in row-major order | [optional] 

## Example

```python
from openapi_client.models.sheet_data import SheetData

# TODO update the JSON string below
json = "{}"
# create an instance of SheetData from a JSON string
sheet_data_instance = SheetData.from_json(json)
# print the JSON string representation of the object
print(SheetData.to_json())

# convert the object into a dict
sheet_data_dict = sheet_data_instance.to_dict()
# create an instance of SheetData from a dict
sheet_data_from_dict = SheetData.from_dict(sheet_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


