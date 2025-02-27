// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.AppComplianceAutomation.V20221116Preview.Outputs
{

    /// <summary>
    /// Report's properties.
    /// </summary>
    [OutputType]
    public sealed class ReportPropertiesResponse
    {
        /// <summary>
        /// Report compliance status.
        /// </summary>
        public readonly Outputs.ReportComplianceStatusResponse ComplianceStatus;
        /// <summary>
        /// Report id in database.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Report last collection trigger time.
        /// </summary>
        public readonly string LastTriggerTime;
        /// <summary>
        /// Report next collection trigger time.
        /// </summary>
        public readonly string NextTriggerTime;
        /// <summary>
        /// Report offer Guid.
        /// </summary>
        public readonly string? OfferGuid;
        /// <summary>
        /// Azure lifecycle management
        /// </summary>
        public readonly string ProvisioningState;
        /// <summary>
        /// Report name.
        /// </summary>
        public readonly string ReportName;
        /// <summary>
        /// List of resource data.
        /// </summary>
        public readonly ImmutableArray<Outputs.ResourceMetadataResponse> Resources;
        /// <summary>
        /// Report status.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// List of subscription Ids.
        /// </summary>
        public readonly ImmutableArray<string> Subscriptions;
        /// <summary>
        /// Report's tenant id.
        /// </summary>
        public readonly string TenantId;
        /// <summary>
        /// Report collection trigger time's time zone, the available list can be obtained by executing "Get-TimeZone -ListAvailable" in PowerShell.
        /// An example of valid timezone id is "Pacific Standard Time".
        /// </summary>
        public readonly string TimeZone;
        /// <summary>
        /// Report collection trigger time.
        /// </summary>
        public readonly string TriggerTime;

        [OutputConstructor]
        private ReportPropertiesResponse(
            Outputs.ReportComplianceStatusResponse complianceStatus,

            string id,

            string lastTriggerTime,

            string nextTriggerTime,

            string? offerGuid,

            string provisioningState,

            string reportName,

            ImmutableArray<Outputs.ResourceMetadataResponse> resources,

            string status,

            ImmutableArray<string> subscriptions,

            string tenantId,

            string timeZone,

            string triggerTime)
        {
            ComplianceStatus = complianceStatus;
            Id = id;
            LastTriggerTime = lastTriggerTime;
            NextTriggerTime = nextTriggerTime;
            OfferGuid = offerGuid;
            ProvisioningState = provisioningState;
            ReportName = reportName;
            Resources = resources;
            Status = status;
            Subscriptions = subscriptions;
            TenantId = tenantId;
            TimeZone = timeZone;
            TriggerTime = triggerTime;
        }
    }
}
