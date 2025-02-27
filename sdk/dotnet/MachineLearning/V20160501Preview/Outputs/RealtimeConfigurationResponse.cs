// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.MachineLearning.V20160501Preview.Outputs
{

    /// <summary>
    /// Holds the available configuration options for an Azure ML web service endpoint.
    /// </summary>
    [OutputType]
    public sealed class RealtimeConfigurationResponse
    {
        /// <summary>
        /// Specifies the maximum concurrent calls that can be made to the web service. Minimum value: 4, Maximum value: 200.
        /// </summary>
        public readonly int? MaxConcurrentCalls;

        [OutputConstructor]
        private RealtimeConfigurationResponse(int? maxConcurrentCalls)
        {
            MaxConcurrentCalls = maxConcurrentCalls;
        }
    }
}
