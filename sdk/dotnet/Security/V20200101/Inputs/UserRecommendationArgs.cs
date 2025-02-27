// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.Security.V20200101.Inputs
{

    /// <summary>
    /// Represents a user that is recommended to be allowed for a certain rule
    /// </summary>
    public sealed class UserRecommendationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The recommendation action of the machine or rule
        /// </summary>
        [Input("recommendationAction")]
        public Input<string>? RecommendationAction { get; set; }

        /// <summary>
        /// Represents a user that is recommended to be allowed for a certain rule
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public UserRecommendationArgs()
        {
        }
        public static new UserRecommendationArgs Empty => new UserRecommendationArgs();
    }
}
