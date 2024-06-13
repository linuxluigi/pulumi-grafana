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

    public sealed class ContactPointThreemaArgs : global::Pulumi.ResourceArgs
    {
        [Input("apiSecret", required: true)]
        private Input<string>? _apiSecret;

        /// <summary>
        /// The Threema API key.
        /// </summary>
        public Input<string>? ApiSecret
        {
            get => _apiSecret;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _apiSecret = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The templated description of the message.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Whether to disable sending resolve messages. Defaults to `false`.
        /// </summary>
        [Input("disableResolveMessage")]
        public Input<bool>? DisableResolveMessage { get; set; }

        /// <summary>
        /// The Threema gateway ID.
        /// </summary>
        [Input("gatewayId", required: true)]
        public Input<string> GatewayId { get; set; } = null!;

        /// <summary>
        /// The ID of the recipient of the message.
        /// </summary>
        [Input("recipientId", required: true)]
        public Input<string> RecipientId { get; set; } = null!;

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

        /// <summary>
        /// The templated title of the message.
        /// </summary>
        [Input("title")]
        public Input<string>? Title { get; set; }

        /// <summary>
        /// The UID of the contact point.
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        public ContactPointThreemaArgs()
        {
        }
        public static new ContactPointThreemaArgs Empty => new ContactPointThreemaArgs();
    }
}
