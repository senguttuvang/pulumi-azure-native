# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .elastic_san import *
from .get_elastic_san import *
from .get_private_endpoint_connection import *
from .get_volume import *
from .get_volume_group import *
from .get_volume_snapshot import *
from .private_endpoint_connection import *
from .volume import *
from .volume_group import *
from .volume_snapshot import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.elasticsan.v20211120preview as __v20211120preview
    v20211120preview = __v20211120preview
    import pulumi_azure_native.elasticsan.v20221201preview as __v20221201preview
    v20221201preview = __v20221201preview
    import pulumi_azure_native.elasticsan.v20230101 as __v20230101
    v20230101 = __v20230101
    import pulumi_azure_native.elasticsan.v20240501 as __v20240501
    v20240501 = __v20240501
else:
    v20211120preview = _utilities.lazy_import('pulumi_azure_native.elasticsan.v20211120preview')
    v20221201preview = _utilities.lazy_import('pulumi_azure_native.elasticsan.v20221201preview')
    v20230101 = _utilities.lazy_import('pulumi_azure_native.elasticsan.v20230101')
    v20240501 = _utilities.lazy_import('pulumi_azure_native.elasticsan.v20240501')

