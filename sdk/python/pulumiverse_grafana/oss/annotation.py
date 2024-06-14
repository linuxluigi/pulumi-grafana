# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AnnotationArgs', 'Annotation']

@pulumi.input_type
class AnnotationArgs:
    def __init__(__self__, *,
                 text: pulumi.Input[str],
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 panel_id: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 time: Optional[pulumi.Input[str]] = None,
                 time_end: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Annotation resource.
        :param pulumi.Input[str] text: The text to associate with the annotation.
        :param pulumi.Input[int] dashboard_id: The ID of the dashboard on which to create the annotation. Deprecated: Use dashboard_uid instead.
        :param pulumi.Input[str] dashboard_uid: The ID of the dashboard on which to create the annotation.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[int] panel_id: The ID of the dashboard panel on which to create the annotation.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags to associate with the annotation.
        :param pulumi.Input[str] time: The RFC 3339-formatted time string indicating the annotation's time.
        :param pulumi.Input[str] time_end: The RFC 3339-formatted time string indicating the annotation's end time.
        """
        pulumi.set(__self__, "text", text)
        if dashboard_id is not None:
            warnings.warn("""Use dashboard_uid instead.""", DeprecationWarning)
            pulumi.log.warn("""dashboard_id is deprecated: Use dashboard_uid instead.""")
        if dashboard_id is not None:
            pulumi.set(__self__, "dashboard_id", dashboard_id)
        if dashboard_uid is not None:
            pulumi.set(__self__, "dashboard_uid", dashboard_uid)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if panel_id is not None:
            pulumi.set(__self__, "panel_id", panel_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if time is not None:
            pulumi.set(__self__, "time", time)
        if time_end is not None:
            pulumi.set(__self__, "time_end", time_end)

    @property
    @pulumi.getter
    def text(self) -> pulumi.Input[str]:
        """
        The text to associate with the annotation.
        """
        return pulumi.get(self, "text")

    @text.setter
    def text(self, value: pulumi.Input[str]):
        pulumi.set(self, "text", value)

    @property
    @pulumi.getter(name="dashboardId")
    def dashboard_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the dashboard on which to create the annotation. Deprecated: Use dashboard_uid instead.
        """
        warnings.warn("""Use dashboard_uid instead.""", DeprecationWarning)
        pulumi.log.warn("""dashboard_id is deprecated: Use dashboard_uid instead.""")

        return pulumi.get(self, "dashboard_id")

    @dashboard_id.setter
    def dashboard_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dashboard_id", value)

    @property
    @pulumi.getter(name="dashboardUid")
    def dashboard_uid(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the dashboard on which to create the annotation.
        """
        return pulumi.get(self, "dashboard_uid")

    @dashboard_uid.setter
    def dashboard_uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_uid", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="panelId")
    def panel_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the dashboard panel on which to create the annotation.
        """
        return pulumi.get(self, "panel_id")

    @panel_id.setter
    def panel_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "panel_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags to associate with the annotation.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def time(self) -> Optional[pulumi.Input[str]]:
        """
        The RFC 3339-formatted time string indicating the annotation's time.
        """
        return pulumi.get(self, "time")

    @time.setter
    def time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time", value)

    @property
    @pulumi.getter(name="timeEnd")
    def time_end(self) -> Optional[pulumi.Input[str]]:
        """
        The RFC 3339-formatted time string indicating the annotation's end time.
        """
        return pulumi.get(self, "time_end")

    @time_end.setter
    def time_end(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_end", value)


@pulumi.input_type
class _AnnotationState:
    def __init__(__self__, *,
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 panel_id: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 text: Optional[pulumi.Input[str]] = None,
                 time: Optional[pulumi.Input[str]] = None,
                 time_end: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Annotation resources.
        :param pulumi.Input[int] dashboard_id: The ID of the dashboard on which to create the annotation. Deprecated: Use dashboard_uid instead.
        :param pulumi.Input[str] dashboard_uid: The ID of the dashboard on which to create the annotation.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[int] panel_id: The ID of the dashboard panel on which to create the annotation.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags to associate with the annotation.
        :param pulumi.Input[str] text: The text to associate with the annotation.
        :param pulumi.Input[str] time: The RFC 3339-formatted time string indicating the annotation's time.
        :param pulumi.Input[str] time_end: The RFC 3339-formatted time string indicating the annotation's end time.
        """
        if dashboard_id is not None:
            warnings.warn("""Use dashboard_uid instead.""", DeprecationWarning)
            pulumi.log.warn("""dashboard_id is deprecated: Use dashboard_uid instead.""")
        if dashboard_id is not None:
            pulumi.set(__self__, "dashboard_id", dashboard_id)
        if dashboard_uid is not None:
            pulumi.set(__self__, "dashboard_uid", dashboard_uid)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if panel_id is not None:
            pulumi.set(__self__, "panel_id", panel_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if text is not None:
            pulumi.set(__self__, "text", text)
        if time is not None:
            pulumi.set(__self__, "time", time)
        if time_end is not None:
            pulumi.set(__self__, "time_end", time_end)

    @property
    @pulumi.getter(name="dashboardId")
    def dashboard_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the dashboard on which to create the annotation. Deprecated: Use dashboard_uid instead.
        """
        warnings.warn("""Use dashboard_uid instead.""", DeprecationWarning)
        pulumi.log.warn("""dashboard_id is deprecated: Use dashboard_uid instead.""")

        return pulumi.get(self, "dashboard_id")

    @dashboard_id.setter
    def dashboard_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dashboard_id", value)

    @property
    @pulumi.getter(name="dashboardUid")
    def dashboard_uid(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the dashboard on which to create the annotation.
        """
        return pulumi.get(self, "dashboard_uid")

    @dashboard_uid.setter
    def dashboard_uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_uid", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter(name="panelId")
    def panel_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the dashboard panel on which to create the annotation.
        """
        return pulumi.get(self, "panel_id")

    @panel_id.setter
    def panel_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "panel_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags to associate with the annotation.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[str]]:
        """
        The text to associate with the annotation.
        """
        return pulumi.get(self, "text")

    @text.setter
    def text(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "text", value)

    @property
    @pulumi.getter
    def time(self) -> Optional[pulumi.Input[str]]:
        """
        The RFC 3339-formatted time string indicating the annotation's time.
        """
        return pulumi.get(self, "time")

    @time.setter
    def time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time", value)

    @property
    @pulumi.getter(name="timeEnd")
    def time_end(self) -> Optional[pulumi.Input[str]]:
        """
        The RFC 3339-formatted time string indicating the annotation's end time.
        """
        return pulumi.get(self, "time_end")

    @time_end.setter
    def time_end(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_end", value)


class Annotation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 panel_id: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 text: Optional[pulumi.Input[str]] = None,
                 time: Optional[pulumi.Input[str]] = None,
                 time_end: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/annotate-visualizations/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/annotations/)

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_grafana as grafana

        test = grafana.oss.Annotation("test", text="basic text")
        ```

        ## Import

        ```sh
        $ pulumi import grafana:oss/annotation:Annotation name "{{ id }}"
        ```

        ```sh
        $ pulumi import grafana:oss/annotation:Annotation name "{{ orgID }}:{{ id }}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] dashboard_id: The ID of the dashboard on which to create the annotation. Deprecated: Use dashboard_uid instead.
        :param pulumi.Input[str] dashboard_uid: The ID of the dashboard on which to create the annotation.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[int] panel_id: The ID of the dashboard panel on which to create the annotation.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags to associate with the annotation.
        :param pulumi.Input[str] text: The text to associate with the annotation.
        :param pulumi.Input[str] time: The RFC 3339-formatted time string indicating the annotation's time.
        :param pulumi.Input[str] time_end: The RFC 3339-formatted time string indicating the annotation's end time.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AnnotationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/annotate-visualizations/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/annotations/)

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_grafana as grafana

        test = grafana.oss.Annotation("test", text="basic text")
        ```

        ## Import

        ```sh
        $ pulumi import grafana:oss/annotation:Annotation name "{{ id }}"
        ```

        ```sh
        $ pulumi import grafana:oss/annotation:Annotation name "{{ orgID }}:{{ id }}"
        ```

        :param str resource_name: The name of the resource.
        :param AnnotationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AnnotationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 panel_id: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 text: Optional[pulumi.Input[str]] = None,
                 time: Optional[pulumi.Input[str]] = None,
                 time_end: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AnnotationArgs.__new__(AnnotationArgs)

            __props__.__dict__["dashboard_id"] = dashboard_id
            __props__.__dict__["dashboard_uid"] = dashboard_uid
            __props__.__dict__["org_id"] = org_id
            __props__.__dict__["panel_id"] = panel_id
            __props__.__dict__["tags"] = tags
            if text is None and not opts.urn:
                raise TypeError("Missing required property 'text'")
            __props__.__dict__["text"] = text
            __props__.__dict__["time"] = time
            __props__.__dict__["time_end"] = time_end
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="grafana:index/annotation:Annotation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Annotation, __self__).__init__(
            'grafana:oss/annotation:Annotation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dashboard_id: Optional[pulumi.Input[int]] = None,
            dashboard_uid: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            panel_id: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            text: Optional[pulumi.Input[str]] = None,
            time: Optional[pulumi.Input[str]] = None,
            time_end: Optional[pulumi.Input[str]] = None) -> 'Annotation':
        """
        Get an existing Annotation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] dashboard_id: The ID of the dashboard on which to create the annotation. Deprecated: Use dashboard_uid instead.
        :param pulumi.Input[str] dashboard_uid: The ID of the dashboard on which to create the annotation.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[int] panel_id: The ID of the dashboard panel on which to create the annotation.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags to associate with the annotation.
        :param pulumi.Input[str] text: The text to associate with the annotation.
        :param pulumi.Input[str] time: The RFC 3339-formatted time string indicating the annotation's time.
        :param pulumi.Input[str] time_end: The RFC 3339-formatted time string indicating the annotation's end time.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AnnotationState.__new__(_AnnotationState)

        __props__.__dict__["dashboard_id"] = dashboard_id
        __props__.__dict__["dashboard_uid"] = dashboard_uid
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["panel_id"] = panel_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["text"] = text
        __props__.__dict__["time"] = time
        __props__.__dict__["time_end"] = time_end
        return Annotation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dashboardId")
    def dashboard_id(self) -> pulumi.Output[Optional[int]]:
        """
        The ID of the dashboard on which to create the annotation. Deprecated: Use dashboard_uid instead.
        """
        warnings.warn("""Use dashboard_uid instead.""", DeprecationWarning)
        pulumi.log.warn("""dashboard_id is deprecated: Use dashboard_uid instead.""")

        return pulumi.get(self, "dashboard_id")

    @property
    @pulumi.getter(name="dashboardUid")
    def dashboard_uid(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the dashboard on which to create the annotation.
        """
        return pulumi.get(self, "dashboard_uid")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter(name="panelId")
    def panel_id(self) -> pulumi.Output[Optional[int]]:
        """
        The ID of the dashboard panel on which to create the annotation.
        """
        return pulumi.get(self, "panel_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The tags to associate with the annotation.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def text(self) -> pulumi.Output[str]:
        """
        The text to associate with the annotation.
        """
        return pulumi.get(self, "text")

    @property
    @pulumi.getter
    def time(self) -> pulumi.Output[str]:
        """
        The RFC 3339-formatted time string indicating the annotation's time.
        """
        return pulumi.get(self, "time")

    @property
    @pulumi.getter(name="timeEnd")
    def time_end(self) -> pulumi.Output[str]:
        """
        The RFC 3339-formatted time string indicating the annotation's end time.
        """
        return pulumi.get(self, "time_end")

