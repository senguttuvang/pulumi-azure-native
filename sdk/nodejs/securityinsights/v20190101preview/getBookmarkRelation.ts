// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

/**
 * Gets a bookmark relation.
 */
export function getBookmarkRelation(args: GetBookmarkRelationArgs, opts?: pulumi.InvokeOptions): Promise<GetBookmarkRelationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:securityinsights/v20190101preview:getBookmarkRelation", {
        "bookmarkId": args.bookmarkId,
        "operationalInsightsResourceProvider": args.operationalInsightsResourceProvider,
        "relationName": args.relationName,
        "resourceGroupName": args.resourceGroupName,
        "workspaceName": args.workspaceName,
    }, opts);
}

export interface GetBookmarkRelationArgs {
    /**
     * Bookmark ID
     */
    bookmarkId: string;
    /**
     * The namespace of workspaces resource provider- Microsoft.OperationalInsights.
     */
    operationalInsightsResourceProvider: string;
    /**
     * Relation Name
     */
    relationName: string;
    /**
     * The name of the resource group within the user's subscription. The name is case insensitive.
     */
    resourceGroupName: string;
    /**
     * The name of the workspace.
     */
    workspaceName: string;
}

/**
 * Represents a relation between two resources
 */
export interface GetBookmarkRelationResult {
    /**
     * Etag of the azure resource
     */
    readonly etag?: string;
    /**
     * Azure resource Id
     */
    readonly id: string;
    /**
     * Azure resource name
     */
    readonly name: string;
    /**
     * The resource ID of the related resource
     */
    readonly relatedResourceId: string;
    /**
     * The resource kind of the related resource
     */
    readonly relatedResourceKind: string;
    /**
     * The name of the related resource
     */
    readonly relatedResourceName: string;
    /**
     * The resource type of the related resource
     */
    readonly relatedResourceType: string;
    /**
     * Azure resource type
     */
    readonly type: string;
}
/**
 * Gets a bookmark relation.
 */
export function getBookmarkRelationOutput(args: GetBookmarkRelationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetBookmarkRelationResult> {
    return pulumi.output(args).apply((a: any) => getBookmarkRelation(a, opts))
}

export interface GetBookmarkRelationOutputArgs {
    /**
     * Bookmark ID
     */
    bookmarkId: pulumi.Input<string>;
    /**
     * The namespace of workspaces resource provider- Microsoft.OperationalInsights.
     */
    operationalInsightsResourceProvider: pulumi.Input<string>;
    /**
     * Relation Name
     */
    relationName: pulumi.Input<string>;
    /**
     * The name of the resource group within the user's subscription. The name is case insensitive.
     */
    resourceGroupName: pulumi.Input<string>;
    /**
     * The name of the workspace.
     */
    workspaceName: pulumi.Input<string>;
}
