// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.grafana.AlertNotificationArgs;
import com.pulumi.grafana.Utilities;
import com.pulumi.grafana.inputs.AlertNotificationState;
import java.lang.Boolean;
import java.lang.Object;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * ## Example Usage
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.grafana.AlertNotification;
 * import com.pulumi.grafana.AlertNotificationArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var emailSometeam = new AlertNotification(&#34;emailSometeam&#34;, AlertNotificationArgs.builder()        
 *             .frequency(&#34;24h&#34;)
 *             .isDefault(false)
 *             .sendReminder(true)
 *             .settings(Map.ofEntries(
 *                 Map.entry(&#34;addresses&#34;, &#34;foo@example.net;bar@example.net&#34;),
 *                 Map.entry(&#34;uploadImage&#34;, &#34;false&#34;)
 *             ))
 *             .type(&#34;email&#34;)
 *             .build());
 * 
 *     }
 * }
 * ```
 * 
 * ## Import
 * 
 * ```sh
 *  $ pulumi import grafana:index/alertNotification:AlertNotification alert_notification_name {{alert_notification_id}}
 * ```
 * 
 */
@ResourceType(type="grafana:index/alertNotification:AlertNotification")
public class AlertNotification extends com.pulumi.resources.CustomResource {
    /**
     * Whether to disable sending resolve messages. Defaults to `false`.
     * 
     */
    @Export(name="disableResolveMessage", type=Boolean.class, parameters={})
    private Output</* @Nullable */ Boolean> disableResolveMessage;

    /**
     * @return Whether to disable sending resolve messages. Defaults to `false`.
     * 
     */
    public Output<Optional<Boolean>> disableResolveMessage() {
        return Codegen.optional(this.disableResolveMessage);
    }
    /**
     * Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.
     * 
     */
    @Export(name="frequency", type=String.class, parameters={})
    private Output</* @Nullable */ String> frequency;

    /**
     * @return Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.
     * 
     */
    public Output<Optional<String>> frequency() {
        return Codegen.optional(this.frequency);
    }
    /**
     * Is this the default channel for all your alerts. Defaults to `false`.
     * 
     */
    @Export(name="isDefault", type=Boolean.class, parameters={})
    private Output</* @Nullable */ Boolean> isDefault;

    /**
     * @return Is this the default channel for all your alerts. Defaults to `false`.
     * 
     */
    public Output<Optional<Boolean>> isDefault() {
        return Codegen.optional(this.isDefault);
    }
    /**
     * The name of the alert notification channel.
     * 
     */
    @Export(name="name", type=String.class, parameters={})
    private Output<String> name;

    /**
     * @return The name of the alert notification channel.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * Additional secure settings, for full reference lookup [Grafana Supported Settings documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings).
     * 
     */
    @Export(name="secureSettings", type=Map.class, parameters={String.class, Object.class})
    private Output</* @Nullable */ Map<String,Object>> secureSettings;

    /**
     * @return Additional secure settings, for full reference lookup [Grafana Supported Settings documentation](https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings).
     * 
     */
    public Output<Optional<Map<String,Object>>> secureSettings() {
        return Codegen.optional(this.secureSettings);
    }
    /**
     * Whether to send reminders for triggered alerts. Defaults to `false`.
     * 
     */
    @Export(name="sendReminder", type=Boolean.class, parameters={})
    private Output</* @Nullable */ Boolean> sendReminder;

    /**
     * @return Whether to send reminders for triggered alerts. Defaults to `false`.
     * 
     */
    public Output<Optional<Boolean>> sendReminder() {
        return Codegen.optional(this.sendReminder);
    }
    /**
     * Additional settings, for full reference see [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/developers/http_api/alerting_notification_channels/).
     * 
     */
    @Export(name="settings", type=Map.class, parameters={String.class, Object.class})
    private Output</* @Nullable */ Map<String,Object>> settings;

    /**
     * @return Additional settings, for full reference see [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/developers/http_api/alerting_notification_channels/).
     * 
     */
    public Output<Optional<Map<String,Object>>> settings() {
        return Codegen.optional(this.settings);
    }
    /**
     * The type of the alert notification channel.
     * 
     */
    @Export(name="type", type=String.class, parameters={})
    private Output<String> type;

    /**
     * @return The type of the alert notification channel.
     * 
     */
    public Output<String> type() {
        return this.type;
    }
    /**
     * Unique identifier. If unset, this will be automatically generated.
     * 
     */
    @Export(name="uid", type=String.class, parameters={})
    private Output<String> uid;

    /**
     * @return Unique identifier. If unset, this will be automatically generated.
     * 
     */
    public Output<String> uid() {
        return this.uid;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public AlertNotification(String name) {
        this(name, AlertNotificationArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public AlertNotification(String name, AlertNotificationArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public AlertNotification(String name, AlertNotificationArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/alertNotification:AlertNotification", name, args == null ? AlertNotificationArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private AlertNotification(String name, Output<String> id, @Nullable AlertNotificationState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/alertNotification:AlertNotification", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .additionalSecretOutputs(List.of(
                "secureSettings"
            ))
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static AlertNotification get(String name, Output<String> id, @Nullable AlertNotificationState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new AlertNotification(name, id, state, options);
    }
}
