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

    public sealed class DataSourcePermissionPermissionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the basic role to manage permissions for. Options: `Viewer`, `Editor` or `Admin`. Can only be set from Grafana v9.2.3+. Defaults to ``.
        /// </summary>
        [Input("builtInRole")]
        public Input<string>? BuiltInRole { get; set; }

        /// <summary>
        /// Permission to associate with item. Options: `Query` or `Edit` (`Edit` can only be used with Grafana v9.2.3+).
        /// </summary>
        [Input("permission", required: true)]
        public Input<string> Permission { get; set; } = null!;

        /// <summary>
        /// ID of the team to manage permissions for. Defaults to `0`.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        /// <summary>
        /// ID of the user to manage permissions for. Defaults to `0`.
        /// </summary>
        [Input("userId")]
        public Input<int>? UserId { get; set; }

        public DataSourcePermissionPermissionArgs()
        {
        }
        public static new DataSourcePermissionPermissionArgs Empty => new DataSourcePermissionPermissionArgs();
    }
}
