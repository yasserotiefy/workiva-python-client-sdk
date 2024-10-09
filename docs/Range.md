# Range

A range in a sheet. If any field is omitted or null, the range is unbounded in that direction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_row** | **int** | The index of the first row of the range, inclusive | [optional] 
**stop_row** | **int** | The index of the last row of the range, inclusive | [optional] 
**start_column** | **int** | The index of the first column of the range, inclusive | [optional] 
**stop_column** | **int** | The index of the last column of the range, inclusive | [optional] 

## Example

```python
from openapi_client.models.range import Range

# TODO update the JSON string below
json = "{}"
# create an instance of Range from a JSON string
range_instance = Range.from_json(json)
# print the JSON string representation of the object
print(Range.to_json())

# convert the object into a dict
range_dict = range_instance.to_dict()
# create an instance of Range from a dict
range_from_dict = Range.from_dict(range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


