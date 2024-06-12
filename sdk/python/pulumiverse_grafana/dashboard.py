# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DashboardArgs', 'Dashboard']

@pulumi.input_type
class DashboardArgs:
    def __init__(__self__, *,
                 config_json: pulumi.Input[str],
                 folder: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 overwrite: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Dashboard resource.
        :param pulumi.Input[str] config_json: The complete dashboard model JSON.
        :param pulumi.Input[str] folder: The id or UID of the folder to save the dashboard in.
        :param pulumi.Input[str] message: Set a commit message for the version history.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[bool] overwrite: Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid.
        """
        pulumi.set(__self__, "config_json", config_json)
        if folder is not None:
            pulumi.set(__self__, "folder", folder)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if overwrite is not None:
            pulumi.set(__self__, "overwrite", overwrite)

    @property
    @pulumi.getter(name="configJson")
    def config_json(self) -> pulumi.Input[str]:
        """
        The complete dashboard model JSON.
        """
        return pulumi.get(self, "config_json")

    @config_json.setter
    def config_json(self, value: pulumi.Input[str]):
        pulumi.set(self, "config_json", value)

    @property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[str]]:
        """
        The id or UID of the folder to save the dashboard in.
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        Set a commit message for the version history.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

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
    @pulumi.getter
    def overwrite(self) -> Optional[pulumi.Input[bool]]:
        """
        Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid.
        """
        return pulumi.get(self, "overwrite")

    @overwrite.setter
    def overwrite(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "overwrite", value)


@pulumi.input_type
class _DashboardState:
    def __init__(__self__, *,
                 config_json: Optional[pulumi.Input[str]] = None,
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 overwrite: Optional[pulumi.Input[bool]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Dashboard resources.
        :param pulumi.Input[str] config_json: The complete dashboard model JSON.
        :param pulumi.Input[int] dashboard_id: The numeric ID of the dashboard computed by Grafana.
        :param pulumi.Input[str] folder: The id or UID of the folder to save the dashboard in.
        :param pulumi.Input[str] message: Set a commit message for the version history.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[bool] overwrite: Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid.
        :param pulumi.Input[str] uid: The unique identifier of a dashboard. This is used to construct its URL. It's automatically generated if not provided when creating a dashboard. The uid allows having consistent URLs for accessing dashboards and when syncing dashboards between multiple Grafana installs.
        :param pulumi.Input[str] url: The full URL of the dashboard.
        :param pulumi.Input[int] version: Whenever you save a version of your dashboard, a copy of that version is saved so that previous versions of your dashboard are not lost.
        """
        if config_json is not None:
            pulumi.set(__self__, "config_json", config_json)
        if dashboard_id is not None:
            pulumi.set(__self__, "dashboard_id", dashboard_id)
        if folder is not None:
            pulumi.set(__self__, "folder", folder)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if overwrite is not None:
            pulumi.set(__self__, "overwrite", overwrite)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="configJson")
    def config_json(self) -> Optional[pulumi.Input[str]]:
        """
        The complete dashboard model JSON.
        """
        return pulumi.get(self, "config_json")

    @config_json.setter
    def config_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_json", value)

    @property
    @pulumi.getter(name="dashboardId")
    def dashboard_id(self) -> Optional[pulumi.Input[int]]:
        """
        The numeric ID of the dashboard computed by Grafana.
        """
        return pulumi.get(self, "dashboard_id")

    @dashboard_id.setter
    def dashboard_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dashboard_id", value)

    @property
    @pulumi.getter
    def folder(self) -> Optional[pulumi.Input[str]]:
        """
        The id or UID of the folder to save the dashboard in.
        """
        return pulumi.get(self, "folder")

    @folder.setter
    def folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        Set a commit message for the version history.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

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
    @pulumi.getter
    def overwrite(self) -> Optional[pulumi.Input[bool]]:
        """
        Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid.
        """
        return pulumi.get(self, "overwrite")

    @overwrite.setter
    def overwrite(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "overwrite", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier of a dashboard. This is used to construct its URL. It's automatically generated if not provided when creating a dashboard. The uid allows having consistent URLs for accessing dashboards and when syncing dashboards between multiple Grafana installs.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The full URL of the dashboard.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        Whenever you save a version of your dashboard, a copy of that version is saved so that previous versions of your dashboard are not lost.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class Dashboard(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_json: Optional[pulumi.Input[str]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 overwrite: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages Grafana dashboards.

        * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/)

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import json
        import pulumiverse_grafana as grafana

        test_folder = grafana.Folder("testFolder",
            title="My Folder",
            uid="my-folder-uid")
        test_dashboard = grafana.Dashboard("testDashboard",
            folder=test_folder.uid,
            config_json=json.dumps({
                "title": "My Dashboard",
                "uid": "my-dashboard-uid",
            }))
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import grafana:index/dashboard:Dashboard name "{{ uid }}"
        ```

        ```sh
        $ pulumi import grafana:index/dashboard:Dashboard name "{{ orgID }}:{{ uid }}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config_json: The complete dashboard model JSON.
        :param pulumi.Input[str] folder: The id or UID of the folder to save the dashboard in.
        :param pulumi.Input[str] message: Set a commit message for the version history.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[bool] overwrite: Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DashboardArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages Grafana dashboards.

        * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/)

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import json
        import pulumiverse_grafana as grafana

        test_folder = grafana.Folder("testFolder",
            title="My Folder",
            uid="my-folder-uid")
        test_dashboard = grafana.Dashboard("testDashboard",
            folder=test_folder.uid,
            config_json=json.dumps({
                "title": "My Dashboard",
                "uid": "my-dashboard-uid",
            }))
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import grafana:index/dashboard:Dashboard name "{{ uid }}"
        ```

        ```sh
        $ pulumi import grafana:index/dashboard:Dashboard name "{{ orgID }}:{{ uid }}"
        ```

        :param str resource_name: The name of the resource.
        :param DashboardArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DashboardArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_json: Optional[pulumi.Input[str]] = None,
                 folder: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 overwrite: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DashboardArgs.__new__(DashboardArgs)

            if config_json is None and not opts.urn:
                raise TypeError("Missing required property 'config_json'")
            __props__.__dict__["config_json"] = config_json
            __props__.__dict__["folder"] = folder
            __props__.__dict__["message"] = message
            __props__.__dict__["org_id"] = org_id
            __props__.__dict__["overwrite"] = overwrite
            __props__.__dict__["dashboard_id"] = None
            __props__.__dict__["uid"] = None
            __props__.__dict__["url"] = None
            __props__.__dict__["version"] = None
        super(Dashboard, __self__).__init__(
            'grafana:index/dashboard:Dashboard',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config_json: Optional[pulumi.Input[str]] = None,
            dashboard_id: Optional[pulumi.Input[int]] = None,
            folder: Optional[pulumi.Input[str]] = None,
            message: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            overwrite: Optional[pulumi.Input[bool]] = None,
            uid: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'Dashboard':
        """
        Get an existing Dashboard resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config_json: The complete dashboard model JSON.
        :param pulumi.Input[int] dashboard_id: The numeric ID of the dashboard computed by Grafana.
        :param pulumi.Input[str] folder: The id or UID of the folder to save the dashboard in.
        :param pulumi.Input[str] message: Set a commit message for the version history.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[bool] overwrite: Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid.
        :param pulumi.Input[str] uid: The unique identifier of a dashboard. This is used to construct its URL. It's automatically generated if not provided when creating a dashboard. The uid allows having consistent URLs for accessing dashboards and when syncing dashboards between multiple Grafana installs.
        :param pulumi.Input[str] url: The full URL of the dashboard.
        :param pulumi.Input[int] version: Whenever you save a version of your dashboard, a copy of that version is saved so that previous versions of your dashboard are not lost.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DashboardState.__new__(_DashboardState)

        __props__.__dict__["config_json"] = config_json
        __props__.__dict__["dashboard_id"] = dashboard_id
        __props__.__dict__["folder"] = folder
        __props__.__dict__["message"] = message
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["overwrite"] = overwrite
        __props__.__dict__["uid"] = uid
        __props__.__dict__["url"] = url
        __props__.__dict__["version"] = version
        return Dashboard(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="configJson")
    def config_json(self) -> pulumi.Output[str]:
        """
        The complete dashboard model JSON.
        """
        return pulumi.get(self, "config_json")

    @property
    @pulumi.getter(name="dashboardId")
    def dashboard_id(self) -> pulumi.Output[int]:
        """
        The numeric ID of the dashboard computed by Grafana.
        """
        return pulumi.get(self, "dashboard_id")

    @property
    @pulumi.getter
    def folder(self) -> pulumi.Output[Optional[str]]:
        """
        The id or UID of the folder to save the dashboard in.
        """
        return pulumi.get(self, "folder")

    @property
    @pulumi.getter
    def message(self) -> pulumi.Output[Optional[str]]:
        """
        Set a commit message for the version history.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def overwrite(self) -> pulumi.Output[Optional[bool]]:
        """
        Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid.
        """
        return pulumi.get(self, "overwrite")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        The unique identifier of a dashboard. This is used to construct its URL. It's automatically generated if not provided when creating a dashboard. The uid allows having consistent URLs for accessing dashboards and when syncing dashboards between multiple Grafana installs.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The full URL of the dashboard.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        Whenever you save a version of your dashboard, a copy of that version is saved so that previous versions of your dashboard are not lost.
        """
        return pulumi.get(self, "version")

