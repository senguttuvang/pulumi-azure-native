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
    'CustomerMetadataArgs',
    'KpiPropertiesArgs',
    'PivotPropertiesArgs',
    'ReportConfigAggregationArgs',
    'ReportConfigComparisonExpressionArgs',
    'ReportConfigDatasetConfigurationArgs',
    'ReportConfigDatasetArgs',
    'ReportConfigFilterArgs',
    'ReportConfigGroupingArgs',
    'ReportConfigSortingArgs',
    'ReportConfigTimePeriodArgs',
    'TagInheritancePropertiesArgs',
]

@pulumi.input_type
class CustomerMetadataArgs:
    def __init__(__self__, *,
                 billing_account_id: pulumi.Input[str],
                 billing_profile_id: pulumi.Input[str]):
        """
        The customer billing metadata
        :param pulumi.Input[str] billing_account_id: Customer billing account id
        :param pulumi.Input[str] billing_profile_id: Customer billing profile id
        """
        pulumi.set(__self__, "billing_account_id", billing_account_id)
        pulumi.set(__self__, "billing_profile_id", billing_profile_id)

    @property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> pulumi.Input[str]:
        """
        Customer billing account id
        """
        return pulumi.get(self, "billing_account_id")

    @billing_account_id.setter
    def billing_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "billing_account_id", value)

    @property
    @pulumi.getter(name="billingProfileId")
    def billing_profile_id(self) -> pulumi.Input[str]:
        """
        Customer billing profile id
        """
        return pulumi.get(self, "billing_profile_id")

    @billing_profile_id.setter
    def billing_profile_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "billing_profile_id", value)


@pulumi.input_type
class KpiPropertiesArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'KpiTypeType']]] = None):
        """
        Each KPI must contain a 'type' and 'enabled' key.
        :param pulumi.Input[bool] enabled: show the KPI in the UI?
        :param pulumi.Input[str] id: ID of resource related to metric (budget).
        :param pulumi.Input[Union[str, 'KpiTypeType']] type: KPI type (Forecast, Budget).
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        show the KPI in the UI?
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of resource related to metric (budget).
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'KpiTypeType']]]:
        """
        KPI type (Forecast, Budget).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'KpiTypeType']]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class PivotPropertiesArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'PivotTypeType']]] = None):
        """
        Each pivot must contain a 'type' and 'name'.
        :param pulumi.Input[str] name: Data field to show in view.
        :param pulumi.Input[Union[str, 'PivotTypeType']] type: Data type to show in view.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Data field to show in view.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'PivotTypeType']]]:
        """
        Data type to show in view.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'PivotTypeType']]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class ReportConfigAggregationArgs:
    def __init__(__self__, *,
                 function: pulumi.Input[Union[str, 'FunctionType']],
                 name: pulumi.Input[str]):
        """
        The aggregation expression to be used in the report.
        :param pulumi.Input[Union[str, 'FunctionType']] function: The name of the aggregation function to use.
        :param pulumi.Input[str] name: The name of the column to aggregate.
        """
        pulumi.set(__self__, "function", function)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def function(self) -> pulumi.Input[Union[str, 'FunctionType']]:
        """
        The name of the aggregation function to use.
        """
        return pulumi.get(self, "function")

    @function.setter
    def function(self, value: pulumi.Input[Union[str, 'FunctionType']]):
        pulumi.set(self, "function", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the column to aggregate.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class ReportConfigComparisonExpressionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 operator: pulumi.Input[Union[str, 'OperatorType']],
                 values: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        The comparison expression to be used in the report.
        :param pulumi.Input[str] name: The name of the column to use in comparison.
        :param pulumi.Input[Union[str, 'OperatorType']] operator: The operator to use for comparison.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] values: Array of values to use for comparison
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the column to use in comparison.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def operator(self) -> pulumi.Input[Union[str, 'OperatorType']]:
        """
        The operator to use for comparison.
        """
        return pulumi.get(self, "operator")

    @operator.setter
    def operator(self, value: pulumi.Input[Union[str, 'OperatorType']]):
        pulumi.set(self, "operator", value)

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Array of values to use for comparison
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "values", value)


@pulumi.input_type
class ReportConfigDatasetConfigurationArgs:
    def __init__(__self__, *,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The configuration of dataset in the report.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] columns: Array of column names to be included in the report. Any valid report column name is allowed. If not provided, then report includes all columns.
        """
        if columns is not None:
            pulumi.set(__self__, "columns", columns)

    @property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Array of column names to be included in the report. Any valid report column name is allowed. If not provided, then report includes all columns.
        """
        return pulumi.get(self, "columns")

    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "columns", value)


@pulumi.input_type
class ReportConfigDatasetArgs:
    def __init__(__self__, *,
                 aggregation: Optional[pulumi.Input[Mapping[str, pulumi.Input['ReportConfigAggregationArgs']]]] = None,
                 configuration: Optional[pulumi.Input['ReportConfigDatasetConfigurationArgs']] = None,
                 filter: Optional[pulumi.Input['ReportConfigFilterArgs']] = None,
                 granularity: Optional[pulumi.Input[Union[str, 'ReportGranularityType']]] = None,
                 grouping: Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigGroupingArgs']]]] = None,
                 sorting: Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigSortingArgs']]]] = None):
        """
        The definition of data present in the report.
        :param pulumi.Input[Mapping[str, pulumi.Input['ReportConfigAggregationArgs']]] aggregation: Dictionary of aggregation expression to use in the report. The key of each item in the dictionary is the alias for the aggregated column. Report can have up to 2 aggregation clauses.
        :param pulumi.Input['ReportConfigDatasetConfigurationArgs'] configuration: Has configuration information for the data in the report. The configuration will be ignored if aggregation and grouping are provided.
        :param pulumi.Input['ReportConfigFilterArgs'] filter: Has filter expression to use in the report.
        :param pulumi.Input[Union[str, 'ReportGranularityType']] granularity: The granularity of rows in the report.
        :param pulumi.Input[Sequence[pulumi.Input['ReportConfigGroupingArgs']]] grouping: Array of group by expression to use in the report. Report can have up to 2 group by clauses.
        :param pulumi.Input[Sequence[pulumi.Input['ReportConfigSortingArgs']]] sorting: Array of order by expression to use in the report.
        """
        if aggregation is not None:
            pulumi.set(__self__, "aggregation", aggregation)
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if granularity is not None:
            pulumi.set(__self__, "granularity", granularity)
        if grouping is not None:
            pulumi.set(__self__, "grouping", grouping)
        if sorting is not None:
            pulumi.set(__self__, "sorting", sorting)

    @property
    @pulumi.getter
    def aggregation(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['ReportConfigAggregationArgs']]]]:
        """
        Dictionary of aggregation expression to use in the report. The key of each item in the dictionary is the alias for the aggregated column. Report can have up to 2 aggregation clauses.
        """
        return pulumi.get(self, "aggregation")

    @aggregation.setter
    def aggregation(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['ReportConfigAggregationArgs']]]]):
        pulumi.set(self, "aggregation", value)

    @property
    @pulumi.getter
    def configuration(self) -> Optional[pulumi.Input['ReportConfigDatasetConfigurationArgs']]:
        """
        Has configuration information for the data in the report. The configuration will be ignored if aggregation and grouping are provided.
        """
        return pulumi.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: Optional[pulumi.Input['ReportConfigDatasetConfigurationArgs']]):
        pulumi.set(self, "configuration", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input['ReportConfigFilterArgs']]:
        """
        Has filter expression to use in the report.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input['ReportConfigFilterArgs']]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def granularity(self) -> Optional[pulumi.Input[Union[str, 'ReportGranularityType']]]:
        """
        The granularity of rows in the report.
        """
        return pulumi.get(self, "granularity")

    @granularity.setter
    def granularity(self, value: Optional[pulumi.Input[Union[str, 'ReportGranularityType']]]):
        pulumi.set(self, "granularity", value)

    @property
    @pulumi.getter
    def grouping(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigGroupingArgs']]]]:
        """
        Array of group by expression to use in the report. Report can have up to 2 group by clauses.
        """
        return pulumi.get(self, "grouping")

    @grouping.setter
    def grouping(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigGroupingArgs']]]]):
        pulumi.set(self, "grouping", value)

    @property
    @pulumi.getter
    def sorting(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigSortingArgs']]]]:
        """
        Array of order by expression to use in the report.
        """
        return pulumi.get(self, "sorting")

    @sorting.setter
    def sorting(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigSortingArgs']]]]):
        pulumi.set(self, "sorting", value)


@pulumi.input_type
class ReportConfigFilterArgs:
    def __init__(__self__, *,
                 and_: Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]]] = None,
                 dimensions: Optional[pulumi.Input['ReportConfigComparisonExpressionArgs']] = None,
                 or_: Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]]] = None,
                 tags: Optional[pulumi.Input['ReportConfigComparisonExpressionArgs']] = None):
        """
        The filter expression to be used in the report.
        :param pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]] and_: The logical "AND" expression. Must have at least 2 items.
        :param pulumi.Input['ReportConfigComparisonExpressionArgs'] dimensions: Has comparison expression for a dimension
        :param pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]] or_: The logical "OR" expression. Must have at least 2 items.
        :param pulumi.Input['ReportConfigComparisonExpressionArgs'] tags: Has comparison expression for a tag
        """
        if and_ is not None:
            pulumi.set(__self__, "and_", and_)
        if dimensions is not None:
            pulumi.set(__self__, "dimensions", dimensions)
        if or_ is not None:
            pulumi.set(__self__, "or_", or_)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]]]:
        """
        The logical "AND" expression. Must have at least 2 items.
        """
        return pulumi.get(self, "and_")

    @and_.setter
    def and_(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]]]):
        pulumi.set(self, "and_", value)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[pulumi.Input['ReportConfigComparisonExpressionArgs']]:
        """
        Has comparison expression for a dimension
        """
        return pulumi.get(self, "dimensions")

    @dimensions.setter
    def dimensions(self, value: Optional[pulumi.Input['ReportConfigComparisonExpressionArgs']]):
        pulumi.set(self, "dimensions", value)

    @property
    @pulumi.getter(name="or")
    def or_(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]]]:
        """
        The logical "OR" expression. Must have at least 2 items.
        """
        return pulumi.get(self, "or_")

    @or_.setter
    def or_(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ReportConfigFilterArgs']]]]):
        pulumi.set(self, "or_", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input['ReportConfigComparisonExpressionArgs']]:
        """
        Has comparison expression for a tag
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input['ReportConfigComparisonExpressionArgs']]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class ReportConfigGroupingArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 type: pulumi.Input[Union[str, 'ReportConfigColumnType']]):
        """
        The group by expression to be used in the report.
        :param pulumi.Input[str] name: The name of the column to group. This version supports subscription lowest possible grain.
        :param pulumi.Input[Union[str, 'ReportConfigColumnType']] type: Has type of the column to group.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the column to group. This version supports subscription lowest possible grain.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'ReportConfigColumnType']]:
        """
        Has type of the column to group.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'ReportConfigColumnType']]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class ReportConfigSortingArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 direction: Optional[pulumi.Input[Union[str, 'ReportConfigSortingType']]] = None):
        """
        The order by expression to be used in the report.
        :param pulumi.Input[str] name: The name of the column to sort.
        :param pulumi.Input[Union[str, 'ReportConfigSortingType']] direction: Direction of sort.
        """
        pulumi.set(__self__, "name", name)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the column to sort.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[Union[str, 'ReportConfigSortingType']]]:
        """
        Direction of sort.
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[pulumi.Input[Union[str, 'ReportConfigSortingType']]]):
        pulumi.set(self, "direction", value)


@pulumi.input_type
class ReportConfigTimePeriodArgs:
    def __init__(__self__, *,
                 from_: pulumi.Input[str],
                 to: pulumi.Input[str]):
        """
        The start and end date for pulling data for the report.
        :param pulumi.Input[str] from_: The start date to pull data from.
        :param pulumi.Input[str] to: The end date to pull data to.
        """
        pulumi.set(__self__, "from_", from_)
        pulumi.set(__self__, "to", to)

    @property
    @pulumi.getter(name="from")
    def from_(self) -> pulumi.Input[str]:
        """
        The start date to pull data from.
        """
        return pulumi.get(self, "from_")

    @from_.setter
    def from_(self, value: pulumi.Input[str]):
        pulumi.set(self, "from_", value)

    @property
    @pulumi.getter
    def to(self) -> pulumi.Input[str]:
        """
        The end date to pull data to.
        """
        return pulumi.get(self, "to")

    @to.setter
    def to(self, value: pulumi.Input[str]):
        pulumi.set(self, "to", value)


@pulumi.input_type
class TagInheritancePropertiesArgs:
    def __init__(__self__, *,
                 prefer_container_tags: pulumi.Input[bool]):
        """
        The properties of the tag inheritance setting.
        :param pulumi.Input[bool] prefer_container_tags: When resource has the same tag as subscription or resource group and this property is set to true - the subscription or resource group tag will be applied. If subscription and resource group tags are also the same, subscription tag will be applied.
        """
        pulumi.set(__self__, "prefer_container_tags", prefer_container_tags)

    @property
    @pulumi.getter(name="preferContainerTags")
    def prefer_container_tags(self) -> pulumi.Input[bool]:
        """
        When resource has the same tag as subscription or resource group and this property is set to true - the subscription or resource group tag will be applied. If subscription and resource group tags are also the same, subscription tag will be applied.
        """
        return pulumi.get(self, "prefer_container_tags")

    @prefer_container_tags.setter
    def prefer_container_tags(self, value: pulumi.Input[bool]):
        pulumi.set(self, "prefer_container_tags", value)


