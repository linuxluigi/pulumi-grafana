// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.grafana.inputs.SyntheticMonitoringCheckSettingsArgs;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class SyntheticMonitoringCheckArgs extends com.pulumi.resources.ResourceArgs {

    public static final SyntheticMonitoringCheckArgs Empty = new SyntheticMonitoringCheckArgs();

    /**
     * Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert levels](https://grafana.com/docs/grafana-cloud/monitor-public-endpoints/synthetic-monitoring-alerting/). Defaults to `none`.
     * 
     */
    @Import(name="alertSensitivity")
    private @Nullable Output<String> alertSensitivity;

    /**
     * @return Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert levels](https://grafana.com/docs/grafana-cloud/monitor-public-endpoints/synthetic-monitoring-alerting/). Defaults to `none`.
     * 
     */
    public Optional<Output<String>> alertSensitivity() {
        return Optional.ofNullable(this.alertSensitivity);
    }

    /**
     * Metrics are reduced by default. Set this to `false` if you&#39;d like to publish all metrics. We maintain a [full list of metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each. Defaults to `true`.
     * 
     */
    @Import(name="basicMetricsOnly")
    private @Nullable Output<Boolean> basicMetricsOnly;

    /**
     * @return Metrics are reduced by default. Set this to `false` if you&#39;d like to publish all metrics. We maintain a [full list of metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each. Defaults to `true`.
     * 
     */
    public Optional<Output<Boolean>> basicMetricsOnly() {
        return Optional.ofNullable(this.basicMetricsOnly);
    }

    /**
     * Whether to enable the check. Defaults to `true`.
     * 
     */
    @Import(name="enabled")
    private @Nullable Output<Boolean> enabled;

    /**
     * @return Whether to enable the check. Defaults to `true`.
     * 
     */
    public Optional<Output<Boolean>> enabled() {
        return Optional.ofNullable(this.enabled);
    }

    /**
     * How often the check runs in milliseconds (the value is not truly a &#34;frequency&#34; but a &#34;period&#34;). The minimum acceptable value is 1 second (1000 ms), and the maximum is 120 seconds (120000 ms). Defaults to `60000`.
     * 
     */
    @Import(name="frequency")
    private @Nullable Output<Integer> frequency;

    /**
     * @return How often the check runs in milliseconds (the value is not truly a &#34;frequency&#34; but a &#34;period&#34;). The minimum acceptable value is 1 second (1000 ms), and the maximum is 120 seconds (120000 ms). Defaults to `60000`.
     * 
     */
    public Optional<Output<Integer>> frequency() {
        return Optional.ofNullable(this.frequency);
    }

    /**
     * Name used for job label.
     * 
     */
    @Import(name="job", required=true)
    private Output<String> job;

    /**
     * @return Name used for job label.
     * 
     */
    public Output<String> job() {
        return this.job;
    }

    /**
     * Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of the labels cannot be empty, and the maximum length is 32 bytes.
     * 
     */
    @Import(name="labels")
    private @Nullable Output<Map<String,String>> labels;

    /**
     * @return Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of the labels cannot be empty, and the maximum length is 32 bytes.
     * 
     */
    public Optional<Output<Map<String,String>>> labels() {
        return Optional.ofNullable(this.labels);
    }

    /**
     * List of probe location IDs where this target will be checked from.
     * 
     */
    @Import(name="probes", required=true)
    private Output<List<Integer>> probes;

    /**
     * @return List of probe location IDs where this target will be checked from.
     * 
     */
    public Output<List<Integer>> probes() {
        return this.probes;
    }

    /**
     * Check settings. Should contain exactly one nested block.
     * 
     */
    @Import(name="settings", required=true)
    private Output<SyntheticMonitoringCheckSettingsArgs> settings;

    /**
     * @return Check settings. Should contain exactly one nested block.
     * 
     */
    public Output<SyntheticMonitoringCheckSettingsArgs> settings() {
        return this.settings;
    }

    /**
     * Hostname to ping.
     * 
     */
    @Import(name="target", required=true)
    private Output<String> target;

    /**
     * @return Hostname to ping.
     * 
     */
    public Output<String> target() {
        return this.target;
    }

    /**
     * Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms), and the maximum 10 seconds (10000 ms). Defaults to `3000`.
     * 
     */
    @Import(name="timeout")
    private @Nullable Output<Integer> timeout;

    /**
     * @return Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms), and the maximum 10 seconds (10000 ms). Defaults to `3000`.
     * 
     */
    public Optional<Output<Integer>> timeout() {
        return Optional.ofNullable(this.timeout);
    }

    private SyntheticMonitoringCheckArgs() {}

    private SyntheticMonitoringCheckArgs(SyntheticMonitoringCheckArgs $) {
        this.alertSensitivity = $.alertSensitivity;
        this.basicMetricsOnly = $.basicMetricsOnly;
        this.enabled = $.enabled;
        this.frequency = $.frequency;
        this.job = $.job;
        this.labels = $.labels;
        this.probes = $.probes;
        this.settings = $.settings;
        this.target = $.target;
        this.timeout = $.timeout;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(SyntheticMonitoringCheckArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private SyntheticMonitoringCheckArgs $;

        public Builder() {
            $ = new SyntheticMonitoringCheckArgs();
        }

        public Builder(SyntheticMonitoringCheckArgs defaults) {
            $ = new SyntheticMonitoringCheckArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param alertSensitivity Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert levels](https://grafana.com/docs/grafana-cloud/monitor-public-endpoints/synthetic-monitoring-alerting/). Defaults to `none`.
         * 
         * @return builder
         * 
         */
        public Builder alertSensitivity(@Nullable Output<String> alertSensitivity) {
            $.alertSensitivity = alertSensitivity;
            return this;
        }

        /**
         * @param alertSensitivity Can be set to `none`, `low`, `medium`, or `high` to correspond to the check [alert levels](https://grafana.com/docs/grafana-cloud/monitor-public-endpoints/synthetic-monitoring-alerting/). Defaults to `none`.
         * 
         * @return builder
         * 
         */
        public Builder alertSensitivity(String alertSensitivity) {
            return alertSensitivity(Output.of(alertSensitivity));
        }

        /**
         * @param basicMetricsOnly Metrics are reduced by default. Set this to `false` if you&#39;d like to publish all metrics. We maintain a [full list of metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each. Defaults to `true`.
         * 
         * @return builder
         * 
         */
        public Builder basicMetricsOnly(@Nullable Output<Boolean> basicMetricsOnly) {
            $.basicMetricsOnly = basicMetricsOnly;
            return this;
        }

        /**
         * @param basicMetricsOnly Metrics are reduced by default. Set this to `false` if you&#39;d like to publish all metrics. We maintain a [full list of metrics](https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata) collected for each. Defaults to `true`.
         * 
         * @return builder
         * 
         */
        public Builder basicMetricsOnly(Boolean basicMetricsOnly) {
            return basicMetricsOnly(Output.of(basicMetricsOnly));
        }

        /**
         * @param enabled Whether to enable the check. Defaults to `true`.
         * 
         * @return builder
         * 
         */
        public Builder enabled(@Nullable Output<Boolean> enabled) {
            $.enabled = enabled;
            return this;
        }

        /**
         * @param enabled Whether to enable the check. Defaults to `true`.
         * 
         * @return builder
         * 
         */
        public Builder enabled(Boolean enabled) {
            return enabled(Output.of(enabled));
        }

        /**
         * @param frequency How often the check runs in milliseconds (the value is not truly a &#34;frequency&#34; but a &#34;period&#34;). The minimum acceptable value is 1 second (1000 ms), and the maximum is 120 seconds (120000 ms). Defaults to `60000`.
         * 
         * @return builder
         * 
         */
        public Builder frequency(@Nullable Output<Integer> frequency) {
            $.frequency = frequency;
            return this;
        }

        /**
         * @param frequency How often the check runs in milliseconds (the value is not truly a &#34;frequency&#34; but a &#34;period&#34;). The minimum acceptable value is 1 second (1000 ms), and the maximum is 120 seconds (120000 ms). Defaults to `60000`.
         * 
         * @return builder
         * 
         */
        public Builder frequency(Integer frequency) {
            return frequency(Output.of(frequency));
        }

        /**
         * @param job Name used for job label.
         * 
         * @return builder
         * 
         */
        public Builder job(Output<String> job) {
            $.job = job;
            return this;
        }

        /**
         * @param job Name used for job label.
         * 
         * @return builder
         * 
         */
        public Builder job(String job) {
            return job(Output.of(job));
        }

        /**
         * @param labels Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of the labels cannot be empty, and the maximum length is 32 bytes.
         * 
         * @return builder
         * 
         */
        public Builder labels(@Nullable Output<Map<String,String>> labels) {
            $.labels = labels;
            return this;
        }

        /**
         * @param labels Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of the labels cannot be empty, and the maximum length is 32 bytes.
         * 
         * @return builder
         * 
         */
        public Builder labels(Map<String,String> labels) {
            return labels(Output.of(labels));
        }

        /**
         * @param probes List of probe location IDs where this target will be checked from.
         * 
         * @return builder
         * 
         */
        public Builder probes(Output<List<Integer>> probes) {
            $.probes = probes;
            return this;
        }

        /**
         * @param probes List of probe location IDs where this target will be checked from.
         * 
         * @return builder
         * 
         */
        public Builder probes(List<Integer> probes) {
            return probes(Output.of(probes));
        }

        /**
         * @param probes List of probe location IDs where this target will be checked from.
         * 
         * @return builder
         * 
         */
        public Builder probes(Integer... probes) {
            return probes(List.of(probes));
        }

        /**
         * @param settings Check settings. Should contain exactly one nested block.
         * 
         * @return builder
         * 
         */
        public Builder settings(Output<SyntheticMonitoringCheckSettingsArgs> settings) {
            $.settings = settings;
            return this;
        }

        /**
         * @param settings Check settings. Should contain exactly one nested block.
         * 
         * @return builder
         * 
         */
        public Builder settings(SyntheticMonitoringCheckSettingsArgs settings) {
            return settings(Output.of(settings));
        }

        /**
         * @param target Hostname to ping.
         * 
         * @return builder
         * 
         */
        public Builder target(Output<String> target) {
            $.target = target;
            return this;
        }

        /**
         * @param target Hostname to ping.
         * 
         * @return builder
         * 
         */
        public Builder target(String target) {
            return target(Output.of(target));
        }

        /**
         * @param timeout Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms), and the maximum 10 seconds (10000 ms). Defaults to `3000`.
         * 
         * @return builder
         * 
         */
        public Builder timeout(@Nullable Output<Integer> timeout) {
            $.timeout = timeout;
            return this;
        }

        /**
         * @param timeout Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms), and the maximum 10 seconds (10000 ms). Defaults to `3000`.
         * 
         * @return builder
         * 
         */
        public Builder timeout(Integer timeout) {
            return timeout(Output.of(timeout));
        }

        public SyntheticMonitoringCheckArgs build() {
            $.job = Objects.requireNonNull($.job, "expected parameter 'job' to be non-null");
            $.probes = Objects.requireNonNull($.probes, "expected parameter 'probes' to be non-null");
            $.settings = Objects.requireNonNull($.settings, "expected parameter 'settings' to be non-null");
            $.target = Objects.requireNonNull($.target, "expected parameter 'target' to be non-null");
            return $;
        }
    }

}
