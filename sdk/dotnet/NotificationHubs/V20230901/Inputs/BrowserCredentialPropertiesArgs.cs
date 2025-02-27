// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.NotificationHubs.V20230901.Inputs
{

    /// <summary>
    /// Description of a NotificationHub BrowserCredential.
    /// </summary>
    public sealed class BrowserCredentialPropertiesArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Gets or sets web push subject.
        /// </summary>
        [Input("subject", required: true)]
        public Input<string> Subject { get; set; } = null!;

        /// <summary>
        /// Gets or sets VAPID private key.
        /// </summary>
        [Input("vapidPrivateKey", required: true)]
        public Input<string> VapidPrivateKey { get; set; } = null!;

        /// <summary>
        /// Gets or sets VAPID public key.
        /// </summary>
        [Input("vapidPublicKey", required: true)]
        public Input<string> VapidPublicKey { get; set; } = null!;

        public BrowserCredentialPropertiesArgs()
        {
        }
        public static new BrowserCredentialPropertiesArgs Empty => new BrowserCredentialPropertiesArgs();
    }
}
