// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.Network.V20200601
{
    public static class GetVirtualHub
    {
        /// <summary>
        /// Retrieves the details of a VirtualHub.
        /// </summary>
        public static Task<GetVirtualHubResult> InvokeAsync(GetVirtualHubArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVirtualHubResult>("azure-native:network/v20200601:getVirtualHub", args ?? new GetVirtualHubArgs(), options.WithDefaults());

        /// <summary>
        /// Retrieves the details of a VirtualHub.
        /// </summary>
        public static Output<GetVirtualHubResult> Invoke(GetVirtualHubInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVirtualHubResult>("azure-native:network/v20200601:getVirtualHub", args ?? new GetVirtualHubInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVirtualHubArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The resource group name of the VirtualHub.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public string ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// The name of the VirtualHub.
        /// </summary>
        [Input("virtualHubName", required: true)]
        public string VirtualHubName { get; set; } = null!;

        public GetVirtualHubArgs()
        {
        }
        public static new GetVirtualHubArgs Empty => new GetVirtualHubArgs();
    }

    public sealed class GetVirtualHubInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The resource group name of the VirtualHub.
        /// </summary>
        [Input("resourceGroupName", required: true)]
        public Input<string> ResourceGroupName { get; set; } = null!;

        /// <summary>
        /// The name of the VirtualHub.
        /// </summary>
        [Input("virtualHubName", required: true)]
        public Input<string> VirtualHubName { get; set; } = null!;

        public GetVirtualHubInvokeArgs()
        {
        }
        public static new GetVirtualHubInvokeArgs Empty => new GetVirtualHubInvokeArgs();
    }


    [OutputType]
    public sealed class GetVirtualHubResult
    {
        /// <summary>
        /// Address-prefix for this VirtualHub.
        /// </summary>
        public readonly string? AddressPrefix;
        /// <summary>
        /// The azureFirewall associated with this VirtualHub.
        /// </summary>
        public readonly Outputs.SubResourceResponse? AzureFirewall;
        /// <summary>
        /// List of references to Bgp Connections.
        /// </summary>
        public readonly ImmutableArray<Outputs.SubResourceResponse> BgpConnections;
        /// <summary>
        /// Flag to control route propogation for VirtualRouter hub.
        /// </summary>
        public readonly bool? EnableVirtualRouterRoutePropogation;
        /// <summary>
        /// A unique read-only string that changes whenever the resource is updated.
        /// </summary>
        public readonly string Etag;
        /// <summary>
        /// The expressRouteGateway associated with this VirtualHub.
        /// </summary>
        public readonly Outputs.SubResourceResponse? ExpressRouteGateway;
        /// <summary>
        /// Resource ID.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// List of references to IpConfigurations.
        /// </summary>
        public readonly ImmutableArray<Outputs.SubResourceResponse> IpConfigurations;
        /// <summary>
        /// Resource location.
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// Resource name.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The P2SVpnGateway associated with this VirtualHub.
        /// </summary>
        public readonly Outputs.SubResourceResponse? P2SVpnGateway;
        /// <summary>
        /// The provisioning state of the virtual hub resource.
        /// </summary>
        public readonly string ProvisioningState;
        /// <summary>
        /// The routeTable associated with this virtual hub.
        /// </summary>
        public readonly Outputs.VirtualHubRouteTableResponse? RouteTable;
        /// <summary>
        /// The routing state.
        /// </summary>
        public readonly string RoutingState;
        /// <summary>
        /// The securityPartnerProvider associated with this VirtualHub.
        /// </summary>
        public readonly Outputs.SubResourceResponse? SecurityPartnerProvider;
        /// <summary>
        /// The Security Provider name.
        /// </summary>
        public readonly string? SecurityProviderName;
        /// <summary>
        /// The sku of this VirtualHub.
        /// </summary>
        public readonly string? Sku;
        /// <summary>
        /// Resource tags.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Tags;
        /// <summary>
        /// Resource type.
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// List of all virtual hub route table v2s associated with this VirtualHub.
        /// </summary>
        public readonly ImmutableArray<Outputs.VirtualHubRouteTableV2Response> VirtualHubRouteTableV2s;
        /// <summary>
        /// VirtualRouter ASN.
        /// </summary>
        public readonly double? VirtualRouterAsn;
        /// <summary>
        /// VirtualRouter IPs.
        /// </summary>
        public readonly ImmutableArray<string> VirtualRouterIps;
        /// <summary>
        /// The VirtualWAN to which the VirtualHub belongs.
        /// </summary>
        public readonly Outputs.SubResourceResponse? VirtualWan;
        /// <summary>
        /// The VpnGateway associated with this VirtualHub.
        /// </summary>
        public readonly Outputs.SubResourceResponse? VpnGateway;

        [OutputConstructor]
        private GetVirtualHubResult(
            string? addressPrefix,

            Outputs.SubResourceResponse? azureFirewall,

            ImmutableArray<Outputs.SubResourceResponse> bgpConnections,

            bool? enableVirtualRouterRoutePropogation,

            string etag,

            Outputs.SubResourceResponse? expressRouteGateway,

            string? id,

            ImmutableArray<Outputs.SubResourceResponse> ipConfigurations,

            string location,

            string name,

            Outputs.SubResourceResponse? p2SVpnGateway,

            string provisioningState,

            Outputs.VirtualHubRouteTableResponse? routeTable,

            string routingState,

            Outputs.SubResourceResponse? securityPartnerProvider,

            string? securityProviderName,

            string? sku,

            ImmutableDictionary<string, string>? tags,

            string type,

            ImmutableArray<Outputs.VirtualHubRouteTableV2Response> virtualHubRouteTableV2s,

            double? virtualRouterAsn,

            ImmutableArray<string> virtualRouterIps,

            Outputs.SubResourceResponse? virtualWan,

            Outputs.SubResourceResponse? vpnGateway)
        {
            AddressPrefix = addressPrefix;
            AzureFirewall = azureFirewall;
            BgpConnections = bgpConnections;
            EnableVirtualRouterRoutePropogation = enableVirtualRouterRoutePropogation;
            Etag = etag;
            ExpressRouteGateway = expressRouteGateway;
            Id = id;
            IpConfigurations = ipConfigurations;
            Location = location;
            Name = name;
            P2SVpnGateway = p2SVpnGateway;
            ProvisioningState = provisioningState;
            RouteTable = routeTable;
            RoutingState = routingState;
            SecurityPartnerProvider = securityPartnerProvider;
            SecurityProviderName = securityProviderName;
            Sku = sku;
            Tags = tags;
            Type = type;
            VirtualHubRouteTableV2s = virtualHubRouteTableV2s;
            VirtualRouterAsn = virtualRouterAsn;
            VirtualRouterIps = virtualRouterIps;
            VirtualWan = virtualWan;
            VpnGateway = vpnGateway;
        }
    }
}
