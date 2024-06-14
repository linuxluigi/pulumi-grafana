// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-grafana/sdk/go/grafana/internal"
)

// Deprecated: grafana.index/getlibrarypanel.getLibraryPanel has been deprecated in favor of grafana.oss/getlibrarypanel.getLibraryPanel
func LookupLibraryPanel(ctx *pulumi.Context, args *LookupLibraryPanelArgs, opts ...pulumi.InvokeOption) (*LookupLibraryPanelResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLibraryPanelResult
	err := ctx.Invoke("grafana:index/getLibraryPanel:getLibraryPanel", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLibraryPanel.
type LookupLibraryPanelArgs struct {
	Name  *string `pulumi:"name"`
	OrgId *string `pulumi:"orgId"`
	Uid   *string `pulumi:"uid"`
}

// A collection of values returned by getLibraryPanel.
type LookupLibraryPanelResult struct {
	Created      string `pulumi:"created"`
	DashboardIds []int  `pulumi:"dashboardIds"`
	Description  string `pulumi:"description"`
	// Deprecated: Use `folderUid` instead
	FolderId   string `pulumi:"folderId"`
	FolderName string `pulumi:"folderName"`
	FolderUid  string `pulumi:"folderUid"`
	// The provider-assigned unique ID for this managed resource.
	Id        string  `pulumi:"id"`
	ModelJson string  `pulumi:"modelJson"`
	Name      *string `pulumi:"name"`
	OrgId     *string `pulumi:"orgId"`
	PanelId   int     `pulumi:"panelId"`
	Type      string  `pulumi:"type"`
	Uid       *string `pulumi:"uid"`
	Updated   string  `pulumi:"updated"`
	Version   int     `pulumi:"version"`
}

func LookupLibraryPanelOutput(ctx *pulumi.Context, args LookupLibraryPanelOutputArgs, opts ...pulumi.InvokeOption) LookupLibraryPanelResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLibraryPanelResult, error) {
			args := v.(LookupLibraryPanelArgs)
			r, err := LookupLibraryPanel(ctx, &args, opts...)
			var s LookupLibraryPanelResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLibraryPanelResultOutput)
}

// A collection of arguments for invoking getLibraryPanel.
type LookupLibraryPanelOutputArgs struct {
	Name  pulumi.StringPtrInput `pulumi:"name"`
	OrgId pulumi.StringPtrInput `pulumi:"orgId"`
	Uid   pulumi.StringPtrInput `pulumi:"uid"`
}

func (LookupLibraryPanelOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLibraryPanelArgs)(nil)).Elem()
}

// A collection of values returned by getLibraryPanel.
type LookupLibraryPanelResultOutput struct{ *pulumi.OutputState }

func (LookupLibraryPanelResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLibraryPanelResult)(nil)).Elem()
}

func (o LookupLibraryPanelResultOutput) ToLookupLibraryPanelResultOutput() LookupLibraryPanelResultOutput {
	return o
}

func (o LookupLibraryPanelResultOutput) ToLookupLibraryPanelResultOutputWithContext(ctx context.Context) LookupLibraryPanelResultOutput {
	return o
}

func (o LookupLibraryPanelResultOutput) Created() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.Created }).(pulumi.StringOutput)
}

func (o LookupLibraryPanelResultOutput) DashboardIds() pulumi.IntArrayOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) []int { return v.DashboardIds }).(pulumi.IntArrayOutput)
}

func (o LookupLibraryPanelResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.Description }).(pulumi.StringOutput)
}

// Deprecated: Use `folderUid` instead
func (o LookupLibraryPanelResultOutput) FolderId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.FolderId }).(pulumi.StringOutput)
}

func (o LookupLibraryPanelResultOutput) FolderName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.FolderName }).(pulumi.StringOutput)
}

func (o LookupLibraryPanelResultOutput) FolderUid() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.FolderUid }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupLibraryPanelResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupLibraryPanelResultOutput) ModelJson() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.ModelJson }).(pulumi.StringOutput)
}

func (o LookupLibraryPanelResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupLibraryPanelResultOutput) OrgId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) *string { return v.OrgId }).(pulumi.StringPtrOutput)
}

func (o LookupLibraryPanelResultOutput) PanelId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) int { return v.PanelId }).(pulumi.IntOutput)
}

func (o LookupLibraryPanelResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.Type }).(pulumi.StringOutput)
}

func (o LookupLibraryPanelResultOutput) Uid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) *string { return v.Uid }).(pulumi.StringPtrOutput)
}

func (o LookupLibraryPanelResultOutput) Updated() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) string { return v.Updated }).(pulumi.StringOutput)
}

func (o LookupLibraryPanelResultOutput) Version() pulumi.IntOutput {
	return o.ApplyT(func(v LookupLibraryPanelResult) int { return v.Version }).(pulumi.IntOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLibraryPanelResultOutput{})
}
