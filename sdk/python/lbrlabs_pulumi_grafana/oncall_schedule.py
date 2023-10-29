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

__all__ = ['OncallScheduleArgs', 'OncallSchedule']

@pulumi.input_type
class OncallScheduleArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 enable_web_overrides: Optional[pulumi.Input[bool]] = None,
                 ical_url_overrides: Optional[pulumi.Input[str]] = None,
                 ical_url_primary: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 shifts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 slack: Optional[pulumi.Input['OncallScheduleSlackArgs']] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OncallSchedule resource.
        :param pulumi.Input[str] type: The schedule's type.
        :param pulumi.Input[bool] enable_web_overrides: Enable overrides via web UI (it will ignore ical*url*overrides).
        :param pulumi.Input[str] ical_url_overrides: The URL of external iCal calendar which override primary events.
        :param pulumi.Input[str] ical_url_primary: The URL of the external calendar iCal file.
        :param pulumi.Input[str] name: The schedule's name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] shifts: The list of ID's of on-call shifts.
        :param pulumi.Input['OncallScheduleSlackArgs'] slack: The Slack-specific settings for a schedule.
        :param pulumi.Input[str] team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        :param pulumi.Input[str] time_zone: The schedule's time zone.
        """
        pulumi.set(__self__, "type", type)
        if enable_web_overrides is not None:
            pulumi.set(__self__, "enable_web_overrides", enable_web_overrides)
        if ical_url_overrides is not None:
            pulumi.set(__self__, "ical_url_overrides", ical_url_overrides)
        if ical_url_primary is not None:
            pulumi.set(__self__, "ical_url_primary", ical_url_primary)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if shifts is not None:
            pulumi.set(__self__, "shifts", shifts)
        if slack is not None:
            pulumi.set(__self__, "slack", slack)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The schedule's type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="enableWebOverrides")
    def enable_web_overrides(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable overrides via web UI (it will ignore ical*url*overrides).
        """
        return pulumi.get(self, "enable_web_overrides")

    @enable_web_overrides.setter
    def enable_web_overrides(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_web_overrides", value)

    @property
    @pulumi.getter(name="icalUrlOverrides")
    def ical_url_overrides(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of external iCal calendar which override primary events.
        """
        return pulumi.get(self, "ical_url_overrides")

    @ical_url_overrides.setter
    def ical_url_overrides(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ical_url_overrides", value)

    @property
    @pulumi.getter(name="icalUrlPrimary")
    def ical_url_primary(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the external calendar iCal file.
        """
        return pulumi.get(self, "ical_url_primary")

    @ical_url_primary.setter
    def ical_url_primary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ical_url_primary", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The schedule's name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def shifts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of ID's of on-call shifts.
        """
        return pulumi.get(self, "shifts")

    @shifts.setter
    def shifts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "shifts", value)

    @property
    @pulumi.getter
    def slack(self) -> Optional[pulumi.Input['OncallScheduleSlackArgs']]:
        """
        The Slack-specific settings for a schedule.
        """
        return pulumi.get(self, "slack")

    @slack.setter
    def slack(self, value: Optional[pulumi.Input['OncallScheduleSlackArgs']]):
        pulumi.set(self, "slack", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The schedule's time zone.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)


@pulumi.input_type
class _OncallScheduleState:
    def __init__(__self__, *,
                 enable_web_overrides: Optional[pulumi.Input[bool]] = None,
                 ical_url_overrides: Optional[pulumi.Input[str]] = None,
                 ical_url_primary: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 shifts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 slack: Optional[pulumi.Input['OncallScheduleSlackArgs']] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OncallSchedule resources.
        :param pulumi.Input[bool] enable_web_overrides: Enable overrides via web UI (it will ignore ical*url*overrides).
        :param pulumi.Input[str] ical_url_overrides: The URL of external iCal calendar which override primary events.
        :param pulumi.Input[str] ical_url_primary: The URL of the external calendar iCal file.
        :param pulumi.Input[str] name: The schedule's name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] shifts: The list of ID's of on-call shifts.
        :param pulumi.Input['OncallScheduleSlackArgs'] slack: The Slack-specific settings for a schedule.
        :param pulumi.Input[str] team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        :param pulumi.Input[str] time_zone: The schedule's time zone.
        :param pulumi.Input[str] type: The schedule's type.
        """
        if enable_web_overrides is not None:
            pulumi.set(__self__, "enable_web_overrides", enable_web_overrides)
        if ical_url_overrides is not None:
            pulumi.set(__self__, "ical_url_overrides", ical_url_overrides)
        if ical_url_primary is not None:
            pulumi.set(__self__, "ical_url_primary", ical_url_primary)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if shifts is not None:
            pulumi.set(__self__, "shifts", shifts)
        if slack is not None:
            pulumi.set(__self__, "slack", slack)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="enableWebOverrides")
    def enable_web_overrides(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable overrides via web UI (it will ignore ical*url*overrides).
        """
        return pulumi.get(self, "enable_web_overrides")

    @enable_web_overrides.setter
    def enable_web_overrides(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_web_overrides", value)

    @property
    @pulumi.getter(name="icalUrlOverrides")
    def ical_url_overrides(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of external iCal calendar which override primary events.
        """
        return pulumi.get(self, "ical_url_overrides")

    @ical_url_overrides.setter
    def ical_url_overrides(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ical_url_overrides", value)

    @property
    @pulumi.getter(name="icalUrlPrimary")
    def ical_url_primary(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the external calendar iCal file.
        """
        return pulumi.get(self, "ical_url_primary")

    @ical_url_primary.setter
    def ical_url_primary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ical_url_primary", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The schedule's name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def shifts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of ID's of on-call shifts.
        """
        return pulumi.get(self, "shifts")

    @shifts.setter
    def shifts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "shifts", value)

    @property
    @pulumi.getter
    def slack(self) -> Optional[pulumi.Input['OncallScheduleSlackArgs']]:
        """
        The Slack-specific settings for a schedule.
        """
        return pulumi.get(self, "slack")

    @slack.setter
    def slack(self, value: Optional[pulumi.Input['OncallScheduleSlackArgs']]):
        pulumi.set(self, "slack", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The schedule's time zone.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The schedule's type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class OncallSchedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_web_overrides: Optional[pulumi.Input[bool]] = None,
                 ical_url_overrides: Optional[pulumi.Input[str]] = None,
                 ical_url_primary: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 shifts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 slack: Optional[pulumi.Input[pulumi.InputType['OncallScheduleSlackArgs']]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/schedules/)

        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_grafana as grafana
        import pulumi_grafana as grafana

        example_slack_channel = grafana.get_on_call_slack_channel(name="example_slack_channel")
        example_user_group = grafana.get_oncall_user_group(slack_handle="example_slack_handle")
        # ICal based schedule
        example_schedule_oncall_schedule = grafana.OncallSchedule("exampleScheduleOncallSchedule",
            type="ical",
            ical_url_primary="https://example.com/example_ical.ics",
            ical_url_overrides="https://example.com/example_overrides_ical.ics",
            slack=grafana.OncallScheduleSlackArgs(
                channel_id=example_slack_channel.slack_id,
                user_group_id=example_user_group.slack_id,
            ))
        # Shift based schedule
        example_schedule_index_oncall_schedule_oncall_schedule = grafana.OncallSchedule("exampleScheduleIndex/oncallScheduleOncallSchedule",
            type="calendar",
            time_zone="America/New_York",
            shifts=[],
            ical_url_overrides="https://example.com/example_overrides_ical.ics")
        ```

        ## Import

        ```sh
         $ pulumi import grafana:index/oncallSchedule:OncallSchedule schedule_name {{schedule_id}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_web_overrides: Enable overrides via web UI (it will ignore ical*url*overrides).
        :param pulumi.Input[str] ical_url_overrides: The URL of external iCal calendar which override primary events.
        :param pulumi.Input[str] ical_url_primary: The URL of the external calendar iCal file.
        :param pulumi.Input[str] name: The schedule's name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] shifts: The list of ID's of on-call shifts.
        :param pulumi.Input[pulumi.InputType['OncallScheduleSlackArgs']] slack: The Slack-specific settings for a schedule.
        :param pulumi.Input[str] team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        :param pulumi.Input[str] time_zone: The schedule's time zone.
        :param pulumi.Input[str] type: The schedule's type.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OncallScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/schedules/)

        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_grafana as grafana
        import pulumi_grafana as grafana

        example_slack_channel = grafana.get_on_call_slack_channel(name="example_slack_channel")
        example_user_group = grafana.get_oncall_user_group(slack_handle="example_slack_handle")
        # ICal based schedule
        example_schedule_oncall_schedule = grafana.OncallSchedule("exampleScheduleOncallSchedule",
            type="ical",
            ical_url_primary="https://example.com/example_ical.ics",
            ical_url_overrides="https://example.com/example_overrides_ical.ics",
            slack=grafana.OncallScheduleSlackArgs(
                channel_id=example_slack_channel.slack_id,
                user_group_id=example_user_group.slack_id,
            ))
        # Shift based schedule
        example_schedule_index_oncall_schedule_oncall_schedule = grafana.OncallSchedule("exampleScheduleIndex/oncallScheduleOncallSchedule",
            type="calendar",
            time_zone="America/New_York",
            shifts=[],
            ical_url_overrides="https://example.com/example_overrides_ical.ics")
        ```

        ## Import

        ```sh
         $ pulumi import grafana:index/oncallSchedule:OncallSchedule schedule_name {{schedule_id}}
        ```

        :param str resource_name: The name of the resource.
        :param OncallScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OncallScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_web_overrides: Optional[pulumi.Input[bool]] = None,
                 ical_url_overrides: Optional[pulumi.Input[str]] = None,
                 ical_url_primary: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 shifts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 slack: Optional[pulumi.Input[pulumi.InputType['OncallScheduleSlackArgs']]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OncallScheduleArgs.__new__(OncallScheduleArgs)

            __props__.__dict__["enable_web_overrides"] = enable_web_overrides
            __props__.__dict__["ical_url_overrides"] = ical_url_overrides
            __props__.__dict__["ical_url_primary"] = ical_url_primary
            __props__.__dict__["name"] = name
            __props__.__dict__["shifts"] = shifts
            __props__.__dict__["slack"] = slack
            __props__.__dict__["team_id"] = team_id
            __props__.__dict__["time_zone"] = time_zone
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(OncallSchedule, __self__).__init__(
            'grafana:index/oncallSchedule:OncallSchedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enable_web_overrides: Optional[pulumi.Input[bool]] = None,
            ical_url_overrides: Optional[pulumi.Input[str]] = None,
            ical_url_primary: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            shifts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            slack: Optional[pulumi.Input[pulumi.InputType['OncallScheduleSlackArgs']]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            time_zone: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'OncallSchedule':
        """
        Get an existing OncallSchedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_web_overrides: Enable overrides via web UI (it will ignore ical*url*overrides).
        :param pulumi.Input[str] ical_url_overrides: The URL of external iCal calendar which override primary events.
        :param pulumi.Input[str] ical_url_primary: The URL of the external calendar iCal file.
        :param pulumi.Input[str] name: The schedule's name.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] shifts: The list of ID's of on-call shifts.
        :param pulumi.Input[pulumi.InputType['OncallScheduleSlackArgs']] slack: The Slack-specific settings for a schedule.
        :param pulumi.Input[str] team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        :param pulumi.Input[str] time_zone: The schedule's time zone.
        :param pulumi.Input[str] type: The schedule's type.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OncallScheduleState.__new__(_OncallScheduleState)

        __props__.__dict__["enable_web_overrides"] = enable_web_overrides
        __props__.__dict__["ical_url_overrides"] = ical_url_overrides
        __props__.__dict__["ical_url_primary"] = ical_url_primary
        __props__.__dict__["name"] = name
        __props__.__dict__["shifts"] = shifts
        __props__.__dict__["slack"] = slack
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["time_zone"] = time_zone
        __props__.__dict__["type"] = type
        return OncallSchedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="enableWebOverrides")
    def enable_web_overrides(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable overrides via web UI (it will ignore ical*url*overrides).
        """
        return pulumi.get(self, "enable_web_overrides")

    @property
    @pulumi.getter(name="icalUrlOverrides")
    def ical_url_overrides(self) -> pulumi.Output[Optional[str]]:
        """
        The URL of external iCal calendar which override primary events.
        """
        return pulumi.get(self, "ical_url_overrides")

    @property
    @pulumi.getter(name="icalUrlPrimary")
    def ical_url_primary(self) -> pulumi.Output[Optional[str]]:
        """
        The URL of the external calendar iCal file.
        """
        return pulumi.get(self, "ical_url_primary")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The schedule's name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def shifts(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of ID's of on-call shifts.
        """
        return pulumi.get(self, "shifts")

    @property
    @pulumi.getter
    def slack(self) -> pulumi.Output[Optional['outputs.OncallScheduleSlack']]:
        """
        The Slack-specific settings for a schedule.
        """
        return pulumi.get(self, "slack")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `get_oncall_team` datasource.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[str]]:
        """
        The schedule's time zone.
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The schedule's type.
        """
        return pulumi.get(self, "type")

