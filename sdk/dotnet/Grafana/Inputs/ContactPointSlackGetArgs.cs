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

    public sealed class ContactPointSlackGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether to disable sending resolve messages. Defaults to `false`.
        /// </summary>
        [Input("disableResolveMessage")]
        public Input<bool>? DisableResolveMessage { get; set; }

        /// <summary>
        /// Use this to override the Slack API endpoint URL to send requests to.
        /// </summary>
        [Input("endpointUrl")]
        public Input<string>? EndpointUrl { get; set; }

        /// <summary>
        /// The name of a Slack workspace emoji to use as the bot icon.
        /// </summary>
        [Input("iconEmoji")]
        public Input<string>? IconEmoji { get; set; }

        /// <summary>
        /// A URL of an image to use as the bot icon.
        /// </summary>
        [Input("iconUrl")]
        public Input<string>? IconUrl { get; set; }

        /// <summary>
        /// Describes how to ping the slack channel that messages are being sent to. Options are `here` for an @here ping, `channel` for @channel, or empty for no ping.
        /// </summary>
        [Input("mentionChannel")]
        public Input<string>? MentionChannel { get; set; }

        /// <summary>
        /// Comma-separated list of groups to mention in the message.
        /// </summary>
        [Input("mentionGroups")]
        public Input<string>? MentionGroups { get; set; }

        /// <summary>
        /// Comma-separated list of users to mention in the message.
        /// </summary>
        [Input("mentionUsers")]
        public Input<string>? MentionUsers { get; set; }

        /// <summary>
        /// Channel, private group, or IM channel (can be an encoded ID or a name) to send messages to.
        /// </summary>
        [Input("recipient")]
        public Input<string>? Recipient { get; set; }

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
        /// Templated content of the message.
        /// </summary>
        [Input("text")]
        public Input<string>? Text { get; set; }

        /// <summary>
        /// Templated title of the message.
        /// </summary>
        [Input("title")]
        public Input<string>? Title { get; set; }

        /// <summary>
        /// A Slack API token,for sending messages directly without the webhook method.
        /// </summary>
        [Input("token")]
        public Input<string>? Token { get; set; }

        /// <summary>
        /// The UID of the contact point.
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        /// <summary>
        /// A Slack webhook URL,for sending messages via the webhook method.
        /// </summary>
        [Input("url")]
        public Input<string>? Url { get; set; }

        /// <summary>
        /// Username for the bot to use.
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public ContactPointSlackGetArgs()
        {
        }
        public static new ContactPointSlackGetArgs Empty => new ContactPointSlackGetArgs();
    }
}
