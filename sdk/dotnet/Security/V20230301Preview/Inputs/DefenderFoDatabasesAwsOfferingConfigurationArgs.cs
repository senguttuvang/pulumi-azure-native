// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.Security.V20230301Preview.Inputs
{

    /// <summary>
    /// Configuration for servers Arc auto provisioning
    /// </summary>
    public sealed class DefenderFoDatabasesAwsOfferingConfigurationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional Arc private link scope resource id to link the Arc agent
        /// </summary>
        [Input("privateLinkScope")]
        public Input<string>? PrivateLinkScope { get; set; }

        /// <summary>
        /// Optional http proxy endpoint to use for the Arc agent
        /// </summary>
        [Input("proxy")]
        public Input<string>? Proxy { get; set; }

        public DefenderFoDatabasesAwsOfferingConfigurationArgs()
        {
        }
        public static new DefenderFoDatabasesAwsOfferingConfigurationArgs Empty => new DefenderFoDatabasesAwsOfferingConfigurationArgs();
    }
}
