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

    public sealed class ContactPointAlertmanagerGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("basicAuthPassword")]
        private Input<string>? _basicAuthPassword;

        /// <summary>
        /// The password component of the basic auth credentials to use.
        /// </summary>
        public Input<string>? BasicAuthPassword
        {
            get => _basicAuthPassword;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _basicAuthPassword = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The username component of the basic auth credentials to use.
        /// </summary>
        [Input("basicAuthUser")]
        public Input<string>? BasicAuthUser { get; set; }

        /// <summary>
        /// Whether to disable sending resolve messages. Defaults to `false`.
        /// </summary>
        [Input("disableResolveMessage")]
        public Input<bool>? DisableResolveMessage { get; set; }

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
        /// The UID of the contact point.
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        /// <summary>
        /// The URL of the Alertmanager instance.
        /// </summary>
        [Input("url", required: true)]
        public Input<string> Url { get; set; } = null!;

        public ContactPointAlertmanagerGetArgs()
        {
        }
        public static new ContactPointAlertmanagerGetArgs Empty => new ContactPointAlertmanagerGetArgs();
    }
}
