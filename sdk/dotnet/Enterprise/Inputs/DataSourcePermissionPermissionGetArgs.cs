// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Enterprise.Inputs
{

    public sealed class DataSourcePermissionPermissionGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the basic role to manage permissions for. Options: `Viewer`, `Editor` or `Admin`.
        /// </summary>
        [Input("builtInRole")]
        public Input<string>? BuiltInRole { get; set; }

        /// <summary>
        /// Permission to associate with item. Options: `Query`, `Edit` or `Admin` (`Admin` can only be used with Grafana v10.3.0+).
        /// </summary>
        [Input("permission", required: true)]
        public Input<string> Permission { get; set; } = null!;

        /// <summary>
        /// ID of the team to manage permissions for. Defaults to `0`.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        /// <summary>
        /// ID of the user or service account to manage permissions for. Defaults to `0`.
        /// </summary>
        [Input("userId")]
        public Input<string>? UserId { get; set; }

        public DataSourcePermissionPermissionGetArgs()
        {
        }
        public static new DataSourcePermissionPermissionGetArgs Empty => new DataSourcePermissionPermissionGetArgs();
    }
}
