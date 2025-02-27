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
    'GetNetworkFunctionResult',
    'AwaitableGetNetworkFunctionResult',
    'get_network_function',
    'get_network_function_output',
]

@pulumi.output_type
class GetNetworkFunctionResult:
    """
    AO5GC Network Function Resource
    """
    def __init__(__self__, capacity=None, deployment_notes=None, id=None, infrastructure_element_count=None, location=None, name=None, network_function_administrative_state=None, network_function_operational_status=None, network_function_type=None, provisioning_state=None, sku=None, system_data=None, tags=None, type=None, user_description=None):
        if capacity and not isinstance(capacity, int):
            raise TypeError("Expected argument 'capacity' to be a int")
        pulumi.set(__self__, "capacity", capacity)
        if deployment_notes and not isinstance(deployment_notes, str):
            raise TypeError("Expected argument 'deployment_notes' to be a str")
        pulumi.set(__self__, "deployment_notes", deployment_notes)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if infrastructure_element_count and not isinstance(infrastructure_element_count, int):
            raise TypeError("Expected argument 'infrastructure_element_count' to be a int")
        pulumi.set(__self__, "infrastructure_element_count", infrastructure_element_count)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_function_administrative_state and not isinstance(network_function_administrative_state, str):
            raise TypeError("Expected argument 'network_function_administrative_state' to be a str")
        pulumi.set(__self__, "network_function_administrative_state", network_function_administrative_state)
        if network_function_operational_status and not isinstance(network_function_operational_status, str):
            raise TypeError("Expected argument 'network_function_operational_status' to be a str")
        pulumi.set(__self__, "network_function_operational_status", network_function_operational_status)
        if network_function_type and not isinstance(network_function_type, str):
            raise TypeError("Expected argument 'network_function_type' to be a str")
        pulumi.set(__self__, "network_function_type", network_function_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, str):
            raise TypeError("Expected argument 'sku' to be a str")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_description and not isinstance(user_description, str):
            raise TypeError("Expected argument 'user_description' to be a str")
        pulumi.set(__self__, "user_description", user_description)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[int]:
        """
        Capacity of the network function in units of 10000.  This represents the session count or the Simultaneously Attached Users (SAU) count as applicable
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter(name="deploymentNotes")
    def deployment_notes(self) -> Optional[str]:
        """
        User provided deployment notes.  This is used to optionally provide details about the NF deployment
        """
        return pulumi.get(self, "deployment_notes")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="infrastructureElementCount")
    def infrastructure_element_count(self) -> int:
        """
        Count of infrastructure elements used by this network function (vCPUs, in units of 8)
        """
        return pulumi.get(self, "infrastructure_element_count")

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
    @pulumi.getter(name="networkFunctionAdministrativeState")
    def network_function_administrative_state(self) -> str:
        """
        Administrative state of the network function
        """
        return pulumi.get(self, "network_function_administrative_state")

    @property
    @pulumi.getter(name="networkFunctionOperationalStatus")
    def network_function_operational_status(self) -> str:
        """
        Operational state of the network function
        """
        return pulumi.get(self, "network_function_operational_status")

    @property
    @pulumi.getter(name="networkFunctionType")
    def network_function_type(self) -> str:
        """
        Type of network function
        """
        return pulumi.get(self, "network_function_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> str:
        """
        Provisioned SKU Value.
        """
        return pulumi.get(self, "sku")

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

    @property
    @pulumi.getter(name="userDescription")
    def user_description(self) -> Optional[str]:
        """
        User provided description
        """
        return pulumi.get(self, "user_description")


class AwaitableGetNetworkFunctionResult(GetNetworkFunctionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkFunctionResult(
            capacity=self.capacity,
            deployment_notes=self.deployment_notes,
            id=self.id,
            infrastructure_element_count=self.infrastructure_element_count,
            location=self.location,
            name=self.name,
            network_function_administrative_state=self.network_function_administrative_state,
            network_function_operational_status=self.network_function_operational_status,
            network_function_type=self.network_function_type,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            user_description=self.user_description)


def get_network_function(network_function_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkFunctionResult:
    """
    Get a NetworkFunctionResource


    :param str network_function_name: The name of the network function
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['networkFunctionName'] = network_function_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:mobilepacketcore/v20230515preview:getNetworkFunction', __args__, opts=opts, typ=GetNetworkFunctionResult).value

    return AwaitableGetNetworkFunctionResult(
        capacity=pulumi.get(__ret__, 'capacity'),
        deployment_notes=pulumi.get(__ret__, 'deployment_notes'),
        id=pulumi.get(__ret__, 'id'),
        infrastructure_element_count=pulumi.get(__ret__, 'infrastructure_element_count'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_function_administrative_state=pulumi.get(__ret__, 'network_function_administrative_state'),
        network_function_operational_status=pulumi.get(__ret__, 'network_function_operational_status'),
        network_function_type=pulumi.get(__ret__, 'network_function_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        sku=pulumi.get(__ret__, 'sku'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        user_description=pulumi.get(__ret__, 'user_description'))


@_utilities.lift_output_func(get_network_function)
def get_network_function_output(network_function_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkFunctionResult]:
    """
    Get a NetworkFunctionResource


    :param str network_function_name: The name of the network function
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
