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
    'MigrateProjectPropertiesResponse',
    'PrivateEndpointConnectionPropertiesResponse',
    'PrivateEndpointConnectionResponse',
    'PrivateLinkServiceConnectionStateResponse',
    'ProjectSummaryResponse',
    'ResourceIdResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class MigrateProjectPropertiesResponse(dict):
    """
    Properties of a migrate project.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "lastSummaryRefreshedTime":
            suggest = "last_summary_refreshed_time"
        elif key == "privateEndpointConnections":
            suggest = "private_endpoint_connections"
        elif key == "refreshSummaryState":
            suggest = "refresh_summary_state"
        elif key == "registeredTools":
            suggest = "registered_tools"
        elif key == "publicNetworkAccess":
            suggest = "public_network_access"
        elif key == "serviceEndpoint":
            suggest = "service_endpoint"
        elif key == "utilityStorageAccountId":
            suggest = "utility_storage_account_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MigrateProjectPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MigrateProjectPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MigrateProjectPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 last_summary_refreshed_time: str,
                 private_endpoint_connections: Sequence['outputs.PrivateEndpointConnectionResponse'],
                 refresh_summary_state: str,
                 registered_tools: Sequence[str],
                 summary: Mapping[str, 'outputs.ProjectSummaryResponse'],
                 public_network_access: Optional[str] = None,
                 service_endpoint: Optional[str] = None,
                 utility_storage_account_id: Optional[str] = None):
        """
        Properties of a migrate project.
        :param str last_summary_refreshed_time: Last summary refresh time.
        :param Sequence['PrivateEndpointConnectionResponse'] private_endpoint_connections: Gets the private endpoint connections.
        :param str refresh_summary_state: Refresh summary state.
        :param Sequence[str] registered_tools: Register tools inside project.
        :param Mapping[str, 'ProjectSummaryResponse'] summary: Project summary.
        :param str public_network_access: Gets or sets the state of public network access.
        :param str service_endpoint: Service endpoint.
        :param str utility_storage_account_id: Utility storage account id.
        """
        pulumi.set(__self__, "last_summary_refreshed_time", last_summary_refreshed_time)
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        pulumi.set(__self__, "refresh_summary_state", refresh_summary_state)
        pulumi.set(__self__, "registered_tools", registered_tools)
        pulumi.set(__self__, "summary", summary)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if service_endpoint is not None:
            pulumi.set(__self__, "service_endpoint", service_endpoint)
        if utility_storage_account_id is not None:
            pulumi.set(__self__, "utility_storage_account_id", utility_storage_account_id)

    @property
    @pulumi.getter(name="lastSummaryRefreshedTime")
    def last_summary_refreshed_time(self) -> str:
        """
        Last summary refresh time.
        """
        return pulumi.get(self, "last_summary_refreshed_time")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        Gets the private endpoint connections.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="refreshSummaryState")
    def refresh_summary_state(self) -> str:
        """
        Refresh summary state.
        """
        return pulumi.get(self, "refresh_summary_state")

    @property
    @pulumi.getter(name="registeredTools")
    def registered_tools(self) -> Sequence[str]:
        """
        Register tools inside project.
        """
        return pulumi.get(self, "registered_tools")

    @property
    @pulumi.getter
    def summary(self) -> Mapping[str, 'outputs.ProjectSummaryResponse']:
        """
        Project summary.
        """
        return pulumi.get(self, "summary")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Gets or sets the state of public network access.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> Optional[str]:
        """
        Service endpoint.
        """
        return pulumi.get(self, "service_endpoint")

    @property
    @pulumi.getter(name="utilityStorageAccountId")
    def utility_storage_account_id(self) -> Optional[str]:
        """
        Utility storage account id.
        """
        return pulumi.get(self, "utility_storage_account_id")


@pulumi.output_type
class PrivateEndpointConnectionPropertiesResponse(dict):
    """
    Properties of a private endpoint connection.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "privateEndpoint":
            suggest = "private_endpoint"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "privateLinkServiceConnectionState":
            suggest = "private_link_service_connection_state"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateEndpointConnectionPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateEndpointConnectionPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateEndpointConnectionPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 private_endpoint: 'outputs.ResourceIdResponse',
                 provisioning_state: str,
                 private_link_service_connection_state: Optional['outputs.PrivateLinkServiceConnectionStateResponse'] = None):
        """
        Properties of a private endpoint connection.
        :param str provisioning_state: Provisioning state.
        :param 'PrivateLinkServiceConnectionStateResponse' private_link_service_connection_state: Gets the properties of the object.
        """
        pulumi.set(__self__, "private_endpoint", private_endpoint)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if private_link_service_connection_state is not None:
            pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> 'outputs.ResourceIdResponse':
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional['outputs.PrivateLinkServiceConnectionStateResponse']:
        """
        Gets the properties of the object.
        """
        return pulumi.get(self, "private_link_service_connection_state")


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    """
    REST model used to encapsulate the user visible state of a PrivateEndpoint.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "eTag":
            suggest = "e_tag"
        elif key == "systemData":
            suggest = "system_data"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateEndpointConnectionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 e_tag: str,
                 id: str,
                 name: str,
                 properties: 'outputs.PrivateEndpointConnectionPropertiesResponse',
                 system_data: 'outputs.SystemDataResponse',
                 type: str):
        """
        REST model used to encapsulate the user visible state of a PrivateEndpoint.
        :param str e_tag: Gets the tag for optimistic concurrency control.
        :param str id: Relative URL to get this Sites.
        :param str name: Gets the name of the resource.
        :param 'PrivateEndpointConnectionPropertiesResponse' properties: Gets the properties of the object.
        :param 'SystemDataResponse' system_data: Metadata pertaining to creation and last modification of the resource.
        :param str type: Gets the resource type.
        """
        pulumi.set(__self__, "e_tag", e_tag)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "system_data", system_data)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> str:
        """
        Gets the tag for optimistic concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Relative URL to get this Sites.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.PrivateEndpointConnectionPropertiesResponse':
        """
        Gets the properties of the object.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    """
    Private endpoint connection state.
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
        Private endpoint connection state.
        :param str actions_required: Action required.
        :param str description: Description of the object.
        :param str status: Private link connection state.
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
        Action required.
        """
        return pulumi.get(self, "actions_required")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the object.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Private link connection state.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class ProjectSummaryResponse(dict):
    """
    Project summary.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "instanceType":
            suggest = "instance_type"
        elif key == "extendedSummary":
            suggest = "extended_summary"
        elif key == "lastSummaryRefreshedTime":
            suggest = "last_summary_refreshed_time"
        elif key == "refreshSummaryState":
            suggest = "refresh_summary_state"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectSummaryResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectSummaryResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectSummaryResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 instance_type: str,
                 extended_summary: Optional[Mapping[str, str]] = None,
                 last_summary_refreshed_time: Optional[str] = None,
                 refresh_summary_state: Optional[str] = None):
        """
        Project summary.
        :param str instance_type: Instance type.
        :param Mapping[str, str] extended_summary: Extended summary.
        :param str last_summary_refreshed_time: Last summary refresh time.
        :param str refresh_summary_state: Refresh summary state.
        """
        pulumi.set(__self__, "instance_type", instance_type)
        if extended_summary is not None:
            pulumi.set(__self__, "extended_summary", extended_summary)
        if last_summary_refreshed_time is not None:
            pulumi.set(__self__, "last_summary_refreshed_time", last_summary_refreshed_time)
        if refresh_summary_state is not None:
            pulumi.set(__self__, "refresh_summary_state", refresh_summary_state)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> str:
        """
        Instance type.
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="extendedSummary")
    def extended_summary(self) -> Optional[Mapping[str, str]]:
        """
        Extended summary.
        """
        return pulumi.get(self, "extended_summary")

    @property
    @pulumi.getter(name="lastSummaryRefreshedTime")
    def last_summary_refreshed_time(self) -> Optional[str]:
        """
        Last summary refresh time.
        """
        return pulumi.get(self, "last_summary_refreshed_time")

    @property
    @pulumi.getter(name="refreshSummaryState")
    def refresh_summary_state(self) -> Optional[str]:
        """
        Refresh summary state.
        """
        return pulumi.get(self, "refresh_summary_state")


@pulumi.output_type
class ResourceIdResponse(dict):
    def __init__(__self__, *,
                 id: str):
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The type of identity that last modified the resource.
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


