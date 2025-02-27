// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// Export sub-modules:
import * as v20230415preview from "./v20230415preview";
import * as v20230901preview from "./v20230901preview";
import * as v20231027preview from "./v20231027preview";
import * as v20231101 from "./v20231101";
import * as v20240101 from "./v20240101";
import * as v20240322preview from "./v20240322preview";

export {
    v20230415preview,
    v20230901preview,
    v20231027preview,
    v20231101,
    v20240101,
    v20240322preview,
};

export const FilterType = {
    Simple: "Simple",
} as const;

/**
 * Enum that discriminates between filter types. Currently only `Simple` type is supported.
 */
export type FilterType = (typeof FilterType)[keyof typeof FilterType];

export const ResourceIdentityType = {
    None: "None",
    SystemAssigned: "SystemAssigned",
    UserAssigned: "UserAssigned",
} as const;

/**
 * String of the resource identity type.
 */
export type ResourceIdentityType = (typeof ResourceIdentityType)[keyof typeof ResourceIdentityType];

export const SelectorType = {
    List: "List",
    Query: "Query",
} as const;

/**
 * Enum of the selector type.
 */
export type SelectorType = (typeof SelectorType)[keyof typeof SelectorType];

export const TargetReferenceType = {
    ChaosTarget: "ChaosTarget",
} as const;

/**
 * Enum of the Target reference type.
 */
export type TargetReferenceType = (typeof TargetReferenceType)[keyof typeof TargetReferenceType];
