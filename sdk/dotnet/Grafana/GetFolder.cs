// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs.PulumiPackage.Grafana
{
    public static class GetFolder
    {
        /// <summary>
        /// * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/dashboard-folders/)
        /// * [HTTP API](https://grafana.com/docs/grafana/latest/http_api/folder/)
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Grafana = Lbrlabs.PulumiPackage.Grafana;
        /// using Grafana = Pulumi.Grafana;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var test = new Grafana.Folder("test", new()
        ///     {
        ///         Title = "test-folder",
        ///         Uid = "test-ds-folder-uid",
        ///     });
        /// 
        ///     var fromTitle = Grafana.GetFolder.Invoke(new()
        ///     {
        ///         Title = test.Title,
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetFolderResult> InvokeAsync(GetFolderArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetFolderResult>("grafana:index/getFolder:getFolder", args ?? new GetFolderArgs(), options.WithDefaults());

        /// <summary>
        /// * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/dashboard-folders/)
        /// * [HTTP API](https://grafana.com/docs/grafana/latest/http_api/folder/)
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using Pulumi;
        /// using Grafana = Lbrlabs.PulumiPackage.Grafana;
        /// using Grafana = Pulumi.Grafana;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var test = new Grafana.Folder("test", new()
        ///     {
        ///         Title = "test-folder",
        ///         Uid = "test-ds-folder-uid",
        ///     });
        /// 
        ///     var fromTitle = Grafana.GetFolder.Invoke(new()
        ///     {
        ///         Title = test.Title,
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetFolderResult> Invoke(GetFolderInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetFolderResult>("grafana:index/getFolder:getFolder", args ?? new GetFolderInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetFolderArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Grafana folder.
        /// </summary>
        [Input("title", required: true)]
        public string Title { get; set; } = null!;

        public GetFolderArgs()
        {
        }
        public static new GetFolderArgs Empty => new GetFolderArgs();
    }

    public sealed class GetFolderInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Grafana folder.
        /// </summary>
        [Input("title", required: true)]
        public Input<string> Title { get; set; } = null!;

        public GetFolderInvokeArgs()
        {
        }
        public static new GetFolderInvokeArgs Empty => new GetFolderInvokeArgs();
    }


    [OutputType]
    public sealed class GetFolderResult
    {
        /// <summary>
        /// The numerical ID of the Grafana folder.
        /// </summary>
        public readonly int Id;
        /// <summary>
        /// The name of the Grafana folder.
        /// </summary>
        public readonly string Title;
        /// <summary>
        /// The uid of the Grafana folder.
        /// </summary>
        public readonly string Uid;
        /// <summary>
        /// The full URL of the folder.
        /// </summary>
        public readonly string Url;

        [OutputConstructor]
        private GetFolderResult(
            int id,

            string title,

            string uid,

            string url)
        {
            Id = id;
            Title = title;
            Uid = uid;
            Url = url;
        }
    }
}
