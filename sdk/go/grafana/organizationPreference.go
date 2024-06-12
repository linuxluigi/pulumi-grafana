// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

// * [Official documentation](https://grafana.com/docs/grafana/latest/administration/organization-management/)
// * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/preferences/#get-current-org-prefs)
//
// ## Example Usage
//
// <!--Start PulumiCodeChooser -->
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := grafana.NewOrganizationPreference(ctx, "test", &grafana.OrganizationPreferenceArgs{
//				Theme:     pulumi.String("light"),
//				Timezone:  pulumi.String("utc"),
//				WeekStart: pulumi.String("sunday"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
// <!--End PulumiCodeChooser -->
//
// ## Import
//
// ```sh
// $ pulumi import grafana:index/organizationPreference:OrganizationPreference name "{{ orgID }}"
// ```
type OrganizationPreference struct {
	pulumi.CustomResourceState

	// The Organization home dashboard ID. Deprecated: Use `homeDashboardUid` instead.
	//
	// Deprecated: Use `homeDashboardUid` instead.
	HomeDashboardId pulumi.IntPtrOutput `pulumi:"homeDashboardId"`
	// The Organization home dashboard UID. This is only available in Grafana 9.0+.
	HomeDashboardUid pulumi.StringPtrOutput `pulumi:"homeDashboardUid"`
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrOutput `pulumi:"orgId"`
	// The Organization theme. Available values are `light`, `dark`, `system`, or an empty string for the default.
	Theme pulumi.StringPtrOutput `pulumi:"theme"`
	// The Organization timezone. Available values are `utc`, `browser`, or an empty string for the default.
	Timezone pulumi.StringPtrOutput `pulumi:"timezone"`
	// The Organization week start day. Available values are `sunday`, `monday`, `saturday`, or an empty string for the default. Defaults to ``.
	WeekStart pulumi.StringPtrOutput `pulumi:"weekStart"`
}

// NewOrganizationPreference registers a new resource with the given unique name, arguments, and options.
func NewOrganizationPreference(ctx *pulumi.Context,
	name string, args *OrganizationPreferenceArgs, opts ...pulumi.ResourceOption) (*OrganizationPreference, error) {
	if args == nil {
		args = &OrganizationPreferenceArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource OrganizationPreference
	err := ctx.RegisterResource("grafana:index/organizationPreference:OrganizationPreference", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrganizationPreference gets an existing OrganizationPreference resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrganizationPreference(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrganizationPreferenceState, opts ...pulumi.ResourceOption) (*OrganizationPreference, error) {
	var resource OrganizationPreference
	err := ctx.ReadResource("grafana:index/organizationPreference:OrganizationPreference", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OrganizationPreference resources.
type organizationPreferenceState struct {
	// The Organization home dashboard ID. Deprecated: Use `homeDashboardUid` instead.
	//
	// Deprecated: Use `homeDashboardUid` instead.
	HomeDashboardId *int `pulumi:"homeDashboardId"`
	// The Organization home dashboard UID. This is only available in Grafana 9.0+.
	HomeDashboardUid *string `pulumi:"homeDashboardUid"`
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId *string `pulumi:"orgId"`
	// The Organization theme. Available values are `light`, `dark`, `system`, or an empty string for the default.
	Theme *string `pulumi:"theme"`
	// The Organization timezone. Available values are `utc`, `browser`, or an empty string for the default.
	Timezone *string `pulumi:"timezone"`
	// The Organization week start day. Available values are `sunday`, `monday`, `saturday`, or an empty string for the default. Defaults to ``.
	WeekStart *string `pulumi:"weekStart"`
}

type OrganizationPreferenceState struct {
	// The Organization home dashboard ID. Deprecated: Use `homeDashboardUid` instead.
	//
	// Deprecated: Use `homeDashboardUid` instead.
	HomeDashboardId pulumi.IntPtrInput
	// The Organization home dashboard UID. This is only available in Grafana 9.0+.
	HomeDashboardUid pulumi.StringPtrInput
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrInput
	// The Organization theme. Available values are `light`, `dark`, `system`, or an empty string for the default.
	Theme pulumi.StringPtrInput
	// The Organization timezone. Available values are `utc`, `browser`, or an empty string for the default.
	Timezone pulumi.StringPtrInput
	// The Organization week start day. Available values are `sunday`, `monday`, `saturday`, or an empty string for the default. Defaults to ``.
	WeekStart pulumi.StringPtrInput
}

func (OrganizationPreferenceState) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationPreferenceState)(nil)).Elem()
}

type organizationPreferenceArgs struct {
	// The Organization home dashboard ID. Deprecated: Use `homeDashboardUid` instead.
	//
	// Deprecated: Use `homeDashboardUid` instead.
	HomeDashboardId *int `pulumi:"homeDashboardId"`
	// The Organization home dashboard UID. This is only available in Grafana 9.0+.
	HomeDashboardUid *string `pulumi:"homeDashboardUid"`
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId *string `pulumi:"orgId"`
	// The Organization theme. Available values are `light`, `dark`, `system`, or an empty string for the default.
	Theme *string `pulumi:"theme"`
	// The Organization timezone. Available values are `utc`, `browser`, or an empty string for the default.
	Timezone *string `pulumi:"timezone"`
	// The Organization week start day. Available values are `sunday`, `monday`, `saturday`, or an empty string for the default. Defaults to ``.
	WeekStart *string `pulumi:"weekStart"`
}

// The set of arguments for constructing a OrganizationPreference resource.
type OrganizationPreferenceArgs struct {
	// The Organization home dashboard ID. Deprecated: Use `homeDashboardUid` instead.
	//
	// Deprecated: Use `homeDashboardUid` instead.
	HomeDashboardId pulumi.IntPtrInput
	// The Organization home dashboard UID. This is only available in Grafana 9.0+.
	HomeDashboardUid pulumi.StringPtrInput
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrInput
	// The Organization theme. Available values are `light`, `dark`, `system`, or an empty string for the default.
	Theme pulumi.StringPtrInput
	// The Organization timezone. Available values are `utc`, `browser`, or an empty string for the default.
	Timezone pulumi.StringPtrInput
	// The Organization week start day. Available values are `sunday`, `monday`, `saturday`, or an empty string for the default. Defaults to ``.
	WeekStart pulumi.StringPtrInput
}

func (OrganizationPreferenceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationPreferenceArgs)(nil)).Elem()
}

type OrganizationPreferenceInput interface {
	pulumi.Input

	ToOrganizationPreferenceOutput() OrganizationPreferenceOutput
	ToOrganizationPreferenceOutputWithContext(ctx context.Context) OrganizationPreferenceOutput
}

func (*OrganizationPreference) ElementType() reflect.Type {
	return reflect.TypeOf((**OrganizationPreference)(nil)).Elem()
}

func (i *OrganizationPreference) ToOrganizationPreferenceOutput() OrganizationPreferenceOutput {
	return i.ToOrganizationPreferenceOutputWithContext(context.Background())
}

func (i *OrganizationPreference) ToOrganizationPreferenceOutputWithContext(ctx context.Context) OrganizationPreferenceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationPreferenceOutput)
}

// OrganizationPreferenceArrayInput is an input type that accepts OrganizationPreferenceArray and OrganizationPreferenceArrayOutput values.
// You can construct a concrete instance of `OrganizationPreferenceArrayInput` via:
//
//	OrganizationPreferenceArray{ OrganizationPreferenceArgs{...} }
type OrganizationPreferenceArrayInput interface {
	pulumi.Input

	ToOrganizationPreferenceArrayOutput() OrganizationPreferenceArrayOutput
	ToOrganizationPreferenceArrayOutputWithContext(context.Context) OrganizationPreferenceArrayOutput
}

type OrganizationPreferenceArray []OrganizationPreferenceInput

func (OrganizationPreferenceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OrganizationPreference)(nil)).Elem()
}

func (i OrganizationPreferenceArray) ToOrganizationPreferenceArrayOutput() OrganizationPreferenceArrayOutput {
	return i.ToOrganizationPreferenceArrayOutputWithContext(context.Background())
}

func (i OrganizationPreferenceArray) ToOrganizationPreferenceArrayOutputWithContext(ctx context.Context) OrganizationPreferenceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationPreferenceArrayOutput)
}

// OrganizationPreferenceMapInput is an input type that accepts OrganizationPreferenceMap and OrganizationPreferenceMapOutput values.
// You can construct a concrete instance of `OrganizationPreferenceMapInput` via:
//
//	OrganizationPreferenceMap{ "key": OrganizationPreferenceArgs{...} }
type OrganizationPreferenceMapInput interface {
	pulumi.Input

	ToOrganizationPreferenceMapOutput() OrganizationPreferenceMapOutput
	ToOrganizationPreferenceMapOutputWithContext(context.Context) OrganizationPreferenceMapOutput
}

type OrganizationPreferenceMap map[string]OrganizationPreferenceInput

func (OrganizationPreferenceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OrganizationPreference)(nil)).Elem()
}

func (i OrganizationPreferenceMap) ToOrganizationPreferenceMapOutput() OrganizationPreferenceMapOutput {
	return i.ToOrganizationPreferenceMapOutputWithContext(context.Background())
}

func (i OrganizationPreferenceMap) ToOrganizationPreferenceMapOutputWithContext(ctx context.Context) OrganizationPreferenceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationPreferenceMapOutput)
}

type OrganizationPreferenceOutput struct{ *pulumi.OutputState }

func (OrganizationPreferenceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OrganizationPreference)(nil)).Elem()
}

func (o OrganizationPreferenceOutput) ToOrganizationPreferenceOutput() OrganizationPreferenceOutput {
	return o
}

func (o OrganizationPreferenceOutput) ToOrganizationPreferenceOutputWithContext(ctx context.Context) OrganizationPreferenceOutput {
	return o
}

// The Organization home dashboard ID. Deprecated: Use `homeDashboardUid` instead.
//
// Deprecated: Use `homeDashboardUid` instead.
func (o OrganizationPreferenceOutput) HomeDashboardId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *OrganizationPreference) pulumi.IntPtrOutput { return v.HomeDashboardId }).(pulumi.IntPtrOutput)
}

// The Organization home dashboard UID. This is only available in Grafana 9.0+.
func (o OrganizationPreferenceOutput) HomeDashboardUid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OrganizationPreference) pulumi.StringPtrOutput { return v.HomeDashboardUid }).(pulumi.StringPtrOutput)
}

// The Organization ID. If not set, the Org ID defined in the provider block will be used.
func (o OrganizationPreferenceOutput) OrgId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OrganizationPreference) pulumi.StringPtrOutput { return v.OrgId }).(pulumi.StringPtrOutput)
}

// The Organization theme. Available values are `light`, `dark`, `system`, or an empty string for the default.
func (o OrganizationPreferenceOutput) Theme() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OrganizationPreference) pulumi.StringPtrOutput { return v.Theme }).(pulumi.StringPtrOutput)
}

// The Organization timezone. Available values are `utc`, `browser`, or an empty string for the default.
func (o OrganizationPreferenceOutput) Timezone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OrganizationPreference) pulumi.StringPtrOutput { return v.Timezone }).(pulumi.StringPtrOutput)
}

// The Organization week start day. Available values are `sunday`, `monday`, `saturday`, or an empty string for the default. Defaults to “.
func (o OrganizationPreferenceOutput) WeekStart() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OrganizationPreference) pulumi.StringPtrOutput { return v.WeekStart }).(pulumi.StringPtrOutput)
}

type OrganizationPreferenceArrayOutput struct{ *pulumi.OutputState }

func (OrganizationPreferenceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OrganizationPreference)(nil)).Elem()
}

func (o OrganizationPreferenceArrayOutput) ToOrganizationPreferenceArrayOutput() OrganizationPreferenceArrayOutput {
	return o
}

func (o OrganizationPreferenceArrayOutput) ToOrganizationPreferenceArrayOutputWithContext(ctx context.Context) OrganizationPreferenceArrayOutput {
	return o
}

func (o OrganizationPreferenceArrayOutput) Index(i pulumi.IntInput) OrganizationPreferenceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *OrganizationPreference {
		return vs[0].([]*OrganizationPreference)[vs[1].(int)]
	}).(OrganizationPreferenceOutput)
}

type OrganizationPreferenceMapOutput struct{ *pulumi.OutputState }

func (OrganizationPreferenceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OrganizationPreference)(nil)).Elem()
}

func (o OrganizationPreferenceMapOutput) ToOrganizationPreferenceMapOutput() OrganizationPreferenceMapOutput {
	return o
}

func (o OrganizationPreferenceMapOutput) ToOrganizationPreferenceMapOutputWithContext(ctx context.Context) OrganizationPreferenceMapOutput {
	return o
}

func (o OrganizationPreferenceMapOutput) MapIndex(k pulumi.StringInput) OrganizationPreferenceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *OrganizationPreference {
		return vs[0].(map[string]*OrganizationPreference)[vs[1].(string)]
	}).(OrganizationPreferenceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationPreferenceInput)(nil)).Elem(), &OrganizationPreference{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationPreferenceArrayInput)(nil)).Elem(), OrganizationPreferenceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrganizationPreferenceMapInput)(nil)).Elem(), OrganizationPreferenceMap{})
	pulumi.RegisterOutputType(OrganizationPreferenceOutput{})
	pulumi.RegisterOutputType(OrganizationPreferenceArrayOutput{})
	pulumi.RegisterOutputType(OrganizationPreferenceMapOutput{})
}
