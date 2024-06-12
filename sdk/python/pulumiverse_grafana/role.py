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

__all__ = ['RoleArgs', 'Role']

@pulumi.input_type
class RoleArgs:
    def __init__(__self__, *,
                 auto_increment_version: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 global_: Optional[pulumi.Input[bool]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 hidden: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Role resource.
        :param pulumi.Input[bool] auto_increment_version: Whether the role version should be incremented automatically on updates (and set to 1 on creation). This field or `version` should be set.
        :param pulumi.Input[str] description: Description of the role.
        :param pulumi.Input[str] display_name: Display name of the role. Available with Grafana 8.5+.
        :param pulumi.Input[bool] global_: Boolean to state whether the role is available across all organizations or not. Defaults to `false`.
        :param pulumi.Input[str] group: Group of the role. Available with Grafana 8.5+.
        :param pulumi.Input[bool] hidden: Boolean to state whether the role should be visible in the Grafana UI or not. Available with Grafana 8.5+. Defaults to `false`.
        :param pulumi.Input[str] name: Name of the role
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]] permissions: Specific set of actions granted by the role.
        :param pulumi.Input[str] uid: Unique identifier of the role. Used for assignments.
        :param pulumi.Input[int] version: Version of the role. A role is updated only on version increase. This field or `auto_increment_version` should be set.
        """
        if auto_increment_version is not None:
            pulumi.set(__self__, "auto_increment_version", auto_increment_version)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if global_ is not None:
            pulumi.set(__self__, "global_", global_)
        if group is not None:
            pulumi.set(__self__, "group", group)
        if hidden is not None:
            pulumi.set(__self__, "hidden", hidden)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="autoIncrementVersion")
    def auto_increment_version(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the role version should be incremented automatically on updates (and set to 1 on creation). This field or `version` should be set.
        """
        return pulumi.get(self, "auto_increment_version")

    @auto_increment_version.setter
    def auto_increment_version(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_increment_version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the role.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the role. Available with Grafana 8.5+.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="global")
    def global_(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean to state whether the role is available across all organizations or not. Defaults to `false`.
        """
        return pulumi.get(self, "global_")

    @global_.setter
    def global_(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "global_", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        Group of the role. Available with Grafana 8.5+.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter
    def hidden(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean to state whether the role should be visible in the Grafana UI or not. Available with Grafana 8.5+. Defaults to `false`.
        """
        return pulumi.get(self, "hidden")

    @hidden.setter
    def hidden(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hidden", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the role
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]]]:
        """
        Specific set of actions granted by the role.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the role. Used for assignments.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        Version of the role. A role is updated only on version increase. This field or `auto_increment_version` should be set.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class _RoleState:
    def __init__(__self__, *,
                 auto_increment_version: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 global_: Optional[pulumi.Input[bool]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 hidden: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Role resources.
        :param pulumi.Input[bool] auto_increment_version: Whether the role version should be incremented automatically on updates (and set to 1 on creation). This field or `version` should be set.
        :param pulumi.Input[str] description: Description of the role.
        :param pulumi.Input[str] display_name: Display name of the role. Available with Grafana 8.5+.
        :param pulumi.Input[bool] global_: Boolean to state whether the role is available across all organizations or not. Defaults to `false`.
        :param pulumi.Input[str] group: Group of the role. Available with Grafana 8.5+.
        :param pulumi.Input[bool] hidden: Boolean to state whether the role should be visible in the Grafana UI or not. Available with Grafana 8.5+. Defaults to `false`.
        :param pulumi.Input[str] name: Name of the role
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]] permissions: Specific set of actions granted by the role.
        :param pulumi.Input[str] uid: Unique identifier of the role. Used for assignments.
        :param pulumi.Input[int] version: Version of the role. A role is updated only on version increase. This field or `auto_increment_version` should be set.
        """
        if auto_increment_version is not None:
            pulumi.set(__self__, "auto_increment_version", auto_increment_version)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if global_ is not None:
            pulumi.set(__self__, "global_", global_)
        if group is not None:
            pulumi.set(__self__, "group", group)
        if hidden is not None:
            pulumi.set(__self__, "hidden", hidden)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if uid is not None:
            pulumi.set(__self__, "uid", uid)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="autoIncrementVersion")
    def auto_increment_version(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the role version should be incremented automatically on updates (and set to 1 on creation). This field or `version` should be set.
        """
        return pulumi.get(self, "auto_increment_version")

    @auto_increment_version.setter
    def auto_increment_version(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_increment_version", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the role.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the role. Available with Grafana 8.5+.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="global")
    def global_(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean to state whether the role is available across all organizations or not. Defaults to `false`.
        """
        return pulumi.get(self, "global_")

    @global_.setter
    def global_(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "global_", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        Group of the role. Available with Grafana 8.5+.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter
    def hidden(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean to state whether the role should be visible in the Grafana UI or not. Available with Grafana 8.5+. Defaults to `false`.
        """
        return pulumi.get(self, "hidden")

    @hidden.setter
    def hidden(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "hidden", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the role
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]]]:
        """
        Specific set of actions granted by the role.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter
    def uid(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the role. Used for assignments.
        """
        return pulumi.get(self, "uid")

    @uid.setter
    def uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uid", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        Version of the role. A role is updated only on version increase. This field or `auto_increment_version` should be set.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class Role(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_increment_version: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 global_: Optional[pulumi.Input[bool]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 hidden: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RolePermissionArgs']]]]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        **Note:** This resource is available only with Grafana Enterprise 8.+.

        * [Official documentation](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/access-control/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/access_control/)

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumiverse_grafana as grafana

        super_user = grafana.Role("superUser",
            description="My Super User description",
            global_=True,
            permissions=[
                grafana.RolePermissionArgs(
                    action="org.users:add",
                    scope="users:*",
                ),
                grafana.RolePermissionArgs(
                    action="org.users:write",
                    scope="users:*",
                ),
                grafana.RolePermissionArgs(
                    action="org.users:read",
                    scope="users:*",
                ),
            ],
            uid="superuseruid",
            version=1)
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import grafana:index/role:Role name "{{ uid }}"
        ```

        ```sh
        $ pulumi import grafana:index/role:Role name "{{ orgID }}:{{ uid }}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_increment_version: Whether the role version should be incremented automatically on updates (and set to 1 on creation). This field or `version` should be set.
        :param pulumi.Input[str] description: Description of the role.
        :param pulumi.Input[str] display_name: Display name of the role. Available with Grafana 8.5+.
        :param pulumi.Input[bool] global_: Boolean to state whether the role is available across all organizations or not. Defaults to `false`.
        :param pulumi.Input[str] group: Group of the role. Available with Grafana 8.5+.
        :param pulumi.Input[bool] hidden: Boolean to state whether the role should be visible in the Grafana UI or not. Available with Grafana 8.5+. Defaults to `false`.
        :param pulumi.Input[str] name: Name of the role
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RolePermissionArgs']]]] permissions: Specific set of actions granted by the role.
        :param pulumi.Input[str] uid: Unique identifier of the role. Used for assignments.
        :param pulumi.Input[int] version: Version of the role. A role is updated only on version increase. This field or `auto_increment_version` should be set.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[RoleArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        **Note:** This resource is available only with Grafana Enterprise 8.+.

        * [Official documentation](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/access-control/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/access_control/)

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumiverse_grafana as grafana

        super_user = grafana.Role("superUser",
            description="My Super User description",
            global_=True,
            permissions=[
                grafana.RolePermissionArgs(
                    action="org.users:add",
                    scope="users:*",
                ),
                grafana.RolePermissionArgs(
                    action="org.users:write",
                    scope="users:*",
                ),
                grafana.RolePermissionArgs(
                    action="org.users:read",
                    scope="users:*",
                ),
            ],
            uid="superuseruid",
            version=1)
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import grafana:index/role:Role name "{{ uid }}"
        ```

        ```sh
        $ pulumi import grafana:index/role:Role name "{{ orgID }}:{{ uid }}"
        ```

        :param str resource_name: The name of the resource.
        :param RoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_increment_version: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 global_: Optional[pulumi.Input[bool]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 hidden: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RolePermissionArgs']]]]] = None,
                 uid: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RoleArgs.__new__(RoleArgs)

            __props__.__dict__["auto_increment_version"] = auto_increment_version
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["global_"] = global_
            __props__.__dict__["group"] = group
            __props__.__dict__["hidden"] = hidden
            __props__.__dict__["name"] = name
            __props__.__dict__["org_id"] = org_id
            __props__.__dict__["permissions"] = permissions
            __props__.__dict__["uid"] = uid
            __props__.__dict__["version"] = version
        super(Role, __self__).__init__(
            'grafana:index/role:Role',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auto_increment_version: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            global_: Optional[pulumi.Input[bool]] = None,
            group: Optional[pulumi.Input[str]] = None,
            hidden: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            org_id: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RolePermissionArgs']]]]] = None,
            uid: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'Role':
        """
        Get an existing Role resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_increment_version: Whether the role version should be incremented automatically on updates (and set to 1 on creation). This field or `version` should be set.
        :param pulumi.Input[str] description: Description of the role.
        :param pulumi.Input[str] display_name: Display name of the role. Available with Grafana 8.5+.
        :param pulumi.Input[bool] global_: Boolean to state whether the role is available across all organizations or not. Defaults to `false`.
        :param pulumi.Input[str] group: Group of the role. Available with Grafana 8.5+.
        :param pulumi.Input[bool] hidden: Boolean to state whether the role should be visible in the Grafana UI or not. Available with Grafana 8.5+. Defaults to `false`.
        :param pulumi.Input[str] name: Name of the role
        :param pulumi.Input[str] org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RolePermissionArgs']]]] permissions: Specific set of actions granted by the role.
        :param pulumi.Input[str] uid: Unique identifier of the role. Used for assignments.
        :param pulumi.Input[int] version: Version of the role. A role is updated only on version increase. This field or `auto_increment_version` should be set.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RoleState.__new__(_RoleState)

        __props__.__dict__["auto_increment_version"] = auto_increment_version
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["global_"] = global_
        __props__.__dict__["group"] = group
        __props__.__dict__["hidden"] = hidden
        __props__.__dict__["name"] = name
        __props__.__dict__["org_id"] = org_id
        __props__.__dict__["permissions"] = permissions
        __props__.__dict__["uid"] = uid
        __props__.__dict__["version"] = version
        return Role(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoIncrementVersion")
    def auto_increment_version(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the role version should be incremented automatically on updates (and set to 1 on creation). This field or `version` should be set.
        """
        return pulumi.get(self, "auto_increment_version")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the role.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Display name of the role. Available with Grafana 8.5+.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="global")
    def global_(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean to state whether the role is available across all organizations or not. Defaults to `false`.
        """
        return pulumi.get(self, "global_")

    @property
    @pulumi.getter
    def group(self) -> pulumi.Output[Optional[str]]:
        """
        Group of the role. Available with Grafana 8.5+.
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter
    def hidden(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean to state whether the role should be visible in the Grafana UI or not. Available with Grafana 8.5+. Defaults to `false`.
        """
        return pulumi.get(self, "hidden")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the role
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence['outputs.RolePermission']]]:
        """
        Specific set of actions granted by the role.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter
    def uid(self) -> pulumi.Output[str]:
        """
        Unique identifier of the role. Used for assignments.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[int]]:
        """
        Version of the role. A role is updated only on version increase. This field or `auto_increment_version` should be set.
        """
        return pulumi.get(self, "version")

