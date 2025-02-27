// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.Web.V20190801.Inputs
{

    /// <summary>
    /// Network access control entry.
    /// </summary>
    public sealed class NetworkAccessControlEntryArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Action object.
        /// </summary>
        [Input("action")]
        public Input<Pulumi.AzureNative.Web.V20190801.AccessControlEntryAction>? Action { get; set; }

        /// <summary>
        /// Description of network access control entry.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Order of precedence.
        /// </summary>
        [Input("order")]
        public Input<int>? Order { get; set; }

        /// <summary>
        /// Remote subnet.
        /// </summary>
        [Input("remoteSubnet")]
        public Input<string>? RemoteSubnet { get; set; }

        public NetworkAccessControlEntryArgs()
        {
        }
        public static new NetworkAccessControlEntryArgs Empty => new NetworkAccessControlEntryArgs();
    }
}
