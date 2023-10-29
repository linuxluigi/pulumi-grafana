// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs.PulumiPackage.Grafana.Outputs
{

    [OutputType]
    public sealed class SyntheticMonitoringCheckSettingsTcpTlsConfig
    {
        /// <summary>
        /// CA certificate in PEM format.
        /// </summary>
        public readonly string? CaCert;
        /// <summary>
        /// Client certificate in PEM format.
        /// </summary>
        public readonly string? ClientCert;
        /// <summary>
        /// Client key in PEM format.
        /// </summary>
        public readonly string? ClientKey;
        /// <summary>
        /// Disable target certificate validation. Defaults to `false`.
        /// </summary>
        public readonly bool? InsecureSkipVerify;
        /// <summary>
        /// Used to verify the hostname for the targets.
        /// </summary>
        public readonly string? ServerName;

        [OutputConstructor]
        private SyntheticMonitoringCheckSettingsTcpTlsConfig(
            string? caCert,

            string? clientCert,

            string? clientKey,

            bool? insecureSkipVerify,

            string? serverName)
        {
            CaCert = caCert;
            ClientCert = clientCert;
            ClientKey = clientKey;
            InsecureSkipVerify = insecureSkipVerify;
            ServerName = serverName;
        }
    }
}
