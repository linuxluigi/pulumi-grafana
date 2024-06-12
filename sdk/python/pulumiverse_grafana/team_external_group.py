# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TeamExternalGroupArgs', 'TeamExternalGroup']

@pulumi.input_type
class TeamExternalGroupArgs:
    def __init__(__self__, *,
                 groups: pulumi.Input[Sequence[pulumi.Input[str]]],
                 team_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a TeamExternalGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] groups: The team external groups list
        :param pulumi.Input[str] team_id: The Team ID
        """
        pulumi.set(__self__, "groups", groups)
        pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter
    def groups(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The team external groups list
        """
        return pulumi.get(self, "groups")

    @groups.setter
    def groups(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "groups", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Input[str]:
        """
        The Team ID
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "team_id", value)


@pulumi.input_type
class _TeamExternalGroupState:
    def __init__(__self__, *,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TeamExternalGroup resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] groups: The team external groups list
        :param pulumi.Input[str] team_id: The Team ID
        """
        if groups is not None:
            pulumi.set(__self__, "groups", groups)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter
    def groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The team external groups list
        """
        return pulumi.get(self, "groups")

    @groups.setter
    def groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "groups", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Team ID
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)


class TeamExternalGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Equivalent to the the `team_sync` attribute of the `Team` resource. Use one or the other to configure a team's external groups syncing config.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumiverse_grafana as grafana

        my_team = grafana.Team("myTeam")
        test_team_group = grafana.TeamExternalGroup("test-team-group",
            team_id=my_team.id,
            groups=[
                "test-group-1",
                "test-group-2",
            ])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import grafana:index/teamExternalGroup:TeamExternalGroup name "{{ teamID }}"
        ```

        ```sh
        $ pulumi import grafana:index/teamExternalGroup:TeamExternalGroup name "{{ orgID }}:{{ teamID }}"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] groups: The team external groups list
        :param pulumi.Input[str] team_id: The Team ID
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TeamExternalGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Equivalent to the the `team_sync` attribute of the `Team` resource. Use one or the other to configure a team's external groups syncing config.

        ## Example Usage

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import pulumiverse_grafana as grafana

        my_team = grafana.Team("myTeam")
        test_team_group = grafana.TeamExternalGroup("test-team-group",
            team_id=my_team.id,
            groups=[
                "test-group-1",
                "test-group-2",
            ])
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        ```sh
        $ pulumi import grafana:index/teamExternalGroup:TeamExternalGroup name "{{ teamID }}"
        ```

        ```sh
        $ pulumi import grafana:index/teamExternalGroup:TeamExternalGroup name "{{ orgID }}:{{ teamID }}"
        ```

        :param str resource_name: The name of the resource.
        :param TeamExternalGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TeamExternalGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TeamExternalGroupArgs.__new__(TeamExternalGroupArgs)

            if groups is None and not opts.urn:
                raise TypeError("Missing required property 'groups'")
            __props__.__dict__["groups"] = groups
            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__.__dict__["team_id"] = team_id
        super(TeamExternalGroup, __self__).__init__(
            'grafana:index/teamExternalGroup:TeamExternalGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            team_id: Optional[pulumi.Input[str]] = None) -> 'TeamExternalGroup':
        """
        Get an existing TeamExternalGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] groups: The team external groups list
        :param pulumi.Input[str] team_id: The Team ID
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TeamExternalGroupState.__new__(_TeamExternalGroupState)

        __props__.__dict__["groups"] = groups
        __props__.__dict__["team_id"] = team_id
        return TeamExternalGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def groups(self) -> pulumi.Output[Sequence[str]]:
        """
        The team external groups list
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        The Team ID
        """
        return pulumi.get(self, "team_id")

