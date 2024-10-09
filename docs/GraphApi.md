# openapi_client.GraphApi

All URIs are relative to *https://api.app.wdesk.com/platform/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_edits**](GraphApi.md#create_edits) | **POST** /graph/edits | Create new record edits
[**get_record_by_id**](GraphApi.md#get_record_by_id) | **GET** /graph/records/{recordId} | Retrieve a single record
[**get_records**](GraphApi.md#get_records) | **GET** /graph/records | Retrieve a list of records
[**get_report_as_csv**](GraphApi.md#get_report_as_csv) | **GET** /graph/reports/{reportId}/csv | Retrieve the CSV of a saved report
[**get_type_by_id**](GraphApi.md#get_type_by_id) | **GET** /graph/types/{typeId} | Retrieve a single type
[**get_types**](GraphApi.md#get_types) | **GET** /graph/types | Retrieve a list of types
[**graph_report_export**](GraphApi.md#graph_report_export) | **POST** /graph/reports/{reportId}/export | Initiate a graph report export


# **create_edits**
> EditsResult create_edits(edit)

Create new record edits

Creates new record [edits](ref:platform-graph#edit) given their properties. Each edit in the supplied array requires at least an `operation` and `targetId`. Up to 1000 edits may be processed per request. If there are invalid edits, the error details will include a list of errors encountered. Each message will include the zero-based position of the failed edit in the provided list of edits.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.edit import Edit
from openapi_client.models.edits_result import EditsResult
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
    api_instance = openapi_client.GraphApi(api_client)
    edit = [openapi_client.Edit()] # List[Edit] | An array of edits

    try:
        # Create new record edits
        api_response = api_instance.create_edits(edit)
        print("The response of GraphApi->create_edits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphApi->create_edits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit** | [**List[Edit]**](Edit.md)| An array of edits | 

### Return type

[**EditsResult**](EditsResult.md)

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

# **get_record_by_id**
> Record get_record_by_id(record_id, expand=expand)

Retrieve a single record

Retrieves a [record](ref:platform-graph#record) given its ID. The unique identifier is typically a UUID, but it may be a different unique string in some cases.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.record import Record
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
    api_instance = openapi_client.GraphApi(api_client)
    record_id = 'record_id_example' # str | The unique identifier of the record
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrieve a single record
        api_response = api_instance.get_record_by_id(record_id, expand=expand)
        print("The response of GraphApi->get_record_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphApi->get_record_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_id** | **str**| The unique identifier of the record | 
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**Record**](Record.md)

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

# **get_records**
> RecordsListResult get_records(expand=expand, filter=filter)

Retrieve a list of records

Returns a list of [records](ref:platform-graph#record) matching the provided filters. At least one filter is required. If no filter is provided an error will be returned.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.records_list_result import RecordsListResult
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
    api_instance = openapi_client.GraphApi(api_client)
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)
    filter = 'filter_example' # str | The properties to filter the results by. (optional)

    try:
        # Retrieve a list of records
        api_response = api_instance.get_records(expand=expand, filter=filter)
        print("The response of GraphApi->get_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphApi->get_records: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 
 **filter** | **str**| The properties to filter the results by. | [optional] 

### Return type

[**RecordsListResult**](RecordsListResult.md)

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

# **get_report_as_csv**
> str get_report_as_csv(report_id)

Retrieve the CSV of a saved report

This endpoint will execute the query of a saved report and return the data as a CSV string. The ID of the [record](ref:platform-graph#record) containing the saved report is used for the `reportID` path element. Reports are stored in records of type `DataSource` and `ReportView`. The list of applicable records can be retrieved from the `/records` endpoint such as `GET /records?$filter=type eq DataSource or type eq ReportView`. A filter on the `title` property should be used to return a particular report.

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
    api_instance = openapi_client.GraphApi(api_client)
    report_id = 'report_id_example' # str | The unique identifier of the report

    try:
        # Retrieve the CSV of a saved report
        api_response = api_instance.get_report_as_csv(report_id)
        print("The response of GraphApi->get_report_as_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphApi->get_report_as_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The unique identifier of the report | 

### Return type

**str**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv; charset=UTF-8, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_type_by_id**
> Type get_type_by_id(type_id, expand=expand)

Retrieve a single type

Returns a record [type](ref:platform-graph#type) given its ID (name) 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.type import Type
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
    api_instance = openapi_client.GraphApi(api_client)
    type_id = 'type_id_example' # str | The unique identifier of the type
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrieve a single type
        api_response = api_instance.get_type_by_id(type_id, expand=expand)
        print("The response of GraphApi->get_type_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphApi->get_type_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_id** | **str**| The unique identifier of the type | 
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**Type**](Type.md)

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

# **get_types**
> TypesListResult get_types(expand=expand)

Retrieve a list of types

The Types endpoint is used to discover what [types](ref:platform-graph#type) of records exist and their attributes. This endpoint lets you know what to expect from the Records endpoints. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.types_list_result import TypesListResult
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
    api_instance = openapi_client.GraphApi(api_client)
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrieve a list of types
        api_response = api_instance.get_types(expand=expand)
        print("The response of GraphApi->get_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GraphApi->get_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**TypesListResult**](TypesListResult.md)

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

# **graph_report_export**
> graph_report_export(report_id, graph_report_export)

Initiate a graph report export

Asynchronously exports a graph report (only CSV available at this time). This endpoint will execute the query of a saved report and export to the specified format (only CSV available at this time). The ID of the [record](ref:platform-graph#record) containing the saved report is used for the `reportID` path element. Reports are stored in records of type `DataSource` and `ReportView`. The list of applicable records can be retrieved from the `/records` endpoint such as `GET /records?$filter=type eq DataSource or type eq ReportView`. A filter on the `title` property should be used to return a particular report. Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:platform-authentication). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_report_export import GraphReportExport
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
    api_instance = openapi_client.GraphApi(api_client)
    report_id = 'report_id_example' # str | The unique identifier of the report
    graph_report_export = openapi_client.GraphReportExport() # GraphReportExport | Details about the report export

    try:
        # Initiate a graph report export
        api_instance.graph_report_export(report_id, graph_report_export)
    except Exception as e:
        print("Exception when calling GraphApi->graph_report_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| The unique identifier of the report | 
 **graph_report_export** | [**GraphReportExport**](GraphReportExport.md)| Details about the report export | 

### Return type

void (empty response body)

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

