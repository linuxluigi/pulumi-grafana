// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/** @deprecated grafana.index/getcloudips.getCloudIps has been deprecated in favor of grafana.cloud/getips.getIps */
export function getCloudIps(opts?: pulumi.InvokeOptions): Promise<GetCloudIpsResult> {
    pulumi.log.warn("getCloudIps is deprecated: grafana.index/getcloudips.getCloudIps has been deprecated in favor of grafana.cloud/getips.getIps")

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getCloudIps:getCloudIps", {
    }, opts);
}

/**
 * A collection of values returned by getCloudIps.
 */
export interface GetCloudIpsResult {
    readonly hostedAlerts: string[];
    readonly hostedGrafanas: string[];
    readonly hostedLogs: string[];
    readonly hostedMetrics: string[];
    readonly hostedTraces: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
/** @deprecated grafana.index/getcloudips.getCloudIps has been deprecated in favor of grafana.cloud/getips.getIps */
export function getCloudIpsOutput(opts?: pulumi.InvokeOptions): pulumi.Output<GetCloudIpsResult> {
    return pulumi.output(getCloudIps(opts))
}
