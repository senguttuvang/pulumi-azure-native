// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Product serial and status for the service
 */
export function listPaloAltoNetworksCloudngfwProductSerialNumberStatus(args?: ListPaloAltoNetworksCloudngfwProductSerialNumberStatusArgs, opts?: pulumi.InvokeOptions): Promise<ListPaloAltoNetworksCloudngfwProductSerialNumberStatusResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:cloudngfw/v20240207preview:listPaloAltoNetworksCloudngfwProductSerialNumberStatus", {
    }, opts);
}

export interface ListPaloAltoNetworksCloudngfwProductSerialNumberStatusArgs {
}

/**
 * Product serial and status for the service
 */
export interface ListPaloAltoNetworksCloudngfwProductSerialNumberStatusResult {
    /**
     * product Serial associated with given resource
     */
    readonly serialNumber?: string;
    /**
     * allocation status of the product serial number
     */
    readonly status: string;
}
/**
 * Product serial and status for the service
 */
export function listPaloAltoNetworksCloudngfwProductSerialNumberStatusOutput(opts?: pulumi.InvokeOptions): pulumi.Output<ListPaloAltoNetworksCloudngfwProductSerialNumberStatusResult> {
    return pulumi.output(listPaloAltoNetworksCloudngfwProductSerialNumberStatus(opts))
}
