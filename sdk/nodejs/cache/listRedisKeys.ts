// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Retrieve a Redis cache's access keys. This operation requires write permission to the cache resource.
 * Azure REST API version: 2023-04-01.
 *
 * Other available API versions: 2015-08-01, 2017-02-01, 2019-07-01, 2020-06-01, 2023-05-01-preview, 2023-08-01, 2024-03-01, 2024-04-01-preview.
 */
export function listRedisKeys(args: ListRedisKeysArgs, opts?: pulumi.InvokeOptions): Promise<ListRedisKeysResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:cache:listRedisKeys", {
        "name": args.name,
        "resourceGroupName": args.resourceGroupName,
    }, opts);
}

export interface ListRedisKeysArgs {
    /**
     * The name of the Redis cache.
     */
    name: string;
    /**
     * The name of the resource group.
     */
    resourceGroupName: string;
}

/**
 * Redis cache access keys.
 */
export interface ListRedisKeysResult {
    /**
     * The current primary key that clients can use to authenticate with Redis cache.
     */
    readonly primaryKey: string;
    /**
     * The current secondary key that clients can use to authenticate with Redis cache.
     */
    readonly secondaryKey: string;
}
/**
 * Retrieve a Redis cache's access keys. This operation requires write permission to the cache resource.
 * Azure REST API version: 2023-04-01.
 *
 * Other available API versions: 2015-08-01, 2017-02-01, 2019-07-01, 2020-06-01, 2023-05-01-preview, 2023-08-01, 2024-03-01, 2024-04-01-preview.
 */
export function listRedisKeysOutput(args: ListRedisKeysOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<ListRedisKeysResult> {
    return pulumi.output(args).apply((a: any) => listRedisKeys(a, opts))
}

export interface ListRedisKeysOutputArgs {
    /**
     * The name of the Redis cache.
     */
    name: pulumi.Input<string>;
    /**
     * The name of the resource group.
     */
    resourceGroupName: pulumi.Input<string>;
}
