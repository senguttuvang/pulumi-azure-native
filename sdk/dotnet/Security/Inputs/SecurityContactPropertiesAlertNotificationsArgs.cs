// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.Security.Inputs
{

    /// <summary>
    /// Defines whether to send email notifications about new security alerts
    /// </summary>
    public sealed class SecurityContactPropertiesAlertNotificationsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Defines the minimal alert severity which will be sent as email notifications
        /// </summary>
        [Input("minimalSeverity")]
        public InputUnion<string, Pulumi.AzureNative.Security.MinimalSeverity>? MinimalSeverity { get; set; }

        /// <summary>
        /// Defines if email notifications will be sent about new security alerts
        /// </summary>
        [Input("state")]
        public InputUnion<string, Pulumi.AzureNative.Security.State>? State { get; set; }

        public SecurityContactPropertiesAlertNotificationsArgs()
        {
        }
        public static new SecurityContactPropertiesAlertNotificationsArgs Empty => new SecurityContactPropertiesAlertNotificationsArgs();
    }
}
