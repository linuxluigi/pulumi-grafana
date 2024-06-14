// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Oss
{
    /// <summary>
    /// Manages Grafana dashboards.
    /// 
    /// * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/)
    /// * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/dashboard/)
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using System.Text.Json;
    /// using Pulumi;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var testFolder = new Grafana.Oss.Folder("testFolder", new()
    ///     {
    ///         Title = "My Folder",
    ///         Uid = "my-folder-uid",
    ///     });
    /// 
    ///     var testDashboard = new Grafana.Oss.Dashboard("testDashboard", new()
    ///     {
    ///         Folder = testFolder.Uid,
    ///         ConfigJson = JsonSerializer.Serialize(new Dictionary&lt;string, object?&gt;
    ///         {
    ///             ["title"] = "My Dashboard",
    ///             ["uid"] = "my-dashboard-uid",
    ///         }),
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    /// $ pulumi import grafana:oss/dashboard:Dashboard name "{{ uid }}"
    /// ```
    /// 
    /// ```sh
    /// $ pulumi import grafana:oss/dashboard:Dashboard name "{{ orgID }}:{{ uid }}"
    /// ```
    /// </summary>
    [GrafanaResourceType("grafana:oss/dashboard:Dashboard")]
    public partial class Dashboard : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The complete dashboard model JSON.
        /// </summary>
        [Output("configJson")]
        public Output<string> ConfigJson { get; private set; } = null!;

        /// <summary>
        /// The numeric ID of the dashboard computed by Grafana.
        /// </summary>
        [Output("dashboardId")]
        public Output<int> DashboardId { get; private set; } = null!;

        /// <summary>
        /// The id or UID of the folder to save the dashboard in.
        /// </summary>
        [Output("folder")]
        public Output<string?> Folder { get; private set; } = null!;

        /// <summary>
        /// Set a commit message for the version history.
        /// </summary>
        [Output("message")]
        public Output<string?> Message { get; private set; } = null!;

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Output("orgId")]
        public Output<string?> OrgId { get; private set; } = null!;

        /// <summary>
        /// Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid.
        /// </summary>
        [Output("overwrite")]
        public Output<bool?> Overwrite { get; private set; } = null!;

        /// <summary>
        /// The unique identifier of a dashboard. This is used to construct its URL. It's automatically generated if not provided when creating a dashboard. The uid allows having consistent URLs for accessing dashboards and when syncing dashboards between multiple Grafana installs.
        /// </summary>
        [Output("uid")]
        public Output<string> Uid { get; private set; } = null!;

        /// <summary>
        /// The full URL of the dashboard.
        /// </summary>
        [Output("url")]
        public Output<string> Url { get; private set; } = null!;

        /// <summary>
        /// Whenever you save a version of your dashboard, a copy of that version is saved so that previous versions of your dashboard are not lost.
        /// </summary>
        [Output("version")]
        public Output<int> Version { get; private set; } = null!;


        /// <summary>
        /// Create a Dashboard resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Dashboard(string name, DashboardArgs args, CustomResourceOptions? options = null)
            : base("grafana:oss/dashboard:Dashboard", name, args ?? new DashboardArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Dashboard(string name, Input<string> id, DashboardState? state = null, CustomResourceOptions? options = null)
            : base("grafana:oss/dashboard:Dashboard", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
                Aliases =
                {
                    new global::Pulumi.Alias { Type = "grafana:index/dashboard:Dashboard" },
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Dashboard resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Dashboard Get(string name, Input<string> id, DashboardState? state = null, CustomResourceOptions? options = null)
        {
            return new Dashboard(name, id, state, options);
        }
    }

    public sealed class DashboardArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The complete dashboard model JSON.
        /// </summary>
        [Input("configJson", required: true)]
        public Input<string> ConfigJson { get; set; } = null!;

        /// <summary>
        /// The id or UID of the folder to save the dashboard in.
        /// </summary>
        [Input("folder")]
        public Input<string>? Folder { get; set; }

        /// <summary>
        /// Set a commit message for the version history.
        /// </summary>
        [Input("message")]
        public Input<string>? Message { get; set; }

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        /// <summary>
        /// Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid.
        /// </summary>
        [Input("overwrite")]
        public Input<bool>? Overwrite { get; set; }

        public DashboardArgs()
        {
        }
        public static new DashboardArgs Empty => new DashboardArgs();
    }

    public sealed class DashboardState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The complete dashboard model JSON.
        /// </summary>
        [Input("configJson")]
        public Input<string>? ConfigJson { get; set; }

        /// <summary>
        /// The numeric ID of the dashboard computed by Grafana.
        /// </summary>
        [Input("dashboardId")]
        public Input<int>? DashboardId { get; set; }

        /// <summary>
        /// The id or UID of the folder to save the dashboard in.
        /// </summary>
        [Input("folder")]
        public Input<string>? Folder { get; set; }

        /// <summary>
        /// Set a commit message for the version history.
        /// </summary>
        [Input("message")]
        public Input<string>? Message { get; set; }

        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        /// <summary>
        /// Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid.
        /// </summary>
        [Input("overwrite")]
        public Input<bool>? Overwrite { get; set; }

        /// <summary>
        /// The unique identifier of a dashboard. This is used to construct its URL. It's automatically generated if not provided when creating a dashboard. The uid allows having consistent URLs for accessing dashboards and when syncing dashboards between multiple Grafana installs.
        /// </summary>
        [Input("uid")]
        public Input<string>? Uid { get; set; }

        /// <summary>
        /// The full URL of the dashboard.
        /// </summary>
        [Input("url")]
        public Input<string>? Url { get; set; }

        /// <summary>
        /// Whenever you save a version of your dashboard, a copy of that version is saved so that previous versions of your dashboard are not lost.
        /// </summary>
        [Input("version")]
        public Input<int>? Version { get; set; }

        public DashboardState()
        {
        }
        public static new DashboardState Empty => new DashboardState();
    }
}
