// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.OnCall.Outputs
{

    [OutputType]
    public sealed class RouteSlack
    {
        /// <summary>
        /// Slack channel id. Alerts will be directed to this channel in Slack.
        /// </summary>
        public readonly string? ChannelId;
        /// <summary>
        /// Enable notification in Slack. Defaults to `true`.
        /// </summary>
        public readonly bool? Enabled;

        [OutputConstructor]
        private RouteSlack(
            string? channelId,

            bool? enabled)
        {
            ChannelId = channelId;
            Enabled = enabled;
        }
    }
}
