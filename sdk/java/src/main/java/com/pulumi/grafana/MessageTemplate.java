// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.grafana.MessageTemplateArgs;
import com.pulumi.grafana.Utilities;
import com.pulumi.grafana.inputs.MessageTemplateState;
import java.lang.String;
import javax.annotation.Nullable;

/**
 * Manages Grafana Alerting message templates.
 * 
 * * [Official documentation](https://grafana.com/docs/grafana/next/alerting/contact-points/message-templating/)
 * * [HTTP API](https://grafana.com/docs/grafana/next/developers/http_api/alerting_provisioning/#templates)
 * 
 * This resource requires Grafana 9.1.0 or later.
 * 
 * ## Example Usage
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.grafana.MessageTemplate;
 * import com.pulumi.grafana.MessageTemplateArgs;
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
 *         var myTemplate = new MessageTemplate(&#34;myTemplate&#34;, MessageTemplateArgs.builder()        
 *             .template(&#34;&#34;&#34;
 * {{define &#34;My Reusable Template&#34; }}
 *  template content
 * {{ end }}
 *             &#34;&#34;&#34;)
 *             .build());
 * 
 *     }
 * }
 * ```
 * 
 * ## Import
 * 
 * ```sh
 *  $ pulumi import grafana:index/messageTemplate:MessageTemplate message_template_name {{message_template_name}}
 * ```
 * 
 */
@ResourceType(type="grafana:index/messageTemplate:MessageTemplate")
public class MessageTemplate extends com.pulumi.resources.CustomResource {
    /**
     * The name of the message template.
     * 
     */
    @Export(name="name", type=String.class, parameters={})
    private Output<String> name;

    /**
     * @return The name of the message template.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * The content of the message template.
     * 
     */
    @Export(name="template", type=String.class, parameters={})
    private Output<String> template;

    /**
     * @return The content of the message template.
     * 
     */
    public Output<String> template() {
        return this.template;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public MessageTemplate(String name) {
        this(name, MessageTemplateArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public MessageTemplate(String name, MessageTemplateArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public MessageTemplate(String name, MessageTemplateArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/messageTemplate:MessageTemplate", name, args == null ? MessageTemplateArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private MessageTemplate(String name, Output<String> id, @Nullable MessageTemplateState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/messageTemplate:MessageTemplate", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
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
    public static MessageTemplate get(String name, Output<String> id, @Nullable MessageTemplateState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new MessageTemplate(name, id, state, options);
    }
}
