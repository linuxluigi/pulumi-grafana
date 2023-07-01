# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetFoldersResult',
    'AwaitableGetFoldersResult',
    'get_folders',
]

@pulumi.output_type
class GetFoldersResult:
    """
    A collection of values returned by getFolders.
    """
    def __init__(__self__, folders=None, id=None):
        if folders and not isinstance(folders, list):
            raise TypeError("Expected argument 'folders' to be a list")
        pulumi.set(__self__, "folders", folders)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def folders(self) -> Sequence['outputs.GetFoldersFolderResult']:
        """
        The Grafana instance's folders.
        """
        return pulumi.get(self, "folders")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetFoldersResult(GetFoldersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFoldersResult(
            folders=self.folders,
            id=self.id)


def get_folders(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFoldersResult:
    """
    * [Official documentation](https://grafana.com/docs/grafana/latest/dashboards/manage-dashboards/)
    * [HTTP API](https://grafana.com/docs/grafana/latest/developers/http_api/folder/)

    ## Example Usage

    ```python
    import pulumi
    import lbrlabs_pulumi_grafana as grafana
    import pulumi_grafana as grafana

    test_a = grafana.Folder("testA",
        title="test-folder-a",
        uid="test-ds-folder-uid-a")
    test_b = grafana.Folder("testB",
        title="test-folder-b",
        uid="test-ds-folder-uid-b")
    test = grafana.get_folders()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('grafana:index/getFolders:getFolders', __args__, opts=opts, typ=GetFoldersResult).value

    return AwaitableGetFoldersResult(
        folders=pulumi.get(__ret__, 'folders'),
        id=pulumi.get(__ret__, 'id'))
