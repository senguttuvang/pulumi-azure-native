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
    'ManagedGrafanaPropertiesResponse',
    'ManagedIdentityResponse',
    'ResourceSkuResponse',
    'SystemDataResponse',
    'UserAssignedIdentityResponse',
]

@pulumi.output_type
class ManagedGrafanaPropertiesResponse(dict):
    """
    Properties specific to the grafana resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "grafanaVersion":
            suggest = "grafana_version"
        elif key == "autoGeneratedDomainNameLabelScope":
            suggest = "auto_generated_domain_name_label_scope"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "zoneRedundancy":
            suggest = "zone_redundancy"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ManagedGrafanaPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ManagedGrafanaPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ManagedGrafanaPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 endpoint: str,
                 grafana_version: str,
                 auto_generated_domain_name_label_scope: Optional[str] = None,
                 provisioning_state: Optional[str] = None,
                 zone_redundancy: Optional[str] = None):
        """
        Properties specific to the grafana resource.
        :param str endpoint: The endpoint of the Grafana instance.
        :param str grafana_version: The Grafana software version.
        :param str provisioning_state: Provisioning state of the resource.
        """
        pulumi.set(__self__, "endpoint", endpoint)
        pulumi.set(__self__, "grafana_version", grafana_version)
        if auto_generated_domain_name_label_scope is not None:
            pulumi.set(__self__, "auto_generated_domain_name_label_scope", auto_generated_domain_name_label_scope)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if zone_redundancy is not None:
            pulumi.set(__self__, "zone_redundancy", zone_redundancy)

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        The endpoint of the Grafana instance.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="grafanaVersion")
    def grafana_version(self) -> str:
        """
        The Grafana software version.
        """
        return pulumi.get(self, "grafana_version")

    @property
    @pulumi.getter(name="autoGeneratedDomainNameLabelScope")
    def auto_generated_domain_name_label_scope(self) -> Optional[str]:
        return pulumi.get(self, "auto_generated_domain_name_label_scope")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="zoneRedundancy")
    def zone_redundancy(self) -> Optional[str]:
        return pulumi.get(self, "zone_redundancy")


@pulumi.output_type
class ManagedIdentityResponse(dict):
    """
    The managed identity of a resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"
        elif key == "userAssignedIdentities":
            suggest = "user_assigned_identities"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ManagedIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ManagedIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ManagedIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None,
                 user_assigned_identities: Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']] = None):
        """
        The managed identity of a resource.
        :param str principal_id: The principal id of the system assigned identity.
        :param str tenant_id: The tenant id of the system assigned identity.
        :param str type: The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the resource.
        :param Mapping[str, 'UserAssignedIdentityResponse'] user_assigned_identities: Dictionary of user assigned identities.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal id of the system assigned identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant id of the system assigned identity.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']]:
        """
        Dictionary of user assigned identities.
        """
        return pulumi.get(self, "user_assigned_identities")


@pulumi.output_type
class ResourceSkuResponse(dict):
    def __init__(__self__, *,
                 name: str):
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")


@pulumi.output_type
class SystemDataResponse(dict):
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
        :param str created_by_type: The type of identity that created the resource.
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
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
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
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        return pulumi.get(self, "last_modified_by_type")


@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"
        elif key == "principalId":
            suggest = "principal_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserAssignedIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserAssignedIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserAssignedIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_id: str,
                 principal_id: str):
        """
        :param str client_id: The client id of user assigned identity.
        :param str principal_id: The principal id of user assigned identity.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "principal_id", principal_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        The client id of user assigned identity.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal id of user assigned identity.
        """
        return pulumi.get(self, "principal_id")


