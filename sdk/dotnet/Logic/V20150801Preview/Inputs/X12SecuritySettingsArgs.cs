// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.Logic.V20150801Preview.Inputs
{

    public sealed class X12SecuritySettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The authorization qualifier.
        /// </summary>
        [Input("authorizationQualifier")]
        public Input<string>? AuthorizationQualifier { get; set; }

        /// <summary>
        /// The authorization value.
        /// </summary>
        [Input("authorizationValue")]
        public Input<string>? AuthorizationValue { get; set; }

        /// <summary>
        /// The password value.
        /// </summary>
        [Input("passwordValue")]
        public Input<string>? PasswordValue { get; set; }

        /// <summary>
        /// The security qualifier.
        /// </summary>
        [Input("securityQualifier")]
        public Input<string>? SecurityQualifier { get; set; }

        public X12SecuritySettingsArgs()
        {
        }
        public static new X12SecuritySettingsArgs Empty => new X12SecuritySettingsArgs();
    }
}
