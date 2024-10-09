# Insertion

Insertion instruction. Describes how to insert a block of rows or columns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | The index to insert at | 
**count** | **int** | The number of rows or columns to insert | 

## Example

```python
from openapi_client.models.insertion import Insertion

# TODO update the JSON string below
json = "{}"
# create an instance of Insertion from a JSON string
insertion_instance = Insertion.from_json(json)
# print the JSON string representation of the object
print(Insertion.to_json())

# convert the object into a dict
insertion_dict = insertion_instance.to_dict()
# create an instance of Insertion from a dict
insertion_from_dict = Insertion.from_dict(insertion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


