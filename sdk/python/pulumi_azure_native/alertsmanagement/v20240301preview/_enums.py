# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ActionType',
    'DaysOfWeek',
    'Field',
    'NotificationsForCorrelatedAlerts',
    'Operator',
    'RecurrenceType',
    'UpdateType',
]


class ActionType(str, Enum):
    """
    Action that should be applied.
    """
    ADD_ACTION_GROUPS = "AddActionGroups"
    REMOVE_ALL_ACTION_GROUPS = "RemoveAllActionGroups"
    CORRELATE_ALERTS = "CorrelateAlerts"


class DaysOfWeek(str, Enum):
    """
    Days of week.
    """
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class Field(str, Enum):
    """
    Field for a given condition.
    """
    SEVERITY = "Severity"
    MONITOR_SERVICE = "MonitorService"
    MONITOR_CONDITION = "MonitorCondition"
    SIGNAL_TYPE = "SignalType"
    TARGET_RESOURCE_TYPE = "TargetResourceType"
    TARGET_RESOURCE = "TargetResource"
    TARGET_RESOURCE_GROUP = "TargetResourceGroup"
    ALERT_RULE_ID = "AlertRuleId"
    ALERT_RULE_NAME = "AlertRuleName"
    DESCRIPTION = "Description"
    ALERT_CONTEXT = "AlertContext"


class NotificationsForCorrelatedAlerts(str, Enum):
    """
    Indicates how to handle child alerts notifications.
    """
    NOTIFY_ALWAYS = "NotifyAlways"
    SUPPRESS_ALWAYS = "SuppressAlways"


class Operator(str, Enum):
    """
    Operator for a given condition.
    """
    EQUALS = "Equals"
    NOT_EQUALS = "NotEquals"
    CONTAINS = "Contains"
    DOES_NOT_CONTAIN = "DoesNotContain"


class RecurrenceType(str, Enum):
    """
    Specifies when the recurrence should be applied.
    """
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"


class UpdateType(str, Enum):
    """
    The type of update that needs to be performed.
    """
    TIME_BASED = "timeBased"
