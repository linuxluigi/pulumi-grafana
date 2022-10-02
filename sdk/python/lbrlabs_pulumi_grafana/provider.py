# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 auth: Optional[pulumi.Input[str]] = None,
                 ca_cert: Optional[pulumi.Input[str]] = None,
                 cloud_api_key: Optional[pulumi.Input[str]] = None,
                 cloud_api_url: Optional[pulumi.Input[str]] = None,
                 http_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 oncall_access_token: Optional[pulumi.Input[str]] = None,
                 oncall_url: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[int]] = None,
                 retries: Optional[pulumi.Input[int]] = None,
                 sm_access_token: Optional[pulumi.Input[str]] = None,
                 sm_url: Optional[pulumi.Input[str]] = None,
                 store_dashboard_sha256: Optional[pulumi.Input[bool]] = None,
                 tls_cert: Optional[pulumi.Input[str]] = None,
                 tls_key: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] auth: API token or basic auth `username:password`. May alternatively be set via the `GRAFANA_AUTH` environment variable.
        :param pulumi.Input[str] ca_cert: Certificate CA bundle to use to verify the Grafana server's certificate. May alternatively be set via the
               `GRAFANA_CA_CERT` environment variable.
        :param pulumi.Input[str] cloud_api_key: API key for Grafana Cloud. May alternatively be set via the `GRAFANA_CLOUD_API_KEY` environment variable.
        :param pulumi.Input[str] cloud_api_url: Grafana Cloud's API URL. May alternatively be set via the `GRAFANA_CLOUD_API_URL` environment variable.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] http_headers: Optional. HTTP headers mapping keys to values used for accessing the Grafana API. May alternatively be set via the
               `GRAFANA_HTTP_HEADERS` environment variable in JSON format.
        :param pulumi.Input[bool] insecure_skip_verify: Skip TLS certificate verification. May alternatively be set via the `GRAFANA_INSECURE_SKIP_VERIFY` environment variable.
        :param pulumi.Input[str] oncall_access_token: A Grafana OnCall access token. May alternatively be set via the `GRAFANA_ONCALL_ACCESS_TOKEN` environment variable.
        :param pulumi.Input[str] oncall_url: An Grafana OnCall backend address. May alternatively be set via the `GRAFANA_ONCALL_URL` environment variable.
        :param pulumi.Input[int] org_id: The organization id to operate on within grafana. May alternatively be set via the `GRAFANA_ORG_ID` environment
               variable.
        :param pulumi.Input[int] retries: The amount of retries to use for Grafana API calls. May alternatively be set via the `GRAFANA_RETRIES` environment
               variable.
        :param pulumi.Input[str] sm_access_token: A Synthetic Monitoring access token. May alternatively be set via the `GRAFANA_SM_ACCESS_TOKEN` environment variable.
        :param pulumi.Input[str] sm_url: Synthetic monitoring backend address. May alternatively be set via the `GRAFANA_SM_URL` environment variable. The
               correct value for each service region is cited in the [Synthetic Monitoring
               documentation](https://grafana.com/docs/grafana-cloud/synthetic-monitoring/private-probes/#probe-api-server-url). Note
               the `sm_url` value is optional, but it must correspond with the value specified as the `region_slug` in the
               `grafana_cloud_stack` resource. Also note that when a Terraform configuration contains multiple provider instances
               managing SM resources associated with the same Grafana stack, specifying an explicit `sm_url` set to the same value for
               each provider ensures all providers interact with the same SM API.
        :param pulumi.Input[bool] store_dashboard_sha256: Set to true if you want to save only the sha256sum instead of complete dashboard model JSON in the tfstate.
        :param pulumi.Input[str] tls_cert: Client TLS certificate file to use to authenticate to the Grafana server. May alternatively be set via the
               `GRAFANA_TLS_CERT` environment variable.
        :param pulumi.Input[str] tls_key: Client TLS key file to use to authenticate to the Grafana server. May alternatively be set via the `GRAFANA_TLS_KEY`
               environment variable.
        :param pulumi.Input[str] url: The root URL of a Grafana server. May alternatively be set via the `GRAFANA_URL` environment variable.
        """
        if auth is None:
            auth = _utilities.get_env('GRAFANA_AUTH')
        if auth is not None:
            pulumi.set(__self__, "auth", auth)
        if ca_cert is None:
            ca_cert = _utilities.get_env('GRAFANA_CA_CERT')
        if ca_cert is not None:
            pulumi.set(__self__, "ca_cert", ca_cert)
        if cloud_api_key is None:
            cloud_api_key = _utilities.get_env('GRAFANA_CLOUD_API_KEY')
        if cloud_api_key is not None:
            pulumi.set(__self__, "cloud_api_key", cloud_api_key)
        if cloud_api_url is None:
            cloud_api_url = _utilities.get_env('GRAFANA_CLOUD_API_URL')
        if cloud_api_url is not None:
            pulumi.set(__self__, "cloud_api_url", cloud_api_url)
        if http_headers is not None:
            pulumi.set(__self__, "http_headers", http_headers)
        if insecure_skip_verify is None:
            insecure_skip_verify = _utilities.get_env_bool('GRAFANA_INSECURE_SKIP_VERIFY')
        if insecure_skip_verify is not None:
            pulumi.set(__self__, "insecure_skip_verify", insecure_skip_verify)
        if oncall_access_token is None:
            oncall_access_token = _utilities.get_env('GRAFANA_ONCALL_ACCESS_TOKEN')
        if oncall_access_token is not None:
            pulumi.set(__self__, "oncall_access_token", oncall_access_token)
        if oncall_url is None:
            oncall_url = _utilities.get_env('GRAFANA_ONCALL_URL')
        if oncall_url is not None:
            pulumi.set(__self__, "oncall_url", oncall_url)
        if org_id is None:
            org_id = _utilities.get_env_int('GRAFANA_ORG_ID')
        if org_id is not None:
            pulumi.set(__self__, "org_id", org_id)
        if retries is None:
            retries = _utilities.get_env_int('GRAFANA_RETRIES')
        if retries is not None:
            pulumi.set(__self__, "retries", retries)
        if sm_access_token is None:
            sm_access_token = _utilities.get_env('GRAFANA_SM_ACCESS_TOKEN')
        if sm_access_token is not None:
            pulumi.set(__self__, "sm_access_token", sm_access_token)
        if sm_url is None:
            sm_url = _utilities.get_env('GRAFANA_SM_URL')
        if sm_url is not None:
            pulumi.set(__self__, "sm_url", sm_url)
        if store_dashboard_sha256 is None:
            store_dashboard_sha256 = _utilities.get_env_bool('GRAFANA_STORE_DASHBOARD_SHA256')
        if store_dashboard_sha256 is not None:
            pulumi.set(__self__, "store_dashboard_sha256", store_dashboard_sha256)
        if tls_cert is None:
            tls_cert = _utilities.get_env('GRAFANA_TLS_CERT')
        if tls_cert is not None:
            pulumi.set(__self__, "tls_cert", tls_cert)
        if tls_key is None:
            tls_key = _utilities.get_env('GRAFANA_TLS_KEY')
        if tls_key is not None:
            pulumi.set(__self__, "tls_key", tls_key)
        if url is None:
            url = _utilities.get_env('GRAFANA_URL')
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def auth(self) -> Optional[pulumi.Input[str]]:
        """
        API token or basic auth `username:password`. May alternatively be set via the `GRAFANA_AUTH` environment variable.
        """
        return pulumi.get(self, "auth")

    @auth.setter
    def auth(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth", value)

    @property
    @pulumi.getter(name="caCert")
    def ca_cert(self) -> Optional[pulumi.Input[str]]:
        """
        Certificate CA bundle to use to verify the Grafana server's certificate. May alternatively be set via the
        `GRAFANA_CA_CERT` environment variable.
        """
        return pulumi.get(self, "ca_cert")

    @ca_cert.setter
    def ca_cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ca_cert", value)

    @property
    @pulumi.getter(name="cloudApiKey")
    def cloud_api_key(self) -> Optional[pulumi.Input[str]]:
        """
        API key for Grafana Cloud. May alternatively be set via the `GRAFANA_CLOUD_API_KEY` environment variable.
        """
        return pulumi.get(self, "cloud_api_key")

    @cloud_api_key.setter
    def cloud_api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_api_key", value)

    @property
    @pulumi.getter(name="cloudApiUrl")
    def cloud_api_url(self) -> Optional[pulumi.Input[str]]:
        """
        Grafana Cloud's API URL. May alternatively be set via the `GRAFANA_CLOUD_API_URL` environment variable.
        """
        return pulumi.get(self, "cloud_api_url")

    @cloud_api_url.setter
    def cloud_api_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cloud_api_url", value)

    @property
    @pulumi.getter(name="httpHeaders")
    def http_headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. HTTP headers mapping keys to values used for accessing the Grafana API. May alternatively be set via the
        `GRAFANA_HTTP_HEADERS` environment variable in JSON format.
        """
        return pulumi.get(self, "http_headers")

    @http_headers.setter
    def http_headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "http_headers", value)

    @property
    @pulumi.getter(name="insecureSkipVerify")
    def insecure_skip_verify(self) -> Optional[pulumi.Input[bool]]:
        """
        Skip TLS certificate verification. May alternatively be set via the `GRAFANA_INSECURE_SKIP_VERIFY` environment variable.
        """
        return pulumi.get(self, "insecure_skip_verify")

    @insecure_skip_verify.setter
    def insecure_skip_verify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure_skip_verify", value)

    @property
    @pulumi.getter(name="oncallAccessToken")
    def oncall_access_token(self) -> Optional[pulumi.Input[str]]:
        """
        A Grafana OnCall access token. May alternatively be set via the `GRAFANA_ONCALL_ACCESS_TOKEN` environment variable.
        """
        return pulumi.get(self, "oncall_access_token")

    @oncall_access_token.setter
    def oncall_access_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oncall_access_token", value)

    @property
    @pulumi.getter(name="oncallUrl")
    def oncall_url(self) -> Optional[pulumi.Input[str]]:
        """
        An Grafana OnCall backend address. May alternatively be set via the `GRAFANA_ONCALL_URL` environment variable.
        """
        return pulumi.get(self, "oncall_url")

    @oncall_url.setter
    def oncall_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oncall_url", value)

    @property
    @pulumi.getter(name="orgId")
    def org_id(self) -> Optional[pulumi.Input[int]]:
        """
        The organization id to operate on within grafana. May alternatively be set via the `GRAFANA_ORG_ID` environment
        variable.
        """
        return pulumi.get(self, "org_id")

    @org_id.setter
    def org_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "org_id", value)

    @property
    @pulumi.getter
    def retries(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of retries to use for Grafana API calls. May alternatively be set via the `GRAFANA_RETRIES` environment
        variable.
        """
        return pulumi.get(self, "retries")

    @retries.setter
    def retries(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retries", value)

    @property
    @pulumi.getter(name="smAccessToken")
    def sm_access_token(self) -> Optional[pulumi.Input[str]]:
        """
        A Synthetic Monitoring access token. May alternatively be set via the `GRAFANA_SM_ACCESS_TOKEN` environment variable.
        """
        return pulumi.get(self, "sm_access_token")

    @sm_access_token.setter
    def sm_access_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sm_access_token", value)

    @property
    @pulumi.getter(name="smUrl")
    def sm_url(self) -> Optional[pulumi.Input[str]]:
        """
        Synthetic monitoring backend address. May alternatively be set via the `GRAFANA_SM_URL` environment variable. The
        correct value for each service region is cited in the [Synthetic Monitoring
        documentation](https://grafana.com/docs/grafana-cloud/synthetic-monitoring/private-probes/#probe-api-server-url). Note
        the `sm_url` value is optional, but it must correspond with the value specified as the `region_slug` in the
        `grafana_cloud_stack` resource. Also note that when a Terraform configuration contains multiple provider instances
        managing SM resources associated with the same Grafana stack, specifying an explicit `sm_url` set to the same value for
        each provider ensures all providers interact with the same SM API.
        """
        return pulumi.get(self, "sm_url")

    @sm_url.setter
    def sm_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sm_url", value)

    @property
    @pulumi.getter(name="storeDashboardSha256")
    def store_dashboard_sha256(self) -> Optional[pulumi.Input[bool]]:
        """
        Set to true if you want to save only the sha256sum instead of complete dashboard model JSON in the tfstate.
        """
        return pulumi.get(self, "store_dashboard_sha256")

    @store_dashboard_sha256.setter
    def store_dashboard_sha256(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "store_dashboard_sha256", value)

    @property
    @pulumi.getter(name="tlsCert")
    def tls_cert(self) -> Optional[pulumi.Input[str]]:
        """
        Client TLS certificate file to use to authenticate to the Grafana server. May alternatively be set via the
        `GRAFANA_TLS_CERT` environment variable.
        """
        return pulumi.get(self, "tls_cert")

    @tls_cert.setter
    def tls_cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_cert", value)

    @property
    @pulumi.getter(name="tlsKey")
    def tls_key(self) -> Optional[pulumi.Input[str]]:
        """
        Client TLS key file to use to authenticate to the Grafana server. May alternatively be set via the `GRAFANA_TLS_KEY`
        environment variable.
        """
        return pulumi.get(self, "tls_key")

    @tls_key.setter
    def tls_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tls_key", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The root URL of a Grafana server. May alternatively be set via the `GRAFANA_URL` environment variable.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth: Optional[pulumi.Input[str]] = None,
                 ca_cert: Optional[pulumi.Input[str]] = None,
                 cloud_api_key: Optional[pulumi.Input[str]] = None,
                 cloud_api_url: Optional[pulumi.Input[str]] = None,
                 http_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 oncall_access_token: Optional[pulumi.Input[str]] = None,
                 oncall_url: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[int]] = None,
                 retries: Optional[pulumi.Input[int]] = None,
                 sm_access_token: Optional[pulumi.Input[str]] = None,
                 sm_url: Optional[pulumi.Input[str]] = None,
                 store_dashboard_sha256: Optional[pulumi.Input[bool]] = None,
                 tls_cert: Optional[pulumi.Input[str]] = None,
                 tls_key: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the grafana package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth: API token or basic auth `username:password`. May alternatively be set via the `GRAFANA_AUTH` environment variable.
        :param pulumi.Input[str] ca_cert: Certificate CA bundle to use to verify the Grafana server's certificate. May alternatively be set via the
               `GRAFANA_CA_CERT` environment variable.
        :param pulumi.Input[str] cloud_api_key: API key for Grafana Cloud. May alternatively be set via the `GRAFANA_CLOUD_API_KEY` environment variable.
        :param pulumi.Input[str] cloud_api_url: Grafana Cloud's API URL. May alternatively be set via the `GRAFANA_CLOUD_API_URL` environment variable.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] http_headers: Optional. HTTP headers mapping keys to values used for accessing the Grafana API. May alternatively be set via the
               `GRAFANA_HTTP_HEADERS` environment variable in JSON format.
        :param pulumi.Input[bool] insecure_skip_verify: Skip TLS certificate verification. May alternatively be set via the `GRAFANA_INSECURE_SKIP_VERIFY` environment variable.
        :param pulumi.Input[str] oncall_access_token: A Grafana OnCall access token. May alternatively be set via the `GRAFANA_ONCALL_ACCESS_TOKEN` environment variable.
        :param pulumi.Input[str] oncall_url: An Grafana OnCall backend address. May alternatively be set via the `GRAFANA_ONCALL_URL` environment variable.
        :param pulumi.Input[int] org_id: The organization id to operate on within grafana. May alternatively be set via the `GRAFANA_ORG_ID` environment
               variable.
        :param pulumi.Input[int] retries: The amount of retries to use for Grafana API calls. May alternatively be set via the `GRAFANA_RETRIES` environment
               variable.
        :param pulumi.Input[str] sm_access_token: A Synthetic Monitoring access token. May alternatively be set via the `GRAFANA_SM_ACCESS_TOKEN` environment variable.
        :param pulumi.Input[str] sm_url: Synthetic monitoring backend address. May alternatively be set via the `GRAFANA_SM_URL` environment variable. The
               correct value for each service region is cited in the [Synthetic Monitoring
               documentation](https://grafana.com/docs/grafana-cloud/synthetic-monitoring/private-probes/#probe-api-server-url). Note
               the `sm_url` value is optional, but it must correspond with the value specified as the `region_slug` in the
               `grafana_cloud_stack` resource. Also note that when a Terraform configuration contains multiple provider instances
               managing SM resources associated with the same Grafana stack, specifying an explicit `sm_url` set to the same value for
               each provider ensures all providers interact with the same SM API.
        :param pulumi.Input[bool] store_dashboard_sha256: Set to true if you want to save only the sha256sum instead of complete dashboard model JSON in the tfstate.
        :param pulumi.Input[str] tls_cert: Client TLS certificate file to use to authenticate to the Grafana server. May alternatively be set via the
               `GRAFANA_TLS_CERT` environment variable.
        :param pulumi.Input[str] tls_key: Client TLS key file to use to authenticate to the Grafana server. May alternatively be set via the `GRAFANA_TLS_KEY`
               environment variable.
        :param pulumi.Input[str] url: The root URL of a Grafana server. May alternatively be set via the `GRAFANA_URL` environment variable.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the grafana package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth: Optional[pulumi.Input[str]] = None,
                 ca_cert: Optional[pulumi.Input[str]] = None,
                 cloud_api_key: Optional[pulumi.Input[str]] = None,
                 cloud_api_url: Optional[pulumi.Input[str]] = None,
                 http_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 oncall_access_token: Optional[pulumi.Input[str]] = None,
                 oncall_url: Optional[pulumi.Input[str]] = None,
                 org_id: Optional[pulumi.Input[int]] = None,
                 retries: Optional[pulumi.Input[int]] = None,
                 sm_access_token: Optional[pulumi.Input[str]] = None,
                 sm_url: Optional[pulumi.Input[str]] = None,
                 store_dashboard_sha256: Optional[pulumi.Input[bool]] = None,
                 tls_cert: Optional[pulumi.Input[str]] = None,
                 tls_key: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            if auth is None:
                auth = _utilities.get_env('GRAFANA_AUTH')
            __props__.__dict__["auth"] = None if auth is None else pulumi.Output.secret(auth)
            if ca_cert is None:
                ca_cert = _utilities.get_env('GRAFANA_CA_CERT')
            __props__.__dict__["ca_cert"] = ca_cert
            if cloud_api_key is None:
                cloud_api_key = _utilities.get_env('GRAFANA_CLOUD_API_KEY')
            __props__.__dict__["cloud_api_key"] = None if cloud_api_key is None else pulumi.Output.secret(cloud_api_key)
            if cloud_api_url is None:
                cloud_api_url = _utilities.get_env('GRAFANA_CLOUD_API_URL')
            __props__.__dict__["cloud_api_url"] = cloud_api_url
            __props__.__dict__["http_headers"] = None if pulumi.Output.from_input(http_headers).apply(pulumi.runtime.to_json) if http_headers is not None else None is None else pulumi.Output.secret(pulumi.Output.from_input(http_headers).apply(pulumi.runtime.to_json) if http_headers is not None else None)
            if insecure_skip_verify is None:
                insecure_skip_verify = _utilities.get_env_bool('GRAFANA_INSECURE_SKIP_VERIFY')
            __props__.__dict__["insecure_skip_verify"] = pulumi.Output.from_input(insecure_skip_verify).apply(pulumi.runtime.to_json) if insecure_skip_verify is not None else None
            if oncall_access_token is None:
                oncall_access_token = _utilities.get_env('GRAFANA_ONCALL_ACCESS_TOKEN')
            __props__.__dict__["oncall_access_token"] = None if oncall_access_token is None else pulumi.Output.secret(oncall_access_token)
            if oncall_url is None:
                oncall_url = _utilities.get_env('GRAFANA_ONCALL_URL')
            __props__.__dict__["oncall_url"] = oncall_url
            if org_id is None:
                org_id = _utilities.get_env_int('GRAFANA_ORG_ID')
            __props__.__dict__["org_id"] = pulumi.Output.from_input(org_id).apply(pulumi.runtime.to_json) if org_id is not None else None
            if retries is None:
                retries = _utilities.get_env_int('GRAFANA_RETRIES')
            __props__.__dict__["retries"] = pulumi.Output.from_input(retries).apply(pulumi.runtime.to_json) if retries is not None else None
            if sm_access_token is None:
                sm_access_token = _utilities.get_env('GRAFANA_SM_ACCESS_TOKEN')
            __props__.__dict__["sm_access_token"] = None if sm_access_token is None else pulumi.Output.secret(sm_access_token)
            if sm_url is None:
                sm_url = _utilities.get_env('GRAFANA_SM_URL')
            __props__.__dict__["sm_url"] = sm_url
            if store_dashboard_sha256 is None:
                store_dashboard_sha256 = _utilities.get_env_bool('GRAFANA_STORE_DASHBOARD_SHA256')
            __props__.__dict__["store_dashboard_sha256"] = pulumi.Output.from_input(store_dashboard_sha256).apply(pulumi.runtime.to_json) if store_dashboard_sha256 is not None else None
            if tls_cert is None:
                tls_cert = _utilities.get_env('GRAFANA_TLS_CERT')
            __props__.__dict__["tls_cert"] = tls_cert
            if tls_key is None:
                tls_key = _utilities.get_env('GRAFANA_TLS_KEY')
            __props__.__dict__["tls_key"] = tls_key
            if url is None:
                url = _utilities.get_env('GRAFANA_URL')
            __props__.__dict__["url"] = url
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["auth", "cloudApiKey", "oncallAccessToken", "smAccessToken"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'grafana',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter
    def auth(self) -> pulumi.Output[Optional[str]]:
        """
        API token or basic auth `username:password`. May alternatively be set via the `GRAFANA_AUTH` environment variable.
        """
        return pulumi.get(self, "auth")

    @property
    @pulumi.getter(name="caCert")
    def ca_cert(self) -> pulumi.Output[Optional[str]]:
        """
        Certificate CA bundle to use to verify the Grafana server's certificate. May alternatively be set via the
        `GRAFANA_CA_CERT` environment variable.
        """
        return pulumi.get(self, "ca_cert")

    @property
    @pulumi.getter(name="cloudApiKey")
    def cloud_api_key(self) -> pulumi.Output[Optional[str]]:
        """
        API key for Grafana Cloud. May alternatively be set via the `GRAFANA_CLOUD_API_KEY` environment variable.
        """
        return pulumi.get(self, "cloud_api_key")

    @property
    @pulumi.getter(name="cloudApiUrl")
    def cloud_api_url(self) -> pulumi.Output[Optional[str]]:
        """
        Grafana Cloud's API URL. May alternatively be set via the `GRAFANA_CLOUD_API_URL` environment variable.
        """
        return pulumi.get(self, "cloud_api_url")

    @property
    @pulumi.getter(name="oncallAccessToken")
    def oncall_access_token(self) -> pulumi.Output[Optional[str]]:
        """
        A Grafana OnCall access token. May alternatively be set via the `GRAFANA_ONCALL_ACCESS_TOKEN` environment variable.
        """
        return pulumi.get(self, "oncall_access_token")

    @property
    @pulumi.getter(name="oncallUrl")
    def oncall_url(self) -> pulumi.Output[Optional[str]]:
        """
        An Grafana OnCall backend address. May alternatively be set via the `GRAFANA_ONCALL_URL` environment variable.
        """
        return pulumi.get(self, "oncall_url")

    @property
    @pulumi.getter(name="smAccessToken")
    def sm_access_token(self) -> pulumi.Output[Optional[str]]:
        """
        A Synthetic Monitoring access token. May alternatively be set via the `GRAFANA_SM_ACCESS_TOKEN` environment variable.
        """
        return pulumi.get(self, "sm_access_token")

    @property
    @pulumi.getter(name="smUrl")
    def sm_url(self) -> pulumi.Output[Optional[str]]:
        """
        Synthetic monitoring backend address. May alternatively be set via the `GRAFANA_SM_URL` environment variable. The
        correct value for each service region is cited in the [Synthetic Monitoring
        documentation](https://grafana.com/docs/grafana-cloud/synthetic-monitoring/private-probes/#probe-api-server-url). Note
        the `sm_url` value is optional, but it must correspond with the value specified as the `region_slug` in the
        `grafana_cloud_stack` resource. Also note that when a Terraform configuration contains multiple provider instances
        managing SM resources associated with the same Grafana stack, specifying an explicit `sm_url` set to the same value for
        each provider ensures all providers interact with the same SM API.
        """
        return pulumi.get(self, "sm_url")

    @property
    @pulumi.getter(name="tlsCert")
    def tls_cert(self) -> pulumi.Output[Optional[str]]:
        """
        Client TLS certificate file to use to authenticate to the Grafana server. May alternatively be set via the
        `GRAFANA_TLS_CERT` environment variable.
        """
        return pulumi.get(self, "tls_cert")

    @property
    @pulumi.getter(name="tlsKey")
    def tls_key(self) -> pulumi.Output[Optional[str]]:
        """
        Client TLS key file to use to authenticate to the Grafana server. May alternatively be set via the `GRAFANA_TLS_KEY`
        environment variable.
        """
        return pulumi.get(self, "tls_key")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[str]]:
        """
        The root URL of a Grafana server. May alternatively be set via the `GRAFANA_URL` environment variable.
        """
        return pulumi.get(self, "url")

