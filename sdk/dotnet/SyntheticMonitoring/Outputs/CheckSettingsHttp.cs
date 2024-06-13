// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.SyntheticMonitoring.Outputs
{

    [OutputType]
    public sealed class CheckSettingsHttp
    {
        /// <summary>
        /// Basic auth settings.
        /// </summary>
        public readonly Outputs.CheckSettingsHttpBasicAuth? BasicAuth;
        /// <summary>
        /// Token for use with bearer authorization header.
        /// </summary>
        public readonly string? BearerToken;
        /// <summary>
        /// The body of the HTTP request used in probe.
        /// </summary>
        public readonly string? Body;
        /// <summary>
        /// The name of the query parameter used to prevent the server from using a cached response. Each probe will assign a random value to this parameter each time a request is made.
        /// </summary>
        public readonly string? CacheBustingQueryParamName;
        /// <summary>
        /// List of regexes. If any match the response body, the check will fail.
        /// </summary>
        public readonly ImmutableArray<string> FailIfBodyMatchesRegexps;
        /// <summary>
        /// List of regexes. If any do not match the response body, the check will fail.
        /// </summary>
        public readonly ImmutableArray<string> FailIfBodyNotMatchesRegexps;
        /// <summary>
        /// Check fails if headers match.
        /// </summary>
        public readonly ImmutableArray<Outputs.CheckSettingsHttpFailIfHeaderMatchesRegexp> FailIfHeaderMatchesRegexps;
        /// <summary>
        /// Check fails if headers do not match.
        /// </summary>
        public readonly ImmutableArray<Outputs.CheckSettingsHttpFailIfHeaderNotMatchesRegexp> FailIfHeaderNotMatchesRegexps;
        /// <summary>
        /// Fail if SSL is not present. Defaults to `false`.
        /// </summary>
        public readonly bool? FailIfNotSsl;
        /// <summary>
        /// Fail if SSL is present. Defaults to `false`.
        /// </summary>
        public readonly bool? FailIfSsl;
        /// <summary>
        /// The HTTP headers set for the probe.
        /// </summary>
        public readonly ImmutableArray<string> Headers;
        /// <summary>
        /// Options are `V4`, `V6`, `Any`. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The `Any` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to `V4`.
        /// </summary>
        public readonly string? IpVersion;
        /// <summary>
        /// Request method. One of `GET`, `CONNECT`, `DELETE`, `HEAD`, `OPTIONS`, `POST`, `PUT`, `TRACE` Defaults to `GET`.
        /// </summary>
        public readonly string? Method;
        /// <summary>
        /// Do not follow redirects. Defaults to `false`.
        /// </summary>
        public readonly bool? NoFollowRedirects;
        /// <summary>
        /// The HTTP headers sent to the proxy URL
        /// </summary>
        public readonly ImmutableArray<string> ProxyConnectHeaders;
        /// <summary>
        /// Proxy URL.
        /// </summary>
        public readonly string? ProxyUrl;
        /// <summary>
        /// TLS config.
        /// </summary>
        public readonly Outputs.CheckSettingsHttpTlsConfig? TlsConfig;
        /// <summary>
        /// List of valid HTTP versions. Options include `HTTP/1.0`, `HTTP/1.1`, `HTTP/2.0`
        /// </summary>
        public readonly ImmutableArray<string> ValidHttpVersions;
        /// <summary>
        /// Accepted status codes. If unset, defaults to 2xx.
        /// </summary>
        public readonly ImmutableArray<int> ValidStatusCodes;

        [OutputConstructor]
        private CheckSettingsHttp(
            Outputs.CheckSettingsHttpBasicAuth? basicAuth,

            string? bearerToken,

            string? body,

            string? cacheBustingQueryParamName,

            ImmutableArray<string> failIfBodyMatchesRegexps,

            ImmutableArray<string> failIfBodyNotMatchesRegexps,

            ImmutableArray<Outputs.CheckSettingsHttpFailIfHeaderMatchesRegexp> failIfHeaderMatchesRegexps,

            ImmutableArray<Outputs.CheckSettingsHttpFailIfHeaderNotMatchesRegexp> failIfHeaderNotMatchesRegexps,

            bool? failIfNotSsl,

            bool? failIfSsl,

            ImmutableArray<string> headers,

            string? ipVersion,

            string? method,

            bool? noFollowRedirects,

            ImmutableArray<string> proxyConnectHeaders,

            string? proxyUrl,

            Outputs.CheckSettingsHttpTlsConfig? tlsConfig,

            ImmutableArray<string> validHttpVersions,

            ImmutableArray<int> validStatusCodes)
        {
            BasicAuth = basicAuth;
            BearerToken = bearerToken;
            Body = body;
            CacheBustingQueryParamName = cacheBustingQueryParamName;
            FailIfBodyMatchesRegexps = failIfBodyMatchesRegexps;
            FailIfBodyNotMatchesRegexps = failIfBodyNotMatchesRegexps;
            FailIfHeaderMatchesRegexps = failIfHeaderMatchesRegexps;
            FailIfHeaderNotMatchesRegexps = failIfHeaderNotMatchesRegexps;
            FailIfNotSsl = failIfNotSsl;
            FailIfSsl = failIfSsl;
            Headers = headers;
            IpVersion = ipVersion;
            Method = method;
            NoFollowRedirects = noFollowRedirects;
            ProxyConnectHeaders = proxyConnectHeaders;
            ProxyUrl = proxyUrl;
            TlsConfig = tlsConfig;
            ValidHttpVersions = validHttpVersions;
            ValidStatusCodes = validStatusCodes;
        }
    }
}
