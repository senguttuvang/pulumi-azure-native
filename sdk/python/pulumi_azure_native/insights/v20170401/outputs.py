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
    'ActivityLogAlertActionGroupResponse',
    'ActivityLogAlertActionListResponse',
    'ActivityLogAlertAllOfConditionResponse',
    'ActivityLogAlertLeafConditionResponse',
]

@pulumi.output_type
class ActivityLogAlertActionGroupResponse(dict):
    """
    A pointer to an Azure Action Group.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionGroupId":
            suggest = "action_group_id"
        elif key == "webhookProperties":
            suggest = "webhook_properties"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ActivityLogAlertActionGroupResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ActivityLogAlertActionGroupResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ActivityLogAlertActionGroupResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action_group_id: str,
                 webhook_properties: Optional[Mapping[str, str]] = None):
        """
        A pointer to an Azure Action Group.
        :param str action_group_id: The resourceId of the action group. This cannot be null or empty.
        :param Mapping[str, str] webhook_properties: the dictionary of custom properties to include with the post operation. These data are appended to the webhook payload.
        """
        pulumi.set(__self__, "action_group_id", action_group_id)
        if webhook_properties is not None:
            pulumi.set(__self__, "webhook_properties", webhook_properties)

    @property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> str:
        """
        The resourceId of the action group. This cannot be null or empty.
        """
        return pulumi.get(self, "action_group_id")

    @property
    @pulumi.getter(name="webhookProperties")
    def webhook_properties(self) -> Optional[Mapping[str, str]]:
        """
        the dictionary of custom properties to include with the post operation. These data are appended to the webhook payload.
        """
        return pulumi.get(self, "webhook_properties")


@pulumi.output_type
class ActivityLogAlertActionListResponse(dict):
    """
    A list of activity log alert actions.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionGroups":
            suggest = "action_groups"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ActivityLogAlertActionListResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ActivityLogAlertActionListResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ActivityLogAlertActionListResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action_groups: Optional[Sequence['outputs.ActivityLogAlertActionGroupResponse']] = None):
        """
        A list of activity log alert actions.
        :param Sequence['ActivityLogAlertActionGroupResponse'] action_groups: The list of activity log alerts.
        """
        if action_groups is not None:
            pulumi.set(__self__, "action_groups", action_groups)

    @property
    @pulumi.getter(name="actionGroups")
    def action_groups(self) -> Optional[Sequence['outputs.ActivityLogAlertActionGroupResponse']]:
        """
        The list of activity log alerts.
        """
        return pulumi.get(self, "action_groups")


@pulumi.output_type
class ActivityLogAlertAllOfConditionResponse(dict):
    """
    An Activity Log alert condition that is met when all its member conditions are met.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allOf":
            suggest = "all_of"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ActivityLogAlertAllOfConditionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ActivityLogAlertAllOfConditionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ActivityLogAlertAllOfConditionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 all_of: Sequence['outputs.ActivityLogAlertLeafConditionResponse']):
        """
        An Activity Log alert condition that is met when all its member conditions are met.
        :param Sequence['ActivityLogAlertLeafConditionResponse'] all_of: The list of activity log alert conditions.
        """
        pulumi.set(__self__, "all_of", all_of)

    @property
    @pulumi.getter(name="allOf")
    def all_of(self) -> Sequence['outputs.ActivityLogAlertLeafConditionResponse']:
        """
        The list of activity log alert conditions.
        """
        return pulumi.get(self, "all_of")


@pulumi.output_type
class ActivityLogAlertLeafConditionResponse(dict):
    """
    An Activity Log alert condition that is met by comparing an activity log field and value.
    """
    def __init__(__self__, *,
                 equals: str,
                 field: str):
        """
        An Activity Log alert condition that is met by comparing an activity log field and value.
        :param str equals: The field value will be compared to this value (case-insensitive) to determine if the condition is met.
        :param str field: The name of the field that this condition will examine. The possible values for this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties.'.
        """
        pulumi.set(__self__, "equals", equals)
        pulumi.set(__self__, "field", field)

    @property
    @pulumi.getter
    def equals(self) -> str:
        """
        The field value will be compared to this value (case-insensitive) to determine if the condition is met.
        """
        return pulumi.get(self, "equals")

    @property
    @pulumi.getter
    def field(self) -> str:
        """
        The name of the field that this condition will examine. The possible values for this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties.'.
        """
        return pulumi.get(self, "field")


