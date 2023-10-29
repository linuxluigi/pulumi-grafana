// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.grafana.inputs.SyntheticMonitoringCheckSettingsHttpBasicAuthArgs;
import com.pulumi.grafana.inputs.SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpArgs;
import com.pulumi.grafana.inputs.SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpArgs;
import com.pulumi.grafana.inputs.SyntheticMonitoringCheckSettingsHttpTlsConfigArgs;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class SyntheticMonitoringCheckSettingsHttpArgs extends com.pulumi.resources.ResourceArgs {

    public static final SyntheticMonitoringCheckSettingsHttpArgs Empty = new SyntheticMonitoringCheckSettingsHttpArgs();

    /**
     * Basic auth settings.
     * 
     */
    @Import(name="basicAuth")
    private @Nullable Output<SyntheticMonitoringCheckSettingsHttpBasicAuthArgs> basicAuth;

    /**
     * @return Basic auth settings.
     * 
     */
    public Optional<Output<SyntheticMonitoringCheckSettingsHttpBasicAuthArgs>> basicAuth() {
        return Optional.ofNullable(this.basicAuth);
    }

    /**
     * Token for use with bearer authorization header.
     * 
     */
    @Import(name="bearerToken")
    private @Nullable Output<String> bearerToken;

    /**
     * @return Token for use with bearer authorization header.
     * 
     */
    public Optional<Output<String>> bearerToken() {
        return Optional.ofNullable(this.bearerToken);
    }

    /**
     * The body of the HTTP request used in probe.
     * 
     */
    @Import(name="body")
    private @Nullable Output<String> body;

    /**
     * @return The body of the HTTP request used in probe.
     * 
     */
    public Optional<Output<String>> body() {
        return Optional.ofNullable(this.body);
    }

    /**
     * The name of the query parameter used to prevent the server from using a cached response. Each probe will assign a random value to this parameter each time a request is made.
     * 
     */
    @Import(name="cacheBustingQueryParamName")
    private @Nullable Output<String> cacheBustingQueryParamName;

    /**
     * @return The name of the query parameter used to prevent the server from using a cached response. Each probe will assign a random value to this parameter each time a request is made.
     * 
     */
    public Optional<Output<String>> cacheBustingQueryParamName() {
        return Optional.ofNullable(this.cacheBustingQueryParamName);
    }

    /**
     * List of regexes. If any match the response body, the check will fail.
     * 
     */
    @Import(name="failIfBodyMatchesRegexps")
    private @Nullable Output<List<String>> failIfBodyMatchesRegexps;

    /**
     * @return List of regexes. If any match the response body, the check will fail.
     * 
     */
    public Optional<Output<List<String>>> failIfBodyMatchesRegexps() {
        return Optional.ofNullable(this.failIfBodyMatchesRegexps);
    }

    /**
     * List of regexes. If any do not match the response body, the check will fail.
     * 
     */
    @Import(name="failIfBodyNotMatchesRegexps")
    private @Nullable Output<List<String>> failIfBodyNotMatchesRegexps;

    /**
     * @return List of regexes. If any do not match the response body, the check will fail.
     * 
     */
    public Optional<Output<List<String>>> failIfBodyNotMatchesRegexps() {
        return Optional.ofNullable(this.failIfBodyNotMatchesRegexps);
    }

    /**
     * Check fails if headers match.
     * 
     */
    @Import(name="failIfHeaderMatchesRegexps")
    private @Nullable Output<List<SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpArgs>> failIfHeaderMatchesRegexps;

    /**
     * @return Check fails if headers match.
     * 
     */
    public Optional<Output<List<SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpArgs>>> failIfHeaderMatchesRegexps() {
        return Optional.ofNullable(this.failIfHeaderMatchesRegexps);
    }

    /**
     * Check fails if headers do not match.
     * 
     */
    @Import(name="failIfHeaderNotMatchesRegexps")
    private @Nullable Output<List<SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpArgs>> failIfHeaderNotMatchesRegexps;

    /**
     * @return Check fails if headers do not match.
     * 
     */
    public Optional<Output<List<SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpArgs>>> failIfHeaderNotMatchesRegexps() {
        return Optional.ofNullable(this.failIfHeaderNotMatchesRegexps);
    }

    /**
     * Fail if SSL is not present. Defaults to `false`.
     * 
     */
    @Import(name="failIfNotSsl")
    private @Nullable Output<Boolean> failIfNotSsl;

    /**
     * @return Fail if SSL is not present. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> failIfNotSsl() {
        return Optional.ofNullable(this.failIfNotSsl);
    }

    /**
     * Fail if SSL is present. Defaults to `false`.
     * 
     */
    @Import(name="failIfSsl")
    private @Nullable Output<Boolean> failIfSsl;

    /**
     * @return Fail if SSL is present. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> failIfSsl() {
        return Optional.ofNullable(this.failIfSsl);
    }

    /**
     * The HTTP headers set for the probe.
     * 
     */
    @Import(name="headers")
    private @Nullable Output<List<String>> headers;

    /**
     * @return The HTTP headers set for the probe.
     * 
     */
    public Optional<Output<List<String>>> headers() {
        return Optional.ofNullable(this.headers);
    }

    /**
     * Options are `V4`, `V6`, `Any`. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The `Any` value indicates that IPv6 should be used, falling back to IPv4 if that&#39;s not available. Defaults to `V4`.
     * 
     */
    @Import(name="ipVersion")
    private @Nullable Output<String> ipVersion;

    /**
     * @return Options are `V4`, `V6`, `Any`. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The `Any` value indicates that IPv6 should be used, falling back to IPv4 if that&#39;s not available. Defaults to `V4`.
     * 
     */
    public Optional<Output<String>> ipVersion() {
        return Optional.ofNullable(this.ipVersion);
    }

    /**
     * Request method. One of `GET`, `CONNECT`, `DELETE`, `HEAD`, `OPTIONS`, `POST`, `PUT`, `TRACE` Defaults to `GET`.
     * 
     */
    @Import(name="method")
    private @Nullable Output<String> method;

    /**
     * @return Request method. One of `GET`, `CONNECT`, `DELETE`, `HEAD`, `OPTIONS`, `POST`, `PUT`, `TRACE` Defaults to `GET`.
     * 
     */
    public Optional<Output<String>> method() {
        return Optional.ofNullable(this.method);
    }

    /**
     * Do not follow redirects. Defaults to `false`.
     * 
     */
    @Import(name="noFollowRedirects")
    private @Nullable Output<Boolean> noFollowRedirects;

    /**
     * @return Do not follow redirects. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> noFollowRedirects() {
        return Optional.ofNullable(this.noFollowRedirects);
    }

    /**
     * Proxy URL.
     * 
     */
    @Import(name="proxyUrl")
    private @Nullable Output<String> proxyUrl;

    /**
     * @return Proxy URL.
     * 
     */
    public Optional<Output<String>> proxyUrl() {
        return Optional.ofNullable(this.proxyUrl);
    }

    /**
     * TLS config.
     * 
     */
    @Import(name="tlsConfig")
    private @Nullable Output<SyntheticMonitoringCheckSettingsHttpTlsConfigArgs> tlsConfig;

    /**
     * @return TLS config.
     * 
     */
    public Optional<Output<SyntheticMonitoringCheckSettingsHttpTlsConfigArgs>> tlsConfig() {
        return Optional.ofNullable(this.tlsConfig);
    }

    /**
     * List of valid HTTP versions. Options include `HTTP/1.0`, `HTTP/1.1`, `HTTP/2.0`
     * 
     */
    @Import(name="validHttpVersions")
    private @Nullable Output<List<String>> validHttpVersions;

    /**
     * @return List of valid HTTP versions. Options include `HTTP/1.0`, `HTTP/1.1`, `HTTP/2.0`
     * 
     */
    public Optional<Output<List<String>>> validHttpVersions() {
        return Optional.ofNullable(this.validHttpVersions);
    }

    /**
     * Accepted status codes. If unset, defaults to 2xx.
     * 
     */
    @Import(name="validStatusCodes")
    private @Nullable Output<List<Integer>> validStatusCodes;

    /**
     * @return Accepted status codes. If unset, defaults to 2xx.
     * 
     */
    public Optional<Output<List<Integer>>> validStatusCodes() {
        return Optional.ofNullable(this.validStatusCodes);
    }

    private SyntheticMonitoringCheckSettingsHttpArgs() {}

    private SyntheticMonitoringCheckSettingsHttpArgs(SyntheticMonitoringCheckSettingsHttpArgs $) {
        this.basicAuth = $.basicAuth;
        this.bearerToken = $.bearerToken;
        this.body = $.body;
        this.cacheBustingQueryParamName = $.cacheBustingQueryParamName;
        this.failIfBodyMatchesRegexps = $.failIfBodyMatchesRegexps;
        this.failIfBodyNotMatchesRegexps = $.failIfBodyNotMatchesRegexps;
        this.failIfHeaderMatchesRegexps = $.failIfHeaderMatchesRegexps;
        this.failIfHeaderNotMatchesRegexps = $.failIfHeaderNotMatchesRegexps;
        this.failIfNotSsl = $.failIfNotSsl;
        this.failIfSsl = $.failIfSsl;
        this.headers = $.headers;
        this.ipVersion = $.ipVersion;
        this.method = $.method;
        this.noFollowRedirects = $.noFollowRedirects;
        this.proxyUrl = $.proxyUrl;
        this.tlsConfig = $.tlsConfig;
        this.validHttpVersions = $.validHttpVersions;
        this.validStatusCodes = $.validStatusCodes;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(SyntheticMonitoringCheckSettingsHttpArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private SyntheticMonitoringCheckSettingsHttpArgs $;

        public Builder() {
            $ = new SyntheticMonitoringCheckSettingsHttpArgs();
        }

        public Builder(SyntheticMonitoringCheckSettingsHttpArgs defaults) {
            $ = new SyntheticMonitoringCheckSettingsHttpArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param basicAuth Basic auth settings.
         * 
         * @return builder
         * 
         */
        public Builder basicAuth(@Nullable Output<SyntheticMonitoringCheckSettingsHttpBasicAuthArgs> basicAuth) {
            $.basicAuth = basicAuth;
            return this;
        }

        /**
         * @param basicAuth Basic auth settings.
         * 
         * @return builder
         * 
         */
        public Builder basicAuth(SyntheticMonitoringCheckSettingsHttpBasicAuthArgs basicAuth) {
            return basicAuth(Output.of(basicAuth));
        }

        /**
         * @param bearerToken Token for use with bearer authorization header.
         * 
         * @return builder
         * 
         */
        public Builder bearerToken(@Nullable Output<String> bearerToken) {
            $.bearerToken = bearerToken;
            return this;
        }

        /**
         * @param bearerToken Token for use with bearer authorization header.
         * 
         * @return builder
         * 
         */
        public Builder bearerToken(String bearerToken) {
            return bearerToken(Output.of(bearerToken));
        }

        /**
         * @param body The body of the HTTP request used in probe.
         * 
         * @return builder
         * 
         */
        public Builder body(@Nullable Output<String> body) {
            $.body = body;
            return this;
        }

        /**
         * @param body The body of the HTTP request used in probe.
         * 
         * @return builder
         * 
         */
        public Builder body(String body) {
            return body(Output.of(body));
        }

        /**
         * @param cacheBustingQueryParamName The name of the query parameter used to prevent the server from using a cached response. Each probe will assign a random value to this parameter each time a request is made.
         * 
         * @return builder
         * 
         */
        public Builder cacheBustingQueryParamName(@Nullable Output<String> cacheBustingQueryParamName) {
            $.cacheBustingQueryParamName = cacheBustingQueryParamName;
            return this;
        }

        /**
         * @param cacheBustingQueryParamName The name of the query parameter used to prevent the server from using a cached response. Each probe will assign a random value to this parameter each time a request is made.
         * 
         * @return builder
         * 
         */
        public Builder cacheBustingQueryParamName(String cacheBustingQueryParamName) {
            return cacheBustingQueryParamName(Output.of(cacheBustingQueryParamName));
        }

        /**
         * @param failIfBodyMatchesRegexps List of regexes. If any match the response body, the check will fail.
         * 
         * @return builder
         * 
         */
        public Builder failIfBodyMatchesRegexps(@Nullable Output<List<String>> failIfBodyMatchesRegexps) {
            $.failIfBodyMatchesRegexps = failIfBodyMatchesRegexps;
            return this;
        }

        /**
         * @param failIfBodyMatchesRegexps List of regexes. If any match the response body, the check will fail.
         * 
         * @return builder
         * 
         */
        public Builder failIfBodyMatchesRegexps(List<String> failIfBodyMatchesRegexps) {
            return failIfBodyMatchesRegexps(Output.of(failIfBodyMatchesRegexps));
        }

        /**
         * @param failIfBodyMatchesRegexps List of regexes. If any match the response body, the check will fail.
         * 
         * @return builder
         * 
         */
        public Builder failIfBodyMatchesRegexps(String... failIfBodyMatchesRegexps) {
            return failIfBodyMatchesRegexps(List.of(failIfBodyMatchesRegexps));
        }

        /**
         * @param failIfBodyNotMatchesRegexps List of regexes. If any do not match the response body, the check will fail.
         * 
         * @return builder
         * 
         */
        public Builder failIfBodyNotMatchesRegexps(@Nullable Output<List<String>> failIfBodyNotMatchesRegexps) {
            $.failIfBodyNotMatchesRegexps = failIfBodyNotMatchesRegexps;
            return this;
        }

        /**
         * @param failIfBodyNotMatchesRegexps List of regexes. If any do not match the response body, the check will fail.
         * 
         * @return builder
         * 
         */
        public Builder failIfBodyNotMatchesRegexps(List<String> failIfBodyNotMatchesRegexps) {
            return failIfBodyNotMatchesRegexps(Output.of(failIfBodyNotMatchesRegexps));
        }

        /**
         * @param failIfBodyNotMatchesRegexps List of regexes. If any do not match the response body, the check will fail.
         * 
         * @return builder
         * 
         */
        public Builder failIfBodyNotMatchesRegexps(String... failIfBodyNotMatchesRegexps) {
            return failIfBodyNotMatchesRegexps(List.of(failIfBodyNotMatchesRegexps));
        }

        /**
         * @param failIfHeaderMatchesRegexps Check fails if headers match.
         * 
         * @return builder
         * 
         */
        public Builder failIfHeaderMatchesRegexps(@Nullable Output<List<SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpArgs>> failIfHeaderMatchesRegexps) {
            $.failIfHeaderMatchesRegexps = failIfHeaderMatchesRegexps;
            return this;
        }

        /**
         * @param failIfHeaderMatchesRegexps Check fails if headers match.
         * 
         * @return builder
         * 
         */
        public Builder failIfHeaderMatchesRegexps(List<SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpArgs> failIfHeaderMatchesRegexps) {
            return failIfHeaderMatchesRegexps(Output.of(failIfHeaderMatchesRegexps));
        }

        /**
         * @param failIfHeaderMatchesRegexps Check fails if headers match.
         * 
         * @return builder
         * 
         */
        public Builder failIfHeaderMatchesRegexps(SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpArgs... failIfHeaderMatchesRegexps) {
            return failIfHeaderMatchesRegexps(List.of(failIfHeaderMatchesRegexps));
        }

        /**
         * @param failIfHeaderNotMatchesRegexps Check fails if headers do not match.
         * 
         * @return builder
         * 
         */
        public Builder failIfHeaderNotMatchesRegexps(@Nullable Output<List<SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpArgs>> failIfHeaderNotMatchesRegexps) {
            $.failIfHeaderNotMatchesRegexps = failIfHeaderNotMatchesRegexps;
            return this;
        }

        /**
         * @param failIfHeaderNotMatchesRegexps Check fails if headers do not match.
         * 
         * @return builder
         * 
         */
        public Builder failIfHeaderNotMatchesRegexps(List<SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpArgs> failIfHeaderNotMatchesRegexps) {
            return failIfHeaderNotMatchesRegexps(Output.of(failIfHeaderNotMatchesRegexps));
        }

        /**
         * @param failIfHeaderNotMatchesRegexps Check fails if headers do not match.
         * 
         * @return builder
         * 
         */
        public Builder failIfHeaderNotMatchesRegexps(SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpArgs... failIfHeaderNotMatchesRegexps) {
            return failIfHeaderNotMatchesRegexps(List.of(failIfHeaderNotMatchesRegexps));
        }

        /**
         * @param failIfNotSsl Fail if SSL is not present. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder failIfNotSsl(@Nullable Output<Boolean> failIfNotSsl) {
            $.failIfNotSsl = failIfNotSsl;
            return this;
        }

        /**
         * @param failIfNotSsl Fail if SSL is not present. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder failIfNotSsl(Boolean failIfNotSsl) {
            return failIfNotSsl(Output.of(failIfNotSsl));
        }

        /**
         * @param failIfSsl Fail if SSL is present. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder failIfSsl(@Nullable Output<Boolean> failIfSsl) {
            $.failIfSsl = failIfSsl;
            return this;
        }

        /**
         * @param failIfSsl Fail if SSL is present. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder failIfSsl(Boolean failIfSsl) {
            return failIfSsl(Output.of(failIfSsl));
        }

        /**
         * @param headers The HTTP headers set for the probe.
         * 
         * @return builder
         * 
         */
        public Builder headers(@Nullable Output<List<String>> headers) {
            $.headers = headers;
            return this;
        }

        /**
         * @param headers The HTTP headers set for the probe.
         * 
         * @return builder
         * 
         */
        public Builder headers(List<String> headers) {
            return headers(Output.of(headers));
        }

        /**
         * @param headers The HTTP headers set for the probe.
         * 
         * @return builder
         * 
         */
        public Builder headers(String... headers) {
            return headers(List.of(headers));
        }

        /**
         * @param ipVersion Options are `V4`, `V6`, `Any`. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The `Any` value indicates that IPv6 should be used, falling back to IPv4 if that&#39;s not available. Defaults to `V4`.
         * 
         * @return builder
         * 
         */
        public Builder ipVersion(@Nullable Output<String> ipVersion) {
            $.ipVersion = ipVersion;
            return this;
        }

        /**
         * @param ipVersion Options are `V4`, `V6`, `Any`. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The `Any` value indicates that IPv6 should be used, falling back to IPv4 if that&#39;s not available. Defaults to `V4`.
         * 
         * @return builder
         * 
         */
        public Builder ipVersion(String ipVersion) {
            return ipVersion(Output.of(ipVersion));
        }

        /**
         * @param method Request method. One of `GET`, `CONNECT`, `DELETE`, `HEAD`, `OPTIONS`, `POST`, `PUT`, `TRACE` Defaults to `GET`.
         * 
         * @return builder
         * 
         */
        public Builder method(@Nullable Output<String> method) {
            $.method = method;
            return this;
        }

        /**
         * @param method Request method. One of `GET`, `CONNECT`, `DELETE`, `HEAD`, `OPTIONS`, `POST`, `PUT`, `TRACE` Defaults to `GET`.
         * 
         * @return builder
         * 
         */
        public Builder method(String method) {
            return method(Output.of(method));
        }

        /**
         * @param noFollowRedirects Do not follow redirects. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder noFollowRedirects(@Nullable Output<Boolean> noFollowRedirects) {
            $.noFollowRedirects = noFollowRedirects;
            return this;
        }

        /**
         * @param noFollowRedirects Do not follow redirects. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder noFollowRedirects(Boolean noFollowRedirects) {
            return noFollowRedirects(Output.of(noFollowRedirects));
        }

        /**
         * @param proxyUrl Proxy URL.
         * 
         * @return builder
         * 
         */
        public Builder proxyUrl(@Nullable Output<String> proxyUrl) {
            $.proxyUrl = proxyUrl;
            return this;
        }

        /**
         * @param proxyUrl Proxy URL.
         * 
         * @return builder
         * 
         */
        public Builder proxyUrl(String proxyUrl) {
            return proxyUrl(Output.of(proxyUrl));
        }

        /**
         * @param tlsConfig TLS config.
         * 
         * @return builder
         * 
         */
        public Builder tlsConfig(@Nullable Output<SyntheticMonitoringCheckSettingsHttpTlsConfigArgs> tlsConfig) {
            $.tlsConfig = tlsConfig;
            return this;
        }

        /**
         * @param tlsConfig TLS config.
         * 
         * @return builder
         * 
         */
        public Builder tlsConfig(SyntheticMonitoringCheckSettingsHttpTlsConfigArgs tlsConfig) {
            return tlsConfig(Output.of(tlsConfig));
        }

        /**
         * @param validHttpVersions List of valid HTTP versions. Options include `HTTP/1.0`, `HTTP/1.1`, `HTTP/2.0`
         * 
         * @return builder
         * 
         */
        public Builder validHttpVersions(@Nullable Output<List<String>> validHttpVersions) {
            $.validHttpVersions = validHttpVersions;
            return this;
        }

        /**
         * @param validHttpVersions List of valid HTTP versions. Options include `HTTP/1.0`, `HTTP/1.1`, `HTTP/2.0`
         * 
         * @return builder
         * 
         */
        public Builder validHttpVersions(List<String> validHttpVersions) {
            return validHttpVersions(Output.of(validHttpVersions));
        }

        /**
         * @param validHttpVersions List of valid HTTP versions. Options include `HTTP/1.0`, `HTTP/1.1`, `HTTP/2.0`
         * 
         * @return builder
         * 
         */
        public Builder validHttpVersions(String... validHttpVersions) {
            return validHttpVersions(List.of(validHttpVersions));
        }

        /**
         * @param validStatusCodes Accepted status codes. If unset, defaults to 2xx.
         * 
         * @return builder
         * 
         */
        public Builder validStatusCodes(@Nullable Output<List<Integer>> validStatusCodes) {
            $.validStatusCodes = validStatusCodes;
            return this;
        }

        /**
         * @param validStatusCodes Accepted status codes. If unset, defaults to 2xx.
         * 
         * @return builder
         * 
         */
        public Builder validStatusCodes(List<Integer> validStatusCodes) {
            return validStatusCodes(Output.of(validStatusCodes));
        }

        /**
         * @param validStatusCodes Accepted status codes. If unset, defaults to 2xx.
         * 
         * @return builder
         * 
         */
        public Builder validStatusCodes(Integer... validStatusCodes) {
            return validStatusCodes(List.of(validStatusCodes));
        }

        public SyntheticMonitoringCheckSettingsHttpArgs build() {
            return $;
        }
    }

}
