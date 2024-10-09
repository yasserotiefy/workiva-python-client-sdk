# openapi_client.DocumentsApi

All URIs are relative to *https://api.app.wdesk.com/platform/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_section**](DocumentsApi.md#copy_section) | **POST** /documents/{documentId}/sections/{sectionId}/copy | Copy section
[**create_section**](DocumentsApi.md#create_section) | **POST** /documents/{documentId}/sections | Create a new section in a document
[**delete_section_by_id**](DocumentsApi.md#delete_section_by_id) | **DELETE** /documents/{documentId}/sections/{sectionId} | Delete a single section
[**document_export**](DocumentsApi.md#document_export) | **POST** /documents/{documentId}/export | Initiate a document export
[**get_document_by_id**](DocumentsApi.md#get_document_by_id) | **GET** /documents/{documentId} | Retrieve a single document
[**get_documents**](DocumentsApi.md#get_documents) | **GET** /documents | Retrieve a list of documents
[**get_section_by_id**](DocumentsApi.md#get_section_by_id) | **GET** /documents/{documentId}/sections/{sectionId} | Retrieve a single section
[**get_sections**](DocumentsApi.md#get_sections) | **GET** /documents/{documentId}/sections | Retrieve a list of sections
[**partially_update_section_by_id**](DocumentsApi.md#partially_update_section_by_id) | **PATCH** /documents/{documentId}/sections/{sectionId} | Partially update a single section
[**update_section_by_id**](DocumentsApi.md#update_section_by_id) | **PUT** /documents/{documentId}/sections/{sectionId} | Update a single section


# **copy_section**
> copy_section(document_id, section_id, section_copy)

Copy section

Asynchronously copies a [section](ref:platform-documents#section) given details about the copy's destination within the same or another document. Options are specified using a [SectionCopy](ref:platform-documents#sectioncopy) object.  Copies only the section's content — not any labels, comments, tasks, or formatting from a style guide. Unless otherwise specified, the copy appears at the top level of its destination document, with an index of 0, and with the same name as the original section.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.section_copy import SectionCopy
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
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | The unique identifier of the document
    section_id = 'section_id_example' # str | The unique identifier of the section
    section_copy = openapi_client.SectionCopy() # SectionCopy | A SectionCopy object

    try:
        # Copy section
        api_instance.copy_section(document_id, section_id, section_copy)
    except Exception as e:
        print("Exception when calling DocumentsApi->copy_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The unique identifier of the document | 
 **section_id** | **str**| The unique identifier of the section | 
 **section_copy** | [**SectionCopy**](SectionCopy.md)| A SectionCopy object | 

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

# **create_section**
> Section create_section(document_id, section)

Create a new section in a document

Creates a new [section](ref:platform-documents#section) in a [document](ref:platform-documents#document), given its properties. By default, the new section appears at the top-most position. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.section import Section
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
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | The unique identifier of the document
    section = {"name":"Risk Factor","parent":{"id":"a8b3adb687644b27fafcb3a9875f0f0d_18"}} # Section | The properties of the section to create

    try:
        # Create a new section in a document
        api_response = api_instance.create_section(document_id, section)
        print("The response of DocumentsApi->create_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->create_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The unique identifier of the document | 
 **section** | [**Section**](Section.md)| The properties of the section to create | 

### Return type

[**Section**](Section.md)

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

# **delete_section_by_id**
> delete_section_by_id(document_id, section_id)

Delete a single section

Deletes a [section](ref:platform-documents#section) given its ID. 

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
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | The unique identifier of the document
    section_id = 'section_id_example' # str | The unique identifier of the section

    try:
        # Delete a single section
        api_instance.delete_section_by_id(document_id, section_id)
    except Exception as e:
        print("Exception when calling DocumentsApi->delete_section_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The unique identifier of the document | 
 **section_id** | **str**| The unique identifier of the section | 

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

# **document_export**
> document_export(document_id, document_export)

Initiate a document export

Asynchronously exports a [document](ref:platform-documents#document) as .PDF or .DOCX., or .XHTML. Options are specified using a [DocumentExport](ref:platform-documents#documentexport) object. When exporting XHTML that you plan to edit or modify, use the `editableXhtml` option. Otherwise, the export retains fidelity so it visually matches the document as it appears in the browser. Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:platform-authentication). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.document_export import DocumentExport
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
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | The unique identifier of the document
    document_export = openapi_client.DocumentExport() # DocumentExport | Details about the document export.

    try:
        # Initiate a document export
        api_instance.document_export(document_id, document_export)
    except Exception as e:
        print("Exception when calling DocumentsApi->document_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The unique identifier of the document | 
 **document_export** | [**DocumentExport**](DocumentExport.md)| Details about the document export. | 

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

# **get_document_by_id**
> Document get_document_by_id(document_id, expand=expand)

Retrieve a single document

Retrieves a [document](ref:platform-documents#document) given its ID. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.document import Document
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
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | The unique identifier of the document
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrieve a single document
        api_response = api_instance.get_document_by_id(document_id, expand=expand)
        print("The response of DocumentsApi->get_document_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The unique identifier of the document | 
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**Document**](Document.md)

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

# **get_documents**
> DocumentsListResult get_documents(filter=filter, order_by=order_by, maxpagesize=maxpagesize, next=next)

Retrieve a list of documents

Returns a paginated list of [documents](ref:platform-documents#document).

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.documents_list_result import DocumentsListResult
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
    api_instance = openapi_client.DocumentsApi(api_client)
    filter = 'filter_example' # str | The properties to filter the results by. (optional)
    order_by = 'order_by_example' # str | One or more comma-separated expressions to indicate the order in which to sort the results. (optional)
    maxpagesize = 1000 # int | The maximum number of results to retrieve (optional) (default to 1000)
    next = 'JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA' # str | Pagination cursor for next set of results. (optional)

    try:
        # Retrieve a list of documents
        api_response = api_instance.get_documents(filter=filter, order_by=order_by, maxpagesize=maxpagesize, next=next)
        print("The response of DocumentsApi->get_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The properties to filter the results by. | [optional] 
 **order_by** | **str**| One or more comma-separated expressions to indicate the order in which to sort the results. | [optional] 
 **maxpagesize** | **int**| The maximum number of results to retrieve | [optional] [default to 1000]
 **next** | **str**| Pagination cursor for next set of results. | [optional] 

### Return type

[**DocumentsListResult**](DocumentsListResult.md)

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

# **get_section_by_id**
> Section get_section_by_id(document_id, section_id)

Retrieve a single section

Retrieves a [section](ref:platform-documents#section) given its ID. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.section import Section
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
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | The unique identifier of the document
    section_id = 'section_id_example' # str | The unique identifier of the section

    try:
        # Retrieve a single section
        api_response = api_instance.get_section_by_id(document_id, section_id)
        print("The response of DocumentsApi->get_section_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_section_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The unique identifier of the document | 
 **section_id** | **str**| The unique identifier of the section | 

### Return type

[**Section**](Section.md)

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

# **get_sections**
> SectionsListResult get_sections(document_id)

Retrieve a list of sections

Returns a list of [sections](ref:platform-documents#section). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.sections_list_result import SectionsListResult
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
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | The unique identifier of the document

    try:
        # Retrieve a list of sections
        api_response = api_instance.get_sections(document_id)
        print("The response of DocumentsApi->get_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The unique identifier of the document | 

### Return type

[**SectionsListResult**](SectionsListResult.md)

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

# **partially_update_section_by_id**
> Section partially_update_section_by_id(document_id, section_id, json_patch_operation)

Partially update a single section

Partially updates the properties of a [section](ref:platform-documents#section). ### Options |Path|PATCH Operations Supported| |---|---| |`/name`|`replace`| |`/index`|`replace`| |`/parent`|`replace`|  ### Examples #### Update the name of a section ```json [   {     \"op\": \"replace\",     \"path\": \"/name\",     \"value\": \"Introduction\"   } ] ``` #### Update the parent of a section (preserving its index) ```json [   {     \"op\": \"replace\",     \"path\": \"/parent\",     \"value\": {       \"id\": \"b9b3ddb587744a27aafda3c9865f1f0a_1\"     }   } ] ``` #### Update the parent of a section (making it the first child) ```json [   {     \"op\": \"replace\",     \"path\": \"/parent\",     \"value\": {       \"id\": \"b9b3ddb587744a27aafda3c9865f1f0a_1\"     }   },   {     \"op\": \"replace\",     \"path\": \"/index\",     \"value\": 0   } ] ``` 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.json_patch_operation import JSONPatchOperation
from openapi_client.models.section import Section
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
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | The unique identifier of the document
    section_id = 'section_id_example' # str | The unique identifier of the section
    json_patch_operation = [{"op":"replace","path":"/name","value":"New Name"}] # List[JSONPatchOperation] | A collection of patch operations to apply to the section.

    try:
        # Partially update a single section
        api_response = api_instance.partially_update_section_by_id(document_id, section_id, json_patch_operation)
        print("The response of DocumentsApi->partially_update_section_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->partially_update_section_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The unique identifier of the document | 
 **section_id** | **str**| The unique identifier of the section | 
 **json_patch_operation** | [**List[JSONPatchOperation]**](JSONPatchOperation.md)| A collection of patch operations to apply to the section. | 

### Return type

[**Section**](Section.md)

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

# **update_section_by_id**
> Section update_section_by_id(document_id, section_id, section)

Update a single section

Fully replaces all details of a [section](ref:platform-documents#section) given its properties; this is *not* a partial update.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.section import Section
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
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | The unique identifier of the document
    section_id = 'section_id_example' # str | The unique identifier of the section
    section = {"name":"Risk Factor","index":1,"parent":{"id":"a8b3adb687644b27fafcb3a9875f0f0d_18"}} # Section | All properties for the section, not just those to update

    try:
        # Update a single section
        api_response = api_instance.update_section_by_id(document_id, section_id, section)
        print("The response of DocumentsApi->update_section_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->update_section_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The unique identifier of the document | 
 **section_id** | **str**| The unique identifier of the section | 
 **section** | [**Section**](Section.md)| All properties for the section, not just those to update | 

### Return type

[**Section**](Section.md)

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

