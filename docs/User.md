# User

Details about the user, including their name, ID, and email address 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the user | [optional] 
**user_name** | **str** | Username of the user | [optional] [readonly] 
**display_name** | **str** | Display name of the user | [optional] [readonly] 
**first_name** | **str** | First name of the user | [optional] [readonly] 
**last_name** | **str** | Last name of the user | [optional] [readonly] 
**email** | **str** | Email address of the user | [optional] [readonly] 

## Example

```python
from openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


