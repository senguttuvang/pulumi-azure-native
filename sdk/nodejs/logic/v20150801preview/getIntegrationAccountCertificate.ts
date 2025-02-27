// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets an integration account certificate.
 */
export function getIntegrationAccountCertificate(args: GetIntegrationAccountCertificateArgs, opts?: pulumi.InvokeOptions): Promise<GetIntegrationAccountCertificateResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:logic/v20150801preview:getIntegrationAccountCertificate", {
        "certificateName": args.certificateName,
        "integrationAccountName": args.integrationAccountName,
        "resourceGroupName": args.resourceGroupName,
    }, opts);
}

export interface GetIntegrationAccountCertificateArgs {
    /**
     * The integration account certificate name.
     */
    certificateName: string;
    /**
     * The integration account name.
     */
    integrationAccountName: string;
    /**
     * The resource group name.
     */
    resourceGroupName: string;
}

export interface GetIntegrationAccountCertificateResult {
    /**
     * The changed time.
     */
    readonly changedTime: string;
    /**
     * The created time.
     */
    readonly createdTime: string;
    /**
     * The resource id.
     */
    readonly id?: string;
    /**
     * The key details in the key vault.
     */
    readonly key?: outputs.logic.v20150801preview.KeyVaultKeyReferenceResponse;
    /**
     * The resource location.
     */
    readonly location?: string;
    /**
     * The metadata.
     */
    readonly metadata?: any;
    /**
     * The resource name.
     */
    readonly name?: string;
    /**
     * The public certificate.
     */
    readonly publicCertificate?: string;
    /**
     * The resource tags.
     */
    readonly tags?: {[key: string]: string};
    /**
     * The resource type.
     */
    readonly type?: string;
}
/**
 * Gets an integration account certificate.
 */
export function getIntegrationAccountCertificateOutput(args: GetIntegrationAccountCertificateOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetIntegrationAccountCertificateResult> {
    return pulumi.output(args).apply((a: any) => getIntegrationAccountCertificate(a, opts))
}

export interface GetIntegrationAccountCertificateOutputArgs {
    /**
     * The integration account certificate name.
     */
    certificateName: pulumi.Input<string>;
    /**
     * The integration account name.
     */
    integrationAccountName: pulumi.Input<string>;
    /**
     * The resource group name.
     */
    resourceGroupName: pulumi.Input<string>;
}
