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
from ._enums import *

__all__ = [
    'AsymmetricEncryptedSecretResponse',
    'BandwidthScheduleResponse',
    'FailoverSetEligibilityResultResponse',
    'FailoverSetResponse',
    'FailoverTargetResponse',
    'ManagerIntrinsicSettingsResponse',
    'ManagerSkuResponse',
    'ScheduleRecurrenceResponse',
    'TargetEligibilityErrorMessageResponse',
    'TargetEligibilityResultResponse',
    'TimeResponse',
    'VolumeContainerFailoverMetadataResponse',
    'VolumeFailoverMetadataResponse',
]

@pulumi.output_type
class AsymmetricEncryptedSecretResponse(dict):
    """
    Represent the secrets intended for encryption with asymmetric key pair.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "encryptionAlgorithm":
            suggest = "encryption_algorithm"
        elif key == "encryptionCertThumbprint":
            suggest = "encryption_cert_thumbprint"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AsymmetricEncryptedSecretResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AsymmetricEncryptedSecretResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AsymmetricEncryptedSecretResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 encryption_algorithm: str,
                 value: str,
                 encryption_cert_thumbprint: Optional[str] = None):
        """
        Represent the secrets intended for encryption with asymmetric key pair.
        :param str encryption_algorithm: The algorithm used to encrypt "Value".
        :param str value: The value of the secret.
        :param str encryption_cert_thumbprint: Thumbprint certificate that was used to encrypt "Value". If the value in unencrypted, it will be null.
        """
        pulumi.set(__self__, "encryption_algorithm", encryption_algorithm)
        pulumi.set(__self__, "value", value)
        if encryption_cert_thumbprint is not None:
            pulumi.set(__self__, "encryption_cert_thumbprint", encryption_cert_thumbprint)

    @property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> str:
        """
        The algorithm used to encrypt "Value".
        """
        return pulumi.get(self, "encryption_algorithm")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the secret.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter(name="encryptionCertThumbprint")
    def encryption_cert_thumbprint(self) -> Optional[str]:
        """
        Thumbprint certificate that was used to encrypt "Value". If the value in unencrypted, it will be null.
        """
        return pulumi.get(self, "encryption_cert_thumbprint")


@pulumi.output_type
class BandwidthScheduleResponse(dict):
    """
    The schedule for bandwidth setting.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "rateInMbps":
            suggest = "rate_in_mbps"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BandwidthScheduleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BandwidthScheduleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BandwidthScheduleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 days: Sequence[str],
                 rate_in_mbps: int,
                 start: 'outputs.TimeResponse',
                 stop: 'outputs.TimeResponse'):
        """
        The schedule for bandwidth setting.
        :param Sequence[str] days: The days of the week when this schedule is applicable.
        :param int rate_in_mbps: The rate in Mbps.
        :param 'TimeResponse' start: The start time of the schedule.
        :param 'TimeResponse' stop: The stop time of the schedule.
        """
        pulumi.set(__self__, "days", days)
        pulumi.set(__self__, "rate_in_mbps", rate_in_mbps)
        pulumi.set(__self__, "start", start)
        pulumi.set(__self__, "stop", stop)

    @property
    @pulumi.getter
    def days(self) -> Sequence[str]:
        """
        The days of the week when this schedule is applicable.
        """
        return pulumi.get(self, "days")

    @property
    @pulumi.getter(name="rateInMbps")
    def rate_in_mbps(self) -> int:
        """
        The rate in Mbps.
        """
        return pulumi.get(self, "rate_in_mbps")

    @property
    @pulumi.getter
    def start(self) -> 'outputs.TimeResponse':
        """
        The start time of the schedule.
        """
        return pulumi.get(self, "start")

    @property
    @pulumi.getter
    def stop(self) -> 'outputs.TimeResponse':
        """
        The stop time of the schedule.
        """
        return pulumi.get(self, "stop")


@pulumi.output_type
class FailoverSetEligibilityResultResponse(dict):
    """
    The eligibility result of failover set, for failover.
    """
    def __init__(__self__, *,
                 error_message: Optional[str] = None,
                 is_eligible_for_failover: Optional[bool] = None):
        """
        The eligibility result of failover set, for failover.
        :param str error_message: The error message, if the failover set is not eligible for failover.
        :param bool is_eligible_for_failover: Represents if this failover set is eligible for failover or not.
        """
        if error_message is not None:
            pulumi.set(__self__, "error_message", error_message)
        if is_eligible_for_failover is not None:
            pulumi.set(__self__, "is_eligible_for_failover", is_eligible_for_failover)

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> Optional[str]:
        """
        The error message, if the failover set is not eligible for failover.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter(name="isEligibleForFailover")
    def is_eligible_for_failover(self) -> Optional[bool]:
        """
        Represents if this failover set is eligible for failover or not.
        """
        return pulumi.get(self, "is_eligible_for_failover")


@pulumi.output_type
class FailoverSetResponse(dict):
    """
    The failover set on a device.
    """
    def __init__(__self__, *,
                 eligibility_result: Optional['outputs.FailoverSetEligibilityResultResponse'] = None,
                 volume_containers: Optional[Sequence['outputs.VolumeContainerFailoverMetadataResponse']] = None):
        """
        The failover set on a device.
        :param 'FailoverSetEligibilityResultResponse' eligibility_result: The eligibility result of the failover set, for failover.
        :param Sequence['VolumeContainerFailoverMetadataResponse'] volume_containers: The list of meta data of volume containers, which are part of the failover set.
        """
        if eligibility_result is not None:
            pulumi.set(__self__, "eligibility_result", eligibility_result)
        if volume_containers is not None:
            pulumi.set(__self__, "volume_containers", volume_containers)

    @property
    @pulumi.getter(name="eligibilityResult")
    def eligibility_result(self) -> Optional['outputs.FailoverSetEligibilityResultResponse']:
        """
        The eligibility result of the failover set, for failover.
        """
        return pulumi.get(self, "eligibility_result")

    @property
    @pulumi.getter(name="volumeContainers")
    def volume_containers(self) -> Optional[Sequence['outputs.VolumeContainerFailoverMetadataResponse']]:
        """
        The list of meta data of volume containers, which are part of the failover set.
        """
        return pulumi.get(self, "volume_containers")


@pulumi.output_type
class FailoverTargetResponse(dict):
    """
    Represents the eligibility of a device as a failover target device.
    """
    def __init__(__self__, *,
                 available_local_storage_in_bytes: Optional[float] = None,
                 available_tiered_storage_in_bytes: Optional[float] = None,
                 data_containers_count: Optional[int] = None,
                 device_id: Optional[str] = None,
                 device_location: Optional[str] = None,
                 device_software_version: Optional[str] = None,
                 device_status: Optional[str] = None,
                 eligibility_result: Optional['outputs.TargetEligibilityResultResponse'] = None,
                 friendly_device_software_version: Optional[str] = None,
                 model_description: Optional[str] = None,
                 volumes_count: Optional[int] = None):
        """
        Represents the eligibility of a device as a failover target device.
        :param float available_local_storage_in_bytes: The amount of free local storage available on the device in bytes.
        :param float available_tiered_storage_in_bytes: The amount of free tiered storage available for the device in bytes.
        :param int data_containers_count: The count of data containers on the device.
        :param str device_id: The path ID of the device.
        :param str device_location: The geo location (applicable only for cloud appliances) of the device.
        :param str device_software_version: The software version of the device.
        :param str device_status: The status of the device.
        :param 'TargetEligibilityResultResponse' eligibility_result: The eligibility result of the device, as a failover target device.
        :param str friendly_device_software_version: The friendly name for the current version of software on the device.
        :param str model_description: The model number of the device.
        :param int volumes_count: The count of volumes on the device.
        """
        if available_local_storage_in_bytes is not None:
            pulumi.set(__self__, "available_local_storage_in_bytes", available_local_storage_in_bytes)
        if available_tiered_storage_in_bytes is not None:
            pulumi.set(__self__, "available_tiered_storage_in_bytes", available_tiered_storage_in_bytes)
        if data_containers_count is not None:
            pulumi.set(__self__, "data_containers_count", data_containers_count)
        if device_id is not None:
            pulumi.set(__self__, "device_id", device_id)
        if device_location is not None:
            pulumi.set(__self__, "device_location", device_location)
        if device_software_version is not None:
            pulumi.set(__self__, "device_software_version", device_software_version)
        if device_status is not None:
            pulumi.set(__self__, "device_status", device_status)
        if eligibility_result is not None:
            pulumi.set(__self__, "eligibility_result", eligibility_result)
        if friendly_device_software_version is not None:
            pulumi.set(__self__, "friendly_device_software_version", friendly_device_software_version)
        if model_description is not None:
            pulumi.set(__self__, "model_description", model_description)
        if volumes_count is not None:
            pulumi.set(__self__, "volumes_count", volumes_count)

    @property
    @pulumi.getter(name="availableLocalStorageInBytes")
    def available_local_storage_in_bytes(self) -> Optional[float]:
        """
        The amount of free local storage available on the device in bytes.
        """
        return pulumi.get(self, "available_local_storage_in_bytes")

    @property
    @pulumi.getter(name="availableTieredStorageInBytes")
    def available_tiered_storage_in_bytes(self) -> Optional[float]:
        """
        The amount of free tiered storage available for the device in bytes.
        """
        return pulumi.get(self, "available_tiered_storage_in_bytes")

    @property
    @pulumi.getter(name="dataContainersCount")
    def data_containers_count(self) -> Optional[int]:
        """
        The count of data containers on the device.
        """
        return pulumi.get(self, "data_containers_count")

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[str]:
        """
        The path ID of the device.
        """
        return pulumi.get(self, "device_id")

    @property
    @pulumi.getter(name="deviceLocation")
    def device_location(self) -> Optional[str]:
        """
        The geo location (applicable only for cloud appliances) of the device.
        """
        return pulumi.get(self, "device_location")

    @property
    @pulumi.getter(name="deviceSoftwareVersion")
    def device_software_version(self) -> Optional[str]:
        """
        The software version of the device.
        """
        return pulumi.get(self, "device_software_version")

    @property
    @pulumi.getter(name="deviceStatus")
    def device_status(self) -> Optional[str]:
        """
        The status of the device.
        """
        return pulumi.get(self, "device_status")

    @property
    @pulumi.getter(name="eligibilityResult")
    def eligibility_result(self) -> Optional['outputs.TargetEligibilityResultResponse']:
        """
        The eligibility result of the device, as a failover target device.
        """
        return pulumi.get(self, "eligibility_result")

    @property
    @pulumi.getter(name="friendlyDeviceSoftwareVersion")
    def friendly_device_software_version(self) -> Optional[str]:
        """
        The friendly name for the current version of software on the device.
        """
        return pulumi.get(self, "friendly_device_software_version")

    @property
    @pulumi.getter(name="modelDescription")
    def model_description(self) -> Optional[str]:
        """
        The model number of the device.
        """
        return pulumi.get(self, "model_description")

    @property
    @pulumi.getter(name="volumesCount")
    def volumes_count(self) -> Optional[int]:
        """
        The count of volumes on the device.
        """
        return pulumi.get(self, "volumes_count")


@pulumi.output_type
class ManagerIntrinsicSettingsResponse(dict):
    """
    Intrinsic settings which refers to the type of the StorSimple Manager.
    """
    def __init__(__self__, *,
                 type: str):
        """
        Intrinsic settings which refers to the type of the StorSimple Manager.
        :param str type: The type of StorSimple Manager.
        """
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of StorSimple Manager.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ManagerSkuResponse(dict):
    """
    The Sku.
    """
    def __init__(__self__, *,
                 name: str):
        """
        The Sku.
        :param str name: Refers to the sku name which should be "Standard"
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Refers to the sku name which should be "Standard"
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class ScheduleRecurrenceResponse(dict):
    """
    The schedule recurrence.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "recurrenceType":
            suggest = "recurrence_type"
        elif key == "recurrenceValue":
            suggest = "recurrence_value"
        elif key == "weeklyDaysList":
            suggest = "weekly_days_list"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduleRecurrenceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduleRecurrenceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduleRecurrenceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 recurrence_type: str,
                 recurrence_value: int,
                 weekly_days_list: Optional[Sequence[str]] = None):
        """
        The schedule recurrence.
        :param str recurrence_type: The recurrence type.
        :param int recurrence_value: The recurrence value.
        :param Sequence[str] weekly_days_list: The week days list. Applicable only for schedules of recurrence type 'weekly'.
        """
        pulumi.set(__self__, "recurrence_type", recurrence_type)
        pulumi.set(__self__, "recurrence_value", recurrence_value)
        if weekly_days_list is not None:
            pulumi.set(__self__, "weekly_days_list", weekly_days_list)

    @property
    @pulumi.getter(name="recurrenceType")
    def recurrence_type(self) -> str:
        """
        The recurrence type.
        """
        return pulumi.get(self, "recurrence_type")

    @property
    @pulumi.getter(name="recurrenceValue")
    def recurrence_value(self) -> int:
        """
        The recurrence value.
        """
        return pulumi.get(self, "recurrence_value")

    @property
    @pulumi.getter(name="weeklyDaysList")
    def weekly_days_list(self) -> Optional[Sequence[str]]:
        """
        The week days list. Applicable only for schedules of recurrence type 'weekly'.
        """
        return pulumi.get(self, "weekly_days_list")


@pulumi.output_type
class TargetEligibilityErrorMessageResponse(dict):
    """
    The error/warning message due to which the device is ineligible as a failover target device.
    """
    def __init__(__self__, *,
                 message: Optional[str] = None,
                 resolution: Optional[str] = None,
                 result_code: Optional[str] = None):
        """
        The error/warning message due to which the device is ineligible as a failover target device.
        :param str message: The localized error message stating the reason why the device is not eligible as a target device.
        :param str resolution: The localized resolution message for the error.
        :param str result_code: The result code for the error, due to which the device does not qualify as a failover target device.
        """
        if message is not None:
            pulumi.set(__self__, "message", message)
        if resolution is not None:
            pulumi.set(__self__, "resolution", resolution)
        if result_code is not None:
            pulumi.set(__self__, "result_code", result_code)

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        The localized error message stating the reason why the device is not eligible as a target device.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def resolution(self) -> Optional[str]:
        """
        The localized resolution message for the error.
        """
        return pulumi.get(self, "resolution")

    @property
    @pulumi.getter(name="resultCode")
    def result_code(self) -> Optional[str]:
        """
        The result code for the error, due to which the device does not qualify as a failover target device.
        """
        return pulumi.get(self, "result_code")


@pulumi.output_type
class TargetEligibilityResultResponse(dict):
    """
    The eligibility result of device, as a failover target device.
    """
    def __init__(__self__, *,
                 eligibility_status: Optional[str] = None,
                 messages: Optional[Sequence['outputs.TargetEligibilityErrorMessageResponse']] = None):
        """
        The eligibility result of device, as a failover target device.
        :param str eligibility_status: The eligibility status of device, as a failover target device.
        :param Sequence['TargetEligibilityErrorMessageResponse'] messages: The list of error messages, if a device does not qualify as a failover target device.
        """
        if eligibility_status is not None:
            pulumi.set(__self__, "eligibility_status", eligibility_status)
        if messages is not None:
            pulumi.set(__self__, "messages", messages)

    @property
    @pulumi.getter(name="eligibilityStatus")
    def eligibility_status(self) -> Optional[str]:
        """
        The eligibility status of device, as a failover target device.
        """
        return pulumi.get(self, "eligibility_status")

    @property
    @pulumi.getter
    def messages(self) -> Optional[Sequence['outputs.TargetEligibilityErrorMessageResponse']]:
        """
        The list of error messages, if a device does not qualify as a failover target device.
        """
        return pulumi.get(self, "messages")


@pulumi.output_type
class TimeResponse(dict):
    """
    The time.
    """
    def __init__(__self__, *,
                 hours: int,
                 minutes: int,
                 seconds: int):
        """
        The time.
        :param int hours: The hour.
        :param int minutes: The minute.
        :param int seconds: The second.
        """
        pulumi.set(__self__, "hours", hours)
        pulumi.set(__self__, "minutes", minutes)
        pulumi.set(__self__, "seconds", seconds)

    @property
    @pulumi.getter
    def hours(self) -> int:
        """
        The hour.
        """
        return pulumi.get(self, "hours")

    @property
    @pulumi.getter
    def minutes(self) -> int:
        """
        The minute.
        """
        return pulumi.get(self, "minutes")

    @property
    @pulumi.getter
    def seconds(self) -> int:
        """
        The second.
        """
        return pulumi.get(self, "seconds")


@pulumi.output_type
class VolumeContainerFailoverMetadataResponse(dict):
    """
    The metadata of the volume container, that is being considered as part of a failover set.
    """
    def __init__(__self__, *,
                 volume_container_id: Optional[str] = None,
                 volumes: Optional[Sequence['outputs.VolumeFailoverMetadataResponse']] = None):
        """
        The metadata of the volume container, that is being considered as part of a failover set.
        :param str volume_container_id: The path ID of the volume container.
        :param Sequence['VolumeFailoverMetadataResponse'] volumes: The list of metadata of volumes inside the volume container, which contains valid cloud snapshots.
        """
        if volume_container_id is not None:
            pulumi.set(__self__, "volume_container_id", volume_container_id)
        if volumes is not None:
            pulumi.set(__self__, "volumes", volumes)

    @property
    @pulumi.getter(name="volumeContainerId")
    def volume_container_id(self) -> Optional[str]:
        """
        The path ID of the volume container.
        """
        return pulumi.get(self, "volume_container_id")

    @property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence['outputs.VolumeFailoverMetadataResponse']]:
        """
        The list of metadata of volumes inside the volume container, which contains valid cloud snapshots.
        """
        return pulumi.get(self, "volumes")


@pulumi.output_type
class VolumeFailoverMetadataResponse(dict):
    """
    The metadata of a volume that has valid cloud snapshot.
    """
    def __init__(__self__, *,
                 backup_created_date: Optional[str] = None,
                 backup_element_id: Optional[str] = None,
                 backup_id: Optional[str] = None,
                 backup_policy_id: Optional[str] = None,
                 size_in_bytes: Optional[float] = None,
                 volume_id: Optional[str] = None,
                 volume_type: Optional[str] = None):
        """
        The metadata of a volume that has valid cloud snapshot.
        :param str backup_created_date: The date at which the snapshot was taken.
        :param str backup_element_id: The path ID of the backup-element for this volume, inside the backup set.
        :param str backup_id: The path ID of the backup set.
        :param str backup_policy_id: The path ID of the backup policy using which the snapshot was taken.
        :param float size_in_bytes: The size of the volume in bytes at the time the snapshot was taken.
        :param str volume_id: The path ID of the volume.
        :param str volume_type: The type of the volume.
        """
        if backup_created_date is not None:
            pulumi.set(__self__, "backup_created_date", backup_created_date)
        if backup_element_id is not None:
            pulumi.set(__self__, "backup_element_id", backup_element_id)
        if backup_id is not None:
            pulumi.set(__self__, "backup_id", backup_id)
        if backup_policy_id is not None:
            pulumi.set(__self__, "backup_policy_id", backup_policy_id)
        if size_in_bytes is not None:
            pulumi.set(__self__, "size_in_bytes", size_in_bytes)
        if volume_id is not None:
            pulumi.set(__self__, "volume_id", volume_id)
        if volume_type is not None:
            pulumi.set(__self__, "volume_type", volume_type)

    @property
    @pulumi.getter(name="backupCreatedDate")
    def backup_created_date(self) -> Optional[str]:
        """
        The date at which the snapshot was taken.
        """
        return pulumi.get(self, "backup_created_date")

    @property
    @pulumi.getter(name="backupElementId")
    def backup_element_id(self) -> Optional[str]:
        """
        The path ID of the backup-element for this volume, inside the backup set.
        """
        return pulumi.get(self, "backup_element_id")

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> Optional[str]:
        """
        The path ID of the backup set.
        """
        return pulumi.get(self, "backup_id")

    @property
    @pulumi.getter(name="backupPolicyId")
    def backup_policy_id(self) -> Optional[str]:
        """
        The path ID of the backup policy using which the snapshot was taken.
        """
        return pulumi.get(self, "backup_policy_id")

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> Optional[float]:
        """
        The size of the volume in bytes at the time the snapshot was taken.
        """
        return pulumi.get(self, "size_in_bytes")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> Optional[str]:
        """
        The path ID of the volume.
        """
        return pulumi.get(self, "volume_id")

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[str]:
        """
        The type of the volume.
        """
        return pulumi.get(self, "volume_type")


