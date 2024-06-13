// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

// Deprecated: grafana.index/getsyntheticmonitoringprobe.getSyntheticMonitoringProbe has been deprecated in favor of grafana.syntheticmonitoring/getprobe.getProbe
func LookupSyntheticMonitoringProbe(ctx *pulumi.Context, args *LookupSyntheticMonitoringProbeArgs, opts ...pulumi.InvokeOption) (*LookupSyntheticMonitoringProbeResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSyntheticMonitoringProbeResult
	err := ctx.Invoke("grafana:index/getSyntheticMonitoringProbe:getSyntheticMonitoringProbe", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSyntheticMonitoringProbe.
type LookupSyntheticMonitoringProbeArgs struct {
	Name string `pulumi:"name"`
}

// A collection of values returned by getSyntheticMonitoringProbe.
type LookupSyntheticMonitoringProbeResult struct {
	Id        string            `pulumi:"id"`
	Labels    map[string]string `pulumi:"labels"`
	Latitude  float64           `pulumi:"latitude"`
	Longitude float64           `pulumi:"longitude"`
	Name      string            `pulumi:"name"`
	Public    bool              `pulumi:"public"`
	Region    string            `pulumi:"region"`
	TenantId  int               `pulumi:"tenantId"`
}

func LookupSyntheticMonitoringProbeOutput(ctx *pulumi.Context, args LookupSyntheticMonitoringProbeOutputArgs, opts ...pulumi.InvokeOption) LookupSyntheticMonitoringProbeResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSyntheticMonitoringProbeResult, error) {
			args := v.(LookupSyntheticMonitoringProbeArgs)
			r, err := LookupSyntheticMonitoringProbe(ctx, &args, opts...)
			var s LookupSyntheticMonitoringProbeResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSyntheticMonitoringProbeResultOutput)
}

// A collection of arguments for invoking getSyntheticMonitoringProbe.
type LookupSyntheticMonitoringProbeOutputArgs struct {
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupSyntheticMonitoringProbeOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSyntheticMonitoringProbeArgs)(nil)).Elem()
}

// A collection of values returned by getSyntheticMonitoringProbe.
type LookupSyntheticMonitoringProbeResultOutput struct{ *pulumi.OutputState }

func (LookupSyntheticMonitoringProbeResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSyntheticMonitoringProbeResult)(nil)).Elem()
}

func (o LookupSyntheticMonitoringProbeResultOutput) ToLookupSyntheticMonitoringProbeResultOutput() LookupSyntheticMonitoringProbeResultOutput {
	return o
}

func (o LookupSyntheticMonitoringProbeResultOutput) ToLookupSyntheticMonitoringProbeResultOutputWithContext(ctx context.Context) LookupSyntheticMonitoringProbeResultOutput {
	return o
}

func (o LookupSyntheticMonitoringProbeResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSyntheticMonitoringProbeResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupSyntheticMonitoringProbeResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupSyntheticMonitoringProbeResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

func (o LookupSyntheticMonitoringProbeResultOutput) Latitude() pulumi.Float64Output {
	return o.ApplyT(func(v LookupSyntheticMonitoringProbeResult) float64 { return v.Latitude }).(pulumi.Float64Output)
}

func (o LookupSyntheticMonitoringProbeResultOutput) Longitude() pulumi.Float64Output {
	return o.ApplyT(func(v LookupSyntheticMonitoringProbeResult) float64 { return v.Longitude }).(pulumi.Float64Output)
}

func (o LookupSyntheticMonitoringProbeResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSyntheticMonitoringProbeResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupSyntheticMonitoringProbeResultOutput) Public() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupSyntheticMonitoringProbeResult) bool { return v.Public }).(pulumi.BoolOutput)
}

func (o LookupSyntheticMonitoringProbeResultOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSyntheticMonitoringProbeResult) string { return v.Region }).(pulumi.StringOutput)
}

func (o LookupSyntheticMonitoringProbeResultOutput) TenantId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSyntheticMonitoringProbeResult) int { return v.TenantId }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSyntheticMonitoringProbeResultOutput{})
}
