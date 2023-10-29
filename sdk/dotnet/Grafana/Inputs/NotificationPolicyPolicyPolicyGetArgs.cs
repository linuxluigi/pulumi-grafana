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

    public sealed class NotificationPolicyPolicyPolicyGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The contact point to route notifications that match this rule to.
        /// </summary>
        [Input("contactPoint", required: true)]
        public Input<string> ContactPoint { get; set; } = null!;

        /// <summary>
        /// Whether to continue matching subsequent rules if an alert matches the current rule. Otherwise, the rule will be 'consumed' by the first policy to match it.
        /// </summary>
        [Input("continue")]
        public Input<bool>? Continue { get; set; }

        [Input("groupBies")]
        private InputList<string>? _groupBies;

        /// <summary>
        /// A list of alert labels to group alerts into notifications by. Use the special label `...` to group alerts by all labels, effectively disabling grouping. Required for root policy only. If empty, the parent grouping is used.
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

        [Input("matchers")]
        private InputList<Inputs.NotificationPolicyPolicyPolicyMatcherGetArgs>? _matchers;

        /// <summary>
        /// Describes which labels this rule should match. When multiple matchers are supplied, an alert must match ALL matchers to be accepted by this policy. When no matchers are supplied, the rule will match all alert instances.
        /// </summary>
        public InputList<Inputs.NotificationPolicyPolicyPolicyMatcherGetArgs> Matchers
        {
            get => _matchers ?? (_matchers = new InputList<Inputs.NotificationPolicyPolicyPolicyMatcherGetArgs>());
            set => _matchers = value;
        }

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

        [Input("policies")]
        private InputList<Inputs.NotificationPolicyPolicyPolicyPolicyGetArgs>? _policies;

        /// <summary>
        /// Routing rules for specific label sets.
        /// </summary>
        public InputList<Inputs.NotificationPolicyPolicyPolicyPolicyGetArgs> Policies
        {
            get => _policies ?? (_policies = new InputList<Inputs.NotificationPolicyPolicyPolicyPolicyGetArgs>());
            set => _policies = value;
        }

        /// <summary>
        /// Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.
        /// </summary>
        [Input("repeatInterval")]
        public Input<string>? RepeatInterval { get; set; }

        public NotificationPolicyPolicyPolicyGetArgs()
        {
        }
        public static new NotificationPolicyPolicyPolicyGetArgs Empty => new NotificationPolicyPolicyPolicyGetArgs();
    }
}
