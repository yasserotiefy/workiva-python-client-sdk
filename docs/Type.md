# Type


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique name of the record type | [readonly] 
**properties** | **List[str]** | The list of properties related to this record type | [readonly] 
**relationships** | [**List[Relationship]**](Relationship.md) | An array of relationships that exist with this type | [optional] [readonly] 

## Example

```python
from openapi_client.models.type import Type

# TODO update the JSON string below
json = "{}"
# create an instance of Type from a JSON string
type_instance = Type.from_json(json)
# print the JSON string representation of the object
print(Type.to_json())

# convert the object into a dict
type_dict = type_instance.to_dict()
# create an instance of Type from a dict
type_from_dict = Type.from_dict(type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


