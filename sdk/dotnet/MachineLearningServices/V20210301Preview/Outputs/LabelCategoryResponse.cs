// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.MachineLearningServices.V20210301Preview.Outputs
{

    /// <summary>
    /// Label category definition
    /// </summary>
    [OutputType]
    public sealed class LabelCategoryResponse
    {
        /// <summary>
        /// Indicates whether it is allowed to select multiple classes in this category.
        /// </summary>
        public readonly bool? AllowMultiSelect;
        /// <summary>
        /// Dictionary of label classes in this category.
        /// </summary>
        public readonly ImmutableDictionary<string, Outputs.LabelClassResponse>? Classes;
        /// <summary>
        /// Display name of the label category.
        /// </summary>
        public readonly string? DisplayName;

        [OutputConstructor]
        private LabelCategoryResponse(
            bool? allowMultiSelect,

            ImmutableDictionary<string, Outputs.LabelClassResponse>? classes,

            string? displayName)
        {
            AllowMultiSelect = allowMultiSelect;
            Classes = classes;
            DisplayName = displayName;
        }
    }
}
