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
    'GetScheduledQueryRuleResult',
    'AwaitableGetScheduledQueryRuleResult',
    'get_scheduled_query_rule',
    'get_scheduled_query_rule_output',
]

@pulumi.output_type
class GetScheduledQueryRuleResult:
    """
    The scheduled query rule resource.
    """
    def __init__(__self__, actions=None, created_with_api_version=None, criteria=None, description=None, display_name=None, enabled=None, etag=None, evaluation_frequency=None, id=None, is_legacy_log_analytics_rule=None, kind=None, location=None, mute_actions_duration=None, name=None, override_query_time_range=None, scopes=None, severity=None, tags=None, target_resource_types=None, type=None, window_size=None):
        if actions and not isinstance(actions, list):
            raise TypeError("Expected argument 'actions' to be a list")
        pulumi.set(__self__, "actions", actions)
        if created_with_api_version and not isinstance(created_with_api_version, str):
            raise TypeError("Expected argument 'created_with_api_version' to be a str")
        pulumi.set(__self__, "created_with_api_version", created_with_api_version)
        if criteria and not isinstance(criteria, dict):
            raise TypeError("Expected argument 'criteria' to be a dict")
        pulumi.set(__self__, "criteria", criteria)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if evaluation_frequency and not isinstance(evaluation_frequency, str):
            raise TypeError("Expected argument 'evaluation_frequency' to be a str")
        pulumi.set(__self__, "evaluation_frequency", evaluation_frequency)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_legacy_log_analytics_rule and not isinstance(is_legacy_log_analytics_rule, bool):
            raise TypeError("Expected argument 'is_legacy_log_analytics_rule' to be a bool")
        pulumi.set(__self__, "is_legacy_log_analytics_rule", is_legacy_log_analytics_rule)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mute_actions_duration and not isinstance(mute_actions_duration, str):
            raise TypeError("Expected argument 'mute_actions_duration' to be a str")
        pulumi.set(__self__, "mute_actions_duration", mute_actions_duration)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if override_query_time_range and not isinstance(override_query_time_range, str):
            raise TypeError("Expected argument 'override_query_time_range' to be a str")
        pulumi.set(__self__, "override_query_time_range", override_query_time_range)
        if scopes and not isinstance(scopes, list):
            raise TypeError("Expected argument 'scopes' to be a list")
        pulumi.set(__self__, "scopes", scopes)
        if severity and not isinstance(severity, float):
            raise TypeError("Expected argument 'severity' to be a float")
        pulumi.set(__self__, "severity", severity)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_resource_types and not isinstance(target_resource_types, list):
            raise TypeError("Expected argument 'target_resource_types' to be a list")
        pulumi.set(__self__, "target_resource_types", target_resource_types)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if window_size and not isinstance(window_size, str):
            raise TypeError("Expected argument 'window_size' to be a str")
        pulumi.set(__self__, "window_size", window_size)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence['outputs.ActionResponse']]:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="createdWithApiVersion")
    def created_with_api_version(self) -> str:
        """
        The api-version used when creating this alert rule
        """
        return pulumi.get(self, "created_with_api_version")

    @property
    @pulumi.getter
    def criteria(self) -> 'outputs.ScheduledQueryRuleCriteriaResponse':
        """
        The rule criteria that defines the conditions of the scheduled query rule.
        """
        return pulumi.get(self, "criteria")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the scheduled query rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the alert rule
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        The flag which indicates whether this scheduled query rule is enabled. Value should be true or false
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. 
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> str:
        """
        How often the scheduled query rule is evaluated represented in ISO 8601 duration format.
        """
        return pulumi.get(self, "evaluation_frequency")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isLegacyLogAnalyticsRule")
    def is_legacy_log_analytics_rule(self) -> bool:
        """
        True if alert rule is legacy Log Analytic rule
        """
        return pulumi.get(self, "is_legacy_log_analytics_rule")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="muteActionsDuration")
    def mute_actions_duration(self) -> Optional[str]:
        """
        Mute actions for the chosen period of time (in ISO 8601 duration format) after the alert is fired.
        """
        return pulumi.get(self, "mute_actions_duration")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="overrideQueryTimeRange")
    def override_query_time_range(self) -> Optional[str]:
        """
        If specified then overrides the query time range (default is WindowSize*NumberOfEvaluationPeriods)
        """
        return pulumi.get(self, "override_query_time_range")

    @property
    @pulumi.getter
    def scopes(self) -> Sequence[str]:
        """
        The list of resource id's that this scheduled query rule is scoped to.
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def severity(self) -> float:
        """
        Severity of the alert. Should be an integer between [0-4]. Value of 0 is severest
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetResourceTypes")
    def target_resource_types(self) -> Optional[Sequence[str]]:
        """
        List of resource type of the target resource(s) on which the alert is created/updated. For example if the scope is a resource group and targetResourceTypes is Microsoft.Compute/virtualMachines, then a different alert will be fired for each virtual machine in the resource group which meet the alert criteria
        """
        return pulumi.get(self, "target_resource_types")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> str:
        """
        The period of time (in ISO 8601 duration format) on which the Alert query will be executed (bin size).
        """
        return pulumi.get(self, "window_size")


class AwaitableGetScheduledQueryRuleResult(GetScheduledQueryRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScheduledQueryRuleResult(
            actions=self.actions,
            created_with_api_version=self.created_with_api_version,
            criteria=self.criteria,
            description=self.description,
            display_name=self.display_name,
            enabled=self.enabled,
            etag=self.etag,
            evaluation_frequency=self.evaluation_frequency,
            id=self.id,
            is_legacy_log_analytics_rule=self.is_legacy_log_analytics_rule,
            kind=self.kind,
            location=self.location,
            mute_actions_duration=self.mute_actions_duration,
            name=self.name,
            override_query_time_range=self.override_query_time_range,
            scopes=self.scopes,
            severity=self.severity,
            tags=self.tags,
            target_resource_types=self.target_resource_types,
            type=self.type,
            window_size=self.window_size)


def get_scheduled_query_rule(resource_group_name: Optional[str] = None,
                             rule_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScheduledQueryRuleResult:
    """
    Retrieve an scheduled query rule definition.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str rule_name: The name of the rule.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['ruleName'] = rule_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20200501preview:getScheduledQueryRule', __args__, opts=opts, typ=GetScheduledQueryRuleResult).value

    return AwaitableGetScheduledQueryRuleResult(
        actions=pulumi.get(__ret__, 'actions'),
        created_with_api_version=pulumi.get(__ret__, 'created_with_api_version'),
        criteria=pulumi.get(__ret__, 'criteria'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        enabled=pulumi.get(__ret__, 'enabled'),
        etag=pulumi.get(__ret__, 'etag'),
        evaluation_frequency=pulumi.get(__ret__, 'evaluation_frequency'),
        id=pulumi.get(__ret__, 'id'),
        is_legacy_log_analytics_rule=pulumi.get(__ret__, 'is_legacy_log_analytics_rule'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        mute_actions_duration=pulumi.get(__ret__, 'mute_actions_duration'),
        name=pulumi.get(__ret__, 'name'),
        override_query_time_range=pulumi.get(__ret__, 'override_query_time_range'),
        scopes=pulumi.get(__ret__, 'scopes'),
        severity=pulumi.get(__ret__, 'severity'),
        tags=pulumi.get(__ret__, 'tags'),
        target_resource_types=pulumi.get(__ret__, 'target_resource_types'),
        type=pulumi.get(__ret__, 'type'),
        window_size=pulumi.get(__ret__, 'window_size'))


@_utilities.lift_output_func(get_scheduled_query_rule)
def get_scheduled_query_rule_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                    rule_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScheduledQueryRuleResult]:
    """
    Retrieve an scheduled query rule definition.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str rule_name: The name of the rule.
    """
    ...
