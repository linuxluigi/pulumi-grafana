// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.grafana.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.grafana.outputs.GetSlosSloQueryFreeform;
import com.pulumi.grafana.outputs.GetSlosSloQueryRatio;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetSlosSloQuery {
    private @Nullable GetSlosSloQueryFreeform freeform;
    private @Nullable GetSlosSloQueryRatio ratio;
    private String type;

    private GetSlosSloQuery() {}
    public Optional<GetSlosSloQueryFreeform> freeform() {
        return Optional.ofNullable(this.freeform);
    }
    public Optional<GetSlosSloQueryRatio> ratio() {
        return Optional.ofNullable(this.ratio);
    }
    public String type() {
        return this.type;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetSlosSloQuery defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable GetSlosSloQueryFreeform freeform;
        private @Nullable GetSlosSloQueryRatio ratio;
        private String type;
        public Builder() {}
        public Builder(GetSlosSloQuery defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.freeform = defaults.freeform;
    	      this.ratio = defaults.ratio;
    	      this.type = defaults.type;
        }

        @CustomType.Setter
        public Builder freeform(@Nullable GetSlosSloQueryFreeform freeform) {
            this.freeform = freeform;
            return this;
        }
        @CustomType.Setter
        public Builder ratio(@Nullable GetSlosSloQueryRatio ratio) {
            this.ratio = ratio;
            return this;
        }
        @CustomType.Setter
        public Builder type(String type) {
            this.type = Objects.requireNonNull(type);
            return this;
        }
        public GetSlosSloQuery build() {
            final var o = new GetSlosSloQuery();
            o.freeform = freeform;
            o.ratio = ratio;
            o.type = type;
            return o;
        }
    }
}
