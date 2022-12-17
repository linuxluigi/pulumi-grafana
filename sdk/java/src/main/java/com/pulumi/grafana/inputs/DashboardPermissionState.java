// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.grafana.inputs.DashboardPermissionPermissionArgs;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DashboardPermissionState extends com.pulumi.resources.ResourceArgs {

    public static final DashboardPermissionState Empty = new DashboardPermissionState();

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
     * The permission items to add/update. Items that are omitted from the list will be removed.
     * 
     */
    @Import(name="permissions")
    private @Nullable Output<List<DashboardPermissionPermissionArgs>> permissions;

    /**
     * @return The permission items to add/update. Items that are omitted from the list will be removed.
     * 
     */
    public Optional<Output<List<DashboardPermissionPermissionArgs>>> permissions() {
        return Optional.ofNullable(this.permissions);
    }

    private DashboardPermissionState() {}

    private DashboardPermissionState(DashboardPermissionState $) {
        this.dashboardId = $.dashboardId;
        this.dashboardUid = $.dashboardUid;
        this.permissions = $.permissions;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DashboardPermissionState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DashboardPermissionState $;

        public Builder() {
            $ = new DashboardPermissionState();
        }

        public Builder(DashboardPermissionState defaults) {
            $ = new DashboardPermissionState(Objects.requireNonNull(defaults));
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
         * @param permissions The permission items to add/update. Items that are omitted from the list will be removed.
         * 
         * @return builder
         * 
         */
        public Builder permissions(@Nullable Output<List<DashboardPermissionPermissionArgs>> permissions) {
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

        public DashboardPermissionState build() {
            return $;
        }
    }

}
