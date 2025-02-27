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
    'AdminCredentialsArgs',
    'MigrationSecretParametersArgs',
]

@pulumi.input_type
class AdminCredentialsArgs:
    def __init__(__self__, *,
                 source_server_password: pulumi.Input[str],
                 target_server_password: pulumi.Input[str]):
        """
        Server admin credentials.
        """
        pulumi.set(__self__, "source_server_password", source_server_password)
        pulumi.set(__self__, "target_server_password", target_server_password)

    @property
    @pulumi.getter(name="sourceServerPassword")
    def source_server_password(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source_server_password")

    @source_server_password.setter
    def source_server_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_server_password", value)

    @property
    @pulumi.getter(name="targetServerPassword")
    def target_server_password(self) -> pulumi.Input[str]:
        return pulumi.get(self, "target_server_password")

    @target_server_password.setter
    def target_server_password(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_server_password", value)


@pulumi.input_type
class MigrationSecretParametersArgs:
    def __init__(__self__, *,
                 admin_credentials: pulumi.Input['AdminCredentialsArgs']):
        """
        Migration secret parameters.
        :param pulumi.Input['AdminCredentialsArgs'] admin_credentials: Server admin credentials.
        """
        pulumi.set(__self__, "admin_credentials", admin_credentials)

    @property
    @pulumi.getter(name="adminCredentials")
    def admin_credentials(self) -> pulumi.Input['AdminCredentialsArgs']:
        """
        Server admin credentials.
        """
        return pulumi.get(self, "admin_credentials")

    @admin_credentials.setter
    def admin_credentials(self, value: pulumi.Input['AdminCredentialsArgs']):
        pulumi.set(self, "admin_credentials", value)


