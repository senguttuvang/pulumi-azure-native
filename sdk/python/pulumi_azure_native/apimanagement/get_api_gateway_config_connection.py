# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetApiGatewayConfigConnectionResult',
    'AwaitableGetApiGatewayConfigConnectionResult',
    'get_api_gateway_config_connection',
    'get_api_gateway_config_connection_output',
]

@pulumi.output_type
class GetApiGatewayConfigConnectionResult:
    """
    A single API Management gateway resource in List or Get response.
    """
    def __init__(__self__, default_hostname=None, etag=None, hostnames=None, id=None, name=None, provisioning_state=None, source_id=None, type=None):
        if default_hostname and not isinstance(default_hostname, str):
            raise TypeError("Expected argument 'default_hostname' to be a str")
        pulumi.set(__self__, "default_hostname", default_hostname)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if hostnames and not isinstance(hostnames, list):
            raise TypeError("Expected argument 'hostnames' to be a list")
        pulumi.set(__self__, "hostnames", hostnames)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if source_id and not isinstance(source_id, str):
            raise TypeError("Expected argument 'source_id' to be a str")
        pulumi.set(__self__, "source_id", source_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="defaultHostname")
    def default_hostname(self) -> str:
        """
        The default hostname of the data-plane gateway.
        """
        return pulumi.get(self, "default_hostname")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def hostnames(self) -> Optional[Sequence[str]]:
        """
        The hostnames of the data-plane gateway to which requests can be sent.
        """
        return pulumi.get(self, "hostnames")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

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
        The current provisioning state of the API Management gateway config connection 
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[str]:
        """
        The link to the API Management service workspace.
        """
        return pulumi.get(self, "source_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetApiGatewayConfigConnectionResult(GetApiGatewayConfigConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiGatewayConfigConnectionResult(
            default_hostname=self.default_hostname,
            etag=self.etag,
            hostnames=self.hostnames,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            source_id=self.source_id,
            type=self.type)


def get_api_gateway_config_connection(config_connection_name: Optional[str] = None,
                                      gateway_name: Optional[str] = None,
                                      resource_group_name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiGatewayConfigConnectionResult:
    """
    Gets an API Management gateway config connection resource description.
    Azure REST API version: 2023-09-01-preview.


    :param str config_connection_name: The name of the API Management gateway config connection.
    :param str gateway_name: The name of the API Management gateway.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['configConnectionName'] = config_connection_name
    __args__['gatewayName'] = gateway_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement:getApiGatewayConfigConnection', __args__, opts=opts, typ=GetApiGatewayConfigConnectionResult).value

    return AwaitableGetApiGatewayConfigConnectionResult(
        default_hostname=pulumi.get(__ret__, 'default_hostname'),
        etag=pulumi.get(__ret__, 'etag'),
        hostnames=pulumi.get(__ret__, 'hostnames'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        source_id=pulumi.get(__ret__, 'source_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_api_gateway_config_connection)
def get_api_gateway_config_connection_output(config_connection_name: Optional[pulumi.Input[str]] = None,
                                             gateway_name: Optional[pulumi.Input[str]] = None,
                                             resource_group_name: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiGatewayConfigConnectionResult]:
    """
    Gets an API Management gateway config connection resource description.
    Azure REST API version: 2023-09-01-preview.


    :param str config_connection_name: The name of the API Management gateway config connection.
    :param str gateway_name: The name of the API Management gateway.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
