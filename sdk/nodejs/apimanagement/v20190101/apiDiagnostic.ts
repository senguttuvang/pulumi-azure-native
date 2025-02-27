// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Diagnostic details.
 */
export class ApiDiagnostic extends pulumi.CustomResource {
    /**
     * Get an existing ApiDiagnostic resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ApiDiagnostic {
        return new ApiDiagnostic(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure-native:apimanagement/v20190101:ApiDiagnostic';

    /**
     * Returns true if the given object is an instance of ApiDiagnostic.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApiDiagnostic {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApiDiagnostic.__pulumiType;
    }

    /**
     * Specifies for what type of messages sampling settings should not apply.
     */
    public readonly alwaysLog!: pulumi.Output<string | undefined>;
    /**
     * Diagnostic settings for incoming/outgoing HTTP messages to the Backend
     */
    public readonly backend!: pulumi.Output<outputs.apimanagement.v20190101.PipelineDiagnosticSettingsResponse | undefined>;
    /**
     * Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.
     */
    public readonly enableHttpCorrelationHeaders!: pulumi.Output<boolean | undefined>;
    /**
     * Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.
     */
    public readonly frontend!: pulumi.Output<outputs.apimanagement.v20190101.PipelineDiagnosticSettingsResponse | undefined>;
    /**
     * Sets correlation protocol to use for Application Insights diagnostics.
     */
    public readonly httpCorrelationProtocol!: pulumi.Output<string | undefined>;
    /**
     * Resource Id of a target logger.
     */
    public readonly loggerId!: pulumi.Output<string>;
    /**
     * Resource name.
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * Sampling settings for Diagnostic.
     */
    public readonly sampling!: pulumi.Output<outputs.apimanagement.v20190101.SamplingSettingsResponse | undefined>;
    /**
     * Resource type for API Management resource.
     */
    public /*out*/ readonly type!: pulumi.Output<string>;
    /**
     * The verbosity level applied to traces emitted by trace policies.
     */
    public readonly verbosity!: pulumi.Output<string | undefined>;

    /**
     * Create a ApiDiagnostic resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApiDiagnosticArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.apiId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'apiId'");
            }
            if ((!args || args.loggerId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'loggerId'");
            }
            if ((!args || args.resourceGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            resourceInputs["alwaysLog"] = args ? args.alwaysLog : undefined;
            resourceInputs["apiId"] = args ? args.apiId : undefined;
            resourceInputs["backend"] = args ? args.backend : undefined;
            resourceInputs["diagnosticId"] = args ? args.diagnosticId : undefined;
            resourceInputs["enableHttpCorrelationHeaders"] = args ? args.enableHttpCorrelationHeaders : undefined;
            resourceInputs["frontend"] = args ? args.frontend : undefined;
            resourceInputs["httpCorrelationProtocol"] = args ? args.httpCorrelationProtocol : undefined;
            resourceInputs["loggerId"] = args ? args.loggerId : undefined;
            resourceInputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            resourceInputs["sampling"] = args ? args.sampling : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["verbosity"] = args ? args.verbosity : undefined;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
        } else {
            resourceInputs["alwaysLog"] = undefined /*out*/;
            resourceInputs["backend"] = undefined /*out*/;
            resourceInputs["enableHttpCorrelationHeaders"] = undefined /*out*/;
            resourceInputs["frontend"] = undefined /*out*/;
            resourceInputs["httpCorrelationProtocol"] = undefined /*out*/;
            resourceInputs["loggerId"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["sampling"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
            resourceInputs["verbosity"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const aliasOpts = { aliases: [{ type: "azure-native:apimanagement:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20170301:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20180101:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20180601preview:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20191201:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20191201preview:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20200601preview:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20201201:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20210101preview:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20210401preview:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20210801:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20211201preview:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20220401preview:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20220801:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20220901preview:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20230301preview:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20230501preview:ApiDiagnostic" }, { type: "azure-native:apimanagement/v20230901preview:ApiDiagnostic" }] };
        opts = pulumi.mergeOptions(opts, aliasOpts);
        super(ApiDiagnostic.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ApiDiagnostic resource.
 */
export interface ApiDiagnosticArgs {
    /**
     * Specifies for what type of messages sampling settings should not apply.
     */
    alwaysLog?: pulumi.Input<string | enums.apimanagement.v20190101.AlwaysLog>;
    /**
     * API identifier. Must be unique in the current API Management service instance.
     */
    apiId: pulumi.Input<string>;
    /**
     * Diagnostic settings for incoming/outgoing HTTP messages to the Backend
     */
    backend?: pulumi.Input<inputs.apimanagement.v20190101.PipelineDiagnosticSettingsArgs>;
    /**
     * Diagnostic identifier. Must be unique in the current API Management service instance.
     */
    diagnosticId?: pulumi.Input<string>;
    /**
     * Whether to process Correlation Headers coming to Api Management Service. Only applicable to Application Insights diagnostics. Default is true.
     */
    enableHttpCorrelationHeaders?: pulumi.Input<boolean>;
    /**
     * Diagnostic settings for incoming/outgoing HTTP messages to the Gateway.
     */
    frontend?: pulumi.Input<inputs.apimanagement.v20190101.PipelineDiagnosticSettingsArgs>;
    /**
     * Sets correlation protocol to use for Application Insights diagnostics.
     */
    httpCorrelationProtocol?: pulumi.Input<string | enums.apimanagement.v20190101.HttpCorrelationProtocol>;
    /**
     * Resource Id of a target logger.
     */
    loggerId: pulumi.Input<string>;
    /**
     * The name of the resource group.
     */
    resourceGroupName: pulumi.Input<string>;
    /**
     * Sampling settings for Diagnostic.
     */
    sampling?: pulumi.Input<inputs.apimanagement.v20190101.SamplingSettingsArgs>;
    /**
     * The name of the API Management service.
     */
    serviceName: pulumi.Input<string>;
    /**
     * The verbosity level applied to traces emitted by trace policies.
     */
    verbosity?: pulumi.Input<string | enums.apimanagement.v20190101.Verbosity>;
}
