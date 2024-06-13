// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * @deprecated grafana.index/cloudstackapikey.CloudStackApiKey has been deprecated in favor of grafana.cloud/stackapikey.StackApiKey
 */
export class CloudStackApiKey extends pulumi.CustomResource {
    /**
     * Get an existing CloudStackApiKey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CloudStackApiKeyState, opts?: pulumi.CustomResourceOptions): CloudStackApiKey {
        pulumi.log.warn("CloudStackApiKey is deprecated: grafana.index/cloudstackapikey.CloudStackApiKey has been deprecated in favor of grafana.cloud/stackapikey.StackApiKey")
        return new CloudStackApiKey(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/cloudStackApiKey:CloudStackApiKey';

    /**
     * Returns true if the given object is an instance of CloudStackApiKey.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CloudStackApiKey {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CloudStackApiKey.__pulumiType;
    }

    public /*out*/ readonly expiration!: pulumi.Output<string>;
    public /*out*/ readonly key!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public readonly role!: pulumi.Output<string>;
    public readonly secondsToLive!: pulumi.Output<number | undefined>;
    public readonly stackSlug!: pulumi.Output<string>;

    /**
     * Create a CloudStackApiKey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated grafana.index/cloudstackapikey.CloudStackApiKey has been deprecated in favor of grafana.cloud/stackapikey.StackApiKey */
    constructor(name: string, args: CloudStackApiKeyArgs, opts?: pulumi.CustomResourceOptions)
    /** @deprecated grafana.index/cloudstackapikey.CloudStackApiKey has been deprecated in favor of grafana.cloud/stackapikey.StackApiKey */
    constructor(name: string, argsOrState?: CloudStackApiKeyArgs | CloudStackApiKeyState, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("CloudStackApiKey is deprecated: grafana.index/cloudstackapikey.CloudStackApiKey has been deprecated in favor of grafana.cloud/stackapikey.StackApiKey")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CloudStackApiKeyState | undefined;
            resourceInputs["expiration"] = state ? state.expiration : undefined;
            resourceInputs["key"] = state ? state.key : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["role"] = state ? state.role : undefined;
            resourceInputs["secondsToLive"] = state ? state.secondsToLive : undefined;
            resourceInputs["stackSlug"] = state ? state.stackSlug : undefined;
        } else {
            const args = argsOrState as CloudStackApiKeyArgs | undefined;
            if ((!args || args.role === undefined) && !opts.urn) {
                throw new Error("Missing required property 'role'");
            }
            if ((!args || args.stackSlug === undefined) && !opts.urn) {
                throw new Error("Missing required property 'stackSlug'");
            }
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["role"] = args ? args.role : undefined;
            resourceInputs["secondsToLive"] = args ? args.secondsToLive : undefined;
            resourceInputs["stackSlug"] = args ? args.stackSlug : undefined;
            resourceInputs["expiration"] = undefined /*out*/;
            resourceInputs["key"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const aliasOpts = { aliases: [{ type: "grafana:index/cloudStackApiKey:CloudStackApiKey" }] };
        opts = pulumi.mergeOptions(opts, aliasOpts);
        const secretOpts = { additionalSecretOutputs: ["key"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(CloudStackApiKey.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CloudStackApiKey resources.
 */
export interface CloudStackApiKeyState {
    expiration?: pulumi.Input<string>;
    key?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    role?: pulumi.Input<string>;
    secondsToLive?: pulumi.Input<number>;
    stackSlug?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CloudStackApiKey resource.
 */
export interface CloudStackApiKeyArgs {
    name?: pulumi.Input<string>;
    role: pulumi.Input<string>;
    secondsToLive?: pulumi.Input<number>;
    stackSlug: pulumi.Input<string>;
}
