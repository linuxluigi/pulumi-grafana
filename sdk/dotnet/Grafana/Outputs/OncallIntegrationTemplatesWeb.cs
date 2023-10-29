// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs.PulumiPackage.Grafana.Outputs
{

    [OutputType]
    public sealed class OncallIntegrationTemplatesWeb
    {
        /// <summary>
        /// Template for Alert image url.
        /// </summary>
        public readonly string? ImageUrl;
        /// <summary>
        /// Template for Alert message.
        /// </summary>
        public readonly string? Message;
        /// <summary>
        /// Template for Alert title.
        /// </summary>
        public readonly string? Title;

        [OutputConstructor]
        private OncallIntegrationTemplatesWeb(
            string? imageUrl,

            string? message,

            string? title)
        {
            ImageUrl = imageUrl;
            Message = message;
            Title = title;
        }
    }
}
