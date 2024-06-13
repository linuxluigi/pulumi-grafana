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

    public sealed class ContactPointTelegramGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The chat ID to send messages to.
        /// </summary>
        [Input("chatId", required: true)]
        public Input<string> ChatId { get; set; } = null!;

        /// <summary>
        /// When set users will receive a notification with no sound.
        /// </summary>
        [Input("disableNotifications")]
        public Input<bool>? DisableNotifications { get; set; }

        /// <summary>
        /// Whether to disable sending resolve messages. Defaults to `false`.
        /// </summary>
        [Input("disableResolveMessage")]
        public Input<bool>? DisableResolveMessage { get; set; }

        /// <summary>
        /// When set it disables link previews for links in the message.
        /// </summary>
        [Input("disableWebPagePreview")]
        public Input<bool>? DisableWebPagePreview { get; set; }

        /// <summary>
        /// The templated content of the message.
        /// </summary>
        [Input("message")]
        public Input<string>? Message { get; set; }

        /// <summary>
        /// Mode for parsing entities in the message text. Supported: None, Markdown, MarkdownV2, and HTML. HTML is the default.
        /// </summary>
        [Input("parseMode")]
        public Input<string>? ParseMode { get; set; }

        /// <summary>
        /// When set it protects the contents of the message from forwarding and saving.
        /// </summary>
        [Input("protectContent")]
        public Input<bool>? ProtectContent { get; set; }

        [Input("settings")]
        private InputMap<string>? _settings;

        /// <summary>
        /// Additional custom properties to attach to the notifier. Defaults to `map[]`.
        /// </summary>
        public InputMap<string> Settings
        {
            get => _settings ?? (_settings = new InputMap<string>());
            set
            {
                var emptySecret = Output.CreateSecret(ImmutableDictionary.Create<string, string>());
                _settings = Output.All(value, emptySecret).Apply(v => v[0]);
            }
        }

        [Input("token", required: true)]
        private Input<string>? _token;

        /// <summary>
        /// The Telegram bot token.
        /// </summary>
        public Input<string>? Token
        {
            get => _token;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _token = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The UID of the contact point.
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        public ContactPointTelegramGetArgs()
        {
        }
        public static new ContactPointTelegramGetArgs Empty => new ContactPointTelegramGetArgs();
    }
}
