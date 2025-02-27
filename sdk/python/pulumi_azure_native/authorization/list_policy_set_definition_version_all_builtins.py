# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'ListPolicySetDefinitionVersionAllBuiltinsResult',
    'AwaitableListPolicySetDefinitionVersionAllBuiltinsResult',
    'list_policy_set_definition_version_all_builtins',
    'list_policy_set_definition_version_all_builtins_output',
]

@pulumi.output_type
class ListPolicySetDefinitionVersionAllBuiltinsResult:
    """
    List of policy set definition versions.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        The URL to use for getting the next set of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.PolicySetDefinitionVersionResponse']]:
        """
        An array of policy set definition versions.
        """
        return pulumi.get(self, "value")


class AwaitableListPolicySetDefinitionVersionAllBuiltinsResult(ListPolicySetDefinitionVersionAllBuiltinsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListPolicySetDefinitionVersionAllBuiltinsResult(
            next_link=self.next_link,
            value=self.value)


def list_policy_set_definition_version_all_builtins(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListPolicySetDefinitionVersionAllBuiltinsResult:
    """
    This operation lists all the built-in policy set definition versions for all built-in policy set definitions.
    Azure REST API version: 2023-04-01.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:authorization:listPolicySetDefinitionVersionAllBuiltins', __args__, opts=opts, typ=ListPolicySetDefinitionVersionAllBuiltinsResult).value

    return AwaitableListPolicySetDefinitionVersionAllBuiltinsResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_policy_set_definition_version_all_builtins)
def list_policy_set_definition_version_all_builtins_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListPolicySetDefinitionVersionAllBuiltinsResult]:
    """
    This operation lists all the built-in policy set definition versions for all built-in policy set definitions.
    Azure REST API version: 2023-04-01.
    """
    ...
