// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana
{
    [Obsolete(@"grafana.index/serviceaccountpermission.ServiceAccountPermission has been deprecated in favor of grafana.oss/serviceaccountpermission.ServiceAccountPermission")]
    [GrafanaResourceType("grafana:index/serviceAccountPermission:ServiceAccountPermission")]
    public partial class ServiceAccountPermission : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Output("orgId")]
        public Output<string?> OrgId { get; private set; } = null!;

        /// <summary>
        /// The permission items to add/update. Items that are omitted from the list will be removed.
        /// </summary>
        [Output("permissions")]
        public Output<ImmutableArray<Outputs.ServiceAccountPermissionPermission>> Permissions { get; private set; } = null!;

        /// <summary>
        /// The id of the service account.
        /// </summary>
        [Output("serviceAccountId")]
        public Output<string> ServiceAccountId { get; private set; } = null!;


        /// <summary>
        /// Create a ServiceAccountPermission resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServiceAccountPermission(string name, ServiceAccountPermissionArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/serviceAccountPermission:ServiceAccountPermission", name, args ?? new ServiceAccountPermissionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ServiceAccountPermission(string name, Input<string> id, ServiceAccountPermissionState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/serviceAccountPermission:ServiceAccountPermission", name, state, MakeResourceOptions(options, id))
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
                    new global::Pulumi.Alias { Type = "grafana:index/serviceAccountPermission:ServiceAccountPermission" },
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ServiceAccountPermission resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServiceAccountPermission Get(string name, Input<string> id, ServiceAccountPermissionState? state = null, CustomResourceOptions? options = null)
        {
            return new ServiceAccountPermission(name, id, state, options);
        }
    }

    public sealed class ServiceAccountPermissionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        [Input("permissions")]
        private InputList<Inputs.ServiceAccountPermissionPermissionArgs>? _permissions;

        /// <summary>
        /// The permission items to add/update. Items that are omitted from the list will be removed.
        /// </summary>
        public InputList<Inputs.ServiceAccountPermissionPermissionArgs> Permissions
        {
            get => _permissions ?? (_permissions = new InputList<Inputs.ServiceAccountPermissionPermissionArgs>());
            set => _permissions = value;
        }

        /// <summary>
        /// The id of the service account.
        /// </summary>
        [Input("serviceAccountId", required: true)]
        public Input<string> ServiceAccountId { get; set; } = null!;

        public ServiceAccountPermissionArgs()
        {
        }
        public static new ServiceAccountPermissionArgs Empty => new ServiceAccountPermissionArgs();
    }

    public sealed class ServiceAccountPermissionState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Organization ID. If not set, the Org ID defined in the provider block will be used.
        /// </summary>
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        [Input("permissions")]
        private InputList<Inputs.ServiceAccountPermissionPermissionGetArgs>? _permissions;

        /// <summary>
        /// The permission items to add/update. Items that are omitted from the list will be removed.
        /// </summary>
        public InputList<Inputs.ServiceAccountPermissionPermissionGetArgs> Permissions
        {
            get => _permissions ?? (_permissions = new InputList<Inputs.ServiceAccountPermissionPermissionGetArgs>());
            set => _permissions = value;
        }

        /// <summary>
        /// The id of the service account.
        /// </summary>
        [Input("serviceAccountId")]
        public Input<string>? ServiceAccountId { get; set; }

        public ServiceAccountPermissionState()
        {
        }
        public static new ServiceAccountPermissionState Empty => new ServiceAccountPermissionState();
    }
}
