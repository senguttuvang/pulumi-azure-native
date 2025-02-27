// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * List of RP resources which supports pagination.
 */
export function listAzureDevOpsOrgAvailable(args: ListAzureDevOpsOrgAvailableArgs, opts?: pulumi.InvokeOptions): Promise<ListAzureDevOpsOrgAvailableResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:security/v20230901preview:listAzureDevOpsOrgAvailable", {
        "resourceGroupName": args.resourceGroupName,
        "securityConnectorName": args.securityConnectorName,
    }, opts);
}

export interface ListAzureDevOpsOrgAvailableArgs {
    /**
     * The name of the resource group. The name is case insensitive.
     */
    resourceGroupName: string;
    /**
     * The security connector name.
     */
    securityConnectorName: string;
}

/**
 * List of RP resources which supports pagination.
 */
export interface ListAzureDevOpsOrgAvailableResult {
    /**
     * Gets or sets next link to scroll over the results.
     */
    readonly nextLink?: string;
    /**
     * Gets or sets list of resources.
     */
    readonly value?: outputs.security.v20230901preview.AzureDevOpsOrgResponse[];
}
/**
 * List of RP resources which supports pagination.
 */
export function listAzureDevOpsOrgAvailableOutput(args: ListAzureDevOpsOrgAvailableOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<ListAzureDevOpsOrgAvailableResult> {
    return pulumi.output(args).apply((a: any) => listAzureDevOpsOrgAvailable(a, opts))
}

export interface ListAzureDevOpsOrgAvailableOutputArgs {
    /**
     * The name of the resource group. The name is case insensitive.
     */
    resourceGroupName: pulumi.Input<string>;
    /**
     * The security connector name.
     */
    securityConnectorName: pulumi.Input<string>;
}
