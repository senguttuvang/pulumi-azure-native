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
    'ResourceIdentityResponse',
    'SkuResponse',
    'StorageProfileResponse',
]

@pulumi.output_type
class ResourceIdentityResponse(dict):
    """
    Azure Active Directory identity configuration for a resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResourceIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResourceIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResourceIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
        Azure Active Directory identity configuration for a resource.
        :param str principal_id: The Azure Active Directory principal id.
        :param str tenant_id: The Azure Active Directory tenant id.
        :param str type: The identity type. Set this to 'SystemAssigned' in order to automatically create and assign an Azure Active Directory principal for the resource.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The Azure Active Directory principal id.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The Azure Active Directory tenant id.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The identity type. Set this to 'SystemAssigned' in order to automatically create and assign an Azure Active Directory principal for the resource.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class SkuResponse(dict):
    """
    Billing information related properties of a server.
    """
    def __init__(__self__, *,
                 name: str,
                 capacity: Optional[int] = None,
                 family: Optional[str] = None,
                 size: Optional[str] = None,
                 tier: Optional[str] = None):
        """
        Billing information related properties of a server.
        :param str name: The name of the sku, typically, tier + family + cores, e.g. B_Gen4_1, GP_Gen5_8.
        :param int capacity: The scale up/out capacity, representing server's compute units.
        :param str family: The family of hardware.
        :param str size: The size code, to be interpreted by resource as appropriate.
        :param str tier: The tier of the particular SKU, e.g. Basic.
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
    def name(self) -> str:
        """
        The name of the sku, typically, tier + family + cores, e.g. B_Gen4_1, GP_Gen5_8.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def capacity(self) -> Optional[int]:
        """
        The scale up/out capacity, representing server's compute units.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def family(self) -> Optional[str]:
        """
        The family of hardware.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def size(self) -> Optional[str]:
        """
        The size code, to be interpreted by resource as appropriate.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        The tier of the particular SKU, e.g. Basic.
        """
        return pulumi.get(self, "tier")


@pulumi.output_type
class StorageProfileResponse(dict):
    """
    Storage Profile properties of a server
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "backupRetentionDays":
            suggest = "backup_retention_days"
        elif key == "geoRedundantBackup":
            suggest = "geo_redundant_backup"
        elif key == "storageAutogrow":
            suggest = "storage_autogrow"
        elif key == "storageMB":
            suggest = "storage_mb"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StorageProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StorageProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StorageProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 backup_retention_days: Optional[int] = None,
                 geo_redundant_backup: Optional[str] = None,
                 storage_autogrow: Optional[str] = None,
                 storage_mb: Optional[int] = None):
        """
        Storage Profile properties of a server
        :param int backup_retention_days: Backup retention days for the server.
        :param str geo_redundant_backup: Enable Geo-redundant or not for server backup.
        :param str storage_autogrow: Enable Storage Auto Grow.
        :param int storage_mb: Max storage allowed for a server.
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
    def backup_retention_days(self) -> Optional[int]:
        """
        Backup retention days for the server.
        """
        return pulumi.get(self, "backup_retention_days")

    @property
    @pulumi.getter(name="geoRedundantBackup")
    def geo_redundant_backup(self) -> Optional[str]:
        """
        Enable Geo-redundant or not for server backup.
        """
        return pulumi.get(self, "geo_redundant_backup")

    @property
    @pulumi.getter(name="storageAutogrow")
    def storage_autogrow(self) -> Optional[str]:
        """
        Enable Storage Auto Grow.
        """
        return pulumi.get(self, "storage_autogrow")

    @property
    @pulumi.getter(name="storageMB")
    def storage_mb(self) -> Optional[int]:
        """
        Max storage allowed for a server.
        """
        return pulumi.get(self, "storage_mb")


