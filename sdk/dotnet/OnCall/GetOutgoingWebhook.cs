// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.OnCall
{
    public static class GetOutgoingWebhook
    {
        /// <summary>
        /// * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/outgoing_webhooks/)
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Grafana = Pulumi.Grafana;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var exampleOutgoingWebhook = Grafana.OnCall.GetOutgoingWebhook.Invoke(new()
        ///     {
        ///         Name = "example_outgoing_webhook",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Task<GetOutgoingWebhookResult> InvokeAsync(GetOutgoingWebhookArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetOutgoingWebhookResult>("grafana:onCall/getOutgoingWebhook:getOutgoingWebhook", args ?? new GetOutgoingWebhookArgs(), options.WithDefaults());

        /// <summary>
        /// * [HTTP API](https://grafana.com/docs/oncall/latest/oncall-api-reference/outgoing_webhooks/)
        /// 
        /// ## Example Usage
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Grafana = Pulumi.Grafana;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var exampleOutgoingWebhook = Grafana.OnCall.GetOutgoingWebhook.Invoke(new()
        ///     {
        ///         Name = "example_outgoing_webhook",
        ///     });
        /// 
        /// });
        /// ```
        /// </summary>
        public static Output<GetOutgoingWebhookResult> Invoke(GetOutgoingWebhookInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetOutgoingWebhookResult>("grafana:onCall/getOutgoingWebhook:getOutgoingWebhook", args ?? new GetOutgoingWebhookInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetOutgoingWebhookArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The outgoing webhook name.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetOutgoingWebhookArgs()
        {
        }
        public static new GetOutgoingWebhookArgs Empty => new GetOutgoingWebhookArgs();
    }

    public sealed class GetOutgoingWebhookInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The outgoing webhook name.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetOutgoingWebhookInvokeArgs()
        {
        }
        public static new GetOutgoingWebhookInvokeArgs Empty => new GetOutgoingWebhookInvokeArgs();
    }


    [OutputType]
    public sealed class GetOutgoingWebhookResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The outgoing webhook name.
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private GetOutgoingWebhookResult(
            string id,

            string name)
        {
            Id = id;
            Name = name;
        }
    }
}
