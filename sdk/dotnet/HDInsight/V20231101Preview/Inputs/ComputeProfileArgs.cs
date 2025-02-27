// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.HDInsight.V20231101Preview.Inputs
{

    /// <summary>
    /// The compute profile.
    /// </summary>
    public sealed class ComputeProfileArgs : global::Pulumi.ResourceArgs
    {
        [Input("nodes", required: true)]
        private InputList<Inputs.NodeProfileArgs>? _nodes;

        /// <summary>
        /// The nodes definitions.
        /// </summary>
        public InputList<Inputs.NodeProfileArgs> Nodes
        {
            get => _nodes ?? (_nodes = new InputList<Inputs.NodeProfileArgs>());
            set => _nodes = value;
        }

        public ComputeProfileArgs()
        {
        }
        public static new ComputeProfileArgs Empty => new ComputeProfileArgs();
    }
}
