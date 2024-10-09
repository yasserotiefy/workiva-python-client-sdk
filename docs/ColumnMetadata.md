# ColumnMetadata

Metadata about a column

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The width of the column, in points | [optional] 
**hidden** | **bool** | Whether the column is hidden | [optional] 

## Example

```python
from openapi_client.models.column_metadata import ColumnMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ColumnMetadata from a JSON string
column_metadata_instance = ColumnMetadata.from_json(json)
# print the JSON string representation of the object
print(ColumnMetadata.to_json())

# convert the object into a dict
column_metadata_dict = column_metadata_instance.to_dict()
# create an instance of ColumnMetadata from a dict
column_metadata_from_dict = ColumnMetadata.from_dict(column_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


