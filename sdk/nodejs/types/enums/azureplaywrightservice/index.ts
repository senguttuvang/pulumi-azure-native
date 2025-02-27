// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// Export sub-modules:
import * as v20231001preview from "./v20231001preview";
import * as v20240201preview from "./v20240201preview";

export {
    v20231001preview,
    v20240201preview,
};

export const EnablementStatus = {
    /**
     * The feature is Enabled.
     */
    Enabled: "Enabled",
    /**
     * The feature is Disabled.
     */
    Disabled: "Disabled",
} as const;

/**
 * When enabled, Playwright client workers can connect to cloud-hosted browsers. This can increase the number of parallel workers for a test run, significantly minimizing test completion durations.
 */
export type EnablementStatus = (typeof EnablementStatus)[keyof typeof EnablementStatus];
