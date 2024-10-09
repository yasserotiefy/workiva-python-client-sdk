# openapi_client.SpreadsheetsApi

All URIs are relative to *https://api.app.wdesk.com/platform/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_sheet**](SpreadsheetsApi.md#copy_sheet) | **POST** /spreadsheets/{spreadsheetId}/sheets/{sheetId}/copy | Copy sheet
[**create_sheet**](SpreadsheetsApi.md#create_sheet) | **POST** /spreadsheets/{spreadsheetId}/sheets | Create a new sheet in a spreadsheet
[**delete_dataset_by_sheet_id**](SpreadsheetsApi.md#delete_dataset_by_sheet_id) | **DELETE** /spreadsheets/{spreadsheetId}/sheets/{sheetId}/dataset | Delete a single dataset
[**delete_sheet_by_id**](SpreadsheetsApi.md#delete_sheet_by_id) | **DELETE** /spreadsheets/{spreadsheetId}/sheets/{sheetId} | Delete a single sheet
[**get_datasets**](SpreadsheetsApi.md#get_datasets) | **GET** /spreadsheets/{spreadsheetId}/datasets | Retrieve a list of datasets
[**get_sheet_by_id**](SpreadsheetsApi.md#get_sheet_by_id) | **GET** /spreadsheets/{spreadsheetId}/sheets/{sheetId} | Retrieve a single sheet
[**get_sheet_data**](SpreadsheetsApi.md#get_sheet_data) | **GET** /spreadsheets/{spreadsheetId}/sheets/{sheetId}/sheetdata | Retrieve data from a sheet
[**get_sheets**](SpreadsheetsApi.md#get_sheets) | **GET** /spreadsheets/{spreadsheetId}/sheets | Retrieve a list of sheets
[**get_spreadsheet_by_id**](SpreadsheetsApi.md#get_spreadsheet_by_id) | **GET** /spreadsheets/{spreadsheetId} | Retrieve a single spreadsheet
[**get_spreadsheets**](SpreadsheetsApi.md#get_spreadsheets) | **GET** /spreadsheets | Retrieve a list of spreadsheets
[**get_values_by_range**](SpreadsheetsApi.md#get_values_by_range) | **GET** /spreadsheets/{spreadsheetId}/sheets/{sheetId}/values/{range} | Retrieve a list of range values
[**partially_update_sheet_by_id**](SpreadsheetsApi.md#partially_update_sheet_by_id) | **PATCH** /spreadsheets/{spreadsheetId}/sheets/{sheetId} | Partially update a single sheet
[**spreadsheet_export**](SpreadsheetsApi.md#spreadsheet_export) | **POST** /spreadsheets/{spreadsheetId}/export | Initiate a spreadsheet export
[**update_sheet**](SpreadsheetsApi.md#update_sheet) | **POST** /spreadsheets/{spreadsheetId}/sheets/{sheetId}/update | Update sheet content
[**update_sheet_by_id**](SpreadsheetsApi.md#update_sheet_by_id) | **PUT** /spreadsheets/{spreadsheetId}/sheets/{sheetId} | Update a single sheet
[**update_values_by_range**](SpreadsheetsApi.md#update_values_by_range) | **PUT** /spreadsheets/{spreadsheetId}/sheets/{sheetId}/values/{range} | Update values in a range
[**upsert_datasets**](SpreadsheetsApi.md#upsert_datasets) | **POST** /spreadsheets/{spreadsheetId}/datasets/bulkUpsert | Bulk upsert of datasets


# **copy_sheet**
> copy_sheet(spreadsheet_id, sheet_id, sheet_copy)

Copy sheet

Asynchronously copies a [sheet](ref:platform-spreadsheets#sheet) given details about the copy's destination within the same or another spreadsheet. Options are specified using a [SheetCopy](ref:platform-spreadsheets#sheetcopy) object.  This endpoint copies a sheet's content, but does not copy labels, comments, or tasks. It will copy over most formatting, however it does not copy user-defined style guides across spreadsheets. So if the source sheet has  formatting that depends on a user-defined style guide, that formatting will be lost when copying to a new spreadsheet.  Unless otherwise specified, the copy appears at the top level of its  destination spreadsheet, with an index of 0, and with the same name as the original sheet.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.sheet_copy import SheetCopy
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    sheet_id = 'sheet_id_example' # str | The unique identifier of the sheet
    sheet_copy = openapi_client.SheetCopy() # SheetCopy | A SheetCopy object

    try:
        # Copy sheet
        api_instance.copy_sheet(spreadsheet_id, sheet_id, sheet_copy)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->copy_sheet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **sheet_id** | **str**| The unique identifier of the sheet | 
 **sheet_copy** | [**SheetCopy**](SheetCopy.md)| A SheetCopy object | 

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

# **create_sheet**
> Sheet create_sheet(spreadsheet_id, sheet)

Create a new sheet in a spreadsheet

Creates a new [sheet](ref:platform-spreadsheets#sheet) in a [spreadsheet](ref:platform-spreadsheets#spreadsheet), given its properties. If the sheet name provided isn't unique, a number is appended to make it unique. By default, creates a top-level sheet in the top-most position. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.sheet import Sheet
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    sheet = {"index":2,"name":"Q3"} # Sheet | The properties of the sheet to create

    try:
        # Create a new sheet in a spreadsheet
        api_response = api_instance.create_sheet(spreadsheet_id, sheet)
        print("The response of SpreadsheetsApi->create_sheet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->create_sheet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **sheet** | [**Sheet**](Sheet.md)| The properties of the sheet to create | 

### Return type

[**Sheet**](Sheet.md)

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

# **delete_dataset_by_sheet_id**
> delete_dataset_by_sheet_id(spreadsheet_id, sheet_id, deletevalues=deletevalues)

Delete a single dataset

Deletes the [dataset](ref:platform-spreadsheets#dataset) for the specified [sheet](ref:platform-spreadsheets#sheet). <br /><br /> When you delete a dataset, you can select whether to leave its associated values in place. To delete its values, pass `true` for query parameter `$deletevalues` (default is `false`).

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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    sheet_id = 'sheet_id_example' # str | The unique identifier of the sheet
    deletevalues = False # bool | Indicates whether values should be deleted along with the dataset (optional) (default to False)

    try:
        # Delete a single dataset
        api_instance.delete_dataset_by_sheet_id(spreadsheet_id, sheet_id, deletevalues=deletevalues)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->delete_dataset_by_sheet_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **sheet_id** | **str**| The unique identifier of the sheet | 
 **deletevalues** | **bool**| Indicates whether values should be deleted along with the dataset | [optional] [default to False]

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

# **delete_sheet_by_id**
> delete_sheet_by_id(spreadsheet_id, sheet_id)

Delete a single sheet

Deletes a [sheet](ref:platform-spreadsheets#sheet) given its ID. 

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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    sheet_id = 'sheet_id_example' # str | The unique identifier of the sheet

    try:
        # Delete a single sheet
        api_instance.delete_sheet_by_id(spreadsheet_id, sheet_id)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->delete_sheet_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **sheet_id** | **str**| The unique identifier of the sheet | 

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

# **get_datasets**
> DatasetsListResult get_datasets(spreadsheet_id)

Retrieve a list of datasets

Returns a list of [datasets](ref:platform-spreadsheets#dataset). <br /><br /> Use this endpoint to identify any datasets that exist within a given [spreadsheet](ref:platform-spreadsheets#spreadsheet), up to one per [sheet](ref:platform-spreadsheets#sheet).

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.datasets_list_result import DatasetsListResult
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet

    try:
        # Retrieve a list of datasets
        api_response = api_instance.get_datasets(spreadsheet_id)
        print("The response of SpreadsheetsApi->get_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->get_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 

### Return type

[**DatasetsListResult**](DatasetsListResult.md)

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

# **get_sheet_by_id**
> Sheet get_sheet_by_id(spreadsheet_id, sheet_id)

Retrieve a single sheet

Retrieves a [sheet](ref:platform-spreadsheets#sheet) given its ID. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.sheet import Sheet
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    sheet_id = 'sheet_id_example' # str | The unique identifier of the sheet

    try:
        # Retrieve a single sheet
        api_response = api_instance.get_sheet_by_id(spreadsheet_id, sheet_id)
        print("The response of SpreadsheetsApi->get_sheet_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->get_sheet_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **sheet_id** | **str**| The unique identifier of the sheet | 

### Return type

[**Sheet**](Sheet.md)

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

# **get_sheet_data**
> SheetDataResult get_sheet_data(spreadsheet_id, sheet_id, cellrange=cellrange, maxcellsperpage=maxcellsperpage, next=next, fields=fields)

Retrieve data from a sheet

Retrieve data from a range in a sheet. Includes the value & formatting of cells, visibility of columns and cells, merged ranges, etc. Limit the results to particular fields by providing a comma-separated list of paths, rooted at the `data` object. Example: $fields=cells.calculatedValue,cells.formats.valueFormat <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 600 requests per minute.  This rate is shared across your workspace. When you encounter a 429, examine the `Retry-After`  header and retry after that many seconds.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.sheet_data_result import SheetDataResult
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    sheet_id = 'sheet_id_example' # str | The unique identifier of the sheet
    cellrange = 'A2:B' # str | The range to query. If not provided, the entire sheet will be queried. A1 style representation of a cell or range. A range my be unbounded in any/all directions by leaving off the corresponding column or row.  (optional)
    maxcellsperpage = 50000 # int | The maximum number of cells to retrieve. The default is 50000. The maximum allowed value is 50000. (optional) (default to 50000)
    next = 'JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA' # str | Pagination cursor for next set of results. (optional)
    fields = 'fields_example' # str | A restricted set of fields for a given resource. (optional)

    try:
        # Retrieve data from a sheet
        api_response = api_instance.get_sheet_data(spreadsheet_id, sheet_id, cellrange=cellrange, maxcellsperpage=maxcellsperpage, next=next, fields=fields)
        print("The response of SpreadsheetsApi->get_sheet_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->get_sheet_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **sheet_id** | **str**| The unique identifier of the sheet | 
 **cellrange** | **str**| The range to query. If not provided, the entire sheet will be queried. A1 style representation of a cell or range. A range my be unbounded in any/all directions by leaving off the corresponding column or row.  | [optional] 
 **maxcellsperpage** | **int**| The maximum number of cells to retrieve. The default is 50000. The maximum allowed value is 50000. | [optional] [default to 50000]
 **next** | **str**| Pagination cursor for next set of results. | [optional] 
 **fields** | **str**| A restricted set of fields for a given resource. | [optional] 

### Return type

[**SheetDataResult**](SheetDataResult.md)

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

# **get_sheets**
> SheetsListResult get_sheets(spreadsheet_id)

Retrieve a list of sheets

Returns a list of [sheets](ref:platform-spreadsheets#sheet). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.sheets_list_result import SheetsListResult
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet

    try:
        # Retrieve a list of sheets
        api_response = api_instance.get_sheets(spreadsheet_id)
        print("The response of SpreadsheetsApi->get_sheets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->get_sheets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 

### Return type

[**SheetsListResult**](SheetsListResult.md)

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

# **get_spreadsheet_by_id**
> Spreadsheet get_spreadsheet_by_id(spreadsheet_id, expand=expand)

Retrieve a single spreadsheet

Retrieves a [spreadsheet](ref:platform-spreadsheets#spreadsheet) given its ID. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.spreadsheet import Spreadsheet
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrieve a single spreadsheet
        api_response = api_instance.get_spreadsheet_by_id(spreadsheet_id, expand=expand)
        print("The response of SpreadsheetsApi->get_spreadsheet_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->get_spreadsheet_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**Spreadsheet**](Spreadsheet.md)

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

# **get_spreadsheets**
> SpreadsheetsListResult get_spreadsheets(filter=filter, order_by=order_by, maxpagesize=maxpagesize, next=next)

Retrieve a list of spreadsheets

Returns a paginated list of [spreadsheets](ref:platform-spreadsheets#spreadsheet). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.spreadsheets_list_result import SpreadsheetsListResult
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    filter = 'filter_example' # str | The properties to filter the results by. (optional)
    order_by = 'order_by_example' # str | One or more comma-separated expressions to indicate the order in which to sort the results. (optional)
    maxpagesize = 1000 # int | The maximum number of results to retrieve (optional) (default to 1000)
    next = 'JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA' # str | Pagination cursor for next set of results. (optional)

    try:
        # Retrieve a list of spreadsheets
        api_response = api_instance.get_spreadsheets(filter=filter, order_by=order_by, maxpagesize=maxpagesize, next=next)
        print("The response of SpreadsheetsApi->get_spreadsheets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->get_spreadsheets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The properties to filter the results by. | [optional] 
 **order_by** | **str**| One or more comma-separated expressions to indicate the order in which to sort the results. | [optional] 
 **maxpagesize** | **int**| The maximum number of results to retrieve | [optional] [default to 1000]
 **next** | **str**| Pagination cursor for next set of results. | [optional] 

### Return type

[**SpreadsheetsListResult**](SpreadsheetsListResult.md)

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

# **get_values_by_range**
> RangeValuesListResult get_values_by_range(spreadsheet_id, sheet_id, range, maxcellsperpage=maxcellsperpage, next=next, valuestyle=valuestyle)

Retrieve a list of range values

Returns the paginated values for a specified range. When you retrieve values from a range, Ones scale is used regardless of the cell's scale formatting.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.range_values_list_result import RangeValuesListResult
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    sheet_id = 'sheet_id_example' # str | The unique identifier of the sheet
    range = 'range_example' # str | The range of values, in A1-style notation
    maxcellsperpage = 50000 # int | The maximum number of cells to retrieve. The default is 50000. The maximum allowed value is 50000. (optional) (default to 50000)
    next = 'JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA' # str | Pagination cursor for next set of results. (optional)
    valuestyle = calculated # str | Whether to retrieve `raw` or `calculated` cell values. For example, if a cell's value is `=1+1`, `raw` retrieves the value `=1+1`, while `calculated` retrieves `2`. (optional) (default to calculated)

    try:
        # Retrieve a list of range values
        api_response = api_instance.get_values_by_range(spreadsheet_id, sheet_id, range, maxcellsperpage=maxcellsperpage, next=next, valuestyle=valuestyle)
        print("The response of SpreadsheetsApi->get_values_by_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->get_values_by_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **sheet_id** | **str**| The unique identifier of the sheet | 
 **range** | **str**| The range of values, in A1-style notation | 
 **maxcellsperpage** | **int**| The maximum number of cells to retrieve. The default is 50000. The maximum allowed value is 50000. | [optional] [default to 50000]
 **next** | **str**| Pagination cursor for next set of results. | [optional] 
 **valuestyle** | **str**| Whether to retrieve &#x60;raw&#x60; or &#x60;calculated&#x60; cell values. For example, if a cell&#39;s value is &#x60;&#x3D;1+1&#x60;, &#x60;raw&#x60; retrieves the value &#x60;&#x3D;1+1&#x60;, while &#x60;calculated&#x60; retrieves &#x60;2&#x60;. | [optional] [default to calculated]

### Return type

[**RangeValuesListResult**](RangeValuesListResult.md)

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

# **partially_update_sheet_by_id**
> Sheet partially_update_sheet_by_id(spreadsheet_id, sheet_id, json_patch_operation)

Partially update a single sheet

Partially updates the properties of a [sheet](ref:platform-spreadsheets#sheet). ### Options |Path|PATCH Operations Supported| |---|---| |`/name`|`replace`| |`/index`|`replace`| |`/parent`|`replace`|  ### Examples #### Update the name of a sheet ```json [   {     \"op\": \"replace\",     \"path\": \"/name\",     \"value\": \"Q1 Draft\"   } ] ``` #### Update the parent of a sheet (preserving its index) ```json [   {     \"op\": \"replace\",     \"path\": \"/parent\",     \"value\": {       \"id\": \"242a56d3cc0742c8abad0820bd318b23\"     }   } ] ``` #### Update the parent of a sheet (making it the first child) ```json [   {     \"op\": \"replace\",     \"path\": \"/parent\",     \"value\": {       \"id\": \"242a56d3cc0742c8abad0820bd318b23\"     }   },   {     \"op\": \"replace\",     \"path\": \"/index\",     \"value\": 0   } ] ``` 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.json_patch_operation import JSONPatchOperation
from openapi_client.models.sheet import Sheet
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    sheet_id = 'sheet_id_example' # str | The unique identifier of the sheet
    json_patch_operation = [{"op":"replace","path":"/name","value":"New Name"}] # List[JSONPatchOperation] | A collection of patch operations to apply to the sheet.

    try:
        # Partially update a single sheet
        api_response = api_instance.partially_update_sheet_by_id(spreadsheet_id, sheet_id, json_patch_operation)
        print("The response of SpreadsheetsApi->partially_update_sheet_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->partially_update_sheet_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **sheet_id** | **str**| The unique identifier of the sheet | 
 **json_patch_operation** | [**List[JSONPatchOperation]**](JSONPatchOperation.md)| A collection of patch operations to apply to the sheet. | 

### Return type

[**Sheet**](Sheet.md)

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

# **spreadsheet_export**
> spreadsheet_export(spreadsheet_id, spreadsheet_export)

Initiate a spreadsheet export

Asynchronously exports a [spreadsheet](ref:platform-spreadsheets#spreadsheet) as .XLSX, .PDF, or .CSV.  Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:platform-authentication).  Note: To export to .PDF, the spreadsheet can have no more than 250,000 cells. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.spreadsheet_export import SpreadsheetExport
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    spreadsheet_export = openapi_client.SpreadsheetExport() # SpreadsheetExport | Details about the spreadsheet export, including its format and options

    try:
        # Initiate a spreadsheet export
        api_instance.spreadsheet_export(spreadsheet_id, spreadsheet_export)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->spreadsheet_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **spreadsheet_export** | [**SpreadsheetExport**](SpreadsheetExport.md)| Details about the spreadsheet export, including its format and options | 

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

# **update_sheet**
> update_sheet(spreadsheet_id, sheet_id, sheet_update)

Update sheet content

Asynchronously submits a [SheetUpdate](ref:platform-spreadsheets#sheetupdate) to a [sheet](ref:platform-spreadsheets#sheet). Each [SheetUpdate](ref:platform-spreadsheets#sheetupdate) can have only one update field set per request. <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 60 requests per minute.  This rate is shared across your workspace. When you encounter a 429, examine the `Retry-After`  header and retry after that many seconds.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.sheet_update import SheetUpdate
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    sheet_id = 'sheet_id_example' # str | The unique identifier of the sheet
    sheet_update = openapi_client.SheetUpdate() # SheetUpdate | A SheetUpdate

    try:
        # Update sheet content
        api_instance.update_sheet(spreadsheet_id, sheet_id, sheet_update)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->update_sheet: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **sheet_id** | **str**| The unique identifier of the sheet | 
 **sheet_update** | [**SheetUpdate**](SheetUpdate.md)| A SheetUpdate | 

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

# **update_sheet_by_id**
> Sheet update_sheet_by_id(spreadsheet_id, sheet_id, sheet)

Update a single sheet

Replaces the details of a [sheet](ref:platform-spreadsheets#sheet) given its properties. This endpoint performs a full replacement, *not* a partial update. If the provided sheet name is not unique, a number will be appended to make it unique.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.sheet import Sheet
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    sheet_id = 'sheet_id_example' # str | The unique identifier of the sheet
    sheet = {"index":0,"name":"Q3"} # Sheet | All properties for the sheet, not just those to update

    try:
        # Update a single sheet
        api_response = api_instance.update_sheet_by_id(spreadsheet_id, sheet_id, sheet)
        print("The response of SpreadsheetsApi->update_sheet_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->update_sheet_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **sheet_id** | **str**| The unique identifier of the sheet | 
 **sheet** | [**Sheet**](Sheet.md)| All properties for the sheet, not just those to update | 

### Return type

[**Sheet**](Sheet.md)

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

# **update_values_by_range**
> update_values_by_range(spreadsheet_id, sheet_id, range, range_values)

Update values in a range

Overwrites all values in a range with new values. The provided range must not exceed the specified range. If the provided range of values is *smaller* than the specified range, it clears all cells in the range **and** those not covered by the range values. Rows of values in the provided range must be of equal length. An empty range of values is valid and may be used to clear a range. To indicate that a cell's value shouldn't be replaced, use the special cell value `null`. When you add a value to a cell, it uses Ones scale regardless of the cell's scale formatting.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.range_values import RangeValues
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    sheet_id = 'sheet_id_example' # str | The unique identifier of the sheet
    range = 'range_example' # str | The range of values, in A1-style notation
    range_values = {"values":[[1,4],[2,""]]} # RangeValues | All values for the range, not just those to update

    try:
        # Update values in a range
        api_instance.update_values_by_range(spreadsheet_id, sheet_id, range, range_values)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->update_values_by_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **sheet_id** | **str**| The unique identifier of the sheet | 
 **range** | **str**| The range of values, in A1-style notation | 
 **range_values** | [**RangeValues**](RangeValues.md)| All values for the range, not just those to update | 

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

# **upsert_datasets**
> upsert_datasets(spreadsheet_id, dataset)

Bulk upsert of datasets

Asynchronously upserts an array of [datasets](ref:platform-spreadsheets#dataset) to a [spreadsheet](ref:platform-spreadsheets#spreadsheet), given their properties. Each [sheet](ref:platform-spreadsheet#sheet) can have only one dataset, and its range will always start with `A1`. <br /><br /> Bulk upsertion creates or updates datasets in sheets and performs any calculations after it completes. When complete, the dataset's range is locked through both the UI and endpoints that write values to a sheet. To change the values in a dataset, either upsert new values using this endpoint again, or delete the dataset. <br /><br /> If any dataset fails to upsert, no datasets upsert, and no changes commit. <br /><br /> Each dataset in the array requires `sheet` and `values`. Partial upserts are not supported. <br /><br /> Values may be strings, numbers, integers, or booleans. To indicate an empty cell, provide an empty string.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.dataset import Dataset
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
    api_instance = openapi_client.SpreadsheetsApi(api_client)
    spreadsheet_id = 'spreadsheet_id_example' # str | The unique identifier of the spreadsheet
    dataset = [openapi_client.Dataset()] # List[Dataset] | An array of datasets

    try:
        # Bulk upsert of datasets
        api_instance.upsert_datasets(spreadsheet_id, dataset)
    except Exception as e:
        print("Exception when calling SpreadsheetsApi->upsert_datasets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spreadsheet_id** | **str**| The unique identifier of the spreadsheet | 
 **dataset** | [**List[Dataset]**](Dataset.md)| An array of datasets | 

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

