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
    public sealed class NotificationPolicyPolicyPolicyMatcher
    {
        /// <summary>
        /// The name of the label to match against.
        /// </summary>
        public readonly string Label;
        /// <summary>
        /// The operator to apply when matching values of the given label. Allowed operators are `=` for equality, `!=` for negated equality, `=~` for regex equality, and `!~` for negated regex equality.
        /// </summary>
        public readonly string Match;
        /// <summary>
        /// The label value to match against.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private NotificationPolicyPolicyPolicyMatcher(
            string label,

            string match,

            string value)
        {
            Label = label;
            Match = match;
            Value = value;
        }
    }
}
