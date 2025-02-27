# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'PlanArgs',
]

@pulumi.input_type
class PlanArgs:
    def __init__(__self__, *,
                 accessibility: Optional[pulumi.Input[Union[str, 'Accessibility']]] = None):
        """
        :param pulumi.Input[Union[str, 'Accessibility']] accessibility: Plan accessibility
        """
        if accessibility is not None:
            pulumi.set(__self__, "accessibility", accessibility)

    @property
    @pulumi.getter
    def accessibility(self) -> Optional[pulumi.Input[Union[str, 'Accessibility']]]:
        """
        Plan accessibility
        """
        return pulumi.get(self, "accessibility")

    @accessibility.setter
    def accessibility(self, value: Optional[pulumi.Input[Union[str, 'Accessibility']]]):
        pulumi.set(self, "accessibility", value)


