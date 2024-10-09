# UsersListResult

Returns a JSON object with `data` and `@nextLink` properties. `data` contains a list of [`User`](ref:platform-users#user) objects, and `@nextLink` provides the URL to the next set of results. If there are no additional results, `@nextLink` doesn't appear. If the request returns no results at all, `data` contains an empty array.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[User]**](User.md) |  | [optional] 
**next_link** | **str** | Pagination link for next set of results | [optional] 

## Example

```python
from openapi_client.models.users_list_result import UsersListResult

# TODO update the JSON string below
json = "{}"
# create an instance of UsersListResult from a JSON string
users_list_result_instance = UsersListResult.from_json(json)
# print the JSON string representation of the object
print(UsersListResult.to_json())

# convert the object into a dict
users_list_result_dict = users_list_result_instance.to_dict()
# create an instance of UsersListResult from a dict
users_list_result_from_dict = UsersListResult.from_dict(users_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


