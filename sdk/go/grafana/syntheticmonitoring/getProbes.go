// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package syntheticmonitoring

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

// Data source for retrieving all probes.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/syntheticMonitoring"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := syntheticMonitoring.GetProbes(ctx, nil, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetProbes(ctx *pulumi.Context, args *GetProbesArgs, opts ...pulumi.InvokeOption) (*GetProbesResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetProbesResult
	err := ctx.Invoke("grafana:syntheticMonitoring/getProbes:getProbes", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getProbes.
type GetProbesArgs struct {
	// If true, only probes that are not deprecated will be returned. Defaults to `true`.
	FilterDeprecated *bool `pulumi:"filterDeprecated"`
}

// A collection of values returned by getProbes.
type GetProbesResult struct {
	// If true, only probes that are not deprecated will be returned. Defaults to `true`.
	FilterDeprecated *bool `pulumi:"filterDeprecated"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Map of probes with their names as keys and IDs as values.
	Probes map[string]int `pulumi:"probes"`
}

func GetProbesOutput(ctx *pulumi.Context, args GetProbesOutputArgs, opts ...pulumi.InvokeOption) GetProbesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetProbesResult, error) {
			args := v.(GetProbesArgs)
			r, err := GetProbes(ctx, &args, opts...)
			var s GetProbesResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetProbesResultOutput)
}

// A collection of arguments for invoking getProbes.
type GetProbesOutputArgs struct {
	// If true, only probes that are not deprecated will be returned. Defaults to `true`.
	FilterDeprecated pulumi.BoolPtrInput `pulumi:"filterDeprecated"`
}

func (GetProbesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetProbesArgs)(nil)).Elem()
}

// A collection of values returned by getProbes.
type GetProbesResultOutput struct{ *pulumi.OutputState }

func (GetProbesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetProbesResult)(nil)).Elem()
}

func (o GetProbesResultOutput) ToGetProbesResultOutput() GetProbesResultOutput {
	return o
}

func (o GetProbesResultOutput) ToGetProbesResultOutputWithContext(ctx context.Context) GetProbesResultOutput {
	return o
}

// If true, only probes that are not deprecated will be returned. Defaults to `true`.
func (o GetProbesResultOutput) FilterDeprecated() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v GetProbesResult) *bool { return v.FilterDeprecated }).(pulumi.BoolPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetProbesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetProbesResult) string { return v.Id }).(pulumi.StringOutput)
}

// Map of probes with their names as keys and IDs as values.
func (o GetProbesResultOutput) Probes() pulumi.IntMapOutput {
	return o.ApplyT(func(v GetProbesResult) map[string]int { return v.Probes }).(pulumi.IntMapOutput)
}

func init() {
	pulumi.RegisterOutputType(GetProbesResultOutput{})
}
