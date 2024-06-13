# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'SLOAlerting',
    'SLOAlertingAnnotation',
    'SLOAlertingFastburn',
    'SLOAlertingFastburnAnnotation',
    'SLOAlertingFastburnLabel',
    'SLOAlertingLabel',
    'SLOAlertingSlowburn',
    'SLOAlertingSlowburnAnnotation',
    'SLOAlertingSlowburnLabel',
    'SLODestinationDatasource',
    'SLOLabel',
    'SLOObjective',
    'SLOQuery',
    'SLOQueryFreeform',
    'SLOQueryRatio',
    'GetSlosSloResult',
    'GetSlosSloAlertingResult',
    'GetSlosSloAlertingAnnotationResult',
    'GetSlosSloAlertingFastburnResult',
    'GetSlosSloAlertingFastburnAnnotationResult',
    'GetSlosSloAlertingFastburnLabelResult',
    'GetSlosSloAlertingLabelResult',
    'GetSlosSloAlertingSlowburnResult',
    'GetSlosSloAlertingSlowburnAnnotationResult',
    'GetSlosSloAlertingSlowburnLabelResult',
    'GetSlosSloDestinationDatasourceResult',
    'GetSlosSloLabelResult',
    'GetSlosSloObjectiveResult',
    'GetSlosSloQueryResult',
    'GetSlosSloQueryFreeformResult',
    'GetSlosSloQueryRatioResult',
]

@pulumi.output_type
class SLOAlerting(dict):
    def __init__(__self__, *,
                 annotations: Optional[Sequence['outputs.SLOAlertingAnnotation']] = None,
                 fastburns: Optional[Sequence['outputs.SLOAlertingFastburn']] = None,
                 labels: Optional[Sequence['outputs.SLOAlertingLabel']] = None,
                 slowburns: Optional[Sequence['outputs.SLOAlertingSlowburn']] = None):
        """
        :param Sequence['SLOAlertingAnnotationArgs'] annotations: Annotations will be attached to all alerts generated by any of these rules.
        :param Sequence['SLOAlertingFastburnArgs'] fastburns: Alerting Rules generated for Fast Burn alerts
        :param Sequence['SLOAlertingLabelArgs'] labels: Labels will be attached to all alerts generated by any of these rules.
        :param Sequence['SLOAlertingSlowburnArgs'] slowburns: Alerting Rules generated for Slow Burn alerts
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if fastburns is not None:
            pulumi.set(__self__, "fastburns", fastburns)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if slowburns is not None:
            pulumi.set(__self__, "slowburns", slowburns)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[Sequence['outputs.SLOAlertingAnnotation']]:
        """
        Annotations will be attached to all alerts generated by any of these rules.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def fastburns(self) -> Optional[Sequence['outputs.SLOAlertingFastburn']]:
        """
        Alerting Rules generated for Fast Burn alerts
        """
        return pulumi.get(self, "fastburns")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence['outputs.SLOAlertingLabel']]:
        """
        Labels will be attached to all alerts generated by any of these rules.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def slowburns(self) -> Optional[Sequence['outputs.SLOAlertingSlowburn']]:
        """
        Alerting Rules generated for Slow Burn alerts
        """
        return pulumi.get(self, "slowburns")


@pulumi.output_type
class SLOAlertingAnnotation(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class SLOAlertingFastburn(dict):
    def __init__(__self__, *,
                 annotations: Optional[Sequence['outputs.SLOAlertingFastburnAnnotation']] = None,
                 labels: Optional[Sequence['outputs.SLOAlertingFastburnLabel']] = None):
        """
        :param Sequence['SLOAlertingFastburnAnnotationArgs'] annotations: Annotations to attach only to Fast Burn alerts.
        :param Sequence['SLOAlertingFastburnLabelArgs'] labels: Labels to attach only to Fast Burn alerts.
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[Sequence['outputs.SLOAlertingFastburnAnnotation']]:
        """
        Annotations to attach only to Fast Burn alerts.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence['outputs.SLOAlertingFastburnLabel']]:
        """
        Labels to attach only to Fast Burn alerts.
        """
        return pulumi.get(self, "labels")


@pulumi.output_type
class SLOAlertingFastburnAnnotation(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class SLOAlertingFastburnLabel(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class SLOAlertingLabel(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class SLOAlertingSlowburn(dict):
    def __init__(__self__, *,
                 annotations: Optional[Sequence['outputs.SLOAlertingSlowburnAnnotation']] = None,
                 labels: Optional[Sequence['outputs.SLOAlertingSlowburnLabel']] = None):
        """
        :param Sequence['SLOAlertingSlowburnAnnotationArgs'] annotations: Annotations to attach only to Slow Burn alerts.
        :param Sequence['SLOAlertingSlowburnLabelArgs'] labels: Labels to attach only to Slow Burn alerts.
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[Sequence['outputs.SLOAlertingSlowburnAnnotation']]:
        """
        Annotations to attach only to Slow Burn alerts.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence['outputs.SLOAlertingSlowburnLabel']]:
        """
        Labels to attach only to Slow Burn alerts.
        """
        return pulumi.get(self, "labels")


@pulumi.output_type
class SLOAlertingSlowburnAnnotation(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class SLOAlertingSlowburnLabel(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class SLODestinationDatasource(dict):
    def __init__(__self__, *,
                 uid: Optional[str] = None):
        """
        :param str uid: UID for the Mimir Datasource
        """
        if uid is not None:
            pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter
    def uid(self) -> Optional[str]:
        """
        UID for the Mimir Datasource
        """
        return pulumi.get(self, "uid")


@pulumi.output_type
class SLOLabel(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class SLOObjective(dict):
    def __init__(__self__, *,
                 value: float,
                 window: str):
        """
        :param float value: Value between 0 and 1. If the value of the query is above the objective, the SLO is met.
        :param str window: A Prometheus-parsable time duration string like 24h, 60m. This is the time window the objective is measured over.
        """
        pulumi.set(__self__, "value", value)
        pulumi.set(__self__, "window", window)

    @property
    @pulumi.getter
    def value(self) -> float:
        """
        Value between 0 and 1. If the value of the query is above the objective, the SLO is met.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def window(self) -> str:
        """
        A Prometheus-parsable time duration string like 24h, 60m. This is the time window the objective is measured over.
        """
        return pulumi.get(self, "window")


@pulumi.output_type
class SLOQuery(dict):
    def __init__(__self__, *,
                 type: str,
                 freeform: Optional['outputs.SLOQueryFreeform'] = None,
                 ratio: Optional['outputs.SLOQueryRatio'] = None):
        """
        :param str type: Query type must be one of: "freeform", "query", "ratio", or "threshold"
        """
        pulumi.set(__self__, "type", type)
        if freeform is not None:
            pulumi.set(__self__, "freeform", freeform)
        if ratio is not None:
            pulumi.set(__self__, "ratio", ratio)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Query type must be one of: "freeform", "query", "ratio", or "threshold"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def freeform(self) -> Optional['outputs.SLOQueryFreeform']:
        return pulumi.get(self, "freeform")

    @property
    @pulumi.getter
    def ratio(self) -> Optional['outputs.SLOQueryRatio']:
        return pulumi.get(self, "ratio")


@pulumi.output_type
class SLOQueryFreeform(dict):
    def __init__(__self__, *,
                 query: str):
        """
        :param str query: Freeform Query Field
        """
        pulumi.set(__self__, "query", query)

    @property
    @pulumi.getter
    def query(self) -> str:
        """
        Freeform Query Field
        """
        return pulumi.get(self, "query")


@pulumi.output_type
class SLOQueryRatio(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "successMetric":
            suggest = "success_metric"
        elif key == "totalMetric":
            suggest = "total_metric"
        elif key == "groupByLabels":
            suggest = "group_by_labels"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SLOQueryRatio. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SLOQueryRatio.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SLOQueryRatio.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 success_metric: str,
                 total_metric: str,
                 group_by_labels: Optional[Sequence[str]] = None):
        """
        :param str success_metric: Counter metric for success events (numerator)
        :param str total_metric: Metric for total events (denominator)
        :param Sequence[str] group_by_labels: Defines Group By Labels used for per-label alerting. These appear as variables on SLO dashboards to enable filtering and aggregation. Labels must adhere to Prometheus label name schema - "^[a-zA-Z*][a-zA-Z0-9*]*$"
        """
        pulumi.set(__self__, "success_metric", success_metric)
        pulumi.set(__self__, "total_metric", total_metric)
        if group_by_labels is not None:
            pulumi.set(__self__, "group_by_labels", group_by_labels)

    @property
    @pulumi.getter(name="successMetric")
    def success_metric(self) -> str:
        """
        Counter metric for success events (numerator)
        """
        return pulumi.get(self, "success_metric")

    @property
    @pulumi.getter(name="totalMetric")
    def total_metric(self) -> str:
        """
        Metric for total events (denominator)
        """
        return pulumi.get(self, "total_metric")

    @property
    @pulumi.getter(name="groupByLabels")
    def group_by_labels(self) -> Optional[Sequence[str]]:
        """
        Defines Group By Labels used for per-label alerting. These appear as variables on SLO dashboards to enable filtering and aggregation. Labels must adhere to Prometheus label name schema - "^[a-zA-Z*][a-zA-Z0-9*]*$"
        """
        return pulumi.get(self, "group_by_labels")


@pulumi.output_type
class GetSlosSloResult(dict):
    def __init__(__self__, *,
                 alertings: Sequence['outputs.GetSlosSloAlertingResult'],
                 description: str,
                 destination_datasources: Sequence['outputs.GetSlosSloDestinationDatasourceResult'],
                 labels: Sequence['outputs.GetSlosSloLabelResult'],
                 name: str,
                 objectives: Sequence['outputs.GetSlosSloObjectiveResult'],
                 queries: Sequence['outputs.GetSlosSloQueryResult'],
                 uuid: str):
        """
        :param Sequence['GetSlosSloAlertingArgs'] alertings: Configures the alerting rules that will be generated for each
               				time window associated with the SLO. Grafana SLOs can generate
               				alerts when the short-term error budget burn is very high, the
               				long-term error budget burn rate is high, or when the remaining
               				error budget is below a certain threshold. Annotations and Labels support templating.
        :param str description: Description is a free-text field that can provide more context to an SLO.
        :param Sequence['GetSlosSloDestinationDatasourceArgs'] destination_datasources: Destination Datasource sets the datasource defined for an SLO
        :param Sequence['GetSlosSloLabelArgs'] labels: Additional labels that will be attached to all metrics generated from the query. These labels are useful for grouping SLOs in dashboard views that you create by hand. Labels must adhere to Prometheus label name schema - "^[a-zA-Z_][a-zA-Z0-9_]*$"
        :param str name: Name should be a short description of your indicator. Consider names like "API Availability"
        :param Sequence['GetSlosSloObjectiveArgs'] objectives: Over each rolling time window, the remaining error budget will be calculated, and separate alerts can be generated for each time window based on the SLO burn rate or remaining error budget.
        :param Sequence['GetSlosSloQueryArgs'] queries: Query describes the indicator that will be measured against the objective. Freeform Query types are currently supported.
        :param str uuid: A unique, random identifier. This value will also be the name of the resource stored in the API server. This value is read-only.
        """
        pulumi.set(__self__, "alertings", alertings)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "destination_datasources", destination_datasources)
        pulumi.set(__self__, "labels", labels)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "objectives", objectives)
        pulumi.set(__self__, "queries", queries)
        pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter
    def alertings(self) -> Sequence['outputs.GetSlosSloAlertingResult']:
        """
        Configures the alerting rules that will be generated for each
        				time window associated with the SLO. Grafana SLOs can generate
        				alerts when the short-term error budget burn is very high, the
        				long-term error budget burn rate is high, or when the remaining
        				error budget is below a certain threshold. Annotations and Labels support templating.
        """
        return pulumi.get(self, "alertings")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description is a free-text field that can provide more context to an SLO.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationDatasources")
    def destination_datasources(self) -> Sequence['outputs.GetSlosSloDestinationDatasourceResult']:
        """
        Destination Datasource sets the datasource defined for an SLO
        """
        return pulumi.get(self, "destination_datasources")

    @property
    @pulumi.getter
    def labels(self) -> Sequence['outputs.GetSlosSloLabelResult']:
        """
        Additional labels that will be attached to all metrics generated from the query. These labels are useful for grouping SLOs in dashboard views that you create by hand. Labels must adhere to Prometheus label name schema - "^[a-zA-Z_][a-zA-Z0-9_]*$"
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name should be a short description of your indicator. Consider names like "API Availability"
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def objectives(self) -> Sequence['outputs.GetSlosSloObjectiveResult']:
        """
        Over each rolling time window, the remaining error budget will be calculated, and separate alerts can be generated for each time window based on the SLO burn rate or remaining error budget.
        """
        return pulumi.get(self, "objectives")

    @property
    @pulumi.getter
    def queries(self) -> Sequence['outputs.GetSlosSloQueryResult']:
        """
        Query describes the indicator that will be measured against the objective. Freeform Query types are currently supported.
        """
        return pulumi.get(self, "queries")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        A unique, random identifier. This value will also be the name of the resource stored in the API server. This value is read-only.
        """
        return pulumi.get(self, "uuid")


@pulumi.output_type
class GetSlosSloAlertingResult(dict):
    def __init__(__self__, *,
                 annotations: Optional[Sequence['outputs.GetSlosSloAlertingAnnotationResult']] = None,
                 fastburns: Optional[Sequence['outputs.GetSlosSloAlertingFastburnResult']] = None,
                 labels: Optional[Sequence['outputs.GetSlosSloAlertingLabelResult']] = None,
                 slowburns: Optional[Sequence['outputs.GetSlosSloAlertingSlowburnResult']] = None):
        """
        :param Sequence['GetSlosSloAlertingAnnotationArgs'] annotations: Annotations will be attached to all alerts generated by any of these rules.
        :param Sequence['GetSlosSloAlertingFastburnArgs'] fastburns: Alerting Rules generated for Fast Burn alerts
        :param Sequence['GetSlosSloAlertingLabelArgs'] labels: Labels will be attached to all alerts generated by any of these rules.
        :param Sequence['GetSlosSloAlertingSlowburnArgs'] slowburns: Alerting Rules generated for Slow Burn alerts
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if fastburns is not None:
            pulumi.set(__self__, "fastburns", fastburns)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if slowburns is not None:
            pulumi.set(__self__, "slowburns", slowburns)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[Sequence['outputs.GetSlosSloAlertingAnnotationResult']]:
        """
        Annotations will be attached to all alerts generated by any of these rules.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def fastburns(self) -> Optional[Sequence['outputs.GetSlosSloAlertingFastburnResult']]:
        """
        Alerting Rules generated for Fast Burn alerts
        """
        return pulumi.get(self, "fastburns")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence['outputs.GetSlosSloAlertingLabelResult']]:
        """
        Labels will be attached to all alerts generated by any of these rules.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def slowburns(self) -> Optional[Sequence['outputs.GetSlosSloAlertingSlowburnResult']]:
        """
        Alerting Rules generated for Slow Burn alerts
        """
        return pulumi.get(self, "slowburns")


@pulumi.output_type
class GetSlosSloAlertingAnnotationResult(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class GetSlosSloAlertingFastburnResult(dict):
    def __init__(__self__, *,
                 annotations: Optional[Sequence['outputs.GetSlosSloAlertingFastburnAnnotationResult']] = None,
                 labels: Optional[Sequence['outputs.GetSlosSloAlertingFastburnLabelResult']] = None):
        """
        :param Sequence['GetSlosSloAlertingFastburnAnnotationArgs'] annotations: Annotations to attach only to Fast Burn alerts.
        :param Sequence['GetSlosSloAlertingFastburnLabelArgs'] labels: Labels to attach only to Fast Burn alerts.
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[Sequence['outputs.GetSlosSloAlertingFastburnAnnotationResult']]:
        """
        Annotations to attach only to Fast Burn alerts.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence['outputs.GetSlosSloAlertingFastburnLabelResult']]:
        """
        Labels to attach only to Fast Burn alerts.
        """
        return pulumi.get(self, "labels")


@pulumi.output_type
class GetSlosSloAlertingFastburnAnnotationResult(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class GetSlosSloAlertingFastburnLabelResult(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class GetSlosSloAlertingLabelResult(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class GetSlosSloAlertingSlowburnResult(dict):
    def __init__(__self__, *,
                 annotations: Optional[Sequence['outputs.GetSlosSloAlertingSlowburnAnnotationResult']] = None,
                 labels: Optional[Sequence['outputs.GetSlosSloAlertingSlowburnLabelResult']] = None):
        """
        :param Sequence['GetSlosSloAlertingSlowburnAnnotationArgs'] annotations: Annotations to attach only to Slow Burn alerts.
        :param Sequence['GetSlosSloAlertingSlowburnLabelArgs'] labels: Labels to attach only to Slow Burn alerts.
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[Sequence['outputs.GetSlosSloAlertingSlowburnAnnotationResult']]:
        """
        Annotations to attach only to Slow Burn alerts.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Sequence['outputs.GetSlosSloAlertingSlowburnLabelResult']]:
        """
        Labels to attach only to Slow Burn alerts.
        """
        return pulumi.get(self, "labels")


@pulumi.output_type
class GetSlosSloAlertingSlowburnAnnotationResult(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class GetSlosSloAlertingSlowburnLabelResult(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class GetSlosSloDestinationDatasourceResult(dict):
    def __init__(__self__, *,
                 uid: Optional[str] = None):
        """
        :param str uid: UID for the Mimir Datasource
        """
        if uid is not None:
            pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter
    def uid(self) -> Optional[str]:
        """
        UID for the Mimir Datasource
        """
        return pulumi.get(self, "uid")


@pulumi.output_type
class GetSlosSloLabelResult(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


@pulumi.output_type
class GetSlosSloObjectiveResult(dict):
    def __init__(__self__, *,
                 value: float,
                 window: str):
        """
        :param float value: Value between 0 and 1. If the value of the query is above the objective, the SLO is met.
        :param str window: A Prometheus-parsable time duration string like 24h, 60m. This is the time window the objective is measured over.
        """
        pulumi.set(__self__, "value", value)
        pulumi.set(__self__, "window", window)

    @property
    @pulumi.getter
    def value(self) -> float:
        """
        Value between 0 and 1. If the value of the query is above the objective, the SLO is met.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def window(self) -> str:
        """
        A Prometheus-parsable time duration string like 24h, 60m. This is the time window the objective is measured over.
        """
        return pulumi.get(self, "window")


@pulumi.output_type
class GetSlosSloQueryResult(dict):
    def __init__(__self__, *,
                 type: str,
                 freeform: Optional['outputs.GetSlosSloQueryFreeformResult'] = None,
                 ratio: Optional['outputs.GetSlosSloQueryRatioResult'] = None):
        """
        :param str type: Query type must be one of: "freeform", "query", "ratio", or "threshold"
        """
        pulumi.set(__self__, "type", type)
        if freeform is not None:
            pulumi.set(__self__, "freeform", freeform)
        if ratio is not None:
            pulumi.set(__self__, "ratio", ratio)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Query type must be one of: "freeform", "query", "ratio", or "threshold"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def freeform(self) -> Optional['outputs.GetSlosSloQueryFreeformResult']:
        return pulumi.get(self, "freeform")

    @property
    @pulumi.getter
    def ratio(self) -> Optional['outputs.GetSlosSloQueryRatioResult']:
        return pulumi.get(self, "ratio")


@pulumi.output_type
class GetSlosSloQueryFreeformResult(dict):
    def __init__(__self__, *,
                 query: str):
        """
        :param str query: Freeform Query Field
        """
        pulumi.set(__self__, "query", query)

    @property
    @pulumi.getter
    def query(self) -> str:
        """
        Freeform Query Field
        """
        return pulumi.get(self, "query")


@pulumi.output_type
class GetSlosSloQueryRatioResult(dict):
    def __init__(__self__, *,
                 success_metric: str,
                 total_metric: str,
                 group_by_labels: Optional[Sequence[str]] = None):
        """
        :param str success_metric: Counter metric for success events (numerator)
        :param str total_metric: Metric for total events (denominator)
        :param Sequence[str] group_by_labels: Defines Group By Labels used for per-label alerting. These appear as variables on SLO dashboards to enable filtering and aggregation. Labels must adhere to Prometheus label name schema - "^[a-zA-Z_][a-zA-Z0-9_]*$"
        """
        pulumi.set(__self__, "success_metric", success_metric)
        pulumi.set(__self__, "total_metric", total_metric)
        if group_by_labels is not None:
            pulumi.set(__self__, "group_by_labels", group_by_labels)

    @property
    @pulumi.getter(name="successMetric")
    def success_metric(self) -> str:
        """
        Counter metric for success events (numerator)
        """
        return pulumi.get(self, "success_metric")

    @property
    @pulumi.getter(name="totalMetric")
    def total_metric(self) -> str:
        """
        Metric for total events (denominator)
        """
        return pulumi.get(self, "total_metric")

    @property
    @pulumi.getter(name="groupByLabels")
    def group_by_labels(self) -> Optional[Sequence[str]]:
        """
        Defines Group By Labels used for per-label alerting. These appear as variables on SLO dashboards to enable filtering and aggregation. Labels must adhere to Prometheus label name schema - "^[a-zA-Z_][a-zA-Z0-9_]*$"
        """
        return pulumi.get(self, "group_by_labels")


