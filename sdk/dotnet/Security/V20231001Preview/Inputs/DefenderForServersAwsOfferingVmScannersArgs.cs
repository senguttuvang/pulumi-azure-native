// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.Security.V20231001Preview.Inputs
{

    /// <summary>
    /// The Microsoft Defender for Server VM scanning configuration
    /// </summary>
    public sealed class DefenderForServersAwsOfferingVmScannersArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// configuration for Microsoft Defender for Server VM scanning
        /// </summary>
        [Input("configuration")]
        public Input<Inputs.DefenderForServersAwsOfferingConfigurationConfigurationConfigurationArgs>? Configuration { get; set; }

        /// <summary>
        /// Is Microsoft Defender for Server VM scanning enabled
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        public DefenderForServersAwsOfferingVmScannersArgs()
        {
        }
        public static new DefenderForServersAwsOfferingVmScannersArgs Empty => new DefenderForServersAwsOfferingVmScannersArgs();
    }
}
