// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.MachineLearningServices.V20240101Preview.Inputs
{

    /// <summary>
    /// Monitoring workspace connection definition.
    /// </summary>
    public sealed class MonitoringWorkspaceConnectionArgs : global::Pulumi.ResourceArgs
    {
        [Input("environmentVariables")]
        private InputMap<string>? _environmentVariables;

        /// <summary>
        /// The properties of a workspace service connection to store as environment variables in the submitted jobs.
        /// Key is workspace connection property path, name is environment variable key.
        /// </summary>
        public InputMap<string> EnvironmentVariables
        {
            get => _environmentVariables ?? (_environmentVariables = new InputMap<string>());
            set => _environmentVariables = value;
        }

        [Input("secrets")]
        private InputMap<string>? _secrets;

        /// <summary>
        /// The properties of a workspace service connection to store as secrets in the submitted jobs.
        /// Key is workspace connection property path, name is secret key.
        /// </summary>
        public InputMap<string> Secrets
        {
            get => _secrets ?? (_secrets = new InputMap<string>());
            set => _secrets = value;
        }

        public MonitoringWorkspaceConnectionArgs()
        {
        }
        public static new MonitoringWorkspaceConnectionArgs Empty => new MonitoringWorkspaceConnectionArgs();
    }
}
