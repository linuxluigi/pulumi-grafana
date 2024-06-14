// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

// Deprecated: grafana.index/serviceaccountpermissionitem.ServiceAccountPermissionItem has been deprecated in favor of grafana.oss/serviceaccountpermissionitem.ServiceAccountPermissionItem
type ServiceAccountPermissionItem struct {
	pulumi.CustomResourceState

	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringOutput `pulumi:"orgId"`
	// the permission to be assigned
	Permission pulumi.StringOutput `pulumi:"permission"`
	// The ID of the service account.
	ServiceAccountId pulumi.StringOutput `pulumi:"serviceAccountId"`
	// the team onto which the permission is to be assigned
	Team pulumi.StringPtrOutput `pulumi:"team"`
	// the user or service account onto which the permission is to be assigned
	User pulumi.StringPtrOutput `pulumi:"user"`
}

// NewServiceAccountPermissionItem registers a new resource with the given unique name, arguments, and options.
func NewServiceAccountPermissionItem(ctx *pulumi.Context,
	name string, args *ServiceAccountPermissionItemArgs, opts ...pulumi.ResourceOption) (*ServiceAccountPermissionItem, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Permission == nil {
		return nil, errors.New("invalid value for required argument 'Permission'")
	}
	if args.ServiceAccountId == nil {
		return nil, errors.New("invalid value for required argument 'ServiceAccountId'")
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("grafana:index/serviceAccountPermissionItem:ServiceAccountPermissionItem"),
		},
	})
	opts = append(opts, aliases)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ServiceAccountPermissionItem
	err := ctx.RegisterResource("grafana:index/serviceAccountPermissionItem:ServiceAccountPermissionItem", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServiceAccountPermissionItem gets an existing ServiceAccountPermissionItem resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServiceAccountPermissionItem(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServiceAccountPermissionItemState, opts ...pulumi.ResourceOption) (*ServiceAccountPermissionItem, error) {
	var resource ServiceAccountPermissionItem
	err := ctx.ReadResource("grafana:index/serviceAccountPermissionItem:ServiceAccountPermissionItem", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServiceAccountPermissionItem resources.
type serviceAccountPermissionItemState struct {
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId *string `pulumi:"orgId"`
	// the permission to be assigned
	Permission *string `pulumi:"permission"`
	// The ID of the service account.
	ServiceAccountId *string `pulumi:"serviceAccountId"`
	// the team onto which the permission is to be assigned
	Team *string `pulumi:"team"`
	// the user or service account onto which the permission is to be assigned
	User *string `pulumi:"user"`
}

type ServiceAccountPermissionItemState struct {
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrInput
	// the permission to be assigned
	Permission pulumi.StringPtrInput
	// The ID of the service account.
	ServiceAccountId pulumi.StringPtrInput
	// the team onto which the permission is to be assigned
	Team pulumi.StringPtrInput
	// the user or service account onto which the permission is to be assigned
	User pulumi.StringPtrInput
}

func (ServiceAccountPermissionItemState) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceAccountPermissionItemState)(nil)).Elem()
}

type serviceAccountPermissionItemArgs struct {
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId *string `pulumi:"orgId"`
	// the permission to be assigned
	Permission string `pulumi:"permission"`
	// The ID of the service account.
	ServiceAccountId string `pulumi:"serviceAccountId"`
	// the team onto which the permission is to be assigned
	Team *string `pulumi:"team"`
	// the user or service account onto which the permission is to be assigned
	User *string `pulumi:"user"`
}

// The set of arguments for constructing a ServiceAccountPermissionItem resource.
type ServiceAccountPermissionItemArgs struct {
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrInput
	// the permission to be assigned
	Permission pulumi.StringInput
	// The ID of the service account.
	ServiceAccountId pulumi.StringInput
	// the team onto which the permission is to be assigned
	Team pulumi.StringPtrInput
	// the user or service account onto which the permission is to be assigned
	User pulumi.StringPtrInput
}

func (ServiceAccountPermissionItemArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serviceAccountPermissionItemArgs)(nil)).Elem()
}

type ServiceAccountPermissionItemInput interface {
	pulumi.Input

	ToServiceAccountPermissionItemOutput() ServiceAccountPermissionItemOutput
	ToServiceAccountPermissionItemOutputWithContext(ctx context.Context) ServiceAccountPermissionItemOutput
}

func (*ServiceAccountPermissionItem) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceAccountPermissionItem)(nil)).Elem()
}

func (i *ServiceAccountPermissionItem) ToServiceAccountPermissionItemOutput() ServiceAccountPermissionItemOutput {
	return i.ToServiceAccountPermissionItemOutputWithContext(context.Background())
}

func (i *ServiceAccountPermissionItem) ToServiceAccountPermissionItemOutputWithContext(ctx context.Context) ServiceAccountPermissionItemOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceAccountPermissionItemOutput)
}

// ServiceAccountPermissionItemArrayInput is an input type that accepts ServiceAccountPermissionItemArray and ServiceAccountPermissionItemArrayOutput values.
// You can construct a concrete instance of `ServiceAccountPermissionItemArrayInput` via:
//
//	ServiceAccountPermissionItemArray{ ServiceAccountPermissionItemArgs{...} }
type ServiceAccountPermissionItemArrayInput interface {
	pulumi.Input

	ToServiceAccountPermissionItemArrayOutput() ServiceAccountPermissionItemArrayOutput
	ToServiceAccountPermissionItemArrayOutputWithContext(context.Context) ServiceAccountPermissionItemArrayOutput
}

type ServiceAccountPermissionItemArray []ServiceAccountPermissionItemInput

func (ServiceAccountPermissionItemArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ServiceAccountPermissionItem)(nil)).Elem()
}

func (i ServiceAccountPermissionItemArray) ToServiceAccountPermissionItemArrayOutput() ServiceAccountPermissionItemArrayOutput {
	return i.ToServiceAccountPermissionItemArrayOutputWithContext(context.Background())
}

func (i ServiceAccountPermissionItemArray) ToServiceAccountPermissionItemArrayOutputWithContext(ctx context.Context) ServiceAccountPermissionItemArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceAccountPermissionItemArrayOutput)
}

// ServiceAccountPermissionItemMapInput is an input type that accepts ServiceAccountPermissionItemMap and ServiceAccountPermissionItemMapOutput values.
// You can construct a concrete instance of `ServiceAccountPermissionItemMapInput` via:
//
//	ServiceAccountPermissionItemMap{ "key": ServiceAccountPermissionItemArgs{...} }
type ServiceAccountPermissionItemMapInput interface {
	pulumi.Input

	ToServiceAccountPermissionItemMapOutput() ServiceAccountPermissionItemMapOutput
	ToServiceAccountPermissionItemMapOutputWithContext(context.Context) ServiceAccountPermissionItemMapOutput
}

type ServiceAccountPermissionItemMap map[string]ServiceAccountPermissionItemInput

func (ServiceAccountPermissionItemMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ServiceAccountPermissionItem)(nil)).Elem()
}

func (i ServiceAccountPermissionItemMap) ToServiceAccountPermissionItemMapOutput() ServiceAccountPermissionItemMapOutput {
	return i.ToServiceAccountPermissionItemMapOutputWithContext(context.Background())
}

func (i ServiceAccountPermissionItemMap) ToServiceAccountPermissionItemMapOutputWithContext(ctx context.Context) ServiceAccountPermissionItemMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServiceAccountPermissionItemMapOutput)
}

type ServiceAccountPermissionItemOutput struct{ *pulumi.OutputState }

func (ServiceAccountPermissionItemOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ServiceAccountPermissionItem)(nil)).Elem()
}

func (o ServiceAccountPermissionItemOutput) ToServiceAccountPermissionItemOutput() ServiceAccountPermissionItemOutput {
	return o
}

func (o ServiceAccountPermissionItemOutput) ToServiceAccountPermissionItemOutputWithContext(ctx context.Context) ServiceAccountPermissionItemOutput {
	return o
}

// The Organization ID. If not set, the Org ID defined in the provider block will be used.
func (o ServiceAccountPermissionItemOutput) OrgId() pulumi.StringOutput {
	return o.ApplyT(func(v *ServiceAccountPermissionItem) pulumi.StringOutput { return v.OrgId }).(pulumi.StringOutput)
}

// the permission to be assigned
func (o ServiceAccountPermissionItemOutput) Permission() pulumi.StringOutput {
	return o.ApplyT(func(v *ServiceAccountPermissionItem) pulumi.StringOutput { return v.Permission }).(pulumi.StringOutput)
}

// The ID of the service account.
func (o ServiceAccountPermissionItemOutput) ServiceAccountId() pulumi.StringOutput {
	return o.ApplyT(func(v *ServiceAccountPermissionItem) pulumi.StringOutput { return v.ServiceAccountId }).(pulumi.StringOutput)
}

// the team onto which the permission is to be assigned
func (o ServiceAccountPermissionItemOutput) Team() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ServiceAccountPermissionItem) pulumi.StringPtrOutput { return v.Team }).(pulumi.StringPtrOutput)
}

// the user or service account onto which the permission is to be assigned
func (o ServiceAccountPermissionItemOutput) User() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ServiceAccountPermissionItem) pulumi.StringPtrOutput { return v.User }).(pulumi.StringPtrOutput)
}

type ServiceAccountPermissionItemArrayOutput struct{ *pulumi.OutputState }

func (ServiceAccountPermissionItemArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ServiceAccountPermissionItem)(nil)).Elem()
}

func (o ServiceAccountPermissionItemArrayOutput) ToServiceAccountPermissionItemArrayOutput() ServiceAccountPermissionItemArrayOutput {
	return o
}

func (o ServiceAccountPermissionItemArrayOutput) ToServiceAccountPermissionItemArrayOutputWithContext(ctx context.Context) ServiceAccountPermissionItemArrayOutput {
	return o
}

func (o ServiceAccountPermissionItemArrayOutput) Index(i pulumi.IntInput) ServiceAccountPermissionItemOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ServiceAccountPermissionItem {
		return vs[0].([]*ServiceAccountPermissionItem)[vs[1].(int)]
	}).(ServiceAccountPermissionItemOutput)
}

type ServiceAccountPermissionItemMapOutput struct{ *pulumi.OutputState }

func (ServiceAccountPermissionItemMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ServiceAccountPermissionItem)(nil)).Elem()
}

func (o ServiceAccountPermissionItemMapOutput) ToServiceAccountPermissionItemMapOutput() ServiceAccountPermissionItemMapOutput {
	return o
}

func (o ServiceAccountPermissionItemMapOutput) ToServiceAccountPermissionItemMapOutputWithContext(ctx context.Context) ServiceAccountPermissionItemMapOutput {
	return o
}

func (o ServiceAccountPermissionItemMapOutput) MapIndex(k pulumi.StringInput) ServiceAccountPermissionItemOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ServiceAccountPermissionItem {
		return vs[0].(map[string]*ServiceAccountPermissionItem)[vs[1].(string)]
	}).(ServiceAccountPermissionItemOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceAccountPermissionItemInput)(nil)).Elem(), &ServiceAccountPermissionItem{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceAccountPermissionItemArrayInput)(nil)).Elem(), ServiceAccountPermissionItemArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServiceAccountPermissionItemMapInput)(nil)).Elem(), ServiceAccountPermissionItemMap{})
	pulumi.RegisterOutputType(ServiceAccountPermissionItemOutput{})
	pulumi.RegisterOutputType(ServiceAccountPermissionItemArrayOutput{})
	pulumi.RegisterOutputType(ServiceAccountPermissionItemMapOutput{})
}
