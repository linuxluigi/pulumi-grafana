// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * * [Official documentation](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/access-control/)
 * * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/folder_permissions/)
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as grafana from "@lbrlabs/pulumi-grafana";
 *
 * const team = new grafana.Team("team", {});
 * const user = new grafana.User("user", {email: "user.name@example.com"});
 * const collection = new grafana.Folder("collection", {title: "Folder Title"});
 * const collectionPermission = new grafana.FolderPermission("collectionPermission", {
 *     folderUid: collection.uid,
 *     permissions: [
 *         {
 *             role: "Editor",
 *             permission: "Edit",
 *         },
 *         {
 *             teamId: team.id,
 *             permission: "View",
 *         },
 *         {
 *             userId: user.id,
 *             permission: "Admin",
 *         },
 *     ],
 * });
 * ```
 */
export class FolderPermission extends pulumi.CustomResource {
    /**
     * Get an existing FolderPermission resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FolderPermissionState, opts?: pulumi.CustomResourceOptions): FolderPermission {
        return new FolderPermission(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'grafana:index/folderPermission:FolderPermission';

    /**
     * Returns true if the given object is an instance of FolderPermission.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FolderPermission {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FolderPermission.__pulumiType;
    }

    /**
     * The UID of the folder.
     */
    public readonly folderUid!: pulumi.Output<string>;
    /**
     * The permission items to add/update. Items that are omitted from the list will be removed.
     */
    public readonly permissions!: pulumi.Output<outputs.FolderPermissionPermission[]>;

    /**
     * Create a FolderPermission resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FolderPermissionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FolderPermissionArgs | FolderPermissionState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as FolderPermissionState | undefined;
            resourceInputs["folderUid"] = state ? state.folderUid : undefined;
            resourceInputs["permissions"] = state ? state.permissions : undefined;
        } else {
            const args = argsOrState as FolderPermissionArgs | undefined;
            if ((!args || args.folderUid === undefined) && !opts.urn) {
                throw new Error("Missing required property 'folderUid'");
            }
            if ((!args || args.permissions === undefined) && !opts.urn) {
                throw new Error("Missing required property 'permissions'");
            }
            resourceInputs["folderUid"] = args ? args.folderUid : undefined;
            resourceInputs["permissions"] = args ? args.permissions : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(FolderPermission.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering FolderPermission resources.
 */
export interface FolderPermissionState {
    /**
     * The UID of the folder.
     */
    folderUid?: pulumi.Input<string>;
    /**
     * The permission items to add/update. Items that are omitted from the list will be removed.
     */
    permissions?: pulumi.Input<pulumi.Input<inputs.FolderPermissionPermission>[]>;
}

/**
 * The set of arguments for constructing a FolderPermission resource.
 */
export interface FolderPermissionArgs {
    /**
     * The UID of the folder.
     */
    folderUid: pulumi.Input<string>;
    /**
     * The permission items to add/update. Items that are omitted from the list will be removed.
     */
    permissions: pulumi.Input<pulumi.Input<inputs.FolderPermissionPermission>[]>;
}
