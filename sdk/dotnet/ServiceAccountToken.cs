// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana
{
    /// <summary>
    /// **Note:** This resource is available only with Grafana 9.1+.
    /// 
    /// * [Official documentation](https://grafana.com/docs/grafana/latest/administration/service-accounts/)
    /// * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/serviceaccount/#service-account-api)
    /// 
    /// ## Example Usage
    /// 
    /// &lt;!--Start PulumiCodeChooser --&gt;
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Grafana = Pulumiverse.Grafana;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var test = new Grafana.ServiceAccount("test", new()
    ///     {
    ///         Role = "Viewer",
    ///     });
    /// 
    ///     var foo = new Grafana.ServiceAccountToken("foo", new()
    ///     {
    ///         ServiceAccountId = test.Id,
    ///     });
    /// 
    ///     var bar = new Grafana.ServiceAccountToken("bar", new()
    ///     {
    ///         ServiceAccountId = test.Id,
    ///         SecondsToLive = 30,
    ///     });
    /// 
    ///     return new Dictionary&lt;string, object?&gt;
    ///     {
    ///         ["serviceAccountTokenFooKeyOnly"] = foo.Key,
    ///         ["serviceAccountTokenBar"] = bar,
    ///     };
    /// });
    /// ```
    /// &lt;!--End PulumiCodeChooser --&gt;
    /// </summary>
    [GrafanaResourceType("grafana:index/serviceAccountToken:ServiceAccountToken")]
    public partial class ServiceAccountToken : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The expiration date of the service account token.
        /// </summary>
        [Output("expiration")]
        public Output<string> Expiration { get; private set; } = null!;

        /// <summary>
        /// The status of the service account token.
        /// </summary>
        [Output("hasExpired")]
        public Output<bool> HasExpired { get; private set; } = null!;

        /// <summary>
        /// The key of the service account token.
        /// </summary>
        [Output("key")]
        public Output<string> Key { get; private set; } = null!;

        /// <summary>
        /// The name of the service account token.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The key expiration in seconds. It is optional. If it is a positive number an expiration date for the key is set. If it is null, zero or is omitted completely (unless `api_key_max_seconds_to_live` configuration option is set) the key will never expire.
        /// </summary>
        [Output("secondsToLive")]
        public Output<int?> SecondsToLive { get; private set; } = null!;

        /// <summary>
        /// The ID of the service account to which the token belongs.
        /// </summary>
        [Output("serviceAccountId")]
        public Output<string> ServiceAccountId { get; private set; } = null!;


        /// <summary>
        /// Create a ServiceAccountToken resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServiceAccountToken(string name, ServiceAccountTokenArgs args, CustomResourceOptions? options = null)
            : base("grafana:index/serviceAccountToken:ServiceAccountToken", name, args ?? new ServiceAccountTokenArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ServiceAccountToken(string name, Input<string> id, ServiceAccountTokenState? state = null, CustomResourceOptions? options = null)
            : base("grafana:index/serviceAccountToken:ServiceAccountToken", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
                AdditionalSecretOutputs =
                {
                    "key",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ServiceAccountToken resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServiceAccountToken Get(string name, Input<string> id, ServiceAccountTokenState? state = null, CustomResourceOptions? options = null)
        {
            return new ServiceAccountToken(name, id, state, options);
        }
    }

    public sealed class ServiceAccountTokenArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the service account token.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The key expiration in seconds. It is optional. If it is a positive number an expiration date for the key is set. If it is null, zero or is omitted completely (unless `api_key_max_seconds_to_live` configuration option is set) the key will never expire.
        /// </summary>
        [Input("secondsToLive")]
        public Input<int>? SecondsToLive { get; set; }

        /// <summary>
        /// The ID of the service account to which the token belongs.
        /// </summary>
        [Input("serviceAccountId", required: true)]
        public Input<string> ServiceAccountId { get; set; } = null!;

        public ServiceAccountTokenArgs()
        {
        }
        public static new ServiceAccountTokenArgs Empty => new ServiceAccountTokenArgs();
    }

    public sealed class ServiceAccountTokenState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The expiration date of the service account token.
        /// </summary>
        [Input("expiration")]
        public Input<string>? Expiration { get; set; }

        /// <summary>
        /// The status of the service account token.
        /// </summary>
        [Input("hasExpired")]
        public Input<bool>? HasExpired { get; set; }

        [Input("key")]
        private Input<string>? _key;

        /// <summary>
        /// The key of the service account token.
        /// </summary>
        public Input<string>? Key
        {
            get => _key;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _key = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The name of the service account token.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The key expiration in seconds. It is optional. If it is a positive number an expiration date for the key is set. If it is null, zero or is omitted completely (unless `api_key_max_seconds_to_live` configuration option is set) the key will never expire.
        /// </summary>
        [Input("secondsToLive")]
        public Input<int>? SecondsToLive { get; set; }

        /// <summary>
        /// The ID of the service account to which the token belongs.
        /// </summary>
        [Input("serviceAccountId")]
        public Input<string>? ServiceAccountId { get; set; }

        public ServiceAccountTokenState()
        {
        }
        public static new ServiceAccountTokenState Empty => new ServiceAccountTokenState();
    }
}
