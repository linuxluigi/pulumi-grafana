// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Lbrlabs.PulumiPackage.Grafana.Inputs
{

    public sealed class SLOAlertingSlowburnArgs : global::Pulumi.ResourceArgs
    {
        [Input("annotations")]
        private InputList<Inputs.SLOAlertingSlowburnAnnotationArgs>? _annotations;

        /// <summary>
        /// Annotations will be attached to all alerts generated by any of these rules.
        /// </summary>
        public InputList<Inputs.SLOAlertingSlowburnAnnotationArgs> Annotations
        {
            get => _annotations ?? (_annotations = new InputList<Inputs.SLOAlertingSlowburnAnnotationArgs>());
            set => _annotations = value;
        }

        [Input("labels")]
        private InputList<Inputs.SLOAlertingSlowburnLabelArgs>? _labels;

        /// <summary>
        /// Labels to attach only to Fast Burn alerts.
        /// </summary>
        public InputList<Inputs.SLOAlertingSlowburnLabelArgs> Labels
        {
            get => _labels ?? (_labels = new InputList<Inputs.SLOAlertingSlowburnLabelArgs>());
            set => _labels = value;
        }

        public SLOAlertingSlowburnArgs()
        {
        }
        public static new SLOAlertingSlowburnArgs Empty => new SLOAlertingSlowburnArgs();
    }
}
