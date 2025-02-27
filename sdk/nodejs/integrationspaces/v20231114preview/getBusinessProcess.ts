// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Get a BusinessProcess
 */
export function getBusinessProcess(args: GetBusinessProcessArgs, opts?: pulumi.InvokeOptions): Promise<GetBusinessProcessResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:integrationspaces/v20231114preview:getBusinessProcess", {
        "applicationName": args.applicationName,
        "businessProcessName": args.businessProcessName,
        "resourceGroupName": args.resourceGroupName,
        "spaceName": args.spaceName,
    }, opts);
}

export interface GetBusinessProcessArgs {
    /**
     * The name of the Application
     */
    applicationName: string;
    /**
     * The name of the business process
     */
    businessProcessName: string;
    /**
     * The name of the resource group. The name is case insensitive.
     */
    resourceGroupName: string;
    /**
     * The name of the space
     */
    spaceName: string;
}

/**
 * A business process under application.
 */
export interface GetBusinessProcessResult {
    /**
     * The business process mapping.
     */
    readonly businessProcessMapping?: {[key: string]: outputs.integrationspaces.v20231114preview.BusinessProcessMappingItemResponse};
    /**
     * The business process stages.
     */
    readonly businessProcessStages?: {[key: string]: outputs.integrationspaces.v20231114preview.BusinessProcessStageResponse};
    /**
     * The description of the business process.
     */
    readonly description?: string;
    /**
     * Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
     */
    readonly id: string;
    /**
     * The business process identifier.
     */
    readonly identifier?: outputs.integrationspaces.v20231114preview.BusinessProcessIdentifierResponse;
    /**
     * The name of the resource
     */
    readonly name: string;
    /**
     * The status of the last operation.
     */
    readonly provisioningState: string;
    /**
     * Azure Resource Manager metadata containing createdBy and modifiedBy information.
     */
    readonly systemData: outputs.integrationspaces.v20231114preview.SystemDataResponse;
    /**
     * The table name of the business process.
     */
    readonly tableName?: string;
    /**
     * The tracking data store reference name.
     */
    readonly trackingDataStoreReferenceName?: string;
    /**
     * The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
     */
    readonly type: string;
    /**
     * The version of the business process.
     */
    readonly version: string;
}
/**
 * Get a BusinessProcess
 */
export function getBusinessProcessOutput(args: GetBusinessProcessOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetBusinessProcessResult> {
    return pulumi.output(args).apply((a: any) => getBusinessProcess(a, opts))
}

export interface GetBusinessProcessOutputArgs {
    /**
     * The name of the Application
     */
    applicationName: pulumi.Input<string>;
    /**
     * The name of the business process
     */
    businessProcessName: pulumi.Input<string>;
    /**
     * The name of the resource group. The name is case insensitive.
     */
    resourceGroupName: pulumi.Input<string>;
    /**
     * The name of the space
     */
    spaceName: pulumi.Input<string>;
}
