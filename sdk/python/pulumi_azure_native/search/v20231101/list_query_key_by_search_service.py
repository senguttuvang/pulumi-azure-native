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
    'ListQueryKeyBySearchServiceResult',
    'AwaitableListQueryKeyBySearchServiceResult',
    'list_query_key_by_search_service',
    'list_query_key_by_search_service_output',
]

@pulumi.output_type
class ListQueryKeyBySearchServiceResult:
    """
    Response containing the query API keys for a given search service.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> str:
        """
        Request URL that can be used to query next page of query keys. Returned when the total number of requested query keys exceed maximum page size.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.QueryKeyResponse']:
        """
        The query keys for the search service.
        """
        return pulumi.get(self, "value")


class AwaitableListQueryKeyBySearchServiceResult(ListQueryKeyBySearchServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListQueryKeyBySearchServiceResult(
            next_link=self.next_link,
            value=self.value)


def list_query_key_by_search_service(resource_group_name: Optional[str] = None,
                                     search_service_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListQueryKeyBySearchServiceResult:
    """
    Returns the list of query API keys for the given search service.


    :param str resource_group_name: The name of the resource group within the current subscription. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str search_service_name: The name of the search service associated with the specified resource group.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['searchServiceName'] = search_service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:search/v20231101:listQueryKeyBySearchService', __args__, opts=opts, typ=ListQueryKeyBySearchServiceResult).value

    return AwaitableListQueryKeyBySearchServiceResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_query_key_by_search_service)
def list_query_key_by_search_service_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                            search_service_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListQueryKeyBySearchServiceResult]:
    """
    Returns the list of query API keys for the given search service.


    :param str resource_group_name: The name of the resource group within the current subscription. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str search_service_name: The name of the search service associated with the specified resource group.
    """
    ...
