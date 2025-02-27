# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AllocationMethod',
    'CreateDiffDisk',
    'DynamicMemoryEnabled',
    'InventoryType',
    'LimitCpuForMigration',
    'ProvisioningAction',
]


class AllocationMethod(str, Enum):
    """
    Gets or sets the mac address type.
    """
    DYNAMIC = "Dynamic"
    """
    Dynamically allocated address.
    """
    STATIC = "Static"
    """
    Statically allocated address.
    """


class CreateDiffDisk(str, Enum):
    """
    Gets or sets a value indicating diff disk.
    """
    TRUE = "true"
    """
    Enable create diff disk.
    """
    FALSE = "false"
    """
    Disable create diff disk.
    """


class DynamicMemoryEnabled(str, Enum):
    """
    Gets or sets a value indicating whether to enable dynamic memory or not.
    """
    TRUE = "true"
    """
    Enable dynamic memory.
    """
    FALSE = "false"
    """
    Disable dynamic memory.
    """


class InventoryType(str, Enum):
    """
    They inventory type.
    """
    CLOUD = "Cloud"
    """
    Cloud inventory type
    """
    VIRTUAL_NETWORK = "VirtualNetwork"
    """
    VirtualNetwork inventory type
    """
    VIRTUAL_MACHINE = "VirtualMachine"
    """
    VirtualMachine inventory type
    """
    VIRTUAL_MACHINE_TEMPLATE = "VirtualMachineTemplate"
    """
    VirtualMachineTemplate inventory type
    """


class LimitCpuForMigration(str, Enum):
    """
    Gets or sets a value indicating whether to enable processor compatibility mode for live migration of VMs.
    """
    TRUE = "true"
    """
    Enable limit CPU for migration.
    """
    FALSE = "false"
    """
    Disable limit CPU for migration.
    """


class ProvisioningAction(str, Enum):
    """
    Gets or sets the guest agent provisioning action.
    """
    INSTALL = "install"
    """
    Install guest agent.
    """
    UNINSTALL = "uninstall"
    """
    Uninstall guest agent.
    """
    REPAIR = "repair"
    """
    Repair guest agent.
    """
