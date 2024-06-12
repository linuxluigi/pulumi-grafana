// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Inputs
{

    public sealed class SyntheticMonitoringCheckSettingsMultihttpEntryRequestHeaderGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the header to send
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// The value of the assertion
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public SyntheticMonitoringCheckSettingsMultihttpEntryRequestHeaderGetArgs()
        {
        }
        public static new SyntheticMonitoringCheckSettingsMultihttpEntryRequestHeaderGetArgs Empty => new SyntheticMonitoringCheckSettingsMultihttpEntryRequestHeaderGetArgs();
    }
}
