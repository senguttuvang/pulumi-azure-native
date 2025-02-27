// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.Search.V20240301Preview.Outputs
{

    /// <summary>
    /// Details about the search service identity. A null value indicates that the search service has no identity assigned.
    /// </summary>
    [OutputType]
    public sealed class IdentityResponse
    {
        /// <summary>
        /// The principal ID of the system-assigned identity of the search service.
        /// </summary>
        public readonly string PrincipalId;
        /// <summary>
        /// The tenant ID of the system-assigned identity of the search service.
        /// </summary>
        public readonly string TenantId;
        /// <summary>
        /// The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes both an identity created by the system and a set of user assigned identities. The type 'None' will remove all identities from the service.
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource IDs in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        /// </summary>
        public readonly ImmutableDictionary<string, Outputs.UserAssignedManagedIdentityResponse>? UserAssignedIdentities;

        [OutputConstructor]
        private IdentityResponse(
            string principalId,

            string tenantId,

            string type,

            ImmutableDictionary<string, Outputs.UserAssignedManagedIdentityResponse>? userAssignedIdentities)
        {
            PrincipalId = principalId;
            TenantId = tenantId;
            Type = type;
            UserAssignedIdentities = userAssignedIdentities;
        }
    }
}
