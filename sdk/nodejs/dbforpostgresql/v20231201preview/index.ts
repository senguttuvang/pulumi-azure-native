// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../../utilities";

// Export members:
export { AdministratorArgs } from "./administrator";
export type Administrator = import("./administrator").Administrator;
export const Administrator: typeof import("./administrator").Administrator = null as any;
utilities.lazyLoad(exports, ["Administrator"], () => require("./administrator"));

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

export { GetAdministratorArgs, GetAdministratorResult, GetAdministratorOutputArgs } from "./getAdministrator";
export const getAdministrator: typeof import("./getAdministrator").getAdministrator = null as any;
export const getAdministratorOutput: typeof import("./getAdministrator").getAdministratorOutput = null as any;
utilities.lazyLoad(exports, ["getAdministrator","getAdministratorOutput"], () => require("./getAdministrator"));

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

export { GetMigrationArgs, GetMigrationResult, GetMigrationOutputArgs } from "./getMigration";
export const getMigration: typeof import("./getMigration").getMigration = null as any;
export const getMigrationOutput: typeof import("./getMigration").getMigrationOutput = null as any;
utilities.lazyLoad(exports, ["getMigration","getMigrationOutput"], () => require("./getMigration"));

export { GetPrivateEndpointConnectionArgs, GetPrivateEndpointConnectionResult, GetPrivateEndpointConnectionOutputArgs } from "./getPrivateEndpointConnection";
export const getPrivateEndpointConnection: typeof import("./getPrivateEndpointConnection").getPrivateEndpointConnection = null as any;
export const getPrivateEndpointConnectionOutput: typeof import("./getPrivateEndpointConnection").getPrivateEndpointConnectionOutput = null as any;
utilities.lazyLoad(exports, ["getPrivateEndpointConnection","getPrivateEndpointConnectionOutput"], () => require("./getPrivateEndpointConnection"));

export { GetServerArgs, GetServerResult, GetServerOutputArgs } from "./getServer";
export const getServer: typeof import("./getServer").getServer = null as any;
export const getServerOutput: typeof import("./getServer").getServerOutput = null as any;
utilities.lazyLoad(exports, ["getServer","getServerOutput"], () => require("./getServer"));

export { GetVirtualEndpointArgs, GetVirtualEndpointResult, GetVirtualEndpointOutputArgs } from "./getVirtualEndpoint";
export const getVirtualEndpoint: typeof import("./getVirtualEndpoint").getVirtualEndpoint = null as any;
export const getVirtualEndpointOutput: typeof import("./getVirtualEndpoint").getVirtualEndpointOutput = null as any;
utilities.lazyLoad(exports, ["getVirtualEndpoint","getVirtualEndpointOutput"], () => require("./getVirtualEndpoint"));

export { MigrationArgs } from "./migration";
export type Migration = import("./migration").Migration;
export const Migration: typeof import("./migration").Migration = null as any;
utilities.lazyLoad(exports, ["Migration"], () => require("./migration"));

export { PrivateEndpointConnectionArgs } from "./privateEndpointConnection";
export type PrivateEndpointConnection = import("./privateEndpointConnection").PrivateEndpointConnection;
export const PrivateEndpointConnection: typeof import("./privateEndpointConnection").PrivateEndpointConnection = null as any;
utilities.lazyLoad(exports, ["PrivateEndpointConnection"], () => require("./privateEndpointConnection"));

export { ServerArgs } from "./server";
export type Server = import("./server").Server;
export const Server: typeof import("./server").Server = null as any;
utilities.lazyLoad(exports, ["Server"], () => require("./server"));

export { VirtualEndpointArgs } from "./virtualEndpoint";
export type VirtualEndpoint = import("./virtualEndpoint").VirtualEndpoint;
export const VirtualEndpoint: typeof import("./virtualEndpoint").VirtualEndpoint = null as any;
utilities.lazyLoad(exports, ["VirtualEndpoint"], () => require("./virtualEndpoint"));


// Export enums:
export * from "../../types/enums/dbforpostgresql/v20231201preview";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "azure-native:dbforpostgresql/v20231201preview:Administrator":
                return new Administrator(name, <any>undefined, { urn })
            case "azure-native:dbforpostgresql/v20231201preview:Configuration":
                return new Configuration(name, <any>undefined, { urn })
            case "azure-native:dbforpostgresql/v20231201preview:Database":
                return new Database(name, <any>undefined, { urn })
            case "azure-native:dbforpostgresql/v20231201preview:FirewallRule":
                return new FirewallRule(name, <any>undefined, { urn })
            case "azure-native:dbforpostgresql/v20231201preview:Migration":
                return new Migration(name, <any>undefined, { urn })
            case "azure-native:dbforpostgresql/v20231201preview:PrivateEndpointConnection":
                return new PrivateEndpointConnection(name, <any>undefined, { urn })
            case "azure-native:dbforpostgresql/v20231201preview:Server":
                return new Server(name, <any>undefined, { urn })
            case "azure-native:dbforpostgresql/v20231201preview:VirtualEndpoint":
                return new VirtualEndpoint(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("azure-native", "dbforpostgresql/v20231201preview", _module)
