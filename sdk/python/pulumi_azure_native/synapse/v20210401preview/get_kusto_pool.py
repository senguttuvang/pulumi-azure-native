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
    'GetKustoPoolResult',
    'AwaitableGetKustoPoolResult',
    'get_kusto_pool',
    'get_kusto_pool_output',
]

@pulumi.output_type
class GetKustoPoolResult:
    """
    Class representing a Kusto kusto pool.
    """
    def __init__(__self__, data_ingestion_uri=None, engine_type=None, etag=None, id=None, location=None, name=None, provisioning_state=None, sku=None, state=None, state_reason=None, system_data=None, tags=None, type=None, uri=None, workspace_uid=None):
        if data_ingestion_uri and not isinstance(data_ingestion_uri, str):
            raise TypeError("Expected argument 'data_ingestion_uri' to be a str")
        pulumi.set(__self__, "data_ingestion_uri", data_ingestion_uri)
        if engine_type and not isinstance(engine_type, str):
            raise TypeError("Expected argument 'engine_type' to be a str")
        pulumi.set(__self__, "engine_type", engine_type)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if state_reason and not isinstance(state_reason, str):
            raise TypeError("Expected argument 'state_reason' to be a str")
        pulumi.set(__self__, "state_reason", state_reason)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if uri and not isinstance(uri, str):
            raise TypeError("Expected argument 'uri' to be a str")
        pulumi.set(__self__, "uri", uri)
        if workspace_uid and not isinstance(workspace_uid, str):
            raise TypeError("Expected argument 'workspace_uid' to be a str")
        pulumi.set(__self__, "workspace_uid", workspace_uid)

    @property
    @pulumi.getter(name="dataIngestionUri")
    def data_ingestion_uri(self) -> str:
        """
        The Kusto Pool data ingestion URI.
        """
        return pulumi.get(self, "data_ingestion_uri")

    @property
    @pulumi.getter(name="engineType")
    def engine_type(self) -> Optional[str]:
        """
        The engine type
        """
        return pulumi.get(self, "engine_type")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

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
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.AzureSkuResponse':
        """
        The SKU of the kusto pool.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> str:
        """
        The reason for the Kusto Pool's current state.
        """
        return pulumi.get(self, "state_reason")

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
    @pulumi.getter
    def uri(self) -> str:
        """
        The Kusto Pool URI.
        """
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter(name="workspaceUid")
    def workspace_uid(self) -> Optional[str]:
        """
        The workspace unique identifier.
        """
        return pulumi.get(self, "workspace_uid")


class AwaitableGetKustoPoolResult(GetKustoPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKustoPoolResult(
            data_ingestion_uri=self.data_ingestion_uri,
            engine_type=self.engine_type,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            state=self.state,
            state_reason=self.state_reason,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            uri=self.uri,
            workspace_uid=self.workspace_uid)


def get_kusto_pool(kusto_pool_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   workspace_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKustoPoolResult:
    """
    Gets a Kusto pool.


    :param str kusto_pool_name: The name of the Kusto pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace
    """
    __args__ = dict()
    __args__['kustoPoolName'] = kusto_pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:synapse/v20210401preview:getKustoPool', __args__, opts=opts, typ=GetKustoPoolResult).value

    return AwaitableGetKustoPoolResult(
        data_ingestion_uri=pulumi.get(__ret__, 'data_ingestion_uri'),
        engine_type=pulumi.get(__ret__, 'engine_type'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        sku=pulumi.get(__ret__, 'sku'),
        state=pulumi.get(__ret__, 'state'),
        state_reason=pulumi.get(__ret__, 'state_reason'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        uri=pulumi.get(__ret__, 'uri'),
        workspace_uid=pulumi.get(__ret__, 'workspace_uid'))


@_utilities.lift_output_func(get_kusto_pool)
def get_kusto_pool_output(kusto_pool_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          workspace_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKustoPoolResult]:
    """
    Gets a Kusto pool.


    :param str kusto_pool_name: The name of the Kusto pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace
    """
    ...
