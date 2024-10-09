# openapi_client.OperationsApi

All URIs are relative to *https://api.app.wdesk.com/platform/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_operation_by_id**](OperationsApi.md#get_operation_by_id) | **GET** /operations/{operationId} | Retrieve a single operation


# **get_operation_by_id**
> Operation get_operation_by_id(operation_id)

Retrieve a single operation

Retrieves an [operation](ref:platform-operations#operation) given its ID. <br /><br /> Note: This endpoint is rate-limited. You may experience rates as low as 1 request per second. When polling for updates, examine the `Retry-After` header and retry after that many seconds. 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.operation import Operation
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
    api_instance = openapi_client.OperationsApi(api_client)
    operation_id = 'operation_id_example' # str | The unique identifier of the operation

    try:
        # Retrieve a single operation
        api_response = api_instance.get_operation_by_id(operation_id)
        print("The response of OperationsApi->get_operation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OperationsApi->get_operation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_id** | **str**| The unique identifier of the operation | 

### Return type

[**Operation**](Operation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Retry-After - The number of seconds to wait before polling for a result and between polling attempts. <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

