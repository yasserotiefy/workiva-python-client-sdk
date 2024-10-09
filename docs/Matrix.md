# Matrix

Details about a matrix, including its name and ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the matrix | [optional] [readonly] 
**name** | **str** | The name of the matrix | [optional] 
**data_columns** | [**List[MatrixColumn]**](MatrixColumn.md) | An array of the data columns in the matrix | [optional] 
**result_columns** | [**List[MatrixColumn]**](MatrixColumn.md) | An array of the result columns in the matrix | [optional] 
**samples** | [**List[MatrixSample]**](MatrixSample.md) | An optional array of partial information about the samples on the matrix. To include in the response, provide the query parameter &#x60;$expand&#x3D;samples&#x60;. To include the samples&#39; attachments, provide the parameter &#x60;$expand&#x3D;samples,samples.attachments&#x60;. | [optional] [readonly] 
**attachments** | [**List[GraphAttachment]**](GraphAttachment.md) | An optional array of partial information about the attachments on the matrix. To include in the response, provide the query string &#x60;$expand&#x3D;attachments&#x60;. | [optional] [readonly] 

## Example

```python
from openapi_client.models.matrix import Matrix

# TODO update the JSON string below
json = "{}"
# create an instance of Matrix from a JSON string
matrix_instance = Matrix.from_json(json)
# print the JSON string representation of the object
print(Matrix.to_json())

# convert the object into a dict
matrix_dict = matrix_instance.to_dict()
# create an instance of Matrix from a dict
matrix_from_dict = Matrix.from_dict(matrix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


