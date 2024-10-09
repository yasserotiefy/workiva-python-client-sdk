# DocumentToDocxOptions

Optional options to export the document as a Microsoft Word document (.DOCX). If no options are provided, all options default to False. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_leader_dots** | **bool** | Whether to include leader dots when exporting to .DOCX. False by default. | [optional] [default to False]
**show_table_cell_shading** | **bool** | Whether to show table cell shading when exporting to .DOCX. False by default. | [optional] [default to False]

## Example

```python
from openapi_client.models.document_to_docx_options import DocumentToDocxOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentToDocxOptions from a JSON string
document_to_docx_options_instance = DocumentToDocxOptions.from_json(json)
# print the JSON string representation of the object
print(DocumentToDocxOptions.to_json())

# convert the object into a dict
document_to_docx_options_dict = document_to_docx_options_instance.to_dict()
# create an instance of DocumentToDocxOptions from a dict
document_to_docx_options_from_dict = DocumentToDocxOptions.from_dict(document_to_docx_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


