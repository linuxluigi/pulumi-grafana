// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Slo.Inputs
{

    public sealed class SLOQueryRatioGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("groupByLabels")]
        private InputList<string>? _groupByLabels;

        /// <summary>
        /// Defines Group By Labels used for per-label alerting. These appear as variables on SLO dashboards to enable filtering and aggregation. Labels must adhere to Prometheus label name schema - "^[a-zA-Z*][a-zA-Z0-9*]*$"
        /// </summary>
        public InputList<string> GroupByLabels
        {
            get => _groupByLabels ?? (_groupByLabels = new InputList<string>());
            set => _groupByLabels = value;
        }

        /// <summary>
        /// Counter metric for success events (numerator)
        /// </summary>
        [Input("successMetric", required: true)]
        public Input<string> SuccessMetric { get; set; } = null!;

        /// <summary>
        /// Metric for total events (denominator)
        /// </summary>
        [Input("totalMetric", required: true)]
        public Input<string> TotalMetric { get; set; } = null!;

        public SLOQueryRatioGetArgs()
        {
        }
        public static new SLOQueryRatioGetArgs Empty => new SLOQueryRatioGetArgs();
    }
}
