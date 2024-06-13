// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Outputs
{

    [OutputType]
    public sealed class ContactPointLine
    {
        /// <summary>
        /// The templated description of the message.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// Whether to disable sending resolve messages.
        /// </summary>
        public readonly bool? DisableResolveMessage;
        /// <summary>
        /// Additional custom properties to attach to the notifier.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Settings;
        /// <summary>
        /// The templated title of the message.
        /// </summary>
        public readonly string? Title;
        /// <summary>
        /// The bearer token used to authorize the client.
        /// </summary>
        public readonly string Token;
        /// <summary>
        /// The UID of the contact point.
        /// </summary>
        public readonly string? Uid;

        [OutputConstructor]
        private ContactPointLine(
            string? description,

            bool? disableResolveMessage,

            ImmutableDictionary<string, string>? settings,

            string? title,

            string token,

            string? uid)
        {
            Description = description;
            DisableResolveMessage = disableResolveMessage;
            Settings = settings;
            Title = title;
            Token = token;
            Uid = uid;
        }
    }
}
