# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AuthenticationMode',
    'AutoStorageAuthenticationMode',
    'KeySource',
    'PoolAllocationMode',
    'PublicNetworkAccessType',
    'ResourceIdentityType',
]


class AuthenticationMode(str, Enum):
    """
    The authentication mode for the Batch account.
    """
    SHARED_KEY = "SharedKey"
    """
    The authentication mode using shared keys.
    """
    AAD = "AAD"
    """
    The authentication mode using Azure Active Directory.
    """
    TASK_AUTHENTICATION_TOKEN = "TaskAuthenticationToken"
    """
    The authentication mode using task authentication tokens.
    """


class AutoStorageAuthenticationMode(str, Enum):
    """
    The authentication mode which the Batch service will use to manage the auto-storage account.
    """
    STORAGE_KEYS = "StorageKeys"
    """
    The Batch service will authenticate requests to auto-storage using storage account keys.
    """
    BATCH_ACCOUNT_MANAGED_IDENTITY = "BatchAccountManagedIdentity"
    """
    The Batch service will authenticate requests to auto-storage using the managed identity assigned to the Batch account.
    """


class KeySource(str, Enum):
    """
    Type of the key source.
    """
    MICROSOFT_BATCH = "Microsoft.Batch"
    """
    Batch creates and manages the encryption keys used to protect the account data.
    """
    MICROSOFT_KEY_VAULT = "Microsoft.KeyVault"
    """
    The encryption keys used to protect the account data are stored in an external key vault. If this is set then the Batch Account identity must be set to `SystemAssigned` and a valid Key Identifier must also be supplied under the keyVaultProperties.
    """


class PoolAllocationMode(str, Enum):
    """
    The pool allocation mode also affects how clients may authenticate to the Batch Service API. If the mode is BatchService, clients may authenticate using access keys or Azure Active Directory. If the mode is UserSubscription, clients must use Azure Active Directory. The default is BatchService.
    """
    BATCH_SERVICE = "BatchService"
    """
    Pools will be allocated in subscriptions owned by the Batch service.
    """
    USER_SUBSCRIPTION = "UserSubscription"
    """
    Pools will be allocated in a subscription owned by the user.
    """


class PublicNetworkAccessType(str, Enum):
    """
    If not specified, the default value is 'enabled'.
    """
    ENABLED = "Enabled"
    """
    Enables connectivity to Azure Batch through public DNS.
    """
    DISABLED = "Disabled"
    """
    Disables public connectivity and enables private connectivity to Azure Batch Service through private endpoint resource.
    """


class ResourceIdentityType(str, Enum):
    """
    The type of identity used for the Batch account.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    """
    Batch account has a system assigned identity with it.
    """
    USER_ASSIGNED = "UserAssigned"
    """
    Batch account has user assigned identities with it.
    """
    NONE = "None"
    """
    Batch account has no identity associated with it. Setting `None` in update account will remove existing identities.
    """
