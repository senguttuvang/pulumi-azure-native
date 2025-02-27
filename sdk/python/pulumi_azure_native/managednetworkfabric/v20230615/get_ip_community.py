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
    'GetIpCommunityResult',
    'AwaitableGetIpCommunityResult',
    'get_ip_community',
    'get_ip_community_output',
]

@pulumi.output_type
class GetIpCommunityResult:
    """
    The IP Community resource definition.
    """
    def __init__(__self__, administrative_state=None, annotation=None, configuration_state=None, id=None, ip_community_rules=None, location=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if administrative_state and not isinstance(administrative_state, str):
            raise TypeError("Expected argument 'administrative_state' to be a str")
        pulumi.set(__self__, "administrative_state", administrative_state)
        if annotation and not isinstance(annotation, str):
            raise TypeError("Expected argument 'annotation' to be a str")
        pulumi.set(__self__, "annotation", annotation)
        if configuration_state and not isinstance(configuration_state, str):
            raise TypeError("Expected argument 'configuration_state' to be a str")
        pulumi.set(__self__, "configuration_state", configuration_state)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_community_rules and not isinstance(ip_community_rules, list):
            raise TypeError("Expected argument 'ip_community_rules' to be a list")
        pulumi.set(__self__, "ip_community_rules", ip_community_rules)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> str:
        """
        Administrative state of the resource.
        """
        return pulumi.get(self, "administrative_state")

    @property
    @pulumi.getter
    def annotation(self) -> Optional[str]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> str:
        """
        Configuration state of the resource.
        """
        return pulumi.get(self, "configuration_state")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipCommunityRules")
    def ip_community_rules(self) -> Sequence['outputs.IpCommunityRuleResponse']:
        """
        List of IP Community Rules.
        """
        return pulumi.get(self, "ip_community_rules")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetIpCommunityResult(GetIpCommunityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpCommunityResult(
            administrative_state=self.administrative_state,
            annotation=self.annotation,
            configuration_state=self.configuration_state,
            id=self.id,
            ip_community_rules=self.ip_community_rules,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_ip_community(ip_community_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpCommunityResult:
    """
    Implements an IP Community GET method.


    :param str ip_community_name: Name of the IP Community.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['ipCommunityName'] = ip_community_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetworkfabric/v20230615:getIpCommunity', __args__, opts=opts, typ=GetIpCommunityResult).value

    return AwaitableGetIpCommunityResult(
        administrative_state=pulumi.get(__ret__, 'administrative_state'),
        annotation=pulumi.get(__ret__, 'annotation'),
        configuration_state=pulumi.get(__ret__, 'configuration_state'),
        id=pulumi.get(__ret__, 'id'),
        ip_community_rules=pulumi.get(__ret__, 'ip_community_rules'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_ip_community)
def get_ip_community_output(ip_community_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIpCommunityResult]:
    """
    Implements an IP Community GET method.


    :param str ip_community_name: Name of the IP Community.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
