# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'MalwareScanningPropertiesResponse',
    'OperationStatusResponse',
    'SensitiveDataDiscoveryPropertiesResponse',
]

@pulumi.output_type
class MalwareScanningPropertiesResponse(dict):
    """
    Properties of Malware Scanning.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "operationStatus":
            suggest = "operation_status"
        elif key == "capGBPerMonth":
            suggest = "cap_gb_per_month"
        elif key == "isEnabled":
            suggest = "is_enabled"
        elif key == "scanResultsEventGridTopicResourceId":
            suggest = "scan_results_event_grid_topic_resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MalwareScanningPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MalwareScanningPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MalwareScanningPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 operation_status: 'outputs.OperationStatusResponse',
                 cap_gb_per_month: Optional[int] = None,
                 is_enabled: Optional[bool] = None,
                 scan_results_event_grid_topic_resource_id: Optional[str] = None):
        """
        Properties of Malware Scanning.
        :param 'OperationStatusResponse' operation_status: Upon failure or partial success. Additional data describing Malware Scanning enable/disable operation.
        :param int cap_gb_per_month: Defines the max GB to be scanned per Month. Set to -1 if no capping is needed.
        :param bool is_enabled: Indicates whether On Upload malware scanning should be enabled.
        :param str scan_results_event_grid_topic_resource_id: Optional. Resource id of an Event Grid Topic to send scan results to.
        """
        pulumi.set(__self__, "operation_status", operation_status)
        if cap_gb_per_month is not None:
            pulumi.set(__self__, "cap_gb_per_month", cap_gb_per_month)
        if is_enabled is not None:
            pulumi.set(__self__, "is_enabled", is_enabled)
        if scan_results_event_grid_topic_resource_id is not None:
            pulumi.set(__self__, "scan_results_event_grid_topic_resource_id", scan_results_event_grid_topic_resource_id)

    @property
    @pulumi.getter(name="operationStatus")
    def operation_status(self) -> 'outputs.OperationStatusResponse':
        """
        Upon failure or partial success. Additional data describing Malware Scanning enable/disable operation.
        """
        return pulumi.get(self, "operation_status")

    @property
    @pulumi.getter(name="capGBPerMonth")
    def cap_gb_per_month(self) -> Optional[int]:
        """
        Defines the max GB to be scanned per Month. Set to -1 if no capping is needed.
        """
        return pulumi.get(self, "cap_gb_per_month")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[bool]:
        """
        Indicates whether On Upload malware scanning should be enabled.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="scanResultsEventGridTopicResourceId")
    def scan_results_event_grid_topic_resource_id(self) -> Optional[str]:
        """
        Optional. Resource id of an Event Grid Topic to send scan results to.
        """
        return pulumi.get(self, "scan_results_event_grid_topic_resource_id")


@pulumi.output_type
class OperationStatusResponse(dict):
    """
    A status describing the success/failure of the enablement/disablement operation.
    """
    def __init__(__self__, *,
                 code: Optional[str] = None,
                 message: Optional[str] = None):
        """
        A status describing the success/failure of the enablement/disablement operation.
        :param str code: The operation status code.
        :param str message: Additional information regarding the success/failure of the operation.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if message is not None:
            pulumi.set(__self__, "message", message)

    @property
    @pulumi.getter
    def code(self) -> Optional[str]:
        """
        The operation status code.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        Additional information regarding the success/failure of the operation.
        """
        return pulumi.get(self, "message")


@pulumi.output_type
class SensitiveDataDiscoveryPropertiesResponse(dict):
    """
    Properties of Sensitive Data Discovery.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "operationStatus":
            suggest = "operation_status"
        elif key == "isEnabled":
            suggest = "is_enabled"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SensitiveDataDiscoveryPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SensitiveDataDiscoveryPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SensitiveDataDiscoveryPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 operation_status: 'outputs.OperationStatusResponse',
                 is_enabled: Optional[bool] = None):
        """
        Properties of Sensitive Data Discovery.
        :param 'OperationStatusResponse' operation_status: Upon failure or partial success. Additional data describing Sensitive Data Discovery enable/disable operation.
        :param bool is_enabled: Indicates whether Sensitive Data Discovery should be enabled.
        """
        pulumi.set(__self__, "operation_status", operation_status)
        if is_enabled is not None:
            pulumi.set(__self__, "is_enabled", is_enabled)

    @property
    @pulumi.getter(name="operationStatus")
    def operation_status(self) -> 'outputs.OperationStatusResponse':
        """
        Upon failure or partial success. Additional data describing Sensitive Data Discovery enable/disable operation.
        """
        return pulumi.get(self, "operation_status")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[bool]:
        """
        Indicates whether Sensitive Data Discovery should be enabled.
        """
        return pulumi.get(self, "is_enabled")


