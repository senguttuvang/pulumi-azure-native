// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Get the details of a Streaming Locator in the Media Services account
 */
export function getStreamingLocator(args: GetStreamingLocatorArgs, opts?: pulumi.InvokeOptions): Promise<GetStreamingLocatorResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:media/v20180330preview:getStreamingLocator", {
        "accountName": args.accountName,
        "resourceGroupName": args.resourceGroupName,
        "streamingLocatorName": args.streamingLocatorName,
    }, opts);
}

export interface GetStreamingLocatorArgs {
    /**
     * The Media Services account name.
     */
    accountName: string;
    /**
     * The name of the resource group within the Azure subscription.
     */
    resourceGroupName: string;
    /**
     * The Streaming Locator name.
     */
    streamingLocatorName: string;
}

/**
 * A Streaming Locator resource
 */
export interface GetStreamingLocatorResult {
    /**
     * Asset Name
     */
    readonly assetName: string;
    /**
     * ContentKeys used by this Streaming Locator
     */
    readonly contentKeys?: outputs.media.v20180330preview.StreamingLocatorUserDefinedContentKeyResponse[];
    /**
     * Creation time of Streaming Locator
     */
    readonly created: string;
    /**
     * Default ContentKeyPolicy used by this Streaming Locator
     */
    readonly defaultContentKeyPolicyName?: string;
    /**
     * EndTime of Streaming Locator
     */
    readonly endTime?: string;
    /**
     * Fully qualified resource ID for the resource.
     */
    readonly id: string;
    /**
     * The name of the resource.
     */
    readonly name: string;
    /**
     * StartTime of Streaming Locator
     */
    readonly startTime?: string;
    /**
     * StreamingLocatorId of Streaming Locator
     */
    readonly streamingLocatorId?: string;
    /**
     * Streaming policy name used by this streaming locator. Either specify the name of streaming policy you created or use one of the predefined streaming polices. The predefined streaming policies available are: 'Predefined_DownloadOnly', 'Predefined_ClearStreamingOnly', 'Predefined_DownloadAndClearStreaming', 'Predefined_ClearKey', 'Predefined_SecureStreaming' and 'Predefined_SecureStreamingWithFairPlay'
     */
    readonly streamingPolicyName: string;
    /**
     * The type of the resource.
     */
    readonly type: string;
}
/**
 * Get the details of a Streaming Locator in the Media Services account
 */
export function getStreamingLocatorOutput(args: GetStreamingLocatorOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetStreamingLocatorResult> {
    return pulumi.output(args).apply((a: any) => getStreamingLocator(a, opts))
}

export interface GetStreamingLocatorOutputArgs {
    /**
     * The Media Services account name.
     */
    accountName: pulumi.Input<string>;
    /**
     * The name of the resource group within the Azure subscription.
     */
    resourceGroupName: pulumi.Input<string>;
    /**
     * The Streaming Locator name.
     */
    streamingLocatorName: pulumi.Input<string>;
}
