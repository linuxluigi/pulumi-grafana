// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.TypeShape;
import com.pulumi.core.internal.Codegen;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Optional;

public final class Config {

    private static final com.pulumi.Config config = com.pulumi.Config.of("grafana");
/**
 * API token, basic auth in the `username:password` format or `anonymous` (string literal). May alternatively be set via
 * the `GRAFANA_AUTH` environment variable.
 * 
 */
    public Optional<String> auth() {
        return Codegen.stringProp("auth").config(config).env("GRAFANA_AUTH").get();
    }
/**
 * Certificate CA bundle (file path or literal value) to use to verify the Grafana server&#39;s certificate. May alternatively
 * be set via the `GRAFANA_CA_CERT` environment variable.
 * 
 */
    public Optional<String> caCert() {
        return Codegen.stringProp("caCert").config(config).env("GRAFANA_CA_CERT").get();
    }
/**
 * Access Policy Token (or API key) for Grafana Cloud. May alternatively be set via the `GRAFANA_CLOUD_API_KEY` environment
 * variable.
 * 
 */
    public Optional<String> cloudApiKey() {
        return Codegen.stringProp("cloudApiKey").config(config).env("GRAFANA_CLOUD_API_KEY").get();
    }
/**
 * Grafana Cloud&#39;s API URL. May alternatively be set via the `GRAFANA_CLOUD_API_URL` environment variable.
 * 
 */
    public Optional<String> cloudApiUrl() {
        return Codegen.stringProp("cloudApiUrl").config(config).env("GRAFANA_CLOUD_API_URL").get();
    }
/**
 * Optional. HTTP headers mapping keys to values used for accessing the Grafana and Grafana Cloud APIs. May alternatively
 * be set via the `GRAFANA_HTTP_HEADERS` environment variable in JSON format.
 * 
 */
    public Optional<Map<String,String>> httpHeaders() {
        return Codegen.objectProp("httpHeaders", TypeShape.<Map<String,String>>builder(Map.class).addParameter(String.class).addParameter(String.class).build()).config(config).get();
    }
/**
 * Skip TLS certificate verification. May alternatively be set via the `GRAFANA_INSECURE_SKIP_VERIFY` environment variable.
 * 
 */
    public Optional<Boolean> insecureSkipVerify() {
        return Codegen.booleanProp("insecureSkipVerify").config(config).env("GRAFANA_INSECURE_SKIP_VERIFY").get();
    }
/**
 * A Grafana OnCall access token. May alternatively be set via the `GRAFANA_ONCALL_ACCESS_TOKEN` environment variable.
 * 
 */
    public Optional<String> oncallAccessToken() {
        return Codegen.stringProp("oncallAccessToken").config(config).env("GRAFANA_ONCALL_ACCESS_TOKEN").get();
    }
/**
 * An Grafana OnCall backend address. May alternatively be set via the `GRAFANA_ONCALL_URL` environment variable.
 * 
 */
    public Optional<String> oncallUrl() {
        return Codegen.stringProp("oncallUrl").config(config).env("GRAFANA_ONCALL_URL").get();
    }
/**
 * Deprecated: Use the `org_id` attributes on resources instead.
 * 
 */
    public Optional<Integer> orgId() {
        return Codegen.integerProp("orgId").config(config).env("GRAFANA_ORG_ID").get();
    }
/**
 * The amount of retries to use for Grafana API and Grafana Cloud API calls. May alternatively be set via the
 * `GRAFANA_RETRIES` environment variable.
 * 
 */
    public Optional<Integer> retries() {
        return Codegen.integerProp("retries").config(config).env("GRAFANA_RETRIES").get();
    }
/**
 * The status codes to retry on for Grafana API and Grafana Cloud API calls. Use `x` as a digit wildcard. Defaults to 429
 * and 5xx. May alternatively be set via the `GRAFANA_RETRY_STATUS_CODES` environment variable.
 * 
 */
    public Optional<List<String>> retryStatusCodes() {
        return Codegen.objectProp("retryStatusCodes", TypeShape.<List<String>>builder(List.class).addParameter(String.class).build()).config(config).get();
    }
/**
 * A Synthetic Monitoring access token. May alternatively be set via the `GRAFANA_SM_ACCESS_TOKEN` environment variable.
 * 
 */
    public Optional<String> smAccessToken() {
        return Codegen.stringProp("smAccessToken").config(config).env("GRAFANA_SM_ACCESS_TOKEN").get();
    }
/**
 * Synthetic monitoring backend address. May alternatively be set via the `GRAFANA_SM_URL` environment variable. The
 * correct value for each service region is cited in the [Synthetic Monitoring
 * documentation](https://grafana.com/docs/grafana-cloud/synthetic-monitoring/private-probes/#probe-api-server-url). Note
 * the `sm_url` value is optional, but it must correspond with the value specified as the `region_slug` in the
 * `grafana_cloud_stack` resource. Also note that when a Terraform configuration contains multiple provider instances
 * managing SM resources associated with the same Grafana stack, specifying an explicit `sm_url` set to the same value for
 * each provider ensures all providers interact with the same SM API.
 * 
 */
    public Optional<String> smUrl() {
        return Codegen.stringProp("smUrl").config(config).env("GRAFANA_SM_URL").get();
    }
/**
 * Set to true if you want to save only the sha256sum instead of complete dashboard model JSON in the tfstate.
 * 
 */
    public Optional<Boolean> storeDashboardSha256() {
        return Codegen.booleanProp("storeDashboardSha256").config(config).env("GRAFANA_STORE_DASHBOARD_SHA256").get();
    }
/**
 * Client TLS certificate (file path or literal value) to use to authenticate to the Grafana server. May alternatively be
 * set via the `GRAFANA_TLS_CERT` environment variable.
 * 
 */
    public Optional<String> tlsCert() {
        return Codegen.stringProp("tlsCert").config(config).env("GRAFANA_TLS_CERT").get();
    }
/**
 * Client TLS key (file path or literal value) to use to authenticate to the Grafana server. May alternatively be set via
 * the `GRAFANA_TLS_KEY` environment variable.
 * 
 */
    public Optional<String> tlsKey() {
        return Codegen.stringProp("tlsKey").config(config).env("GRAFANA_TLS_KEY").get();
    }
/**
 * The root URL of a Grafana server. May alternatively be set via the `GRAFANA_URL` environment variable.
 * 
 */
    public Optional<String> url() {
        return Codegen.stringProp("url").config(config).env("GRAFANA_URL").get();
    }
}
