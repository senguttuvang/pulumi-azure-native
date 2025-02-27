// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * SIM group resource.
 */
export class SimGroup extends pulumi.CustomResource {
    /**
     * Get an existing SimGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SimGroup {
        return new SimGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'azure-native:mobilenetwork/v20220401preview:SimGroup';

    /**
     * Returns true if the given object is an instance of SimGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SimGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SimGroup.__pulumiType;
    }

    /**
     * The timestamp of resource creation (UTC).
     */
    public readonly createdAt!: pulumi.Output<string | undefined>;
    /**
     * The identity that created the resource.
     */
    public readonly createdBy!: pulumi.Output<string | undefined>;
    /**
     * The type of identity that created the resource.
     */
    public readonly createdByType!: pulumi.Output<string | undefined>;
    /**
     * A key to encrypt the SIM data that belongs to this SIM group.
     */
    public readonly encryptionKey!: pulumi.Output<outputs.mobilenetwork.v20220401preview.KeyVaultKeyResponse | undefined>;
    /**
     * The identity used to retrieve the encryption key from Azure key vault.
     */
    public readonly identity!: pulumi.Output<outputs.mobilenetwork.v20220401preview.ManagedServiceIdentityResponse | undefined>;
    /**
     * The timestamp of resource last modification (UTC)
     */
    public readonly lastModifiedAt!: pulumi.Output<string | undefined>;
    /**
     * The identity that last modified the resource.
     */
    public readonly lastModifiedBy!: pulumi.Output<string | undefined>;
    /**
     * The type of identity that last modified the resource.
     */
    public readonly lastModifiedByType!: pulumi.Output<string | undefined>;
    /**
     * The geo-location where the resource lives
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * Mobile network that this SIM belongs to
     */
    public readonly mobileNetwork!: pulumi.Output<outputs.mobilenetwork.v20220401preview.MobileNetworkResourceIdResponse | undefined>;
    /**
     * The name of the resource
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The provisioning state of the SIM group resource.
     */
    public /*out*/ readonly provisioningState!: pulumi.Output<string>;
    /**
     * Azure Resource Manager metadata containing createdBy and modifiedBy information.
     */
    public /*out*/ readonly systemData!: pulumi.Output<outputs.mobilenetwork.v20220401preview.SystemDataResponse>;
    /**
     * Resource tags.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
     */
    public /*out*/ readonly type!: pulumi.Output<string>;

    /**
     * Create a SimGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SimGroupArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.resourceGroupName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceGroupName'");
            }
            resourceInputs["createdAt"] = args ? args.createdAt : undefined;
            resourceInputs["createdBy"] = args ? args.createdBy : undefined;
            resourceInputs["createdByType"] = args ? args.createdByType : undefined;
            resourceInputs["encryptionKey"] = args ? args.encryptionKey : undefined;
            resourceInputs["identity"] = args ? args.identity : undefined;
            resourceInputs["lastModifiedAt"] = args ? args.lastModifiedAt : undefined;
            resourceInputs["lastModifiedBy"] = args ? args.lastModifiedBy : undefined;
            resourceInputs["lastModifiedByType"] = args ? args.lastModifiedByType : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["mobileNetwork"] = args ? args.mobileNetwork : undefined;
            resourceInputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            resourceInputs["simGroupName"] = args ? args.simGroupName : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["provisioningState"] = undefined /*out*/;
            resourceInputs["systemData"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
        } else {
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["createdBy"] = undefined /*out*/;
            resourceInputs["createdByType"] = undefined /*out*/;
            resourceInputs["encryptionKey"] = undefined /*out*/;
            resourceInputs["identity"] = undefined /*out*/;
            resourceInputs["lastModifiedAt"] = undefined /*out*/;
            resourceInputs["lastModifiedBy"] = undefined /*out*/;
            resourceInputs["lastModifiedByType"] = undefined /*out*/;
            resourceInputs["location"] = undefined /*out*/;
            resourceInputs["mobileNetwork"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["provisioningState"] = undefined /*out*/;
            resourceInputs["systemData"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const aliasOpts = { aliases: [{ type: "azure-native:mobilenetwork:SimGroup" }, { type: "azure-native:mobilenetwork/v20221101:SimGroup" }, { type: "azure-native:mobilenetwork/v20230601:SimGroup" }, { type: "azure-native:mobilenetwork/v20230901:SimGroup" }, { type: "azure-native:mobilenetwork/v20240201:SimGroup" }, { type: "azure-native:mobilenetwork/v20240401:SimGroup" }] };
        opts = pulumi.mergeOptions(opts, aliasOpts);
        super(SimGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a SimGroup resource.
 */
export interface SimGroupArgs {
    /**
     * The timestamp of resource creation (UTC).
     */
    createdAt?: pulumi.Input<string>;
    /**
     * The identity that created the resource.
     */
    createdBy?: pulumi.Input<string>;
    /**
     * The type of identity that created the resource.
     */
    createdByType?: pulumi.Input<string | enums.mobilenetwork.v20220401preview.CreatedByType>;
    /**
     * A key to encrypt the SIM data that belongs to this SIM group.
     */
    encryptionKey?: pulumi.Input<inputs.mobilenetwork.v20220401preview.KeyVaultKeyArgs>;
    /**
     * The identity used to retrieve the encryption key from Azure key vault.
     */
    identity?: pulumi.Input<inputs.mobilenetwork.v20220401preview.ManagedServiceIdentityArgs>;
    /**
     * The timestamp of resource last modification (UTC)
     */
    lastModifiedAt?: pulumi.Input<string>;
    /**
     * The identity that last modified the resource.
     */
    lastModifiedBy?: pulumi.Input<string>;
    /**
     * The type of identity that last modified the resource.
     */
    lastModifiedByType?: pulumi.Input<string | enums.mobilenetwork.v20220401preview.CreatedByType>;
    /**
     * The geo-location where the resource lives
     */
    location?: pulumi.Input<string>;
    /**
     * Mobile network that this SIM belongs to
     */
    mobileNetwork?: pulumi.Input<inputs.mobilenetwork.v20220401preview.MobileNetworkResourceIdArgs>;
    /**
     * The name of the resource group. The name is case insensitive.
     */
    resourceGroupName: pulumi.Input<string>;
    /**
     * The name of the SIM Group.
     */
    simGroupName?: pulumi.Input<string>;
    /**
     * Resource tags.
     */
    tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
