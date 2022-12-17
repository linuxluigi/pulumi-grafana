// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Datasource for retrieving all dashboards. Specify list of folder IDs to search in for dashboards.
 *
 * * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/)
 * * [Folder/Dashboard Search HTTP API](https://grafana.com/docs/grafana/latest/http_api/folder_dashboard_search/)
 * * [Dashboard HTTP API](https://grafana.com/docs/grafana/latest/http_api/dashboard/)
 */
export function getDashboards(args?: GetDashboardsArgs, opts?: pulumi.InvokeOptions): Promise<GetDashboardsResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getDashboards:getDashboards", {
        "folderIds": args.folderIds,
        "limit": args.limit,
        "tags": args.tags,
    }, opts);
}

/**
 * A collection of arguments for invoking getDashboards.
 */
export interface GetDashboardsArgs {
    /**
     * Numerical IDs of Grafana folders containing dashboards. Specify to filter for dashboards by folder (eg. `[0]` for General folder), or leave blank to get all dashboards in all folders.
     */
    folderIds?: number[];
    /**
     * Maximum number of dashboard search results to return. Defaults to `5000`.
     */
    limit?: number;
    /**
     * List of string Grafana dashboard tags to search for, eg. `["prod"]`. Used only as search input, i.e., attribute value will remain unchanged.
     */
    tags?: string[];
}

/**
 * A collection of values returned by getDashboards.
 */
export interface GetDashboardsResult {
    readonly dashboards: outputs.GetDashboardsDashboard[];
    /**
     * Numerical IDs of Grafana folders containing dashboards. Specify to filter for dashboards by folder (eg. `[0]` for General folder), or leave blank to get all dashboards in all folders.
     */
    readonly folderIds?: number[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Maximum number of dashboard search results to return. Defaults to `5000`.
     */
    readonly limit?: number;
    /**
     * List of string Grafana dashboard tags to search for, eg. `["prod"]`. Used only as search input, i.e., attribute value will remain unchanged.
     */
    readonly tags?: string[];
}
/**
 * Datasource for retrieving all dashboards. Specify list of folder IDs to search in for dashboards.
 *
 * * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/)
 * * [Folder/Dashboard Search HTTP API](https://grafana.com/docs/grafana/latest/http_api/folder_dashboard_search/)
 * * [Dashboard HTTP API](https://grafana.com/docs/grafana/latest/http_api/dashboard/)
 */
export function getDashboardsOutput(args?: GetDashboardsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDashboardsResult> {
    return pulumi.output(args).apply((a: any) => getDashboards(a, opts))
}

/**
 * A collection of arguments for invoking getDashboards.
 */
export interface GetDashboardsOutputArgs {
    /**
     * Numerical IDs of Grafana folders containing dashboards. Specify to filter for dashboards by folder (eg. `[0]` for General folder), or leave blank to get all dashboards in all folders.
     */
    folderIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Maximum number of dashboard search results to return. Defaults to `5000`.
     */
    limit?: pulumi.Input<number>;
    /**
     * List of string Grafana dashboard tags to search for, eg. `["prod"]`. Used only as search input, i.e., attribute value will remain unchanged.
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
}
