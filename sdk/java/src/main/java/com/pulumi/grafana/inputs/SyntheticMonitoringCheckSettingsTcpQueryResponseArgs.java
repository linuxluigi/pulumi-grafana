// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class SyntheticMonitoringCheckSettingsTcpQueryResponseArgs extends com.pulumi.resources.ResourceArgs {

    public static final SyntheticMonitoringCheckSettingsTcpQueryResponseArgs Empty = new SyntheticMonitoringCheckSettingsTcpQueryResponseArgs();

    /**
     * Response to expect.
     * 
     */
    @Import(name="expect", required=true)
    private Output<String> expect;

    /**
     * @return Response to expect.
     * 
     */
    public Output<String> expect() {
        return this.expect;
    }

    /**
     * Data to send.
     * 
     */
    @Import(name="send", required=true)
    private Output<String> send;

    /**
     * @return Data to send.
     * 
     */
    public Output<String> send() {
        return this.send;
    }

    /**
     * Upgrade TCP connection to TLS. Defaults to `false`.
     * 
     */
    @Import(name="startTls")
    private @Nullable Output<Boolean> startTls;

    /**
     * @return Upgrade TCP connection to TLS. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> startTls() {
        return Optional.ofNullable(this.startTls);
    }

    private SyntheticMonitoringCheckSettingsTcpQueryResponseArgs() {}

    private SyntheticMonitoringCheckSettingsTcpQueryResponseArgs(SyntheticMonitoringCheckSettingsTcpQueryResponseArgs $) {
        this.expect = $.expect;
        this.send = $.send;
        this.startTls = $.startTls;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(SyntheticMonitoringCheckSettingsTcpQueryResponseArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private SyntheticMonitoringCheckSettingsTcpQueryResponseArgs $;

        public Builder() {
            $ = new SyntheticMonitoringCheckSettingsTcpQueryResponseArgs();
        }

        public Builder(SyntheticMonitoringCheckSettingsTcpQueryResponseArgs defaults) {
            $ = new SyntheticMonitoringCheckSettingsTcpQueryResponseArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param expect Response to expect.
         * 
         * @return builder
         * 
         */
        public Builder expect(Output<String> expect) {
            $.expect = expect;
            return this;
        }

        /**
         * @param expect Response to expect.
         * 
         * @return builder
         * 
         */
        public Builder expect(String expect) {
            return expect(Output.of(expect));
        }

        /**
         * @param send Data to send.
         * 
         * @return builder
         * 
         */
        public Builder send(Output<String> send) {
            $.send = send;
            return this;
        }

        /**
         * @param send Data to send.
         * 
         * @return builder
         * 
         */
        public Builder send(String send) {
            return send(Output.of(send));
        }

        /**
         * @param startTls Upgrade TCP connection to TLS. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder startTls(@Nullable Output<Boolean> startTls) {
            $.startTls = startTls;
            return this;
        }

        /**
         * @param startTls Upgrade TCP connection to TLS. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder startTls(Boolean startTls) {
            return startTls(Output.of(startTls));
        }

        public SyntheticMonitoringCheckSettingsTcpQueryResponseArgs build() {
            $.expect = Objects.requireNonNull($.expect, "expected parameter 'expect' to be non-null");
            $.send = Objects.requireNonNull($.send, "expected parameter 'send' to be non-null");
            return $;
        }
    }

}
