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
    'GetADLSGen2StorageAccountDataSetMappingResult',
    'AwaitableGetADLSGen2StorageAccountDataSetMappingResult',
    'get_adls_gen2_storage_account_data_set_mapping',
    'get_adls_gen2_storage_account_data_set_mapping_output',
]

@pulumi.output_type
class GetADLSGen2StorageAccountDataSetMappingResult:
    """
    ADLSGen2 storage account data set mapping.
    """
    def __init__(__self__, container_name=None, data_set_id=None, data_set_mapping_status=None, folder=None, id=None, kind=None, location=None, mount_path=None, name=None, provisioning_state=None, storage_account_resource_id=None, system_data=None, type=None):
        if container_name and not isinstance(container_name, str):
            raise TypeError("Expected argument 'container_name' to be a str")
        pulumi.set(__self__, "container_name", container_name)
        if data_set_id and not isinstance(data_set_id, str):
            raise TypeError("Expected argument 'data_set_id' to be a str")
        pulumi.set(__self__, "data_set_id", data_set_id)
        if data_set_mapping_status and not isinstance(data_set_mapping_status, str):
            raise TypeError("Expected argument 'data_set_mapping_status' to be a str")
        pulumi.set(__self__, "data_set_mapping_status", data_set_mapping_status)
        if folder and not isinstance(folder, str):
            raise TypeError("Expected argument 'folder' to be a str")
        pulumi.set(__self__, "folder", folder)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mount_path and not isinstance(mount_path, str):
            raise TypeError("Expected argument 'mount_path' to be a str")
        pulumi.set(__self__, "mount_path", mount_path)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if storage_account_resource_id and not isinstance(storage_account_resource_id, str):
            raise TypeError("Expected argument 'storage_account_resource_id' to be a str")
        pulumi.set(__self__, "storage_account_resource_id", storage_account_resource_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> str:
        """
        Gets or sets the container name.
        """
        return pulumi.get(self, "container_name")

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> str:
        """
        The id of the source data set.
        """
        return pulumi.get(self, "data_set_id")

    @property
    @pulumi.getter(name="dataSetMappingStatus")
    def data_set_mapping_status(self) -> str:
        """
        Gets the status of the data set mapping.
        """
        return pulumi.get(self, "data_set_mapping_status")

    @property
    @pulumi.getter
    def folder(self) -> str:
        """
        Gets or sets the path to folder within the container.
        """
        return pulumi.get(self, "folder")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id of the azure resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of data set mapping.
        Expected value is 'AdlsGen2StorageAccount'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the sink storage account.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> Optional[str]:
        """
        Gets or sets the mount path
        """
        return pulumi.get(self, "mount_path")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the data set mapping.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> str:
        """
        Resource id of the sink storage account
        """
        return pulumi.get(self, "storage_account_resource_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        System Data of the Azure resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")


class AwaitableGetADLSGen2StorageAccountDataSetMappingResult(GetADLSGen2StorageAccountDataSetMappingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetADLSGen2StorageAccountDataSetMappingResult(
            container_name=self.container_name,
            data_set_id=self.data_set_id,
            data_set_mapping_status=self.data_set_mapping_status,
            folder=self.folder,
            id=self.id,
            kind=self.kind,
            location=self.location,
            mount_path=self.mount_path,
            name=self.name,
            provisioning_state=self.provisioning_state,
            storage_account_resource_id=self.storage_account_resource_id,
            system_data=self.system_data,
            type=self.type)


def get_adls_gen2_storage_account_data_set_mapping(account_name: Optional[str] = None,
                                                   data_set_mapping_name: Optional[str] = None,
                                                   resource_group_name: Optional[str] = None,
                                                   share_subscription_name: Optional[str] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetADLSGen2StorageAccountDataSetMappingResult:
    """
    Get a DataSetMapping in a shareSubscription


    :param str account_name: The name of the share account.
    :param str data_set_mapping_name: The name of the dataSetMapping.
    :param str resource_group_name: The resource group name.
    :param str share_subscription_name: The name of the shareSubscription.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['dataSetMappingName'] = data_set_mapping_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareSubscriptionName'] = share_subscription_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datashare/v20201001preview:getADLSGen2StorageAccountDataSetMapping', __args__, opts=opts, typ=GetADLSGen2StorageAccountDataSetMappingResult).value

    return AwaitableGetADLSGen2StorageAccountDataSetMappingResult(
        container_name=pulumi.get(__ret__, 'container_name'),
        data_set_id=pulumi.get(__ret__, 'data_set_id'),
        data_set_mapping_status=pulumi.get(__ret__, 'data_set_mapping_status'),
        folder=pulumi.get(__ret__, 'folder'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        mount_path=pulumi.get(__ret__, 'mount_path'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        storage_account_resource_id=pulumi.get(__ret__, 'storage_account_resource_id'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_adls_gen2_storage_account_data_set_mapping)
def get_adls_gen2_storage_account_data_set_mapping_output(account_name: Optional[pulumi.Input[str]] = None,
                                                          data_set_mapping_name: Optional[pulumi.Input[str]] = None,
                                                          resource_group_name: Optional[pulumi.Input[str]] = None,
                                                          share_subscription_name: Optional[pulumi.Input[str]] = None,
                                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetADLSGen2StorageAccountDataSetMappingResult]:
    """
    Get a DataSetMapping in a shareSubscription


    :param str account_name: The name of the share account.
    :param str data_set_mapping_name: The name of the dataSetMapping.
    :param str resource_group_name: The resource group name.
    :param str share_subscription_name: The name of the shareSubscription.
    """
    ...
