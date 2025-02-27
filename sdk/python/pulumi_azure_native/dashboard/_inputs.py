# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'AzureMonitorWorkspaceIntegrationArgs',
    'GrafanaIntegrationsArgs',
    'ManagedGrafanaPropertiesArgs',
    'ManagedServiceIdentityArgs',
    'PrivateLinkServiceConnectionStateArgs',
    'ResourceSkuArgs',
]

@pulumi.input_type
class AzureMonitorWorkspaceIntegrationArgs:
    def __init__(__self__, *,
                 azure_monitor_workspace_resource_id: Optional[pulumi.Input[str]] = None):
        """
        Integrations for Azure Monitor Workspace.
        :param pulumi.Input[str] azure_monitor_workspace_resource_id: The resource Id of the connected Azure Monitor Workspace.
        """
        if azure_monitor_workspace_resource_id is not None:
            pulumi.set(__self__, "azure_monitor_workspace_resource_id", azure_monitor_workspace_resource_id)

    @property
    @pulumi.getter(name="azureMonitorWorkspaceResourceId")
    def azure_monitor_workspace_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource Id of the connected Azure Monitor Workspace.
        """
        return pulumi.get(self, "azure_monitor_workspace_resource_id")

    @azure_monitor_workspace_resource_id.setter
    def azure_monitor_workspace_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_monitor_workspace_resource_id", value)


@pulumi.input_type
class GrafanaIntegrationsArgs:
    def __init__(__self__, *,
                 azure_monitor_workspace_integrations: Optional[pulumi.Input[Sequence[pulumi.Input['AzureMonitorWorkspaceIntegrationArgs']]]] = None):
        """
        GrafanaIntegrations is a bundled observability experience (e.g. pre-configured data source, tailored Grafana dashboards, alerting defaults) for common monitoring scenarios.
        """
        if azure_monitor_workspace_integrations is not None:
            pulumi.set(__self__, "azure_monitor_workspace_integrations", azure_monitor_workspace_integrations)

    @property
    @pulumi.getter(name="azureMonitorWorkspaceIntegrations")
    def azure_monitor_workspace_integrations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AzureMonitorWorkspaceIntegrationArgs']]]]:
        return pulumi.get(self, "azure_monitor_workspace_integrations")

    @azure_monitor_workspace_integrations.setter
    def azure_monitor_workspace_integrations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AzureMonitorWorkspaceIntegrationArgs']]]]):
        pulumi.set(self, "azure_monitor_workspace_integrations", value)


@pulumi.input_type
class ManagedGrafanaPropertiesArgs:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[Union[str, 'ApiKey']]] = None,
                 auto_generated_domain_name_label_scope: Optional[pulumi.Input[Union[str, 'AutoGeneratedDomainNameLabelScope']]] = None,
                 deterministic_outbound_ip: Optional[pulumi.Input[Union[str, 'DeterministicOutboundIP']]] = None,
                 grafana_integrations: Optional[pulumi.Input['GrafanaIntegrationsArgs']] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 zone_redundancy: Optional[pulumi.Input[Union[str, 'ZoneRedundancy']]] = None):
        """
        Properties specific to the grafana resource.
        :param pulumi.Input[Union[str, 'ApiKey']] api_key: The api key setting of the Grafana instance.
        :param pulumi.Input[Union[str, 'AutoGeneratedDomainNameLabelScope']] auto_generated_domain_name_label_scope: Scope for dns deterministic name hash calculation.
        :param pulumi.Input[Union[str, 'DeterministicOutboundIP']] deterministic_outbound_ip: Whether a Grafana instance uses deterministic outbound IPs.
        :param pulumi.Input['GrafanaIntegrationsArgs'] grafana_integrations: GrafanaIntegrations is a bundled observability experience (e.g. pre-configured data source, tailored Grafana dashboards, alerting defaults) for common monitoring scenarios.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: Indicate the state for enable or disable traffic over the public interface.
        :param pulumi.Input[Union[str, 'ZoneRedundancy']] zone_redundancy: The zone redundancy setting of the Grafana instance.
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if auto_generated_domain_name_label_scope is not None:
            pulumi.set(__self__, "auto_generated_domain_name_label_scope", auto_generated_domain_name_label_scope)
        if deterministic_outbound_ip is not None:
            pulumi.set(__self__, "deterministic_outbound_ip", deterministic_outbound_ip)
        if grafana_integrations is not None:
            pulumi.set(__self__, "grafana_integrations", grafana_integrations)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if zone_redundancy is not None:
            pulumi.set(__self__, "zone_redundancy", zone_redundancy)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[Union[str, 'ApiKey']]]:
        """
        The api key setting of the Grafana instance.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[Union[str, 'ApiKey']]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="autoGeneratedDomainNameLabelScope")
    def auto_generated_domain_name_label_scope(self) -> Optional[pulumi.Input[Union[str, 'AutoGeneratedDomainNameLabelScope']]]:
        """
        Scope for dns deterministic name hash calculation.
        """
        return pulumi.get(self, "auto_generated_domain_name_label_scope")

    @auto_generated_domain_name_label_scope.setter
    def auto_generated_domain_name_label_scope(self, value: Optional[pulumi.Input[Union[str, 'AutoGeneratedDomainNameLabelScope']]]):
        pulumi.set(self, "auto_generated_domain_name_label_scope", value)

    @property
    @pulumi.getter(name="deterministicOutboundIP")
    def deterministic_outbound_ip(self) -> Optional[pulumi.Input[Union[str, 'DeterministicOutboundIP']]]:
        """
        Whether a Grafana instance uses deterministic outbound IPs.
        """
        return pulumi.get(self, "deterministic_outbound_ip")

    @deterministic_outbound_ip.setter
    def deterministic_outbound_ip(self, value: Optional[pulumi.Input[Union[str, 'DeterministicOutboundIP']]]):
        pulumi.set(self, "deterministic_outbound_ip", value)

    @property
    @pulumi.getter(name="grafanaIntegrations")
    def grafana_integrations(self) -> Optional[pulumi.Input['GrafanaIntegrationsArgs']]:
        """
        GrafanaIntegrations is a bundled observability experience (e.g. pre-configured data source, tailored Grafana dashboards, alerting defaults) for common monitoring scenarios.
        """
        return pulumi.get(self, "grafana_integrations")

    @grafana_integrations.setter
    def grafana_integrations(self, value: Optional[pulumi.Input['GrafanaIntegrationsArgs']]):
        pulumi.set(self, "grafana_integrations", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        Indicate the state for enable or disable traffic over the public interface.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter(name="zoneRedundancy")
    def zone_redundancy(self) -> Optional[pulumi.Input[Union[str, 'ZoneRedundancy']]]:
        """
        The zone redundancy setting of the Grafana instance.
        """
        return pulumi.get(self, "zone_redundancy")

    @zone_redundancy.setter
    def zone_redundancy(self, value: Optional[pulumi.Input[Union[str, 'ZoneRedundancy']]]):
        pulumi.set(self, "zone_redundancy", value)


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[Union[str, 'ManagedServiceIdentityType']],
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Managed service identity (system assigned and/or user assigned identities)
        :param pulumi.Input[Union[str, 'ManagedServiceIdentityType']] type: Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'ManagedServiceIdentityType']]:
        """
        Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'ManagedServiceIdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[str] actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param pulumi.Input[str] description: The reason for approval/rejection of the connection.
        :param pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']] status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[str]]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actions_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class ResourceSkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str]):
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


