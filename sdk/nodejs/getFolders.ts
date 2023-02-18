// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/manage-dashboards/)
 * * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/folder/)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@lbrlabs/pulumi-grafana";
 * import * as grafana from "@pulumi/grafana";
 *
 * const testA = new grafana.Folder("testA", {
 *     title: "test-folder-a",
 *     uid: "test-ds-folder-uid-a",
 * });
 * const testB = new grafana.Folder("testB", {
 *     title: "test-folder-b",
 *     uid: "test-ds-folder-uid-b",
 * });
 * const test = grafana.getFolders({});
 * ```
 */
export function getFolders(opts?: pulumi.InvokeOptions): Promise<GetFoldersResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getFolders:getFolders", {
    }, opts);
}

/**
 * A collection of values returned by getFolders.
 */
export interface GetFoldersResult {
    /**
     * The Grafana instance's folders.
     */
    readonly folders: outputs.GetFoldersFolder[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
