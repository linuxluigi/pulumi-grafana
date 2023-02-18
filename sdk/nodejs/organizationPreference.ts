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
 * import * as grafana from "@lbrlabs/pulumi-grafana";
 *
 * const test = new grafana.OrganizationPreference("test", {
 *     theme: "light",
 *     timezone: "utc",
 *     weekStart: "Tuesday",
 * });
 * ```
 */
export class OrganizationPreference extends pulumi.CustomResource {
    /**
     * Get an existing OrganizationPreference resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrganizationPreferenceState, opts?: pulumi.CustomResourceOptions): OrganizationPreference {
        return new OrganizationPreference(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/organizationPreference:OrganizationPreference';

    /**
     * Returns true if the given object is an instance of OrganizationPreference.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OrganizationPreference {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OrganizationPreference.__pulumiType;
    }

    /**
     * The Organization home dashboard ID.
     */
    public readonly homeDashboardId!: pulumi.Output<number | undefined>;
    /**
     * The Organization home dashboard UID. This is only available in Grafana 9.0+.
     */
    public readonly homeDashboardUid!: pulumi.Output<string | undefined>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    public readonly orgId!: pulumi.Output<string | undefined>;
    /**
     * The Organization theme. Available values are `light`, `dark`, or an empty string for the default.
     */
    public readonly theme!: pulumi.Output<string | undefined>;
    /**
     * The Organization timezone. Available values are `utc`, `browser`, or an empty string for the default.
     */
    public readonly timezone!: pulumi.Output<string | undefined>;
    /**
     * The Organization week start.
     */
    public readonly weekStart!: pulumi.Output<string | undefined>;

    /**
     * Create a OrganizationPreference resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: OrganizationPreferenceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: OrganizationPreferenceArgs | OrganizationPreferenceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as OrganizationPreferenceState | undefined;
            resourceInputs["homeDashboardId"] = state ? state.homeDashboardId : undefined;
            resourceInputs["homeDashboardUid"] = state ? state.homeDashboardUid : undefined;
            resourceInputs["orgId"] = state ? state.orgId : undefined;
            resourceInputs["theme"] = state ? state.theme : undefined;
            resourceInputs["timezone"] = state ? state.timezone : undefined;
            resourceInputs["weekStart"] = state ? state.weekStart : undefined;
        } else {
            const args = argsOrState as OrganizationPreferenceArgs | undefined;
            resourceInputs["homeDashboardId"] = args ? args.homeDashboardId : undefined;
            resourceInputs["homeDashboardUid"] = args ? args.homeDashboardUid : undefined;
            resourceInputs["orgId"] = args ? args.orgId : undefined;
            resourceInputs["theme"] = args ? args.theme : undefined;
            resourceInputs["timezone"] = args ? args.timezone : undefined;
            resourceInputs["weekStart"] = args ? args.weekStart : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(OrganizationPreference.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering OrganizationPreference resources.
 */
export interface OrganizationPreferenceState {
    /**
     * The Organization home dashboard ID.
     */
    homeDashboardId?: pulumi.Input<number>;
    /**
     * The Organization home dashboard UID. This is only available in Grafana 9.0+.
     */
    homeDashboardUid?: pulumi.Input<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * The Organization theme. Available values are `light`, `dark`, or an empty string for the default.
     */
    theme?: pulumi.Input<string>;
    /**
     * The Organization timezone. Available values are `utc`, `browser`, or an empty string for the default.
     */
    timezone?: pulumi.Input<string>;
    /**
     * The Organization week start.
     */
    weekStart?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a OrganizationPreference resource.
 */
export interface OrganizationPreferenceArgs {
    /**
     * The Organization home dashboard ID.
     */
    homeDashboardId?: pulumi.Input<number>;
    /**
     * The Organization home dashboard UID. This is only available in Grafana 9.0+.
     */
    homeDashboardUid?: pulumi.Input<string>;
    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     */
    orgId?: pulumi.Input<string>;
    /**
     * The Organization theme. Available values are `light`, `dark`, or an empty string for the default.
     */
    theme?: pulumi.Input<string>;
    /**
     * The Organization timezone. Available values are `utc`, `browser`, or an empty string for the default.
     */
    timezone?: pulumi.Input<string>;
    /**
     * The Organization week start.
     */
    weekStart?: pulumi.Input<string>;
}
