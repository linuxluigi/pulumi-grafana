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
    public sealed class ServiceAccountPermissionPermission
    {
        /// <summary>
        /// Permission to associate with item. Must be one of `View`, `Edit`, or `Admin`.
        /// </summary>
        public readonly string Permission;
        /// <summary>
        /// ID of the team to manage permissions for. Defaults to `0`.
        /// </summary>
        public readonly string? TeamId;
        /// <summary>
        /// ID of the user or service account to manage permissions for. Defaults to `0`.
        /// </summary>
        public readonly string? UserId;

        [OutputConstructor]
        private ServiceAccountPermissionPermission(
            string permission,

            string? teamId,

            string? userId)
        {
            Permission = permission;
            TeamId = teamId;
            UserId = userId;
        }
    }
}
