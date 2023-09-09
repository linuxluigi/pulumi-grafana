// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetDataSourcePlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetDataSourcePlainArgs Empty = new GetDataSourcePlainArgs();

    /**
     * The ID of this resource.
     * 
     */
    @Import(name="id")
    private @Nullable String id;

    /**
     * @return The ID of this resource.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    @Import(name="name")
    private @Nullable String name;

    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The Organization ID. If not set, the Org ID defined in the provider block will be used.
     * 
     */
    @Import(name="orgId")
    private @Nullable String orgId;

    /**
     * @return The Organization ID. If not set, the Org ID defined in the provider block will be used.
     * 
     */
    public Optional<String> orgId() {
        return Optional.ofNullable(this.orgId);
    }

    @Import(name="uid")
    private @Nullable String uid;

    public Optional<String> uid() {
        return Optional.ofNullable(this.uid);
    }

    private GetDataSourcePlainArgs() {}

    private GetDataSourcePlainArgs(GetDataSourcePlainArgs $) {
        this.id = $.id;
        this.name = $.name;
        this.orgId = $.orgId;
        this.uid = $.uid;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetDataSourcePlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetDataSourcePlainArgs $;

        public Builder() {
            $ = new GetDataSourcePlainArgs();
        }

        public Builder(GetDataSourcePlainArgs defaults) {
            $ = new GetDataSourcePlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id The ID of this resource.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        /**
         * @param orgId The Organization ID. If not set, the Org ID defined in the provider block will be used.
         * 
         * @return builder
         * 
         */
        public Builder orgId(@Nullable String orgId) {
            $.orgId = orgId;
            return this;
        }

        public Builder uid(@Nullable String uid) {
            $.uid = uid;
            return this;
        }

        public GetDataSourcePlainArgs build() {
            return $;
        }
    }

}
