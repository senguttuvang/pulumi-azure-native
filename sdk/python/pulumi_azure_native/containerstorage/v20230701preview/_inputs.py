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
    'AssignmentArgs',
    'AzureDiskArgs',
    'DiskArgs',
    'ElasticSanArgs',
    'EncryptionArgs',
    'EphemeralDiskArgs',
    'ManagedServiceIdentityArgs',
    'PoolTypeArgs',
    'RequestsArgs',
    'ResourcesArgs',
]

@pulumi.input_type
class AssignmentArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str]):
        """
        Assignment Properties
        :param pulumi.Input[str] id: Resource id for the assigned resource
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Resource id for the assigned resource
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class AzureDiskArgs:
    def __init__(__self__, *,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]] = None,
                 encryption: Optional[pulumi.Input['EncryptionArgs']] = None,
                 sku_name: Optional[pulumi.Input[Union[str, 'AzureDiskSkuName']]] = None):
        """
        Azure Disk Pool Properties
        :param pulumi.Input[Sequence[pulumi.Input['DiskArgs']]] disks: Only required if individual disk selection is desired. Path to disk, e.g. <nodename>:/dev/sda or WWN. Supports specifying multiple disks (same syntax as tags).
        :param pulumi.Input['EncryptionArgs'] encryption: Encryption specifies the encryption configuration for the Azure Disk pool
        :param pulumi.Input[Union[str, 'AzureDiskSkuName']] sku_name: Sku name
        """
        if disks is not None:
            pulumi.set(__self__, "disks", disks)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if sku_name is not None:
            pulumi.set(__self__, "sku_name", sku_name)

    @property
    @pulumi.getter
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]]:
        """
        Only required if individual disk selection is desired. Path to disk, e.g. <nodename>:/dev/sda or WWN. Supports specifying multiple disks (same syntax as tags).
        """
        return pulumi.get(self, "disks")

    @disks.setter
    def disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]]):
        pulumi.set(self, "disks", value)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input['EncryptionArgs']]:
        """
        Encryption specifies the encryption configuration for the Azure Disk pool
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input['EncryptionArgs']]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> Optional[pulumi.Input[Union[str, 'AzureDiskSkuName']]]:
        """
        Sku name
        """
        return pulumi.get(self, "sku_name")

    @sku_name.setter
    def sku_name(self, value: Optional[pulumi.Input[Union[str, 'AzureDiskSkuName']]]):
        pulumi.set(self, "sku_name", value)


@pulumi.input_type
class DiskArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 reference: pulumi.Input[str]):
        """
        Model for disk for that pool is using
        :param pulumi.Input[str] id: ID is the disk identifier visible to the OS. It is typically the WWN or disk ID in formats such as eui.e8238fa6bf530001001b448b45263379 or 0x5002cf6cbc5dd460
        :param pulumi.Input[str] reference: Reference is the location of the disk in an external system.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "reference", reference)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        ID is the disk identifier visible to the OS. It is typically the WWN or disk ID in formats such as eui.e8238fa6bf530001001b448b45263379 or 0x5002cf6cbc5dd460
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def reference(self) -> pulumi.Input[str]:
        """
        Reference is the location of the disk in an external system.
        """
        return pulumi.get(self, "reference")

    @reference.setter
    def reference(self, value: pulumi.Input[str]):
        pulumi.set(self, "reference", value)


@pulumi.input_type
class ElasticSanArgs:
    def __init__(__self__, *,
                 encryption: Optional[pulumi.Input['EncryptionArgs']] = None,
                 sku_name: Optional[pulumi.Input[Union[str, 'ElasticSanSkuName']]] = None):
        """
        Elastic San Pool Properties
        :param pulumi.Input['EncryptionArgs'] encryption: Encryption specifies the encryption configuration for the Azure Disk pool
        :param pulumi.Input[Union[str, 'ElasticSanSkuName']] sku_name: Sku name
        """
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if sku_name is not None:
            pulumi.set(__self__, "sku_name", sku_name)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input['EncryptionArgs']]:
        """
        Encryption specifies the encryption configuration for the Azure Disk pool
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input['EncryptionArgs']]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter(name="skuName")
    def sku_name(self) -> Optional[pulumi.Input[Union[str, 'ElasticSanSkuName']]]:
        """
        Sku name
        """
        return pulumi.get(self, "sku_name")

    @sku_name.setter
    def sku_name(self, value: Optional[pulumi.Input[Union[str, 'ElasticSanSkuName']]]):
        pulumi.set(self, "sku_name", value)


@pulumi.input_type
class EncryptionArgs:
    def __init__(__self__, *,
                 key_name: pulumi.Input[str],
                 key_vault_uri: pulumi.Input[str],
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None):
        """
        Encryption key properties for the pool.
        :param pulumi.Input[str] key_name: The name of the key vault key.
        :param pulumi.Input[str] key_vault_uri: The URI of the key vault.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: The managed service identities assigned to this resource.
        """
        pulumi.set(__self__, "key_name", key_name)
        pulumi.set(__self__, "key_vault_uri", key_vault_uri)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[str]:
        """
        The name of the key vault key.
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> pulumi.Input[str]:
        """
        The URI of the key vault.
        """
        return pulumi.get(self, "key_vault_uri")

    @key_vault_uri.setter
    def key_vault_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_uri", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)


@pulumi.input_type
class EphemeralDiskArgs:
    def __init__(__self__, *,
                 disks: Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]] = None,
                 replicas: Optional[pulumi.Input[float]] = None):
        """
        Ephemeral Disk Pool Properties
        :param pulumi.Input[Sequence[pulumi.Input['DiskArgs']]] disks: Only required if individual disk selection is desired. Path to disk, e.g. <nodename>:/dev/sda or WWN. Supports specifying multiple disks (same syntax as tags).
        :param pulumi.Input[float] replicas: The number of data copies. Default 3.
        """
        if disks is not None:
            pulumi.set(__self__, "disks", disks)
        if replicas is None:
            replicas = 3
        if replicas is not None:
            pulumi.set(__self__, "replicas", replicas)

    @property
    @pulumi.getter
    def disks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]]:
        """
        Only required if individual disk selection is desired. Path to disk, e.g. <nodename>:/dev/sda or WWN. Supports specifying multiple disks (same syntax as tags).
        """
        return pulumi.get(self, "disks")

    @disks.setter
    def disks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DiskArgs']]]]):
        pulumi.set(self, "disks", value)

    @property
    @pulumi.getter
    def replicas(self) -> Optional[pulumi.Input[float]]:
        """
        The number of data copies. Default 3.
        """
        return pulumi.get(self, "replicas")

    @replicas.setter
    def replicas(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "replicas", value)


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
class PoolTypeArgs:
    def __init__(__self__, *,
                 azure_disk: Optional[pulumi.Input['AzureDiskArgs']] = None,
                 elastic_san: Optional[pulumi.Input['ElasticSanArgs']] = None,
                 ephemeral_disk: Optional[pulumi.Input['EphemeralDiskArgs']] = None):
        """
        Type of the Pool: ephemeralDisk, azureDisk, or elasticsan
        :param pulumi.Input['AzureDiskArgs'] azure_disk: Disk Pool Properties
        :param pulumi.Input['ElasticSanArgs'] elastic_san: Elastic San Pool Properties
        :param pulumi.Input['EphemeralDiskArgs'] ephemeral_disk: Ephemeral Pool Properties
        """
        if azure_disk is not None:
            pulumi.set(__self__, "azure_disk", azure_disk)
        if elastic_san is not None:
            pulumi.set(__self__, "elastic_san", elastic_san)
        if ephemeral_disk is not None:
            pulumi.set(__self__, "ephemeral_disk", ephemeral_disk)

    @property
    @pulumi.getter(name="azureDisk")
    def azure_disk(self) -> Optional[pulumi.Input['AzureDiskArgs']]:
        """
        Disk Pool Properties
        """
        return pulumi.get(self, "azure_disk")

    @azure_disk.setter
    def azure_disk(self, value: Optional[pulumi.Input['AzureDiskArgs']]):
        pulumi.set(self, "azure_disk", value)

    @property
    @pulumi.getter(name="elasticSan")
    def elastic_san(self) -> Optional[pulumi.Input['ElasticSanArgs']]:
        """
        Elastic San Pool Properties
        """
        return pulumi.get(self, "elastic_san")

    @elastic_san.setter
    def elastic_san(self, value: Optional[pulumi.Input['ElasticSanArgs']]):
        pulumi.set(self, "elastic_san", value)

    @property
    @pulumi.getter(name="ephemeralDisk")
    def ephemeral_disk(self) -> Optional[pulumi.Input['EphemeralDiskArgs']]:
        """
        Ephemeral Pool Properties
        """
        return pulumi.get(self, "ephemeral_disk")

    @ephemeral_disk.setter
    def ephemeral_disk(self, value: Optional[pulumi.Input['EphemeralDiskArgs']]):
        pulumi.set(self, "ephemeral_disk", value)


@pulumi.input_type
class RequestsArgs:
    def __init__(__self__, *,
                 storage: Optional[pulumi.Input[float]] = None):
        """
        Requests for capacity for the pool.
        :param pulumi.Input[float] storage: Requested capacity of the pool in GiB.
        """
        if storage is None:
            storage = 1024
        if storage is not None:
            pulumi.set(__self__, "storage", storage)

    @property
    @pulumi.getter
    def storage(self) -> Optional[pulumi.Input[float]]:
        """
        Requested capacity of the pool in GiB.
        """
        return pulumi.get(self, "storage")

    @storage.setter
    def storage(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "storage", value)


@pulumi.input_type
class ResourcesArgs:
    def __init__(__self__, *,
                 requests: Optional[pulumi.Input['RequestsArgs']] = None):
        """
        Resource Requests for the pool.
        :param pulumi.Input['RequestsArgs'] requests: Requests for capacity for the pool.
        """
        if requests is not None:
            pulumi.set(__self__, "requests", requests)

    @property
    @pulumi.getter
    def requests(self) -> Optional[pulumi.Input['RequestsArgs']]:
        """
        Requests for capacity for the pool.
        """
        return pulumi.get(self, "requests")

    @requests.setter
    def requests(self, value: Optional[pulumi.Input['RequestsArgs']]):
        pulumi.set(self, "requests", value)


