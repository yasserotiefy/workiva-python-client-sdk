# MatrixColumn

Details about a matrix column including its ID and name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the matrix column | [optional] 
**name** | **str** | The name of the matrix column | [optional] 
**external_id** | **str** | A user defined external ID for the column | [optional] 
**testable** | **bool** | Whether the column is testable | [optional] [readonly] 

## Example

```python
from openapi_client.models.matrix_column import MatrixColumn

# TODO update the JSON string below
json = "{}"
# create an instance of MatrixColumn from a JSON string
matrix_column_instance = MatrixColumn.from_json(json)
# print the JSON string representation of the object
print(MatrixColumn.to_json())

# convert the object into a dict
matrix_column_dict = matrix_column_instance.to_dict()
# create an instance of MatrixColumn from a dict
matrix_column_from_dict = MatrixColumn.from_dict(matrix_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


