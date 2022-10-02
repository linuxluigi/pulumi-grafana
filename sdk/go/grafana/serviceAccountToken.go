// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// **Note:** This resource is available only with Grafana 9.1+.
//
// * [Official documentation](https://grafana.com/docs/grafana/latest/administration/service-accounts/)
// * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api)
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/lbrlabs/pulumi-grafana/sdk/go/grafana"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			foo, err := grafana.NewServiceAccountToken(ctx, "foo", &grafana.ServiceAccountTokenArgs{
//				ServiceAccountId: pulumi.Int(1),
//			})
//			if err != nil {
//				return err
//			}
//			bar, err := grafana.NewServiceAccountToken(ctx, "bar", &grafana.ServiceAccountTokenArgs{
//				ServiceAccountId: pulumi.Int(1),
//				SecondsToLive:    pulumi.Int(30),
//			})
//			if err != nil {
//				return err
//			}
//			ctx.Export("serviceAccountTokenFooKeyOnly", foo.Key)
//			ctx.Export("serviceAccountTokenBar", bar)
//			return nil
//		})
//	}
//
// ```
type ServiceAccountToken struct {
	pulumi.CustomResourceState

	Expiration       pulumi.StringOutput `pulumi:"expiration"`
	HasExpired       pulumi.BoolOutput   `pulumi:"hasExpired"`
	Key              pulumi.StringOutput `pulumi:"key"`
	Name             pulumi.StringOutput `pulumi:"name"`
	SecondsToLive    pulumi.IntPtrOutput `pulumi:"secondsToLive"`
	ServiceAccountId pulumi.IntOutput    `pulumi:"serviceAccountId"`
}

// NewServiceAccountToken registers a new resource with the given unique name, arguments, and options.
func NewServiceAccountToken(ctx *pulumi.Context,
	name string, args *ServiceAccountTokenArgs, opts ...pulumi.ResourceOption) (*ServiceAccountToken, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ServiceAccountId == nil {
		return nil, errors.New("invalid value for required argument 'ServiceAccountId'")
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"key",
	})
	opts = append(opts, secrets)
	opts = pkgResourceDefaultOpts(opts)
	var resource ServiceAccountToken
	err := ctx.RegisterResource("grafana:index/serviceAccountToken:ServiceAccountToken", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServiceAccountToken gets an existing ServiceAccountToken resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServiceAccountToken(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceAccountTokenState, opts ...pulumi.ResourceOption) (*ServiceAccountToken, error) {
	var resource ServiceAccountToken
	err := ctx.ReadResource("grafana:index/serviceAccountToken:ServiceAccountToken", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServiceAccountToken resources.
type serviceAccountTokenState struct {
	Expiration       *string `pulumi:"expiration"`
	HasExpired       *bool   `pulumi:"hasExpired"`
	Key              *string `pulumi:"key"`
	Name             *string `pulumi:"name"`
	SecondsToLive    *int    `pulumi:"secondsToLive"`
	ServiceAccountId *int    `pulumi:"serviceAccountId"`
}

type ServiceAccountTokenState struct {
	Expiration       pulumi.StringPtrInput
	HasExpired       pulumi.BoolPtrInput
	Key              pulumi.StringPtrInput
	Name             pulumi.StringPtrInput
	SecondsToLive    pulumi.IntPtrInput
	ServiceAccountId pulumi.IntPtrInput
}

func (ServiceAccountTokenState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceAccountTokenState)(nil)).Elem()
}

type serviceAccountTokenArgs struct {
	Name             *string `pulumi:"name"`
	SecondsToLive    *int    `pulumi:"secondsToLive"`
	ServiceAccountId int     `pulumi:"serviceAccountId"`
}

// The set of arguments for constructing a ServiceAccountToken resource.
type ServiceAccountTokenArgs struct {
	Name             pulumi.StringPtrInput
	SecondsToLive    pulumi.IntPtrInput
	ServiceAccountId pulumi.IntInput
}

func (ServiceAccountTokenArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceAccountTokenArgs)(nil)).Elem()
}

type ServiceAccountTokenInput interface {
	pulumi.Input

	ToServiceAccountTokenOutput() ServiceAccountTokenOutput
	ToServiceAccountTokenOutputWithContext(ctx context.Context) ServiceAccountTokenOutput
}

func (*ServiceAccountToken) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceAccountToken)(nil)).Elem()
}

func (i *ServiceAccountToken) ToServiceAccountTokenOutput() ServiceAccountTokenOutput {
	return i.ToServiceAccountTokenOutputWithContext(context.Background())
}

func (i *ServiceAccountToken) ToServiceAccountTokenOutputWithContext(ctx context.Context) ServiceAccountTokenOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceAccountTokenOutput)
}

// ServiceAccountTokenArrayInput is an input type that accepts ServiceAccountTokenArray and ServiceAccountTokenArrayOutput values.
// You can construct a concrete instance of `ServiceAccountTokenArrayInput` via:
//
//	ServiceAccountTokenArray{ ServiceAccountTokenArgs{...} }
type ServiceAccountTokenArrayInput interface {
	pulumi.Input

	ToServiceAccountTokenArrayOutput() ServiceAccountTokenArrayOutput
	ToServiceAccountTokenArrayOutputWithContext(context.Context) ServiceAccountTokenArrayOutput
}

type ServiceAccountTokenArray []ServiceAccountTokenInput

func (ServiceAccountTokenArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ServiceAccountToken)(nil)).Elem()
}

func (i ServiceAccountTokenArray) ToServiceAccountTokenArrayOutput() ServiceAccountTokenArrayOutput {
	return i.ToServiceAccountTokenArrayOutputWithContext(context.Background())
}

func (i ServiceAccountTokenArray) ToServiceAccountTokenArrayOutputWithContext(ctx context.Context) ServiceAccountTokenArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceAccountTokenArrayOutput)
}

// ServiceAccountTokenMapInput is an input type that accepts ServiceAccountTokenMap and ServiceAccountTokenMapOutput values.
// You can construct a concrete instance of `ServiceAccountTokenMapInput` via:
//
//	ServiceAccountTokenMap{ "key": ServiceAccountTokenArgs{...} }
type ServiceAccountTokenMapInput interface {
	pulumi.Input

	ToServiceAccountTokenMapOutput() ServiceAccountTokenMapOutput
	ToServiceAccountTokenMapOutputWithContext(context.Context) ServiceAccountTokenMapOutput
}

type ServiceAccountTokenMap map[string]ServiceAccountTokenInput

func (ServiceAccountTokenMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ServiceAccountToken)(nil)).Elem()
}

func (i ServiceAccountTokenMap) ToServiceAccountTokenMapOutput() ServiceAccountTokenMapOutput {
	return i.ToServiceAccountTokenMapOutputWithContext(context.Background())
}

func (i ServiceAccountTokenMap) ToServiceAccountTokenMapOutputWithContext(ctx context.Context) ServiceAccountTokenMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceAccountTokenMapOutput)
}

type ServiceAccountTokenOutput struct{ *pulumi.OutputState }

func (ServiceAccountTokenOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceAccountToken)(nil)).Elem()
}

func (o ServiceAccountTokenOutput) ToServiceAccountTokenOutput() ServiceAccountTokenOutput {
	return o
}

func (o ServiceAccountTokenOutput) ToServiceAccountTokenOutputWithContext(ctx context.Context) ServiceAccountTokenOutput {
	return o
}

func (o ServiceAccountTokenOutput) Expiration() pulumi.StringOutput {
	return o.ApplyT(func(v *ServiceAccountToken) pulumi.StringOutput { return v.Expiration }).(pulumi.StringOutput)
}

func (o ServiceAccountTokenOutput) HasExpired() pulumi.BoolOutput {
	return o.ApplyT(func(v *ServiceAccountToken) pulumi.BoolOutput { return v.HasExpired }).(pulumi.BoolOutput)
}

func (o ServiceAccountTokenOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v *ServiceAccountToken) pulumi.StringOutput { return v.Key }).(pulumi.StringOutput)
}

func (o ServiceAccountTokenOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ServiceAccountToken) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o ServiceAccountTokenOutput) SecondsToLive() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *ServiceAccountToken) pulumi.IntPtrOutput { return v.SecondsToLive }).(pulumi.IntPtrOutput)
}

func (o ServiceAccountTokenOutput) ServiceAccountId() pulumi.IntOutput {
	return o.ApplyT(func(v *ServiceAccountToken) pulumi.IntOutput { return v.ServiceAccountId }).(pulumi.IntOutput)
}

type ServiceAccountTokenArrayOutput struct{ *pulumi.OutputState }

func (ServiceAccountTokenArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ServiceAccountToken)(nil)).Elem()
}

func (o ServiceAccountTokenArrayOutput) ToServiceAccountTokenArrayOutput() ServiceAccountTokenArrayOutput {
	return o
}

func (o ServiceAccountTokenArrayOutput) ToServiceAccountTokenArrayOutputWithContext(ctx context.Context) ServiceAccountTokenArrayOutput {
	return o
}

func (o ServiceAccountTokenArrayOutput) Index(i pulumi.IntInput) ServiceAccountTokenOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ServiceAccountToken {
		return vs[0].([]*ServiceAccountToken)[vs[1].(int)]
	}).(ServiceAccountTokenOutput)
}

type ServiceAccountTokenMapOutput struct{ *pulumi.OutputState }

func (ServiceAccountTokenMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ServiceAccountToken)(nil)).Elem()
}

func (o ServiceAccountTokenMapOutput) ToServiceAccountTokenMapOutput() ServiceAccountTokenMapOutput {
	return o
}

func (o ServiceAccountTokenMapOutput) ToServiceAccountTokenMapOutputWithContext(ctx context.Context) ServiceAccountTokenMapOutput {
	return o
}

func (o ServiceAccountTokenMapOutput) MapIndex(k pulumi.StringInput) ServiceAccountTokenOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ServiceAccountToken {
		return vs[0].(map[string]*ServiceAccountToken)[vs[1].(string)]
	}).(ServiceAccountTokenOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceAccountTokenInput)(nil)).Elem(), &ServiceAccountToken{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceAccountTokenArrayInput)(nil)).Elem(), ServiceAccountTokenArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceAccountTokenMapInput)(nil)).Elem(), ServiceAccountTokenMap{})
	pulumi.RegisterOutputType(ServiceAccountTokenOutput{})
	pulumi.RegisterOutputType(ServiceAccountTokenArrayOutput{})
	pulumi.RegisterOutputType(ServiceAccountTokenMapOutput{})
}
