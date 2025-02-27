// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// Export sub-modules:
import * as v20230201 from "./v20230201";
import * as v20230301preview from "./v20230301preview";
import * as v20230601preview from "./v20230601preview";
import * as v20230801preview from "./v20230801preview";
import * as v20240101preview from "./v20240101preview";
import * as v20240301 from "./v20240301";

export {
    v20230201,
    v20230301preview,
    v20230601preview,
    v20230801preview,
    v20240101preview,
    v20240301,
};

export const ACLAction = {
    Allow: "Allow",
    Deny: "Deny",
} as const;

/**
 * Azure Networking ACL Action.
 */
export type ACLAction = (typeof ACLAction)[keyof typeof ACLAction];

export const FeatureFlags = {
    ServiceMode: "ServiceMode",
    EnableConnectivityLogs: "EnableConnectivityLogs",
    EnableMessagingLogs: "EnableMessagingLogs",
    EnableLiveTrace: "EnableLiveTrace",
} as const;

/**
 * FeatureFlags is the supported features of Azure SignalR service.
 * - ServiceMode: Flag for backend server for SignalR service. Values allowed: "Default": have your own backend server; "Serverless": your application doesn't have a backend server; "Classic": for backward compatibility. Support both Default and Serverless mode but not recommended; "PredefinedOnly": for future use.
 * - EnableConnectivityLogs: "true"/"false", to enable/disable the connectivity log category respectively.
 * - EnableMessagingLogs: "true"/"false", to enable/disable the connectivity log category respectively.
 * - EnableLiveTrace: Live Trace allows you to know what's happening inside Azure SignalR service, it will give you live traces in real time, it will be helpful when you developing your own Azure SignalR based web application or self-troubleshooting some issues. Please note that live traces are counted as outbound messages that will be charged. Values allowed: "true"/"false", to enable/disable live trace feature.
 */
export type FeatureFlags = (typeof FeatureFlags)[keyof typeof FeatureFlags];

export const ManagedIdentityType = {
    None: "None",
    SystemAssigned: "SystemAssigned",
    UserAssigned: "UserAssigned",
} as const;

/**
 * Represents the identity type: systemAssigned, userAssigned, None
 */
export type ManagedIdentityType = (typeof ManagedIdentityType)[keyof typeof ManagedIdentityType];

export const PrivateLinkServiceConnectionStatus = {
    Pending: "Pending",
    Approved: "Approved",
    Rejected: "Rejected",
    Disconnected: "Disconnected",
} as const;

/**
 * Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
 */
export type PrivateLinkServiceConnectionStatus = (typeof PrivateLinkServiceConnectionStatus)[keyof typeof PrivateLinkServiceConnectionStatus];

export const ServiceKind = {
    SignalR: "SignalR",
    RawWebSockets: "RawWebSockets",
} as const;

/**
 * The kind of the service, it can be SignalR or RawWebSockets
 */
export type ServiceKind = (typeof ServiceKind)[keyof typeof ServiceKind];

export const SignalRRequestType = {
    ClientConnection: "ClientConnection",
    ServerConnection: "ServerConnection",
    RESTAPI: "RESTAPI",
    Trace: "Trace",
} as const;

/**
 * The incoming request type to the service
 */
export type SignalRRequestType = (typeof SignalRRequestType)[keyof typeof SignalRRequestType];

export const SignalRSkuTier = {
    Free: "Free",
    Basic: "Basic",
    Standard: "Standard",
    Premium: "Premium",
} as const;

/**
 * Optional tier of this particular SKU. 'Standard' or 'Free'. 
 * 
 * `Basic` is deprecated, use `Standard` instead.
 */
export type SignalRSkuTier = (typeof SignalRSkuTier)[keyof typeof SignalRSkuTier];

export const UpstreamAuthType = {
    None: "None",
    ManagedIdentity: "ManagedIdentity",
} as const;

/**
 * Upstream auth type enum.
 */
export type UpstreamAuthType = (typeof UpstreamAuthType)[keyof typeof UpstreamAuthType];
