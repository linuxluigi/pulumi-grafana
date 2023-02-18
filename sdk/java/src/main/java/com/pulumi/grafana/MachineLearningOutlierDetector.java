// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.grafana.MachineLearningOutlierDetectorArgs;
import com.pulumi.grafana.Utilities;
import com.pulumi.grafana.inputs.MachineLearningOutlierDetectorState;
import com.pulumi.grafana.outputs.MachineLearningOutlierDetectorAlgorithm;
import java.lang.Integer;
import java.lang.Object;
import java.lang.String;
import java.util.Map;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * An outlier detector monitors the results of a query and reports when its values are outside normal bands.
 * 
 * The normal band is configured by choice of algorithm, its sensitivity and other configuration.
 * 
 * Visit https://grafana.com/docs/grafana-cloud/machine-learning/outlier-detection/ for more details.
 * 
 */
@ResourceType(type="grafana:index/machineLearningOutlierDetector:MachineLearningOutlierDetector")
public class MachineLearningOutlierDetector extends com.pulumi.resources.CustomResource {
    /**
     * The algorithm to use and its configuration. See https://grafana.com/docs/grafana-cloud/machine-learning/outlier-detection/ for details.
     * 
     */
    @Export(name="algorithm", type=MachineLearningOutlierDetectorAlgorithm.class, parameters={})
    private Output<MachineLearningOutlierDetectorAlgorithm> algorithm;

    /**
     * @return The algorithm to use and its configuration. See https://grafana.com/docs/grafana-cloud/machine-learning/outlier-detection/ for details.
     * 
     */
    public Output<MachineLearningOutlierDetectorAlgorithm> algorithm() {
        return this.algorithm;
    }
    /**
     * The id of the datasource to query.
     * 
     */
    @Export(name="datasourceId", type=Integer.class, parameters={})
    private Output</* @Nullable */ Integer> datasourceId;

    /**
     * @return The id of the datasource to query.
     * 
     */
    public Output<Optional<Integer>> datasourceId() {
        return Codegen.optional(this.datasourceId);
    }
    /**
     * The type of datasource being queried. Currently allowed values are prometheus, graphite, loki, postgres, and datadog.
     * 
     */
    @Export(name="datasourceType", type=String.class, parameters={})
    private Output<String> datasourceType;

    /**
     * @return The type of datasource being queried. Currently allowed values are prometheus, graphite, loki, postgres, and datadog.
     * 
     */
    public Output<String> datasourceType() {
        return this.datasourceType;
    }
    /**
     * The uid of the datasource to query.
     * 
     */
    @Export(name="datasourceUid", type=String.class, parameters={})
    private Output</* @Nullable */ String> datasourceUid;

    /**
     * @return The uid of the datasource to query.
     * 
     */
    public Output<Optional<String>> datasourceUid() {
        return Codegen.optional(this.datasourceUid);
    }
    /**
     * A description of the outlier detector.
     * 
     */
    @Export(name="description", type=String.class, parameters={})
    private Output</* @Nullable */ String> description;

    /**
     * @return A description of the outlier detector.
     * 
     */
    public Output<Optional<String>> description() {
        return Codegen.optional(this.description);
    }
    /**
     * The data interval in seconds to monitor. Defaults to `300`.
     * 
     */
    @Export(name="interval", type=Integer.class, parameters={})
    private Output</* @Nullable */ Integer> interval;

    /**
     * @return The data interval in seconds to monitor. Defaults to `300`.
     * 
     */
    public Output<Optional<Integer>> interval() {
        return Codegen.optional(this.interval);
    }
    /**
     * The metric used to query the outlier detector results.
     * 
     */
    @Export(name="metric", type=String.class, parameters={})
    private Output<String> metric;

    /**
     * @return The metric used to query the outlier detector results.
     * 
     */
    public Output<String> metric() {
        return this.metric;
    }
    /**
     * The name of the outlier detector.
     * 
     */
    @Export(name="name", type=String.class, parameters={})
    private Output<String> name;

    /**
     * @return The name of the outlier detector.
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * An object representing the query params to query Grafana with.
     * 
     */
    @Export(name="queryParams", type=Map.class, parameters={String.class, Object.class})
    private Output<Map<String,Object>> queryParams;

    /**
     * @return An object representing the query params to query Grafana with.
     * 
     */
    public Output<Map<String,Object>> queryParams() {
        return this.queryParams;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public MachineLearningOutlierDetector(String name) {
        this(name, MachineLearningOutlierDetectorArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public MachineLearningOutlierDetector(String name, MachineLearningOutlierDetectorArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public MachineLearningOutlierDetector(String name, MachineLearningOutlierDetectorArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/machineLearningOutlierDetector:MachineLearningOutlierDetector", name, args == null ? MachineLearningOutlierDetectorArgs.Empty : args, makeResourceOptions(options, Codegen.empty()));
    }

    private MachineLearningOutlierDetector(String name, Output<String> id, @Nullable MachineLearningOutlierDetectorState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("grafana:index/machineLearningOutlierDetector:MachineLearningOutlierDetector", name, state, makeResourceOptions(options, id));
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
    public static MachineLearningOutlierDetector get(String name, Output<String> id, @Nullable MachineLearningOutlierDetectorState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new MachineLearningOutlierDetector(name, id, state, options);
    }
}
