// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs.PulumiPackage.Grafana
{
    /// <summary>
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using Pulumi;
    /// using Grafana = Lbrlabs.PulumiPackage.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var emailSometeam = new Grafana.AlertNotification("emailSometeam", new()
    ///     {
    ///         Frequency = "24h",
    ///         IsDefault = false,
    ///         SendReminder = true,
    ///         Settings = 
    ///         {
    ///             { "addresses", "foo@example.net;bar@example.net" },
    ///             { "uploadImage", "false" },
    ///         },
    ///         Type = "email",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import grafana:index/alertNotification:AlertNotification alert_notification_name {{alert_notification_id}}
    /// ```
    /// </summary>
    [GrafanaResourceType("grafana:index/alertNotification:AlertNotification")]
    public partial class AlertNotification : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Whether to disable sending resolve messages. Defaults to `false`.
        /// </summary>
        [Output("disableResolveMessage")]
        public Output<bool?> DisableResolveMessage { get; private set; } = null!;

        /// <summary>
        /// Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.
        /// </summary>
        [Output("frequency")]
        public Output<string?> Frequency { get; private set; } = null!;

        /// <summary>
        /// Is this the default channel for all your alerts. Defaults to `false`.
        /// </summary>
        [Output("isDefault")]
        public Output<bool?> IsDefault { get; private set; } = null!;

        /// <summary>
        /// The name of the alert notification channel.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Additional secure settings, for full reference lookup [Grafana Supported Settings documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings).
        /// </summary>
        [Output("secureSettings")]
        public Output<ImmutableDictionary<string, object>?> SecureSettings { get; private set; } = null!;

        /// <summary>
        /// Whether to send reminders for triggered alerts. Defaults to `false`.
        /// </summary>
        [Output("sendReminder")]
        public Output<bool?> SendReminder { get; private set; } = null!;

        /// <summary>
        /// Additional settings, for full reference see [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/developers/http_api/alerting_notification_channels/).
        /// </summary>
        [Output("settings")]
        public Output<ImmutableDictionary<string, object>?> Settings { get; private set; } = null!;

        /// <summary>
        /// The type of the alert notification channel.
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;

        /// <summary>
        /// Unique identifier. If unset, this will be automatically generated.
        /// </summary>
        [Output("uid")]
        public Output<string> Uid { get; private set; } = null!;


        /// <summary>
        /// Create a AlertNotification resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AlertNotification(string name, AlertNotificationArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/alertNotification:AlertNotification", name, args ?? new AlertNotificationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AlertNotification(string name, Input<string> id, AlertNotificationState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/alertNotification:AlertNotification", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/lbrlabs",
                AdditionalSecretOutputs =
                {
                    "secureSettings",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AlertNotification resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AlertNotification Get(string name, Input<string> id, AlertNotificationState? state = null, CustomResourceOptions? options = null)
        {
            return new AlertNotification(name, id, state, options);
        }
    }

    public sealed class AlertNotificationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether to disable sending resolve messages. Defaults to `false`.
        /// </summary>
        [Input("disableResolveMessage")]
        public Input<bool>? DisableResolveMessage { get; set; }

        /// <summary>
        /// Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.
        /// </summary>
        [Input("frequency")]
        public Input<string>? Frequency { get; set; }

        /// <summary>
        /// Is this the default channel for all your alerts. Defaults to `false`.
        /// </summary>
        [Input("isDefault")]
        public Input<bool>? IsDefault { get; set; }

        /// <summary>
        /// The name of the alert notification channel.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("secureSettings")]
        private InputMap<object>? _secureSettings;

        /// <summary>
        /// Additional secure settings, for full reference lookup [Grafana Supported Settings documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings).
        /// </summary>
        public InputMap<object> SecureSettings
        {
            get => _secureSettings ?? (_secureSettings = new InputMap<object>());
            set
            {
                var emptySecret = Output.CreateSecret(ImmutableDictionary.Create<string, object>());
                _secureSettings = Output.All(value, emptySecret).Apply(v => v[0]);
            }
        }

        /// <summary>
        /// Whether to send reminders for triggered alerts. Defaults to `false`.
        /// </summary>
        [Input("sendReminder")]
        public Input<bool>? SendReminder { get; set; }

        [Input("settings")]
        private InputMap<object>? _settings;

        /// <summary>
        /// Additional settings, for full reference see [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/developers/http_api/alerting_notification_channels/).
        /// </summary>
        public InputMap<object> Settings
        {
            get => _settings ?? (_settings = new InputMap<object>());
            set => _settings = value;
        }

        /// <summary>
        /// The type of the alert notification channel.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        /// <summary>
        /// Unique identifier. If unset, this will be automatically generated.
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        public AlertNotificationArgs()
        {
        }
        public static new AlertNotificationArgs Empty => new AlertNotificationArgs();
    }

    public sealed class AlertNotificationState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether to disable sending resolve messages. Defaults to `false`.
        /// </summary>
        [Input("disableResolveMessage")]
        public Input<bool>? DisableResolveMessage { get; set; }

        /// <summary>
        /// Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.
        /// </summary>
        [Input("frequency")]
        public Input<string>? Frequency { get; set; }

        /// <summary>
        /// Is this the default channel for all your alerts. Defaults to `false`.
        /// </summary>
        [Input("isDefault")]
        public Input<bool>? IsDefault { get; set; }

        /// <summary>
        /// The name of the alert notification channel.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("secureSettings")]
        private InputMap<object>? _secureSettings;

        /// <summary>
        /// Additional secure settings, for full reference lookup [Grafana Supported Settings documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings).
        /// </summary>
        public InputMap<object> SecureSettings
        {
            get => _secureSettings ?? (_secureSettings = new InputMap<object>());
            set
            {
                var emptySecret = Output.CreateSecret(ImmutableDictionary.Create<string, object>());
                _secureSettings = Output.All(value, emptySecret).Apply(v => v[0]);
            }
        }

        /// <summary>
        /// Whether to send reminders for triggered alerts. Defaults to `false`.
        /// </summary>
        [Input("sendReminder")]
        public Input<bool>? SendReminder { get; set; }

        [Input("settings")]
        private InputMap<object>? _settings;

        /// <summary>
        /// Additional settings, for full reference see [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/developers/http_api/alerting_notification_channels/).
        /// </summary>
        public InputMap<object> Settings
        {
            get => _settings ?? (_settings = new InputMap<object>());
            set => _settings = value;
        }

        /// <summary>
        /// The type of the alert notification channel.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// Unique identifier. If unset, this will be automatically generated.
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        public AlertNotificationState()
        {
        }
        public static new AlertNotificationState Empty => new AlertNotificationState();
    }
}
