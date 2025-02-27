// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.ContainerService.V20230602Preview.Inputs
{

    /// <summary>
    /// The security settings of an agent pool.
    /// </summary>
    public sealed class AgentPoolSecurityProfileArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// SSH access method of an agent pool.
        /// </summary>
        [Input("sshAccess")]
        public InputUnion<string, Pulumi.AzureNative.ContainerService.V20230602Preview.AgentPoolSSHAccess>? SshAccess { get; set; }

        public AgentPoolSecurityProfileArgs()
        {
        }
        public static new AgentPoolSecurityProfileArgs Empty => new AgentPoolSecurityProfileArgs();
    }
}
