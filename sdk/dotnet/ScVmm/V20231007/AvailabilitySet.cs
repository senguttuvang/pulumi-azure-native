// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.ScVmm.V20231007
{
    /// <summary>
    /// The AvailabilitySets resource definition.
    /// </summary>
    [AzureNativeResourceType("azure-native:scvmm/v20231007:AvailabilitySet")]
    public partial class AvailabilitySet : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Name of the availability set.
        /// </summary>
        [Output("availabilitySetName")]
        public Output<string?> AvailabilitySetName { get; private set; } = null!;

        /// <summary>
        /// The extended location.
        /// </summary>
        [Output("extendedLocation")]
        public Output<Outputs.ExtendedLocationResponse> ExtendedLocation { get; private set; } = null!;

        /// <summary>
        /// The geo-location where the resource lives
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// The name of the resource
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Provisioning state of the resource.
        /// </summary>
        [Output("provisioningState")]
        public Output<string> ProvisioningState { get; private set; } = null!;

        /// <summary>
        /// Azure Resource Manager metadata containing createdBy and modifiedBy information.
        /// </summary>
        [Output("systemData")]
        public Output<Outputs.SystemDataResponse> SystemData { get; private set; } = null!;

        /// <summary>
        /// Resource tags.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;

        /// <summary>
        /// The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;

        /// <summary>
        /// ARM Id of the vmmServer resource in which this resource resides.
        /// </summary>
        [Output("vmmServerId")]
        public Output<string?> VmmServerId { get; private set; } = null!;


        /// <summary>
        /// Create a AvailabilitySet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AvailabilitySet(string name, AvailabilitySetArgs args, CustomResourceOptions? options = null)
            : base("azure-native:scvmm/v20231007:AvailabilitySet", name, args ?? new AvailabilitySetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AvailabilitySet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("azure-native:scvmm/v20231007:AvailabilitySet", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                Aliases =
                {
                    new global::Pulumi.Alias { Type = "azure-native:scvmm:AvailabilitySet" },
                    new global::Pulumi.Alias { Type = "azure-native:scvmm/v20200605preview:AvailabilitySet" },
                    new global::Pulumi.Alias { Type = "azure-native:scvmm/v20220521preview:AvailabilitySet" },
                    new global::Pulumi.Alias { Type = "azure-native:scvmm/v20230401preview:AvailabilitySet" },
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AvailabilitySet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AvailabilitySet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new AvailabilitySet(name, id, options);
        }
    }

    public sealed class AvailabilitySetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the availability set.
        /// </summary>
        [Input("availabilitySetName")]
        public Input<string>? AvailabilitySetName { get; set; }

        /// <summary>
        /// Name of the AvailabilitySet.
        /// </summary>
        [Input("availabilitySetResourceName")]
        public Input<string>? AvailabilitySetResourceName { get; set; }

        /// <summary>
        /// The extended location.
        /// </summary>
        [Input("extendedLocation", required: true)]
        public Input<Inputs.ExtendedLocationArgs> ExtendedLocation { get; set; } = null!;

        /// <summary>
        /// The geo-location where the resource lives
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// The name of the resource group. The name is case insensitive.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// Resource tags.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        /// <summary>
        /// ARM Id of the vmmServer resource in which this resource resides.
        /// </summary>
        [Input("vmmServerId")]
        public Input<string>? VmmServerId { get; set; }

        public AvailabilitySetArgs()
        {
        }
        public static new AvailabilitySetArgs Empty => new AvailabilitySetArgs();
    }
}
