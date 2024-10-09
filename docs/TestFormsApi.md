# openapi_client.TestFormsApi

All URIs are relative to *https://api.app.wdesk.com/platform/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_matrix**](TestFormsApi.md#create_matrix) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices | Create a new matrix
[**create_sample**](TestFormsApi.md#create_sample) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples | Create a new sample
[**get_matrices**](TestFormsApi.md#get_matrices) | **GET** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices | Retrieve a list of matrices
[**get_matrix_attachment_by_id**](TestFormsApi.md#get_matrix_attachment_by_id) | **GET** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/attachments/{attachmentId} | Retrieve a single matrix attachment
[**get_matrix_attachments**](TestFormsApi.md#get_matrix_attachments) | **GET** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/attachments | Retrieve a list of matrix attachments
[**get_matrix_by_id**](TestFormsApi.md#get_matrix_by_id) | **GET** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId} | Retrieve a single matrix
[**get_sample_attachment_by_id**](TestFormsApi.md#get_sample_attachment_by_id) | **GET** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}/attachments/{attachmentId} | Retrieve a single sample attachment
[**get_sample_attachments**](TestFormsApi.md#get_sample_attachments) | **GET** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}/attachments | Retrieve a list of sample attachments
[**get_sample_by_id**](TestFormsApi.md#get_sample_by_id) | **GET** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId} | Retrieve a single sample
[**get_samples**](TestFormsApi.md#get_samples) | **GET** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples | Retrieve a list of samples
[**get_test_form_by_id**](TestFormsApi.md#get_test_form_by_id) | **GET** /testForms/{testFormId} | Retrieve a single test form
[**get_test_forms**](TestFormsApi.md#get_test_forms) | **GET** /testForms | Retrieve a list of test forms
[**get_test_phase_attachment_by_id**](TestFormsApi.md#get_test_phase_attachment_by_id) | **GET** /testForms/{testFormId}/testPhases/{testPhaseId}/attachments/{attachmentId} | Retrieve a single test phase attachment
[**get_test_phase_attachments**](TestFormsApi.md#get_test_phase_attachments) | **GET** /testForms/{testFormId}/testPhases/{testPhaseId}/attachments | Retrieve a list of test phase attachments
[**get_test_phase_by_id**](TestFormsApi.md#get_test_phase_by_id) | **GET** /testForms/{testFormId}/testPhases/{testPhaseId} | Retrive a single test phase
[**get_test_phases**](TestFormsApi.md#get_test_phases) | **GET** /testForms/{testFormId}/testPhases | Retrieve a list of test phases
[**matrix_attachment_download_by_id**](TestFormsApi.md#matrix_attachment_download_by_id) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/attachments/{attachmentId}/download | Initiate a matrix attachment download
[**matrix_attachment_export_by_id**](TestFormsApi.md#matrix_attachment_export_by_id) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/attachments/{attachmentId}/export | Initiate an export of a matrix attachment
[**matrix_attachment_upload**](TestFormsApi.md#matrix_attachment_upload) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/attachmentUpload | Initiate a matrix attachment upload
[**partially_update_sample_by_id**](TestFormsApi.md#partially_update_sample_by_id) | **PATCH** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId} | Partially update a single sample
[**sample_attachment_download_by_id**](TestFormsApi.md#sample_attachment_download_by_id) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}/attachments/{attachmentId}/download | Initiate a download of a sample attachment
[**sample_attachment_export_by_id**](TestFormsApi.md#sample_attachment_export_by_id) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}/attachments/{attachmentId}/export | Initiate an export of a sample attachment
[**sample_attachment_upload**](TestFormsApi.md#sample_attachment_upload) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId}/attachmentUpload | Initiate an upload of a sample attachment
[**sample_insertion**](TestFormsApi.md#sample_insertion) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/insertion | Insert samples
[**sample_update**](TestFormsApi.md#sample_update) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/update | Update samples
[**test_form_export**](TestFormsApi.md#test_form_export) | **POST** /testForms/{testFormId}/export | Initiate a test form export
[**test_phase_attachment_download_by_id**](TestFormsApi.md#test_phase_attachment_download_by_id) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/attachments/{attachmentId}/download | Initiate a test phase attachment download
[**test_phase_attachment_export_by_id**](TestFormsApi.md#test_phase_attachment_export_by_id) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/attachments/{attachmentId}/export | Initiate a test phase attachment export
[**test_phase_attachment_upload**](TestFormsApi.md#test_phase_attachment_upload) | **POST** /testForms/{testFormId}/testPhases/{testPhaseId}/attachmentUpload | Initiate a test phase attachment upload
[**update_sample_by_id**](TestFormsApi.md#update_sample_by_id) | **PUT** /testForms/{testFormId}/testPhases/{testPhaseId}/matrices/{matrixId}/samples/{sampleId} | Update a single sample


# **create_matrix**
> Matrix create_matrix(test_form_id, test_phase_id, matrix)

Create a new matrix

Create a new empty [matrix](ref:platform-testforms#matrix). The `id` field for the matrix and its columns should be left blank; this will be populated by the endpoint. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.matrix import Matrix
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix = {"name":"Purchase Orders","dataColumns":[{"name":"PO Number","externalId":"TA05"},{"name":"Amount","externalId":"TA06"}],"resultColumns":[{"name":"A","externalId":"TA07"}]} # Matrix | The properties of the matrix to create

    try:
        # Create a new matrix
        api_response = api_instance.create_matrix(test_form_id, test_phase_id, matrix)
        print("The response of TestFormsApi->create_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->create_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix** | [**Matrix**](Matrix.md)| The properties of the matrix to create | 

### Return type

[**Matrix**](Matrix.md)

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

# **create_sample**
> MatrixSample create_sample(test_form_id, test_phase_id, matrix_id, matrix_sample)

Create a new sample

Create a new [sample](ref:platform-testforms#matrixsample) in a [matrix](ref:platform-testforms#matrix). The new sample will be appended to the end of the matrix. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.matrix_sample import MatrixSample
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    matrix_sample = {"dataValues":[{"column":"d795d7a3-e7f7-4b3f-be6a-109653b2929b","value":789},{"column":"fbd818ec-4fd1-42ad-9112-3c80e71dc2dc","value":303.3}],"resultValues":[{"column":"d795d7a3-e7f7-4b3f-be6a-109653b2c34d","value":"PASS"}]} # MatrixSample | The properties of the sample to create

    try:
        # Create a new sample
        api_response = api_instance.create_sample(test_form_id, test_phase_id, matrix_id, matrix_sample)
        print("The response of TestFormsApi->create_sample:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->create_sample: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **matrix_sample** | [**MatrixSample**](MatrixSample.md)| The properties of the sample to create | 

### Return type

[**MatrixSample**](MatrixSample.md)

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

# **get_matrices**
> MatricesListResult get_matrices(test_form_id, test_phase_id, expand=expand)

Retrieve a list of matrices

Returns a list of [matrices](ref:platform-testforms#matrix). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.matrices_list_result import MatricesListResult
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrieve a list of matrices
        api_response = api_instance.get_matrices(test_form_id, test_phase_id, expand=expand)
        print("The response of TestFormsApi->get_matrices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_matrices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**MatricesListResult**](MatricesListResult.md)

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

# **get_matrix_attachment_by_id**
> GraphAttachment get_matrix_attachment_by_id(test_form_id, test_phase_id, matrix_id, attachment_id)

Retrieve a single matrix attachment

Retrieve a single [attachment](ref:platform-testforms#graphattachment) by its ID. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_attachment import GraphAttachment
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    attachment_id = 'attachment_id_example' # str | The unique identifier of the attachment

    try:
        # Retrieve a single matrix attachment
        api_response = api_instance.get_matrix_attachment_by_id(test_form_id, test_phase_id, matrix_id, attachment_id)
        print("The response of TestFormsApi->get_matrix_attachment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_matrix_attachment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **attachment_id** | **str**| The unique identifier of the attachment | 

### Return type

[**GraphAttachment**](GraphAttachment.md)

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

# **get_matrix_attachments**
> GraphAttachmentsListResult get_matrix_attachments(test_form_id, test_phase_id, matrix_id)

Retrieve a list of matrix attachments

Returns a list of [attachments](ref:platform-testforms#graphattachment) for a matrix. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_attachments_list_result import GraphAttachmentsListResult
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix

    try:
        # Retrieve a list of matrix attachments
        api_response = api_instance.get_matrix_attachments(test_form_id, test_phase_id, matrix_id)
        print("The response of TestFormsApi->get_matrix_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_matrix_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 

### Return type

[**GraphAttachmentsListResult**](GraphAttachmentsListResult.md)

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

# **get_matrix_by_id**
> Matrix get_matrix_by_id(test_form_id, test_phase_id, matrix_id, expand=expand)

Retrieve a single matrix

Retrieves a [matrix](ref:platform-testforms#matrix) given its ID. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.matrix import Matrix
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrieve a single matrix
        api_response = api_instance.get_matrix_by_id(test_form_id, test_phase_id, matrix_id, expand=expand)
        print("The response of TestFormsApi->get_matrix_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_matrix_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**Matrix**](Matrix.md)

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

# **get_sample_attachment_by_id**
> GraphAttachment get_sample_attachment_by_id(test_form_id, test_phase_id, matrix_id, sample_id, attachment_id)

Retrieve a single sample attachment

Retrieve a single [attachment](ref:platform-testforms#graphattachment) by its ID. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_attachment import GraphAttachment
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    sample_id = 'sample_id_example' # str | The unique identifier of the sample
    attachment_id = 'attachment_id_example' # str | The unique identifier of the attachment

    try:
        # Retrieve a single sample attachment
        api_response = api_instance.get_sample_attachment_by_id(test_form_id, test_phase_id, matrix_id, sample_id, attachment_id)
        print("The response of TestFormsApi->get_sample_attachment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_sample_attachment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **sample_id** | **str**| The unique identifier of the sample | 
 **attachment_id** | **str**| The unique identifier of the attachment | 

### Return type

[**GraphAttachment**](GraphAttachment.md)

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

# **get_sample_attachments**
> GraphAttachmentsListResult get_sample_attachments(test_form_id, test_phase_id, matrix_id, sample_id)

Retrieve a list of sample attachments

Returns a list of [attachments](ref:platform-testforms#graphattachment) for a [sample](ref:platform-testforms#matrixsample). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_attachments_list_result import GraphAttachmentsListResult
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    sample_id = 'sample_id_example' # str | The unique identifier of the sample

    try:
        # Retrieve a list of sample attachments
        api_response = api_instance.get_sample_attachments(test_form_id, test_phase_id, matrix_id, sample_id)
        print("The response of TestFormsApi->get_sample_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_sample_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **sample_id** | **str**| The unique identifier of the sample | 

### Return type

[**GraphAttachmentsListResult**](GraphAttachmentsListResult.md)

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

# **get_sample_by_id**
> MatrixSample get_sample_by_id(test_form_id, test_phase_id, matrix_id, sample_id, expand=expand)

Retrieve a single sample

Retrieves a [sample](ref:platform-testforms#matrixsample) given its ID. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.matrix_sample import MatrixSample
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    sample_id = 'sample_id_example' # str | The unique identifier of the sample
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrieve a single sample
        api_response = api_instance.get_sample_by_id(test_form_id, test_phase_id, matrix_id, sample_id, expand=expand)
        print("The response of TestFormsApi->get_sample_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_sample_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **sample_id** | **str**| The unique identifier of the sample | 
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**MatrixSample**](MatrixSample.md)

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

# **get_samples**
> MatrixSamplesListResult get_samples(test_form_id, test_phase_id, matrix_id, expand=expand)

Retrieve a list of samples

Returns a list of [samples](ref:platform-testforms#matrixsample). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.matrix_samples_list_result import MatrixSamplesListResult
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrieve a list of samples
        api_response = api_instance.get_samples(test_form_id, test_phase_id, matrix_id, expand=expand)
        print("The response of TestFormsApi->get_samples:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_samples: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**MatrixSamplesListResult**](MatrixSamplesListResult.md)

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

# **get_test_form_by_id**
> TestForm get_test_form_by_id(test_form_id, expand=expand)

Retrieve a single test form

Retrieves a [test form](ref:platform-testforms#testform) given its ID. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.test_form import TestForm
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrieve a single test form
        api_response = api_instance.get_test_form_by_id(test_form_id, expand=expand)
        print("The response of TestFormsApi->get_test_form_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_test_form_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**TestForm**](TestForm.md)

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

# **get_test_forms**
> TestFormsListResult get_test_forms(expand=expand)

Retrieve a list of test forms

Retrieves a list of [test forms](ref:platform-testforms#testform). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.test_forms_list_result import TestFormsListResult
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
    api_instance = openapi_client.TestFormsApi(api_client)
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrieve a list of test forms
        api_response = api_instance.get_test_forms(expand=expand)
        print("The response of TestFormsApi->get_test_forms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_test_forms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**TestFormsListResult**](TestFormsListResult.md)

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

# **get_test_phase_attachment_by_id**
> GraphAttachment get_test_phase_attachment_by_id(test_form_id, test_phase_id, attachment_id)

Retrieve a single test phase attachment

Retrieve a single [attachment](ref:platform-testforms#graphattachment) by its ID. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_attachment import GraphAttachment
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    attachment_id = 'attachment_id_example' # str | The unique identifier of the attachment

    try:
        # Retrieve a single test phase attachment
        api_response = api_instance.get_test_phase_attachment_by_id(test_form_id, test_phase_id, attachment_id)
        print("The response of TestFormsApi->get_test_phase_attachment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_test_phase_attachment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **attachment_id** | **str**| The unique identifier of the attachment | 

### Return type

[**GraphAttachment**](GraphAttachment.md)

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

# **get_test_phase_attachments**
> GraphAttachmentsListResult get_test_phase_attachments(test_form_id, test_phase_id)

Retrieve a list of test phase attachments

Returns a list of [attachments](ref:platform-testforms#graphattachment) for a [test phase](ref:platform-testforms#testphase). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_attachments_list_result import GraphAttachmentsListResult
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase

    try:
        # Retrieve a list of test phase attachments
        api_response = api_instance.get_test_phase_attachments(test_form_id, test_phase_id)
        print("The response of TestFormsApi->get_test_phase_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_test_phase_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 

### Return type

[**GraphAttachmentsListResult**](GraphAttachmentsListResult.md)

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

# **get_test_phase_by_id**
> TestPhase get_test_phase_by_id(test_form_id, test_phase_id, expand=expand)

Retrive a single test phase

Retrieves a [test phase](ref:platform-testforms#testphase) given its ID. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.test_phase import TestPhase
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrive a single test phase
        api_response = api_instance.get_test_phase_by_id(test_form_id, test_phase_id, expand=expand)
        print("The response of TestFormsApi->get_test_phase_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_test_phase_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**TestPhase**](TestPhase.md)

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

# **get_test_phases**
> TestPhasesListResult get_test_phases(test_form_id, expand=expand)

Retrieve a list of test phases

Returns a list of [test phases](ref:platform-testforms#testphase). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.test_phases_list_result import TestPhasesListResult
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    expand = '?$expand=relationships ' # str | Returns related resources inline with the main resource (optional)

    try:
        # Retrieve a list of test phases
        api_response = api_instance.get_test_phases(test_form_id, expand=expand)
        print("The response of TestFormsApi->get_test_phases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->get_test_phases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **expand** | **str**| Returns related resources inline with the main resource | [optional] 

### Return type

[**TestPhasesListResult**](TestPhasesListResult.md)

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

# **matrix_attachment_download_by_id**
> matrix_attachment_download_by_id(test_form_id, test_phase_id, matrix_id, attachment_id)

Initiate a matrix attachment download

Asynchronously downloads an attachment from a [matrix](ref:platform-testforms#matrix).  Responses include a `Location` header, which indicates where to poll for download results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid). When the download is ready, its status will be `completed`, and the response body includes a `resourceURL`. To download the file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the download request. For more details, see [Authentication documentation](ref:platform-authentication). 

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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    attachment_id = 'attachment_id_example' # str | The unique identifier of the attachment

    try:
        # Initiate a matrix attachment download
        api_instance.matrix_attachment_download_by_id(test_form_id, test_phase_id, matrix_id, attachment_id)
    except Exception as e:
        print("Exception when calling TestFormsApi->matrix_attachment_download_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **attachment_id** | **str**| The unique identifier of the attachment | 

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

# **matrix_attachment_export_by_id**
> matrix_attachment_export_by_id(test_form_id, test_phase_id, matrix_id, attachment_id, graph_attachment_export)

Initiate an export of a matrix attachment

Asynchronously exports an attachment for a [matrix](ref:platform-testforms#matrix) to .PDF.  Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:platform-authentication). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_attachment_export import GraphAttachmentExport
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    attachment_id = 'attachment_id_example' # str | The unique identifier of the attachment
    graph_attachment_export = openapi_client.GraphAttachmentExport() # GraphAttachmentExport | Details about the attachment upload

    try:
        # Initiate an export of a matrix attachment
        api_instance.matrix_attachment_export_by_id(test_form_id, test_phase_id, matrix_id, attachment_id, graph_attachment_export)
    except Exception as e:
        print("Exception when calling TestFormsApi->matrix_attachment_export_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **attachment_id** | **str**| The unique identifier of the attachment | 
 **graph_attachment_export** | [**GraphAttachmentExport**](GraphAttachmentExport.md)| Details about the attachment upload | 

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

# **matrix_attachment_upload**
> GraphAttachmentUploadResponse matrix_attachment_upload(test_form_id, test_phase_id, matrix_id, graph_attachment_upload)

Initiate a matrix attachment upload

Starts the process to upload and attach a file to a [matrix](ref:platform-testforms#matrix) using a [graph attachment upload](ref:platform-testforms#graphattachmentupload) object. The response body will include an `uploadUrl`. To upload the file contents, perform a PUT on the `uploadUrl` with the same authentication credentials and flow as the attachmentUpload request. For more details, see [Authentication documentation](ref:platform-overview#authentication).  The response also includes a `Location` header, which indicates where to poll for operation results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_attachment_upload import GraphAttachmentUpload
from openapi_client.models.graph_attachment_upload_response import GraphAttachmentUploadResponse
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    graph_attachment_upload = openapi_client.GraphAttachmentUpload() # GraphAttachmentUpload | Details about the attachment upload

    try:
        # Initiate a matrix attachment upload
        api_response = api_instance.matrix_attachment_upload(test_form_id, test_phase_id, matrix_id, graph_attachment_upload)
        print("The response of TestFormsApi->matrix_attachment_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->matrix_attachment_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **graph_attachment_upload** | [**GraphAttachmentUpload**](GraphAttachmentUpload.md)| Details about the attachment upload | 

### Return type

[**GraphAttachmentUploadResponse**](GraphAttachmentUploadResponse.md)

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

# **partially_update_sample_by_id**
> MatrixSample partially_update_sample_by_id(test_form_id, test_phase_id, matrix_id, sample_id, json_patch_operation)

Partially update a single sample

Partially updates the properties of a [sample](ref:platform-testforms#matrixsample). Note: Cell values must always be strings, even if they represent a number. ### Options |Path|PATCH Operations Supported| |---|---| |`/dataValues/<index>/value`|`replace`| |`/resultValues/<index>/value`|`replace`| 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.json_patch_operation import JSONPatchOperation
from openapi_client.models.matrix_sample import MatrixSample
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    sample_id = 'sample_id_example' # str | The unique identifier of the sample
    json_patch_operation = [{"op":"replace","path":"/dataValues/0/value","value":"22.5"}] # List[JSONPatchOperation] | A collection of patch operations to apply to the sample.

    try:
        # Partially update a single sample
        api_response = api_instance.partially_update_sample_by_id(test_form_id, test_phase_id, matrix_id, sample_id, json_patch_operation)
        print("The response of TestFormsApi->partially_update_sample_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->partially_update_sample_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **sample_id** | **str**| The unique identifier of the sample | 
 **json_patch_operation** | [**List[JSONPatchOperation]**](JSONPatchOperation.md)| A collection of patch operations to apply to the sample. | 

### Return type

[**MatrixSample**](MatrixSample.md)

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

# **sample_attachment_download_by_id**
> sample_attachment_download_by_id(test_form_id, test_phase_id, matrix_id, sample_id, attachment_id)

Initiate a download of a sample attachment

Asynchronously downloads an attachment from a [sample](ref:platform-testforms#matrixsample).  Responses include a `Location` header, which indicates where to poll for download results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid). When the download is ready, its status will be `completed`, and the response body includes a `resourceURL`. To download the file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the download request. For more details, see [Authentication documentation](ref:platform-authentication). 

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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    sample_id = 'sample_id_example' # str | The unique identifier of the sample
    attachment_id = 'attachment_id_example' # str | The unique identifier of the attachment

    try:
        # Initiate a download of a sample attachment
        api_instance.sample_attachment_download_by_id(test_form_id, test_phase_id, matrix_id, sample_id, attachment_id)
    except Exception as e:
        print("Exception when calling TestFormsApi->sample_attachment_download_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **sample_id** | **str**| The unique identifier of the sample | 
 **attachment_id** | **str**| The unique identifier of the attachment | 

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

# **sample_attachment_export_by_id**
> sample_attachment_export_by_id(test_form_id, test_phase_id, matrix_id, sample_id, attachment_id, graph_attachment_export)

Initiate an export of a sample attachment

Asynchronously exports an attachment for a [sample](ref:platform-testforms#matrixsample) to .PDF.  Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:platform-authentication). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_attachment_export import GraphAttachmentExport
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    sample_id = 'sample_id_example' # str | The unique identifier of the sample
    attachment_id = 'attachment_id_example' # str | The unique identifier of the attachment
    graph_attachment_export = openapi_client.GraphAttachmentExport() # GraphAttachmentExport | Details about the attachment export

    try:
        # Initiate an export of a sample attachment
        api_instance.sample_attachment_export_by_id(test_form_id, test_phase_id, matrix_id, sample_id, attachment_id, graph_attachment_export)
    except Exception as e:
        print("Exception when calling TestFormsApi->sample_attachment_export_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **sample_id** | **str**| The unique identifier of the sample | 
 **attachment_id** | **str**| The unique identifier of the attachment | 
 **graph_attachment_export** | [**GraphAttachmentExport**](GraphAttachmentExport.md)| Details about the attachment export | 

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

# **sample_attachment_upload**
> GraphAttachmentUploadResponse sample_attachment_upload(test_form_id, test_phase_id, matrix_id, sample_id, graph_attachment_upload)

Initiate an upload of a sample attachment

Starts the process to upload and attach a file to a [sample](ref:platform-testforms#matrixsample) using a [graph attachment upload](ref:platform-testforms#graphattachmentupload) object. The response body will include an `uploadUrl`. To upload the file contents, perform a PUT on the `uploadUrl` with the same authentication credentials and flow as the attachmentUpload request. For more details, see [Authentication documentation](ref:platform-authentication).  The response also includes a `Location` header, which indicates where to poll for operation results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_attachment_upload import GraphAttachmentUpload
from openapi_client.models.graph_attachment_upload_response import GraphAttachmentUploadResponse
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    sample_id = 'sample_id_example' # str | The unique identifier of the sample
    graph_attachment_upload = openapi_client.GraphAttachmentUpload() # GraphAttachmentUpload | Details about the attachment upload

    try:
        # Initiate an upload of a sample attachment
        api_response = api_instance.sample_attachment_upload(test_form_id, test_phase_id, matrix_id, sample_id, graph_attachment_upload)
        print("The response of TestFormsApi->sample_attachment_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->sample_attachment_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **sample_id** | **str**| The unique identifier of the sample | 
 **graph_attachment_upload** | [**GraphAttachmentUpload**](GraphAttachmentUpload.md)| Details about the attachment upload | 

### Return type

[**GraphAttachmentUploadResponse**](GraphAttachmentUploadResponse.md)

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

# **sample_insertion**
> sample_insertion(test_form_id, test_phase_id, matrix_id, matrix_sample)

Insert samples

Inserts multiple [samples](ref:platform-testforms#matrixsamples) into a [matrix](ref:platform-testforms#matrix), and appends new samples to the end of the matrix. You can leave columns empty for later use. For new samples, provide no IDs; the endpoint generates them.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.matrix_sample import MatrixSample
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    matrix_sample = [{"dataValues":[{"column":"d795d7a3-e7f7-4b3f-be6a-109653b2929b","value":123},{"column":"fbd818ec-4fd1-42ad-9112-3c80e71dc2dc","value":101.1}],"resultValues":[{"column":"d795d7a3-e7f7-4b3f-be6a-109653b2c34d","value":"PASS"}]},{"dataValues":[{"column":"d795d7a3-e7f7-4b3f-be6a-109653b2929b","value":456},{"column":"fbd818ec-4fd1-42ad-9112-3c80e71dc2dc","value":202.2}],"resultValues":[{"column":"d795d7a3-e7f7-4b3f-be6a-109653b2c34d","value":"FAIL"}]}] # List[MatrixSample] | Details about the samples to insert

    try:
        # Insert samples
        api_instance.sample_insertion(test_form_id, test_phase_id, matrix_id, matrix_sample)
    except Exception as e:
        print("Exception when calling TestFormsApi->sample_insertion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **matrix_sample** | [**List[MatrixSample]**](MatrixSample.md)| Details about the samples to insert | 

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

# **sample_update**
> sample_update(test_form_id, test_phase_id, matrix_id, matrix_sample)

Update samples

Updates multiple [samples](ref:platform-testforms#matrixsamples), with the requestBody of each specifying columns to update by their IDs. Columns not included in the request remain as-is.

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.matrix_sample import MatrixSample
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    matrix_sample = [{"id":"3dd42da0-3543-4e03-ac4a-2ddefebe27d6","dataValues":[{"column":"6d870cd1-7bbe-4b14-b85d-f152913b068c","value":23897}],"resultValues":[{"column":"674a9283-fd03-425d-bd62-0552263699e2","value":"PASS"}]},{"id":"4ee53eb1-3543-4e03-ac4a-3eef0fcf38e7","dataValues":[{"column":"6d870cd1-7bbe-4b14-b85d-f152913b068c","value":9125}],"resultValues":[{"column":"674a9283-fd03-425d-bd62-0552263699e2","value":"FAIL"}]}] # List[MatrixSample] | Details about the samples to update

    try:
        # Update samples
        api_instance.sample_update(test_form_id, test_phase_id, matrix_id, matrix_sample)
    except Exception as e:
        print("Exception when calling TestFormsApi->sample_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **matrix_sample** | [**List[MatrixSample]**](MatrixSample.md)| Details about the samples to update | 

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

# **test_form_export**
> test_form_export(test_form_id, test_form_export)

Initiate a test form export

Asynchronously exports a [test form](ref:platform-testforms#testform).  Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:platform-authentication). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.test_form_export import TestFormExport
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_form_export = openapi_client.TestFormExport() # TestFormExport | Details about the test form export

    try:
        # Initiate a test form export
        api_instance.test_form_export(test_form_id, test_form_export)
    except Exception as e:
        print("Exception when calling TestFormsApi->test_form_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_form_export** | [**TestFormExport**](TestFormExport.md)| Details about the test form export | 

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

# **test_phase_attachment_download_by_id**
> test_phase_attachment_download_by_id(test_form_id, test_phase_id, attachment_id)

Initiate a test phase attachment download

Asynchronously downloads an attachment from a [test phase](ref:platform-testforms#testphase).  Responses include a `Location` header, which indicates where to poll for download results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid). When the download is ready, its status will be `completed`, and the response body includes a `resourceURL`. To download the file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the download request. For more details, see [Authentication documentation](ref:platform-authentication). 

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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    attachment_id = 'attachment_id_example' # str | The unique identifier of the attachment

    try:
        # Initiate a test phase attachment download
        api_instance.test_phase_attachment_download_by_id(test_form_id, test_phase_id, attachment_id)
    except Exception as e:
        print("Exception when calling TestFormsApi->test_phase_attachment_download_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **attachment_id** | **str**| The unique identifier of the attachment | 

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

# **test_phase_attachment_export_by_id**
> test_phase_attachment_export_by_id(test_form_id, test_phase_id, attachment_id, graph_attachment_export)

Initiate a test phase attachment export

Asynchronously exports an attachment for a [test phase](ref:platform-testforms#testphase) to .PDF.  Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:platform-authentication). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_attachment_export import GraphAttachmentExport
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    attachment_id = 'attachment_id_example' # str | The unique identifier of the attachment
    graph_attachment_export = openapi_client.GraphAttachmentExport() # GraphAttachmentExport | Details about the attachment export

    try:
        # Initiate a test phase attachment export
        api_instance.test_phase_attachment_export_by_id(test_form_id, test_phase_id, attachment_id, graph_attachment_export)
    except Exception as e:
        print("Exception when calling TestFormsApi->test_phase_attachment_export_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **attachment_id** | **str**| The unique identifier of the attachment | 
 **graph_attachment_export** | [**GraphAttachmentExport**](GraphAttachmentExport.md)| Details about the attachment export | 

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

# **test_phase_attachment_upload**
> GraphAttachmentUploadResponse test_phase_attachment_upload(test_form_id, test_phase_id, graph_attachment_upload)

Initiate a test phase attachment upload

Starts the process to upload and attach a file to a [test phase](ref:platform-testforms#testphase) using a [graph attachment upload](ref:platform-testforms#graphattachmentupload) object. The response body will include an `uploadUrl`. To upload the file contents, perform a PUT on the `uploadUrl` with the same authentication credentials and flow as the attachmentUpload request. For more details, see [Authentication documentation](ref:platform-authentication).  The response also includes a `Location` header, which indicates where to poll for operation results. For more details on long-running job polling, see [Operations endpoint](ref:platform-operations#getoperationbyid).

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.graph_attachment_upload import GraphAttachmentUpload
from openapi_client.models.graph_attachment_upload_response import GraphAttachmentUploadResponse
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    graph_attachment_upload = openapi_client.GraphAttachmentUpload() # GraphAttachmentUpload | Details about the attachment

    try:
        # Initiate a test phase attachment upload
        api_response = api_instance.test_phase_attachment_upload(test_form_id, test_phase_id, graph_attachment_upload)
        print("The response of TestFormsApi->test_phase_attachment_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->test_phase_attachment_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **graph_attachment_upload** | [**GraphAttachmentUpload**](GraphAttachmentUpload.md)| Details about the attachment | 

### Return type

[**GraphAttachmentUploadResponse**](GraphAttachmentUploadResponse.md)

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

# **update_sample_by_id**
> MatrixSample update_sample_by_id(test_form_id, test_phase_id, matrix_id, sample_id, matrix_sample)

Update a single sample

Fully replaces all elements of a [sample](ref:platform-testforms#matrixsample); this is *not* a partial update. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.matrix_sample import MatrixSample
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
    api_instance = openapi_client.TestFormsApi(api_client)
    test_form_id = 'test_form_id_example' # str | The unique identifier of the test form
    test_phase_id = 'test_phase_id_example' # str | The unique identifier of the test phase
    matrix_id = 'matrix_id_example' # str | The unique identifier of the matrix
    sample_id = 'sample_id_example' # str | The unique identifier of the sample
    matrix_sample = {"id":"ce4a6c7f-15ad-445c-a76a-f457d53f667a","dataValues":[{"column":"d795d7a3-e7f7-4b3f-be6a-109653b2929b","value":124},{"column":"fbd818ec-4fd1-42ad-9112-3c80e71dc2dc","value":101.2}],"resultValues":[{"column":"d795d7a3-e7f7-4b3f-be6a-109653b2c34d","value":"PASS"}]} # MatrixSample | All properties for the sample, not just those to update

    try:
        # Update a single sample
        api_response = api_instance.update_sample_by_id(test_form_id, test_phase_id, matrix_id, sample_id, matrix_sample)
        print("The response of TestFormsApi->update_sample_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestFormsApi->update_sample_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_form_id** | **str**| The unique identifier of the test form | 
 **test_phase_id** | **str**| The unique identifier of the test phase | 
 **matrix_id** | **str**| The unique identifier of the matrix | 
 **sample_id** | **str**| The unique identifier of the sample | 
 **matrix_sample** | [**MatrixSample**](MatrixSample.md)| All properties for the sample, not just those to update | 

### Return type

[**MatrixSample**](MatrixSample.md)

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

