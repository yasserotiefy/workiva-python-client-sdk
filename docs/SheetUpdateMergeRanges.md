# SheetUpdateMergeRanges

Merge ranges

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ranges** | [**List[Range]**](Range.md) | The ranges to merge | 
**merge_type** | **str** | How cells should be merged | [optional] [default to 'ALL']
**force** | **bool** | Force the merge through source links, xbrl facts, ESG connections, etc | [optional] 

## Example

```python
from openapi_client.models.sheet_update_merge_ranges import SheetUpdateMergeRanges

# TODO update the JSON string below
json = "{}"
# create an instance of SheetUpdateMergeRanges from a JSON string
sheet_update_merge_ranges_instance = SheetUpdateMergeRanges.from_json(json)
# print the JSON string representation of the object
print(SheetUpdateMergeRanges.to_json())

# convert the object into a dict
sheet_update_merge_ranges_dict = sheet_update_merge_ranges_instance.to_dict()
# create an instance of SheetUpdateMergeRanges from a dict
sheet_update_merge_ranges_from_dict = SheetUpdateMergeRanges.from_dict(sheet_update_merge_ranges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


