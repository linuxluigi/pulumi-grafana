// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.grafana.CloudAccessPolicyTokenArgs;
import com.pulumi.grafana.Utilities;
import com.pulumi.grafana.inputs.CloudAccessPolicyTokenState;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * * [Official documentation](https://grafana.com/docs/grafana-cloud/authentication-and-permissions/access-policies/)
 * * [API documentation](https://grafana.com/docs/grafana-cloud/reference/cloud-api/#create-a-token)
 * 
 * ## Example Usage
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.grafana.GrafanaFunctions;
 * import com.pulumi.grafana.inputs.GetCloudOrganizationArgs;
 * import com.pulumi.grafana.CloudAccessPolicy;
 * import com.pulumi.grafana.CloudAccessPolicyArgs;
 * import com.pulumi.grafana.inputs.CloudAccessPolicyRealmArgs;
 * import com.pulumi.grafana.CloudAccessPolicyToken;
 * import com.pulumi.grafana.CloudAccessPolicyTokenArgs;
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
 *         final var current = GrafanaFunctions.getCloudOrganization(GetCloudOrganizationArgs.builder()
 *             .slug(&#34;&lt;your org slug&gt;&#34;)
 *             .build());
 * 
 *         var testCloudAccessPolicy = new CloudAccessPolicy(&#34;testCloudAccessPolicy&#34;, CloudAccessPolicyArgs.builder()        
 *             .region(&#34;us&#34;)
 *             .displayName(&#34;My Policy&#34;)
 *             .scopes(            
 *                 &#34;metrics:read&#34;,
 *                 &#34;logs:read&#34;)
 *             .realms(CloudAccessPolicyRealmArgs.builder()
 *                 .type(&#34;org&#34;)
 *                 .identifier(current.applyValue(getCloudOrganizationResult -&gt; getCloudOrganizationResult.id()))
 *                 .labelPolicies(CloudAccessPolicyRealmLabelPolicyArgs.builder()
 *                     .selector(&#34;{namespace=\&#34;default\&#34;}&#34;)
 *                     .build())
 *                 .build())
 *             .build());
 * 
 *         var testCloudAccessPolicyToken = new CloudAccessPolicyToken(&#34;testCloudAccessPolicyToken&#34;, CloudAccessPolicyTokenArgs.builder()        
 *             .region(&#34;us&#34;)
 *             .accessPolicyId(testCloudAccessPolicy.policyId())
 *             .displayName(&#34;My Policy Token&#34;)
 *             .expiresAt(&#34;2023-01-01T00:00:00Z&#34;)
 *             .build());
 * 
 *     }
 * }
 * ```
 * 
 */
@ResourceType(type="grafana:index/cloudAccessPolicyToken:CloudAccessPolicyToken")
public class CloudAccessPolicyToken extends com.pulumi.resources.CustomResource {
    /**
     * ID of the access policy for which to create a token.
     * 
     */
    @Export(name="accessPolicyId", type=String.class, parameters={})
    private Output<String> accessPolicyId;

    /**
     * @return ID of the access policy for which to create a token.
     * 
     */
    public Output<String> accessPolicyId() {
        return this.accessPolicyId;
    }
    /**
     * Creation date of the access policy token.
     * 
     */
    @Export(name="createdAt", type=String.class, parameters={})
    private Output<String> createdAt;

    /**
     * @return Creation date of the access policy token.
     * 
     */
    public Output<String> createdAt() {
        return this.createdAt;
    }
    /**
     * Display name of the access policy token. Defaults to the name.
     * 
     */
    @Export(name="displayName", type=String.class, parameters={})
    private Output</* @Nullable */ String> displayName;

    /**
     * @return Display name of the access policy token. Defaults to the name.
     * 
     */
    public Output<Optional<String>> displayName() {
        return Codegen.optional(this.displayName);
    }
    /**
     * Expiration date of the access policy token. Does not expire by default.
     * 
     */
    @Export(name="expiresAt", type=String.class, parameters={})
    private Output</* @Nullable */ String> expiresAt;

    /**
     * @return Expiration date of the access policy token. Does not expire by default.
     * 
     */
    public Output<Optional<String>> expiresAt() {
        return Codegen.optional(this.expiresAt);
    }
    /**
     * Name of the access policy token.
     * 
     */
    @Export(name="name", type=String.class, parameters={})
    private Output<String> name;

    /**
     * @return Name of the access policy token.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * Region of the access policy. Should be set to the same region as the access policy. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/reference/cloud-api/#list-regions.
     * 
     */
    @Export(name="region", type=String.class, parameters={})
    private Output<String> region;

    /**
     * @return Region of the access policy. Should be set to the same region as the access policy. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/reference/cloud-api/#list-regions.
     * 
     */
    public Output<String> region() {
        return this.region;
    }
    @Export(name="token", type=String.class, parameters={})
    private Output<String> token;

    public Output<String> token() {
        return this.token;
    }
    /**
     * Last update date of the access policy token.
     * 
     */
    @Export(name="updatedAt", type=String.class, parameters={})
    private Output<String> updatedAt;

    /**
     * @return Last update date of the access policy token.
     * 
     */
    public Output<String> updatedAt() {
        return this.updatedAt;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public CloudAccessPolicyToken(String name) {
        this(name, CloudAccessPolicyTokenArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public CloudAccessPolicyToken(String name, CloudAccessPolicyTokenArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public CloudAccessPolicyToken(String name, CloudAccessPolicyTokenArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/cloudAccessPolicyToken:CloudAccessPolicyToken", name, args == null ? CloudAccessPolicyTokenArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private CloudAccessPolicyToken(String name, Output<String> id, @Nullable CloudAccessPolicyTokenState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/cloudAccessPolicyToken:CloudAccessPolicyToken", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .additionalSecretOutputs(List.of(
                "token"
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
    public static CloudAccessPolicyToken get(String name, Output<String> id, @Nullable CloudAccessPolicyTokenState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new CloudAccessPolicyToken(name, id, state, options);
    }
}
