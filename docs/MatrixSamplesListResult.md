# MatrixSamplesListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`MatrixSample`](ref:platform-testforms#matrixsample) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MatrixSample]**](MatrixSample.md) | A list of &#x60;MatrixSample&#x60; objects | 
**next_link** | **str** | The pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.matrix_samples_list_result import MatrixSamplesListResult

# TODO update the JSON string below
json = "{}"
# create an instance of MatrixSamplesListResult from a JSON string
matrix_samples_list_result_instance = MatrixSamplesListResult.from_json(json)
# print the JSON string representation of the object
print(MatrixSamplesListResult.to_json())

# convert the object into a dict
matrix_samples_list_result_dict = matrix_samples_list_result_instance.to_dict()
# create an instance of MatrixSamplesListResult from a dict
matrix_samples_list_result_from_dict = MatrixSamplesListResult.from_dict(matrix_samples_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


