// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * * [Official documentation](https://grafana.com/docs/grafana/latest/administration/organization-management/)
 * * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/preferences/#get-current-org-prefs)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumi/grafana";
 *
 * const test = grafana.getOrganizationPreferences({});
 * ```
 */
export function getOrganizationPreferences(opts?: pulumi.InvokeOptions): Promise<GetOrganizationPreferencesResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getOrganizationPreferences:getOrganizationPreferences", {
    }, opts);
}

/**
 * A collection of values returned by getOrganizationPreferences.
 */
export interface GetOrganizationPreferencesResult {
    /**
     * The Organization home dashboard ID.
     */
    readonly homeDashboardId: number;
    /**
     * The Organization home dashboard UID. This is only available in Grafana 9.0+.
     */
    readonly homeDashboardUid: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    readonly orgId: string;
    /**
     * The Organization theme. Available values are `light`, `dark`, or an empty string for the default.
     */
    readonly theme: string;
    /**
     * The Organization timezone. Available values are `utc`, `browser`, or an empty string for the default.
     */
    readonly timezone: string;
    /**
     * The Organization week start.
     */
    readonly weekStart: string;
}
/**
 * * [Official documentation](https://grafana.com/docs/grafana/latest/administration/organization-management/)
 * * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/preferences/#get-current-org-prefs)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumi/grafana";
 *
 * const test = grafana.getOrganizationPreferences({});
 * ```
 */
export function getOrganizationPreferencesOutput(opts?: pulumi.InvokeOptions): pulumi.Output<GetOrganizationPreferencesResult> {
    return pulumi.output(getOrganizationPreferences(opts))
}
