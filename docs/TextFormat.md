# TextFormat

Text formats. Fields that are omitted will be ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bold** | **bool** | Text bold format | [optional] 
**italic** | **bool** | Text italic format | [optional] 
**underline** | **bool** | Text underline format | [optional] 
**strikethrough** | **bool** | Text strikethrough format | [optional] 
**font_family** | **str** | Text font format | [optional] 
**font_size** | **float** | Text font size, in points | [optional] 
**font_color** | **str** | A hex color code | [optional] [default to '#000000']

## Example

```python
from openapi_client.models.text_format import TextFormat

# TODO update the JSON string below
json = "{}"
# create an instance of TextFormat from a JSON string
text_format_instance = TextFormat.from_json(json)
# print the JSON string representation of the object
print(TextFormat.to_json())

# convert the object into a dict
text_format_dict = text_format_instance.to_dict()
# create an instance of TextFormat from a dict
text_format_from_dict = TextFormat.from_dict(text_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


