// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * * [Official documentation](https://grafana.com/docs/grafana/latest/alerting/notifications/)
 * * [HTTP API](https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@pulumi/grafana";
 *
 * const emailSometeam = new grafana.AlertNotification("email_someteam", {
 *     frequency: "24h",
 *     isDefault: false,
 *     sendReminder: true,
 *     settings: {
 *         addresses: "foo@example.net;bar@example.net",
 *         uploadImage: "false",
 *     },
 *     type: "email",
 * });
 * ```
 *
 * ## Import
 *
 * ```sh
 *  $ pulumi import grafana:index/alertNotification:AlertNotification alert_notification_name {{alert_notification_id}}
 * ```
 */
export class AlertNotification extends pulumi.CustomResource {
    /**
     * Get an existing AlertNotification resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AlertNotificationState, opts?: pulumi.CustomResourceOptions): AlertNotification {
        return new AlertNotification(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/alertNotification:AlertNotification';

    /**
     * Returns true if the given object is an instance of AlertNotification.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AlertNotification {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AlertNotification.__pulumiType;
    }

    /**
     * Whether to disable sending resolve messages. Defaults to `false`.
     */
    public readonly disableResolveMessage!: pulumi.Output<boolean | undefined>;
    /**
     * Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.
     */
    public readonly frequency!: pulumi.Output<string | undefined>;
    /**
     * Is this the default channel for all your alerts. Defaults to `false`.
     */
    public readonly isDefault!: pulumi.Output<boolean | undefined>;
    /**
     * The name of the alert notification channel.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Additional secure settings, for full reference lookup [Grafana Supported Settings documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings).
     */
    public readonly secureSettings!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * Whether to send reminders for triggered alerts. Defaults to `false`.
     */
    public readonly sendReminder!: pulumi.Output<boolean | undefined>;
    /**
     * Additional settings, for full reference see [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/).
     */
    public readonly settings!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The type of the alert notification channel.
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * Unique identifier. If unset, this will be automatically generated.
     */
    public readonly uid!: pulumi.Output<string>;

    /**
     * Create a AlertNotification resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AlertNotificationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AlertNotificationArgs | AlertNotificationState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AlertNotificationState | undefined;
            resourceInputs["disableResolveMessage"] = state ? state.disableResolveMessage : undefined;
            resourceInputs["frequency"] = state ? state.frequency : undefined;
            resourceInputs["isDefault"] = state ? state.isDefault : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["secureSettings"] = state ? state.secureSettings : undefined;
            resourceInputs["sendReminder"] = state ? state.sendReminder : undefined;
            resourceInputs["settings"] = state ? state.settings : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
            resourceInputs["uid"] = state ? state.uid : undefined;
        } else {
            const args = argsOrState as AlertNotificationArgs | undefined;
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            resourceInputs["disableResolveMessage"] = args ? args.disableResolveMessage : undefined;
            resourceInputs["frequency"] = args ? args.frequency : undefined;
            resourceInputs["isDefault"] = args ? args.isDefault : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["secureSettings"] = args?.secureSettings ? pulumi.secret(args.secureSettings) : undefined;
            resourceInputs["sendReminder"] = args ? args.sendReminder : undefined;
            resourceInputs["settings"] = args ? args.settings : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["uid"] = args ? args.uid : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["secureSettings"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(AlertNotification.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AlertNotification resources.
 */
export interface AlertNotificationState {
    /**
     * Whether to disable sending resolve messages. Defaults to `false`.
     */
    disableResolveMessage?: pulumi.Input<boolean>;
    /**
     * Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.
     */
    frequency?: pulumi.Input<string>;
    /**
     * Is this the default channel for all your alerts. Defaults to `false`.
     */
    isDefault?: pulumi.Input<boolean>;
    /**
     * The name of the alert notification channel.
     */
    name?: pulumi.Input<string>;
    /**
     * Additional secure settings, for full reference lookup [Grafana Supported Settings documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings).
     */
    secureSettings?: pulumi.Input<{[key: string]: any}>;
    /**
     * Whether to send reminders for triggered alerts. Defaults to `false`.
     */
    sendReminder?: pulumi.Input<boolean>;
    /**
     * Additional settings, for full reference see [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/).
     */
    settings?: pulumi.Input<{[key: string]: any}>;
    /**
     * The type of the alert notification channel.
     */
    type?: pulumi.Input<string>;
    /**
     * Unique identifier. If unset, this will be automatically generated.
     */
    uid?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AlertNotification resource.
 */
export interface AlertNotificationArgs {
    /**
     * Whether to disable sending resolve messages. Defaults to `false`.
     */
    disableResolveMessage?: pulumi.Input<boolean>;
    /**
     * Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.
     */
    frequency?: pulumi.Input<string>;
    /**
     * Is this the default channel for all your alerts. Defaults to `false`.
     */
    isDefault?: pulumi.Input<boolean>;
    /**
     * The name of the alert notification channel.
     */
    name?: pulumi.Input<string>;
    /**
     * Additional secure settings, for full reference lookup [Grafana Supported Settings documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings).
     */
    secureSettings?: pulumi.Input<{[key: string]: any}>;
    /**
     * Whether to send reminders for triggered alerts. Defaults to `false`.
     */
    sendReminder?: pulumi.Input<boolean>;
    /**
     * Additional settings, for full reference see [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/).
     */
    settings?: pulumi.Input<{[key: string]: any}>;
    /**
     * The type of the alert notification channel.
     */
    type: pulumi.Input<string>;
    /**
     * Unique identifier. If unset, this will be automatically generated.
     */
    uid?: pulumi.Input<string>;
}
