// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs.PulumiPackage.Grafana.Inputs
{

    public sealed class DataSourceSecureJsonDataArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// (CloudWatch, Athena) The access key used to access the data source.
        /// </summary>
        [Input("accessKey")]
        public Input<string>? AccessKey { get; set; }

        /// <summary>
        /// (Github) The access token used to access the data source.
        /// </summary>
        [Input("accessToken")]
        public Input<string>? AccessToken { get; set; }

        /// <summary>
        /// (Sentry) Authorization token.
        /// </summary>
        [Input("authToken")]
        public Input<string>? AuthToken { get; set; }

        /// <summary>
        /// (All) Password to use for basic authentication.
        /// </summary>
        [Input("basicAuthPassword")]
        public Input<string>? BasicAuthPassword { get; set; }

        /// <summary>
        /// (Azure Monitor) Client secret for authentication.
        /// </summary>
        [Input("clientSecret")]
        public Input<string>? ClientSecret { get; set; }

        /// <summary>
        /// (All) Password to use for authentication.
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// (Stackdriver) The service account key `private_key` to use to access the data source.
        /// </summary>
        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        /// <summary>
        /// (CloudWatch, Athena) The secret key to use to access the data source.
        /// </summary>
        [Input("secretKey")]
        public Input<string>? SecretKey { get; set; }

        /// <summary>
        /// (Elasticsearch and Prometheus) SigV4 access key. Required when using 'keys' auth provider.
        /// </summary>
        [Input("sigv4AccessKey")]
        public Input<string>? Sigv4AccessKey { get; set; }

        /// <summary>
        /// (Elasticsearch and Prometheus) SigV4 secret key. Required when using 'keys' auth provider.
        /// </summary>
        [Input("sigv4SecretKey")]
        public Input<string>? Sigv4SecretKey { get; set; }

        /// <summary>
        /// (All) CA cert for out going requests.
        /// </summary>
        [Input("tlsCaCert")]
        public Input<string>? TlsCaCert { get; set; }

        /// <summary>
        /// (All) TLS Client cert for outgoing requests.
        /// </summary>
        [Input("tlsClientCert")]
        public Input<string>? TlsClientCert { get; set; }

        /// <summary>
        /// (All) TLS Client key for outgoing requests.
        /// </summary>
        [Input("tlsClientKey")]
        public Input<string>? TlsClientKey { get; set; }

        public DataSourceSecureJsonDataArgs()
        {
        }
        public static new DataSourceSecureJsonDataArgs Empty => new DataSourceSecureJsonDataArgs();
    }
}
