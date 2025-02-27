// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const ControlState = {
    /**
     * Field to enable a setting.
     */
    Enabled: "Enabled",
    /**
     * Field to disable a setting.
     */
    Disabled: "Disabled",
} as const;

/**
 * Flag to enable or disable redundancy for data product.
 */
export type ControlState = (typeof ControlState)[keyof typeof ControlState];

export const DataTypeState = {
    /**
     * Field to specify stopped state.
     */
    Stopped: "Stopped",
    /**
     * Field to specify running state.
     */
    Running: "Running",
} as const;

/**
 * State of data type.
 */
export type DataTypeState = (typeof DataTypeState)[keyof typeof DataTypeState];

export const DefaultAction = {
    /**
     * Represents allow action.
     */
    Allow: "Allow",
    /**
     * Represents deny action.
     */
    Deny: "Deny",
} as const;

/**
 * Default Action
 */
export type DefaultAction = (typeof DefaultAction)[keyof typeof DefaultAction];

export const ManagedServiceIdentityType = {
    None: "None",
    SystemAssigned: "SystemAssigned",
    UserAssigned: "UserAssigned",
    SystemAssigned_UserAssigned: "SystemAssigned, UserAssigned",
} as const;

/**
 * Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
 */
export type ManagedServiceIdentityType = (typeof ManagedServiceIdentityType)[keyof typeof ManagedServiceIdentityType];
