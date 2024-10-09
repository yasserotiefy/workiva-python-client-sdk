# EditsResult

A response from the POST edits endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id_map** | **object** | A mapping between temporary and actual record IDs | [optional] [readonly] 

## Example

```python
from openapi_client.models.edits_result import EditsResult

# TODO update the JSON string below
json = "{}"
# create an instance of EditsResult from a JSON string
edits_result_instance = EditsResult.from_json(json)
# print the JSON string representation of the object
print(EditsResult.to_json())

# convert the object into a dict
edits_result_dict = edits_result_instance.to_dict()
# create an instance of EditsResult from a dict
edits_result_from_dict = EditsResult.from_dict(edits_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


