# Record


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the record | [optional] [readonly] 
**type** | **str** | The type of the record | [optional] [readonly] 
**properties** | **object** | The properties related to this type of record. Keyed by the property name, this always includes the &#x60;datatype&#x60; and &#x60;value&#x60;.  * See [edits](ref:platform-createedits) endpoint for modification of record properties | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) | An array of relationships that exist with this record  * See [edits](ref:platform-createedits) endpoint for modification of record relationships | [optional] [readonly] 

## Example

```python
from openapi_client.models.record import Record

# TODO update the JSON string below
json = "{}"
# create an instance of Record from a JSON string
record_instance = Record.from_json(json)
# print the JSON string representation of the object
print(Record.to_json())

# convert the object into a dict
record_dict = record_instance.to_dict()
# create an instance of Record from a dict
record_from_dict = Record.from_dict(record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


