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
    'AssignmentLockSettingsArgs',
    'KeyVaultReferenceArgs',
    'ManagedServiceIdentityArgs',
    'ParameterDefinitionArgs',
    'ParameterValueArgs',
    'ResourceGroupDefinitionArgs',
    'ResourceGroupValueArgs',
    'SecretValueReferenceArgs',
    'UserAssignedIdentityArgs',
]

@pulumi.input_type
class AssignmentLockSettingsArgs:
    def __init__(__self__, *,
                 excluded_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 excluded_principals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mode: Optional[pulumi.Input[Union[str, 'AssignmentLockMode']]] = None):
        """
        Defines how resources deployed by a blueprint assignment are locked.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] excluded_actions: List of management operations that are excluded from blueprint locks. Up to 200 actions are permitted. If the lock mode is set to 'AllResourcesReadOnly', then the following actions are automatically appended to 'excludedActions': '*/read', 'Microsoft.Network/virtualNetworks/subnets/join/action' and 'Microsoft.Authorization/locks/delete'. If the lock mode is set to 'AllResourcesDoNotDelete', then the following actions are automatically appended to 'excludedActions': 'Microsoft.Authorization/locks/delete'. Duplicate actions will get removed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] excluded_principals: List of AAD principals excluded from blueprint locks. Up to 5 principals are permitted.
        :param pulumi.Input[Union[str, 'AssignmentLockMode']] mode: Lock mode.
        """
        if excluded_actions is not None:
            pulumi.set(__self__, "excluded_actions", excluded_actions)
        if excluded_principals is not None:
            pulumi.set(__self__, "excluded_principals", excluded_principals)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)

    @property
    @pulumi.getter(name="excludedActions")
    def excluded_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of management operations that are excluded from blueprint locks. Up to 200 actions are permitted. If the lock mode is set to 'AllResourcesReadOnly', then the following actions are automatically appended to 'excludedActions': '*/read', 'Microsoft.Network/virtualNetworks/subnets/join/action' and 'Microsoft.Authorization/locks/delete'. If the lock mode is set to 'AllResourcesDoNotDelete', then the following actions are automatically appended to 'excludedActions': 'Microsoft.Authorization/locks/delete'. Duplicate actions will get removed.
        """
        return pulumi.get(self, "excluded_actions")

    @excluded_actions.setter
    def excluded_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "excluded_actions", value)

    @property
    @pulumi.getter(name="excludedPrincipals")
    def excluded_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of AAD principals excluded from blueprint locks. Up to 5 principals are permitted.
        """
        return pulumi.get(self, "excluded_principals")

    @excluded_principals.setter
    def excluded_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "excluded_principals", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[str, 'AssignmentLockMode']]]:
        """
        Lock mode.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[str, 'AssignmentLockMode']]]):
        pulumi.set(self, "mode", value)


@pulumi.input_type
class KeyVaultReferenceArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str]):
        """
        Specifies the link to a Key Vault.
        :param pulumi.Input[str] id: Azure resource ID of the Key Vault.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Azure resource ID of the Key Vault.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[Union[str, 'ManagedServiceIdentityType']],
                 principal_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 user_assigned_identities: Optional[pulumi.Input[Mapping[str, pulumi.Input['UserAssignedIdentityArgs']]]] = None):
        """
        Managed identity generic object.
        :param pulumi.Input[Union[str, 'ManagedServiceIdentityType']] type: Type of the managed identity.
        :param pulumi.Input[str] principal_id: Azure Active Directory principal ID associated with this Identity.
        :param pulumi.Input[str] tenant_id: ID of the Azure Active Directory.
        :param pulumi.Input[Mapping[str, pulumi.Input['UserAssignedIdentityArgs']]] user_assigned_identities: The list of user-assigned managed identities associated with the resource. Key is the Azure resource Id of the managed identity.
        """
        pulumi.set(__self__, "type", type)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'ManagedServiceIdentityType']]:
        """
        Type of the managed identity.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'ManagedServiceIdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        Azure Active Directory principal ID associated with this Identity.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the Azure Active Directory.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['UserAssignedIdentityArgs']]]]:
        """
        The list of user-assigned managed identities associated with the resource. Key is the Azure resource Id of the managed identity.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['UserAssignedIdentityArgs']]]]):
        pulumi.set(self, "user_assigned_identities", value)


@pulumi.input_type
class ParameterDefinitionArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[Union[str, 'TemplateParameterType']],
                 allowed_values: Optional[pulumi.Input[Sequence[Any]]] = None,
                 default_value: Optional[Any] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 strong_type: Optional[pulumi.Input[str]] = None):
        """
        Represent a parameter with constrains and metadata.
        :param pulumi.Input[Union[str, 'TemplateParameterType']] type: Allowed data types for Resource Manager template parameters.
        :param pulumi.Input[Sequence[Any]] allowed_values: Array of allowed values for this parameter.
        :param Any default_value: Default Value for this parameter.
        :param pulumi.Input[str] description: Description of this parameter/resourceGroup.
        :param pulumi.Input[str] display_name: DisplayName of this parameter/resourceGroup.
        :param pulumi.Input[str] strong_type: StrongType for UI to render rich experience during blueprint assignment. Supported strong types are resourceType, principalId and location.
        """
        pulumi.set(__self__, "type", type)
        if allowed_values is not None:
            pulumi.set(__self__, "allowed_values", allowed_values)
        if default_value is not None:
            pulumi.set(__self__, "default_value", default_value)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if strong_type is not None:
            pulumi.set(__self__, "strong_type", strong_type)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'TemplateParameterType']]:
        """
        Allowed data types for Resource Manager template parameters.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'TemplateParameterType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> Optional[pulumi.Input[Sequence[Any]]]:
        """
        Array of allowed values for this parameter.
        """
        return pulumi.get(self, "allowed_values")

    @allowed_values.setter
    def allowed_values(self, value: Optional[pulumi.Input[Sequence[Any]]]):
        pulumi.set(self, "allowed_values", value)

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[Any]:
        """
        Default Value for this parameter.
        """
        return pulumi.get(self, "default_value")

    @default_value.setter
    def default_value(self, value: Optional[Any]):
        pulumi.set(self, "default_value", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of this parameter/resourceGroup.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        DisplayName of this parameter/resourceGroup.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="strongType")
    def strong_type(self) -> Optional[pulumi.Input[str]]:
        """
        StrongType for UI to render rich experience during blueprint assignment. Supported strong types are resourceType, principalId and location.
        """
        return pulumi.get(self, "strong_type")

    @strong_type.setter
    def strong_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "strong_type", value)


@pulumi.input_type
class ParameterValueArgs:
    def __init__(__self__, *,
                 reference: Optional[pulumi.Input['SecretValueReferenceArgs']] = None,
                 value: Optional[Any] = None):
        """
        Value for the specified parameter. Can be either 'value' or 'reference' but not both.
        :param pulumi.Input['SecretValueReferenceArgs'] reference: Parameter value as reference type.
        :param Any value: Parameter value. Any valid JSON value is allowed including objects, arrays, strings, numbers and booleans.
        """
        if reference is not None:
            pulumi.set(__self__, "reference", reference)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def reference(self) -> Optional[pulumi.Input['SecretValueReferenceArgs']]:
        """
        Parameter value as reference type.
        """
        return pulumi.get(self, "reference")

    @reference.setter
    def reference(self, value: Optional[pulumi.Input['SecretValueReferenceArgs']]):
        pulumi.set(self, "reference", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Any]:
        """
        Parameter value. Any valid JSON value is allowed including objects, arrays, strings, numbers and booleans.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[Any]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ResourceGroupDefinitionArgs:
    def __init__(__self__, *,
                 depends_on: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 strong_type: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Represents an Azure resource group in a blueprint definition.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] depends_on: Artifacts which need to be deployed before this resource group.
        :param pulumi.Input[str] description: Description of this parameter/resourceGroup.
        :param pulumi.Input[str] display_name: DisplayName of this parameter/resourceGroup.
        :param pulumi.Input[str] location: Location of this resourceGroup. Leave empty if the resource group location will be specified during the blueprint assignment.
        :param pulumi.Input[str] name: Name of this resourceGroup. Leave empty if the resource group name will be specified during the blueprint assignment.
        :param pulumi.Input[str] strong_type: StrongType for UI to render rich experience during blueprint assignment. Supported strong types are resourceType, principalId and location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags to be assigned to this resource group.
        """
        if depends_on is not None:
            pulumi.set(__self__, "depends_on", depends_on)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if strong_type is not None:
            pulumi.set(__self__, "strong_type", strong_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="dependsOn")
    def depends_on(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Artifacts which need to be deployed before this resource group.
        """
        return pulumi.get(self, "depends_on")

    @depends_on.setter
    def depends_on(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "depends_on", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of this parameter/resourceGroup.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        DisplayName of this parameter/resourceGroup.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of this resourceGroup. Leave empty if the resource group location will be specified during the blueprint assignment.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of this resourceGroup. Leave empty if the resource group name will be specified during the blueprint assignment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="strongType")
    def strong_type(self) -> Optional[pulumi.Input[str]]:
        """
        StrongType for UI to render rich experience during blueprint assignment. Supported strong types are resourceType, principalId and location.
        """
        return pulumi.get(self, "strong_type")

    @strong_type.setter
    def strong_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "strong_type", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags to be assigned to this resource group.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class ResourceGroupValueArgs:
    def __init__(__self__, *,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Represents an Azure resource group.
        :param pulumi.Input[str] location: Location of the resource group.
        :param pulumi.Input[str] name: Name of the resource group.
        """
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the resource group.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource group.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class SecretValueReferenceArgs:
    def __init__(__self__, *,
                 key_vault: pulumi.Input['KeyVaultReferenceArgs'],
                 secret_name: pulumi.Input[str],
                 secret_version: Optional[pulumi.Input[str]] = None):
        """
        Reference to a Key Vault secret.
        :param pulumi.Input['KeyVaultReferenceArgs'] key_vault: Specifies the reference to a given Azure Key Vault.
        :param pulumi.Input[str] secret_name: Name of the secret.
        :param pulumi.Input[str] secret_version: The version of the secret to use. If left blank, the latest version of the secret is used.
        """
        pulumi.set(__self__, "key_vault", key_vault)
        pulumi.set(__self__, "secret_name", secret_name)
        if secret_version is not None:
            pulumi.set(__self__, "secret_version", secret_version)

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> pulumi.Input['KeyVaultReferenceArgs']:
        """
        Specifies the reference to a given Azure Key Vault.
        """
        return pulumi.get(self, "key_vault")

    @key_vault.setter
    def key_vault(self, value: pulumi.Input['KeyVaultReferenceArgs']):
        pulumi.set(self, "key_vault", value)

    @property
    @pulumi.getter(name="secretName")
    def secret_name(self) -> pulumi.Input[str]:
        """
        Name of the secret.
        """
        return pulumi.get(self, "secret_name")

    @secret_name.setter
    def secret_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret_name", value)

    @property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the secret to use. If left blank, the latest version of the secret is used.
        """
        return pulumi.get(self, "secret_version")

    @secret_version.setter
    def secret_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_version", value)


@pulumi.input_type
class UserAssignedIdentityArgs:
    def __init__(__self__, *,
                 client_id: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None):
        """
        User-assigned managed identity.
        :param pulumi.Input[str] client_id: Client App Id associated with this identity.
        :param pulumi.Input[str] principal_id: Azure Active Directory principal ID associated with this Identity.
        """
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        Client App Id associated with this identity.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        Azure Active Directory principal ID associated with this Identity.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)


