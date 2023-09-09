// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class TeamPreferencesArgs extends com.pulumi.resources.ResourceArgs {

    public static final TeamPreferencesArgs Empty = new TeamPreferencesArgs();

    @Import(name="homeDashboardUid")
    private @Nullable Output<String> homeDashboardUid;

    public Optional<Output<String>> homeDashboardUid() {
        return Optional.ofNullable(this.homeDashboardUid);
    }

    @Import(name="theme")
    private @Nullable Output<String> theme;

    public Optional<Output<String>> theme() {
        return Optional.ofNullable(this.theme);
    }

    @Import(name="timezone")
    private @Nullable Output<String> timezone;

    public Optional<Output<String>> timezone() {
        return Optional.ofNullable(this.timezone);
    }

    private TeamPreferencesArgs() {}

    private TeamPreferencesArgs(TeamPreferencesArgs $) {
        this.homeDashboardUid = $.homeDashboardUid;
        this.theme = $.theme;
        this.timezone = $.timezone;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(TeamPreferencesArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private TeamPreferencesArgs $;

        public Builder() {
            $ = new TeamPreferencesArgs();
        }

        public Builder(TeamPreferencesArgs defaults) {
            $ = new TeamPreferencesArgs(Objects.requireNonNull(defaults));
        }

        public Builder homeDashboardUid(@Nullable Output<String> homeDashboardUid) {
            $.homeDashboardUid = homeDashboardUid;
            return this;
        }

        public Builder homeDashboardUid(String homeDashboardUid) {
            return homeDashboardUid(Output.of(homeDashboardUid));
        }

        public Builder theme(@Nullable Output<String> theme) {
            $.theme = theme;
            return this;
        }

        public Builder theme(String theme) {
            return theme(Output.of(theme));
        }

        public Builder timezone(@Nullable Output<String> timezone) {
            $.timezone = timezone;
            return this;
        }

        public Builder timezone(String timezone) {
            return timezone(Output.of(timezone));
        }

        public TeamPreferencesArgs build() {
            return $;
        }
    }

}
