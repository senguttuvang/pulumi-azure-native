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
from ._enums import *

__all__ = [
    'DatabasePropertiesResponseGeoReplication',
    'EnterpriseSkuResponse',
    'LinkedDatabaseResponse',
    'ModuleResponse',
    'PersistenceResponse',
    'PrivateEndpointConnectionResponse',
    'PrivateEndpointResponse',
    'PrivateLinkServiceConnectionStateResponse',
]

@pulumi.output_type
class DatabasePropertiesResponseGeoReplication(dict):
    """
    Optional set of properties to configure geo replication for this database.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "groupNickname":
            suggest = "group_nickname"
        elif key == "linkedDatabases":
            suggest = "linked_databases"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DatabasePropertiesResponseGeoReplication. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DatabasePropertiesResponseGeoReplication.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DatabasePropertiesResponseGeoReplication.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 group_nickname: Optional[str] = None,
                 linked_databases: Optional[Sequence['outputs.LinkedDatabaseResponse']] = None):
        """
        Optional set of properties to configure geo replication for this database.
        :param str group_nickname: Name for the group of linked database resources
        :param Sequence['LinkedDatabaseResponse'] linked_databases: List of database resources to link with this database
        """
        if group_nickname is not None:
            pulumi.set(__self__, "group_nickname", group_nickname)
        if linked_databases is not None:
            pulumi.set(__self__, "linked_databases", linked_databases)

    @property
    @pulumi.getter(name="groupNickname")
    def group_nickname(self) -> Optional[str]:
        """
        Name for the group of linked database resources
        """
        return pulumi.get(self, "group_nickname")

    @property
    @pulumi.getter(name="linkedDatabases")
    def linked_databases(self) -> Optional[Sequence['outputs.LinkedDatabaseResponse']]:
        """
        List of database resources to link with this database
        """
        return pulumi.get(self, "linked_databases")


@pulumi.output_type
class EnterpriseSkuResponse(dict):
    """
    SKU parameters supplied to the create RedisEnterprise operation.
    """
    def __init__(__self__, *,
                 name: str,
                 capacity: Optional[int] = None):
        """
        SKU parameters supplied to the create RedisEnterprise operation.
        :param str name: The type of RedisEnterprise cluster to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)
        :param int capacity: The size of the RedisEnterprise cluster. Defaults to 2 or 3 depending on SKU. Valid values are (2, 4, 6, ...) for Enterprise SKUs and (3, 9, 15, ...) for Flash SKUs.
        """
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The type of RedisEnterprise cluster to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def capacity(self) -> Optional[int]:
        """
        The size of the RedisEnterprise cluster. Defaults to 2 or 3 depending on SKU. Valid values are (2, 4, 6, ...) for Enterprise SKUs and (3, 9, 15, ...) for Flash SKUs.
        """
        return pulumi.get(self, "capacity")


@pulumi.output_type
class LinkedDatabaseResponse(dict):
    """
    Specifies details of a linked database resource.
    """
    def __init__(__self__, *,
                 state: str,
                 id: Optional[str] = None):
        """
        Specifies details of a linked database resource.
        :param str state: State of the link between the database resources.
        :param str id: Resource ID of a database resource to link with this database.
        """
        pulumi.set(__self__, "state", state)
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        State of the link between the database resources.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID of a database resource to link with this database.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class ModuleResponse(dict):
    """
    Specifies configuration of a redis module
    """
    def __init__(__self__, *,
                 name: str,
                 version: str,
                 args: Optional[str] = None):
        """
        Specifies configuration of a redis module
        :param str name: The name of the module, e.g. 'RedisBloom', 'RediSearch', 'RedisTimeSeries'
        :param str version: The version of the module, e.g. '1.0'.
        :param str args: Configuration options for the module, e.g. 'ERROR_RATE 0.01 INITIAL_SIZE 400'.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "version", version)
        if args is not None:
            pulumi.set(__self__, "args", args)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the module, e.g. 'RedisBloom', 'RediSearch', 'RedisTimeSeries'
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The version of the module, e.g. '1.0'.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter
    def args(self) -> Optional[str]:
        """
        Configuration options for the module, e.g. 'ERROR_RATE 0.01 INITIAL_SIZE 400'.
        """
        return pulumi.get(self, "args")


@pulumi.output_type
class PersistenceResponse(dict):
    """
    Persistence-related configuration for the RedisEnterprise database
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "aofEnabled":
            suggest = "aof_enabled"
        elif key == "aofFrequency":
            suggest = "aof_frequency"
        elif key == "rdbEnabled":
            suggest = "rdb_enabled"
        elif key == "rdbFrequency":
            suggest = "rdb_frequency"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PersistenceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PersistenceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PersistenceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 aof_enabled: Optional[bool] = None,
                 aof_frequency: Optional[str] = None,
                 rdb_enabled: Optional[bool] = None,
                 rdb_frequency: Optional[str] = None):
        """
        Persistence-related configuration for the RedisEnterprise database
        :param bool aof_enabled: Sets whether AOF is enabled.
        :param str aof_frequency: Sets the frequency at which data is written to disk.
        :param bool rdb_enabled: Sets whether RDB is enabled.
        :param str rdb_frequency: Sets the frequency at which a snapshot of the database is created.
        """
        if aof_enabled is not None:
            pulumi.set(__self__, "aof_enabled", aof_enabled)
        if aof_frequency is not None:
            pulumi.set(__self__, "aof_frequency", aof_frequency)
        if rdb_enabled is not None:
            pulumi.set(__self__, "rdb_enabled", rdb_enabled)
        if rdb_frequency is not None:
            pulumi.set(__self__, "rdb_frequency", rdb_frequency)

    @property
    @pulumi.getter(name="aofEnabled")
    def aof_enabled(self) -> Optional[bool]:
        """
        Sets whether AOF is enabled.
        """
        return pulumi.get(self, "aof_enabled")

    @property
    @pulumi.getter(name="aofFrequency")
    def aof_frequency(self) -> Optional[str]:
        """
        Sets the frequency at which data is written to disk.
        """
        return pulumi.get(self, "aof_frequency")

    @property
    @pulumi.getter(name="rdbEnabled")
    def rdb_enabled(self) -> Optional[bool]:
        """
        Sets whether RDB is enabled.
        """
        return pulumi.get(self, "rdb_enabled")

    @property
    @pulumi.getter(name="rdbFrequency")
    def rdb_frequency(self) -> Optional[str]:
        """
        Sets the frequency at which a snapshot of the database is created.
        """
        return pulumi.get(self, "rdb_frequency")


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    """
    The Private Endpoint Connection resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "privateLinkServiceConnectionState":
            suggest = "private_link_service_connection_state"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "privateEndpoint":
            suggest = "private_endpoint"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateEndpointConnectionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 name: str,
                 private_link_service_connection_state: 'outputs.PrivateLinkServiceConnectionStateResponse',
                 provisioning_state: str,
                 type: str,
                 private_endpoint: Optional['outputs.PrivateEndpointResponse'] = None):
        """
        The Private Endpoint Connection resource.
        :param str id: Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        :param str name: The name of the resource
        :param 'PrivateLinkServiceConnectionStateResponse' private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param str provisioning_state: The provisioning state of the private endpoint connection resource.
        :param str type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        :param 'PrivateEndpointResponse' private_endpoint: The resource of private end point.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "type", type)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)

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
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> 'outputs.PrivateLinkServiceConnectionStateResponse':
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the private endpoint connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional['outputs.PrivateEndpointResponse']:
        """
        The resource of private end point.
        """
        return pulumi.get(self, "private_endpoint")


@pulumi.output_type
class PrivateEndpointResponse(dict):
    """
    The Private Endpoint resource.
    """
    def __init__(__self__, *,
                 id: str):
        """
        The Private Endpoint resource.
        :param str id: The ARM identifier for Private Endpoint
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ARM identifier for Private Endpoint
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    """
    A collection of information about the state of the connection between service consumer and provider.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionsRequired":
            suggest = "actions_required"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateLinkServiceConnectionStateResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 actions_required: Optional[str] = None,
                 description: Optional[str] = None,
                 status: Optional[str] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param str actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param str description: The reason for approval/rejection of the connection.
        :param str status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[str]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")


