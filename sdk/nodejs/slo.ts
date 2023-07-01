// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Resource manages Grafana SLOs.
 *
 * * [Official documentation](https://grafana.com/docs/grafana-cloud/slo/)
 * * [API documentation](https://grafana.com/docs/grafana-cloud/slo/api/)
 */
export class SLO extends pulumi.CustomResource {
    /**
     * Get an existing SLO resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SLOState, opts?: pulumi.CustomResourceOptions): SLO {
        return new SLO(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/sLO:SLO';

    /**
     * Returns true if the given object is an instance of SLO.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SLO {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SLO.__pulumiType;
    }

    /**
     * Configures the alerting rules that will be generated for each
     * 			time window associated with the SLO. Grafana SLOs can generate
     * 			alerts when the short-term error budget burn is very high, the
     * 			long-term error budget burn rate is high, or when the remaining
     * 			error budget is below a certain threshold.
     */
    public readonly alertings!: pulumi.Output<outputs.SLOAlerting[] | undefined>;
    /**
     * Description is a free-text field that can provide more context to an SLO.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * Additional labels that will be attached to all metrics generated from the query. These labels are useful for grouping SLOs in dashboard views that you create by hand.
     */
    public readonly labels!: pulumi.Output<outputs.SLOLabel[] | undefined>;
    /**
     * Name should be a short description of your indicator. Consider names like "API Availability"
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Over each rolling time window, the remaining error budget will be calculated, and separate alerts can be generated for each time window based on the SLO burn rate or remaining error budget.
     */
    public readonly objectives!: pulumi.Output<outputs.SLOObjective[]>;
    /**
     * Query describes the indicator that will be measured against the objective. Freeform Query types are currently supported.
     */
    public readonly queries!: pulumi.Output<outputs.SLOQuery[]>;

    /**
     * Create a SLO resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SLOArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SLOArgs | SLOState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SLOState | undefined;
            resourceInputs["alertings"] = state ? state.alertings : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["labels"] = state ? state.labels : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["objectives"] = state ? state.objectives : undefined;
            resourceInputs["queries"] = state ? state.queries : undefined;
        } else {
            const args = argsOrState as SLOArgs | undefined;
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            if ((!args || args.objectives === undefined) && !opts.urn) {
                throw new Error("Missing required property 'objectives'");
            }
            if ((!args || args.queries === undefined) && !opts.urn) {
                throw new Error("Missing required property 'queries'");
            }
            resourceInputs["alertings"] = args ? args.alertings : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["objectives"] = args ? args.objectives : undefined;
            resourceInputs["queries"] = args ? args.queries : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(SLO.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SLO resources.
 */
export interface SLOState {
    /**
     * Configures the alerting rules that will be generated for each
     * 			time window associated with the SLO. Grafana SLOs can generate
     * 			alerts when the short-term error budget burn is very high, the
     * 			long-term error budget burn rate is high, or when the remaining
     * 			error budget is below a certain threshold.
     */
    alertings?: pulumi.Input<pulumi.Input<inputs.SLOAlerting>[]>;
    /**
     * Description is a free-text field that can provide more context to an SLO.
     */
    description?: pulumi.Input<string>;
    /**
     * Additional labels that will be attached to all metrics generated from the query. These labels are useful for grouping SLOs in dashboard views that you create by hand.
     */
    labels?: pulumi.Input<pulumi.Input<inputs.SLOLabel>[]>;
    /**
     * Name should be a short description of your indicator. Consider names like "API Availability"
     */
    name?: pulumi.Input<string>;
    /**
     * Over each rolling time window, the remaining error budget will be calculated, and separate alerts can be generated for each time window based on the SLO burn rate or remaining error budget.
     */
    objectives?: pulumi.Input<pulumi.Input<inputs.SLOObjective>[]>;
    /**
     * Query describes the indicator that will be measured against the objective. Freeform Query types are currently supported.
     */
    queries?: pulumi.Input<pulumi.Input<inputs.SLOQuery>[]>;
}

/**
 * The set of arguments for constructing a SLO resource.
 */
export interface SLOArgs {
    /**
     * Configures the alerting rules that will be generated for each
     * 			time window associated with the SLO. Grafana SLOs can generate
     * 			alerts when the short-term error budget burn is very high, the
     * 			long-term error budget burn rate is high, or when the remaining
     * 			error budget is below a certain threshold.
     */
    alertings?: pulumi.Input<pulumi.Input<inputs.SLOAlerting>[]>;
    /**
     * Description is a free-text field that can provide more context to an SLO.
     */
    description: pulumi.Input<string>;
    /**
     * Additional labels that will be attached to all metrics generated from the query. These labels are useful for grouping SLOs in dashboard views that you create by hand.
     */
    labels?: pulumi.Input<pulumi.Input<inputs.SLOLabel>[]>;
    /**
     * Name should be a short description of your indicator. Consider names like "API Availability"
     */
    name?: pulumi.Input<string>;
    /**
     * Over each rolling time window, the remaining error budget will be calculated, and separate alerts can be generated for each time window based on the SLO burn rate or remaining error budget.
     */
    objectives: pulumi.Input<pulumi.Input<inputs.SLOObjective>[]>;
    /**
     * Query describes the indicator that will be measured against the objective. Freeform Query types are currently supported.
     */
    queries: pulumi.Input<pulumi.Input<inputs.SLOQuery>[]>;
}
