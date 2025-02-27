// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Lists all effective virtual networks by specified network group.
 */
export function listListEffectiveVirtualNetworkByNetworkGroup(args: ListListEffectiveVirtualNetworkByNetworkGroupArgs, opts?: pulumi.InvokeOptions): Promise<ListListEffectiveVirtualNetworkByNetworkGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:network/v20220401preview:listListEffectiveVirtualNetworkByNetworkGroup", {
        "networkGroupName": args.networkGroupName,
        "networkManagerName": args.networkManagerName,
        "resourceGroupName": args.resourceGroupName,
        "skipToken": args.skipToken,
    }, opts);
}

export interface ListListEffectiveVirtualNetworkByNetworkGroupArgs {
    /**
     * The name of the network group.
     */
    networkGroupName: string;
    /**
     * The name of the network manager.
     */
    networkManagerName: string;
    /**
     * The name of the resource group.
     */
    resourceGroupName: string;
    /**
     * When present, the value can be passed to a subsequent query call (together with the same query and scopes used in the current request) to retrieve the next page of data.
     */
    skipToken?: string;
}

/**
 * Result of the request to list Effective Virtual Network. It contains a list of groups and a URL link to get the next set of results.
 */
export interface ListListEffectiveVirtualNetworkByNetworkGroupResult {
    /**
     * When present, the value can be passed to a subsequent query call (together with the same query and scopes used in the current request) to retrieve the next page of data.
     */
    readonly skipToken?: string;
    /**
     * Gets a page of EffectiveVirtualNetwork
     */
    readonly value?: outputs.network.v20220401preview.EffectiveVirtualNetworkResponse[];
}
/**
 * Lists all effective virtual networks by specified network group.
 */
export function listListEffectiveVirtualNetworkByNetworkGroupOutput(args: ListListEffectiveVirtualNetworkByNetworkGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<ListListEffectiveVirtualNetworkByNetworkGroupResult> {
    return pulumi.output(args).apply((a: any) => listListEffectiveVirtualNetworkByNetworkGroup(a, opts))
}

export interface ListListEffectiveVirtualNetworkByNetworkGroupOutputArgs {
    /**
     * The name of the network group.
     */
    networkGroupName: pulumi.Input<string>;
    /**
     * The name of the network manager.
     */
    networkManagerName: pulumi.Input<string>;
    /**
     * The name of the resource group.
     */
    resourceGroupName: pulumi.Input<string>;
    /**
     * When present, the value can be passed to a subsequent query call (together with the same query and scopes used in the current request) to retrieve the next page of data.
     */
    skipToken?: pulumi.Input<string>;
}
