# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetOrganizationPreferencesResult',
    'AwaitableGetOrganizationPreferencesResult',
    'get_organization_preferences',
    'get_organization_preferences_output',
]

@pulumi.output_type
class GetOrganizationPreferencesResult:
    """
    A collection of values returned by getOrganizationPreferences.
    """
    def __init__(__self__, home_dashboard_id=None, home_dashboard_uid=None, id=None, org_id=None, theme=None, timezone=None, week_start=None):
        if home_dashboard_id and not isinstance(home_dashboard_id, int):
            raise TypeError("Expected argument 'home_dashboard_id' to be a int")
        pulumi.set(__self__, "home_dashboard_id", home_dashboard_id)
        if home_dashboard_uid and not isinstance(home_dashboard_uid, str):
            raise TypeError("Expected argument 'home_dashboard_uid' to be a str")
        pulumi.set(__self__, "home_dashboard_uid", home_dashboard_uid)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if org_id and not isinstance(org_id, str):
            raise TypeError("Expected argument 'org_id' to be a str")
        pulumi.set(__self__, "org_id", org_id)
        if theme and not isinstance(theme, str):
            raise TypeError("Expected argument 'theme' to be a str")
        pulumi.set(__self__, "theme", theme)
        if timezone and not isinstance(timezone, str):
            raise TypeError("Expected argument 'timezone' to be a str")
        pulumi.set(__self__, "timezone", timezone)
        if week_start and not isinstance(week_start, str):
            raise TypeError("Expected argument 'week_start' to be a str")
        pulumi.set(__self__, "week_start", week_start)

    @property
    @pulumi.getter(name="homeDashboardId")
    def home_dashboard_id(self) -> int:
        """
        The Organization home dashboard ID. Deprecated: Use `home_dashboard_uid` instead.
        """
        warnings.warn("""Use `home_dashboard_uid` instead.""", DeprecationWarning)
        pulumi.log.warn("""home_dashboard_id is deprecated: Use `home_dashboard_uid` instead.""")

        return pulumi.get(self, "home_dashboard_id")

    @property
    @pulumi.getter(name="homeDashboardUid")
    def home_dashboard_uid(self) -> str:
        """
        The Organization home dashboard UID. This is only available in Grafana 9.0+.
        """
        return pulumi.get(self, "home_dashboard_uid")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[str]:
        """
        The Organization ID. If not set, the Org ID defined in the provider block will be used.
        """
        return pulumi.get(self, "org_id")

    @property
    @pulumi.getter
    def theme(self) -> str:
        """
        The Organization theme. Available values are `light`, `dark`, `system`, or an empty string for the default.
        """
        return pulumi.get(self, "theme")

    @property
    @pulumi.getter
    def timezone(self) -> str:
        """
        The Organization timezone. Available values are `utc`, `browser`, or an empty string for the default.
        """
        return pulumi.get(self, "timezone")

    @property
    @pulumi.getter(name="weekStart")
    def week_start(self) -> str:
        """
        The Organization week start day. Available values are `sunday`, `monday`, `saturday`, or an empty string for the default.
        """
        return pulumi.get(self, "week_start")


class AwaitableGetOrganizationPreferencesResult(GetOrganizationPreferencesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationPreferencesResult(
            home_dashboard_id=self.home_dashboard_id,
            home_dashboard_uid=self.home_dashboard_uid,
            id=self.id,
            org_id=self.org_id,
            theme=self.theme,
            timezone=self.timezone,
            week_start=self.week_start)


def get_organization_preferences(org_id: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationPreferencesResult:
    """
    * [Official documentation](https://grafana.com/docs/grafana/latest/administration/organization-management/)
    * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/preferences/#get-current-org-prefs)

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_grafana as grafana

    test = grafana.get_organization_preferences()
    ```
    <!--End PulumiCodeChooser -->


    :param str org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
    """
    __args__ = dict()
    __args__['orgId'] = org_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('grafana:index/getOrganizationPreferences:getOrganizationPreferences', __args__, opts=opts, typ=GetOrganizationPreferencesResult).value

    return AwaitableGetOrganizationPreferencesResult(
        home_dashboard_id=pulumi.get(__ret__, 'home_dashboard_id'),
        home_dashboard_uid=pulumi.get(__ret__, 'home_dashboard_uid'),
        id=pulumi.get(__ret__, 'id'),
        org_id=pulumi.get(__ret__, 'org_id'),
        theme=pulumi.get(__ret__, 'theme'),
        timezone=pulumi.get(__ret__, 'timezone'),
        week_start=pulumi.get(__ret__, 'week_start'))


@_utilities.lift_output_func(get_organization_preferences)
def get_organization_preferences_output(org_id: Optional[pulumi.Input[Optional[str]]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrganizationPreferencesResult]:
    """
    * [Official documentation](https://grafana.com/docs/grafana/latest/administration/organization-management/)
    * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/preferences/#get-current-org-prefs)

    ## Example Usage

    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_grafana as grafana

    test = grafana.get_organization_preferences()
    ```
    <!--End PulumiCodeChooser -->


    :param str org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used.
    """
    ...
