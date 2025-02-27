// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.Billing.Outputs
{

    /// <summary>
    /// Details of the Azure plan.
    /// </summary>
    [OutputType]
    public sealed class AzurePlanResponse
    {
        /// <summary>
        /// The sku description.
        /// </summary>
        public readonly string SkuDescription;
        /// <summary>
        /// The sku id.
        /// </summary>
        public readonly string? SkuId;

        [OutputConstructor]
        private AzurePlanResponse(
            string skuDescription,

            string? skuId)
        {
            SkuDescription = skuDescription;
            SkuId = skuId;
        }
    }
}
