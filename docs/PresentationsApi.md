# openapi_client.PresentationsApi

All URIs are relative to *https://api.app.wdesk.com/platform/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**presentation_export**](PresentationsApi.md#presentation_export) | **POST** /presentations/{presentationId}/export | Initiate a presentation export


# **presentation_export**
> presentation_export(presentation_id, presentation_export)

Initiate a presentation export

Asynchronously export a presentation as .PDF or .PPTX. Options are specified using a [PresentationExport](ref:platform-presentations#presentationexport) object.  Responses include a `Location` header, which indicates where to poll for export results. For more details on long-running job polling, see [ Operations endpoint ](ref:platform-operations#getoperationbyid). When the export completes, its status will be `completed`, and the response body includes a `resourceURL`. To download the exported file, perform a GET on the `resourceURL` with the same authentication credentials and flow as the export request. For more details, see [Authentication documentation](ref:platform-authentication). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.presentation_export import PresentationExport
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
    api_instance = openapi_client.PresentationsApi(api_client)
    presentation_id = 'presentation_id_example' # str | The unique identifier of the presentation
    presentation_export = openapi_client.PresentationExport() # PresentationExport | Details about the presentation export.

    try:
        # Initiate a presentation export
        api_instance.presentation_export(presentation_id, presentation_export)
    except Exception as e:
        print("Exception when calling PresentationsApi->presentation_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **presentation_id** | **str**| The unique identifier of the presentation | 
 **presentation_export** | [**PresentationExport**](PresentationExport.md)| Details about the presentation export. | 

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

