# Dataset

Details about the dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sheet** | **str** | The unique identifier of the sheet to which this dataset belongs. | [optional] 
**range** | **str** | A1 style notation describing the range. Datasets are always located in the top left-hand corner of the sheet, so there is no need to specify range when creating a dataset. | [optional] [readonly] 
**values** | **List[List[object]]** | A row-major ordered multidimensional array of cell values. | [optional] 

## Example

```python
from openapi_client.models.dataset import Dataset

# TODO update the JSON string below
json = "{}"
# create an instance of Dataset from a JSON string
dataset_instance = Dataset.from_json(json)
# print the JSON string representation of the object
print(Dataset.to_json())

# convert the object into a dict
dataset_dict = dataset_instance.to_dict()
# create an instance of Dataset from a dict
dataset_from_dict = Dataset.from_dict(dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


