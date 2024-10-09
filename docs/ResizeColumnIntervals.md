# ResizeColumnIntervals

Resize a list of column intervals to a specified size

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The new size for the columns, in points | 
**intervals** | [**List[Interval]**](Interval.md) | The intervals of columns to resize | 

## Example

```python
from openapi_client.models.resize_column_intervals import ResizeColumnIntervals

# TODO update the JSON string below
json = "{}"
# create an instance of ResizeColumnIntervals from a JSON string
resize_column_intervals_instance = ResizeColumnIntervals.from_json(json)
# print the JSON string representation of the object
print(ResizeColumnIntervals.to_json())

# convert the object into a dict
resize_column_intervals_dict = resize_column_intervals_instance.to_dict()
# create an instance of ResizeColumnIntervals from a dict
resize_column_intervals_from_dict = ResizeColumnIntervals.from_dict(resize_column_intervals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


