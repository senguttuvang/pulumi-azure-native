// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AzureNative.Logic.V20150801Preview.Inputs
{

    public sealed class EdifactProtocolSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The EDIFACT acknowledgement settings.
        /// </summary>
        [Input("acknowledgementSettings")]
        public Input<Inputs.EdifactAcknowledgementSettingsArgs>? AcknowledgementSettings { get; set; }

        [Input("edifactDelimiterOverrides")]
        private InputList<Inputs.EdifactDelimiterOverrideArgs>? _edifactDelimiterOverrides;

        /// <summary>
        /// The EDIFACT delimiter override settings.
        /// </summary>
        public InputList<Inputs.EdifactDelimiterOverrideArgs> EdifactDelimiterOverrides
        {
            get => _edifactDelimiterOverrides ?? (_edifactDelimiterOverrides = new InputList<Inputs.EdifactDelimiterOverrideArgs>());
            set => _edifactDelimiterOverrides = value;
        }

        [Input("envelopeOverrides")]
        private InputList<Inputs.EdifactEnvelopeOverrideArgs>? _envelopeOverrides;

        /// <summary>
        /// The EDIFACT envelope override settings.
        /// </summary>
        public InputList<Inputs.EdifactEnvelopeOverrideArgs> EnvelopeOverrides
        {
            get => _envelopeOverrides ?? (_envelopeOverrides = new InputList<Inputs.EdifactEnvelopeOverrideArgs>());
            set => _envelopeOverrides = value;
        }

        /// <summary>
        /// The EDIFACT envelope settings.
        /// </summary>
        [Input("envelopeSettings")]
        public Input<Inputs.EdifactEnvelopeSettingsArgs>? EnvelopeSettings { get; set; }

        /// <summary>
        /// The EDIFACT framing settings.
        /// </summary>
        [Input("framingSettings")]
        public Input<Inputs.EdifactFramingSettingsArgs>? FramingSettings { get; set; }

        /// <summary>
        /// The EDIFACT message filter.
        /// </summary>
        [Input("messageFilter")]
        public Input<Inputs.EdifactMessageFilterArgs>? MessageFilter { get; set; }

        [Input("messageFilterList")]
        private InputList<Inputs.EdifactMessageIdentifierArgs>? _messageFilterList;

        /// <summary>
        /// The EDIFACT message filter list.
        /// </summary>
        public InputList<Inputs.EdifactMessageIdentifierArgs> MessageFilterList
        {
            get => _messageFilterList ?? (_messageFilterList = new InputList<Inputs.EdifactMessageIdentifierArgs>());
            set => _messageFilterList = value;
        }

        /// <summary>
        /// The EDIFACT processing Settings.
        /// </summary>
        [Input("processingSettings")]
        public Input<Inputs.EdifactProcessingSettingsArgs>? ProcessingSettings { get; set; }

        [Input("schemaReferences")]
        private InputList<Inputs.EdifactSchemaReferenceArgs>? _schemaReferences;

        /// <summary>
        /// The EDIFACT schema references.
        /// </summary>
        public InputList<Inputs.EdifactSchemaReferenceArgs> SchemaReferences
        {
            get => _schemaReferences ?? (_schemaReferences = new InputList<Inputs.EdifactSchemaReferenceArgs>());
            set => _schemaReferences = value;
        }

        [Input("validationOverrides")]
        private InputList<Inputs.EdifactValidationOverrideArgs>? _validationOverrides;

        /// <summary>
        /// The EDIFACT validation override settings.
        /// </summary>
        public InputList<Inputs.EdifactValidationOverrideArgs> ValidationOverrides
        {
            get => _validationOverrides ?? (_validationOverrides = new InputList<Inputs.EdifactValidationOverrideArgs>());
            set => _validationOverrides = value;
        }

        /// <summary>
        /// The EDIFACT validation settings.
        /// </summary>
        [Input("validationSettings")]
        public Input<Inputs.EdifactValidationSettingsArgs>? ValidationSettings { get; set; }

        public EdifactProtocolSettingsArgs()
        {
        }
        public static new EdifactProtocolSettingsArgs Empty => new EdifactProtocolSettingsArgs();
    }
}
