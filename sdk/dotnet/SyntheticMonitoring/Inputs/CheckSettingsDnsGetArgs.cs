// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.SyntheticMonitoring.Inputs
{

    public sealed class CheckSettingsDnsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Options are `V4`, `V6`, `Any`. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The `Any` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to `V4`.
        /// </summary>
        [Input("ipVersion")]
        public Input<string>? IpVersion { get; set; }

        /// <summary>
        /// Port to target. Defaults to `53`.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// `TCP` or `UDP`. Defaults to `UDP`.
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// One of `ANY`, `A`, `AAAA`, `CNAME`, `MX`, `NS`, `PTR`, `SOA`, `SRV`, `TXT`. Defaults to `A`.
        /// </summary>
        [Input("recordType")]
        public Input<string>? RecordType { get; set; }

        /// <summary>
        /// DNS server address to target. Defaults to `8.8.8.8`.
        /// </summary>
        [Input("server")]
        public Input<string>? Server { get; set; }

        /// <summary>
        /// Source IP address.
        /// </summary>
        [Input("sourceIpAddress")]
        public Input<string>? SourceIpAddress { get; set; }

        [Input("validRCodes")]
        private InputList<string>? _validRCodes;

        /// <summary>
        /// List of valid response codes. Options include `NOERROR`, `BADALG`, `BADMODE`, `BADKEY`, `BADCOOKIE`, `BADNAME`, `BADSIG`, `BADTIME`, `BADTRUNC`, `BADVERS`, `FORMERR`, `NOTIMP`, `NOTAUTH`, `NOTZONE`, `NXDOMAIN`, `NXRRSET`, `REFUSED`, `SERVFAIL`, `YXDOMAIN`, `YXRRSET`.
        /// </summary>
        public InputList<string> ValidRCodes
        {
            get => _validRCodes ?? (_validRCodes = new InputList<string>());
            set => _validRCodes = value;
        }

        [Input("validateAdditionalRrs")]
        private InputList<Inputs.CheckSettingsDnsValidateAdditionalRrGetArgs>? _validateAdditionalRrs;

        /// <summary>
        /// Validate additional matches.
        /// </summary>
        public InputList<Inputs.CheckSettingsDnsValidateAdditionalRrGetArgs> ValidateAdditionalRrs
        {
            get => _validateAdditionalRrs ?? (_validateAdditionalRrs = new InputList<Inputs.CheckSettingsDnsValidateAdditionalRrGetArgs>());
            set => _validateAdditionalRrs = value;
        }

        /// <summary>
        /// Validate response answer.
        /// </summary>
        [Input("validateAnswerRrs")]
        public Input<Inputs.CheckSettingsDnsValidateAnswerRrsGetArgs>? ValidateAnswerRrs { get; set; }

        /// <summary>
        /// Validate response authority.
        /// </summary>
        [Input("validateAuthorityRrs")]
        public Input<Inputs.CheckSettingsDnsValidateAuthorityRrsGetArgs>? ValidateAuthorityRrs { get; set; }

        public CheckSettingsDnsGetArgs()
        {
        }
        public static new CheckSettingsDnsGetArgs Empty => new CheckSettingsDnsGetArgs();
    }
}
