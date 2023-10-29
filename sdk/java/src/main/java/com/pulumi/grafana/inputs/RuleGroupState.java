// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.grafana.inputs.RuleGroupRuleArgs;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class RuleGroupState extends com.pulumi.resources.ResourceArgs {

    public static final RuleGroupState Empty = new RuleGroupState();

    /**
     * The UID of the folder that the group belongs to.
     * 
     */
    @Import(name="folderUid")
    private @Nullable Output<String> folderUid;

    /**
     * @return The UID of the folder that the group belongs to.
     * 
     */
    public Optional<Output<String>> folderUid() {
        return Optional.ofNullable(this.folderUid);
    }

    /**
     * The interval, in seconds, at which all rules in the group are evaluated. If a group contains many rules, the rules are evaluated sequentially.
     * 
     */
    @Import(name="intervalSeconds")
    private @Nullable Output<Integer> intervalSeconds;

    /**
     * @return The interval, in seconds, at which all rules in the group are evaluated. If a group contains many rules, the rules are evaluated sequentially.
     * 
     */
    public Optional<Output<Integer>> intervalSeconds() {
        return Optional.ofNullable(this.intervalSeconds);
    }

    /**
     * The name of the alert rule.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The name of the alert rule.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The ID of the org to which the group belongs.
     * 
     */
    @Import(name="orgId")
    private @Nullable Output<String> orgId;

    /**
     * @return The ID of the org to which the group belongs.
     * 
     */
    public Optional<Output<String>> orgId() {
        return Optional.ofNullable(this.orgId);
    }

    /**
     * The rules within the group.
     * 
     */
    @Import(name="rules")
    private @Nullable Output<List<RuleGroupRuleArgs>> rules;

    /**
     * @return The rules within the group.
     * 
     */
    public Optional<Output<List<RuleGroupRuleArgs>>> rules() {
        return Optional.ofNullable(this.rules);
    }

    private RuleGroupState() {}

    private RuleGroupState(RuleGroupState $) {
        this.folderUid = $.folderUid;
        this.intervalSeconds = $.intervalSeconds;
        this.name = $.name;
        this.orgId = $.orgId;
        this.rules = $.rules;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(RuleGroupState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private RuleGroupState $;

        public Builder() {
            $ = new RuleGroupState();
        }

        public Builder(RuleGroupState defaults) {
            $ = new RuleGroupState(Objects.requireNonNull(defaults));
        }

        /**
         * @param folderUid The UID of the folder that the group belongs to.
         * 
         * @return builder
         * 
         */
        public Builder folderUid(@Nullable Output<String> folderUid) {
            $.folderUid = folderUid;
            return this;
        }

        /**
         * @param folderUid The UID of the folder that the group belongs to.
         * 
         * @return builder
         * 
         */
        public Builder folderUid(String folderUid) {
            return folderUid(Output.of(folderUid));
        }

        /**
         * @param intervalSeconds The interval, in seconds, at which all rules in the group are evaluated. If a group contains many rules, the rules are evaluated sequentially.
         * 
         * @return builder
         * 
         */
        public Builder intervalSeconds(@Nullable Output<Integer> intervalSeconds) {
            $.intervalSeconds = intervalSeconds;
            return this;
        }

        /**
         * @param intervalSeconds The interval, in seconds, at which all rules in the group are evaluated. If a group contains many rules, the rules are evaluated sequentially.
         * 
         * @return builder
         * 
         */
        public Builder intervalSeconds(Integer intervalSeconds) {
            return intervalSeconds(Output.of(intervalSeconds));
        }

        /**
         * @param name The name of the alert rule.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the alert rule.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param orgId The ID of the org to which the group belongs.
         * 
         * @return builder
         * 
         */
        public Builder orgId(@Nullable Output<String> orgId) {
            $.orgId = orgId;
            return this;
        }

        /**
         * @param orgId The ID of the org to which the group belongs.
         * 
         * @return builder
         * 
         */
        public Builder orgId(String orgId) {
            return orgId(Output.of(orgId));
        }

        /**
         * @param rules The rules within the group.
         * 
         * @return builder
         * 
         */
        public Builder rules(@Nullable Output<List<RuleGroupRuleArgs>> rules) {
            $.rules = rules;
            return this;
        }

        /**
         * @param rules The rules within the group.
         * 
         * @return builder
         * 
         */
        public Builder rules(List<RuleGroupRuleArgs> rules) {
            return rules(Output.of(rules));
        }

        /**
         * @param rules The rules within the group.
         * 
         * @return builder
         * 
         */
        public Builder rules(RuleGroupRuleArgs... rules) {
            return rules(List.of(rules));
        }

        public RuleGroupState build() {
            return $;
        }
    }

}
