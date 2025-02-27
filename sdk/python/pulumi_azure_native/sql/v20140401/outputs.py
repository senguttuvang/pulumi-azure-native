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
    'OperationImpactResponse',
    'RecommendedIndexResponse',
    'ServiceTierAdvisorResponse',
    'SloUsageMetricResponse',
    'TransparentDataEncryptionResponse',
]

@pulumi.output_type
class OperationImpactResponse(dict):
    """
    The impact of an operation, both in absolute and relative terms.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "changeValueAbsolute":
            suggest = "change_value_absolute"
        elif key == "changeValueRelative":
            suggest = "change_value_relative"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OperationImpactResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OperationImpactResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OperationImpactResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 change_value_absolute: float,
                 change_value_relative: float,
                 name: str,
                 unit: str):
        """
        The impact of an operation, both in absolute and relative terms.
        :param float change_value_absolute: The absolute impact to dimension.
        :param float change_value_relative: The relative impact to dimension (null if not applicable)
        :param str name: The name of the impact dimension.
        :param str unit: The unit in which estimated impact to dimension is measured.
        """
        pulumi.set(__self__, "change_value_absolute", change_value_absolute)
        pulumi.set(__self__, "change_value_relative", change_value_relative)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter(name="changeValueAbsolute")
    def change_value_absolute(self) -> float:
        """
        The absolute impact to dimension.
        """
        return pulumi.get(self, "change_value_absolute")

    @property
    @pulumi.getter(name="changeValueRelative")
    def change_value_relative(self) -> float:
        """
        The relative impact to dimension (null if not applicable)
        """
        return pulumi.get(self, "change_value_relative")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the impact dimension.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def unit(self) -> str:
        """
        The unit in which estimated impact to dimension is measured.
        """
        return pulumi.get(self, "unit")


@pulumi.output_type
class RecommendedIndexResponse(dict):
    """
    Represents a database recommended index.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "estimatedImpact":
            suggest = "estimated_impact"
        elif key == "includedColumns":
            suggest = "included_columns"
        elif key == "indexScript":
            suggest = "index_script"
        elif key == "indexType":
            suggest = "index_type"
        elif key == "lastModified":
            suggest = "last_modified"
        elif key == "reportedImpact":
            suggest = "reported_impact"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RecommendedIndexResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RecommendedIndexResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RecommendedIndexResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action: str,
                 columns: Sequence[str],
                 created: str,
                 estimated_impact: Sequence['outputs.OperationImpactResponse'],
                 id: str,
                 included_columns: Sequence[str],
                 index_script: str,
                 index_type: str,
                 last_modified: str,
                 name: str,
                 reported_impact: Sequence['outputs.OperationImpactResponse'],
                 schema: str,
                 state: str,
                 table: str,
                 type: str):
        """
        Represents a database recommended index.
        :param str action: The proposed index action. You can create a missing index, drop an unused index, or rebuild an existing index to improve its performance.
        :param Sequence[str] columns: Columns over which to build index
        :param str created: The UTC datetime showing when this resource was created (ISO8601 format).
        :param Sequence['OperationImpactResponse'] estimated_impact: The estimated impact of doing recommended index action.
        :param str id: Resource ID.
        :param Sequence[str] included_columns: The list of column names to be included in the index
        :param str index_script: The full build index script
        :param str index_type: The type of index (CLUSTERED, NONCLUSTERED, COLUMNSTORE, CLUSTERED COLUMNSTORE)
        :param str last_modified: The UTC datetime of when was this resource last changed (ISO8601 format).
        :param str name: Resource name.
        :param Sequence['OperationImpactResponse'] reported_impact: The values reported after index action is complete.
        :param str schema: The schema where table to build index over resides
        :param str state: The current recommendation state.
        :param str table: The table on which to build index.
        :param str type: Resource type.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "columns", columns)
        pulumi.set(__self__, "created", created)
        pulumi.set(__self__, "estimated_impact", estimated_impact)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "included_columns", included_columns)
        pulumi.set(__self__, "index_script", index_script)
        pulumi.set(__self__, "index_type", index_type)
        pulumi.set(__self__, "last_modified", last_modified)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "reported_impact", reported_impact)
        pulumi.set(__self__, "schema", schema)
        pulumi.set(__self__, "state", state)
        pulumi.set(__self__, "table", table)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def action(self) -> str:
        """
        The proposed index action. You can create a missing index, drop an unused index, or rebuild an existing index to improve its performance.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def columns(self) -> Sequence[str]:
        """
        Columns over which to build index
        """
        return pulumi.get(self, "columns")

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The UTC datetime showing when this resource was created (ISO8601 format).
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="estimatedImpact")
    def estimated_impact(self) -> Sequence['outputs.OperationImpactResponse']:
        """
        The estimated impact of doing recommended index action.
        """
        return pulumi.get(self, "estimated_impact")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includedColumns")
    def included_columns(self) -> Sequence[str]:
        """
        The list of column names to be included in the index
        """
        return pulumi.get(self, "included_columns")

    @property
    @pulumi.getter(name="indexScript")
    def index_script(self) -> str:
        """
        The full build index script
        """
        return pulumi.get(self, "index_script")

    @property
    @pulumi.getter(name="indexType")
    def index_type(self) -> str:
        """
        The type of index (CLUSTERED, NONCLUSTERED, COLUMNSTORE, CLUSTERED COLUMNSTORE)
        """
        return pulumi.get(self, "index_type")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> str:
        """
        The UTC datetime of when was this resource last changed (ISO8601 format).
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="reportedImpact")
    def reported_impact(self) -> Sequence['outputs.OperationImpactResponse']:
        """
        The values reported after index action is complete.
        """
        return pulumi.get(self, "reported_impact")

    @property
    @pulumi.getter
    def schema(self) -> str:
        """
        The schema where table to build index over resides
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current recommendation state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def table(self) -> str:
        """
        The table on which to build index.
        """
        return pulumi.get(self, "table")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ServiceTierAdvisorResponse(dict):
    """
    Represents a Service Tier Advisor.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "activeTimeRatio":
            suggest = "active_time_ratio"
        elif key == "avgDtu":
            suggest = "avg_dtu"
        elif key == "currentServiceLevelObjective":
            suggest = "current_service_level_objective"
        elif key == "currentServiceLevelObjectiveId":
            suggest = "current_service_level_objective_id"
        elif key == "databaseSizeBasedRecommendationServiceLevelObjective":
            suggest = "database_size_based_recommendation_service_level_objective"
        elif key == "databaseSizeBasedRecommendationServiceLevelObjectiveId":
            suggest = "database_size_based_recommendation_service_level_objective_id"
        elif key == "disasterPlanBasedRecommendationServiceLevelObjective":
            suggest = "disaster_plan_based_recommendation_service_level_objective"
        elif key == "disasterPlanBasedRecommendationServiceLevelObjectiveId":
            suggest = "disaster_plan_based_recommendation_service_level_objective_id"
        elif key == "maxDtu":
            suggest = "max_dtu"
        elif key == "maxSizeInGB":
            suggest = "max_size_in_gb"
        elif key == "minDtu":
            suggest = "min_dtu"
        elif key == "observationPeriodEnd":
            suggest = "observation_period_end"
        elif key == "observationPeriodStart":
            suggest = "observation_period_start"
        elif key == "overallRecommendationServiceLevelObjective":
            suggest = "overall_recommendation_service_level_objective"
        elif key == "overallRecommendationServiceLevelObjectiveId":
            suggest = "overall_recommendation_service_level_objective_id"
        elif key == "serviceLevelObjectiveUsageMetrics":
            suggest = "service_level_objective_usage_metrics"
        elif key == "usageBasedRecommendationServiceLevelObjective":
            suggest = "usage_based_recommendation_service_level_objective"
        elif key == "usageBasedRecommendationServiceLevelObjectiveId":
            suggest = "usage_based_recommendation_service_level_objective_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceTierAdvisorResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceTierAdvisorResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceTierAdvisorResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 active_time_ratio: float,
                 avg_dtu: float,
                 confidence: float,
                 current_service_level_objective: str,
                 current_service_level_objective_id: str,
                 database_size_based_recommendation_service_level_objective: str,
                 database_size_based_recommendation_service_level_objective_id: str,
                 disaster_plan_based_recommendation_service_level_objective: str,
                 disaster_plan_based_recommendation_service_level_objective_id: str,
                 id: str,
                 max_dtu: float,
                 max_size_in_gb: float,
                 min_dtu: float,
                 name: str,
                 observation_period_end: str,
                 observation_period_start: str,
                 overall_recommendation_service_level_objective: str,
                 overall_recommendation_service_level_objective_id: str,
                 service_level_objective_usage_metrics: Sequence['outputs.SloUsageMetricResponse'],
                 type: str,
                 usage_based_recommendation_service_level_objective: str,
                 usage_based_recommendation_service_level_objective_id: str):
        """
        Represents a Service Tier Advisor.
        :param float active_time_ratio: The activeTimeRatio for service tier advisor.
        :param float avg_dtu: Gets or sets avgDtu for service tier advisor.
        :param float confidence: Gets or sets confidence for service tier advisor.
        :param str current_service_level_objective: Gets or sets currentServiceLevelObjective for service tier advisor.
        :param str current_service_level_objective_id: Gets or sets currentServiceLevelObjectiveId for service tier advisor.
        :param str database_size_based_recommendation_service_level_objective: Gets or sets databaseSizeBasedRecommendationServiceLevelObjective for service tier advisor.
        :param str database_size_based_recommendation_service_level_objective_id: Gets or sets databaseSizeBasedRecommendationServiceLevelObjectiveId for service tier advisor.
        :param str disaster_plan_based_recommendation_service_level_objective: Gets or sets disasterPlanBasedRecommendationServiceLevelObjective for service tier advisor.
        :param str disaster_plan_based_recommendation_service_level_objective_id: Gets or sets disasterPlanBasedRecommendationServiceLevelObjectiveId for service tier advisor.
        :param str id: Resource ID.
        :param float max_dtu: Gets or sets maxDtu for service tier advisor.
        :param float max_size_in_gb: Gets or sets maxSizeInGB for service tier advisor.
        :param float min_dtu: Gets or sets minDtu for service tier advisor.
        :param str name: Resource name.
        :param str observation_period_end: The observation period start (ISO8601 format).
        :param str observation_period_start: The observation period start (ISO8601 format).
        :param str overall_recommendation_service_level_objective: Gets or sets overallRecommendationServiceLevelObjective for service tier advisor.
        :param str overall_recommendation_service_level_objective_id: Gets or sets overallRecommendationServiceLevelObjectiveId for service tier advisor.
        :param Sequence['SloUsageMetricResponse'] service_level_objective_usage_metrics: Gets or sets serviceLevelObjectiveUsageMetrics for the service tier advisor.
        :param str type: Resource type.
        :param str usage_based_recommendation_service_level_objective: Gets or sets usageBasedRecommendationServiceLevelObjective for service tier advisor.
        :param str usage_based_recommendation_service_level_objective_id: Gets or sets usageBasedRecommendationServiceLevelObjectiveId for service tier advisor.
        """
        pulumi.set(__self__, "active_time_ratio", active_time_ratio)
        pulumi.set(__self__, "avg_dtu", avg_dtu)
        pulumi.set(__self__, "confidence", confidence)
        pulumi.set(__self__, "current_service_level_objective", current_service_level_objective)
        pulumi.set(__self__, "current_service_level_objective_id", current_service_level_objective_id)
        pulumi.set(__self__, "database_size_based_recommendation_service_level_objective", database_size_based_recommendation_service_level_objective)
        pulumi.set(__self__, "database_size_based_recommendation_service_level_objective_id", database_size_based_recommendation_service_level_objective_id)
        pulumi.set(__self__, "disaster_plan_based_recommendation_service_level_objective", disaster_plan_based_recommendation_service_level_objective)
        pulumi.set(__self__, "disaster_plan_based_recommendation_service_level_objective_id", disaster_plan_based_recommendation_service_level_objective_id)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "max_dtu", max_dtu)
        pulumi.set(__self__, "max_size_in_gb", max_size_in_gb)
        pulumi.set(__self__, "min_dtu", min_dtu)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "observation_period_end", observation_period_end)
        pulumi.set(__self__, "observation_period_start", observation_period_start)
        pulumi.set(__self__, "overall_recommendation_service_level_objective", overall_recommendation_service_level_objective)
        pulumi.set(__self__, "overall_recommendation_service_level_objective_id", overall_recommendation_service_level_objective_id)
        pulumi.set(__self__, "service_level_objective_usage_metrics", service_level_objective_usage_metrics)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "usage_based_recommendation_service_level_objective", usage_based_recommendation_service_level_objective)
        pulumi.set(__self__, "usage_based_recommendation_service_level_objective_id", usage_based_recommendation_service_level_objective_id)

    @property
    @pulumi.getter(name="activeTimeRatio")
    def active_time_ratio(self) -> float:
        """
        The activeTimeRatio for service tier advisor.
        """
        return pulumi.get(self, "active_time_ratio")

    @property
    @pulumi.getter(name="avgDtu")
    def avg_dtu(self) -> float:
        """
        Gets or sets avgDtu for service tier advisor.
        """
        return pulumi.get(self, "avg_dtu")

    @property
    @pulumi.getter
    def confidence(self) -> float:
        """
        Gets or sets confidence for service tier advisor.
        """
        return pulumi.get(self, "confidence")

    @property
    @pulumi.getter(name="currentServiceLevelObjective")
    def current_service_level_objective(self) -> str:
        """
        Gets or sets currentServiceLevelObjective for service tier advisor.
        """
        return pulumi.get(self, "current_service_level_objective")

    @property
    @pulumi.getter(name="currentServiceLevelObjectiveId")
    def current_service_level_objective_id(self) -> str:
        """
        Gets or sets currentServiceLevelObjectiveId for service tier advisor.
        """
        return pulumi.get(self, "current_service_level_objective_id")

    @property
    @pulumi.getter(name="databaseSizeBasedRecommendationServiceLevelObjective")
    def database_size_based_recommendation_service_level_objective(self) -> str:
        """
        Gets or sets databaseSizeBasedRecommendationServiceLevelObjective for service tier advisor.
        """
        return pulumi.get(self, "database_size_based_recommendation_service_level_objective")

    @property
    @pulumi.getter(name="databaseSizeBasedRecommendationServiceLevelObjectiveId")
    def database_size_based_recommendation_service_level_objective_id(self) -> str:
        """
        Gets or sets databaseSizeBasedRecommendationServiceLevelObjectiveId for service tier advisor.
        """
        return pulumi.get(self, "database_size_based_recommendation_service_level_objective_id")

    @property
    @pulumi.getter(name="disasterPlanBasedRecommendationServiceLevelObjective")
    def disaster_plan_based_recommendation_service_level_objective(self) -> str:
        """
        Gets or sets disasterPlanBasedRecommendationServiceLevelObjective for service tier advisor.
        """
        return pulumi.get(self, "disaster_plan_based_recommendation_service_level_objective")

    @property
    @pulumi.getter(name="disasterPlanBasedRecommendationServiceLevelObjectiveId")
    def disaster_plan_based_recommendation_service_level_objective_id(self) -> str:
        """
        Gets or sets disasterPlanBasedRecommendationServiceLevelObjectiveId for service tier advisor.
        """
        return pulumi.get(self, "disaster_plan_based_recommendation_service_level_objective_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxDtu")
    def max_dtu(self) -> float:
        """
        Gets or sets maxDtu for service tier advisor.
        """
        return pulumi.get(self, "max_dtu")

    @property
    @pulumi.getter(name="maxSizeInGB")
    def max_size_in_gb(self) -> float:
        """
        Gets or sets maxSizeInGB for service tier advisor.
        """
        return pulumi.get(self, "max_size_in_gb")

    @property
    @pulumi.getter(name="minDtu")
    def min_dtu(self) -> float:
        """
        Gets or sets minDtu for service tier advisor.
        """
        return pulumi.get(self, "min_dtu")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="observationPeriodEnd")
    def observation_period_end(self) -> str:
        """
        The observation period start (ISO8601 format).
        """
        return pulumi.get(self, "observation_period_end")

    @property
    @pulumi.getter(name="observationPeriodStart")
    def observation_period_start(self) -> str:
        """
        The observation period start (ISO8601 format).
        """
        return pulumi.get(self, "observation_period_start")

    @property
    @pulumi.getter(name="overallRecommendationServiceLevelObjective")
    def overall_recommendation_service_level_objective(self) -> str:
        """
        Gets or sets overallRecommendationServiceLevelObjective for service tier advisor.
        """
        return pulumi.get(self, "overall_recommendation_service_level_objective")

    @property
    @pulumi.getter(name="overallRecommendationServiceLevelObjectiveId")
    def overall_recommendation_service_level_objective_id(self) -> str:
        """
        Gets or sets overallRecommendationServiceLevelObjectiveId for service tier advisor.
        """
        return pulumi.get(self, "overall_recommendation_service_level_objective_id")

    @property
    @pulumi.getter(name="serviceLevelObjectiveUsageMetrics")
    def service_level_objective_usage_metrics(self) -> Sequence['outputs.SloUsageMetricResponse']:
        """
        Gets or sets serviceLevelObjectiveUsageMetrics for the service tier advisor.
        """
        return pulumi.get(self, "service_level_objective_usage_metrics")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="usageBasedRecommendationServiceLevelObjective")
    def usage_based_recommendation_service_level_objective(self) -> str:
        """
        Gets or sets usageBasedRecommendationServiceLevelObjective for service tier advisor.
        """
        return pulumi.get(self, "usage_based_recommendation_service_level_objective")

    @property
    @pulumi.getter(name="usageBasedRecommendationServiceLevelObjectiveId")
    def usage_based_recommendation_service_level_objective_id(self) -> str:
        """
        Gets or sets usageBasedRecommendationServiceLevelObjectiveId for service tier advisor.
        """
        return pulumi.get(self, "usage_based_recommendation_service_level_objective_id")


@pulumi.output_type
class SloUsageMetricResponse(dict):
    """
    A Slo Usage Metric.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "inRangeTimeRatio":
            suggest = "in_range_time_ratio"
        elif key == "serviceLevelObjective":
            suggest = "service_level_objective"
        elif key == "serviceLevelObjectiveId":
            suggest = "service_level_objective_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SloUsageMetricResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SloUsageMetricResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SloUsageMetricResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 in_range_time_ratio: float,
                 service_level_objective: str,
                 service_level_objective_id: str):
        """
        A Slo Usage Metric.
        :param float in_range_time_ratio: Gets or sets inRangeTimeRatio for SLO usage metric.
        :param str service_level_objective: The serviceLevelObjective for SLO usage metric.
        :param str service_level_objective_id: The serviceLevelObjectiveId for SLO usage metric.
        """
        pulumi.set(__self__, "in_range_time_ratio", in_range_time_ratio)
        pulumi.set(__self__, "service_level_objective", service_level_objective)
        pulumi.set(__self__, "service_level_objective_id", service_level_objective_id)

    @property
    @pulumi.getter(name="inRangeTimeRatio")
    def in_range_time_ratio(self) -> float:
        """
        Gets or sets inRangeTimeRatio for SLO usage metric.
        """
        return pulumi.get(self, "in_range_time_ratio")

    @property
    @pulumi.getter(name="serviceLevelObjective")
    def service_level_objective(self) -> str:
        """
        The serviceLevelObjective for SLO usage metric.
        """
        return pulumi.get(self, "service_level_objective")

    @property
    @pulumi.getter(name="serviceLevelObjectiveId")
    def service_level_objective_id(self) -> str:
        """
        The serviceLevelObjectiveId for SLO usage metric.
        """
        return pulumi.get(self, "service_level_objective_id")


@pulumi.output_type
class TransparentDataEncryptionResponse(dict):
    """
    Represents a database transparent data encryption configuration.
    """
    def __init__(__self__, *,
                 id: str,
                 location: str,
                 name: str,
                 type: str,
                 status: Optional[str] = None):
        """
        Represents a database transparent data encryption configuration.
        :param str id: Resource ID.
        :param str location: Resource location.
        :param str name: Resource name.
        :param str type: Resource type.
        :param str status: The status of the database transparent data encryption.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the database transparent data encryption.
        """
        return pulumi.get(self, "status")


