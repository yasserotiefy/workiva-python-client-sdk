# MatrixSample

This object represents a single row of a matrix.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the matrix sample | [optional] 
**data_values** | [**List[SampleCell]**](SampleCell.md) | An array of SampleCell values representing the values for each data column of the sample matrix&#39;s cells | [optional] 
**result_values** | [**List[SampleCell]**](SampleCell.md) | An array of SampleCell values representing the values for each result cell in the sample matrix&#39;s cells. | [optional] 
**attachments** | [**List[GraphAttachment]**](GraphAttachment.md) | An optional array of partial information about the attachments on the matrix sample. To include in the response, provide the query parameter &#x60;$expand&#x3D;attachments&#x60;. | [optional] [readonly] 

## Example

```python
from openapi_client.models.matrix_sample import MatrixSample

# TODO update the JSON string below
json = "{}"
# create an instance of MatrixSample from a JSON string
matrix_sample_instance = MatrixSample.from_json(json)
# print the JSON string representation of the object
print(MatrixSample.to_json())

# convert the object into a dict
matrix_sample_dict = matrix_sample_instance.to_dict()
# create an instance of MatrixSample from a dict
matrix_sample_from_dict = MatrixSample.from_dict(matrix_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


