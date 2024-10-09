# ResizeRowIntervals

Resize a list of row intervals to a specified size

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The new size for the rows, in points | 
**intervals** | [**List[Interval]**](Interval.md) | The intervals of rows to resize | 

## Example

```python
from openapi_client.models.resize_row_intervals import ResizeRowIntervals

# TODO update the JSON string below
json = "{}"
# create an instance of ResizeRowIntervals from a JSON string
resize_row_intervals_instance = ResizeRowIntervals.from_json(json)
# print the JSON string representation of the object
print(ResizeRowIntervals.to_json())

# convert the object into a dict
resize_row_intervals_dict = resize_row_intervals_instance.to_dict()
# create an instance of ResizeRowIntervals from a dict
resize_row_intervals_from_dict = ResizeRowIntervals.from_dict(resize_row_intervals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


