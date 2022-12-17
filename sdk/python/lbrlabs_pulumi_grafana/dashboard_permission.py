# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DashboardPermissionArgs', 'DashboardPermission']

@pulumi.input_type
class DashboardPermissionArgs:
    def __init__(__self__, *,
                 permissions: pulumi.Input[Sequence[pulumi.Input['DashboardPermissionPermissionArgs']]],
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DashboardPermission resource.
        :param pulumi.Input[Sequence[pulumi.Input['DashboardPermissionPermissionArgs']]] permissions: The permission items to add/update. Items that are omitted from the list will be removed.
        :param pulumi.Input[int] dashboard_id: ID of the dashboard to apply permissions to. Deprecated: use `dashboard_uid` instead.
        :param pulumi.Input[str] dashboard_uid: UID of the dashboard to apply permissions to.
        """
        pulumi.set(__self__, "permissions", permissions)
        if dashboard_id is not None:
            warnings.warn("""use `dashboard_uid` instead""", DeprecationWarning)
            pulumi.log.warn("""dashboard_id is deprecated: use `dashboard_uid` instead""")
        if dashboard_id is not None:
            pulumi.set(__self__, "dashboard_id", dashboard_id)
        if dashboard_uid is not None:
            pulumi.set(__self__, "dashboard_uid", dashboard_uid)

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Input[Sequence[pulumi.Input['DashboardPermissionPermissionArgs']]]:
        """
        The permission items to add/update. Items that are omitted from the list will be removed.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: pulumi.Input[Sequence[pulumi.Input['DashboardPermissionPermissionArgs']]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="dashboardId")
    def dashboard_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the dashboard to apply permissions to. Deprecated: use `dashboard_uid` instead.
        """
        return pulumi.get(self, "dashboard_id")

    @dashboard_id.setter
    def dashboard_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dashboard_id", value)

    @property
    @pulumi.getter(name="dashboardUid")
    def dashboard_uid(self) -> Optional[pulumi.Input[str]]:
        """
        UID of the dashboard to apply permissions to.
        """
        return pulumi.get(self, "dashboard_uid")

    @dashboard_uid.setter
    def dashboard_uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_uid", value)


@pulumi.input_type
class _DashboardPermissionState:
    def __init__(__self__, *,
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['DashboardPermissionPermissionArgs']]]] = None):
        """
        Input properties used for looking up and filtering DashboardPermission resources.
        :param pulumi.Input[int] dashboard_id: ID of the dashboard to apply permissions to. Deprecated: use `dashboard_uid` instead.
        :param pulumi.Input[str] dashboard_uid: UID of the dashboard to apply permissions to.
        :param pulumi.Input[Sequence[pulumi.Input['DashboardPermissionPermissionArgs']]] permissions: The permission items to add/update. Items that are omitted from the list will be removed.
        """
        if dashboard_id is not None:
            warnings.warn("""use `dashboard_uid` instead""", DeprecationWarning)
            pulumi.log.warn("""dashboard_id is deprecated: use `dashboard_uid` instead""")
        if dashboard_id is not None:
            pulumi.set(__self__, "dashboard_id", dashboard_id)
        if dashboard_uid is not None:
            pulumi.set(__self__, "dashboard_uid", dashboard_uid)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)

    @property
    @pulumi.getter(name="dashboardId")
    def dashboard_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the dashboard to apply permissions to. Deprecated: use `dashboard_uid` instead.
        """
        return pulumi.get(self, "dashboard_id")

    @dashboard_id.setter
    def dashboard_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dashboard_id", value)

    @property
    @pulumi.getter(name="dashboardUid")
    def dashboard_uid(self) -> Optional[pulumi.Input[str]]:
        """
        UID of the dashboard to apply permissions to.
        """
        return pulumi.get(self, "dashboard_uid")

    @dashboard_uid.setter
    def dashboard_uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_uid", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DashboardPermissionPermissionArgs']]]]:
        """
        The permission items to add/update. Items that are omitted from the list will be removed.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DashboardPermissionPermissionArgs']]]]):
        pulumi.set(self, "permissions", value)


class DashboardPermission(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DashboardPermissionPermissionArgs']]]]] = None,
                 __props__=None):
        """
        * [Official documentation](https://grafana.com/docs/grafana/latest/permissions/dashboard_folder_permissions/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/http_api/dashboard_permissions/)

        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_grafana as grafana

        team = grafana.Team("team")
        user = grafana.User("user", email="user.name@example.com")
        metrics = grafana.Dashboard("metrics", config_json=(lambda path: open(path).read())("grafana-dashboard.json"))
        collection_permission = grafana.DashboardPermission("collectionPermission",
            dashboard_uid=metrics.uid,
            permissions=[
                grafana.DashboardPermissionPermissionArgs(
                    role="Editor",
                    permission="Edit",
                ),
                grafana.DashboardPermissionPermissionArgs(
                    team_id=team.id,
                    permission="View",
                ),
                grafana.DashboardPermissionPermissionArgs(
                    user_id=user.id,
                    permission="Admin",
                ),
            ])
        ```

        ## Import

        ```sh
         $ pulumi import grafana:index/dashboardPermission:DashboardPermission dashboard_name {{dashboard_uid}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] dashboard_id: ID of the dashboard to apply permissions to. Deprecated: use `dashboard_uid` instead.
        :param pulumi.Input[str] dashboard_uid: UID of the dashboard to apply permissions to.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DashboardPermissionPermissionArgs']]]] permissions: The permission items to add/update. Items that are omitted from the list will be removed.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DashboardPermissionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        * [Official documentation](https://grafana.com/docs/grafana/latest/permissions/dashboard_folder_permissions/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/http_api/dashboard_permissions/)

        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_grafana as grafana

        team = grafana.Team("team")
        user = grafana.User("user", email="user.name@example.com")
        metrics = grafana.Dashboard("metrics", config_json=(lambda path: open(path).read())("grafana-dashboard.json"))
        collection_permission = grafana.DashboardPermission("collectionPermission",
            dashboard_uid=metrics.uid,
            permissions=[
                grafana.DashboardPermissionPermissionArgs(
                    role="Editor",
                    permission="Edit",
                ),
                grafana.DashboardPermissionPermissionArgs(
                    team_id=team.id,
                    permission="View",
                ),
                grafana.DashboardPermissionPermissionArgs(
                    user_id=user.id,
                    permission="Admin",
                ),
            ])
        ```

        ## Import

        ```sh
         $ pulumi import grafana:index/dashboardPermission:DashboardPermission dashboard_name {{dashboard_uid}}
        ```

        :param str resource_name: The name of the resource.
        :param DashboardPermissionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DashboardPermissionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_id: Optional[pulumi.Input[int]] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DashboardPermissionPermissionArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DashboardPermissionArgs.__new__(DashboardPermissionArgs)

            if dashboard_id is not None and not opts.urn:
                warnings.warn("""use `dashboard_uid` instead""", DeprecationWarning)
                pulumi.log.warn("""dashboard_id is deprecated: use `dashboard_uid` instead""")
            __props__.__dict__["dashboard_id"] = dashboard_id
            __props__.__dict__["dashboard_uid"] = dashboard_uid
            if permissions is None and not opts.urn:
                raise TypeError("Missing required property 'permissions'")
            __props__.__dict__["permissions"] = permissions
        super(DashboardPermission, __self__).__init__(
            'grafana:index/dashboardPermission:DashboardPermission',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dashboard_id: Optional[pulumi.Input[int]] = None,
            dashboard_uid: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DashboardPermissionPermissionArgs']]]]] = None) -> 'DashboardPermission':
        """
        Get an existing DashboardPermission resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] dashboard_id: ID of the dashboard to apply permissions to. Deprecated: use `dashboard_uid` instead.
        :param pulumi.Input[str] dashboard_uid: UID of the dashboard to apply permissions to.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DashboardPermissionPermissionArgs']]]] permissions: The permission items to add/update. Items that are omitted from the list will be removed.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DashboardPermissionState.__new__(_DashboardPermissionState)

        __props__.__dict__["dashboard_id"] = dashboard_id
        __props__.__dict__["dashboard_uid"] = dashboard_uid
        __props__.__dict__["permissions"] = permissions
        return DashboardPermission(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dashboardId")
    def dashboard_id(self) -> pulumi.Output[int]:
        """
        ID of the dashboard to apply permissions to. Deprecated: use `dashboard_uid` instead.
        """
        return pulumi.get(self, "dashboard_id")

    @property
    @pulumi.getter(name="dashboardUid")
    def dashboard_uid(self) -> pulumi.Output[str]:
        """
        UID of the dashboard to apply permissions to.
        """
        return pulumi.get(self, "dashboard_uid")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Sequence['outputs.DashboardPermissionPermission']]:
        """
        The permission items to add/update. Items that are omitted from the list will be removed.
        """
        return pulumi.get(self, "permissions")

