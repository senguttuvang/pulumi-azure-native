// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.ProviderHub.V20210901Preview.Inputs
{

    public sealed class ThrottlingMetricArgs : global::Pulumi.ResourceArgs
    {
        [Input("interval")]
        public Input<string>? Interval { get; set; }

        [Input("limit", required: true)]
        public Input<double> Limit { get; set; } = null!;

        [Input("type", required: true)]
        public InputUnion<string, Pulumi.AzureNative.ProviderHub.V20210901Preview.ThrottlingMetricType> Type { get; set; } = null!;

        public ThrottlingMetricArgs()
        {
        }
        public static new ThrottlingMetricArgs Empty => new ThrottlingMetricArgs();
    }
}
