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
    'GetPlacementPolicyResult',
    'AwaitableGetPlacementPolicyResult',
    'get_placement_policy',
    'get_placement_policy_output',
]

@pulumi.output_type
class GetPlacementPolicyResult:
    """
    A vSphere Distributed Resource Scheduler (DRS) placement policy
    """
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
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
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> Any:
        """
        placement policy properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetPlacementPolicyResult(GetPlacementPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPlacementPolicyResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_placement_policy(cluster_name: Optional[str] = None,
                         placement_policy_name: Optional[str] = None,
                         private_cloud_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPlacementPolicyResult:
    """
    A vSphere Distributed Resource Scheduler (DRS) placement policy


    :param str cluster_name: Name of the cluster in the private cloud
    :param str placement_policy_name: Name of the VMware vSphere Distributed Resource Scheduler (DRS) placement policy
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['placementPolicyName'] = placement_policy_name
    __args__['privateCloudName'] = private_cloud_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:avs/v20230301:getPlacementPolicy', __args__, opts=opts, typ=GetPlacementPolicyResult).value

    return AwaitableGetPlacementPolicyResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_placement_policy)
def get_placement_policy_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                placement_policy_name: Optional[pulumi.Input[str]] = None,
                                private_cloud_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPlacementPolicyResult]:
    """
    A vSphere Distributed Resource Scheduler (DRS) placement policy


    :param str cluster_name: Name of the cluster in the private cloud
    :param str placement_policy_name: Name of the VMware vSphere Distributed Resource Scheduler (DRS) placement policy
    :param str private_cloud_name: Name of the private cloud
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
