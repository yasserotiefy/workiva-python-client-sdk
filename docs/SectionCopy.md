# SectionCopy

Details about the destination document and, optionally, the destination section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **str** | The unique identifier of the document to copy a section into | 
**section_index** | **int** | The integer index of where within the siblings to place the new section; 0 by default. To place the section at the end of its siblings, use the special value -1. | [optional] 
**section_parent** | **str** | The ID of the parent section to copy the section into. To place the section at the top level of the document, use the default null. | [optional] 
**section_name** | **str** | The name of the new section, if different than the source section | [optional] 

## Example

```python
from openapi_client.models.section_copy import SectionCopy

# TODO update the JSON string below
json = "{}"
# create an instance of SectionCopy from a JSON string
section_copy_instance = SectionCopy.from_json(json)
# print the JSON string representation of the object
print(SectionCopy.to_json())

# convert the object into a dict
section_copy_dict = section_copy_instance.to_dict()
# create an instance of SectionCopy from a dict
section_copy_from_dict = SectionCopy.from_dict(section_copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


