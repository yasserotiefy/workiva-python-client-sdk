# Task

Details about the task, including its ID, status, associated users, and milestone dates. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the task | [optional] [readonly] 
**title** | **str** | The title of the task, up to 500 characters | [optional] 
**description** | **str** | The description of the task, up to 2000 characters | [optional] [default to '']
**status** | **str** | Whether the task is &#x60;Created&#x60;, &#x60;Completed&#x60;, or &#x60;Cancelled&#x60; | [optional] [default to 'Created']
**due_date** | **datetime** | The task&#39;s due date | [optional] 
**source_url** | **str** | The link to the task in Wdesk Home or within a document. | [optional] [readonly] 
**assignee** | [**User**](User.md) |  | [optional] 
**created** | [**Action**](Action.md) |  | [optional] 
**modified** | [**Action**](Action.md) |  | [optional] 
**completed** | [**Action**](Action.md) |  | [optional] 
**location** | [**TaskLocation**](TaskLocation.md) |  | [optional] 

## Example

```python
from openapi_client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


