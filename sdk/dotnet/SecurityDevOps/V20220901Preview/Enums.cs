// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AzureNative.SecurityDevOps.V20220901Preview
{
    [EnumType]
    public readonly struct AutoDiscovery : IEquatable<AutoDiscovery>
    {
        private readonly string _value;

        private AutoDiscovery(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static AutoDiscovery Disabled { get; } = new AutoDiscovery("Disabled");
        public static AutoDiscovery Enabled { get; } = new AutoDiscovery("Enabled");

        public static bool operator ==(AutoDiscovery left, AutoDiscovery right) => left.Equals(right);
        public static bool operator !=(AutoDiscovery left, AutoDiscovery right) => !left.Equals(right);

        public static explicit operator string(AutoDiscovery value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is AutoDiscovery other && Equals(other);
        public bool Equals(AutoDiscovery other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
