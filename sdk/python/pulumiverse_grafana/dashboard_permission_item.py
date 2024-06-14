# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DashboardPermissionItemArgs', 'DashboardPermissionItem']

@pulumi.input_type
class DashboardPermissionItemArgs:
    def __init__(__self__, *,
                 dashboard_uid: pulumi.Input[str],
                 permission: pulumi.Input[str],
                 org_id: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 team: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DashboardPermissionItem resource.
        :param pulumi.Input[str] dashboard_uid: The UID of the dashboard.
        :param pulumi.Input[str] permission: the permission to be assigned
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[str] role: the role onto which the permission is to be assigned
        :param pulumi.Input[str] team: the team onto which the permission is to be assigned
        :param pulumi.Input[str] user: the user or service account onto which the permission is to be assigned
        """
        pulumi.set(__self__, "dashboard_uid", dashboard_uid)
        pulumi.set(__self__, "permission", permission)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if team is not None:
            pulumi.set(__self__, "team", team)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter(name="dashboardUid")
    def dashboard_uid(self) -> pulumi.Input[str]:
        """
        The UID of the dashboard.
        """
        return pulumi.get(self, "dashboard_uid")

    @dashboard_uid.setter
    def dashboard_uid(self, value: pulumi.Input[str]):
        pulumi.set(self, "dashboard_uid", value)

    @property
    @pulumi.getter
    def permission(self) -> pulumi.Input[str]:
        """
        the permission to be assigned
        """
        return pulumi.get(self, "permission")

    @permission.setter
    def permission(self, value: pulumi.Input[str]):
        pulumi.set(self, "permission", value)

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
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        the role onto which the permission is to be assigned
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def team(self) -> Optional[pulumi.Input[str]]:
        """
        the team onto which the permission is to be assigned
        """
        return pulumi.get(self, "team")

    @team.setter
    def team(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        the user or service account onto which the permission is to be assigned
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


@pulumi.input_type
class _DashboardPermissionItemState:
    def __init__(__self__, *,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 permission: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 team: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DashboardPermissionItem resources.
        :param pulumi.Input[str] dashboard_uid: The UID of the dashboard.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[str] permission: the permission to be assigned
        :param pulumi.Input[str] role: the role onto which the permission is to be assigned
        :param pulumi.Input[str] team: the team onto which the permission is to be assigned
        :param pulumi.Input[str] user: the user or service account onto which the permission is to be assigned
        """
        if dashboard_uid is not None:
            pulumi.set(__self__, "dashboard_uid", dashboard_uid)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if permission is not None:
            pulumi.set(__self__, "permission", permission)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if team is not None:
            pulumi.set(__self__, "team", team)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter(name="dashboardUid")
    def dashboard_uid(self) -> Optional[pulumi.Input[str]]:
        """
        The UID of the dashboard.
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
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[str]]:
        """
        the permission to be assigned
        """
        return pulumi.get(self, "permission")

    @permission.setter
    def permission(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "permission", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        the role onto which the permission is to be assigned
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter
    def team(self) -> Optional[pulumi.Input[str]]:
        """
        the team onto which the permission is to be assigned
        """
        return pulumi.get(self, "team")

    @team.setter
    def team(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        the user or service account onto which the permission is to be assigned
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


warnings.warn("""grafana.index/dashboardpermissionitem.DashboardPermissionItem has been deprecated in favor of grafana.oss/dashboardpermissionitem.DashboardPermissionItem""", DeprecationWarning)


class DashboardPermissionItem(pulumi.CustomResource):
    warnings.warn("""grafana.index/dashboardpermissionitem.DashboardPermissionItem has been deprecated in favor of grafana.oss/dashboardpermissionitem.DashboardPermissionItem""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 permission: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 team: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a DashboardPermissionItem resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dashboard_uid: The UID of the dashboard.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[str] permission: the permission to be assigned
        :param pulumi.Input[str] role: the role onto which the permission is to be assigned
        :param pulumi.Input[str] team: the team onto which the permission is to be assigned
        :param pulumi.Input[str] user: the user or service account onto which the permission is to be assigned
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DashboardPermissionItemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DashboardPermissionItem resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DashboardPermissionItemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DashboardPermissionItemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_uid: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 permission: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 team: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""DashboardPermissionItem is deprecated: grafana.index/dashboardpermissionitem.DashboardPermissionItem has been deprecated in favor of grafana.oss/dashboardpermissionitem.DashboardPermissionItem""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DashboardPermissionItemArgs.__new__(DashboardPermissionItemArgs)

            if dashboard_uid is None and not opts.urn:
                raise TypeError("Missing required property 'dashboard_uid'")
            __props__.__dict__["dashboard_uid"] = dashboard_uid
            __props__.__dict__["org_id"] = org_id
            if permission is None and not opts.urn:
                raise TypeError("Missing required property 'permission'")
            __props__.__dict__["permission"] = permission
            __props__.__dict__["role"] = role
            __props__.__dict__["team"] = team
            __props__.__dict__["user"] = user
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="grafana:index/dashboardPermissionItem:DashboardPermissionItem")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DashboardPermissionItem, __self__).__init__(
            'grafana:index/dashboardPermissionItem:DashboardPermissionItem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dashboard_uid: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            permission: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None,
            team: Optional[pulumi.Input[str]] = None,
            user: Optional[pulumi.Input[str]] = None) -> 'DashboardPermissionItem':
        """
        Get an existing DashboardPermissionItem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dashboard_uid: The UID of the dashboard.
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[str] permission: the permission to be assigned
        :param pulumi.Input[str] role: the role onto which the permission is to be assigned
        :param pulumi.Input[str] team: the team onto which the permission is to be assigned
        :param pulumi.Input[str] user: the user or service account onto which the permission is to be assigned
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DashboardPermissionItemState.__new__(_DashboardPermissionItemState)

        __props__.__dict__["dashboard_uid"] = dashboard_uid
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["permission"] = permission
        __props__.__dict__["role"] = role
        __props__.__dict__["team"] = team
        __props__.__dict__["user"] = user
        return DashboardPermissionItem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dashboardUid")
    def dashboard_uid(self) -> pulumi.Output[str]:
        """
        The UID of the dashboard.
        """
        return pulumi.get(self, "dashboard_uid")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[str]:
        """
        The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def permission(self) -> pulumi.Output[str]:
        """
        the permission to be assigned
        """
        return pulumi.get(self, "permission")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[Optional[str]]:
        """
        the role onto which the permission is to be assigned
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter
    def team(self) -> pulumi.Output[Optional[str]]:
        """
        the team onto which the permission is to be assigned
        """
        return pulumi.get(self, "team")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[Optional[str]]:
        """
        the user or service account onto which the permission is to be assigned
        """
        return pulumi.get(self, "user")

