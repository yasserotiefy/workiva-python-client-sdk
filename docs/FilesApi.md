# openapi_client.FilesApi

All URIs are relative to *https://api.app.wdesk.com/platform/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file**](FilesApi.md#create_file) | **POST** /files | Create a new file
[**get_file_by_id**](FilesApi.md#get_file_by_id) | **GET** /files/{fileId} | Retrieve a single file
[**get_files**](FilesApi.md#get_files) | **GET** /files | Retrieve a list of files
[**import_file**](FilesApi.md#import_file) | **POST** /files/import | Initiate a file import
[**partially_update_file_by_id**](FilesApi.md#partially_update_file_by_id) | **PATCH** /files/{fileId} | Partially update a single file
[**update_file_by_id**](FilesApi.md#update_file_by_id) | **PUT** /files/{fileId} | Update a single file


# **create_file**
> File create_file(file)

Create a new file

Creates a new [file](ref:platform-files#file). Requires name and kind. kind must be one of `Document`, `Spreadsheet`, `Presentation`, or `Folder` and is case-sensitive. Use the `container` attribute to specify the container that houses the file, such as a folder. If empty, the root folder is the container. Files are created asynchronously and may not immediately be available on a subsequent `GET`. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.file import File
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
    api_instance = openapi_client.FilesApi(api_client)
    file = '/path/to/file' # File | The properties of the file to create

    try:
        # Create a new file
        api_response = api_instance.create_file(file)
        print("The response of FilesApi->create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**File**](File.md)| The properties of the file to create | 

### Return type

[**File**](File.md)

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

# **get_file_by_id**
> File get_file_by_id(file_id)

Retrieve a single file

Retrieves a [file](ref:platform-files#file) given its ID 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.file import File
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
    api_instance = openapi_client.FilesApi(api_client)
    file_id = 'file_id_example' # str | The unique identifier of the file

    try:
        # Retrieve a single file
        api_response = api_instance.get_file_by_id(file_id)
        print("The response of FilesApi->get_file_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_file_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The unique identifier of the file | 

### Return type

[**File**](File.md)

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

# **get_files**
> FilesListResult get_files(filter=filter, order_by=order_by, maxpagesize=maxpagesize, next=next)

Retrieve a list of files

Returns a paginated list of [files](ref:platform-files#file).

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.files_list_result import FilesListResult
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
    api_instance = openapi_client.FilesApi(api_client)
    filter = 'filter_example' # str | The properties to filter the results by. (optional)
    order_by = 'order_by_example' # str | One or more comma-separated expressions to indicate the order in which to sort the results. (optional)
    maxpagesize = 1000 # int | The maximum number of results to retrieve (optional) (default to 1000)
    next = 'JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA' # str | Pagination cursor for next set of results. (optional)

    try:
        # Retrieve a list of files
        api_response = api_instance.get_files(filter=filter, order_by=order_by, maxpagesize=maxpagesize, next=next)
        print("The response of FilesApi->get_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The properties to filter the results by. | [optional] 
 **order_by** | **str**| One or more comma-separated expressions to indicate the order in which to sort the results. | [optional] 
 **maxpagesize** | **int**| The maximum number of results to retrieve | [optional] [default to 1000]
 **next** | **str**| Pagination cursor for next set of results. | [optional] 

### Return type

[**FilesListResult**](FilesListResult.md)

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

# **import_file**
> FileImportResponse import_file(file_import)

Initiate a file import

Import a file for conversion to a Workiva equivalent. This is a long running operation. Response includes an `uploadUrl` which indicates where to upload the file for import. To upload the file, perform a PUT against the `uploadUrl` with the same authentication credentials and flow as the import request. For more details, see [Authentication documentation](ref:platform-authentication). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.file_import import FileImport
from openapi_client.models.file_import_response import FileImportResponse
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
    api_instance = openapi_client.FilesApi(api_client)
    file_import = openapi_client.FileImport() # FileImport | The details of the file import

    try:
        # Initiate a file import
        api_response = api_instance.import_file(file_import)
        print("The response of FilesApi->import_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->import_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_import** | [**FileImport**](FileImport.md)| The details of the file import | 

### Return type

[**FileImportResponse**](FileImportResponse.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  * Location - The location to poll for the operation result. <br>  * Retry-After - The number of seconds to wait before polling for a result and between polling attempts. <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partially_update_file_by_id**
> File partially_update_file_by_id(file_id, json_patch_operation)

Partially update a single file

Partially updates the properties of a [file](ref:platform-files#file). Only one property may be updated at a time. Updates are applied asynchronously and may not immediately be reflected on a subsequent `GET`. ### Options |Path|PATCH Operations Supported| |---|---| |`/container`|`replace`| 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.file import File
from openapi_client.models.json_patch_operation import JSONPatchOperation
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
    api_instance = openapi_client.FilesApi(api_client)
    file_id = 'file_id_example' # str | The unique identifier of the file
    json_patch_operation = [{"op":"replace","path":"/container","value":""}] # List[JSONPatchOperation] | A collection of patch operations to apply to the file. Currently only one operation may be applied at a time.

    try:
        # Partially update a single file
        api_response = api_instance.partially_update_file_by_id(file_id, json_patch_operation)
        print("The response of FilesApi->partially_update_file_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->partially_update_file_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The unique identifier of the file | 
 **json_patch_operation** | [**List[JSONPatchOperation]**](JSONPatchOperation.md)| A collection of patch operations to apply to the file. Currently only one operation may be applied at a time. | 

### Return type

[**File**](File.md)

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

# **update_file_by_id**
> File update_file_by_id(file_id, file)

Update a single file

Replaces the details of a [file](ref:platform-files#file) given its properties. It is recommended to provide *all* properties in the body, as this endpoint performs a full replacement, *not* a partial update. Updates are applied asynchronously and may not immediately be  reflected on a subsequent `GET`. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.file import File
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
    api_instance = openapi_client.FilesApi(api_client)
    file_id = 'file_id_example' # str | The unique identifier of the file
    file = '/path/to/file' # File | All properties for the file, not just those to update

    try:
        # Update a single file
        api_response = api_instance.update_file_by_id(file_id, file)
        print("The response of FilesApi->update_file_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->update_file_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The unique identifier of the file | 
 **file** | [**File**](File.md)| All properties for the file, not just those to update | 

### Return type

[**File**](File.md)

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

