# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ActionGroupArgs',
    'ActionListArgs',
    'AlertRuleAllOfConditionArgs',
    'AlertRuleAnyOfOrLeafConditionArgs',
    'AlertRuleLeafConditionArgs',
]

@pulumi.input_type
class ActionGroupArgs:
    def __init__(__self__, *,
                 action_group_id: pulumi.Input[str],
                 action_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 webhook_properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        A pointer to an Azure Action Group.
        :param pulumi.Input[str] action_group_id: The resource ID of the Action Group. This cannot be null or empty.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] action_properties: Predefined list of properties and configuration items for the action group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] webhook_properties: the dictionary of custom properties to include with the post operation. These data are appended to the webhook payload.
        """
        pulumi.set(__self__, "action_group_id", action_group_id)
        if action_properties is not None:
            pulumi.set(__self__, "action_properties", action_properties)
        if webhook_properties is not None:
            pulumi.set(__self__, "webhook_properties", webhook_properties)

    @property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the Action Group. This cannot be null or empty.
        """
        return pulumi.get(self, "action_group_id")

    @action_group_id.setter
    def action_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "action_group_id", value)

    @property
    @pulumi.getter(name="actionProperties")
    def action_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Predefined list of properties and configuration items for the action group.
        """
        return pulumi.get(self, "action_properties")

    @action_properties.setter
    def action_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "action_properties", value)

    @property
    @pulumi.getter(name="webhookProperties")
    def webhook_properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        the dictionary of custom properties to include with the post operation. These data are appended to the webhook payload.
        """
        return pulumi.get(self, "webhook_properties")

    @webhook_properties.setter
    def webhook_properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "webhook_properties", value)


@pulumi.input_type
class ActionListArgs:
    def __init__(__self__, *,
                 action_groups: Optional[pulumi.Input[Sequence[pulumi.Input['ActionGroupArgs']]]] = None):
        """
        A list of Activity Log Alert rule actions.
        :param pulumi.Input[Sequence[pulumi.Input['ActionGroupArgs']]] action_groups: The list of the Action Groups.
        """
        if action_groups is not None:
            pulumi.set(__self__, "action_groups", action_groups)

    @property
    @pulumi.getter(name="actionGroups")
    def action_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ActionGroupArgs']]]]:
        """
        The list of the Action Groups.
        """
        return pulumi.get(self, "action_groups")

    @action_groups.setter
    def action_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ActionGroupArgs']]]]):
        pulumi.set(self, "action_groups", value)


@pulumi.input_type
class AlertRuleAllOfConditionArgs:
    def __init__(__self__, *,
                 all_of: pulumi.Input[Sequence[pulumi.Input['AlertRuleAnyOfOrLeafConditionArgs']]]):
        """
        An Activity Log Alert rule condition that is met when all its member conditions are met.
        :param pulumi.Input[Sequence[pulumi.Input['AlertRuleAnyOfOrLeafConditionArgs']]] all_of: The list of Activity Log Alert rule conditions.
        """
        pulumi.set(__self__, "all_of", all_of)

    @property
    @pulumi.getter(name="allOf")
    def all_of(self) -> pulumi.Input[Sequence[pulumi.Input['AlertRuleAnyOfOrLeafConditionArgs']]]:
        """
        The list of Activity Log Alert rule conditions.
        """
        return pulumi.get(self, "all_of")

    @all_of.setter
    def all_of(self, value: pulumi.Input[Sequence[pulumi.Input['AlertRuleAnyOfOrLeafConditionArgs']]]):
        pulumi.set(self, "all_of", value)


@pulumi.input_type
class AlertRuleAnyOfOrLeafConditionArgs:
    def __init__(__self__, *,
                 any_of: Optional[pulumi.Input[Sequence[pulumi.Input['AlertRuleLeafConditionArgs']]]] = None,
                 contains_any: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 equals: Optional[pulumi.Input[str]] = None,
                 field: Optional[pulumi.Input[str]] = None):
        """
        An Activity Log Alert rule condition that is met when all its member conditions are met.
        Each condition can be of one of the following types:
        __Important__: Each type has its unique subset of properties. Properties from different types CANNOT exist in one condition.
           * __Leaf Condition -__ must contain 'field' and either 'equals' or 'containsAny'.
          _Please note, 'anyOf' should __not__ be set in a Leaf Condition._
          * __AnyOf Condition -__ must contain __only__ 'anyOf' (which is an array of Leaf Conditions).
          _Please note, 'field', 'equals' and 'containsAny' should __not__ be set in an AnyOf Condition._

        :param pulumi.Input[Sequence[pulumi.Input['AlertRuleLeafConditionArgs']]] any_of: An Activity Log Alert rule condition that is met when at least one of its member leaf conditions are met.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] contains_any: The value of the event's field will be compared to the values in this array (case-insensitive) to determine if the condition is met.
        :param pulumi.Input[str] equals: The value of the event's field will be compared to this value (case-insensitive) to determine if the condition is met.
        :param pulumi.Input[str] field: The name of the Activity Log event's field that this condition will examine.
               The possible values for this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties'.
        """
        if any_of is not None:
            pulumi.set(__self__, "any_of", any_of)
        if contains_any is not None:
            pulumi.set(__self__, "contains_any", contains_any)
        if equals is not None:
            pulumi.set(__self__, "equals", equals)
        if field is not None:
            pulumi.set(__self__, "field", field)

    @property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AlertRuleLeafConditionArgs']]]]:
        """
        An Activity Log Alert rule condition that is met when at least one of its member leaf conditions are met.
        """
        return pulumi.get(self, "any_of")

    @any_of.setter
    def any_of(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AlertRuleLeafConditionArgs']]]]):
        pulumi.set(self, "any_of", value)

    @property
    @pulumi.getter(name="containsAny")
    def contains_any(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The value of the event's field will be compared to the values in this array (case-insensitive) to determine if the condition is met.
        """
        return pulumi.get(self, "contains_any")

    @contains_any.setter
    def contains_any(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "contains_any", value)

    @property
    @pulumi.getter
    def equals(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the event's field will be compared to this value (case-insensitive) to determine if the condition is met.
        """
        return pulumi.get(self, "equals")

    @equals.setter
    def equals(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "equals", value)

    @property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Activity Log event's field that this condition will examine.
        The possible values for this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties'.
        """
        return pulumi.get(self, "field")

    @field.setter
    def field(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field", value)


@pulumi.input_type
class AlertRuleLeafConditionArgs:
    def __init__(__self__, *,
                 contains_any: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 equals: Optional[pulumi.Input[str]] = None,
                 field: Optional[pulumi.Input[str]] = None):
        """
        An Activity Log Alert rule condition that is met by comparing the field and value of an Activity Log event.
        This condition must contain 'field' and either 'equals' or 'containsAny'.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] contains_any: The value of the event's field will be compared to the values in this array (case-insensitive) to determine if the condition is met.
        :param pulumi.Input[str] equals: The value of the event's field will be compared to this value (case-insensitive) to determine if the condition is met.
        :param pulumi.Input[str] field: The name of the Activity Log event's field that this condition will examine.
               The possible values for this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties'.
        """
        if contains_any is not None:
            pulumi.set(__self__, "contains_any", contains_any)
        if equals is not None:
            pulumi.set(__self__, "equals", equals)
        if field is not None:
            pulumi.set(__self__, "field", field)

    @property
    @pulumi.getter(name="containsAny")
    def contains_any(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The value of the event's field will be compared to the values in this array (case-insensitive) to determine if the condition is met.
        """
        return pulumi.get(self, "contains_any")

    @contains_any.setter
    def contains_any(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "contains_any", value)

    @property
    @pulumi.getter
    def equals(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the event's field will be compared to this value (case-insensitive) to determine if the condition is met.
        """
        return pulumi.get(self, "equals")

    @equals.setter
    def equals(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "equals", value)

    @property
    @pulumi.getter
    def field(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Activity Log event's field that this condition will examine.
        The possible values for this field are (case-insensitive): 'resourceId', 'category', 'caller', 'level', 'operationName', 'resourceGroup', 'resourceProvider', 'status', 'subStatus', 'resourceType', or anything beginning with 'properties'.
        """
        return pulumi.get(self, "field")

    @field.setter
    def field(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "field", value)


