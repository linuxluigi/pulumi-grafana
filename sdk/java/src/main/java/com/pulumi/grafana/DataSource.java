// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.grafana.DataSourceArgs;
import com.pulumi.grafana.Utilities;
import com.pulumi.grafana.inputs.DataSourceState;
import com.pulumi.grafana.outputs.DataSourceJsonData;
import com.pulumi.grafana.outputs.DataSourceSecureJsonData;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * * [Official documentation](https://grafana.com/docs/grafana/latest/datasources/)
 * * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/data_source/)
 * 
 * The required arguments for this resource vary depending on the type of data
 * source selected (via the &#39;type&#39; argument).
 * 
 * ## Example Usage
 * ```java
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.grafana.DataSource;
 * import com.pulumi.grafana.DataSourceArgs;
 * import static com.pulumi.codegen.internal.Serialization.*;
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
 *         var arbitrary_data = new DataSource(&#34;arbitrary-data&#34;, DataSourceArgs.builder()        
 *             .type(&#34;stackdriver&#34;)
 *             .jsonDataEncoded(serializeJson(
 *                 jsonObject(
 *                     jsonProperty(&#34;tokenUri&#34;, &#34;https://oauth2.googleapis.com/token&#34;),
 *                     jsonProperty(&#34;authenticationType&#34;, &#34;jwt&#34;),
 *                     jsonProperty(&#34;defaultProject&#34;, &#34;default-project&#34;),
 *                     jsonProperty(&#34;clientEmail&#34;, &#34;client-email@default-project.iam.gserviceaccount.com&#34;)
 *                 )))
 *             .secureJsonDataEncoded(serializeJson(
 *                 jsonObject(
 *                     jsonProperty(&#34;privateKey&#34;, &#34;&#34;&#34;
 * -----BEGIN PRIVATE KEY-----
 * private-key
 * -----END PRIVATE KEY-----
 *                     &#34;&#34;&#34;)
 *                 )))
 *             .build());
 * 
 *         var influxdb = new DataSource(&#34;influxdb&#34;, DataSourceArgs.builder()        
 *             .type(&#34;influxdb&#34;)
 *             .url(&#34;http://influxdb.example.net:8086/&#34;)
 *             .basicAuthEnabled(true)
 *             .basicAuthUsername(&#34;username&#34;)
 *             .databaseName(influxdb_database.metrics().name())
 *             .jsonDataEncoded(serializeJson(
 *                 jsonObject(
 *                     jsonProperty(&#34;authType&#34;, &#34;default&#34;),
 *                     jsonProperty(&#34;basicAuthPassword&#34;, &#34;mypassword&#34;)
 *                 )))
 *             .build());
 * 
 *         var cloudwatch = new DataSource(&#34;cloudwatch&#34;, DataSourceArgs.builder()        
 *             .type(&#34;cloudwatch&#34;)
 *             .jsonDataEncoded(serializeJson(
 *                 jsonObject(
 *                     jsonProperty(&#34;defaultRegion&#34;, &#34;us-east-1&#34;),
 *                     jsonProperty(&#34;authType&#34;, &#34;keys&#34;)
 *                 )))
 *             .secureJsonDataEncoded(serializeJson(
 *                 jsonObject(
 *                     jsonProperty(&#34;accessKey&#34;, &#34;123&#34;),
 *                     jsonProperty(&#34;secretKey&#34;, &#34;456&#34;)
 *                 )))
 *             .build());
 * 
 *         var prometheus = new DataSource(&#34;prometheus&#34;, DataSourceArgs.builder()        
 *             .type(&#34;prometheus&#34;)
 *             .url(&#34;https://my-instances.com&#34;)
 *             .basicAuthEnabled(true)
 *             .basicAuthUsername(&#34;username&#34;)
 *             .jsonDataEncoded(serializeJson(
 *                 jsonObject(
 *                     jsonProperty(&#34;httpMethod&#34;, &#34;POST&#34;),
 *                     jsonProperty(&#34;prometheusType&#34;, &#34;Mimir&#34;),
 *                     jsonProperty(&#34;prometheusVersion&#34;, &#34;2.4.0&#34;)
 *                 )))
 *             .secureJsonDataEncoded(serializeJson(
 *                 jsonObject(
 *                     jsonProperty(&#34;basicAuthPassword&#34;, &#34;password&#34;)
 *                 )))
 *             .build());
 * 
 *     }
 * }
 * ```
 * 
 * ## Import
 * 
 * ```sh
 *  $ pulumi import grafana:index/dataSource:DataSource by_integer_id {{datasource id}}
 * ```
 * 
 * ```sh
 *  $ pulumi import grafana:index/dataSource:DataSource by_uid {{datasource uid}}
 * ```
 * 
 */
@ResourceType(type="grafana:index/dataSource:DataSource")
public class DataSource extends com.pulumi.resources.CustomResource {
    /**
     * The method by which Grafana will access the data source: `proxy` or `direct`. Defaults to `proxy`.
     * 
     */
    @Export(name="accessMode", type=String.class, parameters={})
    private Output</* @Nullable */ String> accessMode;

    /**
     * @return The method by which Grafana will access the data source: `proxy` or `direct`. Defaults to `proxy`.
     * 
     */
    public Output<Optional<String>> accessMode() {
        return Codegen.optional(this.accessMode);
    }
    /**
     * Whether to enable basic auth for the data source. Defaults to `false`.
     * 
     */
    @Export(name="basicAuthEnabled", type=Boolean.class, parameters={})
    private Output</* @Nullable */ Boolean> basicAuthEnabled;

    /**
     * @return Whether to enable basic auth for the data source. Defaults to `false`.
     * 
     */
    public Output<Optional<Boolean>> basicAuthEnabled() {
        return Codegen.optional(this.basicAuthEnabled);
    }
    /**
     * Use secure*json*data_encoded.basicAuthPassword instead. Defaults to ``.
     * 
     * @deprecated
     * Use secure_json_data_encoded.basicAuthPassword instead.
     * 
     */
    @Deprecated /* Use secure_json_data_encoded.basicAuthPassword instead. */
    @Export(name="basicAuthPassword", type=String.class, parameters={})
    private Output</* @Nullable */ String> basicAuthPassword;

    /**
     * @return Use secure*json*data_encoded.basicAuthPassword instead. Defaults to ``.
     * 
     */
    public Output<Optional<String>> basicAuthPassword() {
        return Codegen.optional(this.basicAuthPassword);
    }
    /**
     * Basic auth username. Defaults to ``.
     * 
     */
    @Export(name="basicAuthUsername", type=String.class, parameters={})
    private Output</* @Nullable */ String> basicAuthUsername;

    /**
     * @return Basic auth username. Defaults to ``.
     * 
     */
    public Output<Optional<String>> basicAuthUsername() {
        return Codegen.optional(this.basicAuthUsername);
    }
    /**
     * (Required by some data source types) The name of the database to use on the selected data source server. Defaults to ``.
     * 
     */
    @Export(name="databaseName", type=String.class, parameters={})
    private Output</* @Nullable */ String> databaseName;

    /**
     * @return (Required by some data source types) The name of the database to use on the selected data source server. Defaults to ``.
     * 
     */
    public Output<Optional<String>> databaseName() {
        return Codegen.optional(this.databaseName);
    }
    /**
     * Custom HTTP headers
     * 
     */
    @Export(name="httpHeaders", type=Map.class, parameters={String.class, String.class})
    private Output</* @Nullable */ Map<String,String>> httpHeaders;

    /**
     * @return Custom HTTP headers
     * 
     */
    public Output<Optional<Map<String,String>>> httpHeaders() {
        return Codegen.optional(this.httpHeaders);
    }
    /**
     * Whether to set the data source as default. This should only be `true` to a single data source. Defaults to `false`.
     * 
     */
    @Export(name="isDefault", type=Boolean.class, parameters={})
    private Output</* @Nullable */ Boolean> isDefault;

    /**
     * @return Whether to set the data source as default. This should only be `true` to a single data source. Defaults to `false`.
     * 
     */
    public Output<Optional<Boolean>> isDefault() {
        return Codegen.optional(this.isDefault);
    }
    /**
     * Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
     * 
     */
    @Export(name="jsonDataEncoded", type=String.class, parameters={})
    private Output</* @Nullable */ String> jsonDataEncoded;

    /**
     * @return Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
     * 
     */
    public Output<Optional<String>> jsonDataEncoded() {
        return Codegen.optional(this.jsonDataEncoded);
    }
    /**
     * Use json*data*encoded instead.
     * 
     * @deprecated
     * Use json_data_encoded instead.
     * 
     */
    @Deprecated /* Use json_data_encoded instead. */
    @Export(name="jsonDatas", type=List.class, parameters={DataSourceJsonData.class})
    private Output</* @Nullable */ List<DataSourceJsonData>> jsonDatas;

    /**
     * @return Use json*data*encoded instead.
     * 
     */
    public Output<Optional<List<DataSourceJsonData>>> jsonDatas() {
        return Codegen.optional(this.jsonDatas);
    }
    /**
     * A unique name for the data source.
     * 
     */
    @Export(name="name", type=String.class, parameters={})
    private Output<String> name;

    /**
     * @return A unique name for the data source.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * Use secure*json*data_encoded.password instead. Defaults to ``.
     * 
     * @deprecated
     * Use secure_json_data_encoded.password instead.
     * 
     */
    @Deprecated /* Use secure_json_data_encoded.password instead. */
    @Export(name="password", type=String.class, parameters={})
    private Output</* @Nullable */ String> password;

    /**
     * @return Use secure*json*data_encoded.password instead. Defaults to ``.
     * 
     */
    public Output<Optional<String>> password() {
        return Codegen.optional(this.password);
    }
    /**
     * Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
     * 
     */
    @Export(name="secureJsonDataEncoded", type=String.class, parameters={})
    private Output</* @Nullable */ String> secureJsonDataEncoded;

    /**
     * @return Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
     * 
     */
    public Output<Optional<String>> secureJsonDataEncoded() {
        return Codegen.optional(this.secureJsonDataEncoded);
    }
    /**
     * Use secure*json*data*encoded instead.
     * 
     * @deprecated
     * Use secure_json_data_encoded instead.
     * 
     */
    @Deprecated /* Use secure_json_data_encoded instead. */
    @Export(name="secureJsonDatas", type=List.class, parameters={DataSourceSecureJsonData.class})
    private Output</* @Nullable */ List<DataSourceSecureJsonData>> secureJsonDatas;

    /**
     * @return Use secure*json*data*encoded instead.
     * 
     */
    public Output<Optional<List<DataSourceSecureJsonData>>> secureJsonDatas() {
        return Codegen.optional(this.secureJsonDatas);
    }
    /**
     * The data source type. Must be one of the supported data source keywords.
     * 
     */
    @Export(name="type", type=String.class, parameters={})
    private Output<String> type;

    /**
     * @return The data source type. Must be one of the supported data source keywords.
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
     * The URL for the data source. The type of URL required varies depending on the chosen data source type.
     * 
     */
    @Export(name="url", type=String.class, parameters={})
    private Output</* @Nullable */ String> url;

    /**
     * @return The URL for the data source. The type of URL required varies depending on the chosen data source type.
     * 
     */
    public Output<Optional<String>> url() {
        return Codegen.optional(this.url);
    }
    /**
     * (Required by some data source types) The username to use to authenticate to the data source. Defaults to ``.
     * 
     */
    @Export(name="username", type=String.class, parameters={})
    private Output</* @Nullable */ String> username;

    /**
     * @return (Required by some data source types) The username to use to authenticate to the data source. Defaults to ``.
     * 
     */
    public Output<Optional<String>> username() {
        return Codegen.optional(this.username);
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public DataSource(String name) {
        this(name, DataSourceArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public DataSource(String name, DataSourceArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public DataSource(String name, DataSourceArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/dataSource:DataSource", name, args == null ? DataSourceArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private DataSource(String name, Output<String> id, @Nullable DataSourceState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/dataSource:DataSource", name, state, makeResourceOptions(options, id));
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .additionalSecretOutputs(List.of(
                "basicAuthPassword",
                "httpHeaders",
                "password",
                "secureJsonDataEncoded",
                "secureJsonDatas"
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
    public static DataSource get(String name, Output<String> id, @Nullable DataSourceState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new DataSource(name, id, state, options);
    }
}
