# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'ListDataProductRolesAssignmentsResult',
    'AwaitableListDataProductRolesAssignmentsResult',
    'list_data_product_roles_assignments',
    'list_data_product_roles_assignments_output',
]

@pulumi.output_type
class ListDataProductRolesAssignmentsResult:
    """
    list role assignments.
    """
    def __init__(__self__, count=None, role_assignment_response=None):
        if count and not isinstance(count, int):
            raise TypeError("Expected argument 'count' to be a int")
        pulumi.set(__self__, "count", count)
        if role_assignment_response and not isinstance(role_assignment_response, list):
            raise TypeError("Expected argument 'role_assignment_response' to be a list")
        pulumi.set(__self__, "role_assignment_response", role_assignment_response)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        Count of role assignments.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="roleAssignmentResponse")
    def role_assignment_response(self) -> Sequence['outputs.RoleAssignmentDetailResponse']:
        """
        list of role assignments
        """
        return pulumi.get(self, "role_assignment_response")


class AwaitableListDataProductRolesAssignmentsResult(ListDataProductRolesAssignmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListDataProductRolesAssignmentsResult(
            count=self.count,
            role_assignment_response=self.role_assignment_response)


def list_data_product_roles_assignments(data_product_name: Optional[str] = None,
                                        resource_group_name: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListDataProductRolesAssignmentsResult:
    """
    List user roles associated with the data product.


    :param str data_product_name: The data product resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['dataProductName'] = data_product_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:networkanalytics/v20231115:listDataProductRolesAssignments', __args__, opts=opts, typ=ListDataProductRolesAssignmentsResult).value

    return AwaitableListDataProductRolesAssignmentsResult(
        count=pulumi.get(__ret__, 'count'),
        role_assignment_response=pulumi.get(__ret__, 'role_assignment_response'))


@_utilities.lift_output_func(list_data_product_roles_assignments)
def list_data_product_roles_assignments_output(data_product_name: Optional[pulumi.Input[str]] = None,
                                               resource_group_name: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListDataProductRolesAssignmentsResult]:
    """
    List user roles associated with the data product.


    :param str data_product_name: The data product resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
