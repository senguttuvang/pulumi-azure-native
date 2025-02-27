# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'PrivateEndpointPropertyArgs',
    'PrivateLinkServiceConnectionStatePropertyArgs',
    'ServerPropertiesForDefaultCreateArgs',
    'ServerPropertiesForGeoRestoreArgs',
    'ServerPropertiesForReplicaArgs',
    'ServerPropertiesForRestoreArgs',
    'SkuArgs',
    'StorageProfileArgs',
]

@pulumi.input_type
class PrivateEndpointPropertyArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] id: Resource id of the private endpoint.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource id of the private endpoint.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class PrivateLinkServiceConnectionStatePropertyArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 status: pulumi.Input[str]):
        """
        :param pulumi.Input[str] description: The private link service connection description.
        :param pulumi.Input[str] status: The private link service connection status.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The private link service connection description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[str]:
        """
        The private link service connection status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[str]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class ServerPropertiesForDefaultCreateArgs:
    def __init__(__self__, *,
                 administrator_login: pulumi.Input[str],
                 administrator_login_password: pulumi.Input[str],
                 create_mode: pulumi.Input[str],
                 ssl_enforcement: Optional[pulumi.Input['SslEnforcementEnum']] = None,
                 storage_profile: Optional[pulumi.Input['StorageProfileArgs']] = None,
                 version: Optional[pulumi.Input[Union[str, 'ServerVersion']]] = None):
        """
        The properties used to create a new server.
        :param pulumi.Input[str] administrator_login: The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        :param pulumi.Input[str] administrator_login_password: The password of the administrator login.
        :param pulumi.Input[str] create_mode: The mode to create a new server.
               Expected value is 'Default'.
        :param pulumi.Input['SslEnforcementEnum'] ssl_enforcement: Enable ssl enforcement or not when connect to server.
        :param pulumi.Input['StorageProfileArgs'] storage_profile: Storage profile of a server.
        :param pulumi.Input[Union[str, 'ServerVersion']] version: Server version.
        """
        pulumi.set(__self__, "administrator_login", administrator_login)
        pulumi.set(__self__, "administrator_login_password", administrator_login_password)
        pulumi.set(__self__, "create_mode", 'Default')
        if ssl_enforcement is not None:
            pulumi.set(__self__, "ssl_enforcement", ssl_enforcement)
        if storage_profile is not None:
            pulumi.set(__self__, "storage_profile", storage_profile)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> pulumi.Input[str]:
        """
        The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @administrator_login.setter
    def administrator_login(self, value: pulumi.Input[str]):
        pulumi.set(self, "administrator_login", value)

    @property
    @pulumi.getter(name="administratorLoginPassword")
    def administrator_login_password(self) -> pulumi.Input[str]:
        """
        The password of the administrator login.
        """
        return pulumi.get(self, "administrator_login_password")

    @administrator_login_password.setter
    def administrator_login_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "administrator_login_password", value)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Input[str]:
        """
        The mode to create a new server.
        Expected value is 'Default'.
        """
        return pulumi.get(self, "create_mode")

    @create_mode.setter
    def create_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "create_mode", value)

    @property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[pulumi.Input['SslEnforcementEnum']]:
        """
        Enable ssl enforcement or not when connect to server.
        """
        return pulumi.get(self, "ssl_enforcement")

    @ssl_enforcement.setter
    def ssl_enforcement(self, value: Optional[pulumi.Input['SslEnforcementEnum']]):
        pulumi.set(self, "ssl_enforcement", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input['StorageProfileArgs']]:
        """
        Storage profile of a server.
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input['StorageProfileArgs']]):
        pulumi.set(self, "storage_profile", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[Union[str, 'ServerVersion']]]:
        """
        Server version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[str, 'ServerVersion']]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class ServerPropertiesForGeoRestoreArgs:
    def __init__(__self__, *,
                 create_mode: pulumi.Input[str],
                 source_server_id: pulumi.Input[str],
                 ssl_enforcement: Optional[pulumi.Input['SslEnforcementEnum']] = None,
                 storage_profile: Optional[pulumi.Input['StorageProfileArgs']] = None,
                 version: Optional[pulumi.Input[Union[str, 'ServerVersion']]] = None):
        """
        The properties used to create a new server by restoring to a different region from a geo replicated backup.
        :param pulumi.Input[str] create_mode: The mode to create a new server.
               Expected value is 'GeoRestore'.
        :param pulumi.Input[str] source_server_id: The source server id to restore from.
        :param pulumi.Input['SslEnforcementEnum'] ssl_enforcement: Enable ssl enforcement or not when connect to server.
        :param pulumi.Input['StorageProfileArgs'] storage_profile: Storage profile of a server.
        :param pulumi.Input[Union[str, 'ServerVersion']] version: Server version.
        """
        pulumi.set(__self__, "create_mode", 'GeoRestore')
        pulumi.set(__self__, "source_server_id", source_server_id)
        if ssl_enforcement is not None:
            pulumi.set(__self__, "ssl_enforcement", ssl_enforcement)
        if storage_profile is not None:
            pulumi.set(__self__, "storage_profile", storage_profile)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Input[str]:
        """
        The mode to create a new server.
        Expected value is 'GeoRestore'.
        """
        return pulumi.get(self, "create_mode")

    @create_mode.setter
    def create_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "create_mode", value)

    @property
    @pulumi.getter(name="sourceServerId")
    def source_server_id(self) -> pulumi.Input[str]:
        """
        The source server id to restore from.
        """
        return pulumi.get(self, "source_server_id")

    @source_server_id.setter
    def source_server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_server_id", value)

    @property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[pulumi.Input['SslEnforcementEnum']]:
        """
        Enable ssl enforcement or not when connect to server.
        """
        return pulumi.get(self, "ssl_enforcement")

    @ssl_enforcement.setter
    def ssl_enforcement(self, value: Optional[pulumi.Input['SslEnforcementEnum']]):
        pulumi.set(self, "ssl_enforcement", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input['StorageProfileArgs']]:
        """
        Storage profile of a server.
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input['StorageProfileArgs']]):
        pulumi.set(self, "storage_profile", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[Union[str, 'ServerVersion']]]:
        """
        Server version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[str, 'ServerVersion']]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class ServerPropertiesForReplicaArgs:
    def __init__(__self__, *,
                 create_mode: pulumi.Input[str],
                 source_server_id: pulumi.Input[str],
                 ssl_enforcement: Optional[pulumi.Input['SslEnforcementEnum']] = None,
                 storage_profile: Optional[pulumi.Input['StorageProfileArgs']] = None,
                 version: Optional[pulumi.Input[Union[str, 'ServerVersion']]] = None):
        """
        The properties to create a new replica.
        :param pulumi.Input[str] create_mode: The mode to create a new server.
               Expected value is 'Replica'.
        :param pulumi.Input[str] source_server_id: The master server id to create replica from.
        :param pulumi.Input['SslEnforcementEnum'] ssl_enforcement: Enable ssl enforcement or not when connect to server.
        :param pulumi.Input['StorageProfileArgs'] storage_profile: Storage profile of a server.
        :param pulumi.Input[Union[str, 'ServerVersion']] version: Server version.
        """
        pulumi.set(__self__, "create_mode", 'Replica')
        pulumi.set(__self__, "source_server_id", source_server_id)
        if ssl_enforcement is not None:
            pulumi.set(__self__, "ssl_enforcement", ssl_enforcement)
        if storage_profile is not None:
            pulumi.set(__self__, "storage_profile", storage_profile)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Input[str]:
        """
        The mode to create a new server.
        Expected value is 'Replica'.
        """
        return pulumi.get(self, "create_mode")

    @create_mode.setter
    def create_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "create_mode", value)

    @property
    @pulumi.getter(name="sourceServerId")
    def source_server_id(self) -> pulumi.Input[str]:
        """
        The master server id to create replica from.
        """
        return pulumi.get(self, "source_server_id")

    @source_server_id.setter
    def source_server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_server_id", value)

    @property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[pulumi.Input['SslEnforcementEnum']]:
        """
        Enable ssl enforcement or not when connect to server.
        """
        return pulumi.get(self, "ssl_enforcement")

    @ssl_enforcement.setter
    def ssl_enforcement(self, value: Optional[pulumi.Input['SslEnforcementEnum']]):
        pulumi.set(self, "ssl_enforcement", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input['StorageProfileArgs']]:
        """
        Storage profile of a server.
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input['StorageProfileArgs']]):
        pulumi.set(self, "storage_profile", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[Union[str, 'ServerVersion']]]:
        """
        Server version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[str, 'ServerVersion']]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class ServerPropertiesForRestoreArgs:
    def __init__(__self__, *,
                 create_mode: pulumi.Input[str],
                 restore_point_in_time: pulumi.Input[str],
                 source_server_id: pulumi.Input[str],
                 ssl_enforcement: Optional[pulumi.Input['SslEnforcementEnum']] = None,
                 storage_profile: Optional[pulumi.Input['StorageProfileArgs']] = None,
                 version: Optional[pulumi.Input[Union[str, 'ServerVersion']]] = None):
        """
        The properties used to create a new server by restoring from a backup.
        :param pulumi.Input[str] create_mode: The mode to create a new server.
               Expected value is 'PointInTimeRestore'.
        :param pulumi.Input[str] restore_point_in_time: Restore point creation time (ISO8601 format), specifying the time to restore from.
        :param pulumi.Input[str] source_server_id: The source server id to restore from.
        :param pulumi.Input['SslEnforcementEnum'] ssl_enforcement: Enable ssl enforcement or not when connect to server.
        :param pulumi.Input['StorageProfileArgs'] storage_profile: Storage profile of a server.
        :param pulumi.Input[Union[str, 'ServerVersion']] version: Server version.
        """
        pulumi.set(__self__, "create_mode", 'PointInTimeRestore')
        pulumi.set(__self__, "restore_point_in_time", restore_point_in_time)
        pulumi.set(__self__, "source_server_id", source_server_id)
        if ssl_enforcement is not None:
            pulumi.set(__self__, "ssl_enforcement", ssl_enforcement)
        if storage_profile is not None:
            pulumi.set(__self__, "storage_profile", storage_profile)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Input[str]:
        """
        The mode to create a new server.
        Expected value is 'PointInTimeRestore'.
        """
        return pulumi.get(self, "create_mode")

    @create_mode.setter
    def create_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "create_mode", value)

    @property
    @pulumi.getter(name="restorePointInTime")
    def restore_point_in_time(self) -> pulumi.Input[str]:
        """
        Restore point creation time (ISO8601 format), specifying the time to restore from.
        """
        return pulumi.get(self, "restore_point_in_time")

    @restore_point_in_time.setter
    def restore_point_in_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "restore_point_in_time", value)

    @property
    @pulumi.getter(name="sourceServerId")
    def source_server_id(self) -> pulumi.Input[str]:
        """
        The source server id to restore from.
        """
        return pulumi.get(self, "source_server_id")

    @source_server_id.setter
    def source_server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_server_id", value)

    @property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[pulumi.Input['SslEnforcementEnum']]:
        """
        Enable ssl enforcement or not when connect to server.
        """
        return pulumi.get(self, "ssl_enforcement")

    @ssl_enforcement.setter
    def ssl_enforcement(self, value: Optional[pulumi.Input['SslEnforcementEnum']]):
        pulumi.set(self, "ssl_enforcement", value)

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional[pulumi.Input['StorageProfileArgs']]:
        """
        Storage profile of a server.
        """
        return pulumi.get(self, "storage_profile")

    @storage_profile.setter
    def storage_profile(self, value: Optional[pulumi.Input['StorageProfileArgs']]):
        pulumi.set(self, "storage_profile", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[Union[str, 'ServerVersion']]]:
        """
        Server version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[Union[str, 'ServerVersion']]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 capacity: Optional[pulumi.Input[int]] = None,
                 family: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input[Union[str, 'SkuTier']]] = None):
        """
        Billing information related properties of a server.
        :param pulumi.Input[str] name: The name of the sku, typically, tier + family + cores, e.g. B_Gen4_1, GP_Gen5_8.
        :param pulumi.Input[int] capacity: The scale up/out capacity, representing server's compute units.
        :param pulumi.Input[str] family: The family of hardware.
        :param pulumi.Input[str] size: The size code, to be interpreted by resource as appropriate.
        :param pulumi.Input[Union[str, 'SkuTier']] tier: The tier of the particular SKU, e.g. Basic.
        """
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the sku, typically, tier + family + cores, e.g. B_Gen4_1, GP_Gen5_8.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        The scale up/out capacity, representing server's compute units.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[str]]:
        """
        The family of hardware.
        """
        return pulumi.get(self, "family")

    @family.setter
    def family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "family", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        The size code, to be interpreted by resource as appropriate.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[str, 'SkuTier']]]:
        """
        The tier of the particular SKU, e.g. Basic.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[str, 'SkuTier']]]):
        pulumi.set(self, "tier", value)


@pulumi.input_type
class StorageProfileArgs:
    def __init__(__self__, *,
                 backup_retention_days: Optional[pulumi.Input[int]] = None,
                 geo_redundant_backup: Optional[pulumi.Input[Union[str, 'GeoRedundantBackup']]] = None,
                 storage_autogrow: Optional[pulumi.Input[Union[str, 'StorageAutogrow']]] = None,
                 storage_mb: Optional[pulumi.Input[int]] = None):
        """
        Storage Profile properties of a server
        :param pulumi.Input[int] backup_retention_days: Backup retention days for the server.
        :param pulumi.Input[Union[str, 'GeoRedundantBackup']] geo_redundant_backup: Enable Geo-redundant or not for server backup.
        :param pulumi.Input[Union[str, 'StorageAutogrow']] storage_autogrow: Enable Storage Auto Grow.
        :param pulumi.Input[int] storage_mb: Max storage allowed for a server.
        """
        if backup_retention_days is not None:
            pulumi.set(__self__, "backup_retention_days", backup_retention_days)
        if geo_redundant_backup is not None:
            pulumi.set(__self__, "geo_redundant_backup", geo_redundant_backup)
        if storage_autogrow is not None:
            pulumi.set(__self__, "storage_autogrow", storage_autogrow)
        if storage_mb is not None:
            pulumi.set(__self__, "storage_mb", storage_mb)

    @property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> Optional[pulumi.Input[int]]:
        """
        Backup retention days for the server.
        """
        return pulumi.get(self, "backup_retention_days")

    @backup_retention_days.setter
    def backup_retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "backup_retention_days", value)

    @property
    @pulumi.getter(name="geoRedundantBackup")
    def geo_redundant_backup(self) -> Optional[pulumi.Input[Union[str, 'GeoRedundantBackup']]]:
        """
        Enable Geo-redundant or not for server backup.
        """
        return pulumi.get(self, "geo_redundant_backup")

    @geo_redundant_backup.setter
    def geo_redundant_backup(self, value: Optional[pulumi.Input[Union[str, 'GeoRedundantBackup']]]):
        pulumi.set(self, "geo_redundant_backup", value)

    @property
    @pulumi.getter(name="storageAutogrow")
    def storage_autogrow(self) -> Optional[pulumi.Input[Union[str, 'StorageAutogrow']]]:
        """
        Enable Storage Auto Grow.
        """
        return pulumi.get(self, "storage_autogrow")

    @storage_autogrow.setter
    def storage_autogrow(self, value: Optional[pulumi.Input[Union[str, 'StorageAutogrow']]]):
        pulumi.set(self, "storage_autogrow", value)

    @property
    @pulumi.getter(name="storageMB")
    def storage_mb(self) -> Optional[pulumi.Input[int]]:
        """
        Max storage allowed for a server.
        """
        return pulumi.get(self, "storage_mb")

    @storage_mb.setter
    def storage_mb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage_mb", value)


