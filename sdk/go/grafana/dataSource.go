// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package grafana

import (
	"context"
	"reflect"

	"errors"
	"github.com/lbrlabs/pulumi-grafana/sdk/go/grafana/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// * [Official documentation](https://grafana.com/docs/grafana/latest/datasources/)
// * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/data_source/)
//
// The required arguments for this resource vary depending on the type of data
// source selected (via the 'type' argument).
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"encoding/json"
//
//	"github.com/lbrlabs/pulumi-grafana/sdk/go/grafana"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			tmpJSON0, err := json.Marshal(map[string]interface{}{
//				"tokenUri":           "https://oauth2.googleapis.com/token",
//				"authenticationType": "jwt",
//				"defaultProject":     "default-project",
//				"clientEmail":        "client-email@default-project.iam.gserviceaccount.com",
//			})
//			if err != nil {
//				return err
//			}
//			json0 := string(tmpJSON0)
//			tmpJSON1, err := json.Marshal(map[string]interface{}{
//				"privateKey": "-----BEGIN PRIVATE KEY-----\nprivate-key\n-----END PRIVATE KEY-----\n",
//			})
//			if err != nil {
//				return err
//			}
//			json1 := string(tmpJSON1)
//			_, err = grafana.NewDataSource(ctx, "arbitrary-data", &grafana.DataSourceArgs{
//				Type:                  pulumi.String("stackdriver"),
//				JsonDataEncoded:       pulumi.String(json0),
//				SecureJsonDataEncoded: pulumi.String(json1),
//			})
//			if err != nil {
//				return err
//			}
//			tmpJSON2, err := json.Marshal(map[string]interface{}{
//				"authType":          "default",
//				"basicAuthPassword": "mypassword",
//			})
//			if err != nil {
//				return err
//			}
//			json2 := string(tmpJSON2)
//			_, err = grafana.NewDataSource(ctx, "influxdb", &grafana.DataSourceArgs{
//				Type:              pulumi.String("influxdb"),
//				Url:               pulumi.String("http://influxdb.example.net:8086/"),
//				BasicAuthEnabled:  pulumi.Bool(true),
//				BasicAuthUsername: pulumi.String("username"),
//				DatabaseName:      pulumi.Any(influxdb_database.Metrics.Name),
//				JsonDataEncoded:   pulumi.String(json2),
//			})
//			if err != nil {
//				return err
//			}
//			tmpJSON3, err := json.Marshal(map[string]interface{}{
//				"defaultRegion": "us-east-1",
//				"authType":      "keys",
//			})
//			if err != nil {
//				return err
//			}
//			json3 := string(tmpJSON3)
//			tmpJSON4, err := json.Marshal(map[string]interface{}{
//				"accessKey": "123",
//				"secretKey": "456",
//			})
//			if err != nil {
//				return err
//			}
//			json4 := string(tmpJSON4)
//			_, err = grafana.NewDataSource(ctx, "cloudwatch", &grafana.DataSourceArgs{
//				Type:                  pulumi.String("cloudwatch"),
//				JsonDataEncoded:       pulumi.String(json3),
//				SecureJsonDataEncoded: pulumi.String(json4),
//			})
//			if err != nil {
//				return err
//			}
//			tmpJSON5, err := json.Marshal(map[string]interface{}{
//				"httpMethod":        "POST",
//				"prometheusType":    "Mimir",
//				"prometheusVersion": "2.4.0",
//			})
//			if err != nil {
//				return err
//			}
//			json5 := string(tmpJSON5)
//			tmpJSON6, err := json.Marshal(map[string]interface{}{
//				"basicAuthPassword": "password",
//			})
//			if err != nil {
//				return err
//			}
//			json6 := string(tmpJSON6)
//			_, err = grafana.NewDataSource(ctx, "prometheus", &grafana.DataSourceArgs{
//				Type:                  pulumi.String("prometheus"),
//				Url:                   pulumi.String("https://my-instances.com"),
//				BasicAuthEnabled:      pulumi.Bool(true),
//				BasicAuthUsername:     pulumi.String("username"),
//				JsonDataEncoded:       pulumi.String(json5),
//				SecureJsonDataEncoded: pulumi.String(json6),
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
//	$ pulumi import grafana:index/dataSource:DataSource by_integer_id {{datasource id}}
//
// ```
//
// ```sh
//
//	$ pulumi import grafana:index/dataSource:DataSource by_uid {{datasource uid}}
//
// ```
type DataSource struct {
	pulumi.CustomResourceState

	// The method by which Grafana will access the data source: `proxy` or `direct`. Defaults to `proxy`.
	AccessMode pulumi.StringPtrOutput `pulumi:"accessMode"`
	// Whether to enable basic auth for the data source. Defaults to `false`.
	BasicAuthEnabled pulumi.BoolPtrOutput `pulumi:"basicAuthEnabled"`
	// Basic auth username. Defaults to ``.
	BasicAuthUsername pulumi.StringPtrOutput `pulumi:"basicAuthUsername"`
	// (Required by some data source types) The name of the database to use on the selected data source server. Defaults to ``.
	DatabaseName pulumi.StringPtrOutput `pulumi:"databaseName"`
	// Custom HTTP headers
	HttpHeaders pulumi.StringMapOutput `pulumi:"httpHeaders"`
	// Whether to set the data source as default. This should only be `true` to a single data source. Defaults to `false`.
	IsDefault pulumi.BoolPtrOutput `pulumi:"isDefault"`
	// Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
	JsonDataEncoded pulumi.StringPtrOutput `pulumi:"jsonDataEncoded"`
	// A unique name for the data source.
	Name pulumi.StringOutput `pulumi:"name"`
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrOutput `pulumi:"orgId"`
	// Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
	SecureJsonDataEncoded pulumi.StringPtrOutput `pulumi:"secureJsonDataEncoded"`
	// The data source type. Must be one of the supported data source keywords.
	Type pulumi.StringOutput `pulumi:"type"`
	// Unique identifier. If unset, this will be automatically generated.
	Uid pulumi.StringOutput `pulumi:"uid"`
	// The URL for the data source. The type of URL required varies depending on the chosen data source type.
	Url pulumi.StringPtrOutput `pulumi:"url"`
	// (Required by some data source types) The username to use to authenticate to the data source. Defaults to ``.
	Username pulumi.StringPtrOutput `pulumi:"username"`
}

// NewDataSource registers a new resource with the given unique name, arguments, and options.
func NewDataSource(ctx *pulumi.Context,
	name string, args *DataSourceArgs, opts ...pulumi.ResourceOption) (*DataSource, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	if args.HttpHeaders != nil {
		args.HttpHeaders = pulumi.ToSecret(args.HttpHeaders).(pulumi.StringMapInput)
	}
	if args.SecureJsonDataEncoded != nil {
		args.SecureJsonDataEncoded = pulumi.ToSecret(args.SecureJsonDataEncoded).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"httpHeaders",
		"secureJsonDataEncoded",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DataSource
	err := ctx.RegisterResource("grafana:index/dataSource:DataSource", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDataSource gets an existing DataSource resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDataSource(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DataSourceState, opts ...pulumi.ResourceOption) (*DataSource, error) {
	var resource DataSource
	err := ctx.ReadResource("grafana:index/dataSource:DataSource", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DataSource resources.
type dataSourceState struct {
	// The method by which Grafana will access the data source: `proxy` or `direct`. Defaults to `proxy`.
	AccessMode *string `pulumi:"accessMode"`
	// Whether to enable basic auth for the data source. Defaults to `false`.
	BasicAuthEnabled *bool `pulumi:"basicAuthEnabled"`
	// Basic auth username. Defaults to ``.
	BasicAuthUsername *string `pulumi:"basicAuthUsername"`
	// (Required by some data source types) The name of the database to use on the selected data source server. Defaults to ``.
	DatabaseName *string `pulumi:"databaseName"`
	// Custom HTTP headers
	HttpHeaders map[string]string `pulumi:"httpHeaders"`
	// Whether to set the data source as default. This should only be `true` to a single data source. Defaults to `false`.
	IsDefault *bool `pulumi:"isDefault"`
	// Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
	JsonDataEncoded *string `pulumi:"jsonDataEncoded"`
	// A unique name for the data source.
	Name *string `pulumi:"name"`
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId *string `pulumi:"orgId"`
	// Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
	SecureJsonDataEncoded *string `pulumi:"secureJsonDataEncoded"`
	// The data source type. Must be one of the supported data source keywords.
	Type *string `pulumi:"type"`
	// Unique identifier. If unset, this will be automatically generated.
	Uid *string `pulumi:"uid"`
	// The URL for the data source. The type of URL required varies depending on the chosen data source type.
	Url *string `pulumi:"url"`
	// (Required by some data source types) The username to use to authenticate to the data source. Defaults to ``.
	Username *string `pulumi:"username"`
}

type DataSourceState struct {
	// The method by which Grafana will access the data source: `proxy` or `direct`. Defaults to `proxy`.
	AccessMode pulumi.StringPtrInput
	// Whether to enable basic auth for the data source. Defaults to `false`.
	BasicAuthEnabled pulumi.BoolPtrInput
	// Basic auth username. Defaults to ``.
	BasicAuthUsername pulumi.StringPtrInput
	// (Required by some data source types) The name of the database to use on the selected data source server. Defaults to ``.
	DatabaseName pulumi.StringPtrInput
	// Custom HTTP headers
	HttpHeaders pulumi.StringMapInput
	// Whether to set the data source as default. This should only be `true` to a single data source. Defaults to `false`.
	IsDefault pulumi.BoolPtrInput
	// Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
	JsonDataEncoded pulumi.StringPtrInput
	// A unique name for the data source.
	Name pulumi.StringPtrInput
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrInput
	// Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
	SecureJsonDataEncoded pulumi.StringPtrInput
	// The data source type. Must be one of the supported data source keywords.
	Type pulumi.StringPtrInput
	// Unique identifier. If unset, this will be automatically generated.
	Uid pulumi.StringPtrInput
	// The URL for the data source. The type of URL required varies depending on the chosen data source type.
	Url pulumi.StringPtrInput
	// (Required by some data source types) The username to use to authenticate to the data source. Defaults to ``.
	Username pulumi.StringPtrInput
}

func (DataSourceState) ElementType() reflect.Type {
	return reflect.TypeOf((*dataSourceState)(nil)).Elem()
}

type dataSourceArgs struct {
	// The method by which Grafana will access the data source: `proxy` or `direct`. Defaults to `proxy`.
	AccessMode *string `pulumi:"accessMode"`
	// Whether to enable basic auth for the data source. Defaults to `false`.
	BasicAuthEnabled *bool `pulumi:"basicAuthEnabled"`
	// Basic auth username. Defaults to ``.
	BasicAuthUsername *string `pulumi:"basicAuthUsername"`
	// (Required by some data source types) The name of the database to use on the selected data source server. Defaults to ``.
	DatabaseName *string `pulumi:"databaseName"`
	// Custom HTTP headers
	HttpHeaders map[string]string `pulumi:"httpHeaders"`
	// Whether to set the data source as default. This should only be `true` to a single data source. Defaults to `false`.
	IsDefault *bool `pulumi:"isDefault"`
	// Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
	JsonDataEncoded *string `pulumi:"jsonDataEncoded"`
	// A unique name for the data source.
	Name *string `pulumi:"name"`
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId *string `pulumi:"orgId"`
	// Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
	SecureJsonDataEncoded *string `pulumi:"secureJsonDataEncoded"`
	// The data source type. Must be one of the supported data source keywords.
	Type string `pulumi:"type"`
	// Unique identifier. If unset, this will be automatically generated.
	Uid *string `pulumi:"uid"`
	// The URL for the data source. The type of URL required varies depending on the chosen data source type.
	Url *string `pulumi:"url"`
	// (Required by some data source types) The username to use to authenticate to the data source. Defaults to ``.
	Username *string `pulumi:"username"`
}

// The set of arguments for constructing a DataSource resource.
type DataSourceArgs struct {
	// The method by which Grafana will access the data source: `proxy` or `direct`. Defaults to `proxy`.
	AccessMode pulumi.StringPtrInput
	// Whether to enable basic auth for the data source. Defaults to `false`.
	BasicAuthEnabled pulumi.BoolPtrInput
	// Basic auth username. Defaults to ``.
	BasicAuthUsername pulumi.StringPtrInput
	// (Required by some data source types) The name of the database to use on the selected data source server. Defaults to ``.
	DatabaseName pulumi.StringPtrInput
	// Custom HTTP headers
	HttpHeaders pulumi.StringMapInput
	// Whether to set the data source as default. This should only be `true` to a single data source. Defaults to `false`.
	IsDefault pulumi.BoolPtrInput
	// Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
	JsonDataEncoded pulumi.StringPtrInput
	// A unique name for the data source.
	Name pulumi.StringPtrInput
	// The Organization ID. If not set, the Org ID defined in the provider block will be used.
	OrgId pulumi.StringPtrInput
	// Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
	SecureJsonDataEncoded pulumi.StringPtrInput
	// The data source type. Must be one of the supported data source keywords.
	Type pulumi.StringInput
	// Unique identifier. If unset, this will be automatically generated.
	Uid pulumi.StringPtrInput
	// The URL for the data source. The type of URL required varies depending on the chosen data source type.
	Url pulumi.StringPtrInput
	// (Required by some data source types) The username to use to authenticate to the data source. Defaults to ``.
	Username pulumi.StringPtrInput
}

func (DataSourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dataSourceArgs)(nil)).Elem()
}

type DataSourceInput interface {
	pulumi.Input

	ToDataSourceOutput() DataSourceOutput
	ToDataSourceOutputWithContext(ctx context.Context) DataSourceOutput
}

func (*DataSource) ElementType() reflect.Type {
	return reflect.TypeOf((**DataSource)(nil)).Elem()
}

func (i *DataSource) ToDataSourceOutput() DataSourceOutput {
	return i.ToDataSourceOutputWithContext(context.Background())
}

func (i *DataSource) ToDataSourceOutputWithContext(ctx context.Context) DataSourceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataSourceOutput)
}

func (i *DataSource) ToOutput(ctx context.Context) pulumix.Output[*DataSource] {
	return pulumix.Output[*DataSource]{
		OutputState: i.ToDataSourceOutputWithContext(ctx).OutputState,
	}
}

// DataSourceArrayInput is an input type that accepts DataSourceArray and DataSourceArrayOutput values.
// You can construct a concrete instance of `DataSourceArrayInput` via:
//
//	DataSourceArray{ DataSourceArgs{...} }
type DataSourceArrayInput interface {
	pulumi.Input

	ToDataSourceArrayOutput() DataSourceArrayOutput
	ToDataSourceArrayOutputWithContext(context.Context) DataSourceArrayOutput
}

type DataSourceArray []DataSourceInput

func (DataSourceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DataSource)(nil)).Elem()
}

func (i DataSourceArray) ToDataSourceArrayOutput() DataSourceArrayOutput {
	return i.ToDataSourceArrayOutputWithContext(context.Background())
}

func (i DataSourceArray) ToDataSourceArrayOutputWithContext(ctx context.Context) DataSourceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataSourceArrayOutput)
}

func (i DataSourceArray) ToOutput(ctx context.Context) pulumix.Output[[]*DataSource] {
	return pulumix.Output[[]*DataSource]{
		OutputState: i.ToDataSourceArrayOutputWithContext(ctx).OutputState,
	}
}

// DataSourceMapInput is an input type that accepts DataSourceMap and DataSourceMapOutput values.
// You can construct a concrete instance of `DataSourceMapInput` via:
//
//	DataSourceMap{ "key": DataSourceArgs{...} }
type DataSourceMapInput interface {
	pulumi.Input

	ToDataSourceMapOutput() DataSourceMapOutput
	ToDataSourceMapOutputWithContext(context.Context) DataSourceMapOutput
}

type DataSourceMap map[string]DataSourceInput

func (DataSourceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DataSource)(nil)).Elem()
}

func (i DataSourceMap) ToDataSourceMapOutput() DataSourceMapOutput {
	return i.ToDataSourceMapOutputWithContext(context.Background())
}

func (i DataSourceMap) ToDataSourceMapOutputWithContext(ctx context.Context) DataSourceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DataSourceMapOutput)
}

func (i DataSourceMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*DataSource] {
	return pulumix.Output[map[string]*DataSource]{
		OutputState: i.ToDataSourceMapOutputWithContext(ctx).OutputState,
	}
}

type DataSourceOutput struct{ *pulumi.OutputState }

func (DataSourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DataSource)(nil)).Elem()
}

func (o DataSourceOutput) ToDataSourceOutput() DataSourceOutput {
	return o
}

func (o DataSourceOutput) ToDataSourceOutputWithContext(ctx context.Context) DataSourceOutput {
	return o
}

func (o DataSourceOutput) ToOutput(ctx context.Context) pulumix.Output[*DataSource] {
	return pulumix.Output[*DataSource]{
		OutputState: o.OutputState,
	}
}

// The method by which Grafana will access the data source: `proxy` or `direct`. Defaults to `proxy`.
func (o DataSourceOutput) AccessMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringPtrOutput { return v.AccessMode }).(pulumi.StringPtrOutput)
}

// Whether to enable basic auth for the data source. Defaults to `false`.
func (o DataSourceOutput) BasicAuthEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.BoolPtrOutput { return v.BasicAuthEnabled }).(pulumi.BoolPtrOutput)
}

// Basic auth username. Defaults to “.
func (o DataSourceOutput) BasicAuthUsername() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringPtrOutput { return v.BasicAuthUsername }).(pulumi.StringPtrOutput)
}

// (Required by some data source types) The name of the database to use on the selected data source server. Defaults to “.
func (o DataSourceOutput) DatabaseName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringPtrOutput { return v.DatabaseName }).(pulumi.StringPtrOutput)
}

// Custom HTTP headers
func (o DataSourceOutput) HttpHeaders() pulumi.StringMapOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringMapOutput { return v.HttpHeaders }).(pulumi.StringMapOutput)
}

// Whether to set the data source as default. This should only be `true` to a single data source. Defaults to `false`.
func (o DataSourceOutput) IsDefault() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.BoolPtrOutput { return v.IsDefault }).(pulumi.BoolPtrOutput)
}

// Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
func (o DataSourceOutput) JsonDataEncoded() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringPtrOutput { return v.JsonDataEncoded }).(pulumi.StringPtrOutput)
}

// A unique name for the data source.
func (o DataSourceOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The Organization ID. If not set, the Org ID defined in the provider block will be used.
func (o DataSourceOutput) OrgId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringPtrOutput { return v.OrgId }).(pulumi.StringPtrOutput)
}

// Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.
func (o DataSourceOutput) SecureJsonDataEncoded() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringPtrOutput { return v.SecureJsonDataEncoded }).(pulumi.StringPtrOutput)
}

// The data source type. Must be one of the supported data source keywords.
func (o DataSourceOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// Unique identifier. If unset, this will be automatically generated.
func (o DataSourceOutput) Uid() pulumi.StringOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringOutput { return v.Uid }).(pulumi.StringOutput)
}

// The URL for the data source. The type of URL required varies depending on the chosen data source type.
func (o DataSourceOutput) Url() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringPtrOutput { return v.Url }).(pulumi.StringPtrOutput)
}

// (Required by some data source types) The username to use to authenticate to the data source. Defaults to “.
func (o DataSourceOutput) Username() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DataSource) pulumi.StringPtrOutput { return v.Username }).(pulumi.StringPtrOutput)
}

type DataSourceArrayOutput struct{ *pulumi.OutputState }

func (DataSourceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DataSource)(nil)).Elem()
}

func (o DataSourceArrayOutput) ToDataSourceArrayOutput() DataSourceArrayOutput {
	return o
}

func (o DataSourceArrayOutput) ToDataSourceArrayOutputWithContext(ctx context.Context) DataSourceArrayOutput {
	return o
}

func (o DataSourceArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*DataSource] {
	return pulumix.Output[[]*DataSource]{
		OutputState: o.OutputState,
	}
}

func (o DataSourceArrayOutput) Index(i pulumi.IntInput) DataSourceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *DataSource {
		return vs[0].([]*DataSource)[vs[1].(int)]
	}).(DataSourceOutput)
}

type DataSourceMapOutput struct{ *pulumi.OutputState }

func (DataSourceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DataSource)(nil)).Elem()
}

func (o DataSourceMapOutput) ToDataSourceMapOutput() DataSourceMapOutput {
	return o
}

func (o DataSourceMapOutput) ToDataSourceMapOutputWithContext(ctx context.Context) DataSourceMapOutput {
	return o
}

func (o DataSourceMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*DataSource] {
	return pulumix.Output[map[string]*DataSource]{
		OutputState: o.OutputState,
	}
}

func (o DataSourceMapOutput) MapIndex(k pulumi.StringInput) DataSourceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *DataSource {
		return vs[0].(map[string]*DataSource)[vs[1].(string)]
	}).(DataSourceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DataSourceInput)(nil)).Elem(), &DataSource{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataSourceArrayInput)(nil)).Elem(), DataSourceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DataSourceMapInput)(nil)).Elem(), DataSourceMap{})
	pulumi.RegisterOutputType(DataSourceOutput{})
	pulumi.RegisterOutputType(DataSourceArrayOutput{})
	pulumi.RegisterOutputType(DataSourceMapOutput{})
}
