// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class CloudAccessPolicyTokenState extends com.pulumi.resources.ResourceArgs {

    public static final CloudAccessPolicyTokenState Empty = new CloudAccessPolicyTokenState();

    /**
     * ID of the access policy for which to create a token.
     * 
     */
    @Import(name="accessPolicyId")
    private @Nullable Output<String> accessPolicyId;

    /**
     * @return ID of the access policy for which to create a token.
     * 
     */
    public Optional<Output<String>> accessPolicyId() {
        return Optional.ofNullable(this.accessPolicyId);
    }

    /**
     * Creation date of the access policy token.
     * 
     */
    @Import(name="createdAt")
    private @Nullable Output<String> createdAt;

    /**
     * @return Creation date of the access policy token.
     * 
     */
    public Optional<Output<String>> createdAt() {
        return Optional.ofNullable(this.createdAt);
    }

    /**
     * Display name of the access policy token. Defaults to the name.
     * 
     */
    @Import(name="displayName")
    private @Nullable Output<String> displayName;

    /**
     * @return Display name of the access policy token. Defaults to the name.
     * 
     */
    public Optional<Output<String>> displayName() {
        return Optional.ofNullable(this.displayName);
    }

    /**
     * Expiration date of the access policy token. Does not expire by default.
     * 
     */
    @Import(name="expiresAt")
    private @Nullable Output<String> expiresAt;

    /**
     * @return Expiration date of the access policy token. Does not expire by default.
     * 
     */
    public Optional<Output<String>> expiresAt() {
        return Optional.ofNullable(this.expiresAt);
    }

    /**
     * Name of the access policy token.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name of the access policy token.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Region of the access policy. Should be set to the same region as the access policy. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/reference/cloud-api/#list-regions.
     * 
     */
    @Import(name="region")
    private @Nullable Output<String> region;

    /**
     * @return Region of the access policy. Should be set to the same region as the access policy. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/reference/cloud-api/#list-regions.
     * 
     */
    public Optional<Output<String>> region() {
        return Optional.ofNullable(this.region);
    }

    @Import(name="token")
    private @Nullable Output<String> token;

    public Optional<Output<String>> token() {
        return Optional.ofNullable(this.token);
    }

    /**
     * Last update date of the access policy token.
     * 
     */
    @Import(name="updatedAt")
    private @Nullable Output<String> updatedAt;

    /**
     * @return Last update date of the access policy token.
     * 
     */
    public Optional<Output<String>> updatedAt() {
        return Optional.ofNullable(this.updatedAt);
    }

    private CloudAccessPolicyTokenState() {}

    private CloudAccessPolicyTokenState(CloudAccessPolicyTokenState $) {
        this.accessPolicyId = $.accessPolicyId;
        this.createdAt = $.createdAt;
        this.displayName = $.displayName;
        this.expiresAt = $.expiresAt;
        this.name = $.name;
        this.region = $.region;
        this.token = $.token;
        this.updatedAt = $.updatedAt;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(CloudAccessPolicyTokenState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private CloudAccessPolicyTokenState $;

        public Builder() {
            $ = new CloudAccessPolicyTokenState();
        }

        public Builder(CloudAccessPolicyTokenState defaults) {
            $ = new CloudAccessPolicyTokenState(Objects.requireNonNull(defaults));
        }

        /**
         * @param accessPolicyId ID of the access policy for which to create a token.
         * 
         * @return builder
         * 
         */
        public Builder accessPolicyId(@Nullable Output<String> accessPolicyId) {
            $.accessPolicyId = accessPolicyId;
            return this;
        }

        /**
         * @param accessPolicyId ID of the access policy for which to create a token.
         * 
         * @return builder
         * 
         */
        public Builder accessPolicyId(String accessPolicyId) {
            return accessPolicyId(Output.of(accessPolicyId));
        }

        /**
         * @param createdAt Creation date of the access policy token.
         * 
         * @return builder
         * 
         */
        public Builder createdAt(@Nullable Output<String> createdAt) {
            $.createdAt = createdAt;
            return this;
        }

        /**
         * @param createdAt Creation date of the access policy token.
         * 
         * @return builder
         * 
         */
        public Builder createdAt(String createdAt) {
            return createdAt(Output.of(createdAt));
        }

        /**
         * @param displayName Display name of the access policy token. Defaults to the name.
         * 
         * @return builder
         * 
         */
        public Builder displayName(@Nullable Output<String> displayName) {
            $.displayName = displayName;
            return this;
        }

        /**
         * @param displayName Display name of the access policy token. Defaults to the name.
         * 
         * @return builder
         * 
         */
        public Builder displayName(String displayName) {
            return displayName(Output.of(displayName));
        }

        /**
         * @param expiresAt Expiration date of the access policy token. Does not expire by default.
         * 
         * @return builder
         * 
         */
        public Builder expiresAt(@Nullable Output<String> expiresAt) {
            $.expiresAt = expiresAt;
            return this;
        }

        /**
         * @param expiresAt Expiration date of the access policy token. Does not expire by default.
         * 
         * @return builder
         * 
         */
        public Builder expiresAt(String expiresAt) {
            return expiresAt(Output.of(expiresAt));
        }

        /**
         * @param name Name of the access policy token.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of the access policy token.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param region Region of the access policy. Should be set to the same region as the access policy. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/reference/cloud-api/#list-regions.
         * 
         * @return builder
         * 
         */
        public Builder region(@Nullable Output<String> region) {
            $.region = region;
            return this;
        }

        /**
         * @param region Region of the access policy. Should be set to the same region as the access policy. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/reference/cloud-api/#list-regions.
         * 
         * @return builder
         * 
         */
        public Builder region(String region) {
            return region(Output.of(region));
        }

        public Builder token(@Nullable Output<String> token) {
            $.token = token;
            return this;
        }

        public Builder token(String token) {
            return token(Output.of(token));
        }

        /**
         * @param updatedAt Last update date of the access policy token.
         * 
         * @return builder
         * 
         */
        public Builder updatedAt(@Nullable Output<String> updatedAt) {
            $.updatedAt = updatedAt;
            return this;
        }

        /**
         * @param updatedAt Last update date of the access policy token.
         * 
         * @return builder
         * 
         */
        public Builder updatedAt(String updatedAt) {
            return updatedAt(Output.of(updatedAt));
        }

        public CloudAccessPolicyTokenState build() {
            return $;
        }
    }

}
