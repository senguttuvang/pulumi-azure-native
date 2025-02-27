# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'ErrorArgs',
    'SpringbootserversPropertiesArgs',
    'SpringbootsitesModelExtendedLocationArgs',
    'SpringbootsitesPropertiesArgs',
]

@pulumi.input_type
class ErrorArgs:
    def __init__(__self__, *,
                 code: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[float]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 possible_causes: Optional[pulumi.Input[str]] = None,
                 recommended_action: Optional[pulumi.Input[str]] = None,
                 run_as_account_id: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[str]] = None,
                 summary_message: Optional[pulumi.Input[str]] = None,
                 updated_time_stamp: Optional[pulumi.Input[str]] = None):
        """
        Defines the error.
        :param pulumi.Input[str] code: The error code.
        :param pulumi.Input[float] id: The error ID.
        :param pulumi.Input[str] message: The detailed error message.
        :param pulumi.Input[str] possible_causes: The error possible causes.
        :param pulumi.Input[str] recommended_action: The error recommended action
        :param pulumi.Input[str] run_as_account_id: The account ID used to login.
        :param pulumi.Input[str] severity: The error severity
        :param pulumi.Input[str] summary_message: The summarized error message.
        :param pulumi.Input[str] updated_time_stamp: Time when this error was last updated.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if possible_causes is not None:
            pulumi.set(__self__, "possible_causes", possible_causes)
        if recommended_action is not None:
            pulumi.set(__self__, "recommended_action", recommended_action)
        if run_as_account_id is not None:
            pulumi.set(__self__, "run_as_account_id", run_as_account_id)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)
        if summary_message is not None:
            pulumi.set(__self__, "summary_message", summary_message)
        if updated_time_stamp is not None:
            pulumi.set(__self__, "updated_time_stamp", updated_time_stamp)

    @property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[str]]:
        """
        The error code.
        """
        return pulumi.get(self, "code")

    @code.setter
    def code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "code", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[float]]:
        """
        The error ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        The detailed error message.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter(name="possibleCauses")
    def possible_causes(self) -> Optional[pulumi.Input[str]]:
        """
        The error possible causes.
        """
        return pulumi.get(self, "possible_causes")

    @possible_causes.setter
    def possible_causes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "possible_causes", value)

    @property
    @pulumi.getter(name="recommendedAction")
    def recommended_action(self) -> Optional[pulumi.Input[str]]:
        """
        The error recommended action
        """
        return pulumi.get(self, "recommended_action")

    @recommended_action.setter
    def recommended_action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recommended_action", value)

    @property
    @pulumi.getter(name="runAsAccountId")
    def run_as_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account ID used to login.
        """
        return pulumi.get(self, "run_as_account_id")

    @run_as_account_id.setter
    def run_as_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "run_as_account_id", value)

    @property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[str]]:
        """
        The error severity
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter(name="summaryMessage")
    def summary_message(self) -> Optional[pulumi.Input[str]]:
        """
        The summarized error message.
        """
        return pulumi.get(self, "summary_message")

    @summary_message.setter
    def summary_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "summary_message", value)

    @property
    @pulumi.getter(name="updatedTimeStamp")
    def updated_time_stamp(self) -> Optional[pulumi.Input[str]]:
        """
        Time when this error was last updated.
        """
        return pulumi.get(self, "updated_time_stamp")

    @updated_time_stamp.setter
    def updated_time_stamp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_time_stamp", value)


@pulumi.input_type
class SpringbootserversPropertiesArgs:
    def __init__(__self__, *,
                 server: pulumi.Input[str],
                 errors: Optional[pulumi.Input[Sequence[pulumi.Input['ErrorArgs']]]] = None,
                 fqdn_and_ip_address_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 machine_arm_id: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 spring_boot_apps: Optional[pulumi.Input[int]] = None,
                 total_apps: Optional[pulumi.Input[int]] = None):
        """
        The springbootservers resource definition.
        :param pulumi.Input[str] server: Server is the target server name or ip address to discover of SpringBootServer.
        :param pulumi.Input[Sequence[pulumi.Input['ErrorArgs']]] errors: The list of errors.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] fqdn_and_ip_address_list: The alternative FQDN or IP addresses to discover for this server
        :param pulumi.Input[str] machine_arm_id: The machine Id from ARM
        :param pulumi.Input[int] port: Target server port for remote login
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The resource provisioning state.
        :param pulumi.Input[int] spring_boot_apps: The total number of spring boot apps been discovered
        :param pulumi.Input[int] total_apps: The total number of apps been discovered
        """
        pulumi.set(__self__, "server", server)
        if errors is not None:
            pulumi.set(__self__, "errors", errors)
        if fqdn_and_ip_address_list is not None:
            pulumi.set(__self__, "fqdn_and_ip_address_list", fqdn_and_ip_address_list)
        if machine_arm_id is not None:
            pulumi.set(__self__, "machine_arm_id", machine_arm_id)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if spring_boot_apps is not None:
            pulumi.set(__self__, "spring_boot_apps", spring_boot_apps)
        if total_apps is not None:
            pulumi.set(__self__, "total_apps", total_apps)

    @property
    @pulumi.getter
    def server(self) -> pulumi.Input[str]:
        """
        Server is the target server name or ip address to discover of SpringBootServer.
        """
        return pulumi.get(self, "server")

    @server.setter
    def server(self, value: pulumi.Input[str]):
        pulumi.set(self, "server", value)

    @property
    @pulumi.getter
    def errors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ErrorArgs']]]]:
        """
        The list of errors.
        """
        return pulumi.get(self, "errors")

    @errors.setter
    def errors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ErrorArgs']]]]):
        pulumi.set(self, "errors", value)

    @property
    @pulumi.getter(name="fqdnAndIpAddressList")
    def fqdn_and_ip_address_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The alternative FQDN or IP addresses to discover for this server
        """
        return pulumi.get(self, "fqdn_and_ip_address_list")

    @fqdn_and_ip_address_list.setter
    def fqdn_and_ip_address_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "fqdn_and_ip_address_list", value)

    @property
    @pulumi.getter(name="machineArmId")
    def machine_arm_id(self) -> Optional[pulumi.Input[str]]:
        """
        The machine Id from ARM
        """
        return pulumi.get(self, "machine_arm_id")

    @machine_arm_id.setter
    def machine_arm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "machine_arm_id", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        Target server port for remote login
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'ProvisioningState']]]:
        """
        The resource provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'ProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="springBootApps")
    def spring_boot_apps(self) -> Optional[pulumi.Input[int]]:
        """
        The total number of spring boot apps been discovered
        """
        return pulumi.get(self, "spring_boot_apps")

    @spring_boot_apps.setter
    def spring_boot_apps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "spring_boot_apps", value)

    @property
    @pulumi.getter(name="totalApps")
    def total_apps(self) -> Optional[pulumi.Input[int]]:
        """
        The total number of apps been discovered
        """
        return pulumi.get(self, "total_apps")

    @total_apps.setter
    def total_apps(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "total_apps", value)


@pulumi.input_type
class SpringbootsitesModelExtendedLocationArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The extended location definition.
        :param pulumi.Input[str] name: The extended location name.
        :param pulumi.Input[str] type: The extended location type.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The extended location name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The extended location type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class SpringbootsitesPropertiesArgs:
    def __init__(__self__, *,
                 master_site_id: Optional[pulumi.Input[str]] = None,
                 migrate_project_id: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None):
        """
        The springbootsites resource definition.
        :param pulumi.Input[str] master_site_id: The master site ID from Azure Migrate.
        :param pulumi.Input[str] migrate_project_id: The migrate project ID from Azure Migrate.
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The resource provisioning state.
        """
        if master_site_id is not None:
            pulumi.set(__self__, "master_site_id", master_site_id)
        if migrate_project_id is not None:
            pulumi.set(__self__, "migrate_project_id", migrate_project_id)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)

    @property
    @pulumi.getter(name="masterSiteId")
    def master_site_id(self) -> Optional[pulumi.Input[str]]:
        """
        The master site ID from Azure Migrate.
        """
        return pulumi.get(self, "master_site_id")

    @master_site_id.setter
    def master_site_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_site_id", value)

    @property
    @pulumi.getter(name="migrateProjectId")
    def migrate_project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The migrate project ID from Azure Migrate.
        """
        return pulumi.get(self, "migrate_project_id")

    @migrate_project_id.setter
    def migrate_project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "migrate_project_id", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'ProvisioningState']]]:
        """
        The resource provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'ProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)


