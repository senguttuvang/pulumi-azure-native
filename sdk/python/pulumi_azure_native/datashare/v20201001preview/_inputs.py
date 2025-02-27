# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'ADLSGen2StorageAccountPathArgs',
    'BlobStorageAccountPathArgs',
]

@pulumi.input_type
class ADLSGen2StorageAccountPathArgs:
    def __init__(__self__, *,
                 container_name: pulumi.Input[str],
                 consumer_path: Optional[pulumi.Input[str]] = None,
                 provider_path: Optional[pulumi.Input[str]] = None):
        """
        Defines a single ADLS Gen2 storage account path.
        :param pulumi.Input[str] container_name: Gets or sets the container name to share.
        :param pulumi.Input[str] consumer_path: Gets or sets the path on the consumer side where the dataset is to be mapped.
        :param pulumi.Input[str] provider_path: Gets or sets the path to file/folder within the container.
        """
        pulumi.set(__self__, "container_name", container_name)
        if consumer_path is not None:
            pulumi.set(__self__, "consumer_path", consumer_path)
        if provider_path is not None:
            pulumi.set(__self__, "provider_path", provider_path)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[str]:
        """
        Gets or sets the container name to share.
        """
        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter(name="consumerPath")
    def consumer_path(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the path on the consumer side where the dataset is to be mapped.
        """
        return pulumi.get(self, "consumer_path")

    @consumer_path.setter
    def consumer_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "consumer_path", value)

    @property
    @pulumi.getter(name="providerPath")
    def provider_path(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the path to file/folder within the container.
        """
        return pulumi.get(self, "provider_path")

    @provider_path.setter
    def provider_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_path", value)


@pulumi.input_type
class BlobStorageAccountPathArgs:
    def __init__(__self__, *,
                 container_name: pulumi.Input[str],
                 consumer_path: Optional[pulumi.Input[str]] = None,
                 provider_path: Optional[pulumi.Input[str]] = None):
        """
        Defines a single blob storage account path.
        :param pulumi.Input[str] container_name: Gets or sets the container name to share.
        :param pulumi.Input[str] consumer_path: Gets or sets the path on the consumer side where the dataset is to be mapped.
        :param pulumi.Input[str] provider_path: Gets or sets the path to file/folder within the container.
        """
        pulumi.set(__self__, "container_name", container_name)
        if consumer_path is not None:
            pulumi.set(__self__, "consumer_path", consumer_path)
        if provider_path is not None:
            pulumi.set(__self__, "provider_path", provider_path)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[str]:
        """
        Gets or sets the container name to share.
        """
        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter(name="consumerPath")
    def consumer_path(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the path on the consumer side where the dataset is to be mapped.
        """
        return pulumi.get(self, "consumer_path")

    @consumer_path.setter
    def consumer_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "consumer_path", value)

    @property
    @pulumi.getter(name="providerPath")
    def provider_path(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the path to file/folder within the container.
        """
        return pulumi.get(self, "provider_path")

    @provider_path.setter
    def provider_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provider_path", value)


