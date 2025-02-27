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
from ._enums import *

__all__ = [
    'AgentPoolUpgradeSettingsResponse',
    'CreationDataResponse',
    'KubeletConfigResponse',
    'LinuxOSConfigResponse',
    'PowerStateResponse',
    'SysctlConfigResponse',
]

@pulumi.output_type
class AgentPoolUpgradeSettingsResponse(dict):
    """
    Settings for upgrading an agentpool
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "maxSurge":
            suggest = "max_surge"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AgentPoolUpgradeSettingsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AgentPoolUpgradeSettingsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AgentPoolUpgradeSettingsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 max_surge: Optional[str] = None):
        """
        Settings for upgrading an agentpool
        :param str max_surge: This can either be set to an integer (e.g. '5') or a percentage (e.g. '50%'). If a percentage is specified, it is the percentage of the total agent pool size at the time of the upgrade. For percentages, fractional nodes are rounded up. If not specified, the default is 1. For more information, including best practices, see: https://docs.microsoft.com/azure/aks/upgrade-cluster#customize-node-surge-upgrade
        """
        if max_surge is not None:
            pulumi.set(__self__, "max_surge", max_surge)

    @property
    @pulumi.getter(name="maxSurge")
    def max_surge(self) -> Optional[str]:
        """
        This can either be set to an integer (e.g. '5') or a percentage (e.g. '50%'). If a percentage is specified, it is the percentage of the total agent pool size at the time of the upgrade. For percentages, fractional nodes are rounded up. If not specified, the default is 1. For more information, including best practices, see: https://docs.microsoft.com/azure/aks/upgrade-cluster#customize-node-surge-upgrade
        """
        return pulumi.get(self, "max_surge")


@pulumi.output_type
class CreationDataResponse(dict):
    """
    Data used when creating a target resource from a source resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "sourceResourceId":
            suggest = "source_resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CreationDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CreationDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CreationDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 source_resource_id: Optional[str] = None):
        """
        Data used when creating a target resource from a source resource.
        :param str source_resource_id: This is the ARM ID of the source object to be used to create the target object.
        """
        if source_resource_id is not None:
            pulumi.set(__self__, "source_resource_id", source_resource_id)

    @property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[str]:
        """
        This is the ARM ID of the source object to be used to create the target object.
        """
        return pulumi.get(self, "source_resource_id")


@pulumi.output_type
class KubeletConfigResponse(dict):
    """
    See [AKS custom node configuration](https://docs.microsoft.com/azure/aks/custom-node-configuration) for more details.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowedUnsafeSysctls":
            suggest = "allowed_unsafe_sysctls"
        elif key == "containerLogMaxFiles":
            suggest = "container_log_max_files"
        elif key == "containerLogMaxSizeMB":
            suggest = "container_log_max_size_mb"
        elif key == "cpuCfsQuota":
            suggest = "cpu_cfs_quota"
        elif key == "cpuCfsQuotaPeriod":
            suggest = "cpu_cfs_quota_period"
        elif key == "cpuManagerPolicy":
            suggest = "cpu_manager_policy"
        elif key == "failSwapOn":
            suggest = "fail_swap_on"
        elif key == "imageGcHighThreshold":
            suggest = "image_gc_high_threshold"
        elif key == "imageGcLowThreshold":
            suggest = "image_gc_low_threshold"
        elif key == "podMaxPids":
            suggest = "pod_max_pids"
        elif key == "topologyManagerPolicy":
            suggest = "topology_manager_policy"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in KubeletConfigResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        KubeletConfigResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        KubeletConfigResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allowed_unsafe_sysctls: Optional[Sequence[str]] = None,
                 container_log_max_files: Optional[int] = None,
                 container_log_max_size_mb: Optional[int] = None,
                 cpu_cfs_quota: Optional[bool] = None,
                 cpu_cfs_quota_period: Optional[str] = None,
                 cpu_manager_policy: Optional[str] = None,
                 fail_swap_on: Optional[bool] = None,
                 image_gc_high_threshold: Optional[int] = None,
                 image_gc_low_threshold: Optional[int] = None,
                 pod_max_pids: Optional[int] = None,
                 topology_manager_policy: Optional[str] = None):
        """
        See [AKS custom node configuration](https://docs.microsoft.com/azure/aks/custom-node-configuration) for more details.
        :param Sequence[str] allowed_unsafe_sysctls: Allowed list of unsafe sysctls or unsafe sysctl patterns (ending in `*`).
        :param int container_log_max_files: The maximum number of container log files that can be present for a container. The number must be ≥ 2.
        :param int container_log_max_size_mb: The maximum size (e.g. 10Mi) of container log file before it is rotated.
        :param bool cpu_cfs_quota: The default is true.
        :param str cpu_cfs_quota_period: The default is '100ms.' Valid values are a sequence of decimal numbers with an optional fraction and a unit suffix. For example: '300ms', '2h45m'. Supported units are 'ns', 'us', 'ms', 's', 'm', and 'h'.
        :param str cpu_manager_policy: The default is 'none'. See [Kubernetes CPU management policies](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#cpu-management-policies) for more information. Allowed values are 'none' and 'static'.
        :param bool fail_swap_on: If set to true it will make the Kubelet fail to start if swap is enabled on the node.
        :param int image_gc_high_threshold: To disable image garbage collection, set to 100. The default is 85%
        :param int image_gc_low_threshold: This cannot be set higher than imageGcHighThreshold. The default is 80%
        :param int pod_max_pids: The maximum number of processes per pod.
        :param str topology_manager_policy: For more information see [Kubernetes Topology Manager](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager). The default is 'none'. Allowed values are 'none', 'best-effort', 'restricted', and 'single-numa-node'.
        """
        if allowed_unsafe_sysctls is not None:
            pulumi.set(__self__, "allowed_unsafe_sysctls", allowed_unsafe_sysctls)
        if container_log_max_files is not None:
            pulumi.set(__self__, "container_log_max_files", container_log_max_files)
        if container_log_max_size_mb is not None:
            pulumi.set(__self__, "container_log_max_size_mb", container_log_max_size_mb)
        if cpu_cfs_quota is not None:
            pulumi.set(__self__, "cpu_cfs_quota", cpu_cfs_quota)
        if cpu_cfs_quota_period is not None:
            pulumi.set(__self__, "cpu_cfs_quota_period", cpu_cfs_quota_period)
        if cpu_manager_policy is not None:
            pulumi.set(__self__, "cpu_manager_policy", cpu_manager_policy)
        if fail_swap_on is not None:
            pulumi.set(__self__, "fail_swap_on", fail_swap_on)
        if image_gc_high_threshold is not None:
            pulumi.set(__self__, "image_gc_high_threshold", image_gc_high_threshold)
        if image_gc_low_threshold is not None:
            pulumi.set(__self__, "image_gc_low_threshold", image_gc_low_threshold)
        if pod_max_pids is not None:
            pulumi.set(__self__, "pod_max_pids", pod_max_pids)
        if topology_manager_policy is not None:
            pulumi.set(__self__, "topology_manager_policy", topology_manager_policy)

    @property
    @pulumi.getter(name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(self) -> Optional[Sequence[str]]:
        """
        Allowed list of unsafe sysctls or unsafe sysctl patterns (ending in `*`).
        """
        return pulumi.get(self, "allowed_unsafe_sysctls")

    @property
    @pulumi.getter(name="containerLogMaxFiles")
    def container_log_max_files(self) -> Optional[int]:
        """
        The maximum number of container log files that can be present for a container. The number must be ≥ 2.
        """
        return pulumi.get(self, "container_log_max_files")

    @property
    @pulumi.getter(name="containerLogMaxSizeMB")
    def container_log_max_size_mb(self) -> Optional[int]:
        """
        The maximum size (e.g. 10Mi) of container log file before it is rotated.
        """
        return pulumi.get(self, "container_log_max_size_mb")

    @property
    @pulumi.getter(name="cpuCfsQuota")
    def cpu_cfs_quota(self) -> Optional[bool]:
        """
        The default is true.
        """
        return pulumi.get(self, "cpu_cfs_quota")

    @property
    @pulumi.getter(name="cpuCfsQuotaPeriod")
    def cpu_cfs_quota_period(self) -> Optional[str]:
        """
        The default is '100ms.' Valid values are a sequence of decimal numbers with an optional fraction and a unit suffix. For example: '300ms', '2h45m'. Supported units are 'ns', 'us', 'ms', 's', 'm', and 'h'.
        """
        return pulumi.get(self, "cpu_cfs_quota_period")

    @property
    @pulumi.getter(name="cpuManagerPolicy")
    def cpu_manager_policy(self) -> Optional[str]:
        """
        The default is 'none'. See [Kubernetes CPU management policies](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#cpu-management-policies) for more information. Allowed values are 'none' and 'static'.
        """
        return pulumi.get(self, "cpu_manager_policy")

    @property
    @pulumi.getter(name="failSwapOn")
    def fail_swap_on(self) -> Optional[bool]:
        """
        If set to true it will make the Kubelet fail to start if swap is enabled on the node.
        """
        return pulumi.get(self, "fail_swap_on")

    @property
    @pulumi.getter(name="imageGcHighThreshold")
    def image_gc_high_threshold(self) -> Optional[int]:
        """
        To disable image garbage collection, set to 100. The default is 85%
        """
        return pulumi.get(self, "image_gc_high_threshold")

    @property
    @pulumi.getter(name="imageGcLowThreshold")
    def image_gc_low_threshold(self) -> Optional[int]:
        """
        This cannot be set higher than imageGcHighThreshold. The default is 80%
        """
        return pulumi.get(self, "image_gc_low_threshold")

    @property
    @pulumi.getter(name="podMaxPids")
    def pod_max_pids(self) -> Optional[int]:
        """
        The maximum number of processes per pod.
        """
        return pulumi.get(self, "pod_max_pids")

    @property
    @pulumi.getter(name="topologyManagerPolicy")
    def topology_manager_policy(self) -> Optional[str]:
        """
        For more information see [Kubernetes Topology Manager](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager). The default is 'none'. Allowed values are 'none', 'best-effort', 'restricted', and 'single-numa-node'.
        """
        return pulumi.get(self, "topology_manager_policy")


@pulumi.output_type
class LinuxOSConfigResponse(dict):
    """
    See [AKS custom node configuration](https://docs.microsoft.com/azure/aks/custom-node-configuration) for more details.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "swapFileSizeMB":
            suggest = "swap_file_size_mb"
        elif key == "transparentHugePageDefrag":
            suggest = "transparent_huge_page_defrag"
        elif key == "transparentHugePageEnabled":
            suggest = "transparent_huge_page_enabled"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LinuxOSConfigResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LinuxOSConfigResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LinuxOSConfigResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 swap_file_size_mb: Optional[int] = None,
                 sysctls: Optional['outputs.SysctlConfigResponse'] = None,
                 transparent_huge_page_defrag: Optional[str] = None,
                 transparent_huge_page_enabled: Optional[str] = None):
        """
        See [AKS custom node configuration](https://docs.microsoft.com/azure/aks/custom-node-configuration) for more details.
        :param int swap_file_size_mb: The size in MB of a swap file that will be created on each node.
        :param 'SysctlConfigResponse' sysctls: Sysctl settings for Linux agent nodes.
        :param str transparent_huge_page_defrag: Valid values are 'always', 'defer', 'defer+madvise', 'madvise' and 'never'. The default is 'madvise'. For more information see [Transparent Hugepages](https://www.kernel.org/doc/html/latest/admin-guide/mm/transhuge.html#admin-guide-transhuge).
        :param str transparent_huge_page_enabled: Valid values are 'always', 'madvise', and 'never'. The default is 'always'. For more information see [Transparent Hugepages](https://www.kernel.org/doc/html/latest/admin-guide/mm/transhuge.html#admin-guide-transhuge).
        """
        if swap_file_size_mb is not None:
            pulumi.set(__self__, "swap_file_size_mb", swap_file_size_mb)
        if sysctls is not None:
            pulumi.set(__self__, "sysctls", sysctls)
        if transparent_huge_page_defrag is not None:
            pulumi.set(__self__, "transparent_huge_page_defrag", transparent_huge_page_defrag)
        if transparent_huge_page_enabled is not None:
            pulumi.set(__self__, "transparent_huge_page_enabled", transparent_huge_page_enabled)

    @property
    @pulumi.getter(name="swapFileSizeMB")
    def swap_file_size_mb(self) -> Optional[int]:
        """
        The size in MB of a swap file that will be created on each node.
        """
        return pulumi.get(self, "swap_file_size_mb")

    @property
    @pulumi.getter
    def sysctls(self) -> Optional['outputs.SysctlConfigResponse']:
        """
        Sysctl settings for Linux agent nodes.
        """
        return pulumi.get(self, "sysctls")

    @property
    @pulumi.getter(name="transparentHugePageDefrag")
    def transparent_huge_page_defrag(self) -> Optional[str]:
        """
        Valid values are 'always', 'defer', 'defer+madvise', 'madvise' and 'never'. The default is 'madvise'. For more information see [Transparent Hugepages](https://www.kernel.org/doc/html/latest/admin-guide/mm/transhuge.html#admin-guide-transhuge).
        """
        return pulumi.get(self, "transparent_huge_page_defrag")

    @property
    @pulumi.getter(name="transparentHugePageEnabled")
    def transparent_huge_page_enabled(self) -> Optional[str]:
        """
        Valid values are 'always', 'madvise', and 'never'. The default is 'always'. For more information see [Transparent Hugepages](https://www.kernel.org/doc/html/latest/admin-guide/mm/transhuge.html#admin-guide-transhuge).
        """
        return pulumi.get(self, "transparent_huge_page_enabled")


@pulumi.output_type
class PowerStateResponse(dict):
    """
    Describes the Power State of the cluster
    """
    def __init__(__self__, *,
                 code: Optional[str] = None):
        """
        Describes the Power State of the cluster
        :param str code: Tells whether the cluster is Running or Stopped
        """
        if code is not None:
            pulumi.set(__self__, "code", code)

    @property
    @pulumi.getter
    def code(self) -> Optional[str]:
        """
        Tells whether the cluster is Running or Stopped
        """
        return pulumi.get(self, "code")


@pulumi.output_type
class SysctlConfigResponse(dict):
    """
    Sysctl settings for Linux agent nodes.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "fsAioMaxNr":
            suggest = "fs_aio_max_nr"
        elif key == "fsFileMax":
            suggest = "fs_file_max"
        elif key == "fsInotifyMaxUserWatches":
            suggest = "fs_inotify_max_user_watches"
        elif key == "fsNrOpen":
            suggest = "fs_nr_open"
        elif key == "kernelThreadsMax":
            suggest = "kernel_threads_max"
        elif key == "netCoreNetdevMaxBacklog":
            suggest = "net_core_netdev_max_backlog"
        elif key == "netCoreOptmemMax":
            suggest = "net_core_optmem_max"
        elif key == "netCoreRmemDefault":
            suggest = "net_core_rmem_default"
        elif key == "netCoreRmemMax":
            suggest = "net_core_rmem_max"
        elif key == "netCoreSomaxconn":
            suggest = "net_core_somaxconn"
        elif key == "netCoreWmemDefault":
            suggest = "net_core_wmem_default"
        elif key == "netCoreWmemMax":
            suggest = "net_core_wmem_max"
        elif key == "netIpv4IpLocalPortRange":
            suggest = "net_ipv4_ip_local_port_range"
        elif key == "netIpv4NeighDefaultGcThresh1":
            suggest = "net_ipv4_neigh_default_gc_thresh1"
        elif key == "netIpv4NeighDefaultGcThresh2":
            suggest = "net_ipv4_neigh_default_gc_thresh2"
        elif key == "netIpv4NeighDefaultGcThresh3":
            suggest = "net_ipv4_neigh_default_gc_thresh3"
        elif key == "netIpv4TcpFinTimeout":
            suggest = "net_ipv4_tcp_fin_timeout"
        elif key == "netIpv4TcpKeepaliveProbes":
            suggest = "net_ipv4_tcp_keepalive_probes"
        elif key == "netIpv4TcpKeepaliveTime":
            suggest = "net_ipv4_tcp_keepalive_time"
        elif key == "netIpv4TcpMaxSynBacklog":
            suggest = "net_ipv4_tcp_max_syn_backlog"
        elif key == "netIpv4TcpMaxTwBuckets":
            suggest = "net_ipv4_tcp_max_tw_buckets"
        elif key == "netIpv4TcpTwReuse":
            suggest = "net_ipv4_tcp_tw_reuse"
        elif key == "netIpv4TcpkeepaliveIntvl":
            suggest = "net_ipv4_tcpkeepalive_intvl"
        elif key == "netNetfilterNfConntrackBuckets":
            suggest = "net_netfilter_nf_conntrack_buckets"
        elif key == "netNetfilterNfConntrackMax":
            suggest = "net_netfilter_nf_conntrack_max"
        elif key == "vmMaxMapCount":
            suggest = "vm_max_map_count"
        elif key == "vmSwappiness":
            suggest = "vm_swappiness"
        elif key == "vmVfsCachePressure":
            suggest = "vm_vfs_cache_pressure"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SysctlConfigResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SysctlConfigResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SysctlConfigResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 fs_aio_max_nr: Optional[int] = None,
                 fs_file_max: Optional[int] = None,
                 fs_inotify_max_user_watches: Optional[int] = None,
                 fs_nr_open: Optional[int] = None,
                 kernel_threads_max: Optional[int] = None,
                 net_core_netdev_max_backlog: Optional[int] = None,
                 net_core_optmem_max: Optional[int] = None,
                 net_core_rmem_default: Optional[int] = None,
                 net_core_rmem_max: Optional[int] = None,
                 net_core_somaxconn: Optional[int] = None,
                 net_core_wmem_default: Optional[int] = None,
                 net_core_wmem_max: Optional[int] = None,
                 net_ipv4_ip_local_port_range: Optional[str] = None,
                 net_ipv4_neigh_default_gc_thresh1: Optional[int] = None,
                 net_ipv4_neigh_default_gc_thresh2: Optional[int] = None,
                 net_ipv4_neigh_default_gc_thresh3: Optional[int] = None,
                 net_ipv4_tcp_fin_timeout: Optional[int] = None,
                 net_ipv4_tcp_keepalive_probes: Optional[int] = None,
                 net_ipv4_tcp_keepalive_time: Optional[int] = None,
                 net_ipv4_tcp_max_syn_backlog: Optional[int] = None,
                 net_ipv4_tcp_max_tw_buckets: Optional[int] = None,
                 net_ipv4_tcp_tw_reuse: Optional[bool] = None,
                 net_ipv4_tcpkeepalive_intvl: Optional[int] = None,
                 net_netfilter_nf_conntrack_buckets: Optional[int] = None,
                 net_netfilter_nf_conntrack_max: Optional[int] = None,
                 vm_max_map_count: Optional[int] = None,
                 vm_swappiness: Optional[int] = None,
                 vm_vfs_cache_pressure: Optional[int] = None):
        """
        Sysctl settings for Linux agent nodes.
        :param int fs_aio_max_nr: Sysctl setting fs.aio-max-nr.
        :param int fs_file_max: Sysctl setting fs.file-max.
        :param int fs_inotify_max_user_watches: Sysctl setting fs.inotify.max_user_watches.
        :param int fs_nr_open: Sysctl setting fs.nr_open.
        :param int kernel_threads_max: Sysctl setting kernel.threads-max.
        :param int net_core_netdev_max_backlog: Sysctl setting net.core.netdev_max_backlog.
        :param int net_core_optmem_max: Sysctl setting net.core.optmem_max.
        :param int net_core_rmem_default: Sysctl setting net.core.rmem_default.
        :param int net_core_rmem_max: Sysctl setting net.core.rmem_max.
        :param int net_core_somaxconn: Sysctl setting net.core.somaxconn.
        :param int net_core_wmem_default: Sysctl setting net.core.wmem_default.
        :param int net_core_wmem_max: Sysctl setting net.core.wmem_max.
        :param str net_ipv4_ip_local_port_range: Sysctl setting net.ipv4.ip_local_port_range.
        :param int net_ipv4_neigh_default_gc_thresh1: Sysctl setting net.ipv4.neigh.default.gc_thresh1.
        :param int net_ipv4_neigh_default_gc_thresh2: Sysctl setting net.ipv4.neigh.default.gc_thresh2.
        :param int net_ipv4_neigh_default_gc_thresh3: Sysctl setting net.ipv4.neigh.default.gc_thresh3.
        :param int net_ipv4_tcp_fin_timeout: Sysctl setting net.ipv4.tcp_fin_timeout.
        :param int net_ipv4_tcp_keepalive_probes: Sysctl setting net.ipv4.tcp_keepalive_probes.
        :param int net_ipv4_tcp_keepalive_time: Sysctl setting net.ipv4.tcp_keepalive_time.
        :param int net_ipv4_tcp_max_syn_backlog: Sysctl setting net.ipv4.tcp_max_syn_backlog.
        :param int net_ipv4_tcp_max_tw_buckets: Sysctl setting net.ipv4.tcp_max_tw_buckets.
        :param bool net_ipv4_tcp_tw_reuse: Sysctl setting net.ipv4.tcp_tw_reuse.
        :param int net_ipv4_tcpkeepalive_intvl: Sysctl setting net.ipv4.tcp_keepalive_intvl.
        :param int net_netfilter_nf_conntrack_buckets: Sysctl setting net.netfilter.nf_conntrack_buckets.
        :param int net_netfilter_nf_conntrack_max: Sysctl setting net.netfilter.nf_conntrack_max.
        :param int vm_max_map_count: Sysctl setting vm.max_map_count.
        :param int vm_swappiness: Sysctl setting vm.swappiness.
        :param int vm_vfs_cache_pressure: Sysctl setting vm.vfs_cache_pressure.
        """
        if fs_aio_max_nr is not None:
            pulumi.set(__self__, "fs_aio_max_nr", fs_aio_max_nr)
        if fs_file_max is not None:
            pulumi.set(__self__, "fs_file_max", fs_file_max)
        if fs_inotify_max_user_watches is not None:
            pulumi.set(__self__, "fs_inotify_max_user_watches", fs_inotify_max_user_watches)
        if fs_nr_open is not None:
            pulumi.set(__self__, "fs_nr_open", fs_nr_open)
        if kernel_threads_max is not None:
            pulumi.set(__self__, "kernel_threads_max", kernel_threads_max)
        if net_core_netdev_max_backlog is not None:
            pulumi.set(__self__, "net_core_netdev_max_backlog", net_core_netdev_max_backlog)
        if net_core_optmem_max is not None:
            pulumi.set(__self__, "net_core_optmem_max", net_core_optmem_max)
        if net_core_rmem_default is not None:
            pulumi.set(__self__, "net_core_rmem_default", net_core_rmem_default)
        if net_core_rmem_max is not None:
            pulumi.set(__self__, "net_core_rmem_max", net_core_rmem_max)
        if net_core_somaxconn is not None:
            pulumi.set(__self__, "net_core_somaxconn", net_core_somaxconn)
        if net_core_wmem_default is not None:
            pulumi.set(__self__, "net_core_wmem_default", net_core_wmem_default)
        if net_core_wmem_max is not None:
            pulumi.set(__self__, "net_core_wmem_max", net_core_wmem_max)
        if net_ipv4_ip_local_port_range is not None:
            pulumi.set(__self__, "net_ipv4_ip_local_port_range", net_ipv4_ip_local_port_range)
        if net_ipv4_neigh_default_gc_thresh1 is not None:
            pulumi.set(__self__, "net_ipv4_neigh_default_gc_thresh1", net_ipv4_neigh_default_gc_thresh1)
        if net_ipv4_neigh_default_gc_thresh2 is not None:
            pulumi.set(__self__, "net_ipv4_neigh_default_gc_thresh2", net_ipv4_neigh_default_gc_thresh2)
        if net_ipv4_neigh_default_gc_thresh3 is not None:
            pulumi.set(__self__, "net_ipv4_neigh_default_gc_thresh3", net_ipv4_neigh_default_gc_thresh3)
        if net_ipv4_tcp_fin_timeout is not None:
            pulumi.set(__self__, "net_ipv4_tcp_fin_timeout", net_ipv4_tcp_fin_timeout)
        if net_ipv4_tcp_keepalive_probes is not None:
            pulumi.set(__self__, "net_ipv4_tcp_keepalive_probes", net_ipv4_tcp_keepalive_probes)
        if net_ipv4_tcp_keepalive_time is not None:
            pulumi.set(__self__, "net_ipv4_tcp_keepalive_time", net_ipv4_tcp_keepalive_time)
        if net_ipv4_tcp_max_syn_backlog is not None:
            pulumi.set(__self__, "net_ipv4_tcp_max_syn_backlog", net_ipv4_tcp_max_syn_backlog)
        if net_ipv4_tcp_max_tw_buckets is not None:
            pulumi.set(__self__, "net_ipv4_tcp_max_tw_buckets", net_ipv4_tcp_max_tw_buckets)
        if net_ipv4_tcp_tw_reuse is not None:
            pulumi.set(__self__, "net_ipv4_tcp_tw_reuse", net_ipv4_tcp_tw_reuse)
        if net_ipv4_tcpkeepalive_intvl is not None:
            pulumi.set(__self__, "net_ipv4_tcpkeepalive_intvl", net_ipv4_tcpkeepalive_intvl)
        if net_netfilter_nf_conntrack_buckets is not None:
            pulumi.set(__self__, "net_netfilter_nf_conntrack_buckets", net_netfilter_nf_conntrack_buckets)
        if net_netfilter_nf_conntrack_max is not None:
            pulumi.set(__self__, "net_netfilter_nf_conntrack_max", net_netfilter_nf_conntrack_max)
        if vm_max_map_count is not None:
            pulumi.set(__self__, "vm_max_map_count", vm_max_map_count)
        if vm_swappiness is not None:
            pulumi.set(__self__, "vm_swappiness", vm_swappiness)
        if vm_vfs_cache_pressure is not None:
            pulumi.set(__self__, "vm_vfs_cache_pressure", vm_vfs_cache_pressure)

    @property
    @pulumi.getter(name="fsAioMaxNr")
    def fs_aio_max_nr(self) -> Optional[int]:
        """
        Sysctl setting fs.aio-max-nr.
        """
        return pulumi.get(self, "fs_aio_max_nr")

    @property
    @pulumi.getter(name="fsFileMax")
    def fs_file_max(self) -> Optional[int]:
        """
        Sysctl setting fs.file-max.
        """
        return pulumi.get(self, "fs_file_max")

    @property
    @pulumi.getter(name="fsInotifyMaxUserWatches")
    def fs_inotify_max_user_watches(self) -> Optional[int]:
        """
        Sysctl setting fs.inotify.max_user_watches.
        """
        return pulumi.get(self, "fs_inotify_max_user_watches")

    @property
    @pulumi.getter(name="fsNrOpen")
    def fs_nr_open(self) -> Optional[int]:
        """
        Sysctl setting fs.nr_open.
        """
        return pulumi.get(self, "fs_nr_open")

    @property
    @pulumi.getter(name="kernelThreadsMax")
    def kernel_threads_max(self) -> Optional[int]:
        """
        Sysctl setting kernel.threads-max.
        """
        return pulumi.get(self, "kernel_threads_max")

    @property
    @pulumi.getter(name="netCoreNetdevMaxBacklog")
    def net_core_netdev_max_backlog(self) -> Optional[int]:
        """
        Sysctl setting net.core.netdev_max_backlog.
        """
        return pulumi.get(self, "net_core_netdev_max_backlog")

    @property
    @pulumi.getter(name="netCoreOptmemMax")
    def net_core_optmem_max(self) -> Optional[int]:
        """
        Sysctl setting net.core.optmem_max.
        """
        return pulumi.get(self, "net_core_optmem_max")

    @property
    @pulumi.getter(name="netCoreRmemDefault")
    def net_core_rmem_default(self) -> Optional[int]:
        """
        Sysctl setting net.core.rmem_default.
        """
        return pulumi.get(self, "net_core_rmem_default")

    @property
    @pulumi.getter(name="netCoreRmemMax")
    def net_core_rmem_max(self) -> Optional[int]:
        """
        Sysctl setting net.core.rmem_max.
        """
        return pulumi.get(self, "net_core_rmem_max")

    @property
    @pulumi.getter(name="netCoreSomaxconn")
    def net_core_somaxconn(self) -> Optional[int]:
        """
        Sysctl setting net.core.somaxconn.
        """
        return pulumi.get(self, "net_core_somaxconn")

    @property
    @pulumi.getter(name="netCoreWmemDefault")
    def net_core_wmem_default(self) -> Optional[int]:
        """
        Sysctl setting net.core.wmem_default.
        """
        return pulumi.get(self, "net_core_wmem_default")

    @property
    @pulumi.getter(name="netCoreWmemMax")
    def net_core_wmem_max(self) -> Optional[int]:
        """
        Sysctl setting net.core.wmem_max.
        """
        return pulumi.get(self, "net_core_wmem_max")

    @property
    @pulumi.getter(name="netIpv4IpLocalPortRange")
    def net_ipv4_ip_local_port_range(self) -> Optional[str]:
        """
        Sysctl setting net.ipv4.ip_local_port_range.
        """
        return pulumi.get(self, "net_ipv4_ip_local_port_range")

    @property
    @pulumi.getter(name="netIpv4NeighDefaultGcThresh1")
    def net_ipv4_neigh_default_gc_thresh1(self) -> Optional[int]:
        """
        Sysctl setting net.ipv4.neigh.default.gc_thresh1.
        """
        return pulumi.get(self, "net_ipv4_neigh_default_gc_thresh1")

    @property
    @pulumi.getter(name="netIpv4NeighDefaultGcThresh2")
    def net_ipv4_neigh_default_gc_thresh2(self) -> Optional[int]:
        """
        Sysctl setting net.ipv4.neigh.default.gc_thresh2.
        """
        return pulumi.get(self, "net_ipv4_neigh_default_gc_thresh2")

    @property
    @pulumi.getter(name="netIpv4NeighDefaultGcThresh3")
    def net_ipv4_neigh_default_gc_thresh3(self) -> Optional[int]:
        """
        Sysctl setting net.ipv4.neigh.default.gc_thresh3.
        """
        return pulumi.get(self, "net_ipv4_neigh_default_gc_thresh3")

    @property
    @pulumi.getter(name="netIpv4TcpFinTimeout")
    def net_ipv4_tcp_fin_timeout(self) -> Optional[int]:
        """
        Sysctl setting net.ipv4.tcp_fin_timeout.
        """
        return pulumi.get(self, "net_ipv4_tcp_fin_timeout")

    @property
    @pulumi.getter(name="netIpv4TcpKeepaliveProbes")
    def net_ipv4_tcp_keepalive_probes(self) -> Optional[int]:
        """
        Sysctl setting net.ipv4.tcp_keepalive_probes.
        """
        return pulumi.get(self, "net_ipv4_tcp_keepalive_probes")

    @property
    @pulumi.getter(name="netIpv4TcpKeepaliveTime")
    def net_ipv4_tcp_keepalive_time(self) -> Optional[int]:
        """
        Sysctl setting net.ipv4.tcp_keepalive_time.
        """
        return pulumi.get(self, "net_ipv4_tcp_keepalive_time")

    @property
    @pulumi.getter(name="netIpv4TcpMaxSynBacklog")
    def net_ipv4_tcp_max_syn_backlog(self) -> Optional[int]:
        """
        Sysctl setting net.ipv4.tcp_max_syn_backlog.
        """
        return pulumi.get(self, "net_ipv4_tcp_max_syn_backlog")

    @property
    @pulumi.getter(name="netIpv4TcpMaxTwBuckets")
    def net_ipv4_tcp_max_tw_buckets(self) -> Optional[int]:
        """
        Sysctl setting net.ipv4.tcp_max_tw_buckets.
        """
        return pulumi.get(self, "net_ipv4_tcp_max_tw_buckets")

    @property
    @pulumi.getter(name="netIpv4TcpTwReuse")
    def net_ipv4_tcp_tw_reuse(self) -> Optional[bool]:
        """
        Sysctl setting net.ipv4.tcp_tw_reuse.
        """
        return pulumi.get(self, "net_ipv4_tcp_tw_reuse")

    @property
    @pulumi.getter(name="netIpv4TcpkeepaliveIntvl")
    def net_ipv4_tcpkeepalive_intvl(self) -> Optional[int]:
        """
        Sysctl setting net.ipv4.tcp_keepalive_intvl.
        """
        return pulumi.get(self, "net_ipv4_tcpkeepalive_intvl")

    @property
    @pulumi.getter(name="netNetfilterNfConntrackBuckets")
    def net_netfilter_nf_conntrack_buckets(self) -> Optional[int]:
        """
        Sysctl setting net.netfilter.nf_conntrack_buckets.
        """
        return pulumi.get(self, "net_netfilter_nf_conntrack_buckets")

    @property
    @pulumi.getter(name="netNetfilterNfConntrackMax")
    def net_netfilter_nf_conntrack_max(self) -> Optional[int]:
        """
        Sysctl setting net.netfilter.nf_conntrack_max.
        """
        return pulumi.get(self, "net_netfilter_nf_conntrack_max")

    @property
    @pulumi.getter(name="vmMaxMapCount")
    def vm_max_map_count(self) -> Optional[int]:
        """
        Sysctl setting vm.max_map_count.
        """
        return pulumi.get(self, "vm_max_map_count")

    @property
    @pulumi.getter(name="vmSwappiness")
    def vm_swappiness(self) -> Optional[int]:
        """
        Sysctl setting vm.swappiness.
        """
        return pulumi.get(self, "vm_swappiness")

    @property
    @pulumi.getter(name="vmVfsCachePressure")
    def vm_vfs_cache_pressure(self) -> Optional[int]:
        """
        Sysctl setting vm.vfs_cache_pressure.
        """
        return pulumi.get(self, "vm_vfs_cache_pressure")


