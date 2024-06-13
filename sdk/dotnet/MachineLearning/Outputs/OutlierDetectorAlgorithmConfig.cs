// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.MachineLearning.Outputs
{

    [OutputType]
    public sealed class OutlierDetectorAlgorithmConfig
    {
        /// <summary>
        /// Specify the epsilon parameter (positive float)
        /// </summary>
        public readonly double Epsilon;

        [OutputConstructor]
        private OutlierDetectorAlgorithmConfig(double epsilon)
        {
            Epsilon = epsilon;
        }
    }
}
