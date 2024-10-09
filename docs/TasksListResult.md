# TasksListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`Task`](ref:platform-tasks#task) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Task]**](Task.md) |  | [optional] 
**next_link** | **str** | Pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.tasks_list_result import TasksListResult

# TODO update the JSON string below
json = "{}"
# create an instance of TasksListResult from a JSON string
tasks_list_result_instance = TasksListResult.from_json(json)
# print the JSON string representation of the object
print(TasksListResult.to_json())

# convert the object into a dict
tasks_list_result_dict = tasks_list_result_instance.to_dict()
# create an instance of TasksListResult from a dict
tasks_list_result_from_dict = TasksListResult.from_dict(tasks_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


