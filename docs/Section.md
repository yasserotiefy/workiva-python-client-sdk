# Section

Details about the section, including its ID and name. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the section | [optional] 
**name** | **str** | The name of the section | [optional] 
**parent** | [**Section**](Section.md) |  | [optional] 
**index** | **int** | The integer index of the section relative to its parent section (or to the document if no parent section). The special value -1 may be used to position a section at the end of its siblings list. | [optional] 
**children** | [**List[Section]**](Section.md) | An array of partial information about any sections within the section | [optional] [readonly] 
**non_printing** | **bool** | Whether or not the section is non-printing | [optional] 

## Example

```python
from openapi_client.models.section import Section

# TODO update the JSON string below
json = "{}"
# create an instance of Section from a JSON string
section_instance = Section.from_json(json)
# print the JSON string representation of the object
print(Section.to_json())

# convert the object into a dict
section_dict = section_instance.to_dict()
# create an instance of Section from a dict
section_from_dict = Section.from_dict(section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


