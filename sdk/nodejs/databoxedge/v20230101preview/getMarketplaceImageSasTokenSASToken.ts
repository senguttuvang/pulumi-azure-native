// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

export function getMarketplaceImageSasTokenSASToken(args: GetMarketplaceImageSasTokenSASTokenArgs, opts?: pulumi.InvokeOptions): Promise<GetMarketplaceImageSasTokenSASTokenResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:databoxedge/v20230101preview:getMarketplaceImageSasTokenSASToken", {
        "deviceName": args.deviceName,
        "offerName": args.offerName,
        "publisherName": args.publisherName,
        "resourceGroupName": args.resourceGroupName,
        "skuName": args.skuName,
        "versionName": args.versionName,
    }, opts);
}

export interface GetMarketplaceImageSasTokenSASTokenArgs {
    deviceName: string;
    offerName: string;
    publisherName: string;
    /**
     * The resource group name.
     */
    resourceGroupName: string;
    skuName: string;
    versionName: string;
}

export interface GetMarketplaceImageSasTokenSASTokenResult {
    readonly sasUri?: string;
    readonly status?: string;
}
export function getMarketplaceImageSasTokenSASTokenOutput(args: GetMarketplaceImageSasTokenSASTokenOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetMarketplaceImageSasTokenSASTokenResult> {
    return pulumi.output(args).apply((a: any) => getMarketplaceImageSasTokenSASToken(a, opts))
}

export interface GetMarketplaceImageSasTokenSASTokenOutputArgs {
    deviceName: pulumi.Input<string>;
    offerName: pulumi.Input<string>;
    publisherName: pulumi.Input<string>;
    /**
     * The resource group name.
     */
    resourceGroupName: pulumi.Input<string>;
    skuName: pulumi.Input<string>;
    versionName: pulumi.Input<string>;
}
