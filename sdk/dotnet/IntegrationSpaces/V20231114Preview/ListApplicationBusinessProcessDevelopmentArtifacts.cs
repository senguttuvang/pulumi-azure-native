// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.IntegrationSpaces.V20231114Preview
{
    public static class ListApplicationBusinessProcessDevelopmentArtifacts
    {
        /// <summary>
        /// The list business process development artifacts action.
        /// </summary>
        public static Task<ListApplicationBusinessProcessDevelopmentArtifactsResult> InvokeAsync(ListApplicationBusinessProcessDevelopmentArtifactsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<ListApplicationBusinessProcessDevelopmentArtifactsResult>("azure-native:integrationspaces/v20231114preview:listApplicationBusinessProcessDevelopmentArtifacts", args ?? new ListApplicationBusinessProcessDevelopmentArtifactsArgs(), options.WithDefaults());

        /// <summary>
        /// The list business process development artifacts action.
        /// </summary>
        public static Output<ListApplicationBusinessProcessDevelopmentArtifactsResult> Invoke(ListApplicationBusinessProcessDevelopmentArtifactsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<ListApplicationBusinessProcessDevelopmentArtifactsResult>("azure-native:integrationspaces/v20231114preview:listApplicationBusinessProcessDevelopmentArtifacts", args ?? new ListApplicationBusinessProcessDevelopmentArtifactsInvokeArgs(), options.WithDefaults());
    }


    public sealed class ListApplicationBusinessProcessDevelopmentArtifactsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Application
        /// </summary>
        [Input("applicationName", required: true)]
        public string ApplicationName { get; set; } = null!;

        /// <summary>
        /// The name of the resource group. The name is case insensitive.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public string ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// The name of the space
        /// </summary>
        [Input("spaceName", required: true)]
        public string SpaceName { get; set; } = null!;

        public ListApplicationBusinessProcessDevelopmentArtifactsArgs()
        {
        }
        public static new ListApplicationBusinessProcessDevelopmentArtifactsArgs Empty => new ListApplicationBusinessProcessDevelopmentArtifactsArgs();
    }

    public sealed class ListApplicationBusinessProcessDevelopmentArtifactsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Application
        /// </summary>
        [Input("applicationName", required: true)]
        public Input<string> ApplicationName { get; set; } = null!;

        /// <summary>
        /// The name of the resource group. The name is case insensitive.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// The name of the space
        /// </summary>
        [Input("spaceName", required: true)]
        public Input<string> SpaceName { get; set; } = null!;

        public ListApplicationBusinessProcessDevelopmentArtifactsInvokeArgs()
        {
        }
        public static new ListApplicationBusinessProcessDevelopmentArtifactsInvokeArgs Empty => new ListApplicationBusinessProcessDevelopmentArtifactsInvokeArgs();
    }


    [OutputType]
    public sealed class ListApplicationBusinessProcessDevelopmentArtifactsResult
    {
        /// <summary>
        /// The list of the business process development artifact.
        /// </summary>
        public readonly ImmutableArray<Outputs.SaveOrGetBusinessProcessDevelopmentArtifactResponseResponse> Value;

        [OutputConstructor]
        private ListApplicationBusinessProcessDevelopmentArtifactsResult(ImmutableArray<Outputs.SaveOrGetBusinessProcessDevelopmentArtifactResponseResponse> value)
        {
            Value = value;
        }
    }
}
