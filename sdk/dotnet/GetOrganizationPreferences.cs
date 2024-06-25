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
    [Obsolete(@"grafana.index/getorganizationpreferences.getOrganizationPreferences has been deprecated in favor of grafana.oss/getorganizationpreferences.getOrganizationPreferences")]
    public static class GetOrganizationPreferences
    {
        public static Task<GetOrganizationPreferencesResult> InvokeAsync(GetOrganizationPreferencesArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOrganizationPreferencesResult>("grafana:index/getOrganizationPreferences:getOrganizationPreferences", args ?? new GetOrganizationPreferencesArgs(), options.WithDefaults());

        public static Output<GetOrganizationPreferencesResult> Invoke(GetOrganizationPreferencesInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOrganizationPreferencesResult>("grafana:index/getOrganizationPreferences:getOrganizationPreferences", args ?? new GetOrganizationPreferencesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOrganizationPreferencesArgs : global::Pulumi.InvokeArgs
    {
        [Input("orgId")]
        public string? OrgId { get; set; }

        public GetOrganizationPreferencesArgs()
        {
        }
        public static new GetOrganizationPreferencesArgs Empty => new GetOrganizationPreferencesArgs();
    }

    public sealed class GetOrganizationPreferencesInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("orgId")]
        public Input<string>? OrgId { get; set; }

        public GetOrganizationPreferencesInvokeArgs()
        {
        }
        public static new GetOrganizationPreferencesInvokeArgs Empty => new GetOrganizationPreferencesInvokeArgs();
    }


    [OutputType]
    public sealed class GetOrganizationPreferencesResult
    {
        public readonly string HomeDashboardUid;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string? OrgId;
        public readonly string Theme;
        public readonly string Timezone;
        public readonly string WeekStart;

        [OutputConstructor]
        private GetOrganizationPreferencesResult(
            string homeDashboardUid,

            string id,

            string? orgId,

            string theme,

            string timezone,

            string weekStart)
        {
            HomeDashboardUid = homeDashboardUid;
            Id = id;
            OrgId = orgId;
            Theme = theme;
            Timezone = timezone;
            WeekStart = weekStart;
        }
    }
}
