# Edit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The operation to carry out (see enumerated values) | 
**label** | **str** | To create or delete a relationship, the label describing how the records are related  | [optional] 
**type** | **str** | To create a record, the type of record to create  | [optional] 
**record_id** | **str** | To create or delete a relationship, the actual ID or temporaryRecordId of the source record. | [optional] 
**target_id** | **str** | To create or delete a relationship, the ID of its target record. If creating, the actual ID or temporaryRecordId. If deleting, the actual ID.  | [optional] 
**temporary_record_id** | **str** | To create a record, a temporary ID that is replaced at time of processing. You can subsequently use this ID within the same request to create relationships between created records. | [optional] 
**properties** | **object** | To create a record or set its properties, the properties related to the record type. Keyed by the property name, this always includes the &#x60;datatype&#x60; and &#x60;value&#x60;. When setting properties, send a partial object representing only the values to update. Valid datatypes are &#x60;integer&#x60;, &#x60;number&#x60;, &#x60;boolean&#x60;, &#x60;string&#x60;, &#x60;date-time&#x60;, &#x60;map&#x60;, &#x60;list&#x60;, &#x60;array&#x60;, and &#x60;set&#x60;. | [optional] 

## Example

```python
from openapi_client.models.edit import Edit

# TODO update the JSON string below
json = "{}"
# create an instance of Edit from a JSON string
edit_instance = Edit.from_json(json)
# print the JSON string representation of the object
print(Edit.to_json())

# convert the object into a dict
edit_dict = edit_instance.to_dict()
# create an instance of Edit from a dict
edit_from_dict = Edit.from_dict(edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


