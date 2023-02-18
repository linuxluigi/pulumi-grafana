// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.grafana.outputs.RuleGroupRuleData;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class RuleGroupRule {
    /**
     * @return Key-value pairs of metadata to attach to the alert rule that may add user-defined context, but cannot be used for matching, grouping, or routing. Defaults to `map[]`.
     * 
     */
    private @Nullable Map<String,String> annotations;
    /**
     * @return The `ref_id` of the query node in the `data` field to use as the alert condition.
     * 
     */
    private String condition;
    /**
     * @return A sequence of stages that describe the contents of the rule.
     * 
     */
    private List<RuleGroupRuleData> datas;
    /**
     * @return Describes what state to enter when the rule&#39;s query is invalid and the rule cannot be executed. Options are OK, Error, and Alerting. Defaults to `Alerting`.
     * 
     */
    private @Nullable String execErrState;
    /**
     * @return The amount of time for which the rule must be breached for the rule to be considered to be Firing. Before this time has elapsed, the rule is only considered to be Pending. Defaults to `0`.
     * 
     */
    private @Nullable String for_;
    /**
     * @return Sets whether the alert should be paused or not. Defaults to `false`.
     * 
     */
    private @Nullable Boolean isPaused;
    /**
     * @return Key-value pairs to attach to the alert rule that can be used in matching, grouping, and routing. Defaults to `map[]`.
     * 
     */
    private @Nullable Map<String,String> labels;
    /**
     * @return The name of the alert rule.
     * 
     */
    private String name;
    /**
     * @return Describes what state to enter when the rule&#39;s query returns No Data. Options are OK, NoData, and Alerting. Defaults to `NoData`.
     * 
     */
    private @Nullable String noDataState;
    /**
     * @return The unique identifier of the alert rule.
     * 
     */
    private @Nullable String uid;

    private RuleGroupRule() {}
    /**
     * @return Key-value pairs of metadata to attach to the alert rule that may add user-defined context, but cannot be used for matching, grouping, or routing. Defaults to `map[]`.
     * 
     */
    public Map<String,String> annotations() {
        return this.annotations == null ? Map.of() : this.annotations;
    }
    /**
     * @return The `ref_id` of the query node in the `data` field to use as the alert condition.
     * 
     */
    public String condition() {
        return this.condition;
    }
    /**
     * @return A sequence of stages that describe the contents of the rule.
     * 
     */
    public List<RuleGroupRuleData> datas() {
        return this.datas;
    }
    /**
     * @return Describes what state to enter when the rule&#39;s query is invalid and the rule cannot be executed. Options are OK, Error, and Alerting. Defaults to `Alerting`.
     * 
     */
    public Optional<String> execErrState() {
        return Optional.ofNullable(this.execErrState);
    }
    /**
     * @return The amount of time for which the rule must be breached for the rule to be considered to be Firing. Before this time has elapsed, the rule is only considered to be Pending. Defaults to `0`.
     * 
     */
    public Optional<String> for_() {
        return Optional.ofNullable(this.for_);
    }
    /**
     * @return Sets whether the alert should be paused or not. Defaults to `false`.
     * 
     */
    public Optional<Boolean> isPaused() {
        return Optional.ofNullable(this.isPaused);
    }
    /**
     * @return Key-value pairs to attach to the alert rule that can be used in matching, grouping, and routing. Defaults to `map[]`.
     * 
     */
    public Map<String,String> labels() {
        return this.labels == null ? Map.of() : this.labels;
    }
    /**
     * @return The name of the alert rule.
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return Describes what state to enter when the rule&#39;s query returns No Data. Options are OK, NoData, and Alerting. Defaults to `NoData`.
     * 
     */
    public Optional<String> noDataState() {
        return Optional.ofNullable(this.noDataState);
    }
    /**
     * @return The unique identifier of the alert rule.
     * 
     */
    public Optional<String> uid() {
        return Optional.ofNullable(this.uid);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(RuleGroupRule defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Map<String,String> annotations;
        private String condition;
        private List<RuleGroupRuleData> datas;
        private @Nullable String execErrState;
        private @Nullable String for_;
        private @Nullable Boolean isPaused;
        private @Nullable Map<String,String> labels;
        private String name;
        private @Nullable String noDataState;
        private @Nullable String uid;
        public Builder() {}
        public Builder(RuleGroupRule defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.annotations = defaults.annotations;
    	      this.condition = defaults.condition;
    	      this.datas = defaults.datas;
    	      this.execErrState = defaults.execErrState;
    	      this.for_ = defaults.for_;
    	      this.isPaused = defaults.isPaused;
    	      this.labels = defaults.labels;
    	      this.name = defaults.name;
    	      this.noDataState = defaults.noDataState;
    	      this.uid = defaults.uid;
        }

        @CustomType.Setter
        public Builder annotations(@Nullable Map<String,String> annotations) {
            this.annotations = annotations;
            return this;
        }
        @CustomType.Setter
        public Builder condition(String condition) {
            this.condition = Objects.requireNonNull(condition);
            return this;
        }
        @CustomType.Setter
        public Builder datas(List<RuleGroupRuleData> datas) {
            this.datas = Objects.requireNonNull(datas);
            return this;
        }
        public Builder datas(RuleGroupRuleData... datas) {
            return datas(List.of(datas));
        }
        @CustomType.Setter
        public Builder execErrState(@Nullable String execErrState) {
            this.execErrState = execErrState;
            return this;
        }
        @CustomType.Setter("for")
        public Builder for_(@Nullable String for_) {
            this.for_ = for_;
            return this;
        }
        @CustomType.Setter
        public Builder isPaused(@Nullable Boolean isPaused) {
            this.isPaused = isPaused;
            return this;
        }
        @CustomType.Setter
        public Builder labels(@Nullable Map<String,String> labels) {
            this.labels = labels;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            this.name = Objects.requireNonNull(name);
            return this;
        }
        @CustomType.Setter
        public Builder noDataState(@Nullable String noDataState) {
            this.noDataState = noDataState;
            return this;
        }
        @CustomType.Setter
        public Builder uid(@Nullable String uid) {
            this.uid = uid;
            return this;
        }
        public RuleGroupRule build() {
            final var o = new RuleGroupRule();
            o.annotations = annotations;
            o.condition = condition;
            o.datas = datas;
            o.execErrState = execErrState;
            o.for_ = for_;
            o.isPaused = isPaused;
            o.labels = labels;
            o.name = name;
            o.noDataState = noDataState;
            o.uid = uid;
            return o;
        }
    }
}
