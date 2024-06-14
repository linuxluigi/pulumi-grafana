// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/** @deprecated grafana.index/getfolder.getFolder has been deprecated in favor of grafana.oss/getfolder.getFolder */
export function getFolder(args: GetFolderArgs, opts?: pulumi.InvokeOptions): Promise<GetFolderResult> {
    pulumi.log.warn("getFolder is deprecated: grafana.index/getfolder.getFolder has been deprecated in favor of grafana.oss/getfolder.getFolder")

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getFolder:getFolder", {
        "orgId": args.orgId,
        "title": args.title,
    }, opts);
}

/**
 * A collection of arguments for invoking getFolder.
 */
export interface GetFolderArgs {
    orgId?: string;
    title: string;
}

/**
 * A collection of values returned by getFolder.
 */
export interface GetFolderResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly orgId?: string;
    readonly parentFolderUid: string;
    readonly title: string;
    readonly uid: string;
    readonly url: string;
}
/** @deprecated grafana.index/getfolder.getFolder has been deprecated in favor of grafana.oss/getfolder.getFolder */
export function getFolderOutput(args: GetFolderOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetFolderResult> {
    return pulumi.output(args).apply((a: any) => getFolder(a, opts))
}

/**
 * A collection of arguments for invoking getFolder.
 */
export interface GetFolderOutputArgs {
    orgId?: pulumi.Input<string>;
    title: pulumi.Input<string>;
}
