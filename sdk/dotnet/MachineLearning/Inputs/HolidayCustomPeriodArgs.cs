// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.MachineLearning.Inputs
{

    public sealed class HolidayCustomPeriodArgs : global::Pulumi.ResourceArgs
    {
        [Input("endTime", required: true)]
        public Input<string> EndTime { get; set; } = null!;

        /// <summary>
        /// The name of the custom period.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("startTime", required: true)]
        public Input<string> StartTime { get; set; } = null!;

        public HolidayCustomPeriodArgs()
        {
        }
        public static new HolidayCustomPeriodArgs Empty => new HolidayCustomPeriodArgs();
    }
}
