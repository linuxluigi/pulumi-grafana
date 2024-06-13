// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Grafana.Alerting.Inputs
{

    public sealed class MuteTimingIntervalGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("daysOfMonths")]
        private InputList<string>? _daysOfMonths;

        /// <summary>
        /// An inclusive range of days, 1-31, within a month, e.g. "1" or "14:16". Negative values can be used to represent days counting from the end of a month, e.g. "-1".
        /// </summary>
        public InputList<string> DaysOfMonths
        {
            get => _daysOfMonths ?? (_daysOfMonths = new InputList<string>());
            set => _daysOfMonths = value;
        }

        /// <summary>
        /// Provides the time zone for the time interval. Must be a location in the IANA time zone database, e.g "America/New_York"
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        [Input("months")]
        private InputList<string>? _months;

        /// <summary>
        /// An inclusive range of months, either numerical or full calendar month, e.g. "1:3", "december", or "may:august".
        /// </summary>
        public InputList<string> Months
        {
            get => _months ?? (_months = new InputList<string>());
            set => _months = value;
        }

        [Input("times")]
        private InputList<Inputs.MuteTimingIntervalTimeGetArgs>? _times;

        /// <summary>
        /// The time ranges, represented in minutes, during which to mute in a given day.
        /// </summary>
        public InputList<Inputs.MuteTimingIntervalTimeGetArgs> Times
        {
            get => _times ?? (_times = new InputList<Inputs.MuteTimingIntervalTimeGetArgs>());
            set => _times = value;
        }

        [Input("weekdays")]
        private InputList<string>? _weekdays;

        /// <summary>
        /// An inclusive range of weekdays, e.g. "monday" or "tuesday:thursday".
        /// </summary>
        public InputList<string> Weekdays
        {
            get => _weekdays ?? (_weekdays = new InputList<string>());
            set => _weekdays = value;
        }

        [Input("years")]
        private InputList<string>? _years;

        /// <summary>
        /// A positive inclusive range of years, e.g. "2030" or "2025:2026".
        /// </summary>
        public InputList<string> Years
        {
            get => _years ?? (_years = new InputList<string>());
            set => _years = value;
        }

        public MuteTimingIntervalGetArgs()
        {
        }
        public static new MuteTimingIntervalGetArgs Empty => new MuteTimingIntervalGetArgs();
    }
}
