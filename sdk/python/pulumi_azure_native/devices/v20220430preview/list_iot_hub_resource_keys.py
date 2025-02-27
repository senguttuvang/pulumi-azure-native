# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'ListIotHubResourceKeysResult',
    'AwaitableListIotHubResourceKeysResult',
    'list_iot_hub_resource_keys',
    'list_iot_hub_resource_keys_output',
]

@pulumi.output_type
class ListIotHubResourceKeysResult:
    """
    The list of shared access policies with a next link.
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
    def next_link(self) -> str:
        """
        The next link.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.SharedAccessSignatureAuthorizationRuleResponse']]:
        """
        The list of shared access policies.
        """
        return pulumi.get(self, "value")


class AwaitableListIotHubResourceKeysResult(ListIotHubResourceKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListIotHubResourceKeysResult(
            next_link=self.next_link,
            value=self.value)


def list_iot_hub_resource_keys(resource_group_name: Optional[str] = None,
                               resource_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListIotHubResourceKeysResult:
    """
    Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.


    :param str resource_group_name: The name of the resource group that contains the IoT hub.
    :param str resource_name: The name of the IoT hub.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devices/v20220430preview:listIotHubResourceKeys', __args__, opts=opts, typ=ListIotHubResourceKeysResult).value

    return AwaitableListIotHubResourceKeysResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_iot_hub_resource_keys)
def list_iot_hub_resource_keys_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                      resource_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListIotHubResourceKeysResult]:
    """
    Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.


    :param str resource_group_name: The name of the resource group that contains the IoT hub.
    :param str resource_name: The name of the IoT hub.
    """
    ...
