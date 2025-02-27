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
    'ComputeBindingArgs',
    'EncryptionPropertyArgs',
    'IdentityArgs',
    'KeyVaultPropertiesArgs',
    'LabelCategoryArgs',
    'LabelClassArgs',
    'LabelingDatasetConfigurationArgs',
    'LabelingJobImagePropertiesArgs',
    'LabelingJobInstructionsArgs',
    'LabelingJobPropertiesArgs',
    'LinkedServicePropsArgs',
    'MLAssistConfigurationArgs',
    'SharedPrivateLinkResourceArgs',
    'SkuArgs',
]

@pulumi.input_type
class ComputeBindingArgs:
    def __init__(__self__, *,
                 compute_id: Optional[pulumi.Input[str]] = None,
                 node_count: Optional[pulumi.Input[int]] = None):
        """
        Compute binding definition.
        :param pulumi.Input[str] compute_id: ID of the compute resource.
        :param pulumi.Input[int] node_count: Number of nodes.
        """
        if compute_id is not None:
            pulumi.set(__self__, "compute_id", compute_id)
        if node_count is not None:
            pulumi.set(__self__, "node_count", node_count)

    @property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the compute resource.
        """
        return pulumi.get(self, "compute_id")

    @compute_id.setter
    def compute_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compute_id", value)

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[int]]:
        """
        Number of nodes.
        """
        return pulumi.get(self, "node_count")

    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_count", value)


@pulumi.input_type
class EncryptionPropertyArgs:
    def __init__(__self__, *,
                 key_vault_properties: pulumi.Input['KeyVaultPropertiesArgs'],
                 status: pulumi.Input[Union[str, 'EncryptionStatus']]):
        """
        :param pulumi.Input['KeyVaultPropertiesArgs'] key_vault_properties: Customer Key vault properties.
        :param pulumi.Input[Union[str, 'EncryptionStatus']] status: Indicates whether or not the encryption is enabled for the workspace.
        """
        pulumi.set(__self__, "key_vault_properties", key_vault_properties)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> pulumi.Input['KeyVaultPropertiesArgs']:
        """
        Customer Key vault properties.
        """
        return pulumi.get(self, "key_vault_properties")

    @key_vault_properties.setter
    def key_vault_properties(self, value: pulumi.Input['KeyVaultPropertiesArgs']):
        pulumi.set(self, "key_vault_properties", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[Union[str, 'EncryptionStatus']]:
        """
        Indicates whether or not the encryption is enabled for the workspace.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[Union[str, 'EncryptionStatus']]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input['ResourceIdentityType']] = None,
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Identity for the resource.
        :param pulumi.Input['ResourceIdentityType'] type: The identity type.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The user assigned identities associated with the resource.
        """
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['ResourceIdentityType']]:
        """
        The identity type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['ResourceIdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The user assigned identities associated with the resource.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(__self__, *,
                 key_identifier: pulumi.Input[str],
                 key_vault_arm_id: pulumi.Input[str],
                 identity_client_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] key_identifier: Key vault uri to access the encryption key.
        :param pulumi.Input[str] key_vault_arm_id: The ArmId of the keyVault where the customer owned encryption key is present.
        :param pulumi.Input[str] identity_client_id: For future use - The client id of the identity which will be used to access key vault.
        """
        pulumi.set(__self__, "key_identifier", key_identifier)
        pulumi.set(__self__, "key_vault_arm_id", key_vault_arm_id)
        if identity_client_id is not None:
            pulumi.set(__self__, "identity_client_id", identity_client_id)

    @property
    @pulumi.getter(name="keyIdentifier")
    def key_identifier(self) -> pulumi.Input[str]:
        """
        Key vault uri to access the encryption key.
        """
        return pulumi.get(self, "key_identifier")

    @key_identifier.setter
    def key_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_identifier", value)

    @property
    @pulumi.getter(name="keyVaultArmId")
    def key_vault_arm_id(self) -> pulumi.Input[str]:
        """
        The ArmId of the keyVault where the customer owned encryption key is present.
        """
        return pulumi.get(self, "key_vault_arm_id")

    @key_vault_arm_id.setter
    def key_vault_arm_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_arm_id", value)

    @property
    @pulumi.getter(name="identityClientId")
    def identity_client_id(self) -> Optional[pulumi.Input[str]]:
        """
        For future use - The client id of the identity which will be used to access key vault.
        """
        return pulumi.get(self, "identity_client_id")

    @identity_client_id.setter
    def identity_client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_client_id", value)


@pulumi.input_type
class LabelCategoryArgs:
    def __init__(__self__, *,
                 classes: pulumi.Input[Mapping[str, pulumi.Input['LabelClassArgs']]],
                 allow_multi_select: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None):
        """
        Represents a category of labels in a labeling job.
        :param pulumi.Input[Mapping[str, pulumi.Input['LabelClassArgs']]] classes: Dictionary of label classes in this category.
        :param pulumi.Input[bool] allow_multi_select: Indicates whether it is allowed to select multiple classes in this category.
        :param pulumi.Input[str] display_name: Display name of the label category.
        """
        pulumi.set(__self__, "classes", classes)
        if allow_multi_select is not None:
            pulumi.set(__self__, "allow_multi_select", allow_multi_select)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter
    def classes(self) -> pulumi.Input[Mapping[str, pulumi.Input['LabelClassArgs']]]:
        """
        Dictionary of label classes in this category.
        """
        return pulumi.get(self, "classes")

    @classes.setter
    def classes(self, value: pulumi.Input[Mapping[str, pulumi.Input['LabelClassArgs']]]):
        pulumi.set(self, "classes", value)

    @property
    @pulumi.getter(name="allowMultiSelect")
    def allow_multi_select(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether it is allowed to select multiple classes in this category.
        """
        return pulumi.get(self, "allow_multi_select")

    @allow_multi_select.setter
    def allow_multi_select(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_multi_select", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the label category.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)


@pulumi.input_type
class LabelClassArgs:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 subclasses: Optional[pulumi.Input[Mapping[str, pulumi.Input['LabelClassArgs']]]] = None):
        """
        Represents a label or a category of labels in a labeling job.
        :param pulumi.Input[str] display_name: Display name of the label class.
        :param pulumi.Input[Mapping[str, pulumi.Input['LabelClassArgs']]] subclasses: Dictionary of subclasses of the label class.
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if subclasses is not None:
            pulumi.set(__self__, "subclasses", subclasses)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the label class.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def subclasses(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['LabelClassArgs']]]]:
        """
        Dictionary of subclasses of the label class.
        """
        return pulumi.get(self, "subclasses")

    @subclasses.setter
    def subclasses(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['LabelClassArgs']]]]):
        pulumi.set(self, "subclasses", value)


@pulumi.input_type
class LabelingDatasetConfigurationArgs:
    def __init__(__self__, *,
                 asset_name: pulumi.Input[str],
                 dataset_version: pulumi.Input[str],
                 enable_incremental_dataset_refresh: Optional[pulumi.Input[bool]] = None):
        """
        Represents configuration of dataset used in a labeling job.
        :param pulumi.Input[str] asset_name: Name of the data asset to perform labeling.
        :param pulumi.Input[str] dataset_version: AML dataset version.
        :param pulumi.Input[bool] enable_incremental_dataset_refresh: Indicates whether to enable incremental dataset refresh.
        """
        pulumi.set(__self__, "asset_name", asset_name)
        pulumi.set(__self__, "dataset_version", dataset_version)
        if enable_incremental_dataset_refresh is not None:
            pulumi.set(__self__, "enable_incremental_dataset_refresh", enable_incremental_dataset_refresh)

    @property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> pulumi.Input[str]:
        """
        Name of the data asset to perform labeling.
        """
        return pulumi.get(self, "asset_name")

    @asset_name.setter
    def asset_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "asset_name", value)

    @property
    @pulumi.getter(name="datasetVersion")
    def dataset_version(self) -> pulumi.Input[str]:
        """
        AML dataset version.
        """
        return pulumi.get(self, "dataset_version")

    @dataset_version.setter
    def dataset_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "dataset_version", value)

    @property
    @pulumi.getter(name="enableIncrementalDatasetRefresh")
    def enable_incremental_dataset_refresh(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to enable incremental dataset refresh.
        """
        return pulumi.get(self, "enable_incremental_dataset_refresh")

    @enable_incremental_dataset_refresh.setter
    def enable_incremental_dataset_refresh(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_incremental_dataset_refresh", value)


@pulumi.input_type
class LabelingJobImagePropertiesArgs:
    def __init__(__self__, *,
                 media_type: pulumi.Input[Union[str, 'MediaType']],
                 annotation_type: Optional[pulumi.Input[Union[str, 'ImageAnnotationType']]] = None):
        """
        :param pulumi.Input[Union[str, 'MediaType']] media_type: Media type of data asset.
        :param pulumi.Input[Union[str, 'ImageAnnotationType']] annotation_type: Annotation type of image labeling tasks.
        """
        pulumi.set(__self__, "media_type", media_type)
        if annotation_type is not None:
            pulumi.set(__self__, "annotation_type", annotation_type)

    @property
    @pulumi.getter(name="mediaType")
    def media_type(self) -> pulumi.Input[Union[str, 'MediaType']]:
        """
        Media type of data asset.
        """
        return pulumi.get(self, "media_type")

    @media_type.setter
    def media_type(self, value: pulumi.Input[Union[str, 'MediaType']]):
        pulumi.set(self, "media_type", value)

    @property
    @pulumi.getter(name="annotationType")
    def annotation_type(self) -> Optional[pulumi.Input[Union[str, 'ImageAnnotationType']]]:
        """
        Annotation type of image labeling tasks.
        """
        return pulumi.get(self, "annotation_type")

    @annotation_type.setter
    def annotation_type(self, value: Optional[pulumi.Input[Union[str, 'ImageAnnotationType']]]):
        pulumi.set(self, "annotation_type", value)


@pulumi.input_type
class LabelingJobInstructionsArgs:
    def __init__(__self__, *,
                 uri: Optional[pulumi.Input[str]] = None):
        """
        Instructions for a labeling job.
        :param pulumi.Input[str] uri: The link to a page with detailed labeling instructions for labelers.
        """
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        The link to a page with detailed labeling instructions for labelers.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)


@pulumi.input_type
class LabelingJobPropertiesArgs:
    def __init__(__self__, *,
                 dataset_configuration: pulumi.Input['LabelingDatasetConfigurationArgs'],
                 job_instructions: pulumi.Input['LabelingJobInstructionsArgs'],
                 label_categories: pulumi.Input[Mapping[str, pulumi.Input['LabelCategoryArgs']]],
                 labeling_job_media_properties: pulumi.Input['LabelingJobImagePropertiesArgs'],
                 ml_assist_configuration: Optional[pulumi.Input['MLAssistConfigurationArgs']] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Definition of a labeling job.
        :param pulumi.Input['LabelingDatasetConfigurationArgs'] dataset_configuration: Dataset configuration for the job.
        :param pulumi.Input['LabelingJobInstructionsArgs'] job_instructions: Instructions for the job.
        :param pulumi.Input[Mapping[str, pulumi.Input['LabelCategoryArgs']]] label_categories: Label categories of the job.
        :param pulumi.Input['LabelingJobImagePropertiesArgs'] labeling_job_media_properties: Media specific properties in a labeling job.
        :param pulumi.Input['MLAssistConfigurationArgs'] ml_assist_configuration: Machine learning assisted configuration for the job.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: The job property dictionary. Properties can be added, but not removed or altered.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The job tag dictionary. Tags can be added, removed, and updated.
        """
        pulumi.set(__self__, "dataset_configuration", dataset_configuration)
        pulumi.set(__self__, "job_instructions", job_instructions)
        pulumi.set(__self__, "label_categories", label_categories)
        pulumi.set(__self__, "labeling_job_media_properties", labeling_job_media_properties)
        if ml_assist_configuration is not None:
            pulumi.set(__self__, "ml_assist_configuration", ml_assist_configuration)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="datasetConfiguration")
    def dataset_configuration(self) -> pulumi.Input['LabelingDatasetConfigurationArgs']:
        """
        Dataset configuration for the job.
        """
        return pulumi.get(self, "dataset_configuration")

    @dataset_configuration.setter
    def dataset_configuration(self, value: pulumi.Input['LabelingDatasetConfigurationArgs']):
        pulumi.set(self, "dataset_configuration", value)

    @property
    @pulumi.getter(name="jobInstructions")
    def job_instructions(self) -> pulumi.Input['LabelingJobInstructionsArgs']:
        """
        Instructions for the job.
        """
        return pulumi.get(self, "job_instructions")

    @job_instructions.setter
    def job_instructions(self, value: pulumi.Input['LabelingJobInstructionsArgs']):
        pulumi.set(self, "job_instructions", value)

    @property
    @pulumi.getter(name="labelCategories")
    def label_categories(self) -> pulumi.Input[Mapping[str, pulumi.Input['LabelCategoryArgs']]]:
        """
        Label categories of the job.
        """
        return pulumi.get(self, "label_categories")

    @label_categories.setter
    def label_categories(self, value: pulumi.Input[Mapping[str, pulumi.Input['LabelCategoryArgs']]]):
        pulumi.set(self, "label_categories", value)

    @property
    @pulumi.getter(name="labelingJobMediaProperties")
    def labeling_job_media_properties(self) -> pulumi.Input['LabelingJobImagePropertiesArgs']:
        """
        Media specific properties in a labeling job.
        """
        return pulumi.get(self, "labeling_job_media_properties")

    @labeling_job_media_properties.setter
    def labeling_job_media_properties(self, value: pulumi.Input['LabelingJobImagePropertiesArgs']):
        pulumi.set(self, "labeling_job_media_properties", value)

    @property
    @pulumi.getter(name="mlAssistConfiguration")
    def ml_assist_configuration(self) -> Optional[pulumi.Input['MLAssistConfigurationArgs']]:
        """
        Machine learning assisted configuration for the job.
        """
        return pulumi.get(self, "ml_assist_configuration")

    @ml_assist_configuration.setter
    def ml_assist_configuration(self, value: Optional[pulumi.Input['MLAssistConfigurationArgs']]):
        pulumi.set(self, "ml_assist_configuration", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The job property dictionary. Properties can be added, but not removed or altered.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The job tag dictionary. Tags can be added, removed, and updated.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class LinkedServicePropsArgs:
    def __init__(__self__, *,
                 linked_service_resource_id: pulumi.Input[str],
                 created_time: Optional[pulumi.Input[str]] = None,
                 link_type: Optional[pulumi.Input['LinkedServiceLinkType']] = None,
                 modified_time: Optional[pulumi.Input[str]] = None):
        """
        LinkedService specific properties.
        :param pulumi.Input[str] linked_service_resource_id: ResourceId of the link target of the linked service.
        :param pulumi.Input[str] created_time: The creation time of the linked service.
        :param pulumi.Input['LinkedServiceLinkType'] link_type: Type of the link target.
        :param pulumi.Input[str] modified_time: The last modified time of the linked service.
        """
        pulumi.set(__self__, "linked_service_resource_id", linked_service_resource_id)
        if created_time is not None:
            pulumi.set(__self__, "created_time", created_time)
        if link_type is not None:
            pulumi.set(__self__, "link_type", link_type)
        if modified_time is not None:
            pulumi.set(__self__, "modified_time", modified_time)

    @property
    @pulumi.getter(name="linkedServiceResourceId")
    def linked_service_resource_id(self) -> pulumi.Input[str]:
        """
        ResourceId of the link target of the linked service.
        """
        return pulumi.get(self, "linked_service_resource_id")

    @linked_service_resource_id.setter
    def linked_service_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "linked_service_resource_id", value)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[str]]:
        """
        The creation time of the linked service.
        """
        return pulumi.get(self, "created_time")

    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_time", value)

    @property
    @pulumi.getter(name="linkType")
    def link_type(self) -> Optional[pulumi.Input['LinkedServiceLinkType']]:
        """
        Type of the link target.
        """
        return pulumi.get(self, "link_type")

    @link_type.setter
    def link_type(self, value: Optional[pulumi.Input['LinkedServiceLinkType']]):
        pulumi.set(self, "link_type", value)

    @property
    @pulumi.getter(name="modifiedTime")
    def modified_time(self) -> Optional[pulumi.Input[str]]:
        """
        The last modified time of the linked service.
        """
        return pulumi.get(self, "modified_time")

    @modified_time.setter
    def modified_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modified_time", value)


@pulumi.input_type
class MLAssistConfigurationArgs:
    def __init__(__self__, *,
                 inferencing_compute_binding: pulumi.Input['ComputeBindingArgs'],
                 model_name_prefix: pulumi.Input[str],
                 training_compute_binding: pulumi.Input['ComputeBindingArgs'],
                 ml_assist_enabled: Optional[pulumi.Input[bool]] = None,
                 prelabel_accuracy_threshold: Optional[pulumi.Input[float]] = None):
        """
        Represents configuration for machine learning assisted features in a labeling job.
        :param pulumi.Input['ComputeBindingArgs'] inferencing_compute_binding: The compute designated for inferencing.
        :param pulumi.Input[str] model_name_prefix: Name prefix to use for machine learning model. For each iteration modelName will be appended with iteration e.g.{modelName}_{i}.
        :param pulumi.Input['ComputeBindingArgs'] training_compute_binding: The compute designated for training.
        :param pulumi.Input[bool] ml_assist_enabled: Indicates whether MLAssist feature is enabled.
        :param pulumi.Input[float] prelabel_accuracy_threshold: Prelabel accuracy threshold used in MLAssist feature.
        """
        pulumi.set(__self__, "inferencing_compute_binding", inferencing_compute_binding)
        pulumi.set(__self__, "model_name_prefix", model_name_prefix)
        pulumi.set(__self__, "training_compute_binding", training_compute_binding)
        if ml_assist_enabled is not None:
            pulumi.set(__self__, "ml_assist_enabled", ml_assist_enabled)
        if prelabel_accuracy_threshold is not None:
            pulumi.set(__self__, "prelabel_accuracy_threshold", prelabel_accuracy_threshold)

    @property
    @pulumi.getter(name="inferencingComputeBinding")
    def inferencing_compute_binding(self) -> pulumi.Input['ComputeBindingArgs']:
        """
        The compute designated for inferencing.
        """
        return pulumi.get(self, "inferencing_compute_binding")

    @inferencing_compute_binding.setter
    def inferencing_compute_binding(self, value: pulumi.Input['ComputeBindingArgs']):
        pulumi.set(self, "inferencing_compute_binding", value)

    @property
    @pulumi.getter(name="modelNamePrefix")
    def model_name_prefix(self) -> pulumi.Input[str]:
        """
        Name prefix to use for machine learning model. For each iteration modelName will be appended with iteration e.g.{modelName}_{i}.
        """
        return pulumi.get(self, "model_name_prefix")

    @model_name_prefix.setter
    def model_name_prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "model_name_prefix", value)

    @property
    @pulumi.getter(name="trainingComputeBinding")
    def training_compute_binding(self) -> pulumi.Input['ComputeBindingArgs']:
        """
        The compute designated for training.
        """
        return pulumi.get(self, "training_compute_binding")

    @training_compute_binding.setter
    def training_compute_binding(self, value: pulumi.Input['ComputeBindingArgs']):
        pulumi.set(self, "training_compute_binding", value)

    @property
    @pulumi.getter(name="mlAssistEnabled")
    def ml_assist_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether MLAssist feature is enabled.
        """
        return pulumi.get(self, "ml_assist_enabled")

    @ml_assist_enabled.setter
    def ml_assist_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ml_assist_enabled", value)

    @property
    @pulumi.getter(name="prelabelAccuracyThreshold")
    def prelabel_accuracy_threshold(self) -> Optional[pulumi.Input[float]]:
        """
        Prelabel accuracy threshold used in MLAssist feature.
        """
        return pulumi.get(self, "prelabel_accuracy_threshold")

    @prelabel_accuracy_threshold.setter
    def prelabel_accuracy_threshold(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "prelabel_accuracy_threshold", value)


@pulumi.input_type
class SharedPrivateLinkResourceArgs:
    def __init__(__self__, *,
                 group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_link_resource_id: Optional[pulumi.Input[str]] = None,
                 request_message: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]] = None):
        """
        :param pulumi.Input[str] group_id: The private link resource group id.
        :param pulumi.Input[str] name: Unique name of the private link.
        :param pulumi.Input[str] private_link_resource_id: The resource id that private link links to.
        :param pulumi.Input[str] request_message: Request message.
        :param pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']] status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if private_link_resource_id is not None:
            pulumi.set(__self__, "private_link_resource_id", private_link_resource_id)
        if request_message is not None:
            pulumi.set(__self__, "request_message", request_message)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The private link resource group id.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique name of the private link.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id that private link links to.
        """
        return pulumi.get(self, "private_link_resource_id")

    @private_link_resource_id.setter
    def private_link_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_resource_id", value)

    @property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[pulumi.Input[str]]:
        """
        Request message.
        """
        return pulumi.get(self, "request_message")

    @request_message.setter
    def request_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_message", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input[str]] = None):
        """
        Sku of the resource
        :param pulumi.Input[str] name: Name of the sku
        :param pulumi.Input[str] tier: Tier of the sku like Basic or Enterprise
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the sku
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[str]]:
        """
        Tier of the sku like Basic or Enterprise
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tier", value)


