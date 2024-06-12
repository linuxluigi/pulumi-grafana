// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/users/)
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumi/grafana";
 *
 * const alex = grafana.getOncallUser({
 *     username: "alex",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getOncallUser(args: GetOncallUserArgs, opts?: pulumi.InvokeOptions): Promise<GetOncallUserResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("grafana:index/getOncallUser:getOncallUser", {
        "username": args.username,
    }, opts);
}

/**
 * A collection of arguments for invoking getOncallUser.
 */
export interface GetOncallUserArgs {
    /**
     * The username of the user.
     */
    username: string;
}

/**
 * A collection of values returned by getOncallUser.
 */
export interface GetOncallUserResult {
    /**
     * The email of the user.
     */
    readonly email: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The role of the user.
     */
    readonly role: string;
    /**
     * The username of the user.
     */
    readonly username: string;
}
/**
 * * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/users/)
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumi/grafana";
 *
 * const alex = grafana.getOncallUser({
 *     username: "alex",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getOncallUserOutput(args: GetOncallUserOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetOncallUserResult> {
    return pulumi.output(args).apply((a: any) => getOncallUser(a, opts))
}

/**
 * A collection of arguments for invoking getOncallUser.
 */
export interface GetOncallUserOutputArgs {
    /**
     * The username of the user.
     */
    username: pulumi.Input<string>;
}
