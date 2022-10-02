// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Manages a single API key on the Grafana Cloud portal (on the organization level)
// * [API documentation](https://grafana.com/docs/grafana-cloud/reference/cloud-api/#api-keys)
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
//			_, err := grafana.NewCloudApiKey(ctx, "test", &grafana.CloudApiKeyArgs{
//				CloudOrgSlug: pulumi.String("myorg"),
//				Role:         pulumi.String("Admin"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// ```sh
//
//	$ pulumi import grafana:index/cloudApiKey:CloudApiKey resource_name "{{org-name}}-{{api_key_name}}"
//
// ```
type CloudApiKey struct {
	pulumi.CustomResourceState

	// The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
	CloudOrgSlug pulumi.StringOutput `pulumi:"cloudOrgSlug"`
	// The generated API key.
	Key pulumi.StringOutput `pulumi:"key"`
	// Name of the API key.
	Name pulumi.StringOutput `pulumi:"name"`
	// Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
	Role pulumi.StringOutput `pulumi:"role"`
}

// NewCloudApiKey registers a new resource with the given unique name, arguments, and options.
func NewCloudApiKey(ctx *pulumi.Context,
	name string, args *CloudApiKeyArgs, opts ...pulumi.ResourceOption) (*CloudApiKey, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CloudOrgSlug == nil {
		return nil, errors.New("invalid value for required argument 'CloudOrgSlug'")
	}
	if args.Role == nil {
		return nil, errors.New("invalid value for required argument 'Role'")
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"key",
	})
	opts = append(opts, secrets)
	opts = pkgResourceDefaultOpts(opts)
	var resource CloudApiKey
	err := ctx.RegisterResource("grafana:index/cloudApiKey:CloudApiKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCloudApiKey gets an existing CloudApiKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCloudApiKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CloudApiKeyState, opts ...pulumi.ResourceOption) (*CloudApiKey, error) {
	var resource CloudApiKey
	err := ctx.ReadResource("grafana:index/cloudApiKey:CloudApiKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering CloudApiKey resources.
type cloudApiKeyState struct {
	// The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
	CloudOrgSlug *string `pulumi:"cloudOrgSlug"`
	// The generated API key.
	Key *string `pulumi:"key"`
	// Name of the API key.
	Name *string `pulumi:"name"`
	// Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
	Role *string `pulumi:"role"`
}

type CloudApiKeyState struct {
	// The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
	CloudOrgSlug pulumi.StringPtrInput
	// The generated API key.
	Key pulumi.StringPtrInput
	// Name of the API key.
	Name pulumi.StringPtrInput
	// Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
	Role pulumi.StringPtrInput
}

func (CloudApiKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*cloudApiKeyState)(nil)).Elem()
}

type cloudApiKeyArgs struct {
	// The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
	CloudOrgSlug string `pulumi:"cloudOrgSlug"`
	// Name of the API key.
	Name *string `pulumi:"name"`
	// Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
	Role string `pulumi:"role"`
}

// The set of arguments for constructing a CloudApiKey resource.
type CloudApiKeyArgs struct {
	// The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
	CloudOrgSlug pulumi.StringInput
	// Name of the API key.
	Name pulumi.StringPtrInput
	// Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
	Role pulumi.StringInput
}

func (CloudApiKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*cloudApiKeyArgs)(nil)).Elem()
}

type CloudApiKeyInput interface {
	pulumi.Input

	ToCloudApiKeyOutput() CloudApiKeyOutput
	ToCloudApiKeyOutputWithContext(ctx context.Context) CloudApiKeyOutput
}

func (*CloudApiKey) ElementType() reflect.Type {
	return reflect.TypeOf((**CloudApiKey)(nil)).Elem()
}

func (i *CloudApiKey) ToCloudApiKeyOutput() CloudApiKeyOutput {
	return i.ToCloudApiKeyOutputWithContext(context.Background())
}

func (i *CloudApiKey) ToCloudApiKeyOutputWithContext(ctx context.Context) CloudApiKeyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CloudApiKeyOutput)
}

// CloudApiKeyArrayInput is an input type that accepts CloudApiKeyArray and CloudApiKeyArrayOutput values.
// You can construct a concrete instance of `CloudApiKeyArrayInput` via:
//
//	CloudApiKeyArray{ CloudApiKeyArgs{...} }
type CloudApiKeyArrayInput interface {
	pulumi.Input

	ToCloudApiKeyArrayOutput() CloudApiKeyArrayOutput
	ToCloudApiKeyArrayOutputWithContext(context.Context) CloudApiKeyArrayOutput
}

type CloudApiKeyArray []CloudApiKeyInput

func (CloudApiKeyArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CloudApiKey)(nil)).Elem()
}

func (i CloudApiKeyArray) ToCloudApiKeyArrayOutput() CloudApiKeyArrayOutput {
	return i.ToCloudApiKeyArrayOutputWithContext(context.Background())
}

func (i CloudApiKeyArray) ToCloudApiKeyArrayOutputWithContext(ctx context.Context) CloudApiKeyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CloudApiKeyArrayOutput)
}

// CloudApiKeyMapInput is an input type that accepts CloudApiKeyMap and CloudApiKeyMapOutput values.
// You can construct a concrete instance of `CloudApiKeyMapInput` via:
//
//	CloudApiKeyMap{ "key": CloudApiKeyArgs{...} }
type CloudApiKeyMapInput interface {
	pulumi.Input

	ToCloudApiKeyMapOutput() CloudApiKeyMapOutput
	ToCloudApiKeyMapOutputWithContext(context.Context) CloudApiKeyMapOutput
}

type CloudApiKeyMap map[string]CloudApiKeyInput

func (CloudApiKeyMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CloudApiKey)(nil)).Elem()
}

func (i CloudApiKeyMap) ToCloudApiKeyMapOutput() CloudApiKeyMapOutput {
	return i.ToCloudApiKeyMapOutputWithContext(context.Background())
}

func (i CloudApiKeyMap) ToCloudApiKeyMapOutputWithContext(ctx context.Context) CloudApiKeyMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CloudApiKeyMapOutput)
}

type CloudApiKeyOutput struct{ *pulumi.OutputState }

func (CloudApiKeyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**CloudApiKey)(nil)).Elem()
}

func (o CloudApiKeyOutput) ToCloudApiKeyOutput() CloudApiKeyOutput {
	return o
}

func (o CloudApiKeyOutput) ToCloudApiKeyOutputWithContext(ctx context.Context) CloudApiKeyOutput {
	return o
}

// The slug of the organization to create the API key in. This is the same slug as the organization name in the URL.
func (o CloudApiKeyOutput) CloudOrgSlug() pulumi.StringOutput {
	return o.ApplyT(func(v *CloudApiKey) pulumi.StringOutput { return v.CloudOrgSlug }).(pulumi.StringOutput)
}

// The generated API key.
func (o CloudApiKeyOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v *CloudApiKey) pulumi.StringOutput { return v.Key }).(pulumi.StringOutput)
}

// Name of the API key.
func (o CloudApiKeyOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *CloudApiKey) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Role of the API key. Should be one of [Viewer Editor Admin MetricsPublisher PluginPublisher]. See https://grafana.com/docs/grafana-cloud/api/#create-api-key for details.
func (o CloudApiKeyOutput) Role() pulumi.StringOutput {
	return o.ApplyT(func(v *CloudApiKey) pulumi.StringOutput { return v.Role }).(pulumi.StringOutput)
}

type CloudApiKeyArrayOutput struct{ *pulumi.OutputState }

func (CloudApiKeyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*CloudApiKey)(nil)).Elem()
}

func (o CloudApiKeyArrayOutput) ToCloudApiKeyArrayOutput() CloudApiKeyArrayOutput {
	return o
}

func (o CloudApiKeyArrayOutput) ToCloudApiKeyArrayOutputWithContext(ctx context.Context) CloudApiKeyArrayOutput {
	return o
}

func (o CloudApiKeyArrayOutput) Index(i pulumi.IntInput) CloudApiKeyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *CloudApiKey {
		return vs[0].([]*CloudApiKey)[vs[1].(int)]
	}).(CloudApiKeyOutput)
}

type CloudApiKeyMapOutput struct{ *pulumi.OutputState }

func (CloudApiKeyMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*CloudApiKey)(nil)).Elem()
}

func (o CloudApiKeyMapOutput) ToCloudApiKeyMapOutput() CloudApiKeyMapOutput {
	return o
}

func (o CloudApiKeyMapOutput) ToCloudApiKeyMapOutputWithContext(ctx context.Context) CloudApiKeyMapOutput {
	return o
}

func (o CloudApiKeyMapOutput) MapIndex(k pulumi.StringInput) CloudApiKeyOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *CloudApiKey {
		return vs[0].(map[string]*CloudApiKey)[vs[1].(string)]
	}).(CloudApiKeyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CloudApiKeyInput)(nil)).Elem(), &CloudApiKey{})
	pulumi.RegisterInputType(reflect.TypeOf((*CloudApiKeyArrayInput)(nil)).Elem(), CloudApiKeyArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CloudApiKeyMapInput)(nil)).Elem(), CloudApiKeyMap{})
	pulumi.RegisterOutputType(CloudApiKeyOutput{})
	pulumi.RegisterOutputType(CloudApiKeyArrayOutput{})
	pulumi.RegisterOutputType(CloudApiKeyMapOutput{})
}
