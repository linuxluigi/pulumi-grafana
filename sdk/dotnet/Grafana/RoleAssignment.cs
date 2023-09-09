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
    /// **Note:** This resource is available only with Grafana Enterprise 9.2+.
    /// * [Official documentation](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/access-control/)
    /// * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/access_control/)
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Lbrlabs.PulumiPackage.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var testRole = new Grafana.Role("testRole", new()
    ///     {
    ///         Uid = "testrole",
    ///         Version = 1,
    ///         Global = true,
    ///         Permissions = new[]
    ///         {
    ///             new Grafana.Inputs.RolePermissionArgs
    ///             {
    ///                 Action = "org.users:add",
    ///                 Scope = "users:*",
    ///             },
    ///         },
    ///     });
    /// 
    ///     var testTeam = new Grafana.Team("testTeam");
    /// 
    ///     var testUser = new Grafana.User("testUser", new()
    ///     {
    ///         Email = "terraform_user@test.com",
    ///         Login = "terraform_user@test.com",
    ///         Password = "password",
    ///     });
    /// 
    ///     var testSa = new Grafana.ServiceAccount("testSa", new()
    ///     {
    ///         Role = "Viewer",
    ///     });
    /// 
    ///     var test = new Grafana.RoleAssignment("test", new()
    ///     {
    ///         RoleUid = testRole.Uid,
    ///         Users = new[]
    ///         {
    ///             testUser.Id,
    ///         },
    ///         Teams = new[]
    ///         {
    ///             testTeam.Id,
    ///         },
    ///         ServiceAccounts = new[]
    ///         {
    ///             testSa.Id,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [GrafanaResourceType("grafana:index/roleAssignment:RoleAssignment")]
    public partial class RoleAssignment : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Grafana RBAC role UID.
        /// </summary>
        [Output("roleUid")]
        public Output<string> RoleUid { get; private set; } = null!;

        /// <summary>
        /// IDs of service accounts that the role should be assigned to.
        /// </summary>
        [Output("serviceAccounts")]
        public Output<ImmutableArray<int>> ServiceAccounts { get; private set; } = null!;

        /// <summary>
        /// IDs of teams that the role should be assigned to.
        /// </summary>
        [Output("teams")]
        public Output<ImmutableArray<string>> Teams { get; private set; } = null!;

        /// <summary>
        /// IDs of users that the role should be assigned to.
        /// </summary>
        [Output("users")]
        public Output<ImmutableArray<int>> Users { get; private set; } = null!;


        /// <summary>
        /// Create a RoleAssignment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RoleAssignment(string name, RoleAssignmentArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/roleAssignment:RoleAssignment", name, args ?? new RoleAssignmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RoleAssignment(string name, Input<string> id, RoleAssignmentState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/roleAssignment:RoleAssignment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/lbrlabs",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing RoleAssignment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RoleAssignment Get(string name, Input<string> id, RoleAssignmentState? state = null, CustomResourceOptions? options = null)
        {
            return new RoleAssignment(name, id, state, options);
        }
    }

    public sealed class RoleAssignmentArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Grafana RBAC role UID.
        /// </summary>
        [Input("roleUid", required: true)]
        public Input<string> RoleUid { get; set; } = null!;

        [Input("serviceAccounts")]
        private InputList<int>? _serviceAccounts;

        /// <summary>
        /// IDs of service accounts that the role should be assigned to.
        /// </summary>
        public InputList<int> ServiceAccounts
        {
            get => _serviceAccounts ?? (_serviceAccounts = new InputList<int>());
            set => _serviceAccounts = value;
        }

        [Input("teams")]
        private InputList<string>? _teams;

        /// <summary>
        /// IDs of teams that the role should be assigned to.
        /// </summary>
        public InputList<string> Teams
        {
            get => _teams ?? (_teams = new InputList<string>());
            set => _teams = value;
        }

        [Input("users")]
        private InputList<int>? _users;

        /// <summary>
        /// IDs of users that the role should be assigned to.
        /// </summary>
        public InputList<int> Users
        {
            get => _users ?? (_users = new InputList<int>());
            set => _users = value;
        }

        public RoleAssignmentArgs()
        {
        }
        public static new RoleAssignmentArgs Empty => new RoleAssignmentArgs();
    }

    public sealed class RoleAssignmentState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Grafana RBAC role UID.
        /// </summary>
        [Input("roleUid")]
        public Input<string>? RoleUid { get; set; }

        [Input("serviceAccounts")]
        private InputList<int>? _serviceAccounts;

        /// <summary>
        /// IDs of service accounts that the role should be assigned to.
        /// </summary>
        public InputList<int> ServiceAccounts
        {
            get => _serviceAccounts ?? (_serviceAccounts = new InputList<int>());
            set => _serviceAccounts = value;
        }

        [Input("teams")]
        private InputList<string>? _teams;

        /// <summary>
        /// IDs of teams that the role should be assigned to.
        /// </summary>
        public InputList<string> Teams
        {
            get => _teams ?? (_teams = new InputList<string>());
            set => _teams = value;
        }

        [Input("users")]
        private InputList<int>? _users;

        /// <summary>
        /// IDs of users that the role should be assigned to.
        /// </summary>
        public InputList<int> Users
        {
            get => _users ?? (_users = new InputList<int>());
            set => _users = value;
        }

        public RoleAssignmentState()
        {
        }
        public static new RoleAssignmentState Empty => new RoleAssignmentState();
    }
}
