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
    'CorsRulesArgs',
    'CorsRuleArgs',
    'CreatorPropertiesArgs',
    'CustomerManagedKeyEncryptionKeyEncryptionKeyIdentityArgs',
    'CustomerManagedKeyEncryptionArgs',
    'EncryptionArgs',
    'LinkedResourceArgs',
    'ManagedServiceIdentityArgs',
    'MapsAccountPropertiesArgs',
    'SkuArgs',
]

@pulumi.input_type
class CorsRulesArgs:
    def __init__(__self__, *,
                 cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input['CorsRuleArgs']]]] = None):
        """
        Sets the CORS rules. You can include up to five CorsRule elements in the request. 
        :param pulumi.Input[Sequence[pulumi.Input['CorsRuleArgs']]] cors_rules: The list of CORS rules. You can include up to five CorsRule elements in the request. 
        """
        if cors_rules is not None:
            pulumi.set(__self__, "cors_rules", cors_rules)

    @property
    @pulumi.getter(name="corsRules")
    def cors_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CorsRuleArgs']]]]:
        """
        The list of CORS rules. You can include up to five CorsRule elements in the request. 
        """
        return pulumi.get(self, "cors_rules")

    @cors_rules.setter
    def cors_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CorsRuleArgs']]]]):
        pulumi.set(self, "cors_rules", value)


@pulumi.input_type
class CorsRuleArgs:
    def __init__(__self__, *,
                 allowed_origins: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        Specifies a CORS rule for the Map Account.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_origins: Required if CorsRule element is present. A list of origin domains that will be allowed via CORS, or "*" to allow all domains
        """
        pulumi.set(__self__, "allowed_origins", allowed_origins)

    @property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Required if CorsRule element is present. A list of origin domains that will be allowed via CORS, or "*" to allow all domains
        """
        return pulumi.get(self, "allowed_origins")

    @allowed_origins.setter
    def allowed_origins(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "allowed_origins", value)


@pulumi.input_type
class CreatorPropertiesArgs:
    def __init__(__self__, *,
                 storage_units: pulumi.Input[int]):
        """
        Creator resource properties
        :param pulumi.Input[int] storage_units: The storage units to be allocated. Integer values from 1 to 100, inclusive.
        """
        pulumi.set(__self__, "storage_units", storage_units)

    @property
    @pulumi.getter(name="storageUnits")
    def storage_units(self) -> pulumi.Input[int]:
        """
        The storage units to be allocated. Integer values from 1 to 100, inclusive.
        """
        return pulumi.get(self, "storage_units")

    @storage_units.setter
    def storage_units(self, value: pulumi.Input[int]):
        pulumi.set(self, "storage_units", value)


@pulumi.input_type
class CustomerManagedKeyEncryptionKeyEncryptionKeyIdentityArgs:
    def __init__(__self__, *,
                 delegated_identity_client_id: Optional[pulumi.Input[str]] = None,
                 identity_type: Optional[pulumi.Input[Union[str, 'IdentityType']]] = None,
                 user_assigned_identity_resource_id: Optional[pulumi.Input[str]] = None):
        """
        All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        :param pulumi.Input[str] delegated_identity_client_id: delegated identity to use for accessing key encryption key Url. Ex: /subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId. Mutually exclusive with identityType systemAssignedIdentity and userAssignedIdentity - internal use only.
        :param pulumi.Input[Union[str, 'IdentityType']] identity_type: Values can be systemAssignedIdentity or userAssignedIdentity
        :param pulumi.Input[str] user_assigned_identity_resource_id: user assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId. Mutually exclusive with identityType systemAssignedIdentity and delegatedResourceIdentity.
        """
        if delegated_identity_client_id is not None:
            pulumi.set(__self__, "delegated_identity_client_id", delegated_identity_client_id)
        if identity_type is not None:
            pulumi.set(__self__, "identity_type", identity_type)
        if user_assigned_identity_resource_id is not None:
            pulumi.set(__self__, "user_assigned_identity_resource_id", user_assigned_identity_resource_id)

    @property
    @pulumi.getter(name="delegatedIdentityClientId")
    def delegated_identity_client_id(self) -> Optional[pulumi.Input[str]]:
        """
        delegated identity to use for accessing key encryption key Url. Ex: /subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId. Mutually exclusive with identityType systemAssignedIdentity and userAssignedIdentity - internal use only.
        """
        return pulumi.get(self, "delegated_identity_client_id")

    @delegated_identity_client_id.setter
    def delegated_identity_client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delegated_identity_client_id", value)

    @property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[Union[str, 'IdentityType']]]:
        """
        Values can be systemAssignedIdentity or userAssignedIdentity
        """
        return pulumi.get(self, "identity_type")

    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[Union[str, 'IdentityType']]]):
        pulumi.set(self, "identity_type", value)

    @property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        user assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId. Mutually exclusive with identityType systemAssignedIdentity and delegatedResourceIdentity.
        """
        return pulumi.get(self, "user_assigned_identity_resource_id")

    @user_assigned_identity_resource_id.setter
    def user_assigned_identity_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_assigned_identity_resource_id", value)


@pulumi.input_type
class CustomerManagedKeyEncryptionArgs:
    def __init__(__self__, *,
                 key_encryption_key_identity: Optional[pulumi.Input['CustomerManagedKeyEncryptionKeyEncryptionKeyIdentityArgs']] = None,
                 key_encryption_key_url: Optional[pulumi.Input[str]] = None):
        """
        All Customer-managed key encryption properties for the resource.
        :param pulumi.Input['CustomerManagedKeyEncryptionKeyEncryptionKeyIdentityArgs'] key_encryption_key_identity: All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        :param pulumi.Input[str] key_encryption_key_url: key encryption key Url, versioned or non-versioned. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek.
        """
        if key_encryption_key_identity is not None:
            pulumi.set(__self__, "key_encryption_key_identity", key_encryption_key_identity)
        if key_encryption_key_url is not None:
            pulumi.set(__self__, "key_encryption_key_url", key_encryption_key_url)

    @property
    @pulumi.getter(name="keyEncryptionKeyIdentity")
    def key_encryption_key_identity(self) -> Optional[pulumi.Input['CustomerManagedKeyEncryptionKeyEncryptionKeyIdentityArgs']]:
        """
        All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        """
        return pulumi.get(self, "key_encryption_key_identity")

    @key_encryption_key_identity.setter
    def key_encryption_key_identity(self, value: Optional[pulumi.Input['CustomerManagedKeyEncryptionKeyEncryptionKeyIdentityArgs']]):
        pulumi.set(self, "key_encryption_key_identity", value)

    @property
    @pulumi.getter(name="keyEncryptionKeyUrl")
    def key_encryption_key_url(self) -> Optional[pulumi.Input[str]]:
        """
        key encryption key Url, versioned or non-versioned. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek.
        """
        return pulumi.get(self, "key_encryption_key_url")

    @key_encryption_key_url.setter
    def key_encryption_key_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_encryption_key_url", value)


@pulumi.input_type
class EncryptionArgs:
    def __init__(__self__, *,
                 customer_managed_key_encryption: Optional[pulumi.Input['CustomerManagedKeyEncryptionArgs']] = None,
                 infrastructure_encryption: Optional[pulumi.Input[Union[str, 'InfrastructureEncryption']]] = None):
        """
        (Optional) Discouraged to include in resource definition. Only needed where it is possible to disable platform (AKA infrastructure) encryption. Azure SQL TDE is an example of this. Values are enabled and disabled.
        :param pulumi.Input['CustomerManagedKeyEncryptionArgs'] customer_managed_key_encryption: All Customer-managed key encryption properties for the resource.
        :param pulumi.Input[Union[str, 'InfrastructureEncryption']] infrastructure_encryption: Values are enabled and disabled.
        """
        if customer_managed_key_encryption is not None:
            pulumi.set(__self__, "customer_managed_key_encryption", customer_managed_key_encryption)
        if infrastructure_encryption is not None:
            pulumi.set(__self__, "infrastructure_encryption", infrastructure_encryption)

    @property
    @pulumi.getter(name="customerManagedKeyEncryption")
    def customer_managed_key_encryption(self) -> Optional[pulumi.Input['CustomerManagedKeyEncryptionArgs']]:
        """
        All Customer-managed key encryption properties for the resource.
        """
        return pulumi.get(self, "customer_managed_key_encryption")

    @customer_managed_key_encryption.setter
    def customer_managed_key_encryption(self, value: Optional[pulumi.Input['CustomerManagedKeyEncryptionArgs']]):
        pulumi.set(self, "customer_managed_key_encryption", value)

    @property
    @pulumi.getter(name="infrastructureEncryption")
    def infrastructure_encryption(self) -> Optional[pulumi.Input[Union[str, 'InfrastructureEncryption']]]:
        """
        Values are enabled and disabled.
        """
        return pulumi.get(self, "infrastructure_encryption")

    @infrastructure_encryption.setter
    def infrastructure_encryption(self, value: Optional[pulumi.Input[Union[str, 'InfrastructureEncryption']]]):
        pulumi.set(self, "infrastructure_encryption", value)


@pulumi.input_type
class LinkedResourceArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 unique_name: pulumi.Input[str]):
        """
        Linked resource is reference to a resource deployed in an Azure subscription, add the linked resource `uniqueName` value as an optional parameter for operations on Azure Maps Geospatial REST APIs.
        :param pulumi.Input[str] id: ARM resource id in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/accounts/{storageName}'.
        :param pulumi.Input[str] unique_name: A provided name which uniquely identifies the linked resource.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "unique_name", unique_name)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        ARM resource id in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/accounts/{storageName}'.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="uniqueName")
    def unique_name(self) -> pulumi.Input[str]:
        """
        A provided name which uniquely identifies the linked resource.
        """
        return pulumi.get(self, "unique_name")

    @unique_name.setter
    def unique_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "unique_name", value)


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
class MapsAccountPropertiesArgs:
    def __init__(__self__, *,
                 cors: Optional[pulumi.Input['CorsRulesArgs']] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 encryption: Optional[pulumi.Input['EncryptionArgs']] = None,
                 linked_resources: Optional[pulumi.Input[Sequence[pulumi.Input['LinkedResourceArgs']]]] = None):
        """
        Additional Map account properties
        :param pulumi.Input['CorsRulesArgs'] cors: Specifies CORS rules for the Blob service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Blob service.
        :param pulumi.Input[bool] disable_local_auth: Allows toggle functionality on Azure Policy to disable Azure Maps local authentication support. This will disable Shared Keys and Shared Access Signature Token authentication from any usage.
        :param pulumi.Input['EncryptionArgs'] encryption: (Optional) Discouraged to include in resource definition. Only needed where it is possible to disable platform (AKA infrastructure) encryption. Azure SQL TDE is an example of this. Values are enabled and disabled.
        :param pulumi.Input[Sequence[pulumi.Input['LinkedResourceArgs']]] linked_resources: The array of associated resources to the Map account. Linked resource in the array cannot individually update, you must update all linked resources in the array together. These resources may be used on operations on the Azure Maps REST API. Access is controlled by the Map Account Managed Identity(s) permissions to those resource(s).
        """
        if cors is not None:
            pulumi.set(__self__, "cors", cors)
        if disable_local_auth is None:
            disable_local_auth = False
        if disable_local_auth is not None:
            pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if linked_resources is not None:
            pulumi.set(__self__, "linked_resources", linked_resources)

    @property
    @pulumi.getter
    def cors(self) -> Optional[pulumi.Input['CorsRulesArgs']]:
        """
        Specifies CORS rules for the Blob service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Blob service.
        """
        return pulumi.get(self, "cors")

    @cors.setter
    def cors(self, value: Optional[pulumi.Input['CorsRulesArgs']]):
        pulumi.set(self, "cors", value)

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Allows toggle functionality on Azure Policy to disable Azure Maps local authentication support. This will disable Shared Keys and Shared Access Signature Token authentication from any usage.
        """
        return pulumi.get(self, "disable_local_auth")

    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_local_auth", value)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input['EncryptionArgs']]:
        """
        (Optional) Discouraged to include in resource definition. Only needed where it is possible to disable platform (AKA infrastructure) encryption. Azure SQL TDE is an example of this. Values are enabled and disabled.
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input['EncryptionArgs']]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter(name="linkedResources")
    def linked_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LinkedResourceArgs']]]]:
        """
        The array of associated resources to the Map account. Linked resource in the array cannot individually update, you must update all linked resources in the array together. These resources may be used on operations on the Azure Maps REST API. Access is controlled by the Map Account Managed Identity(s) permissions to those resource(s).
        """
        return pulumi.get(self, "linked_resources")

    @linked_resources.setter
    def linked_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LinkedResourceArgs']]]]):
        pulumi.set(self, "linked_resources", value)


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[Union[str, 'Name']]):
        """
        The SKU of the Maps Account.
        :param pulumi.Input[Union[str, 'Name']] name: The name of the SKU, in standard format (such as S0).
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'Name']]:
        """
        The name of the SKU, in standard format (such as S0).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'Name']]):
        pulumi.set(self, "name", value)


