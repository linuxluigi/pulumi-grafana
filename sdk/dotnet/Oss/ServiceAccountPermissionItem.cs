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
    /// Manages a single permission item for a service account. Conflicts with the "grafana.oss.ServiceAccountPermission" resource which manages the entire set of permissions for a service account.
    /// * [Official documentation](https://grafana.com/docs/grafana/latest/administration/service-accounts/#manage-users-and-teams-permissions-for-a-service-account-in-grafana)
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var test = new Grafana.Oss.ServiceAccount("test", new()
    ///     {
    ///         Role = "Editor",
    ///         IsDisabled = false,
    ///     });
    /// 
    ///     var team = new Grafana.Oss.Team("team");
    /// 
    ///     var user = new Grafana.Oss.User("user", new()
    ///     {
    ///         Email = "user.name@example.com",
    ///         Login = "user.name",
    ///         Password = "my-password",
    ///     });
    /// 
    ///     var onTeam = new Grafana.Oss.ServiceAccountPermissionItem("onTeam", new()
    ///     {
    ///         ServiceAccountId = test.Id,
    ///         Team = team.Id,
    ///         Permission = "Admin",
    ///     });
    /// 
    ///     var onUser = new Grafana.Oss.ServiceAccountPermissionItem("onUser", new()
    ///     {
    ///         ServiceAccountId = test.Id,
    ///         User = user.Id,
    ///         Permission = "Admin",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    /// $ pulumi import grafana:oss/serviceAccountPermissionItem:ServiceAccountPermissionItem name "{{ serviceAccountID }}:{{ type (role, team, or user) }}:{{ identifier }}"
    /// ```
    /// 
    /// ```sh
    /// $ pulumi import grafana:oss/serviceAccountPermissionItem:ServiceAccountPermissionItem name "{{ orgID }}:{{ serviceAccountID }}:{{ type (role, team, or user) }}:{{ identifier }}"
    /// ```
    /// </summary>
    [GrafanaResourceType("grafana:oss/serviceAccountPermissionItem:ServiceAccountPermissionItem")]
    public partial class ServiceAccountPermissionItem : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Output("orgId")]
        public Output<string> OrgId { get; private set; } = null!;

        /// <summary>
        /// the permission to be assigned
        /// </summary>
        [Output("permission")]
        public Output<string> Permission { get; private set; } = null!;

        /// <summary>
        /// The ID of the service account.
        /// </summary>
        [Output("serviceAccountId")]
        public Output<string> ServiceAccountId { get; private set; } = null!;

        /// <summary>
        /// the team onto which the permission is to be assigned
        /// </summary>
        [Output("team")]
        public Output<string?> Team { get; private set; } = null!;

        /// <summary>
        /// the user or service account onto which the permission is to be assigned
        /// </summary>
        [Output("user")]
        public Output<string?> User { get; private set; } = null!;


        /// <summary>
        /// Create a ServiceAccountPermissionItem resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServiceAccountPermissionItem(string name, ServiceAccountPermissionItemArgs args, CustomResourceOptions? options = null)
            : base("grafana:oss/serviceAccountPermissionItem:ServiceAccountPermissionItem", name, args ?? new ServiceAccountPermissionItemArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ServiceAccountPermissionItem(string name, Input<string> id, ServiceAccountPermissionItemState? state = null, CustomResourceOptions? options = null)
            : base("grafana:oss/serviceAccountPermissionItem:ServiceAccountPermissionItem", name, state, MakeResourceOptions(options, id))
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
                    new global::Pulumi.Alias { Type = "grafana:index/serviceAccountPermissionItem:ServiceAccountPermissionItem" },
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ServiceAccountPermissionItem resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServiceAccountPermissionItem Get(string name, Input<string> id, ServiceAccountPermissionItemState? state = null, CustomResourceOptions? options = null)
        {
            return new ServiceAccountPermissionItem(name, id, state, options);
        }
    }

    public sealed class ServiceAccountPermissionItemArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        /// <summary>
        /// the permission to be assigned
        /// </summary>
        [Input("permission", required: true)]
        public Input<string> Permission { get; set; } = null!;

        /// <summary>
        /// The ID of the service account.
        /// </summary>
        [Input("serviceAccountId", required: true)]
        public Input<string> ServiceAccountId { get; set; } = null!;

        /// <summary>
        /// the team onto which the permission is to be assigned
        /// </summary>
        [Input("team")]
        public Input<string>? Team { get; set; }

        /// <summary>
        /// the user or service account onto which the permission is to be assigned
        /// </summary>
        [Input("user")]
        public Input<string>? User { get; set; }

        public ServiceAccountPermissionItemArgs()
        {
        }
        public static new ServiceAccountPermissionItemArgs Empty => new ServiceAccountPermissionItemArgs();
    }

    public sealed class ServiceAccountPermissionItemState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        /// <summary>
        /// the permission to be assigned
        /// </summary>
        [Input("permission")]
        public Input<string>? Permission { get; set; }

        /// <summary>
        /// The ID of the service account.
        /// </summary>
        [Input("serviceAccountId")]
        public Input<string>? ServiceAccountId { get; set; }

        /// <summary>
        /// the team onto which the permission is to be assigned
        /// </summary>
        [Input("team")]
        public Input<string>? Team { get; set; }

        /// <summary>
        /// the user or service account onto which the permission is to be assigned
        /// </summary>
        [Input("user")]
        public Input<string>? User { get; set; }

        public ServiceAccountPermissionItemState()
        {
        }
        public static new ServiceAccountPermissionItemState Empty => new ServiceAccountPermissionItemState();
    }
}
