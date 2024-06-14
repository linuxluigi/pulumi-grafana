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

// Deprecated: grafana.index/folderpermissionitem.FolderPermissionItem has been deprecated in favor of grafana.oss/folderpermissionitem.FolderPermissionItem
type FolderPermissionItem struct {
	pulumi.CustomResourceState

	// The UID of the folder.
	FolderUid pulumi.StringOutput `pulumi:"folderUid"`
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringOutput `pulumi:"orgId"`
	// the permission to be assigned
	Permission pulumi.StringOutput `pulumi:"permission"`
	// the role onto which the permission is to be assigned
	Role pulumi.StringPtrOutput `pulumi:"role"`
	// the team onto which the permission is to be assigned
	Team pulumi.StringPtrOutput `pulumi:"team"`
	// the user or service account onto which the permission is to be assigned
	User pulumi.StringPtrOutput `pulumi:"user"`
}

// NewFolderPermissionItem registers a new resource with the given unique name, arguments, and options.
func NewFolderPermissionItem(ctx *pulumi.Context,
	name string, args *FolderPermissionItemArgs, opts ...pulumi.ResourceOption) (*FolderPermissionItem, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FolderUid == nil {
		return nil, errors.New("invalid value for required argument 'FolderUid'")
	}
	if args.Permission == nil {
		return nil, errors.New("invalid value for required argument 'Permission'")
	}
	aliases := pulumi.Aliases([]pulumi.Alias{
		{
			Type: pulumi.String("grafana:index/folderPermissionItem:FolderPermissionItem"),
		},
	})
	opts = append(opts, aliases)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource FolderPermissionItem
	err := ctx.RegisterResource("grafana:index/folderPermissionItem:FolderPermissionItem", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFolderPermissionItem gets an existing FolderPermissionItem resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFolderPermissionItem(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FolderPermissionItemState, opts ...pulumi.ResourceOption) (*FolderPermissionItem, error) {
	var resource FolderPermissionItem
	err := ctx.ReadResource("grafana:index/folderPermissionItem:FolderPermissionItem", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FolderPermissionItem resources.
type folderPermissionItemState struct {
	// The UID of the folder.
	FolderUid *string `pulumi:"folderUid"`
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId *string `pulumi:"orgId"`
	// the permission to be assigned
	Permission *string `pulumi:"permission"`
	// the role onto which the permission is to be assigned
	Role *string `pulumi:"role"`
	// the team onto which the permission is to be assigned
	Team *string `pulumi:"team"`
	// the user or service account onto which the permission is to be assigned
	User *string `pulumi:"user"`
}

type FolderPermissionItemState struct {
	// The UID of the folder.
	FolderUid pulumi.StringPtrInput
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrInput
	// the permission to be assigned
	Permission pulumi.StringPtrInput
	// the role onto which the permission is to be assigned
	Role pulumi.StringPtrInput
	// the team onto which the permission is to be assigned
	Team pulumi.StringPtrInput
	// the user or service account onto which the permission is to be assigned
	User pulumi.StringPtrInput
}

func (FolderPermissionItemState) ElementType() reflect.Type {
	return reflect.TypeOf((*folderPermissionItemState)(nil)).Elem()
}

type folderPermissionItemArgs struct {
	// The UID of the folder.
	FolderUid string `pulumi:"folderUid"`
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId *string `pulumi:"orgId"`
	// the permission to be assigned
	Permission string `pulumi:"permission"`
	// the role onto which the permission is to be assigned
	Role *string `pulumi:"role"`
	// the team onto which the permission is to be assigned
	Team *string `pulumi:"team"`
	// the user or service account onto which the permission is to be assigned
	User *string `pulumi:"user"`
}

// The set of arguments for constructing a FolderPermissionItem resource.
type FolderPermissionItemArgs struct {
	// The UID of the folder.
	FolderUid pulumi.StringInput
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrInput
	// the permission to be assigned
	Permission pulumi.StringInput
	// the role onto which the permission is to be assigned
	Role pulumi.StringPtrInput
	// the team onto which the permission is to be assigned
	Team pulumi.StringPtrInput
	// the user or service account onto which the permission is to be assigned
	User pulumi.StringPtrInput
}

func (FolderPermissionItemArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*folderPermissionItemArgs)(nil)).Elem()
}

type FolderPermissionItemInput interface {
	pulumi.Input

	ToFolderPermissionItemOutput() FolderPermissionItemOutput
	ToFolderPermissionItemOutputWithContext(ctx context.Context) FolderPermissionItemOutput
}

func (*FolderPermissionItem) ElementType() reflect.Type {
	return reflect.TypeOf((**FolderPermissionItem)(nil)).Elem()
}

func (i *FolderPermissionItem) ToFolderPermissionItemOutput() FolderPermissionItemOutput {
	return i.ToFolderPermissionItemOutputWithContext(context.Background())
}

func (i *FolderPermissionItem) ToFolderPermissionItemOutputWithContext(ctx context.Context) FolderPermissionItemOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FolderPermissionItemOutput)
}

// FolderPermissionItemArrayInput is an input type that accepts FolderPermissionItemArray and FolderPermissionItemArrayOutput values.
// You can construct a concrete instance of `FolderPermissionItemArrayInput` via:
//
//	FolderPermissionItemArray{ FolderPermissionItemArgs{...} }
type FolderPermissionItemArrayInput interface {
	pulumi.Input

	ToFolderPermissionItemArrayOutput() FolderPermissionItemArrayOutput
	ToFolderPermissionItemArrayOutputWithContext(context.Context) FolderPermissionItemArrayOutput
}

type FolderPermissionItemArray []FolderPermissionItemInput

func (FolderPermissionItemArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*FolderPermissionItem)(nil)).Elem()
}

func (i FolderPermissionItemArray) ToFolderPermissionItemArrayOutput() FolderPermissionItemArrayOutput {
	return i.ToFolderPermissionItemArrayOutputWithContext(context.Background())
}

func (i FolderPermissionItemArray) ToFolderPermissionItemArrayOutputWithContext(ctx context.Context) FolderPermissionItemArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FolderPermissionItemArrayOutput)
}

// FolderPermissionItemMapInput is an input type that accepts FolderPermissionItemMap and FolderPermissionItemMapOutput values.
// You can construct a concrete instance of `FolderPermissionItemMapInput` via:
//
//	FolderPermissionItemMap{ "key": FolderPermissionItemArgs{...} }
type FolderPermissionItemMapInput interface {
	pulumi.Input

	ToFolderPermissionItemMapOutput() FolderPermissionItemMapOutput
	ToFolderPermissionItemMapOutputWithContext(context.Context) FolderPermissionItemMapOutput
}

type FolderPermissionItemMap map[string]FolderPermissionItemInput

func (FolderPermissionItemMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*FolderPermissionItem)(nil)).Elem()
}

func (i FolderPermissionItemMap) ToFolderPermissionItemMapOutput() FolderPermissionItemMapOutput {
	return i.ToFolderPermissionItemMapOutputWithContext(context.Background())
}

func (i FolderPermissionItemMap) ToFolderPermissionItemMapOutputWithContext(ctx context.Context) FolderPermissionItemMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FolderPermissionItemMapOutput)
}

type FolderPermissionItemOutput struct{ *pulumi.OutputState }

func (FolderPermissionItemOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**FolderPermissionItem)(nil)).Elem()
}

func (o FolderPermissionItemOutput) ToFolderPermissionItemOutput() FolderPermissionItemOutput {
	return o
}

func (o FolderPermissionItemOutput) ToFolderPermissionItemOutputWithContext(ctx context.Context) FolderPermissionItemOutput {
	return o
}

// The UID of the folder.
func (o FolderPermissionItemOutput) FolderUid() pulumi.StringOutput {
	return o.ApplyT(func(v *FolderPermissionItem) pulumi.StringOutput { return v.FolderUid }).(pulumi.StringOutput)
}

// The Organization ID. If not set, the Org ID defined in the provider block will be used.
func (o FolderPermissionItemOutput) OrgId() pulumi.StringOutput {
	return o.ApplyT(func(v *FolderPermissionItem) pulumi.StringOutput { return v.OrgId }).(pulumi.StringOutput)
}

// the permission to be assigned
func (o FolderPermissionItemOutput) Permission() pulumi.StringOutput {
	return o.ApplyT(func(v *FolderPermissionItem) pulumi.StringOutput { return v.Permission }).(pulumi.StringOutput)
}

// the role onto which the permission is to be assigned
func (o FolderPermissionItemOutput) Role() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *FolderPermissionItem) pulumi.StringPtrOutput { return v.Role }).(pulumi.StringPtrOutput)
}

// the team onto which the permission is to be assigned
func (o FolderPermissionItemOutput) Team() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *FolderPermissionItem) pulumi.StringPtrOutput { return v.Team }).(pulumi.StringPtrOutput)
}

// the user or service account onto which the permission is to be assigned
func (o FolderPermissionItemOutput) User() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *FolderPermissionItem) pulumi.StringPtrOutput { return v.User }).(pulumi.StringPtrOutput)
}

type FolderPermissionItemArrayOutput struct{ *pulumi.OutputState }

func (FolderPermissionItemArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*FolderPermissionItem)(nil)).Elem()
}

func (o FolderPermissionItemArrayOutput) ToFolderPermissionItemArrayOutput() FolderPermissionItemArrayOutput {
	return o
}

func (o FolderPermissionItemArrayOutput) ToFolderPermissionItemArrayOutputWithContext(ctx context.Context) FolderPermissionItemArrayOutput {
	return o
}

func (o FolderPermissionItemArrayOutput) Index(i pulumi.IntInput) FolderPermissionItemOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *FolderPermissionItem {
		return vs[0].([]*FolderPermissionItem)[vs[1].(int)]
	}).(FolderPermissionItemOutput)
}

type FolderPermissionItemMapOutput struct{ *pulumi.OutputState }

func (FolderPermissionItemMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*FolderPermissionItem)(nil)).Elem()
}

func (o FolderPermissionItemMapOutput) ToFolderPermissionItemMapOutput() FolderPermissionItemMapOutput {
	return o
}

func (o FolderPermissionItemMapOutput) ToFolderPermissionItemMapOutputWithContext(ctx context.Context) FolderPermissionItemMapOutput {
	return o
}

func (o FolderPermissionItemMapOutput) MapIndex(k pulumi.StringInput) FolderPermissionItemOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *FolderPermissionItem {
		return vs[0].(map[string]*FolderPermissionItem)[vs[1].(string)]
	}).(FolderPermissionItemOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*FolderPermissionItemInput)(nil)).Elem(), &FolderPermissionItem{})
	pulumi.RegisterInputType(reflect.TypeOf((*FolderPermissionItemArrayInput)(nil)).Elem(), FolderPermissionItemArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*FolderPermissionItemMapInput)(nil)).Elem(), FolderPermissionItemMap{})
	pulumi.RegisterOutputType(FolderPermissionItemOutput{})
	pulumi.RegisterOutputType(FolderPermissionItemArrayOutput{})
	pulumi.RegisterOutputType(FolderPermissionItemMapOutput{})
}
