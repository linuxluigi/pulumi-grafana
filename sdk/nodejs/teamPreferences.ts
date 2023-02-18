// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * * [Official documentation](https://grafana.com/docs/grafana/latest/administration/organization-preferences/)
 * * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/team/)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as fs from "fs";
 * import * as grafana from "@lbrlabs/pulumi-grafana";
 *
 * const metrics = new grafana.Dashboard("metrics", {configJson: fs.readFileSync("grafana-dashboard.json")});
 * const team = new grafana.Team("team", {});
 * const teamPreferences = new grafana.TeamPreferences("teamPreferences", {
 *     teamId: team.id,
 *     theme: "dark",
 *     timezone: "browser",
 *     homeDashboardId: metrics.dashboardId,
 * });
 * ```
 */
export class TeamPreferences extends pulumi.CustomResource {
    /**
     * Get an existing TeamPreferences resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TeamPreferencesState, opts?: pulumi.CustomResourceOptions): TeamPreferences {
        return new TeamPreferences(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/teamPreferences:TeamPreferences';

    /**
     * Returns true if the given object is an instance of TeamPreferences.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TeamPreferences {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TeamPreferences.__pulumiType;
    }

    /**
     * The numeric ID of the dashboard to display when a team member logs in.
     */
    public readonly homeDashboardId!: pulumi.Output<number | undefined>;
    /**
     * The numeric team ID.
     */
    public readonly teamId!: pulumi.Output<number>;
    /**
     * The theme for the specified team. Available themes are `light`, `dark`, or an empty string for the default theme.
     */
    public readonly theme!: pulumi.Output<string | undefined>;
    /**
     * The timezone for the specified team. Available values are `utc`, `browser`, or an empty string for the default.
     */
    public readonly timezone!: pulumi.Output<string | undefined>;

    /**
     * Create a TeamPreferences resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TeamPreferencesArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TeamPreferencesArgs | TeamPreferencesState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TeamPreferencesState | undefined;
            resourceInputs["homeDashboardId"] = state ? state.homeDashboardId : undefined;
            resourceInputs["teamId"] = state ? state.teamId : undefined;
            resourceInputs["theme"] = state ? state.theme : undefined;
            resourceInputs["timezone"] = state ? state.timezone : undefined;
        } else {
            const args = argsOrState as TeamPreferencesArgs | undefined;
            if ((!args || args.teamId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'teamId'");
            }
            resourceInputs["homeDashboardId"] = args ? args.homeDashboardId : undefined;
            resourceInputs["teamId"] = args ? args.teamId : undefined;
            resourceInputs["theme"] = args ? args.theme : undefined;
            resourceInputs["timezone"] = args ? args.timezone : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(TeamPreferences.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TeamPreferences resources.
 */
export interface TeamPreferencesState {
    /**
     * The numeric ID of the dashboard to display when a team member logs in.
     */
    homeDashboardId?: pulumi.Input<number>;
    /**
     * The numeric team ID.
     */
    teamId?: pulumi.Input<number>;
    /**
     * The theme for the specified team. Available themes are `light`, `dark`, or an empty string for the default theme.
     */
    theme?: pulumi.Input<string>;
    /**
     * The timezone for the specified team. Available values are `utc`, `browser`, or an empty string for the default.
     */
    timezone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a TeamPreferences resource.
 */
export interface TeamPreferencesArgs {
    /**
     * The numeric ID of the dashboard to display when a team member logs in.
     */
    homeDashboardId?: pulumi.Input<number>;
    /**
     * The numeric team ID.
     */
    teamId: pulumi.Input<number>;
    /**
     * The theme for the specified team. Available themes are `light`, `dark`, or an empty string for the default theme.
     */
    theme?: pulumi.Input<string>;
    /**
     * The timezone for the specified team. Available values are `utc`, `browser`, or an empty string for the default.
     */
    timezone?: pulumi.Input<string>;
}
