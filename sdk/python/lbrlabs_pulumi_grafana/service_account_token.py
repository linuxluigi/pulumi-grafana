# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ServiceAccountTokenArgs', 'ServiceAccountToken']

@pulumi.input_type
class ServiceAccountTokenArgs:
    def __init__(__self__, *,
                 service_account_id: pulumi.Input[int],
                 name: Optional[pulumi.Input[str]] = None,
                 seconds_to_live: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ServiceAccountToken resource.
        """
        pulumi.set(__self__, "service_account_id", service_account_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if seconds_to_live is not None:
            pulumi.set(__self__, "seconds_to_live", seconds_to_live)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Input[int]:
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "service_account_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="secondsToLive")
    def seconds_to_live(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "seconds_to_live")

    @seconds_to_live.setter
    def seconds_to_live(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "seconds_to_live", value)


@pulumi.input_type
class _ServiceAccountTokenState:
    def __init__(__self__, *,
                 expiration: Optional[pulumi.Input[str]] = None,
                 has_expired: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 seconds_to_live: Optional[pulumi.Input[int]] = None,
                 service_account_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering ServiceAccountToken resources.
        """
        if expiration is not None:
            pulumi.set(__self__, "expiration", expiration)
        if has_expired is not None:
            pulumi.set(__self__, "has_expired", has_expired)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if seconds_to_live is not None:
            pulumi.set(__self__, "seconds_to_live", seconds_to_live)
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)

    @property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expiration")

    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration", value)

    @property
    @pulumi.getter(name="hasExpired")
    def has_expired(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "has_expired")

    @has_expired.setter
    def has_expired(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "has_expired", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="secondsToLive")
    def seconds_to_live(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "seconds_to_live")

    @seconds_to_live.setter
    def seconds_to_live(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "seconds_to_live", value)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "service_account_id", value)


class ServiceAccountToken(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 seconds_to_live: Optional[pulumi.Input[int]] = None,
                 service_account_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        **Note:** This resource is available only with Grafana 9.1+.

        * [Official documentation](https://grafana.com/docs/grafana/latest/administration/service-accounts/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api)

        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_grafana as grafana

        foo = grafana.ServiceAccountToken("foo", service_account_id=1)
        bar = grafana.ServiceAccountToken("bar",
            service_account_id=1,
            seconds_to_live=30)
        pulumi.export("serviceAccountTokenFooKeyOnly", foo.key)
        pulumi.export("serviceAccountTokenBar", bar)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceAccountTokenArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        **Note:** This resource is available only with Grafana 9.1+.

        * [Official documentation](https://grafana.com/docs/grafana/latest/administration/service-accounts/)
        * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api)

        ## Example Usage

        ```python
        import pulumi
        import lbrlabs_pulumi_grafana as grafana

        foo = grafana.ServiceAccountToken("foo", service_account_id=1)
        bar = grafana.ServiceAccountToken("bar",
            service_account_id=1,
            seconds_to_live=30)
        pulumi.export("serviceAccountTokenFooKeyOnly", foo.key)
        pulumi.export("serviceAccountTokenBar", bar)
        ```

        :param str resource_name: The name of the resource.
        :param ServiceAccountTokenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceAccountTokenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 seconds_to_live: Optional[pulumi.Input[int]] = None,
                 service_account_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceAccountTokenArgs.__new__(ServiceAccountTokenArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["seconds_to_live"] = seconds_to_live
            if service_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_account_id'")
            __props__.__dict__["service_account_id"] = service_account_id
            __props__.__dict__["expiration"] = None
            __props__.__dict__["has_expired"] = None
            __props__.__dict__["key"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["key"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ServiceAccountToken, __self__).__init__(
            'grafana:index/serviceAccountToken:ServiceAccountToken',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            expiration: Optional[pulumi.Input[str]] = None,
            has_expired: Optional[pulumi.Input[bool]] = None,
            key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            seconds_to_live: Optional[pulumi.Input[int]] = None,
            service_account_id: Optional[pulumi.Input[int]] = None) -> 'ServiceAccountToken':
        """
        Get an existing ServiceAccountToken resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServiceAccountTokenState.__new__(_ServiceAccountTokenState)

        __props__.__dict__["expiration"] = expiration
        __props__.__dict__["has_expired"] = has_expired
        __props__.__dict__["key"] = key
        __props__.__dict__["name"] = name
        __props__.__dict__["seconds_to_live"] = seconds_to_live
        __props__.__dict__["service_account_id"] = service_account_id
        return ServiceAccountToken(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def expiration(self) -> pulumi.Output[str]:
        return pulumi.get(self, "expiration")

    @property
    @pulumi.getter(name="hasExpired")
    def has_expired(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "has_expired")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="secondsToLive")
    def seconds_to_live(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "seconds_to_live")

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "service_account_id")

