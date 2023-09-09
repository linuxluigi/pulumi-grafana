// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DataSourcePermissionPermissionArgs extends com.pulumi.resources.ResourceArgs {

    public static final DataSourcePermissionPermissionArgs Empty = new DataSourcePermissionPermissionArgs();

    /**
     * Name of the basic role to manage permissions for. Options: `Viewer`, `Editor` or `Admin`. Can only be set from Grafana v9.2.3+. Defaults to ``.
     * 
     */
    @Import(name="builtInRole")
    private @Nullable Output<String> builtInRole;

    /**
     * @return Name of the basic role to manage permissions for. Options: `Viewer`, `Editor` or `Admin`. Can only be set from Grafana v9.2.3+. Defaults to ``.
     * 
     */
    public Optional<Output<String>> builtInRole() {
        return Optional.ofNullable(this.builtInRole);
    }

    /**
     * Permission to associate with item. Options: `Query` or `Edit` (`Edit` can only be used with Grafana v9.2.3+).
     * 
     */
    @Import(name="permission", required=true)
    private Output<String> permission;

    /**
     * @return Permission to associate with item. Options: `Query` or `Edit` (`Edit` can only be used with Grafana v9.2.3+).
     * 
     */
    public Output<String> permission() {
        return this.permission;
    }

    /**
     * ID of the team to manage permissions for. Defaults to `0`.
     * 
     */
    @Import(name="teamId")
    private @Nullable Output<String> teamId;

    /**
     * @return ID of the team to manage permissions for. Defaults to `0`.
     * 
     */
    public Optional<Output<String>> teamId() {
        return Optional.ofNullable(this.teamId);
    }

    /**
     * ID of the user to manage permissions for. Defaults to `0`.
     * 
     */
    @Import(name="userId")
    private @Nullable Output<Integer> userId;

    /**
     * @return ID of the user to manage permissions for. Defaults to `0`.
     * 
     */
    public Optional<Output<Integer>> userId() {
        return Optional.ofNullable(this.userId);
    }

    private DataSourcePermissionPermissionArgs() {}

    private DataSourcePermissionPermissionArgs(DataSourcePermissionPermissionArgs $) {
        this.builtInRole = $.builtInRole;
        this.permission = $.permission;
        this.teamId = $.teamId;
        this.userId = $.userId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DataSourcePermissionPermissionArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DataSourcePermissionPermissionArgs $;

        public Builder() {
            $ = new DataSourcePermissionPermissionArgs();
        }

        public Builder(DataSourcePermissionPermissionArgs defaults) {
            $ = new DataSourcePermissionPermissionArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param builtInRole Name of the basic role to manage permissions for. Options: `Viewer`, `Editor` or `Admin`. Can only be set from Grafana v9.2.3+. Defaults to ``.
         * 
         * @return builder
         * 
         */
        public Builder builtInRole(@Nullable Output<String> builtInRole) {
            $.builtInRole = builtInRole;
            return this;
        }

        /**
         * @param builtInRole Name of the basic role to manage permissions for. Options: `Viewer`, `Editor` or `Admin`. Can only be set from Grafana v9.2.3+. Defaults to ``.
         * 
         * @return builder
         * 
         */
        public Builder builtInRole(String builtInRole) {
            return builtInRole(Output.of(builtInRole));
        }

        /**
         * @param permission Permission to associate with item. Options: `Query` or `Edit` (`Edit` can only be used with Grafana v9.2.3+).
         * 
         * @return builder
         * 
         */
        public Builder permission(Output<String> permission) {
            $.permission = permission;
            return this;
        }

        /**
         * @param permission Permission to associate with item. Options: `Query` or `Edit` (`Edit` can only be used with Grafana v9.2.3+).
         * 
         * @return builder
         * 
         */
        public Builder permission(String permission) {
            return permission(Output.of(permission));
        }

        /**
         * @param teamId ID of the team to manage permissions for. Defaults to `0`.
         * 
         * @return builder
         * 
         */
        public Builder teamId(@Nullable Output<String> teamId) {
            $.teamId = teamId;
            return this;
        }

        /**
         * @param teamId ID of the team to manage permissions for. Defaults to `0`.
         * 
         * @return builder
         * 
         */
        public Builder teamId(String teamId) {
            return teamId(Output.of(teamId));
        }

        /**
         * @param userId ID of the user to manage permissions for. Defaults to `0`.
         * 
         * @return builder
         * 
         */
        public Builder userId(@Nullable Output<Integer> userId) {
            $.userId = userId;
            return this;
        }

        /**
         * @param userId ID of the user to manage permissions for. Defaults to `0`.
         * 
         * @return builder
         * 
         */
        public Builder userId(Integer userId) {
            return userId(Output.of(userId));
        }

        public DataSourcePermissionPermissionArgs build() {
            $.permission = Objects.requireNonNull($.permission, "expected parameter 'permission' to be non-null");
            return $;
        }
    }

}
