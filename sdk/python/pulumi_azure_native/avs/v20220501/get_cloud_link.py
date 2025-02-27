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
    'GetCloudLinkResult',
    'AwaitableGetCloudLinkResult',
    'get_cloud_link',
    'get_cloud_link_output',
]

@pulumi.output_type
class GetCloudLinkResult:
    """
    A cloud link resource
    """
    def __init__(__self__, id=None, linked_cloud=None, name=None, status=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if linked_cloud and not isinstance(linked_cloud, str):
            raise TypeError("Expected argument 'linked_cloud' to be a str")
        pulumi.set(__self__, "linked_cloud", linked_cloud)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="linkedCloud")
    def linked_cloud(self) -> Optional[str]:
        """
        Identifier of the other private cloud participating in the link.
        """
        return pulumi.get(self, "linked_cloud")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The state of the cloud link.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetCloudLinkResult(GetCloudLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudLinkResult(
            id=self.id,
            linked_cloud=self.linked_cloud,
            name=self.name,
            status=self.status,
            type=self.type)


def get_cloud_link(cloud_link_name: Optional[str] = None,
                   private_cloud_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudLinkResult:
    """
    A cloud link resource


    :param str cloud_link_name: Name of the cloud link resource
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['cloudLinkName'] = cloud_link_name
    __args__['privateCloudName'] = private_cloud_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:avs/v20220501:getCloudLink', __args__, opts=opts, typ=GetCloudLinkResult).value

    return AwaitableGetCloudLinkResult(
        id=pulumi.get(__ret__, 'id'),
        linked_cloud=pulumi.get(__ret__, 'linked_cloud'),
        name=pulumi.get(__ret__, 'name'),
        status=pulumi.get(__ret__, 'status'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_cloud_link)
def get_cloud_link_output(cloud_link_name: Optional[pulumi.Input[str]] = None,
                          private_cloud_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloudLinkResult]:
    """
    A cloud link resource


    :param str cloud_link_name: Name of the cloud link resource
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
