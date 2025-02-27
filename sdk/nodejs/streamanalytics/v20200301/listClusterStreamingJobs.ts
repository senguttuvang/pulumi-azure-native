// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Lists all of the streaming jobs in the given cluster.
 */
export function listClusterStreamingJobs(args: ListClusterStreamingJobsArgs, opts?: pulumi.InvokeOptions): Promise<ListClusterStreamingJobsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:streamanalytics/v20200301:listClusterStreamingJobs", {
        "clusterName": args.clusterName,
        "resourceGroupName": args.resourceGroupName,
    }, opts);
}

export interface ListClusterStreamingJobsArgs {
    /**
     * The name of the cluster.
     */
    clusterName: string;
    /**
     * The name of the resource group. The name is case insensitive.
     */
    resourceGroupName: string;
}

/**
 * A list of streaming jobs. Populated by a List operation.
 */
export interface ListClusterStreamingJobsResult {
    /**
     * The URL to fetch the next set of streaming jobs.
     */
    readonly nextLink: string;
    /**
     * A list of streaming jobs.
     */
    readonly value: outputs.streamanalytics.v20200301.ClusterJobResponse[];
}
/**
 * Lists all of the streaming jobs in the given cluster.
 */
export function listClusterStreamingJobsOutput(args: ListClusterStreamingJobsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<ListClusterStreamingJobsResult> {
    return pulumi.output(args).apply((a: any) => listClusterStreamingJobs(a, opts))
}

export interface ListClusterStreamingJobsOutputArgs {
    /**
     * The name of the cluster.
     */
    clusterName: pulumi.Input<string>;
    /**
     * The name of the resource group. The name is case insensitive.
     */
    resourceGroupName: pulumi.Input<string>;
}
