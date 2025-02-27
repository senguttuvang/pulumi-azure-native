// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.AzureStackHCI.V20221215Preview
{
    public static class GetGuestAgent
    {
        /// <summary>
        /// Implements GuestAgent GET method.
        /// </summary>
        public static Task<GetGuestAgentResult> InvokeAsync(GetGuestAgentArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetGuestAgentResult>("azure-native:azurestackhci/v20221215preview:getGuestAgent", args ?? new GetGuestAgentArgs(), options.WithDefaults());

        /// <summary>
        /// Implements GuestAgent GET method.
        /// </summary>
        public static Output<GetGuestAgentResult> Invoke(GetGuestAgentInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetGuestAgentResult>("azure-native:azurestackhci/v20221215preview:getGuestAgent", args ?? new GetGuestAgentInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetGuestAgentArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the GuestAgent.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The name of the resource group. The name is case insensitive.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public string ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// Name of the vm.
        /// </summary>
        [Input("virtualMachineName", required: true)]
        public string VirtualMachineName { get; set; } = null!;

        public GetGuestAgentArgs()
        {
        }
        public static new GetGuestAgentArgs Empty => new GetGuestAgentArgs();
    }

    public sealed class GetGuestAgentInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the GuestAgent.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The name of the resource group. The name is case insensitive.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// Name of the vm.
        /// </summary>
        [Input("virtualMachineName", required: true)]
        public Input<string> VirtualMachineName { get; set; } = null!;

        public GetGuestAgentInvokeArgs()
        {
        }
        public static new GetGuestAgentInvokeArgs Empty => new GetGuestAgentInvokeArgs();
    }


    [OutputType]
    public sealed class GetGuestAgentResult
    {
        /// <summary>
        /// Username / Password Credentials to provision guest agent.
        /// </summary>
        public readonly Outputs.GuestCredentialResponse? Credentials;
        /// <summary>
        /// HTTP Proxy configuration for the VM.
        /// </summary>
        public readonly Outputs.HttpProxyConfigurationResponse? HttpProxyConfig;
        /// <summary>
        /// Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the resource
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The guest agent provisioning action.
        /// </summary>
        public readonly string? ProvisioningAction;
        /// <summary>
        /// The provisioning state.
        /// </summary>
        public readonly string ProvisioningState;
        /// <summary>
        /// The guest agent status.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// Azure Resource Manager metadata containing createdBy and modifiedBy information.
        /// </summary>
        public readonly Outputs.SystemDataResponse SystemData;
        /// <summary>
        /// The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GetGuestAgentResult(
            Outputs.GuestCredentialResponse? credentials,

            Outputs.HttpProxyConfigurationResponse? httpProxyConfig,

            string id,

            string name,

            string? provisioningAction,

            string provisioningState,

            string status,

            Outputs.SystemDataResponse systemData,

            string type)
        {
            Credentials = credentials;
            HttpProxyConfig = httpProxyConfig;
            Id = id;
            Name = name;
            ProvisioningAction = provisioningAction;
            ProvisioningState = provisioningState;
            Status = status;
            SystemData = systemData;
            Type = type;
        }
    }
}
