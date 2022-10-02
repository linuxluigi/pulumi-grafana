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

    public sealed class ContactPointPagerdutyGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The class or type of event, for example `ping failure`.
        /// </summary>
        [Input("class")]
        public Input<string>? Class { get; set; }

        /// <summary>
        /// The component being affected by the event.
        /// </summary>
        [Input("component")]
        public Input<string>? Component { get; set; }

        /// <summary>
        /// Whether to disable sending resolve messages. Defaults to `false`.
        /// </summary>
        [Input("disableResolveMessage")]
        public Input<bool>? DisableResolveMessage { get; set; }

        /// <summary>
        /// The group to which the provided component belongs to.
        /// </summary>
        [Input("group")]
        public Input<string>? Group { get; set; }

        [Input("integrationKey", required: true)]
        private Input<string>? _integrationKey;

        /// <summary>
        /// The PagerDuty API key.
        /// </summary>
        public Input<string>? IntegrationKey
        {
            get => _integrationKey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _integrationKey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

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
        /// The PagerDuty event severity level. Default is `critical`.
        /// </summary>
        [Input("severity")]
        public Input<string>? Severity { get; set; }

        /// <summary>
        /// The templated summary message of the event.
        /// </summary>
        [Input("summary")]
        public Input<string>? Summary { get; set; }

        /// <summary>
        /// The UID of the contact point.
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        public ContactPointPagerdutyGetArgs()
        {
        }
        public static new ContactPointPagerdutyGetArgs Empty => new ContactPointPagerdutyGetArgs();
    }
}
