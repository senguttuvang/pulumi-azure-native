// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.Migrate.V20230101.Inputs
{

    /// <summary>
    /// Class for solution properties.
    /// </summary>
    public sealed class SolutionPropertiesArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Gets or sets the cleanup state of the solution.
        /// </summary>
        [Input("cleanupState")]
        public InputUnion<string, Pulumi.AzureNative.Migrate.V20230101.CleanupState>? CleanupState { get; set; }

        /// <summary>
        /// Gets or sets the details of the solution.
        /// </summary>
        [Input("details")]
        public Input<Inputs.SolutionDetailsArgs>? Details { get; set; }

        /// <summary>
        /// Gets or sets the goal of the solution.
        /// </summary>
        [Input("goal")]
        public InputUnion<string, Pulumi.AzureNative.Migrate.V20230101.Goal>? Goal { get; set; }

        /// <summary>
        /// Gets or sets the purpose of the solution.
        /// </summary>
        [Input("purpose")]
        public InputUnion<string, Pulumi.AzureNative.Migrate.V20230101.Purpose>? Purpose { get; set; }

        /// <summary>
        /// Gets or sets the current status of the solution.
        /// </summary>
        [Input("status")]
        public InputUnion<string, Pulumi.AzureNative.Migrate.V20230101.Status>? Status { get; set; }

        /// <summary>
        /// Gets or sets the tool being used in the solution.
        /// </summary>
        [Input("tool")]
        public InputUnion<string, Pulumi.AzureNative.Migrate.V20230101.Tool>? Tool { get; set; }

        public SolutionPropertiesArgs()
        {
        }
        public static new SolutionPropertiesArgs Empty => new SolutionPropertiesArgs();
    }
}
