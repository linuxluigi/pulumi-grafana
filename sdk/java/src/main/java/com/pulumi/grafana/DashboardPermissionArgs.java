// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.grafana.inputs.DashboardPermissionPermissionArgs;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DashboardPermissionArgs extends com.pulumi.resources.ResourceArgs {

    public static final DashboardPermissionArgs Empty = new DashboardPermissionArgs();

    /**
     * ID of the dashboard to apply permissions to. Deprecated: use `dashboard_uid` instead.
     * 
     * @deprecated
     * use `dashboard_uid` instead
     * 
     */
    @Deprecated /* use `dashboard_uid` instead */
    @Import(name="dashboardId")
    private @Nullable Output<Integer> dashboardId;

    /**
     * @return ID of the dashboard to apply permissions to. Deprecated: use `dashboard_uid` instead.
     * 
     * @deprecated
     * use `dashboard_uid` instead
     * 
     */
    @Deprecated /* use `dashboard_uid` instead */
    public Optional<Output<Integer>> dashboardId() {
        return Optional.ofNullable(this.dashboardId);
    }

    /**
     * UID of the dashboard to apply permissions to.
     * 
     */
    @Import(name="dashboardUid")
    private @Nullable Output<String> dashboardUid;

    /**
     * @return UID of the dashboard to apply permissions to.
     * 
     */
    public Optional<Output<String>> dashboardUid() {
        return Optional.ofNullable(this.dashboardUid);
    }

    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     * 
     */
    @Import(name="orgId")
    private @Nullable Output<String> orgId;

    /**
     * @return The Organization ID. If not set, the Org ID defined in the provider block will be used.
     * 
     */
    public Optional<Output<String>> orgId() {
        return Optional.ofNullable(this.orgId);
    }

    /**
     * The permission items to add/update. Items that are omitted from the list will be removed.
     * 
     */
    @Import(name="permissions", required=true)
    private Output<List<DashboardPermissionPermissionArgs>> permissions;

    /**
     * @return The permission items to add/update. Items that are omitted from the list will be removed.
     * 
     */
    public Output<List<DashboardPermissionPermissionArgs>> permissions() {
        return this.permissions;
    }

    private DashboardPermissionArgs() {}

    private DashboardPermissionArgs(DashboardPermissionArgs $) {
        this.dashboardId = $.dashboardId;
        this.dashboardUid = $.dashboardUid;
        this.orgId = $.orgId;
        this.permissions = $.permissions;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DashboardPermissionArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DashboardPermissionArgs $;

        public Builder() {
            $ = new DashboardPermissionArgs();
        }

        public Builder(DashboardPermissionArgs defaults) {
            $ = new DashboardPermissionArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param dashboardId ID of the dashboard to apply permissions to. Deprecated: use `dashboard_uid` instead.
         * 
         * @return builder
         * 
         * @deprecated
         * use `dashboard_uid` instead
         * 
         */
        @Deprecated /* use `dashboard_uid` instead */
        public Builder dashboardId(@Nullable Output<Integer> dashboardId) {
            $.dashboardId = dashboardId;
            return this;
        }

        /**
         * @param dashboardId ID of the dashboard to apply permissions to. Deprecated: use `dashboard_uid` instead.
         * 
         * @return builder
         * 
         * @deprecated
         * use `dashboard_uid` instead
         * 
         */
        @Deprecated /* use `dashboard_uid` instead */
        public Builder dashboardId(Integer dashboardId) {
            return dashboardId(Output.of(dashboardId));
        }

        /**
         * @param dashboardUid UID of the dashboard to apply permissions to.
         * 
         * @return builder
         * 
         */
        public Builder dashboardUid(@Nullable Output<String> dashboardUid) {
            $.dashboardUid = dashboardUid;
            return this;
        }

        /**
         * @param dashboardUid UID of the dashboard to apply permissions to.
         * 
         * @return builder
         * 
         */
        public Builder dashboardUid(String dashboardUid) {
            return dashboardUid(Output.of(dashboardUid));
        }

        /**
         * @param orgId The Organization ID. If not set, the Org ID defined in the provider block will be used.
         * 
         * @return builder
         * 
         */
        public Builder orgId(@Nullable Output<String> orgId) {
            $.orgId = orgId;
            return this;
        }

        /**
         * @param orgId The Organization ID. If not set, the Org ID defined in the provider block will be used.
         * 
         * @return builder
         * 
         */
        public Builder orgId(String orgId) {
            return orgId(Output.of(orgId));
        }

        /**
         * @param permissions The permission items to add/update. Items that are omitted from the list will be removed.
         * 
         * @return builder
         * 
         */
        public Builder permissions(Output<List<DashboardPermissionPermissionArgs>> permissions) {
            $.permissions = permissions;
            return this;
        }

        /**
         * @param permissions The permission items to add/update. Items that are omitted from the list will be removed.
         * 
         * @return builder
         * 
         */
        public Builder permissions(List<DashboardPermissionPermissionArgs> permissions) {
            return permissions(Output.of(permissions));
        }

        /**
         * @param permissions The permission items to add/update. Items that are omitted from the list will be removed.
         * 
         * @return builder
         * 
         */
        public Builder permissions(DashboardPermissionPermissionArgs... permissions) {
            return permissions(List.of(permissions));
        }

        public DashboardPermissionArgs build() {
            $.permissions = Objects.requireNonNull($.permissions, "expected parameter 'permissions' to be non-null");
            return $;
        }
    }

}
