// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Slo.Outputs
{

    [OutputType]
    public sealed class GetSlosSloQueryRatioResult
    {
        /// <summary>
        /// Defines Group By Labels used for per-label alerting. These appear as variables on SLO dashboards to enable filtering and aggregation. Labels must adhere to Prometheus label name schema - "^[a-zA-Z_][a-zA-Z0-9_]*$"
        /// </summary>
        public readonly ImmutableArray<string> GroupByLabels;
        /// <summary>
        /// Counter metric for success events (numerator)
        /// </summary>
        public readonly string SuccessMetric;
        /// <summary>
        /// Metric for total events (denominator)
        /// </summary>
        public readonly string TotalMetric;

        [OutputConstructor]
        private GetSlosSloQueryRatioResult(
            ImmutableArray<string> groupByLabels,

            string successMetric,

            string totalMetric)
        {
            GroupByLabels = groupByLabels;
            SuccessMetric = successMetric;
            TotalMetric = totalMetric;
        }
    }
}
