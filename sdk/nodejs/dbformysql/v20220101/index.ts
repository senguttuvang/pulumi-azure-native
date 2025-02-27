// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

// Export members:
export { AzureADAdministratorArgs } from "./azureADAdministrator";
export type AzureADAdministrator = import("./azureADAdministrator").AzureADAdministrator;
export const AzureADAdministrator: typeof import("./azureADAdministrator").AzureADAdministrator = null as any;
utilities.lazyLoad(exports, ["AzureADAdministrator"], () => require("./azureADAdministrator"));

export { ConfigurationArgs } from "./configuration";
export type Configuration = import("./configuration").Configuration;
export const Configuration: typeof import("./configuration").Configuration = null as any;
utilities.lazyLoad(exports, ["Configuration"], () => require("./configuration"));

export { DatabaseArgs } from "./database";
export type Database = import("./database").Database;
export const Database: typeof import("./database").Database = null as any;
utilities.lazyLoad(exports, ["Database"], () => require("./database"));

export { FirewallRuleArgs } from "./firewallRule";
export type FirewallRule = import("./firewallRule").FirewallRule;
export const FirewallRule: typeof import("./firewallRule").FirewallRule = null as any;
utilities.lazyLoad(exports, ["FirewallRule"], () => require("./firewallRule"));

export { GetAzureADAdministratorArgs, GetAzureADAdministratorResult, GetAzureADAdministratorOutputArgs } from "./getAzureADAdministrator";
export const getAzureADAdministrator: typeof import("./getAzureADAdministrator").getAzureADAdministrator = null as any;
export const getAzureADAdministratorOutput: typeof import("./getAzureADAdministrator").getAzureADAdministratorOutput = null as any;
utilities.lazyLoad(exports, ["getAzureADAdministrator","getAzureADAdministratorOutput"], () => require("./getAzureADAdministrator"));

export { GetConfigurationArgs, GetConfigurationResult, GetConfigurationOutputArgs } from "./getConfiguration";
export const getConfiguration: typeof import("./getConfiguration").getConfiguration = null as any;
export const getConfigurationOutput: typeof import("./getConfiguration").getConfigurationOutput = null as any;
utilities.lazyLoad(exports, ["getConfiguration","getConfigurationOutput"], () => require("./getConfiguration"));

export { GetDatabaseArgs, GetDatabaseResult, GetDatabaseOutputArgs } from "./getDatabase";
export const getDatabase: typeof import("./getDatabase").getDatabase = null as any;
export const getDatabaseOutput: typeof import("./getDatabase").getDatabaseOutput = null as any;
utilities.lazyLoad(exports, ["getDatabase","getDatabaseOutput"], () => require("./getDatabase"));

export { GetFirewallRuleArgs, GetFirewallRuleResult, GetFirewallRuleOutputArgs } from "./getFirewallRule";
export const getFirewallRule: typeof import("./getFirewallRule").getFirewallRule = null as any;
export const getFirewallRuleOutput: typeof import("./getFirewallRule").getFirewallRuleOutput = null as any;
utilities.lazyLoad(exports, ["getFirewallRule","getFirewallRuleOutput"], () => require("./getFirewallRule"));

export { GetGetPrivateDnsZoneSuffixExecuteArgs, GetGetPrivateDnsZoneSuffixExecuteResult } from "./getGetPrivateDnsZoneSuffixExecute";
export const getGetPrivateDnsZoneSuffixExecute: typeof import("./getGetPrivateDnsZoneSuffixExecute").getGetPrivateDnsZoneSuffixExecute = null as any;
export const getGetPrivateDnsZoneSuffixExecuteOutput: typeof import("./getGetPrivateDnsZoneSuffixExecute").getGetPrivateDnsZoneSuffixExecuteOutput = null as any;
utilities.lazyLoad(exports, ["getGetPrivateDnsZoneSuffixExecute","getGetPrivateDnsZoneSuffixExecuteOutput"], () => require("./getGetPrivateDnsZoneSuffixExecute"));

export { GetServerArgs, GetServerResult, GetServerOutputArgs } from "./getServer";
export const getServer: typeof import("./getServer").getServer = null as any;
export const getServerOutput: typeof import("./getServer").getServerOutput = null as any;
utilities.lazyLoad(exports, ["getServer","getServerOutput"], () => require("./getServer"));

export { ServerArgs } from "./server";
export type Server = import("./server").Server;
export const Server: typeof import("./server").Server = null as any;
utilities.lazyLoad(exports, ["Server"], () => require("./server"));


// Export enums:
export * from "../../types/enums/dbformysql/v20220101";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "azure-native:dbformysql/v20220101:AzureADAdministrator":
                return new AzureADAdministrator(name, <any>undefined, { urn })
            case "azure-native:dbformysql/v20220101:Configuration":
                return new Configuration(name, <any>undefined, { urn })
            case "azure-native:dbformysql/v20220101:Database":
                return new Database(name, <any>undefined, { urn })
            case "azure-native:dbformysql/v20220101:FirewallRule":
                return new FirewallRule(name, <any>undefined, { urn })
            case "azure-native:dbformysql/v20220101:Server":
                return new Server(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("azure-native", "dbformysql/v20220101", _module)
