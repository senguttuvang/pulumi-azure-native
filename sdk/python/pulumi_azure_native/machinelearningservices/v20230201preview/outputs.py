# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'FeatureResponse',
]

@pulumi.output_type
class FeatureResponse(dict):
    """
    Dto object representing feature
    """
    def __init__(__self__, *,
                 data_type: Optional[str] = None,
                 description: Optional[str] = None,
                 feature_name: Optional[str] = None,
                 tags: Optional[Mapping[str, str]] = None):
        """
        Dto object representing feature
        :param str data_type: Specifies type
        :param str description: Specifies description
        :param str feature_name: Specifies name
        :param Mapping[str, str] tags: Specifies tags
        """
        if data_type is None:
            data_type = 'String'
        if data_type is not None:
            pulumi.set(__self__, "data_type", data_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if feature_name is not None:
            pulumi.set(__self__, "feature_name", feature_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional[str]:
        """
        Specifies type
        """
        return pulumi.get(self, "data_type")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Specifies description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="featureName")
    def feature_name(self) -> Optional[str]:
        """
        Specifies name
        """
        return pulumi.get(self, "feature_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Specifies tags
        """
        return pulumi.get(self, "tags")


