# coding: utf-8

"""
    Platform API

    Use the Workiva Platform API to programmatically manage items in the Workiva platform, such as files, folders, tasks, comments, documents, spreadsheets, and presentations. 

    The version of the OpenAPI document: v1
    Contact: platformsupport@workiva.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.relationship import Relationship
from typing import Optional, Set
from typing_extensions import Self

class Record(BaseModel):
    """
    Record
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the record")
    type: Optional[StrictStr] = Field(default=None, description="The type of the record")
    properties: Optional[Dict[str, Any]] = Field(default=None, description="The properties related to this type of record. Keyed by the property name, this always includes the `datatype` and `value`.  * See [edits](ref:platform-createedits) endpoint for modification of record properties")
    relationships: Optional[List[Relationship]] = Field(default=None, description="An array of relationships that exist with this record  * See [edits](ref:platform-createedits) endpoint for modification of record relationships")
    __properties: ClassVar[List[str]] = ["id", "type", "properties", "relationships"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Record from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "type",
            "relationships",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in relationships (list)
        _items = []
        if self.relationships:
            for _item_relationships in self.relationships:
                if _item_relationships:
                    _items.append(_item_relationships.to_dict())
            _dict['relationships'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Record from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "properties": obj.get("properties"),
            "relationships": [Relationship.from_dict(_item) for _item in obj["relationships"]] if obj.get("relationships") is not None else None
        })
        return _obj

