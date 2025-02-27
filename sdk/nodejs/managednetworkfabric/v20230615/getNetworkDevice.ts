// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../../types/input";
import * as outputs from "../../types/output";
import * as enums from "../../types/enums";
import * as utilities from "../../utilities";

/**
 * Gets the Network Device resource details.
 */
export function getNetworkDevice(args: GetNetworkDeviceArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkDeviceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("azure-native:managednetworkfabric/v20230615:getNetworkDevice", {
        "networkDeviceName": args.networkDeviceName,
        "resourceGroupName": args.resourceGroupName,
    }, opts);
}

export interface GetNetworkDeviceArgs {
    /**
     * Name of the Network Device.
     */
    networkDeviceName: string;
    /**
     * The name of the resource group. The name is case insensitive.
     */
    resourceGroupName: string;
}

/**
 * The Network Device resource definition.
 */
export interface GetNetworkDeviceResult {
    /**
     * Administrative state of the resource.
     */
    readonly administrativeState: string;
    /**
     * Switch configuration description.
     */
    readonly annotation?: string;
    /**
     * Configuration state of the resource.
     */
    readonly configurationState: string;
    /**
     * The host name of the device.
     */
    readonly hostName?: string;
    /**
     * Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
     */
    readonly id: string;
    /**
     * The geo-location where the resource lives
     */
    readonly location: string;
    /**
     * Management IPv4 Address.
     */
    readonly managementIpv4Address: string;
    /**
     * Management IPv6 Address.
     */
    readonly managementIpv6Address: string;
    /**
     * The name of the resource
     */
    readonly name: string;
    /**
     * NetworkDeviceRole is the device role: Example: CE | ToR.
     */
    readonly networkDeviceRole: string;
    /**
     * Network Device SKU name.
     */
    readonly networkDeviceSku?: string;
    /**
     * Reference to network rack resource id.
     */
    readonly networkRackId: string;
    /**
     * Provisioning state of the resource.
     */
    readonly provisioningState: string;
    /**
     * Serial number of the device. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber.
     */
    readonly serialNumber: string;
    /**
     * Azure Resource Manager metadata containing createdBy and modifiedBy information.
     */
    readonly systemData: outputs.managednetworkfabric.v20230615.SystemDataResponse;
    /**
     * Resource tags.
     */
    readonly tags?: {[key: string]: string};
    /**
     * The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
     */
    readonly type: string;
    /**
     * Current version of the device as defined in SKU.
     */
    readonly version: string;
}
/**
 * Gets the Network Device resource details.
 */
export function getNetworkDeviceOutput(args: GetNetworkDeviceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetNetworkDeviceResult> {
    return pulumi.output(args).apply((a: any) => getNetworkDevice(a, opts))
}

export interface GetNetworkDeviceOutputArgs {
    /**
     * Name of the Network Device.
     */
    networkDeviceName: pulumi.Input<string>;
    /**
     * The name of the resource group. The name is case insensitive.
     */
    resourceGroupName: pulumi.Input<string>;
}
