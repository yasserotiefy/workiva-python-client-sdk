# openapi_client.TasksApi

All URIs are relative to *https://api.app.wdesk.com/platform/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](TasksApi.md#create_task) | **POST** /tasks | Create a new task
[**delete_task_by_id**](TasksApi.md#delete_task_by_id) | **DELETE** /tasks/{taskId} | Delete a single task
[**get_task_by_id**](TasksApi.md#get_task_by_id) | **GET** /tasks/{taskId} | Retrieve a single task
[**get_tasks**](TasksApi.md#get_tasks) | **GET** /tasks | Retrieve a list of tasks
[**partially_update_task_by_id**](TasksApi.md#partially_update_task_by_id) | **PATCH** /tasks/{taskId} | Partially update a single task
[**update_task_by_id**](TasksApi.md#update_task_by_id) | **PUT** /tasks/{taskId} | Update a single task


# **create_task**
> Task create_task(task)

Create a new task

Creates a new [task](ref:platform-tasks#task) given its properties. Requires passing in a `title` and `assignee`. <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 75 requests per second.  This rate is shared across your workspace. When you encounter a 429, examine the `Retry-After`  header and retry after that many seconds. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.app.wdesk.com/platform/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.app.wdesk.com/platform/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TasksApi(api_client)
    task = openapi_client.Task() # Task | The properties of the task to create

    try:
        # Create a new task
        api_response = api_instance.create_task(task)
        print("The response of TasksApi->create_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->create_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task** | [**Task**](Task.md)| The properties of the task to create | 

### Return type

[**Task**](Task.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task_by_id**
> delete_task_by_id(task_id)

Delete a single task

Deletes a [task](ref:platform-tasks#task) given its ID <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 75 requests per second.  This rate is shared across your workspace. When you encounter a 429, examine the `Retry-After`  header and retry after that many seconds. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.app.wdesk.com/platform/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.app.wdesk.com/platform/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The unique identifier of the task

    try:
        # Delete a single task
        api_instance.delete_task_by_id(task_id)
    except Exception as e:
        print("Exception when calling TasksApi->delete_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The unique identifier of the task | 

### Return type

void (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_by_id**
> Task get_task_by_id(task_id)

Retrieve a single task

Retrieves a [task](ref:platform-tasks#task) given its ID <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 75 requests per second.  This rate is shared across your workspace. When you encounter a 429, examine the `Retry-After`  header and retry after that many seconds. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.app.wdesk.com/platform/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.app.wdesk.com/platform/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The unique identifier of the task

    try:
        # Retrieve a single task
        api_response = api_instance.get_task_by_id(task_id)
        print("The response of TasksApi->get_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The unique identifier of the task | 

### Return type

[**Task**](Task.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> TasksListResult get_tasks(filter=filter, order_by=order_by, maxpagesize=maxpagesize, next=next)

Retrieve a list of tasks

Returns a paginated list of [tasks](ref:platform-tasks#task). Currently this endpoint only returns general tasks (such as those created as part of editing documents, sheets, and presentations). It does not return tasks created as part of a process, nor does it return tasks from the GRC product. <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 75 requests per second.  This rate is shared across your workspace. When you encounter a 429, examine the `Retry-After`  header and retry after that many seconds. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.tasks_list_result import TasksListResult
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.app.wdesk.com/platform/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.app.wdesk.com/platform/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TasksApi(api_client)
    filter = 'filter_example' # str | The properties to filter the results by. (optional)
    order_by = 'order_by_example' # str | One or more comma-separated expressions to indicate the order in which to sort the results. (optional)
    maxpagesize = 1000 # int | The maximum number of results to retrieve (optional) (default to 1000)
    next = 'JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA' # str | Pagination cursor for next set of results. (optional)

    try:
        # Retrieve a list of tasks
        api_response = api_instance.get_tasks(filter=filter, order_by=order_by, maxpagesize=maxpagesize, next=next)
        print("The response of TasksApi->get_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The properties to filter the results by. | [optional] 
 **order_by** | **str**| One or more comma-separated expressions to indicate the order in which to sort the results. | [optional] 
 **maxpagesize** | **int**| The maximum number of results to retrieve | [optional] [default to 1000]
 **next** | **str**| Pagination cursor for next set of results. | [optional] 

### Return type

[**TasksListResult**](TasksListResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_task_by_id**
> Task partially_update_task_by_id(task_id, json_patch_operation)

Partially update a single task

Partially updates the properties of a [task](ref:platform-tasks#task). <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 75 requests per second.  This rate is shared across your workspace. When you encounter a 429, examine the `Retry-After`  header and retry after that many seconds. ### Options |Path|PATCH Operations Supported| |---|---| |`/status`|`replace`| |`/title`|`replace`| |`/description`|`replace`| |`/assignee/id`|`replace`| |`/dueDate`|`replace`| 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.json_patch_operation import JSONPatchOperation
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.app.wdesk.com/platform/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.app.wdesk.com/platform/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The unique identifier of the task
    json_patch_operation = [{"op":"replace","path":"/title","value":"New Title"}] # List[JSONPatchOperation] | A collection of patch operations to apply to the task.

    try:
        # Partially update a single task
        api_response = api_instance.partially_update_task_by_id(task_id, json_patch_operation)
        print("The response of TasksApi->partially_update_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->partially_update_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The unique identifier of the task | 
 **json_patch_operation** | [**List[JSONPatchOperation]**](JSONPatchOperation.md)| A collection of patch operations to apply to the task. | 

### Return type

[**Task**](Task.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_by_id**
> Task update_task_by_id(task_id, task)

Update a single task

Replaces the details of a [task](ref:platform-tasks#task) given its properties. It is recommended to provide *all* properties in the body, as this endpoint performs a full replacement, *not* a partial update. <br /><br /> *However*, you cannot update a task's `location`. Also, if no `status` is provided, a value of `Created` is used. <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 75 requests per second.  This rate is shared across your workspace. When you encounter a 429, examine the `Retry-After`  header and retry after that many seconds. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.app.wdesk.com/platform/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.app.wdesk.com/platform/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TasksApi(api_client)
    task_id = 'task_id_example' # str | The unique identifier of the task
    task = openapi_client.Task() # Task | All properties for the task, not just those to update

    try:
        # Update a single task
        api_response = api_instance.update_task_by_id(task_id, task)
        print("The response of TasksApi->update_task_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->update_task_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| The unique identifier of the task | 
 **task** | [**Task**](Task.md)| All properties for the task, not just those to update | 

### Return type

[**Task**](Task.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

