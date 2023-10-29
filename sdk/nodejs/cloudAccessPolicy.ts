// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * * [Official documentation](https://grafana.com/docs/grafana-cloud/account-management/authentication-and-permissions/access-policies/)
 * * [API documentation](https://grafana.com/docs/grafana-cloud/developer-resources/api-reference/cloud-api/#create-an-access-policy)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@lbrlabs/pulumi-grafana";
 * import * as grafana from "@pulumi/grafana";
 *
 * const current = grafana.getCloudOrganization({
 *     slug: "<your org slug>",
 * });
 * const testCloudAccessPolicy = new grafana.CloudAccessPolicy("testCloudAccessPolicy", {
 *     region: "us",
 *     displayName: "My Policy",
 *     scopes: [
 *         "metrics:read",
 *         "logs:read",
 *     ],
 *     realms: [{
 *         type: "org",
 *         identifier: current.then(current => current.id),
 *         labelPolicies: [{
 *             selector: "{namespace=\"default\"}",
 *         }],
 *     }],
 * });
 * const testCloudAccessPolicyToken = new grafana.CloudAccessPolicyToken("testCloudAccessPolicyToken", {
 *     region: "us",
 *     accessPolicyId: testCloudAccessPolicy.policyId,
 *     displayName: "My Policy Token",
 *     expiresAt: "2023-01-01T00:00:00Z",
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import grafana:index/cloudAccessPolicy:CloudAccessPolicy policyname {{region}}/{{policy_id}}
 * ```
 */
export class CloudAccessPolicy extends pulumi.CustomResource {
    /**
     * Get an existing CloudAccessPolicy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CloudAccessPolicyState, opts?: pulumi.CustomResourceOptions): CloudAccessPolicy {
        return new CloudAccessPolicy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/cloudAccessPolicy:CloudAccessPolicy';

    /**
     * Returns true if the given object is an instance of CloudAccessPolicy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CloudAccessPolicy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CloudAccessPolicy.__pulumiType;
    }

    /**
     * Creation date of the access policy.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * Display name of the access policy. Defaults to the name.
     */
    public readonly displayName!: pulumi.Output<string | undefined>;
    /**
     * Name of the access policy.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * ID of the access policy.
     */
    public /*out*/ readonly policyId!: pulumi.Output<string>;
    public readonly realms!: pulumi.Output<outputs.CloudAccessPolicyRealm[]>;
    /**
     * Region where the API is deployed. Generally where the stack is deployed. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/developer-resources/api-reference/cloud-api/#list-regions.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * Scopes of the access policy. See https://grafana.com/docs/grafana-cloud/account-management/authentication-and-permissions/access-policies/#scopes for possible values.
     */
    public readonly scopes!: pulumi.Output<string[]>;
    /**
     * Last update date of the access policy.
     */
    public /*out*/ readonly updatedAt!: pulumi.Output<string>;

    /**
     * Create a CloudAccessPolicy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CloudAccessPolicyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CloudAccessPolicyArgs | CloudAccessPolicyState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CloudAccessPolicyState | undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["displayName"] = state ? state.displayName : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["policyId"] = state ? state.policyId : undefined;
            resourceInputs["realms"] = state ? state.realms : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["scopes"] = state ? state.scopes : undefined;
            resourceInputs["updatedAt"] = state ? state.updatedAt : undefined;
        } else {
            const args = argsOrState as CloudAccessPolicyArgs | undefined;
            if ((!args || args.realms === undefined) && !opts.urn) {
                throw new Error("Missing required property 'realms'");
            }
            if ((!args || args.region === undefined) && !opts.urn) {
                throw new Error("Missing required property 'region'");
            }
            if ((!args || args.scopes === undefined) && !opts.urn) {
                throw new Error("Missing required property 'scopes'");
            }
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["realms"] = args ? args.realms : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["scopes"] = args ? args.scopes : undefined;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["policyId"] = undefined /*out*/;
            resourceInputs["updatedAt"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(CloudAccessPolicy.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CloudAccessPolicy resources.
 */
export interface CloudAccessPolicyState {
    /**
     * Creation date of the access policy.
     */
    createdAt?: pulumi.Input<string>;
    /**
     * Display name of the access policy. Defaults to the name.
     */
    displayName?: pulumi.Input<string>;
    /**
     * Name of the access policy.
     */
    name?: pulumi.Input<string>;
    /**
     * ID of the access policy.
     */
    policyId?: pulumi.Input<string>;
    realms?: pulumi.Input<pulumi.Input<inputs.CloudAccessPolicyRealm>[]>;
    /**
     * Region where the API is deployed. Generally where the stack is deployed. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/developer-resources/api-reference/cloud-api/#list-regions.
     */
    region?: pulumi.Input<string>;
    /**
     * Scopes of the access policy. See https://grafana.com/docs/grafana-cloud/account-management/authentication-and-permissions/access-policies/#scopes for possible values.
     */
    scopes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Last update date of the access policy.
     */
    updatedAt?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CloudAccessPolicy resource.
 */
export interface CloudAccessPolicyArgs {
    /**
     * Display name of the access policy. Defaults to the name.
     */
    displayName?: pulumi.Input<string>;
    /**
     * Name of the access policy.
     */
    name?: pulumi.Input<string>;
    realms: pulumi.Input<pulumi.Input<inputs.CloudAccessPolicyRealm>[]>;
    /**
     * Region where the API is deployed. Generally where the stack is deployed. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/developer-resources/api-reference/cloud-api/#list-regions.
     */
    region: pulumi.Input<string>;
    /**
     * Scopes of the access policy. See https://grafana.com/docs/grafana-cloud/account-management/authentication-and-permissions/access-policies/#scopes for possible values.
     */
    scopes: pulumi.Input<pulumi.Input<string>[]>;
}
