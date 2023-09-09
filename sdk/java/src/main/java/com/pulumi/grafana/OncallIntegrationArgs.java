// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.grafana.inputs.OncallIntegrationDefaultRouteArgs;
import com.pulumi.grafana.inputs.OncallIntegrationTemplatesArgs;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class OncallIntegrationArgs extends com.pulumi.resources.ResourceArgs {

    public static final OncallIntegrationArgs Empty = new OncallIntegrationArgs();

    /**
     * The Default route for all alerts from the given integration
     * 
     */
    @Import(name="defaultRoute", required=true)
    private Output<OncallIntegrationDefaultRouteArgs> defaultRoute;

    /**
     * @return The Default route for all alerts from the given integration
     * 
     */
    public Output<OncallIntegrationDefaultRouteArgs> defaultRoute() {
        return this.defaultRoute;
    }

    /**
     * The name of the service integration.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The name of the service integration.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `grafana.getOncallTeam` datasource.
     * 
     */
    @Import(name="teamId")
    private @Nullable Output<String> teamId;

    /**
     * @return The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `grafana.getOncallTeam` datasource.
     * 
     */
    public Optional<Output<String>> teamId() {
        return Optional.ofNullable(this.teamId);
    }

    /**
     * Jinja2 templates for Alert payload.
     * 
     */
    @Import(name="templates")
    private @Nullable Output<OncallIntegrationTemplatesArgs> templates;

    /**
     * @return Jinja2 templates for Alert payload.
     * 
     */
    public Optional<Output<OncallIntegrationTemplatesArgs>> templates() {
        return Optional.ofNullable(this.templates);
    }

    /**
     * The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging.
     * 
     */
    @Import(name="type", required=true)
    private Output<String> type;

    /**
     * @return The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging.
     * 
     */
    public Output<String> type() {
        return this.type;
    }

    private OncallIntegrationArgs() {}

    private OncallIntegrationArgs(OncallIntegrationArgs $) {
        this.defaultRoute = $.defaultRoute;
        this.name = $.name;
        this.teamId = $.teamId;
        this.templates = $.templates;
        this.type = $.type;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(OncallIntegrationArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private OncallIntegrationArgs $;

        public Builder() {
            $ = new OncallIntegrationArgs();
        }

        public Builder(OncallIntegrationArgs defaults) {
            $ = new OncallIntegrationArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param defaultRoute The Default route for all alerts from the given integration
         * 
         * @return builder
         * 
         */
        public Builder defaultRoute(Output<OncallIntegrationDefaultRouteArgs> defaultRoute) {
            $.defaultRoute = defaultRoute;
            return this;
        }

        /**
         * @param defaultRoute The Default route for all alerts from the given integration
         * 
         * @return builder
         * 
         */
        public Builder defaultRoute(OncallIntegrationDefaultRouteArgs defaultRoute) {
            return defaultRoute(Output.of(defaultRoute));
        }

        /**
         * @param name The name of the service integration.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the service integration.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param teamId The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `grafana.getOncallTeam` datasource.
         * 
         * @return builder
         * 
         */
        public Builder teamId(@Nullable Output<String> teamId) {
            $.teamId = teamId;
            return this;
        }

        /**
         * @param teamId The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the `grafana.getOncallTeam` datasource.
         * 
         * @return builder
         * 
         */
        public Builder teamId(String teamId) {
            return teamId(Output.of(teamId));
        }

        /**
         * @param templates Jinja2 templates for Alert payload.
         * 
         * @return builder
         * 
         */
        public Builder templates(@Nullable Output<OncallIntegrationTemplatesArgs> templates) {
            $.templates = templates;
            return this;
        }

        /**
         * @param templates Jinja2 templates for Alert payload.
         * 
         * @return builder
         * 
         */
        public Builder templates(OncallIntegrationTemplatesArgs templates) {
            return templates(Output.of(templates));
        }

        /**
         * @param type The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging.
         * 
         * @return builder
         * 
         */
        public Builder type(Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type The type of integration. Can be grafana, grafana*alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon*sns, curler, sentry, formatted*webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry*platform, zabbix, prtg, slack*channel, inbound*email, direct_paging.
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        public OncallIntegrationArgs build() {
            $.defaultRoute = Objects.requireNonNull($.defaultRoute, "expected parameter 'defaultRoute' to be non-null");
            $.type = Objects.requireNonNull($.type, "expected parameter 'type' to be non-null");
            return $;
        }
    }

}
