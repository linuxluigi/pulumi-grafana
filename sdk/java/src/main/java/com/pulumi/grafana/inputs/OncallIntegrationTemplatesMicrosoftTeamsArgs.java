// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class OncallIntegrationTemplatesMicrosoftTeamsArgs extends com.pulumi.resources.ResourceArgs {

    public static final OncallIntegrationTemplatesMicrosoftTeamsArgs Empty = new OncallIntegrationTemplatesMicrosoftTeamsArgs();

    /**
     * Template for Alert image url.
     * 
     */
    @Import(name="imageUrl")
    private @Nullable Output<String> imageUrl;

    /**
     * @return Template for Alert image url.
     * 
     */
    public Optional<Output<String>> imageUrl() {
        return Optional.ofNullable(this.imageUrl);
    }

    /**
     * Template for Alert message.
     * 
     */
    @Import(name="message")
    private @Nullable Output<String> message;

    /**
     * @return Template for Alert message.
     * 
     */
    public Optional<Output<String>> message() {
        return Optional.ofNullable(this.message);
    }

    /**
     * Template for Alert title.
     * 
     */
    @Import(name="title")
    private @Nullable Output<String> title;

    /**
     * @return Template for Alert title.
     * 
     */
    public Optional<Output<String>> title() {
        return Optional.ofNullable(this.title);
    }

    private OncallIntegrationTemplatesMicrosoftTeamsArgs() {}

    private OncallIntegrationTemplatesMicrosoftTeamsArgs(OncallIntegrationTemplatesMicrosoftTeamsArgs $) {
        this.imageUrl = $.imageUrl;
        this.message = $.message;
        this.title = $.title;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(OncallIntegrationTemplatesMicrosoftTeamsArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private OncallIntegrationTemplatesMicrosoftTeamsArgs $;

        public Builder() {
            $ = new OncallIntegrationTemplatesMicrosoftTeamsArgs();
        }

        public Builder(OncallIntegrationTemplatesMicrosoftTeamsArgs defaults) {
            $ = new OncallIntegrationTemplatesMicrosoftTeamsArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param imageUrl Template for Alert image url.
         * 
         * @return builder
         * 
         */
        public Builder imageUrl(@Nullable Output<String> imageUrl) {
            $.imageUrl = imageUrl;
            return this;
        }

        /**
         * @param imageUrl Template for Alert image url.
         * 
         * @return builder
         * 
         */
        public Builder imageUrl(String imageUrl) {
            return imageUrl(Output.of(imageUrl));
        }

        /**
         * @param message Template for Alert message.
         * 
         * @return builder
         * 
         */
        public Builder message(@Nullable Output<String> message) {
            $.message = message;
            return this;
        }

        /**
         * @param message Template for Alert message.
         * 
         * @return builder
         * 
         */
        public Builder message(String message) {
            return message(Output.of(message));
        }

        /**
         * @param title Template for Alert title.
         * 
         * @return builder
         * 
         */
        public Builder title(@Nullable Output<String> title) {
            $.title = title;
            return this;
        }

        /**
         * @param title Template for Alert title.
         * 
         * @return builder
         * 
         */
        public Builder title(String title) {
            return title(Output.of(title));
        }

        public OncallIntegrationTemplatesMicrosoftTeamsArgs build() {
            return $;
        }
    }

}
