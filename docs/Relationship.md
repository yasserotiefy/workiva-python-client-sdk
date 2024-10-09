# Relationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_label** | **str** | A human-readable description of the relationship between the two items | [optional] [readonly] 
**label** | **str** | A description of the relationship between the two items | [optional] [readonly] 
**from_type** | **str** | The unique identifier of the source type. For a type, its name. | [optional] [readonly] 
**to_type** | **str** | The unique identifier of the target Type. For a type, its name. | [optional] [readonly] 
**from_record** | **str** | The unique identifier of the source record | [optional] [readonly] 
**to_record** | **str** | The unique identifier of the target record | [optional] [readonly] 

## Example

```python
from openapi_client.models.relationship import Relationship

# TODO update the JSON string below
json = "{}"
# create an instance of Relationship from a JSON string
relationship_instance = Relationship.from_json(json)
# print the JSON string representation of the object
print(Relationship.to_json())

# convert the object into a dict
relationship_dict = relationship_instance.to_dict()
# create an instance of Relationship from a dict
relationship_from_dict = Relationship.from_dict(relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


