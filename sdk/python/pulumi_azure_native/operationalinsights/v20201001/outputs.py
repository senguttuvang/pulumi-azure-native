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
    'PrivateLinkScopedResourceResponse',
    'WorkspaceCappingResponse',
    'WorkspaceFeaturesResponse',
    'WorkspaceSkuResponse',
]

@pulumi.output_type
class PrivateLinkScopedResourceResponse(dict):
    """
    The private link scope resource reference.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "resourceId":
            suggest = "resource_id"
        elif key == "scopeId":
            suggest = "scope_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateLinkScopedResourceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateLinkScopedResourceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateLinkScopedResourceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 resource_id: Optional[str] = None,
                 scope_id: Optional[str] = None):
        """
        The private link scope resource reference.
        :param str resource_id: The full resource Id of the private link scope resource.
        :param str scope_id: The private link scope unique Identifier.
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if scope_id is not None:
            pulumi.set(__self__, "scope_id", scope_id)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        The full resource Id of the private link scope resource.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="scopeId")
    def scope_id(self) -> Optional[str]:
        """
        The private link scope unique Identifier.
        """
        return pulumi.get(self, "scope_id")


@pulumi.output_type
class WorkspaceCappingResponse(dict):
    """
    The daily volume cap for ingestion.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dataIngestionStatus":
            suggest = "data_ingestion_status"
        elif key == "quotaNextResetTime":
            suggest = "quota_next_reset_time"
        elif key == "dailyQuotaGb":
            suggest = "daily_quota_gb"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkspaceCappingResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkspaceCappingResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkspaceCappingResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 data_ingestion_status: str,
                 quota_next_reset_time: str,
                 daily_quota_gb: Optional[float] = None):
        """
        The daily volume cap for ingestion.
        :param str data_ingestion_status: The status of data ingestion for this workspace.
        :param str quota_next_reset_time: The time when the quota will be rest.
        :param float daily_quota_gb: The workspace daily quota for ingestion.
        """
        pulumi.set(__self__, "data_ingestion_status", data_ingestion_status)
        pulumi.set(__self__, "quota_next_reset_time", quota_next_reset_time)
        if daily_quota_gb is not None:
            pulumi.set(__self__, "daily_quota_gb", daily_quota_gb)

    @property
    @pulumi.getter(name="dataIngestionStatus")
    def data_ingestion_status(self) -> str:
        """
        The status of data ingestion for this workspace.
        """
        return pulumi.get(self, "data_ingestion_status")

    @property
    @pulumi.getter(name="quotaNextResetTime")
    def quota_next_reset_time(self) -> str:
        """
        The time when the quota will be rest.
        """
        return pulumi.get(self, "quota_next_reset_time")

    @property
    @pulumi.getter(name="dailyQuotaGb")
    def daily_quota_gb(self) -> Optional[float]:
        """
        The workspace daily quota for ingestion.
        """
        return pulumi.get(self, "daily_quota_gb")


@pulumi.output_type
class WorkspaceFeaturesResponse(dict):
    """
    Workspace features.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clusterResourceId":
            suggest = "cluster_resource_id"
        elif key == "disableLocalAuth":
            suggest = "disable_local_auth"
        elif key == "enableDataExport":
            suggest = "enable_data_export"
        elif key == "enableLogAccessUsingOnlyResourcePermissions":
            suggest = "enable_log_access_using_only_resource_permissions"
        elif key == "immediatePurgeDataOn30Days":
            suggest = "immediate_purge_data_on30_days"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkspaceFeaturesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkspaceFeaturesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkspaceFeaturesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cluster_resource_id: Optional[str] = None,
                 disable_local_auth: Optional[bool] = None,
                 enable_data_export: Optional[bool] = None,
                 enable_log_access_using_only_resource_permissions: Optional[bool] = None,
                 immediate_purge_data_on30_days: Optional[bool] = None):
        """
        Workspace features.
        :param str cluster_resource_id: Dedicated LA cluster resourceId that is linked to the workspaces.
        :param bool disable_local_auth: Disable Non-AAD based Auth.
        :param bool enable_data_export: Flag that indicate if data should be exported.
        :param bool enable_log_access_using_only_resource_permissions: Flag that indicate which permission to use - resource or workspace or both.
        :param bool immediate_purge_data_on30_days: Flag that describes if we want to remove the data after 30 days.
        """
        if cluster_resource_id is not None:
            pulumi.set(__self__, "cluster_resource_id", cluster_resource_id)
        if disable_local_auth is not None:
            pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if enable_data_export is not None:
            pulumi.set(__self__, "enable_data_export", enable_data_export)
        if enable_log_access_using_only_resource_permissions is not None:
            pulumi.set(__self__, "enable_log_access_using_only_resource_permissions", enable_log_access_using_only_resource_permissions)
        if immediate_purge_data_on30_days is not None:
            pulumi.set(__self__, "immediate_purge_data_on30_days", immediate_purge_data_on30_days)

    @property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> Optional[str]:
        """
        Dedicated LA cluster resourceId that is linked to the workspaces.
        """
        return pulumi.get(self, "cluster_resource_id")

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[bool]:
        """
        Disable Non-AAD based Auth.
        """
        return pulumi.get(self, "disable_local_auth")

    @property
    @pulumi.getter(name="enableDataExport")
    def enable_data_export(self) -> Optional[bool]:
        """
        Flag that indicate if data should be exported.
        """
        return pulumi.get(self, "enable_data_export")

    @property
    @pulumi.getter(name="enableLogAccessUsingOnlyResourcePermissions")
    def enable_log_access_using_only_resource_permissions(self) -> Optional[bool]:
        """
        Flag that indicate which permission to use - resource or workspace or both.
        """
        return pulumi.get(self, "enable_log_access_using_only_resource_permissions")

    @property
    @pulumi.getter(name="immediatePurgeDataOn30Days")
    def immediate_purge_data_on30_days(self) -> Optional[bool]:
        """
        Flag that describes if we want to remove the data after 30 days.
        """
        return pulumi.get(self, "immediate_purge_data_on30_days")


@pulumi.output_type
class WorkspaceSkuResponse(dict):
    """
    The SKU (tier) of a workspace.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "lastSkuUpdate":
            suggest = "last_sku_update"
        elif key == "capacityReservationLevel":
            suggest = "capacity_reservation_level"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkspaceSkuResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkspaceSkuResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkspaceSkuResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 last_sku_update: str,
                 name: str,
                 capacity_reservation_level: Optional[int] = None):
        """
        The SKU (tier) of a workspace.
        :param str last_sku_update: The last time when the sku was updated.
        :param str name: The name of the SKU.
        :param int capacity_reservation_level: The capacity reservation level for this workspace, when CapacityReservation sku is selected.
        """
        pulumi.set(__self__, "last_sku_update", last_sku_update)
        pulumi.set(__self__, "name", name)
        if capacity_reservation_level is not None:
            pulumi.set(__self__, "capacity_reservation_level", capacity_reservation_level)

    @property
    @pulumi.getter(name="lastSkuUpdate")
    def last_sku_update(self) -> str:
        """
        The last time when the sku was updated.
        """
        return pulumi.get(self, "last_sku_update")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the SKU.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="capacityReservationLevel")
    def capacity_reservation_level(self) -> Optional[int]:
        """
        The capacity reservation level for this workspace, when CapacityReservation sku is selected.
        """
        return pulumi.get(self, "capacity_reservation_level")


