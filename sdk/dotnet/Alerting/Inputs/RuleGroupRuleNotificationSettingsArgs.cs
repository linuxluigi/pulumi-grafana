// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Alerting.Inputs
{

    public sealed class RuleGroupRuleNotificationSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The contact point to route notifications that match this rule to.
        /// </summary>
        [Input("contactPoint", required: true)]
        public Input<string> ContactPoint { get; set; } = null!;

        [Input("groupBies")]
        private InputList<string>? _groupBies;

        /// <summary>
        /// A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping. If empty, no grouping is used. If specified, requires labels 'alertname' and 'grafana_folder' to be included.
        /// </summary>
        public InputList<string> GroupBies
        {
            get => _groupBies ?? (_groupBies = new InputList<string>());
            set => _groupBies = value;
        }

        /// <summary>
        /// Minimum time interval between two notifications for the same group. Default is 5 minutes.
        /// </summary>
        [Input("groupInterval")]
        public Input<string>? GroupInterval { get; set; }

        /// <summary>
        /// Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.
        /// </summary>
        [Input("groupWait")]
        public Input<string>? GroupWait { get; set; }

        [Input("muteTimings")]
        private InputList<string>? _muteTimings;

        /// <summary>
        /// A list of mute timing names to apply to alerts that match this policy.
        /// </summary>
        public InputList<string> MuteTimings
        {
            get => _muteTimings ?? (_muteTimings = new InputList<string>());
            set => _muteTimings = value;
        }

        /// <summary>
        /// Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
        /// </summary>
        [Input("repeatInterval")]
        public Input<string>? RepeatInterval { get; set; }

        public RuleGroupRuleNotificationSettingsArgs()
        {
        }
        public static new RuleGroupRuleNotificationSettingsArgs Empty => new RuleGroupRuleNotificationSettingsArgs();
    }
}
