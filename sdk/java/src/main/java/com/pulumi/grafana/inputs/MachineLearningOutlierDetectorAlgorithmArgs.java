// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.grafana.inputs.MachineLearningOutlierDetectorAlgorithmConfigArgs;
import java.lang.Double;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class MachineLearningOutlierDetectorAlgorithmArgs extends com.pulumi.resources.ResourceArgs {

    public static final MachineLearningOutlierDetectorAlgorithmArgs Empty = new MachineLearningOutlierDetectorAlgorithmArgs();

    /**
     * For DBSCAN only, specify the configuration map
     * 
     */
    @Import(name="config")
    private @Nullable Output<MachineLearningOutlierDetectorAlgorithmConfigArgs> config;

    /**
     * @return For DBSCAN only, specify the configuration map
     * 
     */
    public Optional<Output<MachineLearningOutlierDetectorAlgorithmConfigArgs>> config() {
        return Optional.ofNullable(this.config);
    }

    /**
     * The name of the algorithm to use (&#39;mad&#39; or &#39;dbscan&#39;).
     * 
     */
    @Import(name="name", required=true)
    private Output<String> name;

    /**
     * @return The name of the algorithm to use (&#39;mad&#39; or &#39;dbscan&#39;).
     * 
     */
    public Output<String> name() {
        return this.name;
    }

    /**
     * Specify the sensitivity of the detector (in range [0,1]).
     * 
     */
    @Import(name="sensitivity", required=true)
    private Output<Double> sensitivity;

    /**
     * @return Specify the sensitivity of the detector (in range [0,1]).
     * 
     */
    public Output<Double> sensitivity() {
        return this.sensitivity;
    }

    private MachineLearningOutlierDetectorAlgorithmArgs() {}

    private MachineLearningOutlierDetectorAlgorithmArgs(MachineLearningOutlierDetectorAlgorithmArgs $) {
        this.config = $.config;
        this.name = $.name;
        this.sensitivity = $.sensitivity;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(MachineLearningOutlierDetectorAlgorithmArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private MachineLearningOutlierDetectorAlgorithmArgs $;

        public Builder() {
            $ = new MachineLearningOutlierDetectorAlgorithmArgs();
        }

        public Builder(MachineLearningOutlierDetectorAlgorithmArgs defaults) {
            $ = new MachineLearningOutlierDetectorAlgorithmArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param config For DBSCAN only, specify the configuration map
         * 
         * @return builder
         * 
         */
        public Builder config(@Nullable Output<MachineLearningOutlierDetectorAlgorithmConfigArgs> config) {
            $.config = config;
            return this;
        }

        /**
         * @param config For DBSCAN only, specify the configuration map
         * 
         * @return builder
         * 
         */
        public Builder config(MachineLearningOutlierDetectorAlgorithmConfigArgs config) {
            return config(Output.of(config));
        }

        /**
         * @param name The name of the algorithm to use (&#39;mad&#39; or &#39;dbscan&#39;).
         * 
         * @return builder
         * 
         */
        public Builder name(Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the algorithm to use (&#39;mad&#39; or &#39;dbscan&#39;).
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param sensitivity Specify the sensitivity of the detector (in range [0,1]).
         * 
         * @return builder
         * 
         */
        public Builder sensitivity(Output<Double> sensitivity) {
            $.sensitivity = sensitivity;
            return this;
        }

        /**
         * @param sensitivity Specify the sensitivity of the detector (in range [0,1]).
         * 
         * @return builder
         * 
         */
        public Builder sensitivity(Double sensitivity) {
            return sensitivity(Output.of(sensitivity));
        }

        public MachineLearningOutlierDetectorAlgorithmArgs build() {
            $.name = Objects.requireNonNull($.name, "expected parameter 'name' to be non-null");
            $.sensitivity = Objects.requireNonNull($.sensitivity, "expected parameter 'sensitivity' to be non-null");
            return $;
        }
    }

}
