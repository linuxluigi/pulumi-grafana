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

    public sealed class OncallIntegrationDefaultRouteSlackArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Slack channel id. Alerts will be directed to this channel in Slack.
        /// </summary>
        [Input("channelId")]
        public Input<string>? ChannelId { get; set; }

        /// <summary>
        /// Enable notification in MS teams. Defaults to `true`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        public OncallIntegrationDefaultRouteSlackArgs()
        {
        }
        public static new OncallIntegrationDefaultRouteSlackArgs Empty => new OncallIntegrationDefaultRouteSlackArgs();
    }
}
