# openapi_client.UsersApi

All URIs are relative to *https://api.app.wdesk.com/platform/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_users**](UsersApi.md#get_users) | **GET** /users | Retrieve a list of users


# **get_users**
> UsersListResult get_users(filter=filter, order_by=order_by, maxpagesize=maxpagesize, next=next)

Retrieve a list of users

Returns a paginated list of [users](ref:platform-users#user). 

### Example

* OAuth Authentication (oauth):

```python
import openapi_client
from openapi_client.models.users_list_result import UsersListResult
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
    api_instance = openapi_client.UsersApi(api_client)
    filter = 'filter_example' # str | The properties to filter the results by. (optional)
    order_by = 'order_by_example' # str | One or more comma-separated expressions to indicate the order in which to sort the results. (optional)
    maxpagesize = 1000 # int | The maximum number of results to retrieve (optional) (default to 1000)
    next = 'JTI0bGltaXQ9MTAwJiUyNG9mZnNldD0xMDA' # str | Pagination cursor for next set of results. (optional)

    try:
        # Retrieve a list of users
        api_response = api_instance.get_users(filter=filter, order_by=order_by, maxpagesize=maxpagesize, next=next)
        print("The response of UsersApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The properties to filter the results by. | [optional] 
 **order_by** | **str**| One or more comma-separated expressions to indicate the order in which to sort the results. | [optional] 
 **maxpagesize** | **int**| The maximum number of results to retrieve | [optional] [default to 1000]
 **next** | **str**| Pagination cursor for next set of results. | [optional] 

### Return type

[**UsersListResult**](UsersListResult.md)

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

