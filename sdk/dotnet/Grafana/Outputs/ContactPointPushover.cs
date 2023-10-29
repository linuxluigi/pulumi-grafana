// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs.PulumiPackage.Grafana.Outputs
{

    [OutputType]
    public sealed class ContactPointPushover
    {
        /// <summary>
        /// The Pushover API token.
        /// </summary>
        public readonly string ApiToken;
        /// <summary>
        /// Comma-separated list of devices to which the event is associated.
        /// </summary>
        public readonly string? Device;
        /// <summary>
        /// Whether to disable sending resolve messages. Defaults to `false`.
        /// </summary>
        public readonly bool? DisableResolveMessage;
        /// <summary>
        /// How many seconds for which the notification will continue to be retried by Pushover.
        /// </summary>
        public readonly int? Expire;
        /// <summary>
        /// The templated notification message content.
        /// </summary>
        public readonly string? Message;
        /// <summary>
        /// The priority level of the resolved event.
        /// </summary>
        public readonly int? OkPriority;
        /// <summary>
        /// The sound associated with the resolved notification.
        /// </summary>
        public readonly string? OkSound;
        /// <summary>
        /// The priority level of the event.
        /// </summary>
        public readonly int? Priority;
        /// <summary>
        /// How often, in seconds, the Pushover servers will send the same notification to the user.
        /// </summary>
        public readonly int? Retry;
        /// <summary>
        /// Additional custom properties to attach to the notifier. Defaults to `map[]`.
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Settings;
        /// <summary>
        /// The sound associated with the notification.
        /// </summary>
        public readonly string? Sound;
        /// <summary>
        /// The templated title of the message.
        /// </summary>
        public readonly string? Title;
        /// <summary>
        /// The UID of the contact point.
        /// </summary>
        public readonly string? Uid;
        /// <summary>
        /// Whether to send images in the notification or not. Default is true. Requires Grafana to be configured to send images in notifications.
        /// </summary>
        public readonly bool? UploadImage;
        /// <summary>
        /// The Pushover user key.
        /// </summary>
        public readonly string UserKey;

        [OutputConstructor]
        private ContactPointPushover(
            string apiToken,

            string? device,

            bool? disableResolveMessage,

            int? expire,

            string? message,

            int? okPriority,

            string? okSound,

            int? priority,

            int? retry,

            ImmutableDictionary<string, string>? settings,

            string? sound,

            string? title,

            string? uid,

            bool? uploadImage,

            string userKey)
        {
            ApiToken = apiToken;
            Device = device;
            DisableResolveMessage = disableResolveMessage;
            Expire = expire;
            Message = message;
            OkPriority = okPriority;
            OkSound = okSound;
            Priority = priority;
            Retry = retry;
            Settings = settings;
            Sound = sound;
            Title = title;
            Uid = uid;
            UploadImage = uploadImage;
            UserKey = userKey;
        }
    }
}
