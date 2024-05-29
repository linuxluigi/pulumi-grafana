// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class DataSourceConfig extends pulumi.CustomResource {
    /**
     * Get an existing DataSourceConfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DataSourceConfigState, opts?: pulumi.CustomResourceOptions): DataSourceConfig {
        return new DataSourceConfig(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/dataSourceConfig:DataSourceConfig';

    /**
     * Returns true if the given object is an instance of DataSourceConfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DataSourceConfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DataSourceConfig.__pulumiType;
    }

    /**
     * Custom HTTP headers
     */
    public readonly httpHeaders!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data
     * source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it
     * from the Grafana UI. Note that keys in this map are usually camelCased.
     */
    public readonly jsonDataEncoded!: pulumi.Output<string | undefined>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    public readonly orgId!: pulumi.Output<string | undefined>;
    /**
     * Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options
     * to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when
     * saving it from the Grafana UI. Note that keys in this map are usually camelCased.
     */
    public readonly secureJsonDataEncoded!: pulumi.Output<string | undefined>;
    /**
     * Unique identifier. If unset, this will be automatically generated.
     */
    public readonly uid!: pulumi.Output<string>;

    /**
     * Create a DataSourceConfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DataSourceConfigArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DataSourceConfigArgs | DataSourceConfigState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DataSourceConfigState | undefined;
            resourceInputs["httpHeaders"] = state ? state.httpHeaders : undefined;
            resourceInputs["jsonDataEncoded"] = state ? state.jsonDataEncoded : undefined;
            resourceInputs["orgId"] = state ? state.orgId : undefined;
            resourceInputs["secureJsonDataEncoded"] = state ? state.secureJsonDataEncoded : undefined;
            resourceInputs["uid"] = state ? state.uid : undefined;
        } else {
            const args = argsOrState as DataSourceConfigArgs | undefined;
            resourceInputs["httpHeaders"] = args?.httpHeaders ? pulumi.secret(args.httpHeaders) : undefined;
            resourceInputs["jsonDataEncoded"] = args ? args.jsonDataEncoded : undefined;
            resourceInputs["orgId"] = args ? args.orgId : undefined;
            resourceInputs["secureJsonDataEncoded"] = args?.secureJsonDataEncoded ? pulumi.secret(args.secureJsonDataEncoded) : undefined;
            resourceInputs["uid"] = args ? args.uid : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["httpHeaders", "secureJsonDataEncoded"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(DataSourceConfig.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DataSourceConfig resources.
 */
export interface DataSourceConfigState {
    /**
     * Custom HTTP headers
     */
    httpHeaders?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data
     * source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it
     * from the Grafana UI. Note that keys in this map are usually camelCased.
     */
    jsonDataEncoded?: pulumi.Input<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options
     * to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when
     * saving it from the Grafana UI. Note that keys in this map are usually camelCased.
     */
    secureJsonDataEncoded?: pulumi.Input<string>;
    /**
     * Unique identifier. If unset, this will be automatically generated.
     */
    uid?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DataSourceConfig resource.
 */
export interface DataSourceConfigArgs {
    /**
     * Custom HTTP headers
     */
    httpHeaders?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data
     * source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it
     * from the Grafana UI. Note that keys in this map are usually camelCased.
     */
    jsonDataEncoded?: pulumi.Input<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options
     * to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when
     * saving it from the Grafana UI. Note that keys in this map are usually camelCased.
     */
    secureJsonDataEncoded?: pulumi.Input<string>;
    /**
     * Unique identifier. If unset, this will be automatically generated.
     */
    uid?: pulumi.Input<string>;
}
