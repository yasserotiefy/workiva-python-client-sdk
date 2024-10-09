# RowMetadata

Metadata about a row

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The height of the row, in points | [optional] 
**hidden** | **bool** | Whether the row is hidden | [optional] 
**filtered** | **bool** | Whether the row is filtered | [optional] 

## Example

```python
from openapi_client.models.row_metadata import RowMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RowMetadata from a JSON string
row_metadata_instance = RowMetadata.from_json(json)
# print the JSON string representation of the object
print(RowMetadata.to_json())

# convert the object into a dict
row_metadata_dict = row_metadata_instance.to_dict()
# create an instance of RowMetadata from a dict
row_metadata_from_dict = RowMetadata.from_dict(row_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


