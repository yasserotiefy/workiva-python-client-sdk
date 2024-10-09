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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ValueFormatPeriodFormat(BaseModel):
    """
    Options for formatting a duration string. Valid for PERIOD
    """ # noqa: E501
    display: StrictStr = Field(description="Method of displaying the period value")
    separator: Optional[StrictStr] = Field(default='COMMA', description="The separator to use between denominations if multiple are displayed")
    precision: Optional[Annotated[int, Field(le=15, strict=True, ge=0)]] = Field(default=None, description="Precision to use when rounding decimal numbers for display. Renders with automatic precision if null.")
    show_labels: Optional[StrictBool] = Field(default=True, description="Render a label after each denomination", alias="showLabels")
    show_numbers_as_words: Optional[StrictBool] = Field(default=False, description="Render the numbers as words instead of digits", alias="showNumbersAsWords")
    capitalize_first_word: Optional[StrictBool] = Field(default=False, description="Capitalize the first word", alias="capitalizeFirstWord")
    __properties: ClassVar[List[str]] = ["display", "separator", "precision", "showLabels", "showNumbersAsWords", "capitalizeFirstWord"]

    @field_validator('display')
    def display_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['RAW', 'LARGEST', 'YEARS', 'ALL']):
            raise ValueError("must be one of enum values ('RAW', 'LARGEST', 'YEARS', 'ALL')")
        return value

    @field_validator('separator')
    def separator_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NONE', 'COMMA']):
            raise ValueError("must be one of enum values ('NONE', 'COMMA')")
        return value

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
        """Create an instance of ValueFormatPeriodFormat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if precision (nullable) is None
        # and model_fields_set contains the field
        if self.precision is None and "precision" in self.model_fields_set:
            _dict['precision'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValueFormatPeriodFormat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "display": obj.get("display"),
            "separator": obj.get("separator") if obj.get("separator") is not None else 'COMMA',
            "precision": obj.get("precision"),
            "showLabels": obj.get("showLabels") if obj.get("showLabels") is not None else True,
            "showNumbersAsWords": obj.get("showNumbersAsWords") if obj.get("showNumbersAsWords") is not None else False,
            "capitalizeFirstWord": obj.get("capitalizeFirstWord") if obj.get("capitalizeFirstWord") is not None else False
        })
        return _obj

