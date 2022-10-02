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
    /// * [Official documentation](https://grafana.com/docs/grafana/latest/administration/manage-users-and-permissions/manage-server-users/)
    /// * [HTTP API](https://grafana.com/docs/grafana/latest/http_api/user/)
    /// 
    /// This resource uses Grafana's admin APIs for creating and updating users which
    /// does not currently work with API Tokens. You must use basic auth.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using Pulumi;
    /// using Grafana = Lbrlabs.PulumiPackage.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var staff = new Grafana.User("staff", new()
    ///     {
    ///         Email = "staff.name@example.com",
    ///         IsAdmin = false,
    ///         Login = "staff",
    ///         Password = "my-password",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// ```sh
    ///  $ pulumi import grafana:index/user:User user_name {{user_id}}
    /// ```
    /// </summary>
    [GrafanaResourceType("grafana:index/user:User")]
    public partial class User : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The email address of the Grafana user.
        /// </summary>
        [Output("email")]
        public Output<string> Email { get; private set; } = null!;

        /// <summary>
        /// Whether to make user an admin. Defaults to `false`.
        /// </summary>
        [Output("isAdmin")]
        public Output<bool?> IsAdmin { get; private set; } = null!;

        /// <summary>
        /// The username for the Grafana user.
        /// </summary>
        [Output("login")]
        public Output<string?> Login { get; private set; } = null!;

        /// <summary>
        /// The display name for the Grafana user.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The password for the Grafana user.
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        /// <summary>
        /// The numerical ID of the Grafana user.
        /// </summary>
        [Output("userId")]
        public Output<int> UserId { get; private set; } = null!;


        /// <summary>
        /// Create a User resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public User(string name, UserArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/user:User", name, args ?? new UserArgs(), MakeResourceOptions(options, ""))
        {
        }

        private User(string name, Input<string> id, UserState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/user:User", name, state, MakeResourceOptions(options, id))
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
                    "password",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing User resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static User Get(string name, Input<string> id, UserState? state = null, CustomResourceOptions? options = null)
        {
            return new User(name, id, state, options);
        }
    }

    public sealed class UserArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The email address of the Grafana user.
        /// </summary>
        [Input("email", required: true)]
        public Input<string> Email { get; set; } = null!;

        /// <summary>
        /// Whether to make user an admin. Defaults to `false`.
        /// </summary>
        [Input("isAdmin")]
        public Input<bool>? IsAdmin { get; set; }

        /// <summary>
        /// The username for the Grafana user.
        /// </summary>
        [Input("login")]
        public Input<string>? Login { get; set; }

        /// <summary>
        /// The display name for the Grafana user.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("password", required: true)]
        private Input<string>? _password;

        /// <summary>
        /// The password for the Grafana user.
        /// </summary>
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public UserArgs()
        {
        }
        public static new UserArgs Empty => new UserArgs();
    }

    public sealed class UserState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The email address of the Grafana user.
        /// </summary>
        [Input("email")]
        public Input<string>? Email { get; set; }

        /// <summary>
        /// Whether to make user an admin. Defaults to `false`.
        /// </summary>
        [Input("isAdmin")]
        public Input<bool>? IsAdmin { get; set; }

        /// <summary>
        /// The username for the Grafana user.
        /// </summary>
        [Input("login")]
        public Input<string>? Login { get; set; }

        /// <summary>
        /// The display name for the Grafana user.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("password")]
        private Input<string>? _password;

        /// <summary>
        /// The password for the Grafana user.
        /// </summary>
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The numerical ID of the Grafana user.
        /// </summary>
        [Input("userId")]
        public Input<int>? UserId { get; set; }

        public UserState()
        {
        }
        public static new UserState Empty => new UserState();
    }
}
