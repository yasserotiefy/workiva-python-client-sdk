# TaskLocation

Details about what the task is attached to, such as a file ID. If null, the task isn't attached to anything. Once a location is attached to a task, that location cannot be changed. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | The unique identifier of the file | [optional] 
**file_segment** | **str** | The unique identifier of the fileSegment. A fileSegment is a section in a document, a sheet in a spreadsheet, or a slide in a presentation. | [optional] 

## Example

```python
from openapi_client.models.task_location import TaskLocation

# TODO update the JSON string below
json = "{}"
# create an instance of TaskLocation from a JSON string
task_location_instance = TaskLocation.from_json(json)
# print the JSON string representation of the object
print(TaskLocation.to_json())

# convert the object into a dict
task_location_dict = task_location_instance.to_dict()
# create an instance of TaskLocation from a dict
task_location_from_dict = TaskLocation.from_dict(task_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


