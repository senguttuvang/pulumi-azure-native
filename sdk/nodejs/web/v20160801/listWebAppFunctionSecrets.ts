// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Get function secrets for a function in a web site, or a deployment slot.
 */
export function listWebAppFunctionSecrets(args: ListWebAppFunctionSecretsArgs, opts?: pulumi.InvokeOptions): Promise<ListWebAppFunctionSecretsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:web/v20160801:listWebAppFunctionSecrets", {
        "functionName": args.functionName,
        "name": args.name,
        "resourceGroupName": args.resourceGroupName,
    }, opts);
}

export interface ListWebAppFunctionSecretsArgs {
    /**
     * Function name.
     */
    functionName: string;
    /**
     * Site name.
     */
    name: string;
    /**
     * Name of the resource group to which the resource belongs.
     */
    resourceGroupName: string;
}

/**
 * Function secrets.
 */
export interface ListWebAppFunctionSecretsResult {
    /**
     * Resource Id.
     */
    readonly id: string;
    /**
     * Secret key.
     */
    readonly key?: string;
    /**
     * Kind of resource.
     */
    readonly kind?: string;
    /**
     * Resource Name.
     */
    readonly name: string;
    /**
     * Trigger URL.
     */
    readonly triggerUrl?: string;
    /**
     * Resource type.
     */
    readonly type: string;
}
/**
 * Get function secrets for a function in a web site, or a deployment slot.
 */
export function listWebAppFunctionSecretsOutput(args: ListWebAppFunctionSecretsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<ListWebAppFunctionSecretsResult> {
    return pulumi.output(args).apply((a: any) => listWebAppFunctionSecrets(a, opts))
}

export interface ListWebAppFunctionSecretsOutputArgs {
    /**
     * Function name.
     */
    functionName: pulumi.Input<string>;
    /**
     * Site name.
     */
    name: pulumi.Input<string>;
    /**
     * Name of the resource group to which the resource belongs.
     */
    resourceGroupName: pulumi.Input<string>;
}
