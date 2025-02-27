// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// Export sub-modules:
import * as v20211120preview from "./v20211120preview";
import * as v20221201preview from "./v20221201preview";
import * as v20230101 from "./v20230101";
import * as v20240501 from "./v20240501";

export {
    v20211120preview,
    v20221201preview,
    v20230101,
    v20240501,
};

export const Action = {
    Allow: "Allow",
} as const;

/**
 * The action of virtual network rule.
 */
export type Action = (typeof Action)[keyof typeof Action];

export const EncryptionType = {
    /**
     * Volume is encrypted at rest with Platform managed key. It is the default encryption type.
     */
    EncryptionAtRestWithPlatformKey: "EncryptionAtRestWithPlatformKey",
} as const;

/**
 * Type of encryption
 */
export type EncryptionType = (typeof EncryptionType)[keyof typeof EncryptionType];

export const PrivateEndpointServiceConnectionStatus = {
    Pending: "Pending",
    Approved: "Approved",
    Failed: "Failed",
    Rejected: "Rejected",
} as const;

/**
 * Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
 */
export type PrivateEndpointServiceConnectionStatus = (typeof PrivateEndpointServiceConnectionStatus)[keyof typeof PrivateEndpointServiceConnectionStatus];

export const SkuName = {
    /**
     * Premium locally redundant storage
     */
    Premium_LRS: "Premium_LRS",
    /**
     * Premium zone redundant storage
     */
    Premium_ZRS: "Premium_ZRS",
} as const;

/**
 * The sku name.
 */
export type SkuName = (typeof SkuName)[keyof typeof SkuName];

export const SkuTier = {
    /**
     * Premium Tier
     */
    Premium: "Premium",
} as const;

/**
 * The sku tier.
 */
export type SkuTier = (typeof SkuTier)[keyof typeof SkuTier];

export const StorageTargetType = {
    Iscsi: "Iscsi",
    None: "None",
} as const;

/**
 * Type of storage target
 */
export type StorageTargetType = (typeof StorageTargetType)[keyof typeof StorageTargetType];

export const VolumeCreateOption = {
    None: "None",
} as const;

/**
 * This enumerates the possible sources of a volume creation.
 */
export type VolumeCreateOption = (typeof VolumeCreateOption)[keyof typeof VolumeCreateOption];
