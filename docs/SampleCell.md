# SampleCell

Represents a single cell in a matrix

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** | The ID of the column associated with the cell&#39;s value | [optional] 
**value** | **str** | The string value of the cell | [optional] 

## Example

```python
from openapi_client.models.sample_cell import SampleCell

# TODO update the JSON string below
json = "{}"
# create an instance of SampleCell from a JSON string
sample_cell_instance = SampleCell.from_json(json)
# print the JSON string representation of the object
print(SampleCell.to_json())

# convert the object into a dict
sample_cell_dict = sample_cell_instance.to_dict()
# create an instance of SampleCell from a dict
sample_cell_from_dict = SampleCell.from_dict(sample_cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


