// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets a named add-on of an app.
 */
export function getWebAppPremierAddOn(args: GetWebAppPremierAddOnArgs, opts?: pulumi.InvokeOptions): Promise<GetWebAppPremierAddOnResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:web/v20201001:getWebAppPremierAddOn", {
        "name": args.name,
        "premierAddOnName": args.premierAddOnName,
        "resourceGroupName": args.resourceGroupName,
    }, opts);
}

export interface GetWebAppPremierAddOnArgs {
    /**
     * Name of the app.
     */
    name: string;
    /**
     * Add-on name.
     */
    premierAddOnName: string;
    /**
     * Name of the resource group to which the resource belongs.
     */
    resourceGroupName: string;
}

/**
 * Premier add-on.
 */
export interface GetWebAppPremierAddOnResult {
    /**
     * Resource Id.
     */
    readonly id: string;
    /**
     * Kind of resource.
     */
    readonly kind?: string;
    /**
     * Resource Location.
     */
    readonly location: string;
    /**
     * Premier add on Marketplace offer.
     */
    readonly marketplaceOffer?: string;
    /**
     * Premier add on Marketplace publisher.
     */
    readonly marketplacePublisher?: string;
    /**
     * Resource Name.
     */
    readonly name: string;
    /**
     * Premier add on Product.
     */
    readonly product?: string;
    /**
     * Premier add on SKU.
     */
    readonly sku?: string;
    /**
     * The system metadata relating to this resource.
     */
    readonly systemData: outputs.web.v20201001.SystemDataResponse;
    /**
     * Resource tags.
     */
    readonly tags?: {[key: string]: string};
    /**
     * Resource type.
     */
    readonly type: string;
    /**
     * Premier add on Vendor.
     */
    readonly vendor?: string;
}
/**
 * Gets a named add-on of an app.
 */
export function getWebAppPremierAddOnOutput(args: GetWebAppPremierAddOnOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetWebAppPremierAddOnResult> {
    return pulumi.output(args).apply((a: any) => getWebAppPremierAddOn(a, opts))
}

export interface GetWebAppPremierAddOnOutputArgs {
    /**
     * Name of the app.
     */
    name: pulumi.Input<string>;
    /**
     * Add-on name.
     */
    premierAddOnName: pulumi.Input<string>;
    /**
     * Name of the resource group to which the resource belongs.
     */
    resourceGroupName: pulumi.Input<string>;
}
