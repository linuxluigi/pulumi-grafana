// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ContactPointWecomArgs extends com.pulumi.resources.ResourceArgs {

    public static final ContactPointWecomArgs Empty = new ContactPointWecomArgs();

    /**
     * Agent ID added to the request payload when using APIAPP.
     * 
     */
    @Import(name="agentId")
    private @Nullable Output<String> agentId;

    /**
     * @return Agent ID added to the request payload when using APIAPP.
     * 
     */
    public Optional<Output<String>> agentId() {
        return Optional.ofNullable(this.agentId);
    }

    /**
     * Corp ID used to get token when using APIAPP.
     * 
     */
    @Import(name="corpId")
    private @Nullable Output<String> corpId;

    /**
     * @return Corp ID used to get token when using APIAPP.
     * 
     */
    public Optional<Output<String>> corpId() {
        return Optional.ofNullable(this.corpId);
    }

    /**
     * Whether to disable sending resolve messages. Defaults to `false`.
     * 
     */
    @Import(name="disableResolveMessage")
    private @Nullable Output<Boolean> disableResolveMessage;

    /**
     * @return Whether to disable sending resolve messages. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> disableResolveMessage() {
        return Optional.ofNullable(this.disableResolveMessage);
    }

    /**
     * The templated content of the message to send.
     * 
     */
    @Import(name="message")
    private @Nullable Output<String> message;

    /**
     * @return The templated content of the message to send.
     * 
     */
    public Optional<Output<String>> message() {
        return Optional.ofNullable(this.message);
    }

    /**
     * The type of them message. Supported: markdown, text. Default: text.
     * 
     */
    @Import(name="msgType")
    private @Nullable Output<String> msgType;

    /**
     * @return The type of them message. Supported: markdown, text. Default: text.
     * 
     */
    public Optional<Output<String>> msgType() {
        return Optional.ofNullable(this.msgType);
    }

    /**
     * The secret key required to obtain access token when using APIAPP. See https://work.weixin.qq.com/wework_admin/frame#apps to create APIAPP.
     * 
     */
    @Import(name="secret")
    private @Nullable Output<String> secret;

    /**
     * @return The secret key required to obtain access token when using APIAPP. See https://work.weixin.qq.com/wework_admin/frame#apps to create APIAPP.
     * 
     */
    public Optional<Output<String>> secret() {
        return Optional.ofNullable(this.secret);
    }

    /**
     * Additional custom properties to attach to the notifier. Defaults to `map[]`.
     * 
     */
    @Import(name="settings")
    private @Nullable Output<Map<String,String>> settings;

    /**
     * @return Additional custom properties to attach to the notifier. Defaults to `map[]`.
     * 
     */
    public Optional<Output<Map<String,String>>> settings() {
        return Optional.ofNullable(this.settings);
    }

    /**
     * The templated title of the message to send.
     * 
     */
    @Import(name="title")
    private @Nullable Output<String> title;

    /**
     * @return The templated title of the message to send.
     * 
     */
    public Optional<Output<String>> title() {
        return Optional.ofNullable(this.title);
    }

    /**
     * The ID of user that should receive the message. Multiple entries should be separated by &#39;|&#39;. Default: @all.
     * 
     */
    @Import(name="toUser")
    private @Nullable Output<String> toUser;

    /**
     * @return The ID of user that should receive the message. Multiple entries should be separated by &#39;|&#39;. Default: @all.
     * 
     */
    public Optional<Output<String>> toUser() {
        return Optional.ofNullable(this.toUser);
    }

    /**
     * The UID of the contact point.
     * 
     */
    @Import(name="uid")
    private @Nullable Output<String> uid;

    /**
     * @return The UID of the contact point.
     * 
     */
    public Optional<Output<String>> uid() {
        return Optional.ofNullable(this.uid);
    }

    /**
     * The WeCom webhook URL. Required if using GroupRobot.
     * 
     */
    @Import(name="url")
    private @Nullable Output<String> url;

    /**
     * @return The WeCom webhook URL. Required if using GroupRobot.
     * 
     */
    public Optional<Output<String>> url() {
        return Optional.ofNullable(this.url);
    }

    private ContactPointWecomArgs() {}

    private ContactPointWecomArgs(ContactPointWecomArgs $) {
        this.agentId = $.agentId;
        this.corpId = $.corpId;
        this.disableResolveMessage = $.disableResolveMessage;
        this.message = $.message;
        this.msgType = $.msgType;
        this.secret = $.secret;
        this.settings = $.settings;
        this.title = $.title;
        this.toUser = $.toUser;
        this.uid = $.uid;
        this.url = $.url;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ContactPointWecomArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ContactPointWecomArgs $;

        public Builder() {
            $ = new ContactPointWecomArgs();
        }

        public Builder(ContactPointWecomArgs defaults) {
            $ = new ContactPointWecomArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param agentId Agent ID added to the request payload when using APIAPP.
         * 
         * @return builder
         * 
         */
        public Builder agentId(@Nullable Output<String> agentId) {
            $.agentId = agentId;
            return this;
        }

        /**
         * @param agentId Agent ID added to the request payload when using APIAPP.
         * 
         * @return builder
         * 
         */
        public Builder agentId(String agentId) {
            return agentId(Output.of(agentId));
        }

        /**
         * @param corpId Corp ID used to get token when using APIAPP.
         * 
         * @return builder
         * 
         */
        public Builder corpId(@Nullable Output<String> corpId) {
            $.corpId = corpId;
            return this;
        }

        /**
         * @param corpId Corp ID used to get token when using APIAPP.
         * 
         * @return builder
         * 
         */
        public Builder corpId(String corpId) {
            return corpId(Output.of(corpId));
        }

        /**
         * @param disableResolveMessage Whether to disable sending resolve messages. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder disableResolveMessage(@Nullable Output<Boolean> disableResolveMessage) {
            $.disableResolveMessage = disableResolveMessage;
            return this;
        }

        /**
         * @param disableResolveMessage Whether to disable sending resolve messages. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder disableResolveMessage(Boolean disableResolveMessage) {
            return disableResolveMessage(Output.of(disableResolveMessage));
        }

        /**
         * @param message The templated content of the message to send.
         * 
         * @return builder
         * 
         */
        public Builder message(@Nullable Output<String> message) {
            $.message = message;
            return this;
        }

        /**
         * @param message The templated content of the message to send.
         * 
         * @return builder
         * 
         */
        public Builder message(String message) {
            return message(Output.of(message));
        }

        /**
         * @param msgType The type of them message. Supported: markdown, text. Default: text.
         * 
         * @return builder
         * 
         */
        public Builder msgType(@Nullable Output<String> msgType) {
            $.msgType = msgType;
            return this;
        }

        /**
         * @param msgType The type of them message. Supported: markdown, text. Default: text.
         * 
         * @return builder
         * 
         */
        public Builder msgType(String msgType) {
            return msgType(Output.of(msgType));
        }

        /**
         * @param secret The secret key required to obtain access token when using APIAPP. See https://work.weixin.qq.com/wework_admin/frame#apps to create APIAPP.
         * 
         * @return builder
         * 
         */
        public Builder secret(@Nullable Output<String> secret) {
            $.secret = secret;
            return this;
        }

        /**
         * @param secret The secret key required to obtain access token when using APIAPP. See https://work.weixin.qq.com/wework_admin/frame#apps to create APIAPP.
         * 
         * @return builder
         * 
         */
        public Builder secret(String secret) {
            return secret(Output.of(secret));
        }

        /**
         * @param settings Additional custom properties to attach to the notifier. Defaults to `map[]`.
         * 
         * @return builder
         * 
         */
        public Builder settings(@Nullable Output<Map<String,String>> settings) {
            $.settings = settings;
            return this;
        }

        /**
         * @param settings Additional custom properties to attach to the notifier. Defaults to `map[]`.
         * 
         * @return builder
         * 
         */
        public Builder settings(Map<String,String> settings) {
            return settings(Output.of(settings));
        }

        /**
         * @param title The templated title of the message to send.
         * 
         * @return builder
         * 
         */
        public Builder title(@Nullable Output<String> title) {
            $.title = title;
            return this;
        }

        /**
         * @param title The templated title of the message to send.
         * 
         * @return builder
         * 
         */
        public Builder title(String title) {
            return title(Output.of(title));
        }

        /**
         * @param toUser The ID of user that should receive the message. Multiple entries should be separated by &#39;|&#39;. Default: @all.
         * 
         * @return builder
         * 
         */
        public Builder toUser(@Nullable Output<String> toUser) {
            $.toUser = toUser;
            return this;
        }

        /**
         * @param toUser The ID of user that should receive the message. Multiple entries should be separated by &#39;|&#39;. Default: @all.
         * 
         * @return builder
         * 
         */
        public Builder toUser(String toUser) {
            return toUser(Output.of(toUser));
        }

        /**
         * @param uid The UID of the contact point.
         * 
         * @return builder
         * 
         */
        public Builder uid(@Nullable Output<String> uid) {
            $.uid = uid;
            return this;
        }

        /**
         * @param uid The UID of the contact point.
         * 
         * @return builder
         * 
         */
        public Builder uid(String uid) {
            return uid(Output.of(uid));
        }

        /**
         * @param url The WeCom webhook URL. Required if using GroupRobot.
         * 
         * @return builder
         * 
         */
        public Builder url(@Nullable Output<String> url) {
            $.url = url;
            return this;
        }

        /**
         * @param url The WeCom webhook URL. Required if using GroupRobot.
         * 
         * @return builder
         * 
         */
        public Builder url(String url) {
            return url(Output.of(url));
        }

        public ContactPointWecomArgs build() {
            return $;
        }
    }

}
