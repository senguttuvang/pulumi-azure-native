// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.Logic.V20150201Preview.Outputs
{

    [OutputType]
    public sealed class WorkflowParameterResponse
    {
        /// <summary>
        /// Gets or sets the metadata.
        /// </summary>
        public readonly object? Metadata;
        /// <summary>
        /// Gets or sets the type.
        /// </summary>
        public readonly string? Type;
        /// <summary>
        /// Gets or sets the value.
        /// </summary>
        public readonly object? Value;

        [OutputConstructor]
        private WorkflowParameterResponse(
            object? metadata,

            string? type,

            object? value)
        {
            Metadata = metadata;
            Type = type;
            Value = value;
        }
    }
}
