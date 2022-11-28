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

    public sealed class ContactPointPushoverGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Pushover API token.
        /// </summary>
        [Input("apiToken", required: true)]
        public Input<string> ApiToken { get; set; } = null!;

        /// <summary>
        /// Comma-separated list of devices to which the event is associated.
        /// </summary>
        [Input("device")]
        public Input<string>? Device { get; set; }

        /// <summary>
        /// Whether to disable sending resolve messages. Defaults to `false`.
        /// </summary>
        [Input("disableResolveMessage")]
        public Input<bool>? DisableResolveMessage { get; set; }

        /// <summary>
        /// How many seconds for which the notification will continue to be retried by Pushover.
        /// </summary>
        [Input("expire")]
        public Input<int>? Expire { get; set; }

        /// <summary>
        /// The templated notification message content.
        /// </summary>
        [Input("message")]
        public Input<string>? Message { get; set; }

        /// <summary>
        /// The priority level of the resolved event.
        /// </summary>
        [Input("okPriority")]
        public Input<int>? OkPriority { get; set; }

        /// <summary>
        /// The sound associated with the resolved notification.
        /// </summary>
        [Input("okSound")]
        public Input<string>? OkSound { get; set; }

        /// <summary>
        /// The priority level of the event.
        /// </summary>
        [Input("priority")]
        public Input<int>? Priority { get; set; }

        /// <summary>
        /// How often, in seconds, the Pushover servers will send the same notification to the user.
        /// </summary>
        [Input("retry")]
        public Input<int>? Retry { get; set; }

        [Input("settings")]
        private InputMap<string>? _settings;

        /// <summary>
        /// Additional custom properties to attach to the notifier. Defaults to `map[]`.
        /// </summary>
        public InputMap<string> Settings
        {
            get => _settings ?? (_settings = new InputMap<string>());
            set => _settings = value;
        }

        /// <summary>
        /// The sound associated with the notification.
        /// </summary>
        [Input("sound")]
        public Input<string>? Sound { get; set; }

        /// <summary>
        /// The UID of the contact point.
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        /// <summary>
        /// The Pushover user key.
        /// </summary>
        [Input("userKey", required: true)]
        public Input<string> UserKey { get; set; } = null!;

        public ContactPointPushoverGetArgs()
        {
        }
        public static new ContactPointPushoverGetArgs Empty => new ContactPointPushoverGetArgs();
    }
}
